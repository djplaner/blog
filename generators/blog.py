"""
FILE:   blog.py
PURPOSE: Use mkdocs-gen-file to dynamically generate various blog pages

- categories blog/category/<categoryName>.md
    List of posts in a category
- tags blog/tag/<tagName>.md
    List of posts in a tag
- monthly archives blog/YYYY/MM/index.md
    One for each.

Process
- Retrieve data all blog pages/posts
    - category[<categoryName>] - array of links to posts/pages
    - tags[<tagName>] - array of links to posts/pages
    - archives[YYYY/MM] - array of links to posts/pages
- Call different functions to generate the relative pages
"""

import re
import mkdocs_gen_files
import frontmatter
import pathlib
import yaml
import markdown
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
from pprint import pprint
from pluralizer import Pluralizer

# not sure this is needed
BLOG_FOLDER = ""
# Full path to where the markdown files are there
BLOG_HOME="/Users/davidjones/blog/docs/"
BLOG_URL="https://djon.es/blog/"
#BLOG_URL="https://localhost:8080/blog2/"

NUM_POSTS_HOME_PAGE = 20

def generateCategoryPage(categoryName, items, next, previous):
    """
    Write out a category Markdown page, including frontmatter

    Parameters
    categoryName : str name of the category
    items : list of items in the category
    next : dict containing the next page { text: <text>, url: <url> }
    previous : dict containing the previous page 
    """

#    pprint(items)

    yamlData = {
        'title': f"Items for category <em>{categoryName}</em>",
        'type': 'blog_category',
        'template': 'blog-category.html',
        'item_count': len(items),
        'previous': previous,
        'next': next
    }

    #with mkdocs_gen_files.open(f"blog/category/{categoryName}.md", "w") as f:
    with mkdocs_gen_files.open(f"{BLOG_FOLDER}category/{categoryName}.md", "w") as f:
        #print(f"#### Generating category page for {categoryName} at blog/category/{categoryName}.md")

        f.write("---\n")
        yaml.dump(yamlData, f )
        f.write("---\n")
        
#        f.write(f"""---
#type: blog_category
#template: blog-category.html
#title: Items for {categoryName}
#item_count: {len(items)}
#---
#
#""")

        #-- sort items from most recent to oldest by date
#        items = sorted(items, key=lambda x: x['yaml']['date'], reverse=True)

        for item in items:
            itemContent = generateItemContent(item)
#            f.write("""See also: [Categories](./index.md) 
#
#""")
            f.write(itemContent)

    mkdocs_gen_files.set_edit_path( f"{BLOG_FOLDER}category/{categoryName}.md", "blog.py")

def generateCategoryHomePage(categoryNames : dict):
    """
    Generate the ~/category/index.md page with a list of all the categories with links
    to the individual category pages

    params: categoryNames : dict of category names (keys) and their items (values)
    """

    categories = sorted(categoryNames.keys())
    yamlData = {
        'title': f"All post categories",
        'type': 'blog_category',
        'template': 'blog-category.html',
        'item_count': len(categories),
        'item_value': 'categories',
    }

    pluralizer = Pluralizer()

    with mkdocs_gen_files.open(f"{BLOG_FOLDER}category/index.md", "w") as f:

        f.write("---\n")
        yaml.dump(yamlData, f )
        f.write("""---

<div class="grid cards" markdown>
""")

        for name in categories:
            #-- convert date to YYYY-MM
            itemCount = len(categoryNames[name])
            itemString = f"{itemCount} {pluralizer.pluralize('items', itemCount, False)}"
            f.write(f"- :material-view-list: [{name}](./{name}.md) - {itemString}\n")
#            f.write(f"- [{name}](./{name}.html) - {len(categoryNames[name])} items\n")

        f.write("</div>\n")

    mkdocs_gen_files.set_edit_path( f"{BLOG_FOLDER}category/index.md", "blog.py")

