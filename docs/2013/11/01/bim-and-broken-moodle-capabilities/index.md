---
title: BIM and broken moodle capabilities
date: 2013-11-01 13:15:01+10:00
categories: ['bim']
type: post
template: blog-post.html
---
The following is a long overdue attempt to identify and solve an issue with [BIM](http://bit.ly/bambim).

## The problem

BIM provides a three different interfaces depending on the type of user, these are

1. coordinator;
    
    The name is a hangover from a past institution, but essentially this is the teacher in charge. Can do anything and everything, including the management of the marking being done by other staff.
    
2. marker;
    
    Another staff role, mostly focused on marking/looking after a specific group of students.
    
3. student.
    
    What each student sees.
    

The problem is that the code that distinguishes between the different types of users is not working.

For example, a user who should be a coordinator, BIM thinks is potentially all three.

## The method

The method I use (and which was used in BIM 1 and has worked fine) is based on capabilities, essentially a few ifs \[sourcecode lang="php"\] if ( has\_capability( 'mod/bim:marker', $context )) { # do marker stuff } if ( has\_capability( 'mod/bim:student', $context )) { # do student stuff } if ( has\_capability( 'mod/bim:coordinator', $context)) { # do coordinator stuff } \[/sourcecode\]

These are then defined in db/access.php via the [publicised means](http://docs.moodle.org/dev/NEWMODULE_Adding_capabilities)

## What's happening

To get to the bottom of this, I'm going to create/configure three users who fit each of the BIM user types and see how BIM labels them.

1. coordinator user - BIM thinks can be marker, student or coordinator.
2. marker user - is a marker
3. student user - is a student and a coordinator

The above was tested within BIM itself. There's a capability overview report in Moodle that shows "what permissions that capability has in the definition of every role".

For coordinator, it's showing "Allow" for "Student" and not set for everything else. Not even the manager. Suggesting that there is a mismatch between the BIM code and what Moodle knows. Suggesting that an upgrade of the BIM module is called for.

So, let's update the version number, visit the admin page and do an upgrade. Success. Now check the capability overview report.

The capability overview report is reporting no change. This appears to be where the bug is. What's in the db/access.php file is not being used to update the database.

Seem to have it working.

### Clean test

Need to do a test on a clean Moodle instance.

1. Coordinator - CHECK
2. Teacher - CHECK
3. Student - CHECK

Glad that's out of the way. More work on BIM in the coming weeks.