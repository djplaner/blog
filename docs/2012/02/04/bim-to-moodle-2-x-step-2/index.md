---
title: BIM to Moodle 2.x - Step 2
date: 2012-02-04 17:21:15+10:00
categories: ['bim2']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

_Disclaimer:_ I started this post in November 2011 and never posted it. It is essentially a development diary for some initial steps in development [BIM](/blog2/research/bam-blog-aggregation-management/) for Moodle 2.x.

It is probably of almost no value to anyone but me.

_Current status:_ A BIM activity can be added in Moodle 2.x and some of the functionality works, but not all. A fair bit of porting has to occur to ensure BIM uses all the Moodle 2.x APIs.

So I have a version of the old bim code ported to be recognised by Moodle 2.1. I doubt very much that it actually does anything as much of the code still needs to be modified to run properly in the new version of Moodle. That's the story that the following development journal entry tells.

The first step is, of course, to make sure the changes I've made are [saved on github](https://github.com/djplaner/BIM/tree/bim2) these remain unusable, but at least the changes are somewhat safe.

### Create a course

With Moodle 2.1 running on my laptop, I need to create a course in which to create bim activities. Easy enough and now to create some friendly users

- s00\[123\] - students.
- t00\[123\] - teaching staff.

And they are enrolled and all with different roles.

### Create a BIM activity

And now to try and create a BIM activity. Turn editing on, add a BIM activity....and error

> Coding error detected, it must be fixed by a programmer: Url parameters values can not be arrays!

in the course/modedit.php file.

Time to see if the server is configured to give me all the gory details about errors. Nope. Ahh, that's better

> line 60 of /mod/bim/mod\_form.php: call to MoodleQuickForm->addHelpButton()

A [quick check](http://docs.moodle.org/dev/lib/formslib.php_Form_Definition#addHelpButton) reveals the new signature. Some code changes and....

The BIM configuration screen is shown....problems to fix, include

- Help icons not showing help.  
    Problem with new signature usage. Fixed.
- The Heading is quite large.  
    Seems to be out of my hands. Will leave for now.
- The "About BIM activity" is showing up as "empty" even when data entered, which prevents submission.  
    Remove the requirement and use the intro editor

Bugger, that actually works. It is displaying the activity I've created. I have commented out all the code in view.php. But that's still a bit of a win.

At this stage, there is a bunch of code that isn't even being included in bim when Moodle 2.1 runs it. There is certain to be problems there. The current plan is to slowly uncomment and fix bits of this code. The order will, hopefully, be

- Coordinator - the teacher role configuring the activity.
- Marker - at least the subset that can be done without student feeds.
- Student.

### Coordinator

The idea here is to remove the "Yay it works" and get Moodle to run the coordinator code.

- Update ~/view.php
- Mmm, the "has\_capability" thing isn't working.  
    In the short-term, turn this off and see what the code might do.
- show\_coordinator doesn't produce any output.  
    Ahh, problem in my debugging code. Remove that and it seems to be working. Even the tabs are generated, woot.
- bim\_configuration\_screen is generating some errors, probably due to inappropriate headers etc.  
    Yes, there was a print\_footer where it wasn't needed. Actually, I can see the need to remove the header stuff from ~/view.php and push it down - as per bim. Initially this has been done. Seems to work.
- Still using print\_string and print\_heading in a lot of the code.  
    [print\_heading](http://docs.moodle.org/dev/Deprecated_functions_in_2.0#print_heading_.280.29) is deprecated.
- Each of the tabs in coordinator nav not producing output  
    This is because the code is commented out and for each one there is/will be errors.
- get\_all\_students (part of manage marking)  
    Uses an IN SQL approach that is deprecated.  
    This is something common used in a couple of places. Time to fix it. Here's a one off solution (so I remember) \[code lang="php"\] list( $usql, $params ) = $DB->get\_in\_or\_equal( $ids ); $student\_details = $DB->get\_records\_select( "user", 'id ' . $usql, $params ); \[/code\]

At this stage, the initial pages for each of the tabs for Coordinator are working. There remains additional work, but time to move onto marker.

### Marker

- **TO DO** - The help icons are not being placed nicely, nor generating the appropriate text.
- The View/Mark posts links aren't really looking like tabs  
    Add a box around it. Need to make this pretty in the next round.

### Student

- Use of record\_exists, doesn't have array.
- Remove bim's simplepie stuff and go to the Moodle default ....all working.

### Capabilities

Most of the basic code for bim2 is working, but the capabilities aren't. i.e. identifying the type of user and sending them to the right function.

Mmm, all are working, but not the coordinator.