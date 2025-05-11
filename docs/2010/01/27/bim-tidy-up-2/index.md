---
categories:
- bim
date: 2010-01-27 15:19:51+10:00
next:
  text: Week 12 - Experiencing and sustaining innovation and change - simple test
  url: /blog2/2010/01/31/experiencing-and-sustaining-innovation-and-change-simple-test/
previous:
  text: Some reasons why business intelligence tools aren&#039;t the right fit
  url: /blog2/2010/01/27/some-reasons-why-business-intelligence-tools-arent-the-right-fit/
title: '"BIM - tidy up #2"'
type: post
template: blog-post.html
---
Some more tidying up of BIM to get it ready for release.

### Error messages on student details

When one student views the details, we're getting error messages.

Okay, need another check. That's done.

### Check the group usage

Have got the allocate groups stuff working, is it actually being used by the support functions that return lists of students associated with markers?

No.

So, the get\_records\_select for the tmp table bim\_markers\_students needs to get replaced with something that goes via bim\_group\_allocation and then group\_members to get the userids.

That means changing the signature of the bim\_get\_markers\_students function - take bim now, not course. My, the comments actually said course was temporary.

Update the calls to records select to go via the other tables.

Done.

### Fix up the display of last post in the student details screen

This is a hang over of the change from datetime in BAM to unix timestamps in Moodle. There are at least 2 contributing problems to this :

- Test data from BAM into BIM put in just a year, not the unixtime.  
    So need to modify the lastpost entry in my test bim\_student\_feeds to be using unixtime. All entries changed to the same value.
- The display of the timestamp in BIM isn't doing the right conversion.  
    Already doing this in the allocation and marking form using the PHP date function. Done.

Ahh, but that's the rub. What is actually needed here is how long ago the last post was. That's a different method.

Used function [from here](http://www.charles-reace.com/PHP_and_MySQL/Time_Difference/) to implement.

### Removed sortable links on tables

Haven't groked how to do the flexible\_table sorting. Will leave that for later.