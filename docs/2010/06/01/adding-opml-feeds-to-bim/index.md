---
categories:
- bim
- moodle
date: 2010-06-01 14:04:04+10:00
next:
  text: The role of experience
  url: /blog2/2010/06/02/the-role-of-experience/
previous:
  text: The need for a third way
  url: /blog2/2010/05/31/the-need-for-a-third-way/
title: Adding OPML feeds to BIM
type: post
template: blog-post.html
---
The following describes the process of adding support for the provision of [OPML](http://en.wikipedia.org/wiki/OPML) files to the Moodle activity module [BIM](/blog2/research/bam-blog-aggregation-management/).

### Requirement

[BIM](/blog2/research/bam-blog-aggregation-management/) allows students to register external blogs with Moodle and provides support for teaching staff to track, manage and mark the student blogs. Rather than use BIM and Moodle to find out which students have posted recently, it would nice to allow teaching staff (initially) to download an OPML file for all their students. This file could be imported into most newsreaders and used to track student submissions.

The aim is to start simple and only provide an OPML file for each teaching staff member's "your students". Given the nature of OPML, if the staff wanted to share this with students, they could simply give them the file, but that's their choice.

Longer term there's a range of additional feeds that would be cool for BIM to generate (the top 10 marked posts in an RSS file etc.).

### How to generate OPML files in PHP

I've been wondering if there are any way of generating OPML in PHP or Moodle. A search of the moodle.org site reveals [this forum post](http://moodle.org/mod/forum/discuss.php?d=41299) which mentions [feedcreator](http://feedcreator.org/), which seems to fit the bill.

Questions. Is feedcreator already part of Moodle? Is it the best option? It appears to be quite old (2005). Seems like it is still being used by some and isn't in Moodle. So, let's go for that - I'm after easy wins at the moment.

First, let's write a little php script to test out feedcreator's generation of OPML feeds.

Mmm, not good, it doesn't appear to generate OPML that is recognised by my newsreader. Wonder if this is a problem with it only supporting OPML 1.0?

### Writing my own functions

Given that OPML is a fairly straight forward format, I think the solution will have to be writing my own.

Plan is to have two types of OPML function:

- generate\_opml - which given a hierarchical structure with the data generate a valid OPML file.
- generate\_structure - given various BIM/Moodle variables, construct the structure that can be passed to generate\_opml

The structure will be an array with two elements - head and items. items will be an array of items - the feeds for each student.

generate\_opml is done and fairly simple. Now to figure out what's need to generate the structure.

### The user perspective

The idea is that when visiting the "Your students" tab the teaching staff member should see a link 'Your students OPML file". Click on that link and they get an OPML file to download. So that means a unique/new script to call - marker/generateOpml.php.

Okay, still want to do various checks, so have to go through normal BIM process. Trouble is that it currently always displays the Moodle header and footer - need to be a little more discerning. i.e. don't do either for the OPML feed.

Need a help file, some lang entries. Cleaning things up. Done. Looks like the following

[![BIM with opml generation added](images/4658306149_32b3098c3f_m.jpg)](http://www.flickr.com/photos/david_jones/4658306149/ "BIM with opml generation added by David T Jones, on Flickr")