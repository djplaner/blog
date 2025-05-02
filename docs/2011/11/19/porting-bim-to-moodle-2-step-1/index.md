---
title: Porting BIM to Moodle 2 - Step 1
date: 2011-11-19 16:43:31+10:00
categories: ['bim2']
type: post
template: blog-post.html
---
The wife's out for some culture so I find myself late on a Saturday night taking the initial steps in the second attempt to port BIM to Moodle 2. Started reading Mike Churchward's blog series on [porting modules to Moodle 2](http://tandl.churchward.ca/2011/10/converting-m19-plug-ins-to-m2.html).

Time moves on, and almost a week later I'm putting the finishing touches on this post/development journal entry. It gives a brief summary (mostly for my records) of what I've done to get a version of [BIM](/blog2/research/bam-blog-aggregation-management/) that is being recognised by Moodle 2.1. Not sure how well it is working, but Moodle 2.1 is creating tables and recognising the plugin as being available for use in courses.

The next step will involve experimenting with just how well BIM is working with Moodle 2.1 and fixing what needs to be done. This will involve finishing some of the following.

### Upgrading Moodle

Of course, it's a good 6/7 months since I touched Moodle. So I should probably start by upgrading to the latest version of Moodle, which seems to be 2.1.2.

It is going to take sometime to get back into this.

Oh look at that, Moodle 2.1 requires the next version of PHP. Thankfully some kind soul has produced a [dmg file](http://download.moodle.org/macosx/) with Xampp and Moodle 2.1 for Mac OSX. Let's install that.

That was relatively painless. Moodle 2.1 up and going.

### The plan for git

The source code for BIM is [hosted on BIM](https://github.com/djplaner/BIM/). The previous attempt at BIM2 is also hosted there, need to figure out what to do with this new version.....yes folks, I'm that out of it as a developer.

Ohh, there's a GUI client for Mac OSX now. Looks okay.

[This seems](http://nvie.com/posts/a-successful-git-branching-model/) to be the approach. More on this tomorrow.

The plan is

- Tag the existing bim code as 1.0 (and v1.0 just for good measure - i.e. re-learning git).
- Create a bim2 branch and then a develop branch from there.  
    git checkout -b bim2
- Convert the Moodle 2 branch into a Moodle 2 module.  
    This will be the step-by-step process I start from now, with a vague set of steps something like
    - Do minimum to get Moodle 2 to recognise bim.
    - Comment out everything that creates errors.
    - Gradually bring bits back and convert them to Moodle 2 "format".Be interesting to see how long that plan lasts.

### Get Moodle 2.1 to recognise the bim module

With the code in place (~/mod), when I login as admin to the local Moodle installation, there is the notice that bim is ready to install. Now's when we find out what is missing. There's the error

> Plugin "mod\_bim" is defective or outdated, can not continue, sorry.

The error causing this is

> Missing mandatory en language pack.

If I go looking for the code, it's looking for the file $fullmod/lang/en/$mod.php. More information [here](http://docs.moodle.org/dev/User:Frank_Ralf/Experience_of_converting_a_module_to_Moodle_2#Language_folder_changed) and [this checklist](http://docs.moodle.org/dev/Migrating_to_2.0_checklist)

I'd gotten a fair bit of the way through this conversion process when errors were causing me concern. After a few more side tracks I discovered the following.

Oh dear, simply syntax errors. Need to check those. Using this little bit of shell \[code lang="sh"\] for name in \*.php do php -d display\_errors=1 -l $name done \[/code\]

Fixed up all of those and now have a bit of success, good news this late on a Saturday afternoon, bim is being recognised by Moodle 2.1

#### Language strings

From the [the checklist](http://docs.moodle.org/dev/Migrating_to_2.0_checklist)

- **DONE** rename language folder (en\_utf8 to en)
- **DONE** Change $a to {$a}
- Change popup help files [to \_help lang strings](http://docs.moodle.org/dev/Help_strings) and shorten.  
    Need to run up Moodle 1.9 so I can double check where the help strings are going etc.
    
    Some of these are quite long, I can see some Moodle docs in my future, including:
    
    - Manage marking help "manageMarking.html"
    - yourStudents.html
    - opml.html
    - unregisteredDetails.html
    - registeredDetails.html
    - changingosts.html
    - mods.html
- **DONE** Add $string\[‘pluginname’\] to lang file
- **DONE** Add $string\[‘pluginadministration’\] to lang file

So, does that change the Moodle 2.1 complaints about BIM?

Yes it does. A big green tick and success. You know it's not going to be that easy. Ahh, internal server error. Have to remove the bim code entirely to get Moodle to start up again. Will remove it via Moodle, stick the code back in to see if the problem was due to a time out issue.

Time to go through the rest of the checklist.

#### Database

Also drawing on the [DB layer 2.0 migration docs](http://docs.moodle.org/dev/DB_layer_2.0_migration_docs)

- **DONE**Leave empty db/update.php file
- **DONE**New $DB global objects with functions replace old db functions  
    There is a [PHP script](http://cvs.moodle.org/contrib/tools/check_db_syntax/) that checks for functions.
- $DB parameters swapped to ?
- **DONE**Add and strip slashes no longer required
- **DONE**Remove use of ENUM and ENUMVALUES in install.xml file
- **DONE**Remove STATEMENTS section in install.xml file, use db/install.php or db/log.php instead.
- **DONE** not used..check use of sql\_substr()
- Get\_records() etc now always returning arrays, empty array in case of no records found.
- Db functions throw errors not return false on error
- DB functions offer strictness parameters e.g MUST\_EXIST
- **DONE** Update version.php numbers (esp required)
- **DONE**In version.php add $module->requires = 2010080300; // Requires this Moodle version

More insights from [page on upgrading plugin tables](http://docs.moodle.org/dev/Installing_and_upgrading_plugin_database_tables)

#### Page display

- New $OUTPUT header and footer functions  
    Done the basics at the top level. Need to do more work on this.
- Navigation links need to use $PAGE->navbar
- Make sure that you instantiate the moodle form before any call to $OUTPUT->header()
- Create a renderer
- **DONE** (not used) Change the way image urls are displayed (not $CFG->pixpath any more)
- CSS changes
    - **DONE** (not used) Change styles.php to styles.css
    - Change page id to new structure e.g. course-format-studyplan to page-course-view-studyplan

#### Forms

- Param\_clean parameter type removed
- type required parameter for optional\_and required\_param
- Replace file form elements with new filepicker
- Replace htmleditor with editor form field type
- Change setHelpButton to addHelpButton. (You need to change the arguments, but the new ones are simpler.)

#### Roles and permissions

- **DONE** array name to $capabilities in access.php
- **DONE** Remove references to admin in access.php
- **DONE** Rename legacy to archetypes in access.php
- **DONE** Add manager archetype in access.php
- Ensure require\_login as well as require\_capability checks
- **DONE** (not used) isguest() is depreicated, use !isloggedin() || isguestuser() instead

#### Progress

Somewhere in all of that, things got a bit much. Need to do this differently, for now.

Empty slate and slowly copy stuff in, starting with index.php. index.php requires a valid course id with a bim activity to work directly. But bim is showing up in Moodle 2.1 okay.