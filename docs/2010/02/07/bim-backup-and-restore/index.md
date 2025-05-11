---
categories:
- bim
date: 2010-02-07 11:53:36+10:00
next:
  text: BIM - talking to the gradebook
  url: /blog2/2010/02/07/bim-talking-to-the-gradebook/
previous:
  text: 'Challenges in developing innovative pedagogy in blended learning: The case
    of BIM'
  url: /blog2/2010/02/06/challenges-in-developing-innovative-pedagogy-in-blended-learning-the-case-of-bim/
title: BIM - backup and restore
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: 'BIM &#8211; Tidy up #4 &#8211; Getting ready for user testing &laquo; The
        Weblog of (a) David Jones'
      author_email: null
      author_ip: 74.200.245.188
      author_url: https://djon.es/blog/2010/02/04/bim-tidy-up-4-getting-ready-for-user-testing/
      content: '[...] Backing BIMs up/restoring &#8211; Leave till later [...]'
      date: '2010-02-07 17:47:45'
      date_gmt: '2010-02-07 07:47:45'
      id: '2927'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: Fixing BIM&#8217;s back up and restore &laquo; The Weblog of (a) David Jones
      author_email: null
      author_ip: 74.200.247.228
      author_url: https://djon.es/blog/2010/05/27/fixing-bims-back-up-and-restore/
      content: '[...] BIM&#8217;s back up and&nbsp;restore  The following outlines steps
        to continue work on BIM&#8217;s backup and restore functionality. As per this
        issue the user part of the back up has [...]'
      date: '2010-05-27 15:44:25'
      date_gmt: '2010-05-27 05:44:25'
      id: '2928'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: Backup for BIM 2.0 &laquo; The Weblog of (a) David Jones
      author_email: null
      author_ip: 66.155.9.113
      author_url: https://djon.es/blog/2012/12/29/backup-for-bim-2-0/
      content: '[...] following is based on this 2010 post documenting the development
        work on the backup process for BIM 1.0. With some extra work based on [...]'
      date: '2012-12-29 17:46:12'
      date_gmt: '2012-12-29 07:46:12'
      id: '2929'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
Just about done with development of version 1.0 of the module. A couple of important, but hopefully straight forward tasks to do. One of these is adding the ability for BIM activities to be backed up and restored. That's the purpose of this post. The plan is to find out how it is meant to work and plan how it can be done for BIM.

At this stage, I've worked out the basics of how this works. I think. I haven't implemented it, so new wrinkles may appear. Current status is to defer work on this and focus on that functionality required for immediate use. This can be added in a little while.

### How it works

The Module extension development book I've been using is pretty poor in its treatment of backups/restores. Some existing Moodle documentation includes:

