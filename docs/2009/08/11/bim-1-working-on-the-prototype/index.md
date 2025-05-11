---
categories:
- bam
date: 2009-08-11 11:17:24+10:00
next:
  text: '"BIM#2 - Starting the module"'
  url: /blog2/2009/08/11/bim2-starting-the-module/
previous:
  text: Big Z&#039;s first progeny
  url: /blog2/2009/08/11/big-zs-first-progeny/
title: '"BIM #1: Working on the prototype"'
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: BIM#2 &#8211; Starting the module &laquo; The Weblog of (a) David Jones
      author_email: null
      author_ip: 74.200.244.98
      author_url: https://djon.es/blog/2009/08/11/bim2-starting-the-module/
      content: '[...] The Weblog of (a) David Jones Another voice in the blogosphere    &laquo;
        BIM #1: Working on the&nbsp;prototype [...]'
      date: '2009-08-11 15:21:16'
      date_gmt: '2009-08-11 05:21:16'
      id: '2708'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: 'eLearning and Innovation Specialist report #1: 4-20 August &laquo; The
        Weblog of (a) David Jones'
      author_email: null
      author_ip: 66.135.48.208
      author_url: https://djon.es/blog/2009/08/20/elearning-and-innovation-specialist-report-1-4-20-august/
      content: '[...] the current time period. The work during this period on BIM is summarised
        in a series of 4 posts: 1, 2, 3, and [...]'
      date: '2009-08-20 09:18:18'
      date_gmt: '2009-08-19 23:18:18'
      id: '2709'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
Over the last few weeks I've slowly been getting into Moodle/PHP as part of need to put the [BAM project](/blog2/research/bam-blog-aggregation-management/) into Moodle. I've decided today to abbreviate this project into BIM - BAM into Moodle. It'll do for now.

The [last post](/blog2/2009/07/30/bam-into-moodle-9-a-working-estudyguide-block/) left off on the development of a eStudyGuide block. I'm leaving that behind now and trying to focus on ideas/development of a prototype of BIM so that other folk can look and play with it.

### Requirements for a prototype

I think the aim will be to set up a prototype of how I think BIM will work in such a way that other people can experiment and discover what I think BIM will do. Some ideas:

- Use an old CQU course that has already used BAM.
- Set it up as a Moodle course.
- Add the various BIM links/blocks I'm thinking of initially as HTML, later as hard-coded, then display only, finally working??

I'll use the [2006/T2 offering of COIS20025](http://webfuse.cqu.edu.au/Courses/2006/T2/COIS20025/) as the prototype course. It's the first course to use BAM and I was the coordinator - that lessens issues with permission etc.

### Functionality and plans

[A previous post](/blog2/2009/07/28/bam-into-moodle-6-planning-and-some-real-coding/) outlined a list of tasks users will have to perform with BAM. Each of these will have to be integrated into the prototype and decisions made about how it will be implemented. In the following the tasks are divided into students, coordinator and teaching staff.

The end result of all that, is I need to discover the following:

- Can a Moodle module be used to add a number of different activities?  
    In this case, need to be able to add a "Create and register blog" activity for students and a "BIM Manage" activity for staff.
    
    **Yes**. It appears that this is what the Assignment activity does
    
- Can a Moodle module generate a block - or does the block need to be implemented as block? (I'm guessing the later)  
    Would like there to be a BIM block that shows different information specific to the student/staff looking at the site.
    
    May work around this by simply having a single student BIM activity. Initially it requires registration, then it shows progress.
    
- How does Moodle handle the allocation of students to a marker/staff member?  
    Is this done in the gradebook, for groups? How is done at CQU?  
    
- How can BIM put results into the gradebook?  
    Each blog post will be marked separately and then all results manipulated into a final result. That final result will generally, but not always, need to go into the gradebook. Some other courses may not use the gradebook, so I don't think BIM should be implemented within the gradebook. Just have a connection to it.
    
    This fits with the Moodle model - there's a gradebook API.
    
- How should BIM configure/connect to an assessment item within the gradebook?  
    The gradebook API?? Will check on this.

Will continue this at some later stage.

### One Moodle module - different activities

Initially I'm going to do a search for examples of a Moodle Module that supports multiple activities, however, I'm starting to feel that understanding the Moodle module/activity process might be a better way to go.

Doesn't seem to be anything easily findable via Google - perhaps says more about my grasp of the Moodle vocabulary.

Let's go via the code

- Example activities in a default install - Wiki, Survey, SCORM/AICC, Quiz, Lesson, Gloassary, Forum, choice etc.
- URL is all to mod.php with an id (course?), section, and a "add" parameter  
    Each of the values for "add" appear to match the name of a folder in the ~/mod directory. Implying, one directory, one activity.
- Interestingly, there are 7 mod.php files in Moodle. The one used here is for course.
- mod.php can be passed a range of values - add, type, indent, update, hide, show, copy, moveto, movetosection....
- Ahh, the assignments activity has options - online text, upload, offline, chat specified by a type parameter that is passed in as a parameter.

Ahh, finally found the right words for Google searches, online resources include:

- [this thread](http://moodle.org/mod/forum/discuss.php?d=89225) in a Moodle.org forum.
- [docs.moodle.org page](http://docs.moodle.org/en/Development:Modules) on module development.
- Which points to the NEWMODULE dummy/template module in the contrib code.

### Assignments activity

This activity is an example of an activity with different related tasks. Here's a description of some investigations:

- The "Add activity" drop down on a course page has sub-items for "Assignments" matching each type.  
    So, BIM could be equivalent to "Assignments" and then have two sub-types: CreateAndRegister and Manage?
- Now, does this mean a different form when adding this activity. - Add an online text - add an offline.  
    There are similarities and differences in the forms used.
- Once the assignment activities are added, they use view.php in the activity code with an ID passed. Again, it displays some information that is customised to the type.
- Those that require a form, also go via view with additional parameters.
- There's also an index.php for assignments that takes the course id and shows all the relevant activities in a page.
- The index.php is used as a link in an "Activities" block that lists all activities in a course.

### Perceived mismatch

There seems to be a mismatch here between my ideas and how Moodle works. The first time you add a BIM activity, the Moodle approach seems to be that this is when you configure BIM for the course.

Similarly, the separation of create/register and the progress activities for the student into an activity and a block may not be the best way to go. Perhaps, just a single activity - check progress or something similar.

### Grades

[Docs on the grades](http://docs.moodle.org/en/Grades)/gradebook is the place to find out about this. Some comments:

- Gradebook is designed to be the repository - modules push grades to it, gradebook doesn't go the other way.
- The pushing is done via the [gradebook public API](http://docs.moodle.org/en/Development:Grades#API_for_communication_with_modules.2Fblocks).
- Related terms include:
    - Grades - scores attributed to participants.
    - grade category - collection of grades
    - grade item - stores a grade for each participant.

Will need to read more of this eventually.

### Where next?

After all of that, it appears that a path forward might be to start work on the new module, initially as a prototype and eventually, over time, add the real functionality into it.

So that's the next step.