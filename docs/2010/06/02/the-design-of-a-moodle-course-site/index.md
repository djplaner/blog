---
categories:
- moodle
date: 2010-06-02 17:01:06+10:00
next:
  text: Adopter focused development and diffusion theory
  url: /blog2/2010/06/04/adopter-focused-development-and-diffusion-theory/
previous:
  text: The role of experience
  url: /blog2/2010/06/02/the-role-of-experience/
title: The design of a Moodle course site
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: Andrew Chambers (@atsc)
      author_email: atsc@twitter.example.com
      author_ip: 129.94.149.160
      author_url: http://twitter.com/atsc
      content: Thanks for this blog post. I am in the process of doing the same thing
        for a post grad masters course in business. This helps me think through the process
        and gives me some resources. You have almost convinced me to write up my own blog
        post on the process!
      date: '2011-10-26 14:29:37'
      date_gmt: '2011-10-26 04:29:37'
      id: '3075'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: davidtjones
      author_email: davidthomjones@gmail.com
      author_ip: 124.187.169.111
      author_url: https://djon.es/blog/
      content: 'Glad it was of some use Andrew.  WIthin the next 6-12 months I should
        be revisiting this post/process in more detail as I''ll be starting a new job
        in which I''ll probably be creating more Moodle sites.
    
    
        Would be useful to hear about your ideas and experiences.....does that encourage
        a blog post?'
      date: '2011-10-26 20:53:30'
      date_gmt: '2011-10-26 10:53:30'
      id: '3076'
      parent: '3075'
      type: comment
      user_id: '1'
    
pingbacks:
    - approved: '1'
      author: Should academics manually create course websites? &laquo; The Weblog of
        (a) David Jones
      author_email: null
      author_ip: 74.200.247.107
      author_url: https://djon.es/blog/2010/06/07/should-academics-manually-create-course-websites/
      content: '[...] was more broadly applicable was, &#8220;if you do something more
        than once, automate it&#8221;. I recently had to create a Moodle course site from
        scratch. It was a simple (some might argue simplistic) site, by no [...]'
      date: '2010-06-07 20:36:40'
      date_gmt: '2010-06-07 10:36:40'
      id: '3074'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
For a couple of different reasons I am helping someone with the design and implementation of a Moodle course site. I've developed an activity module for Moodle but have never created an entire course site. Have thought about how it might be done, but never done it. The following is a description and some reflections on the experience.

I'm particular interested in:

- Is the "pragmatic" approach to design a Moodle course site as widespread as I think? Or are their great swathes of teachers creating Moodle course sites from scratch?
- What are the experiences of folk who have used the social format for a course? Good? Bad? Happy with the support Moodle provides for this format?
- What about those using the topic/weekly course formats, how do you deal with scrolling problem?

### Reflection

After doing all of the following, it's not a great surprise that my opinions, biases and prejudices have been confirmed. In particular, it doesn't matter what minimum standards or tool affordances put in place by management and technologists, most academics are looking to tweak how they've previously taught their courses and then move onto other things. If you want to improve the quality of L&T, you have to move beyond developing policies or technologies.

It's also reinforced that Moodle 1.9.x still retains some fairly significant limitations in trying to do something fairly flexible. I'm not sure there's much here that's going to break an academics "tweaking" behaviour. Don't get me wrong, in comparison to some other LMS, it's better, in places. It's just that this isn't exactly a very high bar to jump.

It would be tremendously interesting to have been able to gather some more qualitative stories of how academics have handled this transition and then compare that with what management thinks has gone on and then compare all that with what the students thought.

### The purpose of the course site

I can hear some educational developers I know wanting to step back and look at the outcomes of the course, do a curriculum mapping, evaluate the alignment of the course and identify appropriate learning activities that would improve this. Preferably if we were talking about Chickering and Gamson's (1987) 7 principles for good practice in undergraduate education (a particular lens our institution is using). I can hear another staff member rabbiting on about the work of Oliver (2000), Herrington and colleagues. The learning design crew (Bennett et al 2006), the LAMS folk (Dalziel, 2003) or any of a number of other educationally informed design approaches. Long term Moodle folk might refer [to the "principles"](http://docs.moodle.org/en/Pedagogy#Social_Constructionism_as_a_Referent) often said to underpin Moodle.

The reality is that this academic has other priorities which means the academic wants to do the minimum. To quote

> All I essentially want to do is to copy the last time I ran _..the course.._

