---
categories:
- edc3100
date: 2015-01-21 08:42:39+10:00
next:
  text: '"Barriers to higher education technology adoption: Digital fluency or usefulness?"'
  url: /blog/2015/01/21/perceived-usefulness-is-the-most-influential-factor-on-intention-and-actual-use/
previous:
  text: What might the 3 levels of organisational culture reveal about university
    e-learning
  url: /blog/2015/01/20/what-might-the-3-levels-of-organisational-culture-reveal-about-university-e-learning/
title: Learning to live with a standard look and feel
type: post
template: blog-post.html
---
**About** \- this is an old post (2015) that was never posted. Posting it now for other reasons.

The following outlines experiments and steps taken to live with the dissonances that arise from the implementation of a new institutional look and feel for course sites. The background to this work is documented in [this blog post](/blog/2015/01/20/what-might-the-3-levels-of-organisational-culture-reveal-about-university-e-learning/) which ends with the following questions that I try to answer:

1. Can I change the study schedule and assessment links to my existing approaches?
2. Can I remove the resources link?
3. Can I implement a macro/API system to insert USQ information?
4. What can and might I do around providing a search engine for the course site?

## Jquery to modify links

The first two questions cry out for a bit of javascript modification. Javascript is just one of the more recent web technologies of which I have only passing knowledge.

The menu links have unique classes

- study schedule is "link-studyschedule"
- assessment is "link-assessments"
- resources is "link-resources"

A quick Google search revealed this [post on StackOverflow](http://stackoverflow.com/questions/1933602/how-to-getelementbyclass-instead-of-getelementbyid-with-javascript) that includes an answer with the following approach \[code lang="html"\] <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js"></script> <script type="text/javascript"> $(function(){ $(".classname").hide(); }); </script> \[/code\]

It uses a Google provided jquery source file to enable the use of Jquery. Adding something like this to the top of a Moodle page will hide the link. Quick search for a bit more jquery process and all done. In 10 minutes I've implemented something that would work, but there's one problem.

### Adding it to every study desk page

This only works if the javascript injection is on every page on the study desk. Every page I migrate in (all of those Moodle book chapters would require manual copy and paste) and every page produced by a Moodle plugin (e.g. quiz, discussion forum etc). This is troubling and potentially limiting to what I can do.

If I really wanted to, I could do the manual insertion. But not the quizzes, discussion forums.

The Moodle way would be to include this in the theme. However, I believe that the USQ look and feel is implemented as a site wide theme. Changes specific to a course are not likely to be high on the agenda, let alone organisationally doable. Moodle does allow the notion of course specific themes, but that would require the USQ powers that be to allow this and then enable the creation of a EDC3100 specific theme that used the new look and feel plus my Javascript.

Not likely to happen.

### Adding a redirect + adding to some pages

One option/kludge would involve a combination of injecting the javascript on those pages that I can; and setting the official pages for assessment and study schedule to redirect to where I want them to be. So anyone who finds there way to the page would get sent elsewhere.

It's a questionable approach. It also depends on being able to insert some javascript on the new look and feel's assessment and study schedule pages.

Which you can't. It appears that they've implemented something that prevents javascript inserted into assessment items from being included on the page displayed. Not that surprising, but a pain.

Which suggests that engaging the hierarchy will be required. Oh fun.

## A simple template system

Each of the weekly learning paths on the course site are placed into a topic. Each topic has a label that includes the title of the learning path and the dates for the week in which it is meant to apply. In the image below you should be able to see the "21-25 Jul (Week 1)" near the top of the image.

[![Week1](images/16315335515_b91c408c98_s.jpg)](https://www.flickr.com/photos/david_jones/16315335515 "Week1 by David Jones, on Flickr")

The problem is that this is a screen shot from the Semester 1, 2015 offering of the course. The appropriate date is not 21-25 Jul for this learning path.

The same problem exists with the study schedule as shown in the following image. The August dates are not appropriate for these weeks.

[![studySchedule](images/16135176729_054efae82e_s.jpg)](https://www.flickr.com/photos/david_jones/16135176729 "studySchedule by David Jones, on Flickr")

Each semester, as the course is copied over, I need to manually update these dates and hope that I get them all. The time it takes to do this reduces the amount of time I spend on make truly important changes to the course.

The advantage of the study schedule in the new look and feel is that it does pull the dates for the weeks and includes them automatically. The problem is that it requires you to constrain yourself to the remaining functionality the study schedule page provides.

The aim here is explore whether it's possible to use some Javascript to fix this problem. In summary the plan is to

1. Create a javascript data structure summarising the dates for each week of semester.
2. Replace the hard-coded/explicit week dates (i.e. 11-15 Aug) in the study schedule and the topic titles with a variable. The most likely approach will be to use a simple div such as \[code lang="html"\] <div id="WEEK\_4\_DATE"></div> \[/code\] This means that if this template approach doesn't work, there will just be an empty slot. Not something ugly.But of course the topic headings won't take HTML so the DIV option is out.
3. Have a function that does a search and replace for the variables.

With all three of these in a page, the dates should just be added in. The advantage is that next semester all I need to do is change the data structure and all the pages will be automatically updated.

Oh dear, there's a slight bug in the due dates in the new look and feel. Week 9 is listed as "27-1 April" i.e. 27 April to 1 April. It should be "27 April-1 May". Will have to report that.