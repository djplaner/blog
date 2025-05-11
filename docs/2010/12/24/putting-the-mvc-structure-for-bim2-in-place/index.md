---
categories:
- bim
- bim2
date: 2010-12-24 10:31:11+10:00
next:
  text: The student controller for bim2 - models and view
  url: /blog2/2010/12/28/the-student-controller-for-bim2-models-and-view/
previous:
  text: Adding a bim2 activity - development progress
  url: /blog2/2010/12/20/adding-a-bim2-activity-development-progress/
title: Putting the MVC structure for bim2 in place
type: post
template: blog-post.html
---
So, bim2 is up and going, [at least in terms of being able to create an instance of the activity within a course](/blog2/2010/12/20/adding-a-bim2-activity-development-progress/). The trouble is that it can't do anything. This post starts the process of implementing the design of the user interactions with bim2. The intent is to go with a Model-View-Controller type structure in the hope that this will improve flexibility and reuse.

The plan is to reuse some of the very early work that was done with the [indicators module](/blog2/2010/05/26/adding-multiple-visualisation-approaches-to-indicators-block/) (work that has yet to be completed). The plan here is hopefully to have the basic structure of the MVC approach working in bim2, however, it won't actually do anything real. The idea is that once the structure is in place, I can work on each of the user groups separately.

### Users and state machines

The fundamental assumption of this approach is that the way in which a user can interact with bim2 can be described as a state machine. The idea is that there are a given set of web pages any user can see and a specific set of possible transitions from one web page to the next. In addition, with bim2 there are groups of users. The state machine used by a user depends on the group they belong to and perhaps where they are up to in using bim2.

For example, initially a student must complete the "register a feed" process (state machine). Once that's complete, they will be able to view details. A staff member marking blogs has one process to go through while the staff member in charge of the course has another.

The intent is to model the state machines for each group of users as a separate controller implemented using some simple models and views. The student state machine is the simplest, so I'll start with it. By doing so most of the structure will be put in place.

### Controller factory

But first, before doing that I need to put in place the structure to create the controllers. At the moment, the _view.php_ script for bim has the following code at the core \[sourcecode lang="php"\] if ( has\_capability( 'mod/bim:coordinator', $context)) { // administrator can the configure stuff show\_coordinator( $bim, $userid, $cm, $course ); }else if (has\_capability('mod/bim:student', $context)) { // student can see details of their registered blog show\_student($bim, $userid, $cm, $course ); } else if ( has\_capability( 'mod/bim:marker', $context )) { show\_marker( $bim, $userid, $cm, $course ); } else { error( "No capability to access this page" ); } \[/sourcecode\]

All this basically does is check to see what type of user is trying to use the activity and if this is determined, call an appropriate function to handle what they may want to be doing.

I'm hoping I can change this, and much of what precedes it (in total view.php in bim has 108 lines of code) into something much smaller, something like this.

\[sourcecode lang="php"\] $factory = bimtwo\_ControllerFactory::create( $context ); if ( $factory !== NULL ) { $factory->process(); } \[/sourcecode\] ($context in the above may not make sense in a Moodle module.) Also need to identify how error checking should be done properly, doubt that testing for NULL is the way to go.

### Coding standards

All of the above work was done yesterday while I was without a network connection. So some of it probably doesn't follow the [Moodle coding style](http://docs.moodle.org/en/Development:Coding_style#Classes_2). Time to revisit the work so far and bring it into line. This includes the error checking/exceptions.

First off is that class names should be lower-case english words separate by underscores.

Ahh, class member variables need to be declared. Also passing in DB, OUTPUT etc should probably be done via global.

### Capabilities - identifying type of user

The type of user within a bim2 activity is determined by the bim2 capabilities the user has. So, first I need to become familiar with how capabilities have changed in Moodle 2 (if they have) and then figure out what changes need to be done to bim2 in order to get the appropriate controller being created.

Yea, have got the old bim capabilities working fine within bimtwo. No changes required from Moodle 2.0. Just had to update for the new name of bimtwo. After lunch, shall use this to get the various controllers going - it's just doing "prints" at the moment.

### Getting the controller stuff working

So, a touch more tweaking and the controller structure appears to be working. I'll describe it below. There is a strong chance that the first reaction of many will be along the lines of "Isn't that all just a waste of time, adding yet more abstraction/indirection?". I'd be lying if I said it doesn't feel like that at times. I wonder if I'm wasting my time. However, my prior experience was positive with this approach, so I remain hopeful. Time will tell.

The main _view.php_ file, this is what Moodle calls when a user clicks on the bim2 activity, looks like this now.

\[sourcecode lang="php"\]

require\_once(dirname(dirname(dirname(\_\_FILE\_\_))).'/config.php'); require\_once(dirname(\_\_FILE\_\_).'/lib.php');

require\_once( $CFG->dirroot.'/mod/bimtwo/factory/controller.php' );

$factory = new bimtwo\_controller\_factory(); $controller = $factory->produce(); $controller->process(); \[/sourcecode\]

That's it, and that's all it should ever be.

The idea is that the _bimtwo\_controller\_factory_ examines the input and determines what type of user is making the request. Based on the type of user it then creates a _$controller_ appropriate for that user. The _process_ function for each controller then examines the input a bit more to figure out what the user is trying to do. It then calls the appropriate functions - implemented through a model and controller - to carry out that activity.

Determining what type of user is done using capabilities in the _produce_ function of the factory class. It looks like this.

\[sourcecode lang="php"\] public function produce() {

global $CFG; $path = $CFG->dirroot."/mod/bimtwo";

if ( has\_capability( 'mod/bimtwo:coordinator', $this->context)) { // administrator can the configure stuff require\_once "$path/coordinator/controller.php"; return new bimtwo\_coordinator\_controller( $this ); } else if (has\_capability('mod/bimtwo:student', $this->context)) { // student can see details of their registered blog require\_once "$path/student/controller.php"; return new bimtwo\_student\_controller( $this ); } else if ( has\_capability( 'mod/bimtwo:marker', $this->context )) { require\_once "$path/marker/controller.php"; return new bimtwo\_marker\_controller( $this ); } else { require\_once "$path/factory/controller\_error.php"; return new bimtwo\_error\_controller( $this ); } \[/sourcecode\]

At the moment, the controllers for each group of user simply produces some simply output indicating what type of user it thinks it is.

The next major task will be getting some models and views working, perhaps for the student as its the simplest class of user. But before that, I should probably return to some of the outstanding prior work.

Ahh, help files and help strings. Changes committed to git, onto help.