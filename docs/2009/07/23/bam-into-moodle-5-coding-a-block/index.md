---
categories:
- bam
date: 2009-07-23 15:57:17+10:00
next:
  text: Wicked problems, requirements gathering and the LMS approach to e-learning
  url: /blog/2009/07/24/wicked-problems-requirements-gathering-and-the-lms-approach-to-e-learning/
previous:
  text: 'BAM into Moodle Step #4 - Learning more about Moodle'
  url: /blog/2009/07/23/bam-into-moodle-step-4-learning-more-about-moodle/
title: '"BAM into Moodle #5 - Coding a block?"'
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: 'BAM into Moodle #6 &#8211; Planning and some real coding &laquo; The Weblog
        of (a) David Jones'
      author_email: null
      author_ip: 74.200.246.66
      author_url: https://djon.es/blog/2009/07/28/bam-into-moodle-6-planning-and-some-real-coding/
      content: '[...] into Moodle #6 &#8211; Planning and some real&nbsp;coding  The previous
        post in this series started me along the lines of actually coding something in
        Moodle. It was only a [...]'
      date: '2009-07-28 11:27:48'
      date_gmt: '2009-07-28 01:27:48'
      id: '2653'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
Up to Unit 7 of the [introduction to Moodle programming course](http://dev.moodle.org/course/view.php?id=2), this one is titled "Replicating a moodle block". So the programming begins.

### Creating a simple block

Looks like we'll be doing most of the standard stuff, adding tables, using forms CRUD...Staring with [this tutorial](http://dev.moodle.org/course/view.php?id=2) from the Moodle site. THe process

- Create a single file in a single directory  
    ~/blocks/_lowercase name of block_ is the directory and block\__lowercase name of block_.php is the file.
- File format:
    - first line is block class definition - fixed naming convention
    - class must have an init() method - initially to set to class member variables title and version
    - get\_content - required before it will display something on screen

Bugger, laptop migration didn't work 100% with permissions - XAMPP is playing silly buggers, and now so is Moodle. Ahh, CVS wasn't brought across in the migration either. Bugger, Apple developer CDs - long time to download to get CVS.....

Okay, back to it.

Misc other stuff

- instance\_allow\_config method returns true to allow instance configuration
- config\_instance.html - used to specify HTML/PHP/Moodle functions to implement form to allow configuration
- can't use config variables in init section of blocks
- specialization method is automatically called after init - used to apply config i.e. to specialize the block
- instance\_allow\_multiple method allows multiple instances of the block for a single course - if it returns true
- has\_config - indicates global configuration exists if it returns true - i.e. allows application of config to all instances in all courses.
- config\_global.html - specify HTML form for global configuration

### Skip to Unit 9 - requirements documents

While that's downloading, time to move on. Will need to think about a requirements document some time soon to keep the organisational hierarchy happy and it will probably not require any code. Onto unit 9 - [requirements documents](http://dev.moodle.org/mod/resource/view.php?id=69).

Ahh, believes a requirements document will reduce feature creep - philosophically I disagree with this. It allows the developer to ignore the user's growing knowledge of what they'd like to do with the application. It closes off possibilities - or at least that is how it is used.

It's all fairly standard requirements document guff, little specific to Moodle. Most of it is just really limited in being of any use in a real situation.

This [section of the Moodle developer docs](http://docs.moodle.org/en/Development:Overview#Major_Development) seems to be a bit more useful and talks about creating a specification in Moodle docs. This [one](http://docs.moodle.org/en/Development:Grades) is used as the example.

. Some other alternatives include: [specification of Workshop 2.0](http://docs.moodle.org/en/Development:Workshop_2.0_specification), [blog improvements](http://docs.moodle.org/en/Student_projects/Blog_improvements).

This will have to come later.

### What's next?

Looks like the reinstall of Moodle is going to take a while. Running out of time today. Not all that productive - but that's what you get for changing laptops.

At this stage, it looks like it will be time to move onto the planning and documentation. Which also implies doing a presentation at CQU to generate more requirements. The interesting part of this will be working out which of the types of plugins (or how many of them) BAM will required.

For example, for students, registering their blog and checking marking progress could be thought of as activities. Configuring BAM for a course could, as it stands, be for an assignment. However, I'm not sure I want to limit use of BAM only for assessment. Why not use it as a basis for a course blog - aggregate - oops, is this feature creep?