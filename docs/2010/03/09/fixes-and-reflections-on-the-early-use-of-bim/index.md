---
title: Fixes and reflections on the early use of BIM
date: 2010-03-09 13:35:36+10:00
categories: ['bim']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

[BIM](/blog2/research/bam-blog-aggregation-management/) is into it's 2nd week of being used at CQU (about 3/4 courses approaching 500 students) and there's also talk of it being used at another Australian university. It's time for a couple of reflections on early experience and also time to identify the source of a common problem.

### Not enough pro-active support

A couple of staff using BIM have reported that they can't see all of their students. In both cases this has been because the staff haven't been allocated to the full list of student groups in their course. In BIM, staff only "see" the students they've been allocated to.

What I've learnt from this is that BIM (like many other systems) doesn't bridge the gap between the reality of what the people using it experience/try to do and its own internal organisation. Someone like me, intimately aware of its internal organisation, can identify and fix the problem straight away. A normal person, with no knowledge of the internal organisation, can't. The system needs to bridge this gap.

One initial idea would be to work into BIM some idea of a common "life cycle" that different people go through using BIM. Have BIM know where a particular person is up to in that life cycle and also know what they should have done by now. This would allow BIM to modify itself (i.e. show some hints etc) if the person hasn't completed a necessary task, encouraging them to complete that task. e.g. a coordinator who hasn't allocated any groups to themselves might get a message reminding them to do so.

### They don't get the model

There's been much made of the efforts being made by various staff at the institution to train both students and staff in the use of Moodle. My limited experience with some of the staff suggests that some still don't get the model that underpins Moodle and how it works internally and at the institution. This lack of understanding means they can't easily problem solve and get frustrated with the system.

This connects with the previous point but also points to some limitations (in my mind) to the nature and timing of the training being given.

### Students, staff and lists - and how I didn't get the model

A key part of what a coordinator wants from BIM is the ability to track what students are doing (or not) with BIM. This allows them then to respond pro-actively etc. At it's simplest BIM supports this by providing a list of students who have not yet registered their blog. There's also a list of these unregistered students' email addresses that staff can use to email these students and remind them to register.

While this appeared to be working on my test box, the migration to the real, live system has identified a problem (or two) including:

- It may be possible that some registered students have their email address included in the unregistered list.
- Teaching staff are being included in the unregistered list.
- Some of the students/staff in the list don't have email addresses.

A related problem is that the institution has a "cast of thousands" of support staff that are meant to help academics with the courses. These staff are appearing in the list of teaching staff for "Allocate Markers". This is confusing the real teaching staff.

This is an example of me not getting the model being used on the live instance. So my assumptions in the BIM model, don't match. Need to fix this.

### Fixing the list

Okay, let's fix it. Three problems:

- How to exclude non-teaching staff from marker allocation.
- How to exclude teaching staff from unregistered students.
- Check that registered students can't appear in unregistered list.

#### Non-teaching staff

So, what role do all these non-teaching staff have in Moodle on the live system?

Well it looks like it is some special kludge. The staff don't appear in any of the normal roles or groups for the course, but they do appear in BIM.

The marker allocation page uses get\_users\_by\_capability to get all the staff that have marker or coordinator capabilities as set by BIM. Ahh, the capability for bim:coordinator allows editingteacher, coursecreator and "admin" to have this capability. Wonder if all these staff are in the admin role/group?

In terms of system roles, there is a "Course Developer" role and an administrator role. It appears these are the source.

If this is the case then the admin user on my laptop should appear on a local bim's allocate markers. Yep.

And if I remove the admin allow for coordinator, it should disappear? Nope. But this could because I don't understand how to get this change to operate in a Moodle instance.

Mmm, time to dig into the code for get\_users\_by\_capability to understand what is going on.

Ahh, there's a view param, which can hide users with invisible roles. Let's try that. Nope. Didn't change anything.

In terms of capability, "moodle/site:doanything" is being included in at least one SQL statement.

So, this is the basic problem. get\_users\_by\_capability is including the "important"/admin roles. So, the solutions are either exclude those users or use a different method that only gets teaching roles.

Anything in the forums? Yep, [this](http://moodle.org/mod/forum/discuss.php?d=115636) which has a couple of solutions, including the "doanything" parameter for get\_users\_by\_capability, which - if false - excludes the admins.

### Exclude teaching staff from unregistered students

This is/should be done by the same process, but get's different results for a coordinator under "Your students" and manage marking. Let's try "Manage Marking". The process here is:

- allStudents = bim\_get\_all\_students  
    Again using get\_users\_by\_capability, need to set doanything to false.
- feedDetails = bim\_get\_feed\_details  
    Just a simple get entries from bim\_student\_feeds.
- unregistered = array\_diff( $allStudents, $feedDetails )

That should work now.

### Check registered can't appear unregistered

Don't see how can this can happen now.