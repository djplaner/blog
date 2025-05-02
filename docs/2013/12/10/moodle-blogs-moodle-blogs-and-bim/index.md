---
title: "#moodle, blogs, Moodle blogs and #bim"
date: 2013-12-10 14:17:55+10:00
categories: ['bim', 'bim2', 'moodle']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    []
    
---
[BIM](/blog2/research/bam-blog-aggregation-management/) is a Moodle activity module that I developed and use. BIM evolved from an earlier system called **B**log **A**ggregation **M**anagement (BAM). BIM's acronym is **B**AM **I**nto **M**oodle. As the name suggests, BIM is essentially a port of all of BAM's functionality into Moodle. Both BAM and BIM are designed to help with the task of managing students in a course writing and reflecting on their own individual web blogs. In particular, it was designed to do this for courses with hundreds of students.

The aim of this post is to explore and explain a comment that often arises when BIM is first mentioned. i.e. doesn't Moodle already offer blog integration? The following tweet from @tim\_hunt is an example of this.

https://twitter.com/tim\_hunt/status/397489330169458688

The aim here is to answer the question, "What does BIM offer that Moodle's existing blog integration doesn't already provide?"

In short,

- Blogs in Moodle are focused at providing a way for authors to create a blog inside of a Moodle instance.
- BIM is focused on supporting teaching staff in managing a course where all students are expected to write on their own externally hosted blog.

## Blogs in Moodle

Each user in Moodle has their own [blog](http://docs.moodle.org/24/en/Blogs). i.e. the user's (student, teacher or other) blog resides in Moodle. The functionality used to [create](http://docs.moodle.org/25/en/Using_Blogs#Adding_a_blog_entry) and [edit blog posts](http://docs.moodle.org/25/en/Using_Blogs#Editing_a_blog_entry) is provided by Moodle.

Each user's blog can have an RSS feed if configured (by default this is turned off). However, standard advice appears to be to have [RSS feeds secured](http://docs.moodle.org/dev/Blogs#Secure_RSS_feeds) (i.e. only people who can login to Moodle can access the feed).

There is support for "course tags" which allow particular posts to be associated with a course. Posts associated with courses in this way are still visible elsewhere.

If the Moodle administrators have enabled it, users can register their external blog with their Moodle blog. For example, if I registered this blog with a Moodle blog, then anything I post to this blog would also appear in my Moodle blog. Posts from an external blog can be deleted from a Moodle blog, but can't be edited.

### Summary

Moodle's blog functionality is focused on helping users create and maintain a blog that sits within a Moodle instance.

It is user-focused, not course-focused. e.g. it appears to offer no functionality for teaching staff to find out which students have blogged or haven't, and no functionality to mark blog posts.

The problem here (at least for some) is that

> Reflective learning journals are demanding and time-consuming for both students and staff (Thorpe, 2004, p. 339)

## Blogs with BIM

BIM doesn't provide any functionality for students or teachers to create a blog. Instead, BIM relies on the author creating a blog on their choice of blogging platform (e.g. I always recommend [Wordpress.com](http://wordpress.com/)). This means that the students' blogs (it's almost always student blogs that BIM works with) are hosted external to the LMS. Each student's blog is their individual blog.

What BIM does is

- Make a copy of all the posts students make on their blog within the LMS just in case the dog eats it.
- Provide a couple of aggregated views that shows you who has blogged, how much they've blogged and how recently they've blogged.
- Allows different teaching staff to see these aggregated views for the students they are responsible for (while the "in charge" teacher can see all).
- Shows which students haven't registered their blogs yet and provides a mail merge facility to remind them to do it.
- Provides an interface so students can check what BIM knows about their posts.
- If you really want to, allows you to mark student posts.
    
    This is done by specifying a set of questions that student posts should respond to, and the provision of a marking and moderation interface. Finally, the marks will integrate into the Moodle gradebook.
    

### Summary

BIM functionality is focused on managing (and marking) of student blog posts. It aims to reduce the time-consuming nature of reflective journals implemented using blogs.

What functionality BIM currently provides for this task remains essentially the same as was designed into BAM in 2007. I'm hoping 2014 will see some long overdue evolution in functionality.

## Moodle blogs and BIM?

The Moodle blog functionality is all about helping authors produce blogs. BIM is currently all about helping teachers manage and mark the student use of blogs. It is possible to argue that neither do an overly fantastic job.

This means that it should be possible for the two to work together. i.e. a student could register their Moodle blog with BIM, rather than using Wordpress or some other external service. Indeed it is. I've just successfully registered a Moodle user blog in BIM.

This is of potential interest in situations where what the students are reflecting on might raise privacy concerns (e.g. nursing students - or just about any other profession - reflecting on their placement experiences). In this situation, the students could create their blog within Moodle and register the RSS feed with BIM.

However, the privacy of this approach depends on the [blog visibility settings](http://docs.moodle.org/24/en/Blog_settings#Blog_visibility) within Moodle and their impact on the generation of the RSS file. There appear to be three relevant settings for "blog visiblity" in Moodle

- "The world can read entries set to be world-accessible"
- "All site users can see all blog entries"
- "Users can only see their own blog"

The question is what effect this visibility setting will have on the RSS file required by BIM. i.e. If visibility is set at "Users can only see their own blog" will this stop generation of the RSS file? A quick test seems to suggest that the RSS file is still generated.

This begs another question about privacy. The "security" or "privacy" of the RSS file generated by a Moodle blog is an example of security through obscurity. i.e. if you know the URL for the RSS file, you can view. The "security" arises because the URL includes a long list of hexadecimal numbers that make it hard to guess.

## References

Thorpe, K. (2004). Reflective learning journals : From concept to practice. Reflective practice: International and Multidisciplinary Perspectives, 5(3), 327–343.