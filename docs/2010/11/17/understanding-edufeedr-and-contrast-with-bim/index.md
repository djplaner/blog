---
title: Understanding EduFeedr and contrast with BIM
date: 2010-11-17 22:43:16+10:00
categories: ['bim']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

The following is an attempt to summarise an attempt to understanding [EduFeedr](http://www.edufeedr.net/) a bit more. Especially to compare and contrast it with [BIM](/blog2/research/bam-blog-aggregation-management/). I'm particularly interested in seeing what lessons can be learned from EduFeedr, not to mention what code and ideas can be borrowed.

### What

> EduFeedr is an educationally enhanced feed reader, designed specifically for courses that take place in a distributed learning environment where all students use their personal blogs and other social software.

i.e. EduFeedr is aimed at open courses. The need for it arose out of experiences with such courses and the workload involved in tracking contributions.

EduFeedr offers four main tasks

1. setting up the course;  
    Each course has a ["site"](http://www.edufeedr.net/pg/edufeedr/view_educourse/34). Each site has six sections: (1) course feed, (2) course info, (3) participants, (4) assignments, (5) progress, and (6) social network.
    
    _BIM:_ is a Moodle activity. Each Moodle course can have multiple BIM activities.
    
2. enrolling to the course,  
    Done via a simple form with name, email and blog url
    
    _BIM:_ students have to be enrolled in the Moodle course containing the BIM activity.
    
3. aggregating blog posts and comments, and  
    
    _BIM:_ only aggregates posts
    
4. visualizing the progress and social network between the learners.  
    [Displayed](http://www.edufeedr.net/pg/edufeedr/view_educourse/41?filter=connections) on EduFeedr and also able to be downloaded. Information can be downloaded in various formats, including: OPML file containing all post and comment feeds; a vCard for email addresses of participants; HTML blogroll.
    
    _BIM:_ student details are available via various Moodle sources. BIM does provide an OPML file for teaching staff containing the URLs for their students' feeds.
    

### Implementation

EduFeedr is implemented on top of [Elgg](http://elgg.org/) and uses [Simplepie](http://simplepie.org/), [JSViz](http://code.google.com/p/jsviz/).

Actually, the retrieval of the feeds is done by a companion utility called EduSuckr. EduSuckr is run hourly. _BIM:_ mirroring also run via cron, but time is controlled via the Moodle configuration interface. Mirroring of an individual student blog is also done when a student attempts to view their details.

EduFeedr and EduSuckr appear to communicate via WSDL/SOAP.

### Lessons

- No standard way to locate comments feed.  
    _BIM:_ doesn't look at comments, but I assumed this might be a problem.
- Linking posts to assignments.  
    Appear that they expect students to link to the description of the assignment for the post.
    
    _BIM:_ tries to compare the title and content of the student blog post with the title/content of the assignment question using simple similarity comparison. Teaching staff can also allocate a student post to a particular assignment question....future plan is to allow the students to do this as well.
    
- Linking comments with participants.  
    Again lack of standards with identifying authors of comments, makes this difficult.
    
    _BIM:_ doesn't look at comments, so not a problem.
    
- Only recent items in feeds.  
    This is a problem with BIM as well. EduSuckr uses the same solution as BIM. It keeps a local archive of all posts. The teacher can specify a period when to archive posts. BIM has the option for mirroring to be turned off.