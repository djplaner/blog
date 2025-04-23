---
title: BIM - sending results to the gradebook
date: 2010-01-26 14:27:04+10:00
categories: ['bim']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: BIM &#8211; talking to the gradebook &laquo; The Weblog of (a) David Jones
      author_email: null
      author_ip: 74.200.245.190
      author_url: https://djon.es/blog/2010/02/07/bim-talking-to-the-gradebook/
      content: '[...] the&nbsp;gradebook  One of the bigger tasks left to do is to integrate
        BIM with the gradebook. Some initial exploration has been done, this post seeks
        to document the initial [...]'
      date: '2010-02-07 21:36:14'
      date_gmt: '2010-02-07 11:36:14'
      id: '2916'
      parent: '0'
      type: pingback
      user_id: '0'
    
---

See also: [[blog-home | Home]]

Almost forgot to add this into BIM. BIM is used by staff to manage and mark feed/blog posts from students. Eventually, those marks have to be put into the Moodle gradebook so they can form part of the students final grade. This post summarises a search for information about how this can be done within Moodle and some design thinking about how to get it done in BIM.

### Activity modules sticking stuff into the gradebook

Initially, I'm using the "raw" version of [the Moodle extension development book](http://www.packtpub.com/moodle-1-9-extension-development/book) to get this information. Chapter 4 of the book covers activity modules, including talking to the gradebook. First a quick summary of what I'm reading before I start trying to understand it.

Page 60 talks about a _modgrade_ element of formslib for creating a menu for the user to select a point value for the activity. May need something like this in the coordinators view.

`gradelib.php` seems to be the API. Misc ideas from the gradebook for further lookup

- specify maximum scale.
- `grade_update` accepts an array of grades $grades = array('userid'=>$userid, 'rawgrade'=>$grade);
- parameters for grade update, based on activity module instance $params = array('itemname'=>$foo->name, 'idnumber'=>$foo->id);
- setting $params values for 'gradetype' 'grademax' 'grademin' 'reset'
- Call the grade\_update function return grade\_update('mod/foo', $foo->course, 'mod', 'foo', $foo->id, 0, $grades, $params);

So essentially, the overview is that there's a single grade\_update method that takes a collection of parameters.

I probably could of gotten that from the Moodle docs and the library file. Time to look at those next.

### Moodle resources