def generateCategories(blogItems):
    """
    Generate all categories
    """

    #-- generate list "categoryNames" of all categories from blogItems ['yaml']['categories']
    categoryNames = {}
    for item in blogItems:
        #print(f"item: {item['yaml']['title']}")
        #print(f"categories: {item['yaml']['categories']}")
        if 'categories' in item['yaml']:
            for category in item['yaml']['categories']:
                #print(f"Adding {category} to categoryNames")
                if category not in categoryNames:
                    categoryNames[category] = []
                categoryNames[category].append(item)

    print(f"================ Generating {len(categoryNames)} category pages")
    categories = sorted(categoryNames.keys())
    count = 0
    numCategories = len(categories)

    #for name in categoryNames.keys():
    for name in categories:
        previous = { 'text': 'Home', 'url': '/blog/index.html' }
        next = { 'text': 'Home', 'url': '/blog/index.html' }
        if count > 0:
            next = { 
                    'text': categories[count-1],
                    'url': f"/blog/category/{categories[count-1]}.html"
                       }
        if count < numCategories - 1:
#            pprint(orderedPosts[count+1])
            previous = { 
                    'text': categories[count+1],
                    'url': f"/blog/category/{categories[count+1]}.html"
                   }
        count += 1
        generateCategoryPage(name, categoryNames[name], next, previous) 

    generateCategoryHomePage(categoryNames)

def retrieveBlogItems(blogFolder=BLOG_HOME):
    """
    Retrieve all blog posts/pages from blogFolder, skipping 
    anything that doesn't have the type: post or page
    Add a field to the item ['path'] with the path to the file

    Parameters
    blogFolder : str folder containing the blog markdown files

    Returns
    items : list of blog items ordered by date descending
    """

    # TODO how to exclude a bunch of files - before or after glob
    #files = glob.glob(f"{blogFolder}*.md")
    folder = pathlib.Path(blogFolder)
    files = folder.rglob(f"*.md")
    items = []

    #-- loop through all the files
    for file in files:
        fileContent = extractFileContent(file)
        if 'type' in fileContent['yaml']:
            if fileContent['yaml']['type'] == 'post' or fileContent['yaml']['type'] == 'page':
                ## get the relative path to the web page remove BLOG_HOME
                fileContent['path'] = str(file)
                fileContent['path'] = fileContent['path'].replace(BLOG_HOME, "")
#                print(f"file {str(file)} became {fileContent['path']}")
#                input("Press Enter to continue...")
                #-- extract path wikilink as the name of the last folder in the path
                fileContent['wikilink'] = re.sub(r"^.*?/([^/]*?)/index.md$", r"\1", str(file))
                #-- replace any \" with " in title 
                fileContent['yaml']['title'] = fileContent['yaml']['title'].replace("\\\"", "\"")
                items.append(fileContent)

    ## order items by descending date ['yaml']['date']
    items = sorted(items, key=lambda x: x['yaml']['date'], reverse=True)

    return items

def extractFileContent(path):
    """
    Given full path to DOCS_FOLDER for a markdown file, extract the file content and return it as a hash
    {
        "content": "content of file",
        "yaml": { _all yaml defined variables_ },
        "html": "content of file converted to HTML
    }
    """

    pageData = {}
    with open(path, encoding="utf-8-sig") as f:
        post = frontmatter.load(f)

    pageData['content'] = post.content
    pageData['yaml'] = post.metadata

    return pageData


#    md = markdown.Markdown(extensions=['meta'])
#    pageData = {}
#    with open(path, encoding="utf-8-sig") as f:
#        pageData["content"] = f.read()
#        html = md.convert(pageData["content"])
#        pageData['yaml'] = md.Meta
#        pageData['html'] = html
#
#        for key in pageData['yaml'].keys():
#            # if key is a list, get the first item
#            if isinstance(pageData['yaml'][key], list):
#                pageData['yaml'][key] = pageData['yaml'][key][0]
#            pageData['yaml'][key] = pageData['yaml'][key].lstrip(
#                '\"').rstrip('\"')
#
#    return pageData

