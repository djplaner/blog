---
title: Tweaking Moodle book search
date: 2015-12-15 16:43:30+10:00
categories: ['thesis']
tags: ['moodleopenbook']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Finishing tweaks to Moodle book search block | The Weblog of (a) David Jones
      author_email: null
      author_ip: 192.0.113.137
      author_url: https://davidtjones.wordpress.com/2016/01/17/finishing-tweaks-to-moodle-book-search-block/
      content: '[&#8230;] previous post recorded some early exploration of what tweaks
        might be necessary to be made to the Moodle book [&#8230;]'
      date: '2016-01-17 14:31:20'
      date_gmt: '2016-01-17 04:31:20'
      id: '1463'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
A couple of weeks ago I gave [a presentation](/blog2/2015/11/30/opening-up-and-enhancing-moodle-books-with-github-epub-etc/) showing off some work from the [Moodle open Book project](/blog2/the-moodle-open-book-module-project/). The middle of the presentation was a live demonstration of the Moodle Book and various features. At one point in the presentation members of the audience (including a number of academics who used the Book module in their Moodle sites) gave an audible gasp. This occurred when I showed off [the search block](https://github.com/stronk7/moodle-block_search_books) for the Book module. A tool that allows the user to search the contents of all the books in a Moodle course. The gasp indicated just how much teachers and students desire this feature. A feature I've been [calling out](/blog2/2013/03/07/the-absence-of-a-search-function-my-current-big-problem-with-a-moodle-installation/) for quite some time.

The [GitHub repository](https://github.com/stronk7/moodle-block_search_books) has been around for 2 years. So why isn't this block more widely available in Moodle sites? There's a security flaw in the code and is somewhat unfinished.

The [Moodle SQL injection page](https://docs.moodle.org/dev/Security:SQL_injection) outlines at least two broad steps that Moodle code should take to prevent a nefarious person from gaining inappropriate access. These are

1. Using appropriate parameter cleaning mechanisms on data coming from outside of Moodle (e.g. search terms entered into a form).
2. Using provided Moodle functions to retrieve data from the database (e.g. search the database for content in a Moodle book)

The Moodle book search block currently meets #1, but fails #2.

The following aims to explore and hopefully remedy this problem.

Current status is that some initial changes have been made to a local version of the block that borrows lessons from the forum search.  Need to spend a bit more time on this, but it's on the way.

### The form

The form for the block currently passes the following information.

Added by the block code

- **courseid**; and
- **page**.

The user is able to enter data into: **bsquery**

### The processing

Apart from standard processing the main searching is done in a function named **search** which

- Deals with some apparent differences between flavours of SQL between databases. Seeming to point to a problem in how it's engaging with databases. **DOES FORUM SEARCH DO THIS**
- Focuses attention on books the user is allowed to read.
- Generates strings containing SQL statement See below for the format.
    - Supports + and -
- Uses get\_records\_sql to retrieve any matches Not using placeholders, which is a problem.

A search for "copyright" generates a SQL statement similar to the following

```
SELECT DISTINCT bc.* FROM mdl_book_chapters bc, mdl_book b
        WHERE b.course = 12 AND b.id IN (..long list of book ids)
        AND bc.bookid = b.id AND bc.hidden = 0 AND
        (( bc.title ILIKE '%copyright%' ) OR
         ( bc.content ILIKE '%copyright%' ) )
        ORDER BY bc.bookid, bc.pagenum
```

Each word added to the search phrase adds options to the "ilikes"

( bc.title ILIKE '%copyright%' AND bc.title ILIKE '%creative%' AND bc.title ILIKE '%commons%' )

Questions include

- Can get\_records\_sql be replaced with get\_records
- Can the database dependency be removed
- Can placeholders be used

### Comparison with forum search

The forum search is an accepted part of Moodle.  Checking how it works might provide some inspiration to copy.

Has a slight be compartmentalised structure

\[code lang="php"\]   $forums = forum\_get\_readable\_forums($USER-&gt;id, $courseid);\[/code\]

Has to deal with a lot more complexity than the book search.

Uses $DB->get\_in\_or\_equal

Makes use of a method search\_generate\_SQL to do as the name suggests.  This is something that should be worked into the Book search block.

Initial testing and that is working.  Dig a bit and it makes sense.  Also seems to tidy up the code a fair bit.