---
title: Adding restore to BIM
date: 2013-01-01 16:09:38+10:00
categories: ['bim', 'bim2']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

The following reports on the process to complete the backup/restore functionality for [BIM 2.0](/blog2/research/bam-blog-aggregation-management/). Backup is currently working. Time to add the ability to restore those backups. It draws on the process described in [this documentation - "Restore 2.0 for developers"](http://docs.moodle.org/dev/Restore_2.0_for_developers). Which doesn't appear anywhere as detailed/sequential as the backup 2.0 documentation.

This and some simple mistakes on my part meant the following was spread over a couple of days, rather than a hours as I'd hoped. Restore is currently working, at least according to the tests I've done.

BIM 2.0 might officially be considered alpha code ready to play with. I still need to work through the [issue list](https://github.com/djplaner/BIM/issues) on GitHub before it's truly ready for action.

Back to work tomorrow so BIM development will slow down a bit, though it does remain a priority. Most of the family is heading off on Friday/Saturday, so I might have a bit more time then.

## The process

Two main files restore\_bim\_stepslib.php and restore\_bim\_activity\_task.class.php. Skeleton code is provided. Create those and see if I can figure out what modifications are required.

Confirmed these files are meant to go in the backup directory.

stepslib.php changes

- replace choice with bim.
- define\_structure - replace choice components (option and answer) with bim components (allocation, question, feed, marking) \[code lang="php"\] $paths\[\] = new restore\_path\_element('bim', '/activity/bim'); if ( $userinfo ) { $paths\[\] = new restore\_path\_elements( 'bim\_allocation', '/activity/bim/allocations/allocation' } $paths\[\] = new restore\_path\_element('bim\_question', '/activity/bim/questions/question'); if ($userinfo) { $paths\[\] = new restore\_path\_element('bim\_student\_feed', '/activity/bim/student\_feeds/student\_feed'); $paths\[\] = new restore\_path\_element('bim\_marking', '/activity/bim/markings/marking'); } \[/code\]
- replace the methods process\_choice, process\_choice\_option, process\_choice\_answer with bim equivalents  
    These are responsible for inserting the data extracted from the XML back into the database. There are three parts of this that need to be explored more
    
    1. apply\_activity\_instance in process\_choice, would appear to be used to convert the choiceid in the data to the new element inserted into the database. Apparently only called when adding initial information about the activity.
    2. set\_mapping appears to be used to convert the activity id for the subsequent elements inserted into the database.
    3. add\_related\_files - part of a broader area that needs exploration.
    
    Will need to put in code for the following bim methods, would appear to be a link between the method names and the first parameter in the restore\_path\_elements calls above.
    - process\_bim - done
    - process\_bim\_allocation - there's also a need to "get\_mappingid" for user and group information
    - process\_bim\_question - done
    - process\_bim\_student\_feed - done
    - process\_bim\_marking - done

restore\_choice\_activity\_task.class.php

- define\_decode\_contents - identify the elements that need to have the link decoded run. Will stick for just the intro for BIM.
- define\_restore\_log\_rules - not sure.
- define\_restore\_log\_rules\_for\_course - purpose of this not real clear. Apparently choice specific? Leave it out for now.

### Running it and failing

The code except on the restore 2.0 page doesn't seem to work. Tried a backup and restore via Moodle itself. Backup apparently worked and the restore successfully created the new course. However, the BIM activity was not there.

So there is a problem. The limited nature of the documentation makes this an "interesting" problem to solve.

Check the backup file to see if the bim information is there. Yes. It definitely appears that backup is working.

Time to do debug on restore and try and identify where the failure is occurring. Would be nice if the command-line script was working. Having to do this by the Moodle web interface. Will a Google search reveal anything?

The restore picks up the presence of the bim activity in the confirm stage. Including the fact that it has userinfo saved. But on the settings page (i.e. as part of the preparation for restore, it doesn't show the bim2 activity). This is done by the moodle/backup/restore.php script. Which is implemented using a fairly complex OO structure (compared to 1.9). restore\_ui.class.php does much of the work, drawing on other files.

The bim activity is showing up in some aspects at the start of scheme, but there is something that is preventing it from being included when the sections are displayed.

The "Confirm" stage of the restore is showing the BIM activity as part of Section 0. This appears to be extracting information straight from the MBZ (the Moodle backup file) using "backup\_general\_helper::get\_backup\_information" and then a renderer to show it.

Idiot!

After much wasted time I have figured out the silly mistake I made and can perhaps start making some progress.

## Debugging the completed restore

So it now restores and the BIM activity is present, some problems though

- There are no questions brought across.
- Nor marker allocations
- Nor student feeds, all students are unregistered.

None of the data for the newly restored bim activity is getting restored into the database. There is a new entry in the main bim database, but beyond that nothing.

Essentially only the main configuration stuff has been done correctly. Will need to check

1. Is this information in the backup? - in short yes, but  
    Not sure about the nesting of some of the elements in the backup. It looks wrong \[sourcecode lang="xml"\] <feeds> </feeds> <feed id="1"> <bim>1</bim> <userid>3</userid> <numentries>10</numentries> <lastpost>1355868586</lastpost> <blogurl>http://davidtjones.wordpress.com</blogurl> <feedurl>https://djon.es/blog/feed/</feedurl> </feed> \[/sourcecode\] Shouldn't the feed elements be nested within the feeds elements? Need to check this. Create some data in the forum and do a backup again. As expected, it should be nested.
    
    The building of the tree in backup\_bim\_stepslib.php is incorrect. Fix that and do another test. Bingo. Now try a restore.
    
2. Are there errors in my restore code causing the absence?  
    Mmm, now there is a missing method for bim\_grade\_item\_delete in bim/lib.php. Mm, that was commented out. Removed and now onto next error.
    
    'itemid' cannot be NULL on an insert into mdl\_backup\_ids\_temp. Again, this comes down to a problem with the backup not being done correctly, or some error in the restore. It's a problem with a bim\_question. The backup looks fine.
    
    The problem is in restore. The individual "process\_" methods for each component is not complete. Not setting up the variable $oldid. Will also need to double check the mapping of each field in each of these. But first, does this fix the problem? Nope.
    
    Need to figure out where this is/isn't happening. Ahh, a bit of debugging code and run it again and it appears to complete without the error. A good sign I hope.
    
    Check the database. Nope, nothing being added in the student\_feed, questions, allocations tables. Clean up the database and try one more restore prior to re-checking the restore code.
    
    Okay the problem was with how the bim id was being used in each of the child element methods. i.e. $data->bimid should have been $data->bim. That fixed and much of it is now working. Data is being placed into each of the bim tables from the backup.
    
    However, the problem now is that some of the necessary connections between tables is not being maintained in a consistent method. For example
    
    - question field in bim\_marking is pointing to the question ids from the backed up bim activity and not the newly restored bim activity.  
        So I need to figure out how to get the new id for a question after it has been inserted into the database and update the element for bim\_marking on that basis.
        
        The process\_bim\_question method does call set\_mapping with bim\_question and the old and new ids. This would seem to be the mechanism for saving this information. The question now is how to retrieve and use it.
        
        The discussion forum backup code reveals the expected get\_mappingid. And that works.
        
    - bim\_student\_feeds is not being updated.  
        Due to a problem in the specification of the XML....that's working.
    

### Final testing

Due to the misc. problems with backup and restore the database is not exactly clean. I need to clean it up and then retest the backup and restore process. This will also provide an opportunity to do another set of tests on the other components of the bim activity.

1. Delete all the restored courses - DONE
2. Delete the bim activity on the good course - DONE
3. Check the bim database tables.  
    **Check:** data left in bim\_student\_feeds bim\_marking bim\_questions bim\_group\_allocation  
    This may simply be left overs from prior testing gone wrong. Will need to retest this below.
4. Create a new bim activity in the good course. - DONE
5. Allocate some marking. - DONE
6. Create some questions. - DONE
7. View the bim activity via a student account - DONE
8. Register a blog for that student via the coordinator interface - DONE
9. View the bim activity again as that student - DONE
10. Register a blog as another student - DONE
11. Allocate a question or two - DONE
12. Mark two questions - DONE
13. Release a question - DONE  
    Generates an error to be checked. Added as an issue to github
14. Do a backup - DONE
15. Do a restore - DONE
16. Check the bim database tables - DONE  
    REstored bim has id 15. All three questions there. The two feeds are there. Group allocation and marking also seem good.
17. Compare the restored bim activity with the original. - DONE
18. Repeat the first few steps to double check deletion from database. - DONE  
    **Check:** Deleting a course does not remove all of the data in the other bim tables (question, group\_allocation, feeds, marking)

Will add a few things to the github issues list.