def generateFeeds(blogItems):
    """
    Generate the blog's various feeds
    - blog/feed/ as an RSS
    of the 10 most recent posts

    Use feedgen (https://github.com/lkiesow/python-feedgen) to generate the RSS feed
    - get the NUM_POSTS_HOME_PAGE most recent posts from blogItems
    - generate the RSS feed and write to feed/index.md
    """
 
    mostRecent = blogItems[:NUM_POSTS_HOME_PAGE]
    mostRecent.reverse()
    

    #-- set up the feed
    fg=FeedGenerator()
    fg.id('http://lernfunk.de/media/654321')
    fg.title('Some assemblage required')
    fg.subtitle('Life, technology, and lived environments')
    fg.author( {'name':'David Jones','email':'davidthomjones@gmail.com'} )
    fg.link( href='http://djon.es/blog', rel='self' )
    fg.language('en-AU')
    fg.description('An old guy aiming to tinker with "technologies" for positive ends')
    if len(mostRecent) > 0:
        fg.updated(mostRecent[0]['yaml']['date'])

    #-- add each item to the feed
    for item in mostRecent:
        #-- convert date to RFC 2822 format
        date = item['yaml']['date'].strftime("%a, %d %b %Y %H:%M:%S +0000")
        fe = fg.add_entry()
        fe.title(title=item['yaml']['title'])
        path = f'{BLOG_URL}{item["path"].replace( "docs/", "").replace("index.md", "")}'

        #-- add post's categories
        categories = []
        if 'categories' in item['yaml']:
            for category in item['yaml']['categories']:
                categories.append({"term":category})
            fe.category(categories)

#        print(f"Adding {path} to feed")
        #input("Press Enter to continue...")
        fe.id(path)
        fe.author({'name':'David Jones','email':'davidthomjones@gmail.com'})
        fe.link(href=f"{path}", rel="alternate") # TODO is this the correct link?
#        pprint(item)
#        quit()
        fe.published(published=date)
#        fe.category(item['yaml']['categories']) # TODO category is meant to be one tag for each category

        #-- prepare the content, extract first paragraph as HTML
        content = item['content'].replace("See also: [[blog-home | Home]]", "")
        htmlContent = markdown.markdown(content)
        soup = BeautifulSoup(htmlContent, 'html.parser')
        #content = f"<p>{soup.find_all('p')[0].text}<a href=\"{path}\">...more...</a></p>"
        fe.description(htmlContent) # TODO extract first collection of content

    #-- write the feed to a file
#    with mkdocs_gen_files.open(f"{BLOG_FOLDER}feed/index.md", "w") as f:
#        f.write(str(fg.rss_str(pretty=True)))

    with mkdocs_gen_files.open(f"{BLOG_HOME}feed/feed.rss", "w") as f:
        f.write(str(fg.rss_str(pretty=True), 'utf-8'))

def extractMonths(posts):
    """
    Given a list of posts, extract the months and years - Month, YYYY - from the posts' dates

    parameters
    - posts : list of all blog posts
    returns a dict of dicts in the structure
    {
        YYYY: {
            MM: {
                count: <number of posts in month>,
                year: YYYY,
                month: MM,
                posts: [<list of posts>]
            }
    }
    """

    months = {}
    for item in posts:
        #-- convert date to YYYY-MM
        month = item['yaml']['date'].strftime("%B")
        year = item['yaml']['date'].strftime("%Y")

        if year not in months:
            months[year] = {} 
        if month not in months[year]:
            months[year][month] =  {
                'count': 0,
                'year': year,
                'month': month,
                'posts': []
            }
        months[year][month]['count'] += 1
        months[year][month]['posts'].append(item)

    #-- sort the months in reverse order
    #months = sorted(months, reverse=True)
    monthPosts = []
    for year in months.keys():
        for month in months[year].keys():
            monthPosts.append(months[year][month])

    return monthPosts

def splitArchivesByYear(archives):
    """
    Given a list of dicts sorted by date with values
        { 'month': 'January', 'year': 2023, 'count': 3, 'posts': [<list of posts>] }
    Return a dict of dicts organising the archives by year
    {
        YYYY: {
            MM: {
                count: <number of posts in month>,
                year: YYYY,
                month: MM,
                posts: [<list of posts>]
            }
    }

    params: archives : list of dicts containing the months and years
    returns a dict of dicts in the structure
    """

    yearArchives = {}
    for item in archives:
        month = item['month']
        year = item['year']

        if year not in yearArchives:
            yearArchives[year] = []
        yearArchives[year].append(item)

    return yearArchives

