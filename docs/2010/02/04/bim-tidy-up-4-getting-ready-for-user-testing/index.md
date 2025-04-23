---
title: "BIM - Tidy up #4 - Getting ready for user testing"
date: 2010-02-04 13:58:43+10:00
categories: ['bim']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

Continuing the tidying of BIM. This time the focus is on any and all steps necessary to get BIM ready to go up on a test server and have some real folk actually look and play with it. The structure of this will be based around users and actions. I'm going to do some of my own testing and then also add in anything that comes up from working with others.

This is a work in progress.

The following bullet list will list the different roles and the actions they can perform. It will contain a description of what I found/reflected upon. I'll add any todos in line with the action/user. The users and their actions for BIM currently include:

- Coordinator
    - Remove a bim activity  
        Not what would typically be first, but I have some old test cases laying around and it was the first one I needed to. The standard editing interface will remove the bim from display. It will remove the data from mdl\_bim. Can't confirm if it will remove entries from the other bim tables.
        
        **TO DO:** Check whether removing a BIM will delete all database entries. No, it doesn't.
        
        **TO DO:** Modify lib.php:bim\_delete\_instance so that it removes all evidence from the database tables. Also check if it should actually ask about backups?
        
    
    - Create new bim/Configure;  
        First, let's login as a coordinator of a course and create a new BIM activity.
        
        **TO DO:** having the newly designed icon for bim in place results in a massive icon in the configure page for a new activity. Need to reduce it. (icon is quite large - need to reduce it)
        
        **TO DO:** Need to put in place the help pages.
        
        **TO DO:** Need to put in HTML editor for "about BIM activity". This is a problem with Safari.
        
        **TO DO:** Can the "group mode" option in common module settings be removed? Also "ID number" and "Grade category" Added features parameter to "standard\_coursemodule\_elements"
        
        **TO DO:** Is the "mirroring" check box in configure actually preventing mirroring? YES
        
    
    - Configure  
        Once the BIM is actually created, it's necessary to do some additional configuration that isn't on the standard configuration screen. In particular, add questions and allocate markers.
        
        **TO DO:** Add some description/help to the page to give some indication of what the page is for and how to use it.
        
        **TO DO:** By default allocate the coordinator to all students. Is there a "all students" group? **Don't do this. Up to coordinator to have groups allocated.**
        
        **TO DO:** Add a message on this screen that summarises the current configuration and is especially strong on the fact that students can't register, or mirroring is turned off etc.
        
    - Manage questions
        
        **TO DO:** Add some description/help to the Manage question page to give some indication of what the page is for and how to use it. The message only shows up when there is an existing question. Not when there are no questions.
        
        **TO DO:** Able to enter question without min/max mark
        
        Can't make it required on client side because sometimes there is no new question to add.
        
    
    - Allocate markers
        
        **TO DO:** Fails if there are no markers
        
        > nvalid argument supplied for foreach() in /Applications/XAMPP/xamppfiles/htdocs/moodle/mod/bim/coordinator/marker\_allocation\_form.php on line 34
        
        . Yes, works if there are actually groups. So some error checking needs to be added.
        
        Having a question does reduce the number of errors, but not entirely.
        
        **TO DO:** Error on moodle-training
        
        > SELECT \* FROM m\_bim\_group\_allocation WHERE bim=1 and userid in ( 21, 55348, 3, 104903, 10749, 2 )
        > 
        > \* line 686 of lib/dmllib.php: call to debugging() \* line 609 of lib/dmllib.php: call to get\_recordset\_sql() \* line 930 of lib/dmllib.php: call to get\_recordset\_select() \* line 157 of mod/bim/lib/groups.php: call to get\_records\_select() \* line 30 of mod/bim/coordinator/allocate\_markers.php: call to bim\_get\_all\_markers\_groups() \* line 39 of mod/bim/coordinator/view.php: call to bim\_allocate\_markers() \* line 97 of mod/bim/view.php: call to show\_coordinator()
        
        Being caused by incorrect set up of bim\_group\_allocation table. Have fixed the XMLDBB in moodle-train, but is not taking effect. May need to reinstall after doing more fixing.
        
    
    - Manage marking
        
        **TO DO:** Show message if no marker allocation, as this means this display won't work.
        
        **TO DO:** Fails if there are no markers
        
        .
        
        **TO DO:** May also be a problem with no questions be created.
        
        **TO DO:** When a new question is added and there are no responses to it. Missing: is set to 0. When it should be all students. It's also not a link.
        
        **TO DO:** The list of unregistered students seems to include teaching staff. Need to double check how "all students" are being got. - seems to be working as required. Students role seems to have a few strange allocations
        
    
    - Find student
        
        **TO DO:** Add the hint that a "%" will show all students, which might be useful for smaller classes
        
        **TO DO:** The "show details" link in a list of students is taking us to HRMT20019.
        
        **TO DO:** When showing table of multiple matches, sometimes the "Show Details" link goes to a page saying that the student hasn't registered. Need to show "not registered" in the table.
        
    
    - Your students
        - View student details
            
            **TO DO:** Add in the number of students in the registered and unregistered tables.
            
            **TO DO:** May be a problem with the calculation of the time/date for Last post. 40 years since the last post on my blog?
            
            **TO DO:** Colour code the "Last post" cell.
            
        
        - View post details
        - Allocate post
            
            **TO DO:** After allocating a question the status in the form doesn't seem to reflect the changes.....MOSTLY DONE....drop box still says unallocated but that doesn't change operation
            
            **TO DO:** Add title of post into display.
            
            **TO DO:** Add a link for the coordinator to "process and allocate" existing posts in the database. Maybe just leave it for cron to do...but add a message on allocate to explain.
            
        
        - Mark post
            
            **TO DO:** When simply changing the allocation the post is being set to marked. Should only change the allocation. Also the drop box is keeping the value
            
            **TO DO:** Num Marked of Num Released is wrong way around. Should be released/marked.
            
            **TO DO:** Not checking that mark is within the min/max range. Can this be done on the client? It does require a number, but does not check that it is within the max/mark range - **TO DO:** Add a warning message if it goes above maximum.
            
            **TO DO:** Does the progress result total make use of the max mark for each questions?
            
            **TO DO:** Entering a large number is getting auto translated into 99.
            
            **TO DO:** When re-allocating a post, that is already marked, to a different question - need to check the mark.
            

