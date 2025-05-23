---
categories:
- bim
date: 2016-05-09 14:27:53+10:00
next:
  text: Testing out the Moodle search book block
  url: /blog/2016/05/10/testing-out-the-moodle-book-search/
previous:
  text: Focus, innovation and university IT
  url: /blog/2016/04/28/focus-innovation-and-university-it/
title: How does BIM allocate blog posts to prompts
type: post
template: blog-post.html
---
The following is a response to the following query.

https://twitter.com/UOWMoodleLAB/status/729511696054681600

### Background

[BIM](https://moodle.org/plugins/mod_bim) is a plugin for the Moodle LMS. BIM is "Designed to support the management of individual student blogs (typically external to Moodle) as personal learning/reflective journals". Students create their individual blogs (or anything that produces a RSS/Atom feed) and register it with BIM. BIM then mirrors all posts within the Moodle course and provides functionality to support the management and marking.

A part of that functionality allows the teacher to create "prompts". The [design of the original tool (BAM)](/blog/publications/blog-aggregation-management-reducing-the-aggravation-of-managing-student-blogging/) assumed that students would write posts that respond to these prompts. These posts would be marked by teaching staff.

BAM (and subsequently BIM) was designed to do very simple pattern matching to auto-allocate a student post to a particular prompt. It also provides an interface that allows teaching staff to manually change the allocations.

### Defining a prompt

A prompt in BIM has the following characteristics

- title; A name/title for the prompt. Usually a single line. The original design of BIM assumed that this title was somewhat related to the title of a blog post. The advice to students was to include the title of the prompt in the title of their blog post, or in the body of the blog post.
- description; and, A collection of HTML intended to describe the prompt and the requirements expected of the student's blog post.
- minimum and maximum mark. Numeric indication of the mark range for the post. Used as advice only. If the marker goes outside the range, they get a reminder about the range and it's up to them to take action.

### Auto-allocation

Auto-allocation only occurs during the mirror process. This is the process where BIM checks each student's feed to see if there are new posts.

When BIM finds a new post from a student blog it will loop through all of the un-allocated prompts. i.e. if this student already has a blog post allocated to the first prompt, it won't try to allocate any more posts to that prompt.

BIM will allocate the new post to an unallocated prompt if it finds the prompt title in either the body of the blog post, or the title of the blog post. BIM ignores case and it tries to ignore white space in the prompt title.

For example, if this blog post is the new blog post found by BIM, then BIM will make the following decisions

1. ALLOCATE: the post to a prompt with a title of "**does BIM allocate blog posts**". This matches exactly the title of this blog post.
2. ALLOCATE: the post to a prompt with a title of "**DOES    BIM ALLOCATE   BLOG POSTS**". BIM ignores case and white space, hence this matches the title of this blog post
3. ALLOCATE: the post to a prompt with a title of "**Auto-allocation**". The body of this post includes the word Auto-allocation.
4. DO NOT ALLOCATE: the post to a prompt with a title of "**does BAM allocate blog posts**". (Assuming that the above line didn't appear in this post) This particular phrase (see the A in BAM) would not occur in the title or the body of this post, and hence not be matched.