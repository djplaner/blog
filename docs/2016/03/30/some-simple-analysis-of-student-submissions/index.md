---
categories:
- bad
- edc3100
date: 2016-03-30 11:16:45+10:00
next:
  text: '"Competence with digital technology: Teacher or environment?"'
  url: /blog2/2016/03/31/competence-with-digital-technology-do-they-see-the-point/
previous:
  text: Setting up the analysis of student submissions
  url: /blog2/2016/03/29/setting-up-the-analysis-of-student-submissions/
title: Some simple analysis of student submissions
type: post
template: blog-post.html
---
The [last post](/blog2/2016/03/29/setting-up-the-analysis-of-student-submissions/) outlined the process for extracting data from ~300 student submissions. This one outlines what was done to actually do some analysis on that data.

The analysis has revealed

- Around 10% of the submissions have an issue with the URL entered.
- About 16 lesson plans that have been evaluated by more than 1 student.
- At least 100 students have evaluated a lesson plan found online with the [Australian Curriculum Lessons site](http://www.australiancurriculumlessons.com.au) being the most popular.
- An [education-based site](http://www.dairy.edu.au) set up by the industry group Dairy Australia appears to be the most progressive in terms of applying a CC license to resources (apart from the [OER commons site](http://www.oercommons.org))
- It's enabled allocating related assignments to a single marker, but the process for doing so with the Moodle assignment management system is less than stellar.

Time to do some marking.

### What?

Having extracted the data, the following tests can/should be done

1. Is the lesson plan URL readable?
2. Are there any lesson plans being evaluated by more than one students? Might be useful to allocate these to the same marker.
3. What is the distribution of where lesson plans are sourced from? Did most use their own lesson plan?
4. Pre-check whether the lesson can be used?

### Is the lesson plan readable?

Code is simple enough, but using LWP::Simple::head is having some problems.

Let's try LWP::UserAgent.  That's working better.

Seems that if they successfully enter the URL it's readable.

3 students have used file:/ as a URL - not online.

### Distribution of lesson plans

Aim here is to group all the URLs based on the hostname. This will then allow the generation of some statistics about where the lesson plans are being sourced from. Findings include the following counts for domains

- 1 - domain = UNI (a problem)
- 3 - that don't have a domain
- 96 that appear to be using their own site as the course, indicating their own lesson plan
- 19 domains indicating a lesson planning site Accounting for 107 students
- 32 with some sort of ERROR

That's still not 300. Ahh, we seem to have some problems with entering URLs correctly, common mistakes include

- Just leaving off the http:// entirely
- Mangling bits of http:// (e.g. ttp:// or http//)
- Using a local file i.e. file:////
- Having the URL as "To complete"
- Having the URL empty

Fix those up as much as possible.  Most of these appear to have put something in the cover sheet - if they have one.

### Duplicate URLs

There are 16 lesson plans that are used by more than one student.  Most by 2, 4 by 3, 1 by 4 and 1 by 5 students.

Identifying these mean I can allocate them to the same marker. Would be nice if there was an easier way to do this in Moodle.

### Pre-check use

At least 107 of the students are using a lesson plan find online. The question is whether or not they can use that lesson plan as per copyright etc.

I could manually check each site, but perhaps to short cut it I should check the spreadsheet for a couple of students, see what argument they've mounted for fair use, and then confirm that.

The sites to check are

- http://www.oercommons.org Not surprisingly under a CC-NC-SA license, though the NC is a little bit of a surprise.
- http://www.australiancurriculumlessons.com.au Requires permission to upload.
- http://readwritethink.org Seems to allow reuse.
- http://www.capthat.com.au Copyright applies, but they've been good in granting permission for students to use for this assignment.
- http://www.dairy.edu.au Dairy Australia showing off their online nouse to have applied a CC license.
- http://cdn.3plearning.com Most students appear to have had to request permission.

Interestingly there is some large variation between people using the same site.  Should allocate these to the same marker.  Will cut down on time for them.