---
title: Setting up an Excel checklist
date: 2016-03-10 17:30:02+10:00
categories: ['edc3100']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Setting up the analysis of student submissions &#8211; The Weblog of (a)
        David Jones
      author_email: null
      author_ip: 192.0.113.171
      author_url: https://davidtjones.wordpress.com/2016/03/29/setting-up-the-analysis-of-student-submissions/
      content: '[&#8230;] couple of weeks ago I wrote this post outlining the design of
        an Excel spreadsheet EDC3100 students were asked to use for their first [&#8230;]'
      date: '2016-03-29 14:33:05'
      date_gmt: '2016-03-29 04:33:05'
      id: '3325'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: Planning changes to EDC3100 assignment 1 &#8211; The Weblog of (a) David
        Jones
      author_email: null
      author_ip: 192.0.83.191
      author_url: https://davidtjones.wordpress.com/2016/07/13/planning-changes-to-edc3100-assignment-1/
      content: '[&#8230;] the first half of the year there was a new assignment in EDC3100
        designed to both enhance student learning, but also experiment with making the
        data [&#8230;]'
      date: '2016-07-13 13:19:31'
      date_gmt: '2016-07-13 03:19:31'
      id: '3326'
      parent: '0'
      type: pingback
      user_id: '0'
    
---

See also: [[blog-home | Home]]

For a brand new first assignment for EDC3100 the students are being asked to find a lesson plan that uses digital technologies to enhance learning (ICT and Pedagogy), and evaluate it against a checklist. The following documents my explorations about how to set up this checklist.

### **Current status**

Have [test version](https://dl.dropboxusercontent.com/u/14025788/edc3100/2016-S1/Assessment/1/EarlyTest.xlsx) that appears to be working. Need to test it on different platforms. A task for tomorrow.

If you're an EDC3100 student, then do try [downloading it](https://dl.dropboxusercontent.com/u/14025788/edc3100/2016-S1/Assessment/1/EarlyTest.xlsx) and taking a look, is it going to work for you?  Remember, it is an early test.  Need to do more testing myself.

### Why?

The rationale for this assignment includes the following:

1. Broaden the students' awareness of what is possible with (ICT and Pedagogy).
2. Make them aware of some ways to evaluate how ICT and Pedagogy is being used.
3. Help them question just how they can use a resource they found online
4. Create a "database" of information that I can analyse.

The last point may not sound all that educational, but the hope is that the ability to be able to "mine" (i.e. the ability to use digital technologies to analyse the data) the students' responses and the markers' judgements around this task will enable a range of new practices that will enhance/transform learning and teaching.

Some initial examples of what might be possible

- Pre-marking checks. e.g. students are required to include a URL to a lesson plan. A program could check that the URL is actually correct. In a perfect world, it would warn the student before allowing them to finalise submission - but the LMS isn't flexible enough for that.
- Marker allocation. e.g. if I one of the markers has an interest mathematics, allocating her all of the maths related evaluations might be a good idea.
- Supporting moderation and providing summary feedback. e.g. after marking, a program could analyse how all the students have performed and generate summary feedback. Feedback that could be used to inform the moderation process and also to provide students an overall picture of how everyone went.
- Providing a shareable database of evaluated lesson plans. The assignment has 300+ students finding a lesson plan and evaluating its use of ICT and Pedagogy. These evaluations are then marked by practicing teachers. In an environment where there is abundant information, these evaluations might help focus attention on the what's actually "good". e.g. here's a list of all the lessons that transform (as per [the RAT framework](http://doverdlc.blogspot.com.au/2013/06/the-rat-samr-transformative-technology.html)) student learning using iCT, rather than here's a list of lessons that use ICT.  At the very least, this could be useful within the course.

But before any of those is possible, I have to figure out an appropriate method to create the checklist.

## Requirements

A good method is going to meet the following requirements

1. Easy/efficient/familiar for the students to use.Students will need to:
    - check boxes; and,
    - write/copy and paste small sections of text.
2. Easy/efficient/familiar for the marker Markers will need to
    - read and understand student responses;
    - indicate right/wrong (check boxes);
    - write small sections of text (comments/feedbac);
    - make judgements against a rubric; and,
    - calculate a total
3. Work with the existing technology, including
    - Be submitted/returned via Moodle;
    - Be a format that can be analysed via programs.

The two most obvious options are an Excel spreadsheet, or a Word document. Yep, pandering to closed formats, but then most of the open formats break the first two requirements.

I am assuming that students will have access to Excel, that might be an ask. They may need to resort to Google Sheets or some other tools, the question will be whether doing this gets in the way of any script.

## What can I analyse programatically?

I should probably double check which formats I can actually write programs to analyse.

Excel works nicely - even down to the checkbox.  Word is being more difficult.

I'll go with Excel, though I may be pandering to my prejudices.

## Setting up the checklist in Excel

The requirements are:

- About 90 questions separated into four sections That might seem a bit much, but a fair number of those are covered by lists of ICT to choose what is being used.
    
    Having the different sections on different sheets could be useful.  Might also challenge the students, but that's a good thing.
- Large % of the questions are just checkboxes. Have tested that I can get that to work.
- Another portion of questions require a checkbox plus a textbox to include proof
- Small number are just a textbox
- One has a table like structure
- Marking
    - Almost all the questions have the marking indicating right or wrong What should the default value be?  Wrong or right?
    - A couple of questions require a textbox to make a judgement call
    - Would like the rubric for the assignment in the spreadsheet and for it to be auto-filled in by the marker's actions

Set up different worksheets, that's working.  Got a format that looks okay. And some questions going in.  Checkboxes.

### Can I read the test sheet from a script?

Absolutely, multiple sheets, no worries.  Looking good.