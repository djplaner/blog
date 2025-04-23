---
title: "Getting back into BIM: Summary and way forward"
date: 2009-12-14 14:23:41+10:00
categories: ['bam', 'elearning']
tags: ['bim']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: BIM and Moodle development &#8211; a more coherent overview found? &laquo;
        The Weblog of (a) David Jones
      author_email: null
      author_ip: 72.233.96.141
      author_url: https://djon.es/blog/2009/12/15/bim-and-moodle-a-more-coherent-overview/
      content: '[...] level of annoyance at the state of the public documentation around
        Moodle development slowing down BIM development. That state is essentially with
        stuff all over the place, no coherent path through it [...]'
      date: '2009-12-15 15:57:05'
      date_gmt: '2009-12-15 05:57:05'
      id: '2885'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: BIM &#8211; getting student registration working &laquo; The Weblog of (a)
        David Jones
      author_email: null
      author_ip: 74.200.245.226
      author_url: https://djon.es/blog/2009/12/17/bim-getting-student-registration-working/
      content: '[...] &#8211; getting student registration&nbsp;working  So, getting back
        into BIM development. The last post reminded me where I&#8217;m up to. The following
        is an attempt to plan, implement and document some [...]'
      date: '2009-12-17 10:02:49'
      date_gmt: '2009-12-17 00:02:49'
      id: '2886'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: BIM &#8211; Getting &#8220;show student details&#8221; working &laquo; The
        Weblog of (a) David Jones
      author_email: null
      author_ip: 72.233.96.152
      author_url: https://djon.es/blog/2009/12/17/bim-getting-show-student-details-working/
      content: '[...] next step in BIM development. As summarised in the last post the
        plan is to implement the remaining screens roughly complete so that potential
        users can interact and give feedback. This included the need to [...]'
      date: '2009-12-17 15:58:37'
      date_gmt: '2009-12-17 05:58:37'
      id: '2887'
      parent: '0'
      type: pingback
      user_id: '0'
    
---

See also: [[blog-home | Home]]

The last couple of months have resulted in an absence from work on BIM ([BAM](/blog2/research/bam-blog-aggregation-management/) into Moodle). This post is meant to be a summary of where I had gotten up to and a restatement of what I need to do. The latter part is somewhat uncertain due to limited communication within my local context. Somewhat disappointing.

On the plus side, contributing to my lack of work on BIM was the attendance at a couple of conferences, including [ASCILITE'09](http://www.ascilite.org.au/conferences/auckland09/). It was obvious from a number of ASCILITE presentations that BAM/BIM remains an important and innovative tool that is much needed.

If you've only started following this blog recently, this is they type of post acts as a log/diary of the work I have done on BIM. Probably not much of interest to a broader community.

### Current status

Up until now most of the work has been familiarising myself with the "Moodle way". I'd gotten to the stage where there was:

- A BIM activity module in the Moodle source tree.
- The module would create the BIM database tables.
- The ability to add BIM as an activity to a course.
- The resulting link inserted into the course would operate as the student details screen ([screen dump](http://www.flickr.com/photos/david_jones/3882960287/)) and show details about the students blog posts.
- This screen would react to different data within the database.

The one remaining, fairly important task to be done was to figure out how to get Moodle to take data from the user and appropriately put it into the database. This is essentially the one remaining component of web application development.

Once familiar with this process, the implementation of BIM becomes a translation process from the previous system into Moodle.

### How it will work

This is developed in other posts, but I'm going to re-create it here to refresh all those dormant memory patterns I have. Much of it is pretty similar to BAM. I've included links to screen dumps from BAM of most of the screens listed below. BIM screens will be based on these, but they will likely be different.

The intent is that BIM will work in the following way:

- Creation.
    - Course coordinator will add BIM as an activity to their course.
    - In doing so, the coordinator will need to fill in the **configuration screen** with details of the use of BIM (assignment name, posts etc.)
    - At the end of this process, there will be a [link in the Moodle course to the BIM activity](http://www.flickr.com/photos/david_jones/4183145931/). This is used by both staff and students.
- Normal use.
    - All users of BIM will use the link to the BIM activity added in the creation stage (e.g. [this screen dump](http://www.flickr.com/photos/david_jones/4183145931/)). Depending on what role they perform, they will see different information:
        - Students: there are two different views for students
            - **[Register Blog screen](http://www.flickr.com/photos/david_jones/3268716454/in/set-72157608613577424/)** - appears when the student has not registered their blog. Shows some explanatory text and a text box. The student has to paste in the URL for their blog and hit submit. If there is a valid feed, success.
            - **Student details screen** - appears once the student has registered their blog. It will show what BIM knows about the student blog (where it is, the student's name, the number of posts) and also any marking information (marks and comments) that have been released (only staff within an appropriate role can release marks/comments).
        - Coordinator: will have access to three different screens (all which are also used elsewhere by other people - with some modification).
            - **Configuration screen** - the same as the screen they see when adding BIM as an activity. Allows them to view and change the configuration of BIM for the course. There will need to be some limitations on what can be changed, but this needs to be thought through.
            - **[Show details screen](http://www.flickr.com/photos/david_jones/3268716654/in/set-72157608613577424/)** - shows an overview of the details for all students. "All" students can be chosen as for the course, for a particular marker etc. Details include student name, number, number of entries in blog, and link to live blog.
            - **[Show posts screen](http://www.flickr.com/photos/david_jones/3268716836/in/set-72157608613577424/)** - shows for "all" students an indication of whether they have posted answers to a particular question; number of posts blogged and marked; summary of marks etc.
            - **[Mark post screen](http://www.flickr.com/photos/david_jones/3267891725/in/set-72157608613577424/)** - this is where the students' post is marked (if required - not all courses using BIM mark blog posts).
            - **Re-allocate screen** - BIM attempts to automatically allocate student posts to the question (set by the coordinator) that it matches. This automated match doesn't always work. This screen shows all of the student's posts and allows the coordinator to change the allocation of a post.
        - Other staff: Will have access to the **Show details screen**, **Show posts screen**, **Re-allocate screen** and **Mark post screen** as described for the coordinator. The main difference is that "other staff" can only see details for students that they have been allocated to mark.
    - Aggregation, mirroring and allocation of blog posts.  
        At a regular time interval (set at the system level) BIM will check if there is a new post to each students' blog. If there is, BIM will
        - Add a copy of the new post(s) to a local RSS file, one per student.
        - Examine the new post(s) to see if they match any of the required questions as specified by the coordinator. If there is a match, the database will be updated to indicate another question has been answered.
        - Update the database that some new posts have been made.