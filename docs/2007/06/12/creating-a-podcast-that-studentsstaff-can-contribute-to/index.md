---
title: Creating a podcast that students/staff can contribute to
date: 2007-06-12 20:34:17+10:00
categories: ['web-20-course-sites']
type: post
template: blog-post.html
---
One of the requirements in the Web 2.0 course site for Creative Futuring is to have a podcast that both students and staff can contribute to. The intent is not so much that they will create their own resources but that they will tag interesting podcast episodes that they come across on the web.

The plan is for the students to be already using [Del.icio.us](http://del.icio.us) so it seemed sensible to me that there should be a way to harness that existing process. A little Googling reveals this [approach](http://weblogg-ed.com/2005/delicious-and-podcasting/) using Feedburner. What follows is my trial at using this approach.

## Setting it up

Following the above approach this is what it takes to set the "infrastructure" up.

### Identify the source

Sticking with the course site idea I'm using the mp3 files I created during the second half of 2006 when teaching the course [COIS20025, Systems Development Overview](http://webfuse.cqu.edu.au/Courses/2006/T2/COIS20025/). The mp3 files are part of the [lecture slides page](http://webfuse.cqu.edu.au/Courses/2006/T2/COIS20025/Resources/Lecture_Slides/)

### Tag with del.icio.us

Using "ctrl-click" (right click on a Windows box) while hovering over a link to an MP3 file I select "Tag this Link". This only works because I've got the del.icio.us plugin installed.

I decided to use the tag "cois20025-pod" which results in [this del.icio.us page](http://del.icio.us/davidj1/cois20025-pod).

Initially I just tagged it, but obviously using an appropriate name and description would result in better information within the podcast, so I went back and edited some of that.

### Burn the feed

Visit [Feedburner](http://www.feedburner.com/) put in the URL for [the del.icio.us page](http://del.icio.us/davidj1/cois20025-pod) for the cois20025-pod tag and FeedBurner auto picks up the RSS feed I want.

Get an account and enter in various additional "podcast" information, choose what traffic statistics I want.

All finished and you have a feed that can be subscribed to in iTunes or your choice of podcast software.

The feed for this experiment is [http://feeds.feedburner.com/Delicious/davidj1/cois20025-pod](http://feeds.feedburner.com/Delicious/davidj1/cois20025-pod)

## How would this work for students/staff

All of the above would not have to be done by students or staff. The configuration/setting up process above is what the support staff would do (though academic staff could do it themselves if they wished).

The requirements for staff/students would be

- Have the del.icio.us plugin installed into their browser
- Have an understanding of how to use it
- Know what tag to use to tag resources to add to the podcast
- Know how to subscribe to that podcast

Much of this information could be provided by the course website resources page and backed up with support in class.

During the course they would have to

- Remember to tag what they think is relevant
- Keep an eye on the podcast in iTunes or equivalent