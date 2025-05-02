---
title: "#moodle Activity Viewer (MAV) and the promise for bricolage"
date: 2014-02-02 12:01:49+10:00
categories: ['elearning', 'thesis']
tags: ['mav']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: 'MAV, #moodle, process analytics and I&#8217;m an idiot | The Weblog of
        (a) David Jones'
      author_email: null
      author_ip: 192.0.83.120
      author_url: https://djon.es/blog/2014/02/03/mav-moodle-process-analytics-and-im-an-idiot/
      content: '[&#8230;] currently analysing the structure of a course I teach and have
        been using @damoclarky&#8217;s Moodle Activity Viewer to help with that. In the
        process, I&#8217;ve discovered that I&#8217;m an idiot in having missed [&#8230;]'
      date: '2014-02-03 13:24:46'
      date_gmt: '2014-02-03 03:24:46'
      id: '939'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: Analysing EDC3100 using MAV | The Weblog of (a) David Jones
      author_email: null
      author_ip: 192.0.82.170
      author_url: https://djon.es/blog/2014/02/03/analysing-edc3100-using-mav/
      content: '[&#8230;] that I have the Moodle Activity Viewer (MAV) working, I can
        continue the analysis of the course I teach, EDC3100, ICTs and Pedagogy. This
        post [&#8230;]'
      date: '2014-02-03 15:22:39'
      date_gmt: '2014-02-03 05:22:39'
      id: '940'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: 'Does GPA make any difference to #moodle course usage? | The Weblog of (a)
        David Jones'
      author_email: null
      author_ip: 66.155.8.72
      author_url: https://djon.es/blog/2014/02/20/does-gpa-make-any-difference-to-moodle-course-usage/
      content: '[&#8230;] the Moodle Activity Viewer installed, I have one way to explore
        the usage question for a past course site. To be [&#8230;]'
      date: '2014-02-20 13:50:06'
      date_gmt: '2014-02-20 03:50:06'
      id: '941'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: Does my course suffer from semester droop? | The Weblog of (a) David Jones
      author_email: null
      author_ip: 66.135.48.198
      author_url: https://djon.es/blog/2014/05/09/does-my-course-suffer-from-semester-droop/
      content: '[&#8230;] Created two views of the S2, 2013 EDC3100 course site using
        MAV [&#8230;]'
      date: '2014-05-09 10:09:36'
      date_gmt: '2014-05-09 00:09:36'
      id: '942'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: A perspective on why institutional e-learning is so bad | The Weblog of
        (a) David Jones
      author_email: null
      author_ip: 76.74.255.5
      author_url: https://djon.es/blog/2014/09/22/a-perspective-on-why-institutional-e-learning-is-so-bad/
      content: '[&#8230;] via a web browser running on my laptop. It&#8217;s a personal
        solution. It is based on a particular set of technologies developed by and currently
        being used at CQUni for a strategic project around [&#8230;]'
      date: '2014-09-22 15:26:25'
      date_gmt: '2014-09-22 05:26:25'
      id: '943'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
I've spent the last few days - on and off - getting [the Moodle Activity Viewer](http://damosworld.wordpress.com/2013/08/30/the-moodle-activity-viewer-mav-heatmaps-of-student-activity/) installed on my local Moodle instance. There were two main reasons for doing this

1. Analyse how students were using my 2013 course sites.
    
    This will be the topic of later posts.
    
2. Lay the foundation for exploring MAV as a platform for bricolage.
    
    This is the topic of this post.
    

## Rationale

Over recent months I've heard various statements of the form "We know all there is to know about online learning and teaching". Statements that reflect the perspective that the provision of quality learning and teaching at universities is a tame problem. It typically arises from experts - be they instructional designers or information technologists - and from people in "leadership" positions. Those in "leadership" positions seem increasingly convinced that leadership is the design of a single solution/vision to a problem and the successful implementation of that vision.

The problem is that by seeing "quality learning and teaching" as a tame problem they believe that it can be ["solved in a linear fashion using straightfoward, reductionist, repeatable, sequential techniques"](http://www.drbrd.com/problems_and_solutions/three_types_of_problems.html). As a consequence, you get the organisational decomposition of skills into different organisational units. This decomposition prevents connections between the disparate knowledge bases of technology, pedagogy, content and context. The difficulty (impossibility) of making these connections limits the capability of organisational learning and teaching to learn and improve.

What's worse is that the "tame problem" perspective results in the adoption and perception of technologies (e.g. the LMS) as immovable. This results in the situation where if the technology doesn't well support a particular pedagogy, then you better change the pedagogy because changing the technology is too hard. Again limiting the capability of organisational learning and teaching to learn and improve its practice. It also leads to the problem identified by Ciborra (2002)

> ..if every major player in the industry adopts the same or similar applications, any competitive advantage evaporates.

On a more personal level, all of this results in crappy systems that don't actively help me improve the learning of my students.

For me, using technology to improve learning and teaching is [a complex or wicked problem](http://www.drbrd.com/problems_and_solutions/three_types_of_problems.html). The type of problem where lots of small scale, rapid experiments are the best way forward. The infrastructure underpinning MAV seems to be the best current foundation to enable this.

## How MAV works

MAV is a plug-in for the Firefox plugin that communicates with a MAV server that provides access to a database. It enables the modification of a web page produced by Moodle. Currently it will modify a Moodle course page by adding a heatmap representing how particular groups of students have used the resources and activities on the course page.

It changes something that looks like this

[![Without heat map by David T Jones, on Flickr](http://farm4.static.flickr.com/3777/12260329933_0e2c46119a_m.jpg "Without heat map by David T Jones, on Flickr")](http://www.flickr.com/photos/david_jones/12260329933/)

Into something that looks like this

[![EDC3100 S2, 2013 - heat map by David T Jones, on Flickr](http://farm3.static.flickr.com/2887/12259211486_913cefea74_m.jpg "EDC3100 S2, 2013 - heat map by David T Jones, on Flickr")](http://www.flickr.com/photos/david_jones/12259211486/)

Now this is somewhat useful for a teacher wanting to understand how various aspects of a course site have been used (or not). It can be argued that this information is available via other means (e.g. Moodle's activity report), but I'd suggest that the in-situ, colourful representation provided by MAV provides some additional affordances that the activity report doesn't provide.

MAV does this using the following process

1. I visit my course's home page in Moodle.
2. MAV recognises this as a Moodle course page and adds an "Activity Viewer" option to the Moodle settings.
3. If I've turned MAV on, MAV then sends a request to the MAV server asking for how many students or clicks there have been on all of the links on the course page.
4. The MAV server queries a copy of the Moodle database and sends the results back to MAV.
5. MAV changes the background colours for all of the links (or it can change the size of the text) to represent usage. MAV also adds some text with the actual number of clicks or students.

But MAV's real strength isn't what it currently does, it's how it could be used to support bricoloage.

## It's on my computer

The version of MAV that produced the above screen shots is running on my computer. The server is running on my computer. This means that I can write extensions to MAV to solve the problems I encounter when trying to support 300+ students in a course. If I come across a problem during semester, I currently have three options:

1. engage in the heavy-weight processes associated with trying to get something changed in these systems (which probably won't be able to be changed anyway); or
2. implement some manual work around to solve the problem;
    
    e.g. create a zip file for each of the 60 assignments I marked and manually upload each one individually into the system.
    
3. make do without.

For example, the pre-service teachers who take my course come from a range of sectors including early childhood, primary, middle years, secondary (content specialisations) and vocational education. The type of response I should give to a question can depend on the pre-service teacher's sector. The Moodle discussion forum will tell me the name of the person who asked the question, but it doesn't provide any other information. In fact, it can't because information about a pre-service teacher's sector is very specific to Bachelor of Education students and so is not part of the information from the university's student records system that is inserted into Moodle.

It should be fairly easy to write a MAV extension that whenever it sees a student's name, adds to the name the student's sector. Perhaps even a mouse-over that shows a range of information about the student, perhaps including some personal annotations I've made about the student. Perhaps documenting (and reminding me of) the various unique complications that impinge on the lives of my students.

With MAV (and my capabilities), I can implement this modification without having to engage in the heavy-weight institutional processes. I can engage in [bricolage](http://en.wikipedia.org/wiki/Bricolage#Information_systems).

This example probably doesn't excite the learning theorists or instructional designers. It doesn't offer any large change in the fundamental practice of pedagogy supported by an appropriately convoluted theoretical framework. It's somewhat prosaic, simple, and only a very small change. But then such people don't really get the concept of complex adaptive systems and bricolage (see below).

### An aside on requirements gathering

I almost didn't include the "pre-service teacher sector" example above. I found myself not being able to think of an example about how I might use MAV. This is not indicative of there not being a need for this sort of approach. It is indicative of limitations of human cognitive capabilities/memory and the stupidity of the assumptions underpinning traditional requirements gathering processes.

My difficulty in identifying example arises from the observation that I'm not currently teaching the course. Asking for requirements when I'm not engaged in an activity, is always going to result in significantly fewer and less detailed requirements than asking me while I'm engaged in the activity or actively observing me. And yet, how do organisations gather requirements for new systems? Months or years before people actually start using the system, they ask people, "What would you like to do with this system?"

## The value of bricolage

Of course bricolage is always frowned upon by organisational folk. Bricolage is messy. It can lead to the ultimate evil in organisational IT - [shadow systems](http://en.wikipedia.org/wiki/Shadow_system).

But there is another perspective, again from Ciborra (2002)

> If these approaches look rough compared to neat and tidy formal procedures, they are on the other hand highly situated: they tend to include an added element of ingenuity, experience, and skill belonging to the individual and their community (of practice) rather than to organizational systems. Finally, they all seem to share the same way of operating: small forces, tiny interventions, and on-the-fly add-ons lead, when performed skilfully and with close attention to the local context, to momentous consquences, unrelated to the speed and scope of the initial intervention. These modes of operation unfold in a dance that always includes the key aspects of localness and time (the 'here and now'); modest intervention and large scale effects; on-the-fly appearance but deeply rooted in the personal and collective skill and experience

And drawing on research projects into Strategic Information Systems, Ciborra (2002) goes onto argue that

> The capacity to integrate unique ideas and practical design solutions at the end-user level turns out to be more important than the adoption of structured approaches to systems development or industry analysis

and more directly for those who know the answers

> All these cases recount the same tale: innovative, strategic applications of IT are not fully designed top-down or introduced in one shot; rather they are tried out through prototyping and tinkering. In contrast strategy formulation and design take place within pre-existing cognitive frames and institutional contexts that usually prevent designers and sponsors from seeing and exploiting the potential for innovation hidden in the artefacts....SISs (strategic information systems) emerge when early adopters are able to recognize, in use, some idiosyncratic features that were ignored, devalued, or simply unplanned.

## References

Ciborra, C. (2002). The Labyrinths of Information: Challenging the Wisdom of Systems. Oxford, UK: Oxford University Press.