- Student
    
    **TO DO:** Add the configuration message to the top of this page in someway.
    
    - Register blog
        
        **TO DO:** Errors when registering a successful URL and just before display the details - may have been caused by there not being any questions
        
        **TO DO:** fix up the "string" for the heading.
        
        **TO DO:** add in the "about" for the bim.
        
        **TO DO:** Add in checks to prevent common "bad" URLs that are blogs.
        
    - View details
        
        **TO DO:** Marked questions not showing up as marked.
        
        **TO DO:** Add the message about this activity to the bottom of the page.
        
        **TO DO:** Convert the details into a table, including progress. Use the same function as for the marker bim\_show\_student\_details, move to locallib
        

- Marker
    - View student details
        
        **TO DO:** If there are no allocations for a marker, i.e. no groups. Then display a message suggesting they contact the teacher in charge.
        
    
    - View post details
        
        **TO DO:** IF there are no allocations, has a failure.
        
        > ine 334 of mod/bim/marker/view.php: call to bim\_get\_marking\_details()
        
        No longer a problem as the link to post details is no longer shown if there are 0 students.
        
    
    - Allocate post
    - Mark post

### Non activities related

- Get latest copy of SimplePie.
- Registration of blog posts may be screwing up the lastpost time. My blog posts are being set to 0.
    
    **TO DO:** Check that lastpost in bim\_student\_feeds is being set correctly on registration
    
    **TO DO:** Ensure that lastpost in bim\_student\_feeds is being updated when processing feeds.
    
    **TO DO:** Check num\_entries in bim-student\_feeds is being changed at registration and mirroring.
    
- use addRule numeric on appropriate values
- Generating OPML feeds for staff? Leave till later
- **TO DO:** Is timemarked being updated by the marking process.
- **TO DO:** Add a timereleased to bim\_marking.
- **TO DO:** Get timereleased set when released.???? code is in, can't see why it isn't working. Might be due to database change. Will need to keep an eye on this.
- Check cron is working.
- Gradebook stuff. - moving to [another post](/blog2/2010/02/07/bim-talking-to-the-gradebook/)
- Deleting BIMs.
- Backing BIMs up/restoring - [Leave till later](/blog2/2010/02/07/bim-backup-and-restore/)
- Check whether a student blog url, has already been registered for this bim.

### New problem - instance in course\_module

At the moment, it appears that the setting of the instance field in the course\_module table is being corrupted in some way. Caused by the add\_instance method not returning the id as it should.