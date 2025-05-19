---
categories:
- bim
date: 2010-01-07 12:02:53+10:00
next:
  text: BIM - getting navigation bread crumbs and tabs working
  url: /blog/2010/01/09/bim-getting-navigation-bread-crumbs-and-tabs-working/
previous:
  text: BIM - the show student posts screen
  url: /blog/2009/12/26/bim-the-show-student-posts-screen/
title: BIM - Allocate questions screen
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: BIM &#8211; getting navigation bread crumbs and tabs working &laquo; The
        Weblog of (a) David Jones
      author_email: null
      author_ip: 74.200.245.186
      author_url: https://djon.es/blog/2010/01/09/bim-getting-navigation-bread-crumbs-and-tabs-working/
      content: '[...] The Weblog of (a) David Jones Another voice in the blogosphere    &laquo;
        BIM &#8211; Allocate questions&nbsp;screen [...]'
      date: '2010-01-09 11:47:17'
      date_gmt: '2010-01-09 01:47:17'
      id: '2909'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
[The last bit of work](/blog/2009/12/26/bim-the-show-student-posts-screen/) I did on BIM continue the current trend of getting screens mostly working without some of the extra effort required for a production system. This is in part driven by my desire to become more familiar with differing aspects of Moodle development.

This post continues that trend by describing the implementation of the "allocate questions screen". This is the screen used by a teacher to change the allocation of student posts to questions. A basic premise of BIM is that for a given course students are expected to respond to particular questions. BIM attempts to automatically detect student posts that answer a question and allocate them appropriately. Sometimes, however, there is a need for some manual intervention.

This screen shows a list of all the student posts recognised by BIM, including a specification of which have been allocated to which questions. The teacher can then modify the allocation.

### Required data

The screen is passed the user id of the student and should also be passed the id of the course\_module (course, bim id etc).

- Student user details.
- Markers students (is this student on the markers).
- Summary statistics about marking/submission.
- A progress result in terms of overall marking.
- List of all posts for the student - contents of bim\_marking
- Details of the students feed
- List of all questions for the course.
- Course weeks?  
    The CQU version/BAM converted the time/date posted into the week of the CQU academic term. If a Moodle course is divided into weeks, it might be possible to do the same thing here.

### Implementation questions

- How/should the date/time of a post being posted be converted into the weeks used by the course (if in the weekly structure).
- This will have to include a form and drop down boxes to change the allocation. Need to figure out how this will work (have idea, but needs to be checked).

### Get the data

Most of these are from previous screens or straight forward.

- Student user details.
- Markers students (is this student on the markers).
- Summary statistics about marking/submission.
- A progress result in terms of overall marking.
- List of all posts for the student - contents of bim\_marking
- Details of the students feed
- List of all questions for the course.
- Course weeks?  
    The CQU version/BAM converted the time/date posted into the week of the CQU academic term. If a Moodle course is divided into weeks, it might be possible to do the same thing here.

### Show the data

Two main parts:

- Details table - summary of student details, progress result, num answered/marked etc. **DONE**
- Blog posts - a list of all the blog posts by the user
    
    Going to initially simply implement this is a collection of tables, with no form elements. Get that working and then think about the forms stuff.
    

Okay, the table is working. However, there are a number of questions to be answered:

- Need to get the title of the question to display from the qid.  
    Always good to start with an easy one. The data was there, just had to reference it.
- How to display the timepublished as a human readable time?  
    It may be possible that the methods used to set this time in the database (during creation of the test database) may have been incorrect.
    
    Yep, this is the first problem. I haven't handled the conversion from DATETIME in BAM to the bigint used in Moodle. Have to look at that.
    
    [This discussion forum thread](http://moodle.org/mod/forum/discuss.php?d=55719) explains the usage of UNIX time and methods to go back and forth. Including a pointer to [this online converter](http://www.onlineconversion.com/unix_time.htm) that I'm using for some initial testing. ANd the [PHP date function](http://php.net/manual/en/function.date.php).
    
    Suggests the need to do a complete update of the timestamps in the bim\_marking table.
    
- How to include the form stuff to work appropriately?  
    The requirement is to have one form per post with a drop box that allows allocation to another question (or unallocation).
    
    This comes back to having to grok the moodleforms stuff and how that works. A bit of hunting around and I seem to now have a better handle on it. That will be tomorrow's job.
    
    Ok, time to revisit BAM and see how it is done. A single form for the whole page, each drop box has a name that uniquely identifies the post (uses link, but with BIM can probably use post id)
    
    Finally getting the hang of using formslib.php, including customdata. Part of it is getting back into coding and getting familiar with PHP. The form is being created now. Two tasks to complete: include the title of the post in the header, and process the form.
    
    **Post title** is usually included in the allocate page. Trouble is it's not stored in the dbase. Need to get it from the RSS file that is cached. I could get it from there, but that raises some questions about caching (e.g. what happens if the student posts lots and their blog engine only puts the last X posts in the RSS file?). For now, will not include the title.
    
    **Process the form** Should be able to follow the standard process. Things to check:
    
    - How to get it to auto-submit when a allocation is made?  
        Setting some attributes in the select box for "this.form.submit()". **DONE**
    - What's the URL being generated by the form? (Has to go to the right place)  
        Will need to add some hidden variables. **DONE**
    - Where should that be handled in the view.php?  
        Looks like it should be handled just after when the form is created as it stands. But this raises questions about the first run, when the form data isn't being passed in. Ahh, there's `is_submitted` as a method that helps there. **Done**
    - How should it be handled?  
        Essentially I need to get the data about which of the select menu was changed. The `get_data` method is meant to return the form data, trouble is it's currently only returning the hidden values. Not the values in the select menu chosen.
        
        Is this a problem caused by using the Javascript onchange function? Let's put a submit button in and use it instead. Nope, that doesn't make it work either.
        
        So, is there something else I'm doing wrong? Yep. I was putting a space in the name of each select box. Which meant the first part of each one was the same as the others. Remove the space and with the submit button it shows up. Yep, that fixes the problems with the javascript approach as well.
        
        The only change that a user can make is to one of the allocations. This is shown in the parameter "Reallocate\__id_" (where id is from bim\_marking) is not default. The value of the parameter will be the qid or Unallocated (i.e. not "default"). Have that checking in place.
        
        That all seems to be working.
        
    - Add a link back to the Show Post Details screen.  
        This type of thing, was going to be done - at least in part - with tabs once I figured out how to get them working. This is slightly different.
        
        One option might be to change the bread crumbs in the navigation for the view.php for the bim module. Trouble is, that currently this is done prior to the smarts in the form processing. It looks like I need to move the navigation building down into the processing.
        
        Intent is to create a stand-alone function - bim\_build\_navigation - that I can move around at will until working. This is requiring a fairly major refactoring of the code. Surely there has to be a cleaner way to handle this.
        
        This work deserves its own post.
        
    

### What's left to do

Allocate posts is essentially working.

- Need to reduce the size of the right hand column in the details table.
- Update the timepublished field in bim\_marking to be correct UNIX timestamps.
- Question of converting a given date/time to a specific week within a Moodle course (if using that course structure).
- Some additional testing and tidying up.
- The breadcrumbs will need to be fixed.
- Breadcrumbs for the student view will also need to be revisited.
- Think about adding the "next/prev" student mechanism for allocation and mark.

The next steps in BIM development should probably be:

- Nut out the breadcrumbs for staff and students (so far).
- Maybe get some screen dumps out to current users.
- Get the marking page done.
- Start thinking about the configuration/creation/management interface. (This is linked to the tab interface).