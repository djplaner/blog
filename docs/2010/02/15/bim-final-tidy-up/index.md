---
title: BIM - Final Tidy up
date: 2010-02-15 11:31:36+10:00
categories: ['bim']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

Today is the day that BIM get's handed off to the folk of my institution's central IT division and from there onto [Netspot](http://netspot.com.au/) who will be ensuring that it is "safe" for IT to install it on the institution's live Moodle instantiation. In preparation for the hand over, I've done one last test and identified some issues to fix. This post documents that work.

### Process student feed on view - DONE

Historically, BAM, from which BIM grew, only mirrored students' feeds once every hour. Essentially to be a good citizen on the server. But the delay causes problems. Students don't understand the need to wait.

So the plan it to retain the hourly update, but to add a process student feed for a single student as the first thing that happens when that student attempts to view the details of their BIM activity. This removes the delay. In addition, because of caching and the minimal work involved does not place undue load on the server or the blog services.

Implementation includes:

- How is processing done now?  
    2 main functions
    1. bim\_process\_feed - checks the RSS feed and processes new posts.
    2. bim\_process\_unallocated - checks entries in bim\_marking to see if they match any questions (some might have been added).
- Can it be done for a single student/feed (register?)  
    Yes.
    
    Both functions take the params $bim, $feed, $questions ) - $feed is for single student.
    
- Implement it.  
    Put a call to the two functions in the show\_student\_details method. But only call them if there are actually questions (allocation doesn't work if there are no questions to allocate to).
- Should we show a message?

### Wrong count on student details - DONE

If there are no questions currently allocated, the student details table is still showing 1 as the count of required answers.

Strange problem with PHP count, added check for empty and working now.

### Tell markers configuration - DONE

Currently coordinators and students get messages if they can't register etc. The poor marking staff don't. Add one.

### Suspended post, no description - DONE

Student can see a message about the status of a post in BIM. If the post is suspended, they can't see anything.

Left message the same as marked.

### Changes to released post, no gradebook - DONE

A released post that has the mark changed, is not updating in the gradebook. Have any change to a released post (mark or comments) set the post back to Marked.