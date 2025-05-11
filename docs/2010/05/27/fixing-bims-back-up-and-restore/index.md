---
categories:
- bim
date: 2010-05-27 15:44:14+10:00
next:
  text: One potential approach to provide a Moodle email merge facility
  url: /blog2/2010/05/28/one-potential-approach-to-provide-a-moodle-email-merge-facility/
previous:
  text: Adding multiple visualisation approaches to Indicators block
  url: /blog2/2010/05/26/adding-multiple-visualisation-approaches-to-indicators-block/
title: Fixing BIM's back up and restore
type: post
template: blog-post.html
---
The following outlines steps to continue work on [BIM's backup and restore functionality](/blog2/2010/02/07/bim-backup-and-restore/). As per [this issue](http://github.com/djplaner/BIM/issues#issue/1) the user part of the back up has errors.

It appears that the code was actually working.

### Re-create the problem

It's been a few months since I worked on this. Have to re-create the problem first.

Looking through the bim/backuplib.php code, the first evidence is that the user code is commented out in the function bim\_backup\_one\_mod. Let's uncomment that and try to back up a BIM.

Okay, that seems to have completed. No errors reported. Is the Moodle debugging option set to the highest? Yep. So the problem isn't a syntax error, it's an error in operation/implementation.

Let's look at the resulting backup and see where it is going wrong.

\[sourcecode lang="bash"\] david-joness-macbook-pro:tmp david$ unzip \* Archive: backup.zip creating: course\_files/ creating: course\_files/1/ inflating: course\_files/1/david.2.xml inflating: course\_files/1/david.xml creating: group\_files/ creating: group\_files/60/ creating: group\_files/61/ inflating: moodle.xml creating: site\_files/ \[/sourcecode\]

Should there be BIM specific files here? No, looks like the data is within the files. Okay, there's no user data being saved. Why?

Ahh, there's more commented code to uncomment. Mm, still getting the message "without user data". Missing something.

Ahh, apparently not all users can back up user data. I was logged in as my own account, no permission. Login as root, and there's the user stuff.

Okay, BIM backup appears to work - no errors. Let's look at the files.

Yep, that seems to be working so far. All three tables are being saved in the XML file and in apparently correct format.

### Doing the restore

So, is the problem with the restore? The restore looks to have worked. The big question how do we test. First, let's look at the restored BIM. There are errors. But also no students. Appears that the problem is that the students/users from the backed up course, aren't in the restored and separate course.

What if we do the restore within the same course?

Well the restore process didn't create any errors, but when using the newly restored BIM (in addition to the existing BIM activity) it has the same sorts of errors as when restored in a new course, there's a problem with manage marking.

Let's look at the database and see what's been restored, check each BIM table.

- bim - information about all BIM activities.  
    As expected. 3 BIMs on my test box. The values are all as I'd expect.
    
    The original activity has id 1, 2 is the restore in a new course (course id 15) and id 3 is for the activity restored in the same course (course id 4)
    
- bim\_group\_allocation - which groups are allocated to which staff.  
    Again, there are 3 BIMs listed. The same number of entries for each BIM. The userids of the markers are the same regardless of the course. The group ids are different between courses. As expected (I think).
- bim\_questions - list of questions for the activity.  
    Ok, as expected as it's the user stuff I'm checking and this isn't user stuff.
- bim\_student\_feeds - where are the students registered feeds?  
    All correct. Each of the 3 bims have exactly the same data. The userids are the same regardless of the course. This indicates that the restore is making the right decisions about the students.
- bim\_marking - marking and other information about each student post (3 feeds registered, 10 posts per feed, 3 bims)  
    As expected there are 90 rows in this table. After a quick check, it appears that this is all good.

This is somewhat strange. Looks like it's all working, so why the problems?

Is it because of the user I'm logged in as (admin user), what about a standard teacher? Nope, same errors. Time to look at the code.

The errors being reported are in a Moodle library - tablelib.php. Hence the data being passed in must be corrupt/wrong in some way. If I compare the original BIM activity with the restored one (in the same course) there are differences in the manage marking output. The restored one is missing one of the questions. However, under manage questions all the questions are listed.

The code generating the header of the table generates the same data. Okay, the problem is within the code that generates the contents of the table.

Bugger, my problem here. The function "bim\_get\_question\_id" compares the title of a question to get the unique id of the question. If questions have the same title, which they can and do in this example, then there's a problem. Need to fix that.

### Fixing get\_question\_id

This function is only used once. In this section. So, it looks like the solution is to remove the need to use it.

Let's try simply adding the id of the question as the index for the array.

Yep, that works.

### Does it work now?

So, does that mean the back up and restore process is working? Checking through the restored BIM in the same course, it appears it does. Some errors are there when restored to a new course.

This appears to be because there are no students assigned to the course and the error checking in BIM ain't great. Fix that and the error messages disappear, but there still appear to be users within BIM. Which is probably what should happen because there are no students in the course, but there are in BIM.

Okay, the problems appear to be not with backup/restore, but with courses not having students enrolled and the poor error checking in BIM. If I fix up the error checking, we should be in action.

### Required fixes

- bim\_create\_posts\_display - another area where the same question title is causing problems.

That's it. Seems to be working

Just need to remove the debug statements in the restore process and commit it.