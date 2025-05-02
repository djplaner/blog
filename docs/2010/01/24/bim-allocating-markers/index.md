---
title: BIM - Allocating markers
date: 2010-01-24 09:38:32+10:00
categories: ['bim']
type: post
template: blog-post.html
---
I had sort of hoped that most of the new BIM development was finished. However, after a bit of research at the local institution it becomes obvious that I'll have to implement a marker allocation screen. Hopefully, it won't require that much work.

### Requirement

The aim is to allow the coordinating teacher to specify which groups of students will be marked by which staff. In my head the aim will be to:

- Get and show a list of all the teaching staff currently allocated to a course.
- Get a list of all the current groups allocated for a course.
- Show a list of the groups in a multi-select box against each staff member.
- Allow the coordinator to select and update as required.
- Provide a pointer to the Moodle tools/links to allocating users and adding/managing groups.

The plan is to implement this as another tab for the coordinator.

Once this is implemented will need to modify the existing `bim_get_markers_students` and related functions to use the new method.

Should also look at providing away to make teaching staff coordinators - or is this simply done by capabilities?

### groupslib

[Developement docs](http://docs.moodle.org/en/Development:Groups) for groups in Moodle. Somewhat limited, but does appear to have some important point re: the use of groupings.

Would appear that `groupslib.php is the place to find functions associated with Moodle groups. The following list summarises some of those that might be of interest to this task.`

``   - groups_get_groupname( $gid ) - groups_get_group_by_name       The implementation of this suggests that the `groups` table includes courseid as a field. - groups_get_group( $gid ) - return the record for the group - groups_get_all_groups( $courseid, $userid=0, $groupingid=0 ) - will use this one - groups_get_user_groups( $courseid, $userid ) - groups_get_members( $gid...)  There is something called groupmode applied to activity and course setting. Will need to look at that.  There are also some functions apparently creating menus  - groups_print_course_menu( $course, $urlroot, $return=false) - groups_print_activity_menu( $cm, $urlroot, $return=false, $hideallparticipants=false )  ### Get the data  To implement this will need to retrieve:  - Details of all teaching staff in a course. - List of all groups associated with a course. - How best to do multi-select boxes in Moodle. - Eventually, how to get members of a group.  ### Implementation  #### Add the extra tab  Get the structure going and start doing some testing. Added new allocate_markers.php. Basically done.  #### Testing with groups  My initial though was a simple moodleform to implement this. However, to some extent the existing functions that show menus, might be the way to go?  groups_get_user_groups is currently returning an empty array. Probably because there are no groups configured for this course. Yep, no groups created. Let's create one and see what happens.  Group created, but no-one assigned to it. It still shows up as empty. But I am asking specifically for groups that the user is a member of. What if I go more general?  Yes, groups_get_all_groups for the course, gives me all the groups. Let's allocate the user and see that get_user_groups change. Yep, when allocated, groups_get_user_groups returns the id of the group, but no other information. What is returned from groups_get_all_groups includes full information keyed on id.  I think I will try the Moodle form approach.  #### Getting all teaching staff  In reality, the point is not to get all the teaching staff, but to get all the staff that have the capabilities associated with marking students. For BIM, I've specified these as `mod/bim:marker` and `mod/bim:coordinator`. I'm interested in all users with those capabilities.  There's a `get_users_by_capability` function in accesslib.php - but there's a warning about performance. It [seems the advice](http://tracker.moodle.org/browse/MDL-16300) is to use it just once per page load.  #### Nutting out the life-cycle  In terms of the life-cycle for group allocation for BIM, I can see the following stages:  - No groups at all in the course.       Need to advise the coordinator to go and create some groups. - No teaching staff won't happen, at least the coordinator should be listed.  ### Add the database table  The aim of this form is to allocate staff members to particular groups of students for marking purposes. Am going to need a table to track which groups a staff member has been allocated to. Am thinking of something fairly simple.  ``` CREATE TABLE mdl_bim_group_allocation (     id BIGINT(10) unsigned NOT NULL auto_increment,     bim BIGINT(10) unsigned NOT NULL,     userid BIGINT(10) unsigned NOT NULL,     groupid BIGINT(10) unsigned NOT NULL, CONSTRAINT  PRIMARY KEY (id) ); ```  ### Creating the form  The form will essentially be a list of the markers with a multi-select box containing course groups. From here it becomes a moodle form process.  Basically done, but am not pleased with the layout. Will eventually have to play with the CSS. It's workable as it stands.  ### Processing the form  - Set the values from the existing allocations. - Display the form. - On submission, compare the allocations with those already in the database.  Question here about the best way to proceed:  - Simply delete all entries for the bim and insert the new ones. - Loop through each marker and add or delete as required?  I'm leaning towards the latter. The plan is  - Loop through each marker     - if there's an allocation in the form, that's not in the dBase - add it.     - if there's an allocation in the dBase, but not in the form - delete it.  The question now is whether there's a way in Moodle to execute multiple SQL statements, or whether I should do it one, by one?  `delete_records_sql` seems to be the way to delete records and can do multiples. `insert_record` will insert one at a time.  Okay, after some "issues" with setting the data. All is done.  ### What was done  The marker allocations screen is complete.   ``