- [a start of some developer docs.](http://docs.moodle.org/en/Development:Backup)
[](http://docs.moodle.org/en/Development:Backup)- [](http://docs.moodle.org/en/Development:Backup)[the user forum with links to faq](http://moodle.org/mod/forum/view.php?f=128)

### Some basic stuff gleaned from the code of some activities - incomplete

- Moodle looks for files backuplib.php and restorelib.php
- Data is saved in a simple XML file format.
- backup functions (from core choice module) **QUESTION** Are these specific to choice or common?
    - choice\_backup\_mods($bf,$preferences)  
        Standard, purpose is to backup everything for this module
    - choice\_backup\_one\_mod($bf,$preferences,$choice)  
        Standard, purpose is to backup just a single instance of the module based on the $choice parameter as the id
    - backup\_choice\_answers ($bf,$preferences,$choice)  
        Standard, previous function backs up the instance data and then this one saves some contents
    - backup\_choice\_options ($bf,$preferences,$choice)
    - choice\_check\_backup\_mods($course,$user\_data=false,$backup\_unique\_code,$instances=null)
    - choice\_check\_backup\_mods\_instances($instance,$backup\_unique\_code)
    - choice\_encode\_content\_links ($content,$preferences)
    - choice\_ids ($course)
    - choice\_answer\_ids\_by\_course ($course)
    - choice\_answer\_ids\_by\_instance ($instanceid)
- Need to save
    - instance data

### An attempt to describe the process

- Moodle module backup works be essentially creating a XML file that contains all the information in the database tables associated with the module.
- It assumes a hierarchical relationships in the data.
    - All instances of the module
        - Data specific to an instance. (non-hierarchical)
        - All hierarchical data for an instance (e.g. student feeds for a bim)
            - Data specific to a single instance (e.g. feed\_url)
            - All hierarchical data (e.g. posts made to the feed)
                - Data specific to a single instance (e.g. content of post)
                - All hierarhical data (...and so on)
- The nested/hierarchical relationship with the XML produced is mirrored in the functions that exist. The first one is **_MODULENAME_\_backup\_mods($bf,$preferences)** which calls the next level down...
- Two other required functions with names containing **...\_check\_..** are used to generate some options that allow the user doing the backup to choose what to backup.
- Another function **_MODULENAME_\_encode\_content\_links** is a bit of a mystery. Might be to "support inter-activities linking" or "recode links to ensure they work when reimported" - NOT SURE.  
    I'm assuming that this is needed because as the database ids are created by a restore, they are likely to be different to the original data. If they do change, then it will be necessary to modify some other links. There are two types I could think of:
    
    1. links between database tables
    2. links in URLs with fields in the tables.
    
    The backup stuff for chat, seems to indicate the latter
    
- The functions doing the save are meant to write XML by using **fwrite** and XML functions like "start\_tag" "end\_tag" full\_tag".

### The bim hierarchy

- bim
    - Instance data: id course name intro introformat timecreated timemodified register\_feed mirror\_feed change\_feed grade\_feed ....**Other standard module stuff???**
    - bim\_group\_allocation
        - Instance data: id bim userid groupid
        - NO HIERARCHICAL DATA
    - bim\_questions
        - Instance data: id, bim, title, body, min\_mark, max\_mark
        - NO HIERARCHICAL DATA
    - bim\_student\_feeds
        - Instance data: id, bim, userid, numentries, lastpost, blogurl, feedurl
        - NO HIERARCHICAL DATA
    - bim\_marking
        - Instance data: id, bim, userid, marker, question, mark, status, timepublished, timemarked, link, post, comments, title
        - NO HIERARCHICAL DATA

### Implementing it

Seems a fairly straight forward process in generating the backup. I'm simply copying the backuplib.php functions from the choice and forum modules. Mostly choice as it's simpler.

**NOTE:** In saving the data for an element they are not saving the foreign key back to the instance of the module. i.e. each question belongs to BIM, specified by the bim->id. But the BIM id is not being saved for the question. Obviously to be populated on restore.

I am wondering how some of the large text fields - including HTML - will go.

Also how the underscores in field names in the database tables will go. Seems the Moodle model is to run the text all together - minmark instead of my min\_mark.

#### Getting it to appear

I have an initial backuplib.php up. Have tried to do a backup on the course with a BIM and it failed due to syntax errors in backuplib.php. However, when those were fixed there were no options in the displayed backup page for BIM. Something is missing.

Maybe it is the function bim\_check\_backup\_mods - something in backuplib.php for the module that informs the general back up what to display. Let's try.

Actually, it appears I had a typo in one of the functions.

A bit more provision of functions and hey presto, it is working, at least the bit I've implemented.

#### Next steps

- Writing restore functions for course data.
    
    Got the initial ones working. Even tested them round trip.
    
- Writing the backup functions for the user data.
    - student feeds - write data
    - student feeds - display
    - marking - write data
    - marking - display
    - group allocation - write data
    - group allocation - display
- Writing restore functions for user data.
    
    - group allocation
    - marking
    - student feeds