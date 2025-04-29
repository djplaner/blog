---
title: bim2 - What's working for coordinator
date: 2012-04-05 15:46:28+10:00
categories: ['bim2']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: bim2 &#8211; working on coordinator &#8211; part 1 &laquo; The Weblog of
        (a) David Jones
      author_email: null
      author_ip: 72.232.7.18
      author_url: https://djon.es/blog/2012/04/11/bim2-working-on-coordinator-part-1/
      content: '[...] More work on bim2, this one starting work on the previously identified
        tasks. [...]'
      date: '2012-04-11 21:23:39'
      date_gmt: '2012-04-11 11:23:39'
      id: '311'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: Bug fix and to do for BIM &laquo; The Weblog of (a) David Jones
      author_email: null
      author_ip: 74.200.247.110
      author_url: https://djon.es/blog/2012/12/28/bug-fix-and-to-do-for-bim/
      content: '[...] This post has a list of what was working and not with the coordinator
        interface and a later post updates some of this. Need to revisit these and start
        a list in basecamp. [...]'
      date: '2012-12-28 11:22:10'
      date_gmt: '2012-12-28 01:22:10'
      id: '312'
      parent: '0'
      type: pingback
      user_id: '0'
    
---

See also: [[blog-home | Home]]

More detail on what BIM is [can be found here](/blog2/research/bam-blog-aggregation-management/)

The following documents initial forays into getting the coordinator view of bim. The aim is to summarise what is or isn't working in Moodle 2.1

### What's working, what's not

The main aim in this section is to identify what's working, what's not and ideas for minor improvement.

The coordinator (lead teacher role) is the most complex of the roles. It's major screens and their related activities include

- Configure BIM - set up basics of a BIM activity
    - Display configuration - Basically working  
        Improvements that could be made
        - Help buttons for configuration options.
        - Have the "General Steps" actually link to the appropriate screen.
        - Change "provided below" link to something more human readable.
    - Change configuration - not working
        - Problems on inserting data into the database. Some insertions seem to be putting data in/modifying database, but errors happening
- Manage questions
    - Display existing - Working  
        Improvements
        - help buttons for elements to add.
        - Work on the introductory text.
    - Add new - **NOT WORKING**
        - All seems to be working, but the text of the question isn't appearing in the form and may not be placed into the database. The text is being added when changing an existing question.
        - The pause while displaying results of add new/delete etc is not waiting long enough.
    - Delete existing - Working
    - Change existing - Working
- Allocate markers
    - display - Working  
        Improvements
        - Layout of the submit buttons.
        - Rethink intro text
        - Addition of some help buttons
        - Links to show current course groups and change them.
    - Change - **NOT WORKING**  
        Seems to process the change, but an error prevents it from finishing. Perhaps when deleting/removing any group allocations that have changed. When simply adding a group where none is currently allocated, this does work.
- Manage marking - **NOT WORKING**  
    Doesn't display, crashes and burn after displaying heading.
- Find student
    - Display - works
    - Find student - **NOT WORKING**  
        Error in SQL command, will need fixing.
- Your students - much the same interface as for the markers, so hopefully will work
    - View student details
        - Display - working
        - OPML feed - working
        - change blog - working  
            **Improvements**
            - Once changed, navigation to return to "Your students" is impossible. Need to improve.
    - Mark posts - working
    - Allocate questions - basically working but... **improvements**
        - The progress message after allocating a question occasionally pops up this "\[\[marker\_change\_alloc\_descriptor\]\]" indicating a missing language string.
    - Mark post - working

Time to watch a horse race.