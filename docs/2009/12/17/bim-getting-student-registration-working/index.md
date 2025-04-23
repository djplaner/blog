---
title: BIM - getting student registration working
date: 2009-12-17 10:02:31+10:00
categories: ['bim']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

So, getting back into BIM development. [The last post](/blog2/2009/12/14/getting-back-into-bim-summary-and-way-forward/) reminded me where I'm up to. The following is an attempt to plan, implement and document some code. Am starting where I left off, with the registration process for students. As part of this process I am finally starting to use the [to do list](/blog2/research/bam-blog-aggregation-management/bim-to-do-list/) for what it was meant to be used for.

### Properly creating the form

The registration screen is being shown for student users. But it's not with 100% "proper" Moodle code. i.e. it's not [using the forms library](http://docs.moodle.org/en/Development:lib/formslib.php_Usage). The process is meant to be something like this:

- Create a separate PHP class that has the detail for the form.
- Work the code for [normal usage/processing](http://docs.moodle.org/en/Development:lib/formslib.php_Usage#Basic_Usage_in_A_Normal_Page) of the form into the appropriate PHP file.

I believe, for my needs, this translates into:

- Create a PHP file in the module directory that follows the template.

- Use that form in the view.php file.

#### Create the form

Found a slight difference. The template uses a form where it extends the class **moodleform**. The example I am using from the quiz module extends the class **moodleform\_mod**. The \_mod seems to suggest a special class for use in modules?

According to the [xref docs on the forms stuff](http://xref.moodle.org/nav.html?lib/formslib.php.html) the moodleform class is a

> Moodle specific wrapper that separates quickforms syntax from moodle code. You won't directly use this class you should write a class definition which extends this class or a more specific subclass such a moodleform\_mod for each form you want to display and/or process with formslib.

So it looks like some of the older docs are a bit out of date/wrong. But then docs in the same file suggest otherwise.

[A page on moodleform\_mod](http://phpdocs.moodle.org/19/default/moodleform_mod.html)

At this stage, I'm again suffering my standard problem with Moodle. There seems to be no one place or one approach that helps you get an overview of how things fit together. This shouldn't be this hard.

#### Moving forward

It was at this stage that I discovered [a book](http://www.packtpub.com/moodle-1-9-extension-development/book) that promises to give a more coherent overview of the task of creating an activity module. [Initial impressions](/blog2/2009/12/15/bim-and-moodle-a-more-coherent-overview/) are okay. The true test will be in the work I describe below.

Using the moodleform class. I've been able to get the form being displayed. So, the next steps are:

- Get it displaying what is required.  
    The textual part of this is reasonably easy (I currently believe). Just using the `addElement( 'html', $unregistered )` method to add some HTML in a variable. **IMPORTANT:** The HTML should not be hard coded in a variable. Needs to go in the lang files.
    
    All this "extra" work/abstraction in terms of form is necessary because of the nice way Moodle handles forms and auto puts it into the database (generally). This requires that the names of form elements match the field names in the database. Will also need to identify what other information needs to be held within the form in order update the database.
    
    The database table that holds the student registration is called `bim_student_feeds` and has the following fields
    
    - id - set automatically when values inserted NOT NEEDED
    - bim - the id of the particular instance of bim being referred to. Will need to use this when inserting. Already have this in view.php
    - userid - should be able to get this from existing structures, no need to be in the form.
    - numentries and lastpost - both can be null/0 initially.
    - blogurl - from the form
    - feedurl - needs to be calculated from the blog url
- Figure out how to process that information.  
    This seems to be quite straight forward. In the view.php there are a couple of if statements to control what is done if the user presses the save or cancel buttons. Have this control flow going already. Just need to add in a bit of checking and the code to check the student's blog URL and extract the feed URL from the blog and consequently show appropriate error messages and/or insert the data.
- Get the data entered in the form into the database.  
    Quite straight forward using the Moodle database API calls. The biggest question here (and not a real big on) was to double check the "ids" that are being inserted/checked in the database.

### Check IDs

The details about where each students' blog is located, along with some additional information, is stored in the `bim_student_feeds` table. The fields of this table are listed above. There are three "ids" in the table:

1. `id` - the unique id for each entry in table.
2. `bim` - id for the specific bim activity, link back into the `bim` table. At the moment, I believe the assumption is that there can only be one bim activity per course. Will need to check this, probably no reason that there can't be more than one (from a code perspective).
3. `userid` - the id of the user/student for the feed.

To display the register form for students, there is a `bim_feed_exists` function that returns true if there is already a feed for the student. If there isn't, display the register form, else display the details of the students form.

Obviously, the registration form code has to insert the appropriate data into the table. At the moment, there is a bit of a discrepancy about how that is working. Due mainly to the ad hoc way the data has been added. Time to fix that.

What should happen:

- `bim_feed_exists` should be checking to see if there is already a combination of ``bim and `userid` in the table. `id` doesn't matter, as for duplicate feeds, it will be different. Must change that.``
``- `view.php` needs to insert the right data. And here's the problem. Still hard-coded to 0.``

`   ### What's done  At this stage the student registration process is working. If by working the definition is that the student without any registered blog URL will see the registration form. They can enter their URL and it will be inserted into the database. There is a list of tasks outstanding here:  - Blog URL needs to be validated as correct. - Feed URL needs to be extracted from the blog url. - Some logging of registration needs to be added. - Appropriate error checking and reporting needs to happen with the process. - .. many more..  ### Where to now  Again I come up to the question of depth (complete all the necessary detail for registration to work properly) versus breadth (get all of the screens done so I can show folk).  At this stage, I'm leaning towards the breadth approach. I need to show the users of BIM what things are going to look like, even with the chance of seeing it in action. I face this question previously and chose depth, however, now that I've got database/form processing working I'm thinking the breadth approach might work better.  So, the plan is:  - Design, create and populate the rest of the database tables for bim.       This will allow some of the "show details" screens to have real data to draw upon. The data will be modified/anonymised versions of real data from BAM. - Work through the remaining screens so that they appear to be working but without many of the additional/real working they will need in the end. - Release these iteratively to the folk thinking of using BIM next year.   `