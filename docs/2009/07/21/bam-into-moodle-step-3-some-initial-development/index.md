---
title: "BAM into Moodle - Step #3 - some initial development?"
date: 2009-07-21 15:38:21+10:00
categories: ['bam', 'moodle']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: 'BAM into Moodle Step #4 &#8211; Learning more about Moodle &laquo; The
        Weblog of (a) David Jones'
      author_email: null
      author_ip: 72.233.96.147
      author_url: https://djon.es/blog/2009/07/23/bam-into-moodle-step-4-learning-more-about-moodle/
      content: '[...] into Moodle Step #4 &#8211; Learning more about&nbsp;Moodle  In
        the previous step I got to know a bit more about the Moodle code base, libraries
        and idioms. Even got to modify a bit [...]'
      date: '2009-07-23 13:12:17'
      date_gmt: '2009-07-23 03:12:17'
      id: '2651'
      parent: '0'
      type: pingback
      user_id: '0'
    
---

See also: [[blog-home | Home]]

Okay, so Moodle is installed, configured and working. The next step, I believe, will be playing a bit with Moodle development and trying to get my head around how it works, what the abstractions are and anything else I need to know in order to actually start the design and development of "Moodle BAM".

So this means back to the Introduction to Moodle Programming course and picking things up from Unit 4 - configuring moodle for development.

### Abstractions

Two are introduced

1. Roles - a role contains permissions within a context, within a context a user can be assigned the role. Roles are inherited down the context hierarchy.
    
    Apparently a Systems Administrator can create additional roles. Users can have multiple assigned roles.
    
    1. Administrator
    2. Course creator
    3. Teacher
    4. Non-editing teacher
    5. Student
    6. Guest
2. Contexts - there's no definition of context, but we'll assume a standard one. Essentially a hierarchical set of containers
    - System (no parent)
    - Site (parent = system) - Moodle 1.8 onwards
    - Course category (parent = system)
    - Course (parent = category or system)
    - Module (parent = course or system/site(1.8 onwards))
    - Block (parent = course or system/site(1.8 onwards))
    - User (parent = system)

**Plugins** it appears this is a phrase that's used interchangeable with "blocks". Different terms, same meaning - great way to make it easy to use. Guessing this might be a historical hang over. A little later on I'm looking at the contrib source code, seems plugin is the name of a directory that is used to hold all manner of things, not just blocks. **Is this a mistake in the course docs?**

### Creating a course and some users

Have to create a course for testing, also some users. Ahh, won't let me use the same email address for different users. Will start with two users - david (staff member) and student (guess?). Will revert to numbers for the remaining. The restoring a course example worked seamlessly as well. Perhaps I spoke too soon. heading3 html elements in each topic seem to have been screwed up. The zip file was for 1.9.3, wonder if that was the problem - will ignore this for now.

### Contributed code

There's a separate "contrib" directory/project in source control. Holds a number of contributed blocks, modules etc. However, it appears to use them in an instance, you need to copy them into the Moodle directory hierarchy - in a specific place: blocks for blocks, mod for modules etc.

So, essentially its download, copy into Moodle hierarchy, visit notifications via admin block on site.

Visiting the Moodle admin page after copying a new module across, runs the config/setup for that module - appears to anyway.

**The intro to moodle programming course is suffering from the age old problem of docs for software - it's getting out of date.**

### Reflections on Moodle design for BAM

Currently, from a student's perspective, the main BAM activities that they would perform in Moodle are:

- Register your blog  
    This is where they give Moodle the URL for their blog.
- Check your progress  
    Where they see what the markers have had to say about their contributions. This is different from reading comments on the blog.

It would appear that these would have to be activities that could be added into the topics within a course. Register might be included at the start.

During the process of adding such an activity the Moodle abstraction seems to be this is where a lot of the configuration information goes. Including messages etc. This would be where the default "instructions" for BAM would go, probably .

Academic staff would require a link to the BAM Manage interface. Not sure where this would fit at the moment.

### Moodle's directory structure

Getting into Unit 5, some summary of directories covered

- /admin
    
    - Implementation of Site Administration block
    - docs list 635 files as of Nov 2007 (1.8.3) - 1.9.5 has 962.
    - admin/cron.php is how it runs regular tasks
    - modules get stuff run by cron.php by defining a \_cron function **This is where the BAM mirror process will go**
    - /blocks
        - the course offers a description of blocks again here. Would have been more useful earlier for me.
        - Each block has a directory in /blocks
    - /lang - language files for the help button content
    - /lib
        - Looks like it contains the "support" libraries for the rest of the stuff. Specifies three of the more important ones
        - moodlelib.php - main Moodle library. Contains general purpose functions.
        - weblib.php - functions that produce web output. Actually, it looks like more than web output, but that could be just misinterpreting the names.
        - datalib.php - how to access the database. And just to confuse things, also contains role capability related functions.
    - /mod - contains the key Moodle modules. **Is this where contrib modules go? Yep, it's where they said to put facetoface.**
    
    ### Global variables
    
    Interesting, says you shouldn't generally use globals in PHP and that you should never directly access the small number of Moodle global variables that break this rule. Instead you should access via the API.
    
    Most of the variables seem to use a type of OO approach. The variables are, and most server standard purposes
    
    - $CFG - configuration directives - many, not all.
    - $USER - guess?
    - $COURSE
    - $SITE
    
    A small exercise at the bottom of this section has me updating my first bit of Moodle code - yippee?. Essentially using Dumper() to show content of a global. Interesting, I didn't think the directions provided enough information for a newbie to establish exactly how to do this. Perhaps I'm skimming too much.
    
    ### Moodle libraries
    
    Contains more information about the libraries. Pointer to [XREF](http://xref.moodle.org/) site for browsing the code and finding out more.
    
    Looks at some additional libraries
    
    - lib/dmlib.php - putting records etc into the database. Low level. Not system abstractions like datalib.php
    - lib/ddlib.php - manipulating database schema.
    - lib/accesslib.php - context/roles/permissions functions
    - lib/blocklib.php - everything to use blocks on a course page
    - [lib/formslib.php](http://docs.moodle.org/en/Development:lib/formslib.php) - how to create forms
    
    **Including library files**
    
    - as little as possible.
    - almost always use require\_once
    - config.php is the most common --- first from scratch PHP file written in Moodle
    
    This will be where I'll have to start coming to grips with the differences between the Perl idioms which are essentially second nature and the approaches that should be used in PHP and then also Moodle. I'm sure that will be fun.
    
    ### More on coding guidelines
    
    **Input validation** - lib/moodlelib.php
    
    - required\_param( $parameter, PARAM\_TYPE ) - name and type of parameter that is required. NOt easy to find out what appropriate PARAM\_TYPE values there are. --- Ahh, TYPE has to be replaced with various values INT INTEGER NUMBER ALPHA. The course document actually defines them down below - but after covering other stuff. This will stop if the parameter is missing
    - option\_param( $parameter, $default, PARAM\_TYPE )
    - clean\_param( $variable, PARAM\_TYPE )
    
    It seems the use of $variables in the above is wrong - it's the actual name as the first parameter and the return value should be set $course = required\_param( "course", PARAM\_TEXT );
    
    Output functions [defined here](http://docs.moodle.org/en/Development:Output_functions)
    
    Private tokens - sesskey and confirm\_sesskey can be used to ensure private token sent in forms.
    
    ### What's next
    
    Haven't finished unit 6 - up to the stuff on roles and capabilities. Will start again from here on Thursday