---
title: "Re-using a #moodle course design"
date: 2015-07-04 16:25:51+10:00
categories: ['eds4406', 'moodle']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

This semester I'm course examiner for a new course on [Secondary Computing Curriculum and Pedagogy](http://www.usq.edu.au/course/specification/2015/EDS4406-S2-2015-WEB-TWMBA.html). As the name suggests, the course is intended to help pre-service teachers who are aiming to teach computing in Secondary schools. While I'm the course examiner, the course is being developed and will be largely taught by a couple of practicing and experienced Secondary computing teachers (how's that for "recency of practice"?).

Two weeks before semester start my institution opens up the course sites for students to become familiar with what's on offer. There are some minimum expected standards to meet. My task today is to meet those standards and in doing so set up the skeleton of the course site for the rest of the semester. To do this I'm going to reuse the structure from EDC3100, perhaps with a few tweaks. Besides saving me some time, four of the five students currently enrolled in the course have done EDC3100.

This is also a bit of an exploration of the difference between an empty Moodle course site (even one with a standard look and feel) and one with a structure.

## What I'll need to do

Can I list all I need to do

- Structure of the site
- Study Schedule
- Assessment
- Teaching team
- The initial orientation message.

### Structure

The basic structure is going to match the EDC3100 template. A collection of topics tied directly to each week of semester with a "jump to" bar at the top of the course site. There will also be a collection of "adminstrative" topics.

The following image shows the top of the 2012 version of the EDC3100 site. In 2015 the institution has adopted a default course structure that does away with the need for the "Course Content" and "Course Background" boxes.

[![Welcome](images/6859813387_bbb7cc8890.jpg)](https://www.flickr.com/photos/david_jones/6859813387 "Welcome by David Jones, on Flickr")

The one question about this approach is that EDC3100 has quite a bit of content in each week. Not sure that EDS4406 will have the same quantity. Hence the separate topics for each week may be a bit of overkill.

As it stands each topic does have a formal title meaning it's probably valuable to make use of [the macro facility](/blog2/2015/06/26/and-the-little-one-said-roll-over-roll-over/) I'm using in EDC3100.

Process setting this up includes

1. Copy the "course format" used in EDC3100. "Weekly format" with 12 sections. 10 teaching weeks + an orientation and a "resource" week.
2. Update the names of each section/topic/week of the course. Using the macro facility the names entered into a moodle are in this form ```**\{\{\{W0\_TITLE\}\}\} (\{\{\{W0\_PERIOD\}\}\})**```. A bit of Javascript will replace the "variables" with appropriate values.
3. Put in place the Javascript file to do the translation. I'll create a new one for this course. Copy the EDC3100 js file across and update the values. Week titles first. That's all done. The problem with week numbers changing because of holidays reared it's head again.
4. Stick in the "jump to" Oh, that was nice. Copy the HTML from EDC3100, replace the course id, paste it into the EDS4406 site, and hey presto it all works. Even the tooltips get updated with the new topic names.

### "Administrative" content - Study schedule, assessessment, and teaching team

These three sections are important but don't form part of the students' weekly learning activities. The institutional default course structure provides default tools for display this information, but IMHO they aren't as useful as using a Moodle book to provide course specific information.

At this stage, the detailed information for these sections isn't yet written, I'll just be putting in the initial skeleton. That involves

1. Creating a Moodle book resource for each section.
2. Updating the js file to point the default course structure links to these books.
3. Put in some basic information into the books.

Again the macro system is nice. Copy and paste some HTML from the EDC3100 book that is using the macro approach. Link in the EDS4406 js file and the content automagically updates to EDS4406 information.

### Orientation message

This will need to be a little more than a message. Will work on that tomorrow and update this.