This is in line Stark (2000) identified as the dominant setting for most academics, i.e. teaching an existing course, generally one they've taught before and subsequently they will spend most of their time fine tuning a course or making minor modifications to material or content.

That is, most academics are not going to design a course from scratch. They are going to recreate what they know. This is one of the reasons why one of the most popular local "innovations" around Moodle at my current institution has been a Moodle site "template" that re-creates the hierarchical structure of a course site from Blackboard. The LMS most staff will have used prior to their move to Moodle.

So, this academic is not alone in simply wanting to re-create what they did before.

#### Other constraints

This, however, is not the only constraint. The institution has introduced "Minimum Service Standards for course delivery" which is intended to "provide the pedagogical basis for developing online learning environments and to encourage academic staff to look beyond existing practices and consider the useful features of the new LMS." (Tickle et al, 2009). Anecdotal evidence suggest that for a significant number of staff the minimum standard has become a "tick the boxes" exercise. i.e at the best make sure I have ticked the boxes, at worst, make sure I tick the boxes without necessarily having achieved the standard.

So, the site design will have to meet those requirements.

### Starting the copy process

If the aim is to copy what was done before, the questions are:

- What was done before?  
    What's in the previous course site, how was it structured.
- What can be done now?  
    i.e. what are the constraints and assumptions built into Moodle.
- How can you get from one to the other?

The rest of this seeks to answer those questions.

### What was done before?

