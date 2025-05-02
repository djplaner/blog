---
title: Cooked course feeds - An approach to bringing the PLEs@CQUni, BAM and Indicators projects together?
date: 2009-03-11 09:12:53+10:00
categories: ['bam', 'blackboardindicators', 'elearning', 'innovation', 'plescquni']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: An alternate BAM related idea &laquo; The Weblog of (a) David Jones
      author_email: null
      author_ip: 66.135.48.160
      author_url: https://djon.es/blog/2009/03/11/an-alternate-bam-related-idea/
      content: '[...] The Weblog of (a) David Jones Another voice in the blogosphere    &laquo;
        Cooked course feeds - An approach to bringing the PLEs@CQUni, BAM and Indicators
        projects&nbsp;toget... [...]'
      date: '2009-03-11 10:49:36'
      date_gmt: '2009-03-11 00:49:36'
      id: '2239'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: The Indicators Project &laquo; Col&#8217;s Weblog
      author_email: null
      author_ip: 72.233.96.141
      author_url: http://beerc.wordpress.com/2009/03/15/the-indicators-project/
      content: '[...] Indicators project where we look at what&#8217;s happened and try
        to infer something from it. In David&#8217;s Blog he describes these as lag indicators
        whereas the more interesting and last part of the project is [...]'
      date: '2009-03-15 11:44:40'
      date_gmt: '2009-03-15 01:44:40'
      id: '2240'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The following is floating an idea that might be useful in my [local context](http://www.cqu.edu.au/).

### The idea

The idea is to implement a "cooked feed" for a CQUniversity course. An RSS or OPML feed that either students or staff or both can subscribe to and receive a range of automated information about their course. Since some of this information would be private to the course or the individuals involved, it would be password protected and could be different depending on the identity of the person pulling the feed.

For example, a student of the course would receive generic information about the course (e.g. any recent posts to the discussion forums, details of resources uploaded to the course site) as well as information specific to them (e.g. that their assignment has been marked, or someone has responded to one of their discussion posts). A staff member could receive similar generic and specific information. Since CQU courses are often offered across multiple campuses staff and student information could be specific to the campus or the sets of students (e.g. a tutor would receive regular updates on their students - have they logged into the course site etc)

A staff member might get a set of feeds like this:

1. Student progress - perhaps containing a collection of feeds. One might be _summary_ that summarises progress (or the lack thereof) for all students and then one feed per student.
2. Course site - provides posts related to the course website. For example, posts to discussion forums, usage statistics of resources and features etc.
3. Tasks and events - updates of when assignments are due, when assignments are meant to be marked, when results need to be uploaded. These updates would not only contain information about what needs to be done, but also provide links and advice about how to perform them.

The **"cooked"** adjective suggests that the feeds are not simply raw data from original sources. But that they undergo additional preparation to increase the value of the information they contain. For example, rather than a single post simply listing the students who have (or have not) visited a course site the post might contain the students GPA for previous courses, some indication of how long into a term they normally access a course site, when they added the course (in both date and week format - i.e. week 2 of term), links back to institutional information systems to see photos and other details of the students, links to an email merge facility to send a private/bulk email to all students in a particular category, a list of which staff are responsible for which students etc.

The point is that the "cooking" turns generic LMS information into information that is meaningful for the institution, the course, the staff, and the students. It is this contextual information that will almost always be missing from generic systems, simply because they have to be generic and each institution is going to be different.

### Why?

The [PLEs@CQUNi project](http://cddu.cqu.edu.au/index.php/PLEs%40CQUni) already has a couple of related sub-projects doing work in this area - discussion forums and BAM.

**Discussion forums.** The slideshow below explains how staff can currently access RSS feeds generated from the discussion forums of CQU's current implementation of Blackboard version 6.3. A similar feature has already been developed for the discussion forum used in the other "LMS" being used at CQU.


!!! warning "Outdated content no longer available"

    Presentation from Slideshare no long available


The above slideshow uses the idea of the ["come to me" web](http://personalinfocloud.com/2006/01/the_come_to_me_.html). This meme is encompasses one reason why doing this might be a good thing. It saves time, it makes information more visible to the staff and the students. Information they can draw upon to decide what to do next. Information in a form that allows them to re-purpose and reuse for tasks that make sense to them, but would never be apparent to a central designer.

**BAM.** The [Blog Aggregation Management (BAM) project](/blog2/research/bam-blog-aggregation-management/) now generates an OPML feed unique for each individual staff member to track their students' blog posts. The slidecast below outlines how they can use it.


!!! warning "Outdated content no longer available"

    Presentation from Slideshare no long available


The [indicators project](http://beerc.wordpress.com/2008/12/21/more-on-the-indicators/) is seeking to mine usage logs of the LMS to generate information that is useful to staff. I think there is value in this project looking at generating RSS feeds for staff based on the information it generates. Why depends on the difference between lag and lead indicators.

I've always thought that too much of the data generated at Universities are lag indicators. Indicators that tell you how good or bad things went. For example, "oh dear, course X had a 80% failure rate". While having this information is useful it's too late to do anything. You can't (well you shouldn't be able to) change the failure rate after it has happened.

What is much more useful are lead indicators. Indicators that offer you some insight into what is likely to happen. For example, "oh dear, the students all failed that pop quiz about topic X". If you have some indication that something is starting to go wrong, you may be able to do something about it.

**Aside:** Of course things brings up the problematic way most courses are designed, especially the assessment. They are designed in ways such that there are almost no lead indicators. The staff have no real insight into how the students are going until they hand in an assignment or take an exam. By which time it is too late to do anything.

Having the indicators project generating RSS posts summarising important lead indicators for a course might encourage and help academics take action to prevent problems developing into outright failure.

This is also encompassed in the idea of BAM generating feeds and the very idea of BAM in the first place. It allows staff to see which students are or are not progressing (lead indicator) and then take action they deem appropriate.

It's also a part of the ideas behind [reflective alignment](/blog2/2009/03/09/how-to-improve-lt-and-e-learning-at-universities/). That [post](/blog2/2009/03/09/how-to-improve-lt-and-e-learning-at-universities/) also has some suggestions about how to implement this sort of thing.