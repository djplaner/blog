---
categories:
- bim
date: 2010-02-10 14:36:35+10:00
next:
  text: Implications arising from the absence of the "sameness of meaning"
  url: /blog/2010/02/11/implications-arising-from-the-absence-of-the-sameness-of-meaning/
previous:
  text: BIM - Allowing staff to change student registrations
  url: /blog/2010/02/09/bim-allowing-staff-to-change-student-registrations/
title: BIM - misc changes from moodle-train
type: post
template: blog-post.html
---
Currently testing BIM on the training/testing environment of my current institution. This is where I find all of the problems from the institution's non-vanilla implementation of Moodle.

### Manage marking - not all markers - DONE

Not showing details for all of the markers that have been allocated students. This appears to be because the institution has introduced a new role called "Course coordinator". Checks:

- Change on of the teachers to "teacher" more standard role.
- Then change the access.php file in bim to map the new role appropriately.

Part of this problem is due to students not being allocated to groups **TO DO:** Implies a need to identify those students who are in the course, but not in groups.

Actually, the problem was a misplaced add\_data\_keyed that was outside, instead of inside, a loop.

### Find student view details

> Parse error: syntax error, unexpected ';' in /Applications/XAMPP/xamppfiles/htdocs/moodle/mod/bim/marker/view.php on line 968

### Need to remove mysql\_real\_escape - DONE

This is a hang over from early development and not removed. Won't work on server environments if they aren't using MySQL. -- marker/view.php line 900

### Manage marking - counting all marked posts - DONE

Only 1 post marked, but release is showing 3 marked!!

This is because it's simply adding the total marked for each marker. If there is overlap in students between markers, then the # marked is counted more than once.

**Fix needs completion locally before putting onto -train**

### Marking form - min/max display - DONE

Need to change hard code 0 and 55 to the real min/max values.

### Student viewing details - DONE

The table with student details always shows the progress report. Even for marked posts that have not been released to the student. Initially this table was only for staff. But it is also being used on the students view page. Need the progress mark to only include released posts in its total.

Calculation done in bim\_generate\_student\_results - do it here.

All calls to this function, need to pass in cm

### Breadcrumbs for new functions - DONE

The "change blog" feature doesn't have good bread crumbs. May also be a problem with other new functionality. Check and fix.

Mark post

### Add "register blog" - DONE

Just as marker can change existing feed for a student, add the option to "register a blog" for unregistered students.

### cron job not completing - DONE

> Call to undefined function bim\_get\_mirrored() in **/Applications/XAMPP/xamppfiles/htdocs/moodle/mod/bim/lib.php** on line **176**  

Get this by running the admin/cron.php.

### Setting up help - DONE

Did some minor updates, rest will have to wait