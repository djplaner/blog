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
        dateStr = datetime.datetime.strptime(data[day], "%Y-%m-%d %H:%M:%S%z")
        data[day] = dateStr.strftime("%A, %-d %B %Y %H:%M:%S")
    output = f"""
| Statistic | Value |
| ---- | ----- |
| # posts | {data['numPosts']} | 
| # pages | {data['numPages']} |
| First post | {data['firstPost']} |
| Last post | {data['lastPost']} |
"""
        
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

