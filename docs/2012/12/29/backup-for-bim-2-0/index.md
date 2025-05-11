---
categories:
- bim
- bim2
date: 2012-12-29 17:46:05+10:00
next:
  text: Adding restore to BIM
  url: /blog2/2013/01/01/adding-restore-to-bim/
previous:
  text: Major (Moodle) requirements for BIM 2.0
  url: /blog2/2012/12/29/major-moodle-requirements-for-bim-2-0/
title: Backup for BIM 2.0
type: post
template: blog-post.html
---
What follows is a journal of the attempt to bring [BIM 2.0's](/blog2/research/bam-blog-aggregation-management/) backup functionality into line with the new approach in Moodle 2.x.

Done. Appears to be all working. Will work on restore next and do some testing.

## Backup

First up is trying to understand the [developer docs on the new backup process](http://docs.moodle.org/dev/Backup_2.0_for_developers). What follows is an attempt to both summarise/understand those docs and explain what changes I've made to BIM 2.0. The [Backup 2.0 general architecture documents](http://docs.moodle.org/dev/Backup_2.0_general_architecture) are also used.

What I believe it all boils down to is the ability to convert the database structure for a BIM activity into an XML file/structure. The aim here will be to keep the XML structure produced as close to that produced by 1.9 as possible.

Steps required

1. Preparation - knowing what to backup  
    Much of this is done in the "BIM data" section below.
    1. Draw the DB schema.
    2. Identify where the user information is located in the schema.
    3. Determine correct order of backup.
    4. Identify attributes and elements.  
        All "id" fields should be attributes.
    5. Identify not needed elements.  
        Any field except those in parent elements should be included.
    6. Identify the file areas used.  
        Text fields and attachements appear to fit into this sector. This appears to be a bit new in Moodle 2.
    7. Annotating important bits  
        e.g. the ID fields.
2. Remove the old backup stuff.  
    Basically backuplib.php in the bim directory.
3. Tell Moodle that BIM 2.0 is supporting backups.  
    Add the following to mod/bim/lib.php\[code lang="php"\]case FEATURE\_BACKUP\_MOODLE2: return true;\[/code\]
4. Set up the directory for the code  
    create mod/bim/backup/moodle2
5. Set up and test the backup process (which won't work at the moment).  
    The backup documentation includes a simple script that speeds up the develop/test cycle for backups. put that in place and run it. Breaks as expected
6. Start putting in the code
    1. create empty mod/bim/backup/moodle2/backup\_bim\_settingslib.php
    2. backup\_bim\_stepslib.php - another empty file
    3. backup\_bim\_activity\_task.class.php the place the above files are used. For now just some skeleton code with empty methods.
7. Run the backup again.  
    Which runs without error as expected.
8. Create the bim.xml file - as an empty file
    - Some empty code into backup\_bim\_stepslib.php
    - Call the method from the steps file from backup\_bim\_activity\_task.class.php.
9. Now to define each of the elements essentially a translation of the provided code with the description of the bim data below. This produces an empty backup file for bim.
10. Define the tree of data following the skeleton code.
11. Connecting it all to the database  
    A fairly simple set of method calls building on the above. Tested and all seems to be working. Woo hoo!
12. Annotating IDs  
    This appears to be [related to signposting user](http://docs.moodle.org/dev/Backup_2.0_for_developers#annotate_is_important) (and other) information, something I missed the first time.  
    For BIM, the relevant fields to annotate are user and group.
13. Annotating files  
    **Not sure about this section. Need to read some more and update.**
14. Encode references to URLs?  
    Done as per example.

## BIM Data

The following is based on [this 2010 post](/blog2/2010/02/07/bim-backup-and-restore/) documenting the development work on the backup process for BIM 1.0. With some extra work based on the preparation information from above.

The bim data hierarchy (bullet points represent table names)

- bim  
    id (attr)  
    course (not needed) \*\*\*\* CHECK IF THIS IS INCLUDED \*\*\*\*  
    name  
    intro (????file area???)  
    introformat  
    timecreated  
    timemodified  
    register\_feed  
    mirror\_feed  
    change\_feed  
    grade\_feed  
    - bim\_group\_allocation  
        id (attr)  
        bim (not needed)  
        groupid  
        userid  
        
    - bim\_questions  
        id (attr)  
        BIM (not needed)  
        title (???? file area ???? )  
        body (??? file area????)  
        min\_mark  
        max\_mark
    - bim\_student\_feeds  
        id (attr)  
        bim (not needed)  
        userid  
        numentries  
        lastpost  
        blogurl  
        feedurl  
        
    - bim\_marking  
        id (attr)  
        bim (not needed)  
        userid  
        marker  
        question (this is an id back into bim\_questions)  
        mark  
        status  
        timemarked  
        timereleased  
        link (???file area??)  
        timepublished  
        title (??file area??)  
        post (?? file area?? )  
        comments (?? file area??)

In BIM 1.0 the user data includes: student feeds, marking and group allocation.