---
title: Analysing Moodle community forum discussions about the Moodle book module
date: 2015-06-09 11:52:25+10:00
categories: ['bad', 'elearning', 'moodle', 'moodleopenbook']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: 'Exploring &#8220;post adoptive usage&#8221; of the #moodle Book module
        &#8211; a draft proposal | The Weblog of (a) David Jones'
      author_email: null
      author_ip: 192.0.99.237
      author_url: https://davidtjones.wordpress.com/2015/11/06/exploring-post-adoptive-usage-of-the-moodle-book-module-a-draft-proposal/
      content: '[&#8230;] Some of the Moodle features have discussion forums where people
        using the feature can discuss. Content analysis of the relevant forum might reveal
        patterns. The actual source code for Moodle as well as plans and [&#8230;]'
      date: '2015-11-06 15:39:51'
      date_gmt: '2015-11-06 05:39:51'
      id: '1317'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
As part of the ["Moodle open book" project](/blog2/the-moodle-open-book-module-project/) I'm hoping to increase my knowledge of what the Moodle community has already discussed about the [Book module](https://docs.moodle.org/28/en/Book_module). The following is a summary of the process I'm using to analyse those discussions.

Not finished, but the story so far. Just over 2400 posts extracted from Moodle community forums that appear to mention "Book module". About 250 posts (very roughly) coded so far. The following is a very early summary of the features discussed in those posts is

- 43 - navigation and interface
- 33 - export and import
- 15 - printing
- 13 - integrating activities (mostly quizzes) into the midst of the book.
- 6 - page visibility
- 3 - version control

Though a little interesting, I wouldn't read to much into those figures yet. There are some more statistics on the 2400+ posts below.

### Obtain the data

The process for obtaining the data was

1. Global search for "book module".
    
    Use the "Search forum" functionality in the ["Moodle in English" community](https://moodle.org/course/view.php?id=5) to search for posts that mentioned "book module". This gave 144 pages of forum posts. These were than saved to my laptop.
    
2. Get all the posts from the Book module forum.
    
    Got a copy of all the forum posts to [Book module forum](https://moodle.org/mod/forum/view.php?f=466)
    

### Parse the data

Need to write a Perl script that will extract that information from the HTML files.

The potentially useful data in this set includes

- Post
    - the subject line for the post (parsed)
    - body of the post (parsed)
    - date string when posted (parsed)
    
- Forum
    - link (parsed)
    - name (parsed)
- Author
    - User id
    - Author name (parsed)
    - link to their profile (parsed)

### Stick it in (a) database table(s)

Next step is to have the script stick it all in a database table to ensure that there are no duplicates. moodle\_book\_forum\_posts

That appears to be working. Now to try and get it all the forum posts inserted.

Done, some quick stats from SQL

1. 2442 forum posts
2. 870 authors
3. 146, 71, 41, 41, 41, 41, 36 - the number of posts (in descending order) by the most prolific authors.
4. the posts are from 40 forums. As you would expect, most in the book forum.
    - Book - 1774 posts
    - General help - 143
    - General developer - 86
    - Themes - 46
    - General plugins - 38
    - Gradebook - 37The presence of the gradebook forum potentially points to the biggest flaw with the data so far. i.e. search for "book module" my return posts that include "gradebook module" or similar. This will get ironed out in the later analysis.

### Content analysis - into NVivo

The plan is to use NVivo to do a content analysis on the posts. The aim is to to identify the nature of the posts about the Book module. i.e. are the posts how to use, bug reports, feature requests etc. As part of that what types of features have been requested and when.

The plan was to import the data from the database, but apparently the Mac version of NVivo cannot import data from a database. Meaning I need to go via a spreadsheet/CSV file.

Sadly, Nvivo seems a little constrained. e.g. you can't add to or change a dataset.

But at least Perl and [WriteExcel](http://search.cpan.org/~jmcnamara/Spreadsheet-WriteExcel-2.40/lib/Spreadsheet/WriteExcel.pm) provide some flexibility.

Of course, it appears that I have to load the Excel file produced by Perl into Excel and then save it from Excel before NVivo will import it properly.

### Initial analysis with NVivo

First run through I think I'll use these nodes

- Book or NotBook - to indicate whether a post is related to the book module.
- NewFeature - indicate something to do with new feature
    - Request - asking for a new feature
    - Announce - Announce a new feature
- Bug - indicate a bug has been identified
    - Request - asking for help with a bug
    - Announce - announcing a fix for a bug
- Help - getting help with using book
    - Request - asking for help
    - Announce - answering please for help

Each of the book related nodes will have nodes indicating what is being helped with e.g. export, import, navigation, authoring, permissions, display. Wonder if there's a list of these already.

It's taking a while to do this coding. Pity about the absence of decent keyboard shortcuts in NVivo.

Will probably need to revisit these categories. Such as there are a few categories where the distinction is questionable - e.g. export/print, bug/new feature