def generateArchivesHome(archives):
    """
    Generate the ~/archives/index.md page with a list of all the months with links
    The list is divided up by year, with cards for the year's months following.

    params: archives : dict of months (keys) and their items (values) - sorted by date
        { 'month': 'January', 'year': 2023, 'count': 3, 'posts': [<list of posts>] }
    """

    yamlData = {
        'title': f"Monthly archives of posts",
        'type': 'blog_category',
        'template': 'blog-category.html',
        'item_count': len(archives),
        'item_value': 'months'
    }

    yearArchives = splitArchivesByYear(archives)

    pluralizer = Pluralizer()

    with mkdocs_gen_files.open(f"{BLOG_FOLDER}archives/index.md", "w") as f:

        f.write("---\n")
        yaml.dump(yamlData, f )
        f.write("""---

""")

        #-- for each year, add a card for each month from that year with posts
        for year in yearArchives.keys():
            f.write(f"## {year}\n")
            f.write('<div class="grid cards" markdown>')
            for item in yearArchives[year]:
                f.write(f"- :material-view-list: [{item['month']} {item['year']}](./{item['month']}-{item['year']}.md) - {item['count']} {pluralizer.pluralize('items', item['count'], False)}\n")

            f.write("</div>\n")

    mkdocs_gen_files.set_edit_path( f"{BLOG_FOLDER}archives/index.md", "blog.py")


def generateArchives(archives):
    """
    Generate the month archive pages at 
        blog/Archives/<month>-<year>.md
    Each one to contain excepts of the relevant 

    parameters
    - archives : list of dicts containing the months and years
        { 'month': 'January', 'year': 2023, 'count': 3, 'posts': [<list of posts>] }
    """

    numItems = len(archives)
    count = 0

    for item in archives:
        #-- convert date to YYYY-MM
        path = f"{BLOG_FOLDER}archives/{item['month']}-{item['year']}.md"

        #-- calculate the next and previous months
        # - if this is the first month, set previous to Home
        # - if this is the last month, set next to Home
        previous = { 'text': 'Home', 'url': '/blog/index.html' }
        next = { 'text': 'Home', 'url': '/blog/index.html' }
        if count > 0:
            next = { 
                        'text': f'{archives[count-1]["month"]} {archives[count-1]["year"]}', 
                        'url': f"/blog/archives/{archives[count-1]['month']}-{archives[count-1]['year']}.html" 
                       }
        if count < numItems - 1:
            previous = { 
                    'text': f'{archives[count+1]["month"]} {archives[count+1]["year"]}',
                    'url': f"/blog/archives/{archives[count+1]['month']}-{archives[count+1]['year']}.html" 
                   }

        count += 1

        with mkdocs_gen_files.open(path, "w") as f:
            f.write(f"""---
title: Archives for {item['month']} {item['year']}
type: blog_archive
template: blog-category.html
item_count: {item['count']}
next:
    text: {next['text']}
    url: {next['url']}
previous:
    text: {previous['text']}
    url: {previous['url']}
---

See also: [Archives](./index.md)

""")

            for post in item['posts']:
                content = generateItemContent(post)
                f.write(content)

    #mkdocs_gen_files.set_edit_path( f"{BLOG_FOLDER}index.md", "blog.py")
        mkdocs_gen_files.set_edit_path( path, "blog.py")

    generateArchivesHome(archives)


