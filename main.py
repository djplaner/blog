"""
FILE: main.py
PURPOSE: Define macros using mkdocs-macros-plugin
"""

import yaml
import datetime

def getBlogStats( ):
    """
    Display stats about the blog
    - # of posts
    - # of categories
    - date range - first and last post

    Try reading the "stats.yaml" file in docs - created by mkdocs-gen-files
    """

    STATS_FILE = "/Users/davidjones/blog/docs/stats.yaml"

    data = {}

#    return "hello world"
    with open(STATS_FILE, 'r') as stream:
        data = yaml.safe_load(stream)

        #date = item['yaml']['date'].strftime("%a, %d %b %Y %H:%M:%S +0000")
    ## convert firstPost to DD MMM YYYY
    for day in ['firstPost', 'lastPost']:
        #-- convert data[day] to datetime
        if data[day]!="n/a":
            dateStr = datetime.datetime.strptime(data[day], "%Y-%m-%dT%H:%M:%S.%f%z")
            data[day] = dateStr.strftime("%A, %-d %B %Y %H:%M:%S")

    output = ""
    output = writeBasicStats(data)
    output += writePostsPerYear(data)
    output += writeInternalLinks(data)
    output += writeExternalLinks(data)

    return output

def writeBasicStats(data):
    return f"""

=== "Basic statistics"

    | Statistic | Value |
    | ---- | ----- |
    | # posts | {data['numPosts']} | 
    | # pages | {data['numPages']} |
    | First post | {data['firstPost']} |
    | Last post | {data['lastPost']} |

"""

def writePostsPerYear(data):

    output = f"""

=== "Posts per year"

    | Year | # Posts |
    | ---- | ------- |
"""

    for year, count in data['postsPerYear'].items():
        output += f"    | {year} | {count} |\n"
        
    return output

def writeInternalLinks(data):
    output = f"""
    
=== "Top 20 Internal Links"

    | Link | Count |
    | ---- | ------- |
"""

    for internalLink in data['internalLinks'][:20]:
        output += f"    | [{internalLink['link']}]({internalLink['link']}) | {internalLink['count']} |\n"

    return output

def writeExternalLinks(data):
    output = f"""
=== "Top 20 External Links"
    | Link | Count |
    | ---- | ------- |
"""

    for externalLink in data['externalLinks'][:20]:
        output += f"    | {externalLink['link']} | {externalLink['count']} |\n"

    return output

def define_env(env):
    """
    Define the macros for use in markdown files
    """

    @env.macro
    def blogStats( ):
        """
        """
        return getBlogStats()

