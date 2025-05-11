---
categories:
- bim
date: 2010-01-17 22:20:26+10:00
next:
  text: Questions about alternatives to curriculum mapping
  url: /blog2/2010/01/19/questions-about-alternatives-to-curriculum-mapping/
previous:
  text: BIM - Manage Marking
  url: /blog2/2010/01/17/bim-manage-marking/
title: BIM - manage marking - view and release
type: post
template: blog-post.html
---
This post continues on from [the manage marking](/blog2/2010/01/17/bim-manage-marking/) work and describes the design/implementation of the view and release operations of manage marking. There are strong similarities in what both operations do and how they do it, so doing them in one.

Both view and release take a collection of values and subsequently query/update the bim tables.

### Implement simple controller

`view.php` gets a simple controller to call the right function. `bim_manage_release` and `bim_manage_view`.

### Basic algorithm

Both will follow the same basic algorithm

- Check and get the values for the parameters.
- Perform operation
- Display the result.

### View

Aim to show essentially same data as `show_teacher_post_details` but based on a particular set of student ids.

- Get student ids that match parameters.
- Get matching student, marking and feed details based on student ids.
- Get the details of the specific marker (if one).
- Use the `bim_setup_posts_table` and `bim_create_posts_display` functions.

Posts/students in the "missing" category are going to be somewhat more difficult. "Missing" only makes sense if there is a question allocated. i.e. they are missing posts as answers to that question. So, missing = all students in course - those not belonging to the marker (if marker exists) - those with posts. And some of these will be unregistered, will need to handle those.

**DONE**

### Reset

This is somewhat different - no missing - but mainly because it will seek to update the database, rather than display information from it.

Given either marker, question or neither, the aim is

- generate a number of ids in bim\_marking for posts that match the criteria and then to update them to Released.
- only interested in posts that are:
    - currently in the Marked state
    - match the marker and/or question
    - if none of those, then it should match the bim

All pretty straight forward and it is now working.

### What's been done

The Manage Marking screen for coordinators has been completed. This brings to end most, if not all, of the interface for BIM.

What's left includes:

- The background/cron code to mirror and allocate student posts
- The process for putting results into the gradebook.
- Identify the CQU specific method for putting students and markers into groups together.
- A general re-check of some of the code including:
    - Modification to meet Moodle coding guidelines.
    - Re-factoring the structure and location of functions.
    - Double checking the early functions on the basis of more recent knowledge.
    - Looking at the use of flexible\_tables and in particular the sorting.
- General run through the BIM life cycle.
- Creation of online help resources.
- Adding BIM into the Moodle contrib section.