def generateItemContent(item, homePage=False):
    """
    Given a blog item generate the HTML content to display that item with the first para of blog content

    parameters
    - item : dict containing the blog item
    - homePage : bool if True, generate the content for the home page

    returns
    - itemContent : str containing the HTML content for the item
    """

    itemContent = ""

    relPath = "../"
    if homePage:
        relPath = "./"

    path = item['path'].replace( "docs/", "").replace("index.md", "")
    content = item['content'].replace("See also: [[blog-home | Home]]", "")
    htmlContent = markdown.markdown(content)
    soup = BeautifulSoup(htmlContent, 'html.parser')

    paras = soup.find_all('p')
    text = ""
    if len(paras) > 0:
        text = paras[0].text

    content = f"<p>{text}<a href=\"../{path}\">...more...</a></p>"

    #-- convert date to DD Mon YYYY
    date = item['yaml']['date'].strftime("%d %b %Y")

    coverImage= ""
    if 'coverImage' in item['yaml']:
        coverImage = f"""
    <div class="cover-image">
        <img src="{relPath}{path}images/{ item['yaml']['coverImage'] }" alt="{ item['yaml']['title'] }" width="100%" height="auto">
    </div>
"""

    categories = ""
    if 'categories' in item['yaml']:
        categories = " in: "
        for category in item['yaml']['categories']:
            categories += f'<a href="/blog/category/{category}.html">{category}</a>, '
        ##-- remove the last comma
        categories = categories[:-2]

    itemContent = f"""
<div class="blog-item">
    {coverImage}
  <div class="blog-item-title"><a href="{relPath}{path}">{item['yaml']['title']}</a></div>
  <div class="blog-item-date">📅 {date} {categories}</div>
  <div class="blog-item-content-preview">
    {content}
  </div>
</div>
                    """

    return itemContent
    
def generateHome(posts):
    """
    Write the blog home page by adding 20 of the most recent posts
    Maybe eventually add an intro from the frontmatter.

    - read the home page file ~/docs/index.md
    - throw away the content it is replaced
    - replace the archives frontmatter with the current list of months
    - add the X most recent posts

    parameters
    - posts : list of all blog posts
    """

    fileContent = extractFileContent(f"{BLOG_HOME}index.md")

    #-- replace the archives frontmatter with the current list of months
    archives = extractMonths(posts)
    fileContent['yaml']['archives'] = archives
    description = ""
    if "description" in fileContent['yaml']:
        description = fileContent['yaml']['description']

    generateArchives(archives)

    with mkdocs_gen_files.open(f"{BLOG_FOLDER}index.md", "w") as f:
        #-- write the frontmatter
        f.write(f"""---
{yaml.dump(fileContent['yaml'])}
---

<p>{description}</p>

""")

        for item in posts[:NUM_POSTS_HOME_PAGE]: 
            itemContent = generateItemContent(item, True)
            f.write(itemContent)

    mkdocs_gen_files.set_edit_path( f"{BLOG_FOLDER}index.md", "blog.py")


def writeBlogStats(blogItems):
    """
    Write out the blog stats to a file in the docs folder
    """

    STATS_FILE = f"{BLOG_HOME}stats.yaml"

    #-- get the number of posts
    numPosts = len(list(filter(lambda x: x['yaml']['type'] == 'post', blogItems)))
    numPages = len(list(filter(lambda x: x['yaml']['type'] == 'page', blogItems)))

    #-- get the first and last post dates
    firstPost = "n/a"
    lastPost = "n/a"
    if numPosts!=0:
        firstPost = blogItems[-1]['yaml']['date'].strftime("%Y-%m-%dT%H:%M:%S.%f%z")
        lastPost = blogItems[0]['yaml']['date'].strftime("%Y-%m-%dT%H:%M:%S.%f%z")

    stats = {
        'numPosts': numPosts,
        'numPages': numPages,
        'firstPost': str(firstPost),
        'lastPost': str(lastPost)
    }

    with open(STATS_FILE, 'w') as stream:
        yaml.dump(stats, stream)
    

def generator():
    """
    Main harness for wood duck generator
    """

    # TODO implement
    blogItems = retrieveBlogItems()
    #-- create list pages containing all blog items with type==page
    pages = map(lambda x: x['yaml']['title'], filter(lambda x: x['yaml']['type'] == 'page', blogItems))
    posts = map(lambda x: x['yaml']['title'], filter(lambda x: x['yaml']['type'] == 'post', blogItems))

    # Generate category pages 
    generateCategories( blogItems)

    # Generate RSS feed
    generateFeeds(blogItems)

    # Generate home page
    generateHome(blogItems)

    writeBlogStats(blogItems)


generator()
