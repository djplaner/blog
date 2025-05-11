---
categories:
- bim
- bim2
date: 2010-12-28 16:07:14+10:00
next:
  text: BIM as a Wordpress plugin?
  url: /blog2/2010/12/29/bim-as-a-wordpress-plugin/
previous:
  text: Putting the MVC structure for bim2 in place
  url: /blog2/2010/12/24/putting-the-mvc-structure-for-bim2-in-place/
title: The student controller for bim2 - models and view
type: post
template: blog-post.html
---
bim2 now has a working [controller structure](/blog2/2010/12/24/putting-the-mvc-structure-for-bim2-in-place/), but it doesn't do anything. This post summarises initial attempts to implement the student controller so that it actually implements the state machine for the student interactions. It's also the first attempt to implement some models and views with the MVC structure for bim2. This is liable to raise a range of questions about design, testing and other tasks.

### A change?

The existing bim student set of interactions is limited to essentially two phases

1. Register a feed; and
2. View details of existing feed.  
    This is the everything bim knows about the student and the feed on one page.

There is some room for improvement and Mark Pea has made [some suggestions](https://github.com/djplaner/BIM/issues#issue/26) which are really good. Am thinking I'll adopt and adapt them

Arising from that, current thinking is that there will be three main bim2 pages for students.

1. Activity details;  
    This is the default bim2 activity home page for students. It would always show the description of the bim2 activity as entered by the person who created the activity. It would also show a summary of what is known about the individual student's bim2 with three main options:
    1. Unregistered;  
        Before the student has registered the URL for their feed, the page would show the textbox to enter the feed url and help information/links.
    2. Registered; and  
        Once registered it would show a summary of the information known about the student's participation in bim2 activity.
    3. Unable to register;  
        In this state, the bim2 activity has been created, however, the creator has turned off (or not turned on) the ability for students to register their feed. This is actually a slight modification/cross cutting state to the other two options for this page.
2. Questions;  
    This will be a summary of the questions the student has to respond to via their feed. the questions are created by the person creating the bim2 activity. This should probably show information about when/if the student has responded to the questions.
3. Your posts;  
    This is where bim2 shows what posts it has mirrored from the student's feed. It should also be where the student can allocate (unallocated) posts. This would be a new feature.

Mmm, am thinking it will be a good idea to create hard-coded prototypes for these pages to play around with the information that will be on them. This is a normal practice I got into with the previous development environment, but haven't really gotten into with bim/Moodle.

### Hard-coded views

The idea here is to get a version of bim2 code working with hard-coded templates. i.e. I (or anyone else who downloads it from [git](https://github.com/djplaner/bimtwo) can see what is planned. Hopefully, the following outlines the implementation of this plan. It essentially means that I need to get the basic models and views for the student controller implemented.

But first, that means putting a bit more meat on the bones of the controller, which is essentially an empty function with some "hello world" code.

First step is how to identify the specific page to be displayed. With bim there are three components that are combined to figure out what to show the user

1. The type of user;
2. The "tab" to show;  
    The staff interfaces are "tabbed". The value for the tab parameter specifies which tab.
3. The "screen";  
    A particular tab may have a set of operations that can be operated. This specifies which one. Screen was the wrong choice, will go for _op_ instead.

So, the idea is that the student controller's _process_ function has to examine the value of the parameter _tab_ and then the parameter _op_ to figure out what to do. Given this is what each controller will do, makes sense to put this into the base controller class and get the constructor to do it automatically....if that's how php OO features work. Let's test. Yep, that's how it works.

Of course, this raises the point that perhaps somewhere in here, checking the valid values for tab and op can be semi-automated. That includes the idea of actually calling the appropriate function to handle the task based on the value of tab and op. e.g. what was used in the perl-based system I worked on was a hash of hashes leading to a function name. If there wasn't a value for the particular combination of tab and op an error was produced. If there was, the function name was called to produce the necessary output. (The question fast approaching here will be how this works with the form processing in Moodle).

Ahh, the data structure approach to calling methods seems to work in PHP

\[sourcecode lang="php"\] function process() { $methods = array( "hello" => "doit" ); $this->$methods\['hello'\](); }

function doit() { \[/sourcecode\]

Playing around a bit more I get the following for the student controller

\[sourcecode lang="php"\]

function process() { $methods = array( "default" => array( "default" => "activity\_details" ), "activity" => array( "default" => "activity\_details" ), "questions" => array( "default" => "questions" ), "posts" => array( "default" => "posts" ) );

if ( isset( $methods\[$this->tab\]\[$this->op\] )) { $function = $methods\[$this->tab\]\[$this->op\]; $this->$function(); } } \[/sourcecode\]

The idea is that the _methods_ array defines the set of valid methods and parameters for the student controller. So, if _tab=activity_ and _op=default_ then the _activity\_details_ method would be called. I've added in some more smarts into the base controller class. If tab or op are empty strings, it automatically sets them to _default_.

The actual code for calling the functions should probably be in the base controller class with the method data being specified in the constructor in the specific controller. Wonder if that will work? Yep, that works. So the "isset" stuff is in the base controller and the student controller has a constructor that sets up methods.

This is almost certainly reinventing the wheel (with a few corners) and sounding like a waste of time. But the theory is that this bit of work at the beginning will make for a more flexible bim2. i.e. it will be quicker to improve and change bim2. This is fast becoming an experiment on whether this is likely to happen. It feel's like I'm trading the complexity of large procedural functions for the complexity of class relationships.

### A "working" bim2 for students

So with this basic infrastructure in place, time to move onto getting the methods in place to display some appropriate information for the students.