The course was hosted in [Webfuse](http://webfuse.cqu.edu.au/Courses/2009/T2/) and was implemented as a standard Webfuse minimum course site. Such a site uses a simple hierarchical structure with a home page that had a description of the course and a list of updates and 5 sub-sections:

1. Updates - place where course wide updates were created/archived.  
    Only a couple of system wide updates used.
2. Study Schedule - a week by week breakdown of the course.  
    Reasonably complete with a description of the weeks topic and a collection of basic tasks. The Word documents for the study guide are uploaded in this section. The design assumption (I was the designer of Webfuse) was that it would be uploaded into the Resources section and linked from here and the resource section.
3. Assessment - a description of the assessment for the course.  
    A description of the assessment pieces.
4. Resources - a collection of the learning resources.  
    In this case, only the discussion forum, mailing list and barometer. Having both a discussion forum and a mailing list is interesting.
5. Staff - photos and contact details for all staff and also a staff only section.

A fairly (very) basic course. Two glimmers of hope (if you're taking the learning nazi approach) are:

- the Discussion forum.  
    Quite detailed in structure, the attempt seems to have been made to think this through. However, not many contributions. Given that the vast majority of students in this course are at the international campuses and have a heavy focus on face-to-face instruction (normally) this isn't that surprising.
- use of BAM.  
    Students are expected to maintain individual blogs for reflection as part of the assessment.

### What can be done now?

#### Layout

[This page](http://medusa.ballarat.edu.au/lews/drupal/staff/moodle/howto/layout) from Uni Ballarat gives a good overview of the layout of Moodle course site. i.e. a main course area in the middle and two columns of blocks on either side (thought at least one of the columns can be turned off).

With the blocks it appears that you can add and remove blocks as you like. Will have to test that out later.

With the layout of the main course area, there are three normal Moodle options and a fourth local kludge. The three normal Moodle layouts are:

1. [Weekly](http://cddu.cqu.edu.au/images/Picture11.png) - where the course site is divided into sequential, weekly blocks.
2. [Topical](http://cddu.cqu.edu.au/images/Picture12.png) - where the sequential blocks are based on topics.
3. [Social](http://cddu.cqu.edu.au/images/Picture13.png) - where the site is structured around the discussion forum.

All three of these options might be options for this course. The original study schedule could be copied into either the weekly or topical formats with little or no modification. The use of the discussion forum in the old course, could fit very nicely with the social format with some of the information from the study schedule weaved into messages.

The fourth local kludge, appears to be a mutation of the weekly format where it appears that the course area (non-week first block) is used for a course logo or similar. The first main week's block is used for a collection of HTML tables that creates:

- A welcome course description message in one table.
- A collection of menu items (e.g. the course, resources, discussions, assessment etc.) which give the illusion of a hierarchical site. Under each menu is a collection of links to Moodle activities/resources related to that menu item.
- A simple weekly navigation menu (week 1, week 2 etc.) that links to a simple web page that summarises the tasks for that week.

The second week's block is hidden. This, it appears, is where the actual activities and resources are added to the site. They are then linked, as appropriate, to the menu section and the weekly summaries.

I don't think this will work in this situation. It's a fair bit of work to set up and appears to break the affordances of Moodle. While I'm keen to minimise the difficulty of the transition, surely, you do actually want to move with the affordance of the new tool?

#### Resource and activities

The requirements for this course are fairly limited: a discussion forum, some word documents and a BAM equivalent. As there is no standard module in Moodle that implements a BAM service, this could have been a problem. However, given that the institution is currently using the [BIM activity module](/blog2/research/bam-blog-aggregation-management/) I wrote as a BAM port, this isn't a problem.

### Helping the academic decide

While I can imagine either the weekly/topic or social format versions of this course, I don't think that the academic will be able to. In addition, I've never really seen a social format Moodle course, so I'm not 100% confident that my predictions will match the reality. Hence the need to create examples sites, something concrete for the academic to look at and play with.

#### Create the site

Am doing this on a local install of Moodle, so create the site.

Mm, there are other formats. LAMS, SCORM and one or two others. Whether they are available on the institutional site?

If you choose "Social format" it still asks for number of weeks/topics, wouldn't that be no longer needed?

So, that's the site created. By default it's got some pre-defined blocks down the left hand side - I think these are based on the institutional defaults, might be just normal Moodle defaults. There's the option to add blocks in the right hand column and just about an empty space in the middle but with a button "Add a new discussion topic".

#### Adding the topics

In my head, we're going to borrow the approach used in the old course site's discussion forum. i.e. different forums for different purposes, including each week. The last time I'd taught, I'd used a similar approach. The plan is to use pretty much the same structure.

Oh, that is sad. It appears that rather than separate discussion forums which can be used to separate out tasks, Moodle has by default set the course area as a single forum. Ahh, and the topics are shown with most recent first. Surely there's got to be an option to change that?

It appears not, looks like my assumptions don't match the affordances in Moodle. That's sad and means we're back to the bog standard weekly/topic format.

The general visuals on the Moodle forum were also not that great. Somewhat ugly and not great from an interface perspective. I wonder if that's inherent or arises because of the institutional template? It's sad because the discussion forum tool in Webfuse (circa about 2002) seems to have a better interface (not a great one, but certainly better than Moodle).

### Creating the weekly format

I've chosen weekly because like it or not most of the students/staff think in weeks of term, plus there's not a lot of difference in Moodle between the weekly and topic formats - at least to my inexperienced eye.

So, edit the options for the course to weekly and start a process of re-creating the study schedule from the old site in Moodle.

From here it's a fairly manual process with only a few tweaks about how to do this.

Time to wait and see what the academic thinks.</p

#### The scrolling problem

I think that the "scrolling problem" is a fairly typical complaint about Moodle sites. If you use the topic/week format and have more than a few fairly complete blocks, people have to start scrolling to get any where. That can add to confusion for some.

This was a problem we faced with the [Webfuse study schedule page](http://webfuse.cqu.edu.au/Courses/2006/T2/COIS20025/Study_Schedule/) design. The obvious way to solve it was internal links. If you [visit this study schedule page](http://webfuse.cqu.edu.au/Courses/2006/T2/COIS20025/Study_Schedule/) you will see that each weekly block as internal links to each of the other 12 weeks.

Is there an automated process in Moodle that helps do this?

I think for this site, I'll have to put in a kludge, somewhat like the local kludge course layout.

### References

Bennett, S., S. Agostinho, et al. (2006). "Supporting university teachers create pedagogical sound learning environments using learning designs and learning objects." IADIS Internatioanl Journal on WWW/Internet 4(1): 16-26.

Dalziel, J. (2003). Implementing learning design: The learning activity management syste (LAMS). 20th Annual Conference of the Australasian Society for Computers in Learning in Tertiary Education, Adelaide, SA.

Chickering, A. W. and Z. F. Gamson (1987). "Seven principles for good practice in undergraduate education." AAHE Bulletin 39(7): 3-7.

Oliver, R. (2000). When teaching meets learning: Design principles and strategies for Web-based learning environments that support knowledge construction. ASCILITE'2000, Coffs Harbour.

Stark, J. (2000). "Planning introductory college courses: Content, context and form." Instructional Science 28(5): 413-438.

Tickle, K., N. Muldoon, et al. (2009). Moodle and the institutional repositioning of learning and teaching at CQUniversity. ascilite 2009. Auckland, NZ: 1038-1047.