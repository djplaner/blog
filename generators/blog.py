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
import markdown
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
from pprint import pprint

# not sure this is needed
BLOG_FOLDER = ""
# Full path to where the markdown files are there
BLOG_HOME="/Users/davidjones/blog/docs/"
BLOG_URL="https://djon.es/blog2/"


def generateCategoryPage(categoryName, items):
    """
    """

#    pprint(items)

    #with mkdocs_gen_files.open(f"blog/category/{categoryName}.md", "w") as f:
    with mkdocs_gen_files.open(f"{BLOG_FOLDER}category/{categoryName}.md", "w") as f:
        #print(f"#### Generating category page for {categoryName} at blog/category/{categoryName}.md")
        f.write(f"""---
type: blog_category
template: blog-category.html
category: {categoryName}
item_count: {len(items)}
---

# Items for category {categoryName}

See also: [[blog-home]], [[posts]], [[pages]]

""")

        #-- sort items from most recent to oldest by date
#        items = sorted(items, key=lambda x: x['yaml']['date'], reverse=True)

        for item in items:
            path = item['path'].replace( "docs/", "").replace("index.md", "index.html")
            #-- remove " See also: [.*) from content
#            content = re.sub( r".*See also: ) ", "", item['content'] )
            content = item['content'].replace("See also: [[blog-home | Home]]", "")
            htmlContent = markdown.markdown(content)
            soup = BeautifulSoup(htmlContent, 'html.parser')

            content = f"<p>{soup.find_all('p')[0].text}<a href=\"../{path}\">...more...</a></p>"

#            if categoryName == "thesis":
#                print(f"*******\n{item['content'][:300]}\n")
#                print(f"*******\n{content[:300]}\n")
#                print(f"*******\n{htmlContent}\n")
#                input("Press Enter to continue...")

            
            #-- convert date to DD Mon YYYY
            date = item['yaml']['date'].strftime("%d %b %Y")
             
            f.write( f"""
<div class="blog-item">
  <div class="blog-item-title"><a href="../{path}">{item['yaml']['title']}</a></div>
  <div class="blog-item-date">📅 {date}</div>
  <div class="blog-item-content-preview">
    {content}
  </div>
</div>
                    """)
#            f.write( f"- [{item['yaml']['title']}](../{path})\n\n")
#            f.write( f"  {str(item['yaml']['date'])}\n\n")
            #f.write(f"- [[{item['wikilink']}/index.md]]\n")
    mkdocs_gen_files.set_edit_path( f"{BLOG_FOLDER}category/{categoryName}.md", "blog.py")

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

    for name in categoryNames.keys():
        generateCategoryPage(name, categoryNames[name]) 

def retrieveBlogItems(blogFolder=BLOG_FOLDER):
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
                fileContent['path'] = str(file)
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
    - get the 10 most recent posts from blogItems
    - generate the RSS feed and write to feed/index.md
    """
 
    mostRecent = blogItems[:10]

    #-- set up the feed
    fg=FeedGenerator()
    fg.id('http://lernfunk.de/media/654321')
    fg.title('Some assemblage required')
    fg.author( {'name':'David Jones','email':'davidthomjones@gmail.com'} )
    fg.link( href='http://djon.es/blog', rel='self' )
    fg.language('en-AU')
    fg.description('Some assemblage required - a blog about learning, teaching and technology')

    #-- add each item to the feed
    for item in mostRecent:
        #-- convert date to RFC 2822 format
        date = item['yaml']['date'].strftime("%a, %d %b %Y %H:%M:%S +0000")
        fe = fg.add_entry()
        fe.title(item['yaml']['title'])
        path = f'{BLOG_URL}{item["path"].replace( "docs/", "").replace("index.md", "")}'
#        print(f"Adding {path} to feed")
        #input("Press Enter to continue...")
        fe.id(path)
        fe.title(item['yaml']['title'])
#        fe.link(href=f"{BLOG_URL}feed/") # TODO is this the correct link?
#        fe.pubDate(date)
#        fe.category(item['yaml']['categories']) # TODO category is meant to be one tag for each category

        #-- prepare the content, extract first paragraph as HTML
        content = item['content'].replace("See also: [[blog-home | Home]]", "")
        htmlContent = markdown.markdown(content)
        soup = BeautifulSoup(htmlContent, 'html.parser')
        content = f"<p>{soup.find_all('p')[0].text}<a href=\"{path}\">...more...</a></p>"
        fe.description(content) # TODO extract first collection of content

    #-- write the feed to a file
#    with mkdocs_gen_files.open(f"{BLOG_FOLDER}feed/index.md", "w") as f:
#        f.write(str(fg.rss_str(pretty=True)))

    with mkdocs_gen_files.open(f"{BLOG_HOME}feed/feed.rss", "w") as f:
        f.write(str(fg.rss_str(pretty=True), 'utf-8'))


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


generator()
