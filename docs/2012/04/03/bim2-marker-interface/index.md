---
title: bim2 - Marker interface
date: 2012-04-03 22:51:35+10:00
categories: ['bim2']
type: post
template: blog-post.html
---
In case you're wondering, BIM is a Moodle activity module that helps teaching staff manage individual student blogs. This post is one of a number of posts documenting the development of a version of BIM that will work with Moodle 2.x. More detail on BIM [here](/blog2/research/bam-blog-aggregation-management/)

In the following, I'm continuing work on the marker interface from [prior work](/blog2/2012/03/31/bim2-student-and-marker-fixes/). Work to do includes

- Register a blog for a student **DONE**
- Mark posts - viewing details **DONE**
- Allocate questions **DONE**
- Mark a particular post – which includes a range of changes **DONE**

This means that the marker interface for BIM2 is working. Next step will be the coordinator interface.

### Register a student blog

That actually seems to be working as stands. Not surprising as it reuses the student functions for registering.

However, the main marker screen isn't handling the absence of "unregistered" students well. i.e. if there are none, it's still showing the heading and empty table.

Fixed.

### Mark posts

This is the main marking interface and has a number of components. We'll start with simply displaying the main interface.

Current problems

- Has the same "showquestions" problem as the student had. **DONE**
- Help button not showing in the right place. **DONE**
- It's crashed and burn, not completing. **DONE**  
    Needed to include tablelib.php

### Allocation questions

This seems to be displaying first up.

Some things to improve

- Funny "# posts mirrored" heading appearing - **DONE**
- Allocating a post doesn't seem to be showing actual answers & required answers  
    This problem seems to be due to displaying the stats with old data. It is being updated in the database. A fairly major flaw in the original design of the code.

### Mark a post

Coding error...seems a database problem in marker/view.php 868. Ahh, the syntax for DB->get\_field has changed. Should check that all over. That's it.

Another problem with implode. That's working.

Now problems with help buttons again. Done.

Title for showing the student post is being corrupted. That's fixed.

Now the marker comments title and editor aren't showing up properly. Ahh, it appears ["htmleditor" is deprecated](http://docs.moodle.org/dev/lib/formslib.php_Form_Definition#editor). But the problem is really just the width of things. i.e. use has make the browser window large.

When updating a post having a problem with addslashes still being used. Remove those, no longer needed. Do a quick check where else it is used

**To test:** Do need to populate the test BIM with more questions and students with answers. Done.