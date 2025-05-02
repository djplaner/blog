---
title: bim2 - student and marker fixes
date: 2012-03-31 22:42:04+10:00
categories: ['bim2']
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: Stephen Downes
      author_email: stephen@downes.ca
      author_ip: 156.34.22.90
      author_url: http://downess.wordpress.com
      content: 'OK, while I''m admitting ignorance today: Could you tell your readers
        what Bim is? I assume by context its some sort of software. But what is it? You''ve
        been posting on it for years, and yet you''ve never told your readers (to myt
        knowledge) what it is, what B-I-M stand for (if anything), and what it''s used
        for. Thanks.'
      date: '2012-04-02 10:26:51'
      date_gmt: '2012-04-02 00:26:51'
      id: '300'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: David Jones
      author_email: davidthomjones@gmail.com
      author_ip: 139.86.2.14
      author_url: https://djon.es/blog/
      content: ":) I was always a tad worried about using the blog as a development diary,\
        \ in large part because of this.\n\nWhich is why every now and then I do throw\
        \ in some background.\n\nThe bim2 post prior to this one started with\n<blockquote>So\
        \ it appears that bim2.0 is increasingly needed (if you don\u2019t know what bim\
        \ is, <a href=\"https://djon.es/blog/research/bam-blog-aggregation-management/\"\
        \ rel=\"nofollow\">check this out</a>). </blockquote>\n\nThe link goes to the\
        \ <a href=\"https://djon.es/blog/research/bam-blog-aggregation-management/\" rel=\"\
        nofollow\">BIM page</a> on my blog.\n\nBIM has some vague connection with gRSShopper\
        \ in that it is an aggregator of feeds. It is intended to be used within a Moodle\
        \ course, typically as an assignment where students are responding to activities/tasks\
        \ on their individual blogs.  It helps teaching staff manage/mark/track student\
        \ posts.\n\nBIM started life as BAM - Blog Aggregation Management - in the home-grown\
        \ \"LMS\" I worked on.\n\nIt became BIM when I ported the idea to Moodle.  BIM\
        \ = BAM Into Moodle"
      date: '2012-04-02 10:36:19'
      date_gmt: '2012-04-02 00:36:19'
      id: '301'
      parent: '300'
      type: comment
      user_id: '1'
    - approved: '1'
      author: David Jones
      author_email: davidthomjones@gmail.com
      author_ip: 139.86.2.14
      author_url: https://djon.es/blog/
      content: And I've just noticed that this blog theme doesn't do a great job of making
        links all that obvious.
      date: '2012-04-02 10:36:58'
      date_gmt: '2012-04-02 00:36:58'
      id: '302'
      parent: '0'
      type: comment
      user_id: '1'
    - approved: '1'
      author: Stephen Downes
      author_email: stephen@downes.ca
      author_ip: 156.34.22.90
      author_url: http://downess.wordpress.com
      content: Thanks. Appreciated. The Bim posts are now doubly useful to me.
      date: '2012-04-02 20:28:40'
      date_gmt: '2012-04-02 10:28:40'
      id: '303'
      parent: '0'
      type: comment
      user_id: '0'
    
pingbacks:
    - approved: '1'
      author: bim2 &#8211; Marker interface &laquo; The Weblog of (a) David Jones
      author_email: null
      author_ip: 216.151.210.44
      author_url: https://djon.es/blog/2012/04/03/bim2-marker-interface/
      content: '[...] the following, I&#8217;m continuing work on the marker interface
        from prior work. Work to do [...]'
      date: '2012-04-03 22:51:44'
      date_gmt: '2012-04-03 12:51:44'
      id: '304'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
Some more work on bim2, carrying on from [last night](/blog2/2012/03/30/bim2-status-check-and-whats-next/). Aim here is to attack some of these tasks:

- Fix problem with mirroring of student feeds.
- Double check the marker screens.

### Mirroring of student feeds

Last night I proposed three possible causes

1. The caching/operation of the Moodle 2 version of Simplepie and bim.
2. Left over database entries not cleaned up appropriately during testing.
3. Errors crept into the mirroring code due to Moodle 2 database API changes.

Is bim2 currently using the Moodle2 version of the SimplePie library for mirroring, rss parsing etc.

\[sourcecode language="language="php"\] require\_once( $CFG->libdir.'/simplepie/moodle\_simplepie.php' ); \[/sourcecode\]

Check.

Let's try a brand new student. Yes, same problem. Is not mirroring the feed properly. Keeps adding all the new stuff. Is inserting the same entry into the database each time, perhaps the problem is with the bim2 code.

So time to look at lib/bim\_rss.php. Basic process is

- Create details\_link hash with key being link to posts in the dbase. - BROKEN  
    Is giving an empty hash when there should be 6 entries....bim\_get\_marking\_details is broken. Yep, hasn't been moved across to the Moodle 2 dbase API.
- Loop through items in the feed
    - if not already in the details\_link hash
        - Prepare for entry, including checking if it's an answer to a question.
        - insert it into the dbase

### Minor display problems

In fixing this, there are some minor display problems to fix. This is also probably a porting issue.

- "showquestions" - apparently meant to be details about questions, rather than a link to a label.  
    "showquestions" is a link to the page where students can view the questions they have to answer. However, it should have some descriptive text here. It appears that [link\_to\_popup\_window](http://docs.moodle.org/dev/Deprecated_functions_in_2.0#link_to_popup_window_.280.29) is deprecated in Moodle 2.
    
    Not sure why this was a popup. Make it a normal window and move on...Oh joy, the language files are cached. Need to turn that off.
    
- Links after "All posts" heading - descriptive text is a link  
    Being caused by an unclosed anchor tag. Where is that shown? Ahh, lib/locallib.php - fixed.
- Help buttons "TO DO" - all of them are to do.  
    Another conversion not fixed. All those text files need to be moved into the lang file. Done.

That last task also helped test the various transitions that a post can go through: unallocated, allocated/submitted, marked, suspended and released.

At this stage, the student part of bim2 is a go.

### implode

The problem with get\_marking\_details above was caused by unfinished porting of how SQL " in " statements are handled. The new "get\_in\_or\_equal" method needs to be used.

This needs to be fixed before moving on. Need to search for implode.

**Note:** Will need to keep an eye on bim\_get\_all\_marker\_stats as it needs to be closely tested.

### Marker "screens"

A marker can do the following

- View student details Needed to fix the help popups. Done.
    - View various details about the students - WORKS
    - Download OPML file for their students  
        Error in SQL. This is all done in marker/generateOpml.php. Seems the problem is in bim\_get\_markers\_students. Actually the userid isn't being passed in. that's fixed.
        
        Another problem. It's not actually returning anything for this marker. Actually, a range of problems from the bim1 code. This probably never worked.
        
        It does now.
        
    - Register a blog for a student
    - Send an email to all unregistered students - WORKS
- Mark posts
    - View an overview of marking progress
    - Mark a particular post - which includes a range of changes

Will leave this for now.

Next time I need to continue going through the marker interface.