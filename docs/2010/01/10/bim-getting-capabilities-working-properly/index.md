---
title: BIM - getting capabilities working properly
date: 2010-01-10 17:33:02+10:00
categories: ['bim']
type: post
template: blog-post.html
---
Increasingly BIM development is getting to the stage where the functionality for BIM's three different types of user (coordinator, markers and students) are just about complete. I've been using a very naive, probably misleading interpretation of Moodle's capabilities system to distinguish between the different types of users and what they can do. Yesterday, doing what I thought was some minor updates, it broke. I'm currently having to use a kludge to get BIM to work for different users. This post is documents my attempts to fix this problem.

### The components of the problem

This task is complicated by the mixture of a number of different domains including:

- [CQU practice](http://www.cqu.edu.au/) and the origins of BAM;  
    Must of the design of BAM is based around CQU practice, where BAM started. The basic assumption of BAM/BIM (at the moment) is that there are three types of user:
    1. Coordinator - the teacher in charge(s) of a course, can do just about anything.
    2. Marker - any teacher who isn't a coordinator. Normally responsible for marking the posts of a subset of students.
    3. Students - people registering feeds with BIM.
- Moodle default roles;  
    This is an area of confusion for many and in which I'm still somewhat limited in understanding. My default installation of Moodle has the default user roles of:
    1. Administrator - can do anything in all courses.
    2. Course creator - can create courses and teach in them.
    3. Teacher - can do anything within a course (sounds like a Coordinator)
    4. Non-editing teacher - can teach in courses and grade students, but not alter activities (sounds like marker)
    5. Student
    6. Guests
- How those default roles are being applied at CQU; and  
    It looks like the CQU installation of Moodle has defined some Moodle roles that are more like the original CQU ones defined above. With BIM I'm in the interesting situation of coming from the CQU context but having to create something that will have minimal CQU assumptions so that other institutions can use it.
- Moodle's roles, capabilities, permissions and contexts.  
    Moodle is moving (since 1.7) to a more [flexible permissions system](http://docs.moodle.org/en/Roles_and_capabilities). This is what I need to actually use to achieve the melding of the above. [This seems](http://docs.moodle.org/en/How_permissions_are_calculated) to be the best explanation of how permissions are calculated in this regime.
- How you define capabilities etc within an activity block like bim.

### What I'm planning to do

With an activity module you are meant to define capabilities that exist for that module in the `db/access.php` file. At the moment, I'm hoping to define the following capabilities:

- `mod/bim:coordinator`
- `mod/bim:marker`
- `mod/bim:student`

Hopefully, there's a sensible link between these and the above. In the module code I am using which of these capabilities a user has to drive which part of the code is executed. That had been working. It broke yesterday as I was making changes.

### Testing it

I currently have different user accounts that take on each of the different default Moodle roles. Each of these are configured to receive particular capabilities within BIM. Time to test them and see what bim thinks they are. This is after a re-boot of the computer (separate reason) and so the outcome may be different. I think there was some "caching" issues yesterday.

- Administrator - coordinator (correct)
- Course creator - appears to end up enrolled as a student through moodle. Ignore for now.
- Teacher - coordinator (correct)
- Non-editing teacher - generates an error with no recognised capability
- Student - student (correct)

Okay, seems like non-editing teacher is the only problem. Why?

Dumping out the USER object doesn't give a lot of information, apart from the fact that this user has a value of -1000 for all the bim capabilities. Which appears to imploy that they don't have the capability. Yes, `lib/accesslib.php` defines CAP\_PROHIBIT as -1000. Which implies the capbility I have set to CAP\_ALLOW isn't working.

Is it just this capability. What if I change another? Changing db/access.php doesn't seem to make any different.

First, let's find out what role the user has, or at least Moodle thinks he has.

### Working?

I think it's working now. Seems that after changing `db/access.php` you have to:

- increment the version in version.php
- run the "admin notifications"
- log the use out and then back in again.