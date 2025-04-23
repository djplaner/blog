---
title: BIM - Mark Post screen
date: 2010-01-10 11:38:09+10:00
categories: ['bim']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

This post is meant to document the (hopefully short) process of getting the Mark Post screen implemented in BIM.

### Required data

The screen is passed the various cm->id and the id for bim\_marking. It will need to get:

- Contents of bim\_marking - i.e. the post to mark.
- Details about the student, including progress mark.
- Information about the other questions - mostly to implement the "ReAllocate" drop box.  
    This can borrow from the AllocatePost screen.
- Information to generate the marking progress information - basically all of the student details stuff duplicated from AllocatePost.

### Implementation questions

This will be implemented using a form and be very similar to the AllocatePost screen. Should be able to borrow, reuse and re-factor most of that code.

So, let's try that first. Copy the allocate method and make the changes necessary for marking (if this works, it shows the design ain't that great).

First change is that markingId is passed in, not user id. That fixed, it's basically working. Now need to create the form.

This is essentially a modification of the allocate posts form to deal with a single post and include a HTML editor for creating the comments.

Some initial problems with setting the data, but that's more due to learning more about the forms processing/scripting in Moodle/PHP. All fixed. Just now fiddling with the proper logic in processing the form and displaying a decent message to the user.

### What's been done

That seems to be working. Marking is done.

### What's left to be done

- BAM has the ability for the marker to navigate to the next/previous question for the same student. BIM doesn't have that yet.