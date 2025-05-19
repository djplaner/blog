---
categories:
- blackboardindicators
- coursesites
- elearning
date: 2008-08-28 23:03:29+10:00
next:
  text: Choosing your indicators - why, how and what
  url: /blog/2008/08/31/choosing-your-indicators-why-how-and-what/
previous:
  text: Alternate foundations - the presentation
  url: /blog/2008/08/28/alternate-foundations-the-presentation/
title: Getting started on Blackboard indicators
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Choosing your indicators - why, how and what at David&#8217;s WebLog
      author_email: null
      author_ip: 138.77.94.11
      author_url: http://cq-pan.cqu.edu.au/david-jones/blog/?p=205
      content: '[...] About        &laquo; Getting started on Blackboard indicators [...]'
      date: '2008-08-31 12:52:45'
      date_gmt: '2008-08-31 02:52:45'
      id: '1596'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The [unit](http://cddu.cqu.edu.au/) I work for is responsible for providing assistance to [CQUniversity](http://www.cqu.edu.au/) staff and students in their use of e-learning. Which currently at CQUni is mostly the use of Blackboard.

The current model built into our use of Blackboard is that the academic in charge of the course (or their nominee) is responsible for the design and creation of the course site. In most instances, staff are provided with an empty course site for a new term at which stage they copy over the content from the previous offering, make some modifications and make the site available to students.

Not surprisingly, given the cruftiness of the Blackboard interface, the lack of time many staff have and a range of other reasons there are usually some fairly common, recurrent errors that are made. Errors which create workload for us when students or staff have problems. In many cases it may even be worse than this as students become frustrated and don't even complain, they suffer in agony.

Most of these problems, though not all, are fairly simple mistakes. Things that could be picked up automatically if we had some sort of automated system performing checks on course sites. The fact that Blackboard doesn't provide this type of functionality says something about the assumptions underlying the design of this version of Blackboard - a very teaching academic focus, not so much on the support side.

Developing this sort of system is what the [Blackboard Indicators project](http://cddu.cqu.edu.au/index.php/Blackboard_Indicators) is all about. It's still early days but we've made some progress. Two main steps

- Developed an initial proof of concept.
- Started a literature, colleague and literature search.

### Initial proof of concept

We currently have a web application up and running that, given a term, will display a list of all the courses that are meant to have Blackboard course sites and generate a number between 0 and 100 summarising how well a site has meant a particular indicator.

Currently, the only indicator working is the "Content Indicator". This is meant to perform some objective tests on, what is broadly defined as, the content of the course. Currently this includes

- Is the course actually available to students?  
    The score becomes 0 automatically if this is the case.
- Does the the site contain a link to the course profile?  
    20 is taken off the score there isn't one.
- Is the course profile link for the right term?  
    50 taken off if it's wrong.

At the moment, we're planning to put in place three indicators, the content indicator plus

- "Coordinator Presence"  
    How present is the coordinator of the course? Have they posted any announcements? Are they reading the discussion forum? Posting to it? What activity have they done on the site in the last two weeks?
- "All interactions"  
    What percentage of students and staff are using the site? How often? What are they using?

It's still early days and there remain a lot of questions, which we hope will be answered by our searching and some reflection.

### Literature, web and colleague search

We've started looking in the literature, doing google searches and asking colleagues what they are doing. Have some interesting information already.

What we do find will be discussed in our blogs, bookmarked on [del.icio.us](http://del.icio.us/) (tag: blackboardIndicators) and talked about on the [project page](http://cddu.cqu.edu.au/index.php/Blackboard_Indicators).