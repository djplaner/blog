---
title: Adding a bim2 activity - development progress
date: 2010-12-20 17:31:05+10:00
categories: ['bim', 'bim2']
type: post
template: blog-post.html
---
Okay, so after [fixing up the naming problems](/blog2/2010/12/19/problems-with-naming-of-bim2/) with bim2 etc, it's time to actually get the code going.

### To do

A list of things to do once I get back online

- DONE mod\_form.php needs to be modified to use the new editor element for Moodle 2.0  
    Actually, this looks to have been created by a typo or other problem within the bim2 mod\_form.php. It is now working.
- DONE Check the location/process for help files.  
    Seems like in Moodle 2.0, [help files are being converted to strings](http://docs.moodle.org/en/Development:Help_strings) and reside in the language file.
- DONE Update lib.php:add\_instance to call grade\_item\_update
- See what Rolley can do about making the bim icon transparent.

### mod\_form.php

When someone chooses to add a bim2 activity into a Moodle course, the first thing they see is the form provided by mod\_form.php. I'm hoping/wondering if this can essentially stay the same as that used in bim. So let's copy that across. No, empty page.

Ahh, I have to get the database for bim2 up and going. Seems the transition to _bimTwo_ as the internal Moodle name for bim2 doesn't work entirely. The table name regular expression check doesn't like table names with uppercase characters, so for the tables it will have to be _bimtwo_

So, the tables are created now. Does the mod\_form.php work? No still empty. Something not working here, solving this should be interesting as I'm currently without Internet access. How about commenting out the entire bim2 contents from mod\_form.php. Seems the problem is a bit earlier.

~/course/modedit.php is where this is run from, let's have a look there. Let's stick some debugging stuff in and find out where we get up to. Or, alternatively you could try running the mod\_form.php file through PHP from the commmand line and discover where the syntax error is in the file. i.e. \[sourcecode lang="bash"\] david-joness-macbook-pro-2:~ david$ php mod\_form.php

Parse error: syntax error, unexpected ',' in mod\_form.php on line 89 \[/sourcecode\]

This is why, on one-hand, it would be good to be developing in PHP/Moodle more often. I wouldn't be making so many newbie misassumptions and mistakes.

Ahh, nice, I think. Fixed up the syntax error and no get this error in the browser

> Coding error detected, it must be fixed by a programmer: MFORMS: Coding error, text formats are handled only by new editor element.

My immediate assumption here is that this is being caused by the original bim code including some Moodle 1.x specific code around the use of the HTML editor and its inclusion in forms. I'm offline so can't check the syntax for this, will solve for now by commenting out the offending elements.

Next step is to update the get\_string data. This is how Moodle separates text to be displayed on a web page into separate language files. I haven't updated the bim2 english language file to include the labels used in mod\_form.php.

Somewhat related to this are the help files, most of these should be able to come over, at least at the start. Ahh, appears the naming/directory structure may be a little different (or I've made a simple tranlsation mistake)

So, the form is basically working (minus the HTML editor field). Can I submit, well no, that's the next step.

### add\_instance

The _add\_instance_ function in _~/mod/bimTwo/lib.php_ defines what should happen when the mod\_form.php is submitted. Currently, it is empty/boilerplate. Will have to update it. This is again getting into the area of "Moodle 2 conversion problems". As the database API is one place I believe that has undergone some change.

Actually, the NEWMODULE stuff looks like it might already have been updated. But I'm getting the error

> Coding error detected, it must be fixed by a programmer: moodle\_database::insert\_record\_raw() no fields found.

This is happening in this statement \[sourcecode lang="php"\] $DB->insert\_record('bimTwo', $bimTwo); \[/sourcecode\]

$bimTwo has the contents from the form, and it all appears good. So, some problem in the _insert\_record_ function. Ahh, wonder if this is where the database naming problem crops up, the _'bimTwo'_ that is the first parameter, should probably be without the upper case _T_

Yep, that appears to have fixed up the original error, now I'm getting _Incorrect function_. Ahh, wasn't returning the id. Done. Now a problem _Error reading from database_ I think that may well be another table naming problem.

### course/modedit.php

The error is cropping up when this file is being run. Yep, almost certainly the problem with the different names. Am going to have to revert back to bimtwo as the name for everything.

Yep, that's fixed it. It is now possible to add a bim2 activity (not that it will do anything useful) to Moodle 2. As you can see in the following image.

And the edit button basically works as well, in that it shows the mod\_form.php output yet again and allows changes.

Ahh, but the information about the BIM settings is not being saved from the form to the database. Something is missing. Mmmm, most of the bim specific fields are missing from the basic bimtwo table, have to update that in xmldb. The browser form memory remembers the fields, but it appears that I didn't hit the magic 'Save' in xmldb

Yep, that did it.

[![Evidence of bim2 activity in Moodle 2](images/5276170003_581424dee4_m.jpg)](http://www.flickr.com/photos/david_jones/5276170003/ "Evidence of bim2 activity in Moodle 2 by David T Jones, on Flickr")

### To do

Have a lot of clearing up to do when I can get back online.

The next major step, however, is to start implementing the main user interface of bim2. i.e. the process and output that staff and students see when they actually try to use the bim2 activity, rather than simply create it.

It is here where I'm hoping that I will be making the largest changes between bim2 and bim. It's also where I'm hoping the changes will be worthwhile and not introduce new and interesting problems.