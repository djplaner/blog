---
categories:
- bim
- moodle
date: 2010-04-30 13:37:36+10:00
next:
  text: Can BIM support the use of Moodle blogs?
  url: /blog/2010/05/02/can-bim-support-the-use-of-moodle-blogs/
previous:
  text: The alignment project as leadership
  url: /blog/2010/04/29/the-alignment-project-as-leadership/
title: Adding "deleted" to BIM
type: post
template: blog-post.html
---
The following is a record of the process of adding a "deleted" state for a blog post in [BIM](/blog/research/bam-blog-aggregation-management/). This is in response to [an issue](http://github.com/djplaner/BIM/issues#issue/8) that has arisen out of BIM usage at CQU.

### The problem

BIM always keeps a record of all posts ever found in a student's blog feed. Even if the student deletes the post or changes the post, BIM keeps a record of the post in its internal database. This is a feature of BIM as one of its aims is to provide a "safe/secure" record of what is posted to the students' blogs, just in case the blog service provider goes away.

In addition, BIM also attempts to allocate old posts in its internal database to questions. Sometimes, you do wish to "delete" a post to stop BIM from allocating it. To give the student a chance to post something new.

### Requirements

Requirements for this feature include:

- Only the coordinator can "delete" a post.
- The post is not actually removed from the internal BIM database, it just is no longer able to be "allocated" by BIM, released by the coordinator, visible to the student, or put into the gradebook.
- It must be possible to "undelete" a post.
- Deletion should not change any of the other data about a post (e.g. marker comments).
- Perhaps rather than be invisible to the student, it should just be obvious that it has been deleted.

### Design

- Add "Deleted" status for mdl\_bim\_marking.  
    Modified setting via XMLDB, but the database is not being updated. This has been a problem before which I've kludged around. But it's not something to rely upon for production. Will have to solve this problem.
- Add interface for staff to "delete"
- Modify student view to show that it is deleted