---
title: Installing Moodle - first step in BAM/MoodleAM
date: 2009-07-16 12:10:56+10:00
categories: ['bam']
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: beerc
      author_email: c.beer@cqu.edu.au
      author_ip: 118.208.40.242
      author_url: http://
      content: '"At least some of the Moodle folk are real men!"
    
    
        They would be the 40 year old virgins sitting in the corner surrounded by dilbert
        clippings ;)'
      date: '2009-07-23 17:29:28'
      date_gmt: '2009-07-23 07:29:28'
      id: '2645'
      parent: '0'
      type: comment
      user_id: '0'
    
pingbacks:
    - approved: '1'
      author: 'BAM into Moodle &#8211; Step #2: configuration and questions &laquo; The
        Weblog of (a) David Jones'
      author_email: null
      author_ip: 74.200.245.189
      author_url: https://djon.es/blog/2009/07/21/bam-into-moodle-step-2-configuration-and-questions/
      content: '[...]  It&#8217;s Tuesday, so must be time to take the next step in getting
        BAM into Moodle. Last time I got up to having Moodle checked out from CVS and
        PHP/Apache and MySQL all working nicely [...]'
      date: '2009-07-21 11:28:19'
      date_gmt: '2009-07-21 01:28:19'
      id: '2644'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
Having received [approval](/blog2/2009/07/16/bam-into-moodle-approved-starting-the-process/) to port BAM into Moodle, the first step is to get a Moodle development environment installed on my laptop. I'm meant to be getting a new one this week, however, local IT hasn't been forthcoming in when this is going to be available. Can't wait, I only have two days a week to work on this, and today is the last one this week.

### What's the advice

So, what's the advice from the Moodle community for getting started? I'm going to follow the process embedded in the [Intro to Moodle Programming](http://dev.moodle.org/course/view.php?id=2) course. What follows is some ad hoc reflections as I'm working through the course.

### Unit 1

Found the default text size on the information for "Getting started and General concepts" quite small. Must be getting old.

Okay, at least this has some description of the terminology and "structure" of Moodle, stuff I've been looking for for some time.

- Divides Moodle into "system level" and "course level".
- The interface consists of
    - sections, and  
        This is the stuff that goes down the middle of the interface and ends up with a Moodle page being one long list of stuff (bad IMHO). The content of these sections contain text or activities.
    - blocks.  
        Created by programmers, installed at a system level and then can be chosen by teaching staff to be added to a course site, usually down the left/right hand side of the page.
- Moodle modules provide the code to control instructional activities - a bit different from a block. The course focuses on block development.

Apparently Moodle is big on accessibility and there is a call for developers to pay attention to this. Not sure it's quite as big on simplicity and design....

Seems to suggest that Moodle is OO, at least points folk to OOP descriptions.

Points to a couple of tutorials that I'll need to review (mostly PHP):

- [Moodle coding guidlines](http://docs.moodle.org/en/Coding)
- [PHP](http://www.w3schools.com/php/default.asp);  
    
- [SQL](http://sqlcourse.com/).

The navigation interface to/back from this overview is not great. Using the breadcrumbs I've ended up in a different place than from where I started.

### Unit 2 - creating and working in the dev environment

:) Vim is included in the [Integrated development Environment diagram](http://dev.moodle.org/file.php/2/pictures/Unit2screenshots/vennUnit2nored.gif). At least some of the Moodle folk are real men!. There's even [guidlines for settting Vim](http://docs.moodle.org/en/Development:vim) up for Moodle development. Funny how small things make you feel better about a system.

Time to install a bunch of stuff - much of which shows how long it's been since I was a "developer":

- [Firebug](http://getfirebug.com/)
- [Selenium](http://seleniumhq.org/projects/ide/) and [Molybdenum](https://addons.mozilla.org/en-US/firefox/addon/4149) - though I'm not sure how much I'll use these.
- [XAMMP](http://www.apachefriends.org/en/xampp-macosx.html)  
    Not sure if I really want/need this. I already have versions running, perhaps this is time to move on, or at least keep Webfuse and Moodle totally separate. Yep, didn't like that MySQL was already running - mysqladmin shutdown, shutdown Apache and all is good..

Misc information

- Document root - /Applications/XAMPP/htdocs
- http://localhost/phpmyadmin/

vim configured for Moodle/PHP - first hello Moodle script created. Time for lunch.