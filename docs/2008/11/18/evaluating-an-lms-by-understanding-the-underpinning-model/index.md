---
categories:
- chapter-2
- elearning
- lmsevaluation
- lmsreview
date: 2008-11-18 10:32:26+10:00
next:
  text: The model underpinning blackboard and how ACCT19064 uses it
  url: /blog2/2008/11/19/the-model-underpinning-blackboard-and-how-acct19064-uses-it/
previous:
  text: 'PLEs@CQUni: Origins, rationale and outcomes so far'
  url: /blog2/2008/11/17/plescquni-origins-rationale-and-outcomes-so-far-2/
tags:
- lms
title: Evaluating an LMS by understanding the underpinning "model"
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: joelcfisler
      author_email: joel.fisler@id.uzh.ch
      author_ip: 130.60.112.227
      author_url: null
      content: "From what I understand you are only evaluation Sakai and Moodle. Is there\
        \ a particular reason why you are looking at these two LMS? I would consider also\
        \ talking a look at OLAT, a Swiss open source LMS that we use here at the University\
        \ of Zurich. Check www.olat.org for more information or demo.olat.org for a demo\
        \ LMS server.\nGreetings from Zurich\nJo\xEBl"
      date: '2008-11-25 01:54:44'
      date_gmt: '2008-11-24 15:54:44'
      id: '1889'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: davidtjones
      author_email: d.jones@cqu.edu.au
      author_ip: 138.77.2.131
      author_url: http://cq-pan.cqu.edu.au/david-jones/
      content: 'G''day Joel,
    
    
        Thanks for the comment.
    
    
        The choice of Sakai and Moodle is out of my hands.  It was an organisational decision
        which I have to live with.
    
    
        Frankly, I think the whole LMS model is broken and is one of the contributing
        factors to the current woeful state of most e-learning within universities.  If
        I had my choice I would not have adopted any LMS.
    
    
        So what''s the alternative, essentially something based on the information systems
        design theory I''ve been developing over recent years.
    
    
        https://djon.es/blog/publications/the-formulation-of-an-isdt-for-e-learning/
    
    
        But that''s not surprising given my prejudices.
    
    
        Some other related posts on my blog
    
    
        https://djon.es/blog/2007/09/30/its-all-over-no-need-to-select-an-lms/
    
    
        https://djon.es/blog/2007/06/12/cqus-first-web-20-course-site/
    
    
        and this one
    
    
        https://djon.es/blog/2007/03/13/ateleological-development-as-a-better-way-to-develop-university-e-learning-systems/
    
    
        David.'
      date: '2008-11-25 08:55:55'
      date_gmt: '2008-11-24 22:55:55'
      id: '1890'
      parent: '0'
      type: comment
      user_id: '1'
    
pingbacks:
    - approved: '1'
      author: The model underpinning blackboard and how ACCT19064 uses it &laquo; The
        Weblog of (a) David Jones
      author_email: null
      author_ip: 74.200.244.85
      author_url: https://djon.es/blog/2008/11/19/the-model-underpinning-blackboard-and-how-acct19064-uses-it/
      content: '[...] The Weblog of (a) David Jones Another voice in the blogosphere    &laquo;
        Evaluating an LMS by understanding the underpinning&nbsp;&#8220;model&#8221; [...]'
      date: '2008-11-19 08:43:03'
      date_gmt: '2008-11-18 22:43:03'
      id: '1888'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
Currently, CQUni is undertaking an evaluation of [Sakai](http://sakaiproject.org/portal) and [Moodle](http://moodle.org/) as a replacement for [Blackboard](http://blackboard.com/us/index.bbb) as the organisation's Learning Management System. The evaluation process includes many of the standard activities including

- Developing a long list of criteria/requirements and comparing each LMS against that criteria.
- Getting groups of staff and students together to examine/port courses to each system and compare/contrast.

Personally, I feel that while both approaches are worthwhile they fail to be sufficient to provide the organisation with enough detail to inform the decision. The main limitation is that neither approach tends to develop a deep understanding of the affordances and limitations of the systems. They always lead to the situation that after a few months/years of use people can sit back and say, "We didn't know it would do X".

A few months, at least, of using these systems in real life courses would provide better insight but is also prohibitively expensive. This post is the start of an attempt to try another approach, which might improve a bit on the existing approaches.

### What is the approach?

The approach is based somewhat on [some previous ramblings](/blog2/2008/11/17/the-dissonance-gap-in-systems-and-lms-evaluations/) and is based on the assumption that an LMS is a piece of information technology. Consequently, it has a set of data structures, algorithms and interfaces that either make it hard or easy to perform tasks. The idea is that if you engage with and understand the model, you can get some idea about what tasks are hard or difficult.

Now there is an awful lot of distance between saying that and actually doing it. I'm claiming that the following posts are going to achieve anywhere near what is possible to make this work effectively. My existing current context doesn't allow it.

At best this approach is going to start developing some ideas of what needs to be done and which I didn't do. Hopefully it might "light" the way, a bit.

### Using the concept elsewhere

[We've](http://cddu.cqu.edu.au/) actually been working on this approach as a basis for staff development in using an LMS. Based on the assumption that understanding the basics of the model will make things work somewhat easier for folk to use. The first attempt at this is the slidecast prepared by [Col Beer](http://cddu.cqu.edu.au/index.php/Colin_Beer) and shown below.

[Blackboard@CQ Uni](http://www.slideshare.net/colinwbeer/blackboardcq-uni-presentation?type=powerpoint "Blackboard@CQ Uni")

View SlideShare [presentation](http://www.slideshare.net/colinwbeer/blackboardcq-uni-presentation?type=powerpoint "View Blackboard@CQ Uni on SlideShare") or [Upload](http://www.slideshare.net/upload?type=powerpoint) your own.

### What will be done?

Given time constraints I can only work with a single course, from a single designer. More courses, especially those that are different would be better. But I have to live with one. I've tried to choose one that is likely to test a broader range of features of the LMSes to minise this. But the approach is still inherently limited by this small sample set.

The chosen course is the T2, 2008 offering of [ACCT19064, Auditing and Professional Practice](http://handbook.cqu.edu.au/Handbook/course.jsp?courseid=61458). For 2008 this course underwent a complete re-design driven by two talented and committed members of staff - [Nona Muldoon](http://dtls.cqu.edu.au/FCWViewer/staff.do?site=4&sid=MULDOONN) (an instructional designer) and [Jenny Kofoed](http://fbi.cqu.edu.au/FCWViewer/staff.do?site=1&sid=KOFOEDJ) (an accounting academic). As part of this re-design they made use of [machinima](http://cddu.cqu.edu.au/index.php/ACCT19064_Machinima_Project) produced in Second Life. The re-design was found to be particularly successful and has been [written about](http://cddu.cqu.edu.au/images/e/ec/Machinima.pdf).

The basic steps will be

1. Explain the model underpinning Blackboard and how it is used within the course.
2. Seek to understand and explain the model underpinning Moodle and then Sakai.
3. Identify and differences between the models and how that might impact course design.

Hopefully, all things being equal, you should see a list of posts describing these steps linked below.