[Docs on grades](http://docs.moodle.org/en/Development:Grades) which includes mention of the limited public API used by activities to sent grades. Modules do not read grade tables or use the internal API. And the [docs on the API](http://docs.moodle.org/en/Development:Grades#API_for_communication_with_modules.2Fblocks).

Functions of interest in the API include:

- grade\_is\_locked($courseid, $itemtype, $itemmodule, $iteminstance, $itemnumber, $userid=NULL)  
    To tell whether a grade or grade item is currently locked. i.e. (I believe) the module can't update it. Seems to be confirmed by [this](http://docs.moodle.org/en/Development:Grades#Locked_grades). Related is if grades are manually changed in the gradebook, they become read only in the module.

This [section](http://docs.moodle.org/en/Development:Grades#Updating_module_code) talks about functions required in lib.php of a module. Suggesting that there are "many examples in official modules" with assignment being the most advanced.

There's also some [general docs on Grades](http://docs.moodle.org/en/Grades) which suggests three building blocs of the Moodle gradebook:

- the [grade category](http://docs.moodle.org/en/Grade_categories)  
    Can have its own grade formed by calculating the grades from individual items within the category. Categories may belong to other categories. All categories belong to the course category.
- the [grade item](http://docs.moodle.org/en/Grade_items)  
    An item can only belong to a single category. Become columns in the grader report. May refer to course activities or manual grades.
    
    Modules generate grade items through the Gradebook API to generate a matching grade item.
    
    The gradebook interface allows a number of settings to be edited, including a multiplicator. **Important:** This may imply that BIM only has to add up the total marks and leave the multiplicator to the gradebook. This same editing interface allows specification of whether the item is hidden or locked.
    
- The grade

### Questions

- Is there a need to provide specific functions in mod/bim/lib.php? If so, what do they need to do and how do they relate to the interface for the coordinator to control this?
- Need to learn more about the parameters and implications for the functions in the API.
- How does a item for a specific activity get added to the gradebook? Can you simply add a student's grade and the item for all students will be added OR do you need to create the item and then add student grades?
- It appears scale is related to the grademenu and specifies the [type of scale](http://docs.moodle.org/en/Scales) being used?

### lib.php required functions

It appears necessary to create some functions within the lib.php file for the module. Need to find out more. This is not something that the example from the book uses. No mention of "update\_grades" in the book. It creates a new function (no required by Moodle) called "Foo\_grade".

A search of module code for "update\_grades" finds elements in modules such as: quiz, scorm, lesson, assignment. The [subcourse module](http://docs.moodle.org/en/Subcourse_module) also provides some examples, but not using the standard lib.php type stuff.

Ahh, a [new NEWMODULE.zip](http://download.moodle.org/plugins19/mod/) includes the functions related to gradebook, at least some. Having a look now. Not all that complete, just stuff around scale. Points to the forum module.

Forum module includes the following functions in lib.php which appear to be somewhat common:

- forum\_get\_user\_grades( $forum, $userid=0)  
    Return grade for given user or all users.
    
    Based on type of forum aggregation, do different selects into forum database to get different recordset (get\_records\_sql) and apply some scaling.
    
- forum\_update\_grades( $forum=null, $userid=0, $nullifnone=true)  
    Update grades by firing grade\_updated event.
    
    Based on various conditions call various other grade update functions.
    
- forum\_grade\_item\_update( $forum, $grades=NULL)  
    For a given forum, update grade item.
    
    Wrapper around grade\_update that modifies the params based on various forum settings.
    
- forum\_grade\_item\_delete( $forum )  
    Another wrapper to use grade\_update to delete grade item for the forum.

### Current situation

It appears that there are two separate "APIs" at play here:

- The minimalist gradebook API in gradelib.php that provides the basic operations for a module to update grade items.
- The API/collection of functions that can be defined in the lib.php file of a module so that use of the gradebook API works with the module user interface.

It doesn't appear that it is necessary for you to actually use the module API. The example from the extension development book didn't. But I expect it would be good practice to do so.

I've not been able to find documentation that explains either very well. Beyond of course the actual working code of existing modules.

If you use the "module" API then you should also probably include some options in the mod\_form.php for the type of grading you want for the specific activity to be set.

Then there is this quote from the development grades docs

> Modules usually store raw grades internally and pass them into gradebook every time they change. Gradebook may also request activities to resend the grades.

This suggests that the module API functions may be important so that the gradebook can "request" the resending of grades.

### Playing with Foo

I'm going to install the Foo activity from the extension development book and observe what happens. In particular to answer question #3 from the questions section above.

- Copy the code into the moodle tree.
- Visit the site as the admin user. Upgrade/install of foo works.
- Go back to the course and can now add "Activity Foo!"
- Does include a grade menu in the mod\_form.php.  
    It seems to follow a fairly standard structure. Ahh, this is the modgrade element. Need to find out more about how this works and what it means for users and coding.
- Foo is created, but nothing is added to the gradebook at this stage.
- Use the foo. Ahh, the coordinator/teacher has no access to submit.
- What about a student? Yes, they have access. Submit.
- Has the gradebook changed? No!!!!
- Was viewing the simple "Grader report". Perhaps change has happened, but I just can't see it. No!! Try full view.

### Playing with forum

That hasn't answered any questions. Time to comment the forum grades functions and create a new one. Submitting the form has resulted in an entry being added and also some of the "comments" being displayed (to fast to see though).

Add in a die. It seems to be a call to forum\_grade\_item\_update with grades NULL and the params set to ( \[itemname\] => Another one \[idnumber\] => \[gradetype\] => 2 \[scaleid\] => 1 ) Where "Another one" is the name of the forum, and a believe the name for the grade item.

forum\_grade\_item\_update is only called from with lib.php. One of which is within add\_instance and which passes only the name of the new instance. Also called in update\_instance

### Fixing foo

So, is the problem with the foo module that it isn't creating this grade item in the gradebook before trying to add individual items for students? What does gradelib.php say that grade\_update should do?

From the comments

> Submit new or update grade; update/create grade\_item definition. Grade must have userid specified, rawgrade and feedback with format are optional. rawgrade NULL means 'Not graded', missing property or key means do not change existing.

. So it does both. The question is whether or not foo is doing it properly.

Let's do a comparison of the parameters being passed.

Here's the important bit - in gradelib.php the $grades parameter is set to NULL if you are updating the grade\_item definition.

By adding a call to grade\_update in the add\_instance of the foo activity. I've got it adding the item to the gradebook.

Some other limitations of the module are preventing me from going any further. I think I have a handle on this. Time to submit the errata.

### Suggestion for process

Based on what I've learned so far, the following is what I'm thinking of implementing.

- Modify mod\_form.php to ask for a scale and whether or not this should be graded.
- Modify lib.php functions and database to store the scale.
- Modify add\_instance and other related functions to modify the gradebook in appropriate ways.
- Think about whether we need a special function to use the grade book API.
- Think about how the updating of the gradebook should occur  
    - Grade should be just an addition of the marks to questions.
    - Should gradebook be updated when marked or when released (released?
- Have BIM simply set the raw grade, no support for scales etc, at least not initially.  
    Which means the form option will be "gradebook" or not.

Implementation will have to wait till another time.