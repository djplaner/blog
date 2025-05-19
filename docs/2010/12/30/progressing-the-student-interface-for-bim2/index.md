---
categories:
- bam
- bim
- bim2
date: 2010-12-30 12:33:34+10:00
next:
  text: A command for organisations? Program or be programmed
  url: /blog/2011/01/06/a-command-for-organisations-program-or-be-programmed/
previous:
  text: BIM as a Wordpress plugin?
  url: /blog/2010/12/29/bim-as-a-wordpress-plugin/
title: Progressing the student interface for bim2
type: post
template: blog-post.html
---
The [last post](/blog/2010/12/28/the-student-controller-for-bim2-models-and-view/) ended up with the basics of the student controller and views functioning to produce some simple output. The aim here is to get the entire student interface up and actually reading data from the database. It won't be completely finished. There will be some additional extra features to add. The aim here is to iron our the design of the whole model/view/controller set of classes.

Am going to release this post before it is finished and continue working on it. So it will change.

### To do list

- Help strings are not displaying consistently using either breakdown and also problems with identifiers of the help strings....**Is this a problem with the version of Moodle 2 I have?**
- rationalise the filenames and object names for all of student. Feed into design approach for other users
- Show questions
    - get\_string not replace place holders with values.
    - add in support for due dates for questions.
    - include information about questions answered by the student, also details about whether its marked etc.
- The show questions stuff can/probably should be re-used for staff, especially markers.
- Need to read up more about the proper approach to using OUTPUT and PAGE in generating output, there's a limit to how far simple copying can take you.
- Setting the URL for the tables in show questions and posts, probably also activity details.
- Show posts
    - Need to add user/blog/post summary/details at start
    - Need to test posts of various statuses.
    - Add in the option to allocate posts.
    - Is there a chance to add an internal navigation that allows jumping to individual posts
    - The "Allocated to:" value in details should be link, maybe a popup, to the question
- Check that the views are setting the URL appropriately -- e.g. does "tab" need to be included? is it?
- Consider using html\_table rather than flexible\_table for some of the tables.
- Need to look into table classes and setting styles on cells etc. to ensure table format okay

### Student tabbed interface

Each of the user groups will be using a tab interface to access the different services, so have to get this up and going. After a bit of playing have this working by having the tabs declared in the controller and then having the view figure out how to display them...which is how the division of responsibilities should theoretically work.

Well, that's working for the student views. Able to move between them all as a student with a registered blog. Need to work on the tabs for unregistered..where the other two tabs are inactivated. Actually, that works fine.

### Models and object/relational mapping

The intent is that each individual page will have a model that is responsible for retrieving and manipulating all of the data required for page. That model is passed to the view which uses the data to display the necessary output. Some, if not all, of that data will be retrieved through classes that are essentially object/relational mapping objects.

I'm planning to implement the first of these with the student controller/views. Will start with the questions page as this is the most straight forward. It should simply display all of the questions that have been set for this activity.

#### Put in some data

I'm going to manually insert some test data into the database. The data will be taken from test data from bim.

#### Questions

The intent is to minimise the need for the main bim2 code to know a great deal about the tables and fields in the database. Hide all that behind a specific object, _bimtwo\_questions_. Since Moodle already does much of this, this objects are likely to be fairly simple wrappers (and yes that does raise the question of why add the extra layer of abstraction...) One answer to that question is that some of the objects will have fairly high level methods that will perform important tasks on the data.

These o/r objects are going to sit in the lib directory for now.

The _bimtwo\_questions_ object is going to take the _bimtwo_ identifier and retrieve all of the questions for that bim2 activity from the bimtwo\_questions table.

At the moment, there will be little or no methods for the class. This is likely to change later when the idea of due dates for questions gets added. Methods to determine which questions has passed the deadline etc seem likely.

Data that will be required includes

- questions - the list of questions for the activity;
- answered questions - the list of questions the student has answered.

