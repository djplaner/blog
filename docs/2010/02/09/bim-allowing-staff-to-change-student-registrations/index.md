---
categories:
- bim
date: 2010-02-09 20:25:43+10:00
next:
  text: BIM - misc changes from moodle-train
  url: /blog/2010/02/10/bim-misc-changes-from-moodle-train/
previous:
  text: BIM - talking to the gradebook
  url: /blog/2010/02/07/bim-talking-to-the-gradebook/
title: BIM - Allowing staff to change student registrations
type: post
template: blog-post.html
---
BIM is essentially complete and about to go into user testing, however, initial testing suggests that an ability for staff to change the blog students have registered would be a significant benefit during the first couple of weeks. This post describes the design and implementation of this feature.

### Plan

The aim is to allow all teaching staff should be able to modify the blog that has been registered for any of their students.

- Add to the student details screen, for each registered student, a link "change blog" in the "live blog" - actually change it to "Current blog | Change blog"
- The change blog is a link to a new form, essentially the same as the student register, just ask for a URL.
- When submitted, pass it through the same checks as the student does when registering -- Will need to abstract this code out into a function to use in both places.

### Update the student details screen

Add the change/current blog stuff. Easy, done.

Need to identify the URL for the form....&screen=ChangeBlogRegistration

### Display the form

Need to call the function to show the form for both:

- Marker
- Coordinator

Show the details of the student and the current blog, show a form.

### All done

All done and working. Need to update some of the bread crumbs for navigation, but that is part of another task.