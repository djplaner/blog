---
categories:
- bad
- concretelounges
- edc3100
date: 2015-02-03 12:26:43+10:00
next:
  text: Metaphors and organisational change
  url: /blog/2015/02/06/metaphors-and-organisational-change/
previous:
  text: Learning analytics is better when.....?
  url: /blog/2015/02/02/learning-analytics-is-better-when/
title: '"Concrete lounge #1 - Helping learners find correct, up-to-date course information"'
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Kludging an authoring process with Moodle books (almost) | The Weblog of
        (a) David Jones
      author_email: null
      author_ip: 192.0.80.104
      author_url: https://davidtjones.wordpress.com/2015/02/08/kludging-an-authoring-process-with-moodle-books-etc/
      content: '[&#8230;] outlined in a previous post and shown in the following screenshot
        my course uses &#8220;Moodle books&#8221;. Each Moodle book [&#8230;]'
      date: '2015-02-08 13:13:47'
      date_gmt: '2015-02-08 03:13:47'
      id: '1217'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: And the little one said, &#8220;roll over, roll over&#8221; | The Weblog
        of (a) David Jones
      author_email: null
      author_ip: 192.0.81.50
      author_url: https://davidtjones.wordpress.com/2015/06/26/and-the-little-one-said-roll-over-roll-over/
      content: '[&#8230;] semester I implemented a &#8220;macro&#8221; system. Initial
        implementation had it working just for the semester 1 site. Time to update it
        to work with [&#8230;]'
      date: '2015-06-30 11:33:45'
      date_gmt: '2015-06-30 01:33:45'
      id: '1218'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: Nature of digital technology? Part 2 &#8211; expansion &#8211; The Weblog
        of (a) David Jones
      author_email: null
      author_ip: 192.0.82.14
      author_url: https://davidtjones.wordpress.com/2016/06/29/nature-of-digital-technology-part-2-expansion/
      content: '[&#8230;] the use of digital technologies (and probably beyond). For example,
        my work at doing something with the concrete lounges in my institution&#8217;s
        LMS. But at this stage we&#8217;re starting to enter the area of [&#8230;]'
      date: '2016-06-29 09:16:07'
      date_gmt: '2016-06-28 23:16:07'
      id: '1219'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The following is (hopefully) the first in a growing [list of concrete lounges](http://fedwiki.djon.es/view/welcome-visitors/view/list-of-concrete-lounges) that I've faced in institutional e-learning. The [concrete lounge metaphor](http://fedwiki.djon.es/view/welcome-visitors/view/concrete-lounge) is my attempt to explore the reality of university e-learning, to illustrate some possible reasons why it continues to be so wrong, and see what can be done to address those reasons.

The other main reason for sharing what I'm doing. Perhaps some of this might be useful to other, but more importantly I'm hoping to find out what others have done/think and thereby discover better ways to live with the concrete lounges that institutions are providing for learning and teaching.

The following covers

1. Task - what learning/teaching task am I struggling with.
2. Context - within which I'm struggling.
3. Concrete lounge - a list of the tools provided by the institution to fulfill this task - including:
    - No search engine
    - Topic-based sites and course-wide information
    - Scroll of death
    - Keeping information up to date
4. Bricolage - the tinkering and kludges I've put in place to live with the concrete lounges.
5. Factors - some random, incomplete thoughts about what is behind all this.

## Task

The task this post focuses on is

> Helping learners find correct, up-to-date course information

Information such as what they should be doing each week, what is the assesment, when is it due etc. Both learning and administrative information. If students can't find this information it impacts their learning.

There are suggestions that finding such information at my current institution is a concern that has driven [some institutional practices](/blog/2015/01/20/what-might-the-3-levels-of-organisational-culture-reveal-about-university-e-learning/).

## Context

I have complete this task in the following context.

A 3rd year course taken by all Bachelor of Education students. A course that is offered twice a year. S1 offering with around 300 students both on-campus and online (150+). The S2 offering with around 100 students all online.

The course breaks the semester up into four modules. Each module consisting of a number of weeks as shown by the study schedule below.

[![studySchedule](images/16135176729_054efae82e.jpg)](https://www.flickr.com/photos/david_jones/16135176729 "studySchedule by David Jones, on Flickr")

Moodle as the LMS. Each topic on the course home page equates to a week of semester. Each week consists of a "learning path". i.e. a list of basic activities and resources that are designed to get the students started in their learning. The following image shows the learning path for week 1.

[![Week1](images/16315335515_b91c408c98.jpg)](https://www.flickr.com/photos/david_jones/16315335515 "Week1 by David Jones, on Flickr")

Each learning path makes use of the Moodle book plugin (look for the green book like icons next to elements in the above image) to guide students through the learning path. Each Moodle book tends to be focused on a specific task and generally is wrapped around external resources. For example, the "Toolbelt Theory" book in the above prepares the students to read [this post](http://speedchange.blogspot.com.au/p/blog-page_2046.html) and engage in a number of activities. Including the use of Diigo to share thoughts on the post with others in the course).

## Concrete Lounge

The following identifies the limitations and problems that arise from the technologies provided by the institution. Some of these problems are huge barriers, some require a bit of creative tinkering that may or may not be immediately visible to many folk.

### There is no search engine

Even though I don't provide a lot of information in the Moodle books mentioned above. There still remains a fair bit of information that is provided on the course.

**Moodle - as installed at my institution - does not provide a search engine!!!**

This is the standard mechanism for finding information on the web. Students can't use it on a course site.

### Topic-based Moodle course sites and general information

A Moodle course home page can only use a given [list of formats](https://docs.moodle.org/27/en/Course_formats). The most [common formats](https://docs.moodle.org/27/en/Course_formats#Standard_course_formats) are to structure the course either by topic or week. Essentially a sequence of topics/weeks each containing a collection of activities/resources related to that topic/week.

This raises the question of where to put activities/resources that are important to the course, but are not specific to a particular topic/week. In my course such information includes: the study schedule overview, assessment information, information about the teaching team, a link to register/track blog contributions and a couple other.

This is information that the students will need multiple times throughout the semester and should be able to find it quickly. The following image shows off a remnant of my initial solution - look at the "Course Content" block in the middle of the page and the links it includes.

[![Home page](images/15957952599_594365d7d9.jpg)](https://www.flickr.com/photos/david_jones/15957952599 "Home page by David Jones, on Flickr")

You may also see from the above image that there is also a quite prominent menu in the left-hand column. A menu that appears to point to some of the same information (e.g. study schedule, assessment). This is a new feature of the institutional theme for Moodle that has been rolled out by my university.

It does help address this problem. But amongst other problems I've [discussed earlier](/blog/2015/01/20/what-might-the-3-levels-of-organisational-culture-reveal-about-university-e-learning/) this particular prominent menu provides no scope to add course specific general information. For example, I can't add a "Register blog - check posts" link.

### Scroll of death

The [scroll of death](http://www.markdrechsler.com/?p=720) is a rather well-known problem with Moodle course sites. If you're using the topic/week course format and your course has 10+ topics/weeks and each of those topics/weeks have a list of activities/resources, then your course home page is going to be quite long. This requires students to scroll on and on down the page to find where they are and what they should be doing next.

### Keeping information up to date - problem

My course is offered twice a year. Institutional policy means that we're unable to make major changes to the course (especially the assessment) within a calendar year. Workload implications (such as dealing with concrete lounges) mean that even when I do make changes, those changes tend to be evolutionary, rather than revolutionary. Tweaking what's already there, rather than a holus bolus replacement.

Which means my first step in preparing for a new semester (like many, many other academics) is to migrate the last course site across to the new semester's course site.

The problem is that littered throughout all of the course information is a range of information that I

1. have to change; and, e.g. assessment due dates, the dates associated with each week of semester.
2. some that I might like to change. e.g. The title for a week. The name and email address of the person in charge of the course. etc.

The problem is that this information is not located in one place. It is littered throughout the course site. For example, the due date for an assignment can be found on the: study schedule, the assessment overview, the assignment page for that assignment, and an ad hoc collection of pages in Moodle books designed to help students prepare the assignment.

As it stands, I need to manually find (remember, no search engine) and replace all occurrences of this information.

## Bricolage

Here's an overview of the various workarounds I've employed to address the limitations of this concrete lounge.

### No search engine

In the past - as explained [in this post](/blog/2014/02/25/evernote-as-a-solution-to-a-moodle-problem/) - I have manually imported most of the course content into Evernote and made it [open to the public](https://www.evernote.com/pub/davidthomjones/edc3100ictandpedagogy-2014#st=p). This allows the use of the simple search engine provided by Evernote.

I won't be doing this in the future. It's too much work and difficult to keep the information in Evernote aligned with what's in the course site. I believe it's also somewhat difficult for students to connect this search result with what's in the course site.

### Topic-based moodle sites and general information

The image below shows the original solution I used (which is echoed in the image above).

A hand-coded bit of HTML is placed in the general section at the top of the course site. The HTML points students to the general information. The HTML is styled to align with the institutional look and feel. As you can see, it also takes up more vertical space contributing somewhat to the scroll of death.

[![edc3100 2014](images/15692340534_2b5437ee13.jpg)](https://www.flickr.com/photos/david_jones/15692340534 "edc3100 2014 by David Jones, on Flickr")

As noted above, the institution has rolled out a new look and feel that includes a menu designed to help students find general information. In a perfect world, I'd make use of that menu to point students to the course specific information. Especially the study schedule and assessment information.

Whilst the institutional implementation doesn't support this type of customisation. It is possible through the use of jQuery (a part of the new institutional look and feel). However, the use of this approach is apparently seen as a potential breech of policy.

Time will tell.

### Scroll of death - implementation

The following shot of the next course site shows the addition of "skip navigation" for the weekly learning paths. Near the top of the page the students see an overview of the weeks of semester and can jump directly to the learning path for that week. Each of the links within the skip navigation has a tooltip that tells the student the topic for that week and the dates for that week (the dates are new and are possible due to the tinkering described in the next section). An attempt to help figure out where they were or should be up to.

[![tooltip](images/16406027186_2a4210be9a.jpg)](https://www.flickr.com/photos/david_jones/16406027186 "tooltip by David Jones, on Flickr")

### Keeping information up to date - solution

The skip navigation in the previous screen shot, the study schedule shown above, and the week 1 learning path (also shown above) all display the title given to a week of semester and the dates for that week of semester. Traditionally, I've had to manually change all of this information. No longer.

I've now implemented a [simple "macro" facility](/blog/2014/01/22/a-moodle-course-site-wide-macro-facility/). This has been done by

1. Create a small jQuery/javascript file that
    1. Defines a range of variables and their values. 
```javascript 
var VARIABLES = { 
    // Teaching staff CE\_NAME: "David Jones", CE\_EMAIL: "david.jones@usq.edu.au",
        
    // Weeks W0\_PERIOD:"Before 2 Mar", W0\_TITLE: "Orientation and getting ready",
        
    W1\_PERIOD:"2-6 Mar", W1\_LABEL: "Week 1", W1\_TITLE: "ICT, PLNs and You", 
```
    3. Will perform a search on a web page once it has loaded into a browser, and replace any occurrence of a variable (e.g. _W0\_PERIOD_) with the value (e.g. _Before 2 Mar_).
2. Include that file in any Moodle page that contains this type of information.
3. Replace the "hard-coded" information with an appropriate variable. 
```html 
<!-- this --> Jump to: Week: <a href="#1" title="ICT, PLNs and You">1</a> | <!-- becomes -->; Jump to: Week: <a href="#1" title="\{\{\{W1\_TITLE\}\}\} - \{\{\{W1\_PERIOD\}\}\}" class="dj\_title">1</a> | 
```

!!! note ""

    Due to the pain in making these modifications each semester the period for a given week was never included in the skip navigation. It was too much work to manually update each link in the skip navigation. However, with this functionality I only need to enter the variable once.

Next semester, all I'll need do is create a new version of the VARIABLES containing the new semesters values. Changing this one file will then automatically ensure that it is change on all the pages that use this.

Two interesting issues I'm waiting for

1. Will this use of jQuery generate any backlash from institutional management? The very fact that this is my first question says something about the context.
2. What problems will this kludge generate in terms of students browsers? Will all browsers support this use of jQuery. Seems to work on iPads and modern computer browsers. But 300+ students will almost certainly create an issue.

## Factors

This is just an initial stab. Needs more work.

The argument we made in [this paper](/blog/2014/09/21/breaking-bad-to-bridge-the-realityrhetoric-chasm/) was that the reason why this concrete lounge exists (and also the reason why I'm able to make these changes) is that university e-learning at the institutional level is informed by a [SET mindset](/blog/2014/09/21/breaking-bad-to-bridge-the-realityrhetoric-chasm/#badset) whereas my practice is more informed by a [BAD mindset](/blog/2014/09/21/breaking-bad-to-bridge-the-realityrhetoric-chasm/#badset).

The institutional practice is driven by strategic aims. Important institutional projects (such as the new institutional look and feel for Moodle) are the focus. It's what everyone is meant to work toward. Anything that doesn't fit within the strategic aims is seen as bad or below notice. A strategic project has to work at the level of the entire organisation, and not a the level of an individual course.

I'm not sure that the "keeping information up to date" is a problem that many of those involved in the strategic projects are aware of. If they aren't aware of it, they can't solve it.

But even if they are aware of it, it has to be seen as a problem for everyone and as a problem that can be solved within the available resource constraints.

The solution I've adopted for the "keeping information up to date" is - as it stands - an solution that just anyone could adopt. Transforming that solution into something that could be used across the institution would require a significant mindshift on a number of fronts from those involved centrally.