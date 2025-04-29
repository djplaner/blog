---
title: bim2 - status check and what's next
date: 2012-03-30 22:40:51+10:00
categories: ['bim2']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

So it appears that bim2.0 is increasingly needed (if you don't know what bim is, check [this out](/blog2/research/bam-blog-aggregation-management/)). University of Canberra have gone to Moodle 2 and CQU are about to, the only two places I know that bim is being used. Most importantly, I'm now teaching at a Moodle Uni and am seriously thinking about using bim, and my Uni is about to move to Moodle 2.

In keeping with my practice, this post is another in [a list of posts](/blog2/category/bim/bim2/) that serve as a development journal (mainly because I'm coding so infrequently now I need to remember how to do this stuff). The aim here is to figure out where the porting is up to and perhaps identify where next.

The current code for bim2 can be found [in this branch](https://github.com/djplaner/BIM/tree/bim2) on github. I'll try to keep it up to date.

### Current status

The last work reported

> Most of the basic code for bim2 is working, but the capabilities aren’t. i.e. identifying the type of user and sending them to the right function.
> 
> Mmm, all are working, but not the coordinator.

As it stands the coordinator stuff is working. I wonder if that's because of a hard-coded kludge. Mmm, no. It seems to be coded as required.

I did have earlier problems because of versioning, it appears that's fixed now.

Let's test the other user types and make sure they are working

- Student - working, at least the redirect, the display leaves something to be desired.
- Marker - working as well.
- Coordinator (as a teacher, not as admin user) - bugger, that's not working "error/No capability to access this page"

### To do list

Which leads me to this basic to do list

1. Test out the marker and student views of BIM and find out what's not working.
2. Fix what's not working for marker and student
3. Figure out why the "coordinating" teacher is not being identified as such.

### Not identifying "coordinating" teacher

I can feel this being a bugger to identify where it's going wrong, mostly because my knowledge of the Moodle capability system (let alone the Moodle 2.x capability system) is close to non-existent.

Ha! Noticed that the teacher account only had the role "Coordinator" set and that the access.php file was not looking for "Coordinator" as a role to treat as a bim "coordinator". Added "teacher" as a role and it's working.

Is "coordinator" a standard Moodle 2 role? No, it doesn't [look like it](http://docs.moodle.org/22/en/Standard_roles).

Amazing what some time away will do for perspective and clarity.

### What's working for the student role?

First, why aren't the header/footer being displayed properly. Thinking I haven't added appropriate stuff in "show\_student". Yep, have to call the print\_header functions. Add that in, fix up the call to print the footer and we're working.

So, what can a student do and what do I need to check

- No feed registered
    - View bim - WORKS
    - Register invalid feed
        - URL is not a URL - WORKS
        - URL is not accessible - WORKS
        - URL is not a feed - WORKS
    - Register a valid feed - WORKS
- Feed registered
    - view current details - with no new blog posts added. - WORKS
    - View current details - with new blog post added - Not working so well

### Status for now

Most of the student functionality is working. However, every time the student is viewing their bim activity, the number of mirrored posts is going up by 10. Needs to be fixed.

Some potential causes to investigate

- The caching/operation of the Moodle 2 version of Simplepie and bim.
- Left over database entries not cleaned up appropriately during testing.
- Errors crept into the mirroring code due to Moodle 2 database API changes.