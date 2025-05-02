---
title: bim2 - working on coordinator - part 1
date: 2012-04-11 21:23:31+10:00
categories: ['bim2']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Bug fix and to do for BIM &laquo; The Weblog of (a) David Jones
      author_email: null
      author_ip: 74.200.247.110
      author_url: https://djon.es/blog/2012/12/28/bug-fix-and-to-do-for-bim/
      content: '[...] of an earlier attempt to investigate this, so time to revisit prior
        posts on BIM development. This post identifies the location of the [...]'
      date: '2012-12-28 11:22:07'
      date_gmt: '2012-12-28 01:22:07'
      id: '313'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
More work on bim2, this one starting work on the [previously identified tasks](/blog2/2012/04/05/bim2-whats-working-for-coordinator/). Find out what [BIM is here](/blog2/research/bam-blog-aggregation-management/).

**Status:** At this stage, the user screens from bim2 can be considered in alpha. i.e. they basically work, but there will be bugs and some of the underlying "infrastructure" (i.e. backups and restores, gradebook integration etc) need to be fixed. The current code can [be gotten here](https://github.com/djplaner/BIM/tree/bim2).

### Configure BIM improvements

- Help buttons for configuration options. **DONE**
- Have the “General Steps” actually link to the appropriate screen.
- Change “provided below” link to something more human readable. **DONE** - well kind of.

### Problem with changing the configuration

Ahh, this may be related to the gradebook issue. When the configuration calls for adding an entry to the gradebook, we're getting an error. Confirmed, if I turn "grading" off, it works fine.

This will/should be due to API changes in Moodle 2.x. The question is do I fix it now or leave it until later?

Well, as with most of the Moodle docs, it is incredibly hard to find the canonical answer. Instead, I'll have to revert to looking at the BIM code and comparing that with code in other modules.

The changing of the grade entry for configuration is done in bim\_grade\_item\_update

\[sourcecode lang="php"\] require\_once($CFG->libdir.'/gradelib.php');

$item = array(); $item\['itemname'\] = clean\_param($bim->name, PARAM\_NOTAGS); $item\['gradetype'\] = GRADE\_TYPE\_VALUE; $item\['grademax'\] = $bim->grade; $item\['grademin'\] = 0;

grade\_update('mod/bim', $bim->course, 'mod', 'bim', $bim->id, 0, null, $item); \[/sourcecode\]

The error I'm getting is "Column 'grademax' cannot be null". Mm, that will take a while to solve. Save it for later.

### Manage questions - add new not working

Okay, this seems to boil down to some changes with how to work with the [htmleditor in Moodle forms](http://docs.moodle.org/dev/Using_the_File_API_in_Moodle_forms#Replace_old_htmleditor_with_editor).

### Manage questions - improvements

- help buttons for elements to add. **DONE**
- Work on the introductory text. **DONE**

### Allocate markers

It was crashing, ended up being simple typo. Up and going.

### Manage marking

Displaying the heading, but then crashing. Problem is in bim\_get\_all\_marker\_stats. The in\_or\_equals needs to be used properly as it hasn't made the leap over...complex data structures

Need to look into the problem with html editor within form not showing data in the database. Confirmed that it is getting the data from the database.

Okay, this seems to be connected with the more complicated method for using the editor and passing data into and out of it. Surely this has to be documented somewhere???? Can't find it but I've figured out how to fix it.

### Find student

When actually doing the find generates an error in line 101 of find\_student.

get\_records\_select syntax has changed, fixed that up. Had to make some changes to the "where" part of the SQL used here.

**Note:** wondering if this will make any difference to cross-platform operation

Now the process for showing multiple users isn't working. Problem with get\_records\_select..again. Also problem with table display. Need some rewriting to get the table display working well.

Also some problems with the language strings, which look like they would've caused problems for bim 1. That's fixed. Another problem if the search finds one student who hasn't been registerd. Another hang over from bim 1. That's fixed.