Okay, simple model up and going. Let's get it displaying the content in a reasonably nice way. This means identifying how to produce pretty tables in Moodle 2.0. Seems good old flexible\_table remains. However, it's gone to a oo based implementation.

Well, show questions is working, at least in a basic form. Will leave it there and move onto the other screens.

### Your posts

Initially this can be a simple one and just display the list of posts the system knows about from the student. Eventually this should allow the student to manage the allocation for unallocated or unmarked questions.

First, put some approriate data into the database. bimtwo\_marking needs to be filled in. Done.

Need an o/r mapping object to retrieve this data. Initially the class bimtwo\_posts will be much the same as bimtwo\_questions. Copy and paste and a search and replace.

Now I need to add in a model for the page and use the o/r object to get data and display it simply.

Okay, have the data, time to display it. The question is how. In bim the posts were separated into distinct tables based on state (i.e. allocated, marked, etc). For bim2, initial thinking is two tables unallocated posts and allocated posts. Allocated posts include those that have been marked, returned etc. and thus will have to include columns or some other indication of mark, dates, etc.

Actually, looks like a single table might be the way to go. Pity flexible\_table doesn't want to nest.

Need to update the test data to include posts that are

- allocated  
    Show the time allocated, Show the question that it's been allocated to.
- released  
    Show time allocated, marked and released. Also the mark and also the comments.

### Activity details

This page can take on a number of different forms, depending on whether a feed has been registered and whether or not the students are able to register a feed. The first one I'll implement is the situation where the student has registered a feed and it has started to be mirrored.

In this situation, the page should display

- Configuration details about the bim2 activity;  
    This will be used to identify if registration is turned on, display the description of the activity and other config data around the activity.
    
    This data is already available as part of the bimtwo object within the factory, which is passed in.
    
- feed details for the student;  
    i.e. does the student have a registered feed and, if so, where is it, how many posts etc.
    
    This will likely need to be a new class.
    
- user details.  
    i.e. their name, userid etc. Used to display information, but also to get the feed details and other personal information.
    
    This looks like being a new class. Have made sure that factory stores the user id. This will be needed to get the user records.
    

Ending up with a single class that pulls all this information into the one place. However, it does rely on other classes that can be re-used elsewhere. Will document this at the end.

At the moment, I'm having to put in all the language strings and associated help files. I think I am liking the fact that help strings are now included in the help file, rather than in separate files in a separate directory.

Am having a problem getting parameters passed in correctly to help strings. Ahh, have to put curly braces around them. _Interesting_, I gather this from reading the code, not the Moodle documentation or discussion on moodle.org. Would be buggered without the ability to read the Moodle code.

Still having problems with getting the help strings to work properly. Going to have to put in place holders that aren't working and leave this as a major todo. Downloaded latest version of Moodle and the problem continues. So, probably a problem with my code. Will have to look at this later.

### Back to the start

The next step is to implement the activity details/student view from the start of the student interaction. i.e. before the student has registered their blog and in some cases, before the staff have turned registration on. The stages to be implemented are, when the student visits the activity and:

- _DONE_Registration is not turned on and the student has not registered;  
    Show the activity configuration section shown normally, but precede it with message about how the student has not registered and that registration is not on
- _DONE_Registration is turned on and the student has not registered;  
    Same as above, but show the registration form
- Handle the registration of the student's blog, which has two cases
    - Registration worked  
        Show a success message and then show the normal interface.
    - It didn't work  
        Show an appropriate error message, some direction on how to fix it and show the registration form again

Use the three test students as a test case. Start with the registration not turned on.

Now to add the register form. Seems a straight copy across of the form from bim, a few substitutions for module name (bim to bimtwo) and we're just about done. The processing of the form has to be modified to be more object oriented. i.e. a new class.

Perhaps time now to start a new blog post, this has been going on for weeks. The next one will handle the registration process.