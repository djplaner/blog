---
title: First coding steps for bim2
date: 2010-12-19 12:17:29+10:00
categories: ['bim', 'bim2']
type: post
template: blog-post.html
---
The following records some of the initial steps in actually coding bim2. It includes

- A new name?;
- The new github repo for bim2;
- Resources for Moodle 2 module development; and
- Initial coding steps for bim2.

### A new name?

bim2 is going to be very different from version 1 of bim. Beyond working for a different version of Moodle, I'm hoping bim2 will be a significant improvement in terms of code design and provide a foundation for some interesting stuff. Consequently, I want to keep the distinction between the two systems clear.

Hence, as you can probably guess, I'm using the title **bim2** for version 2.0. This matches the name of the github repo and subsequently the directory on the Moodle server. Am hoping the consistency will work well.....time will tel.

### New github repo for bim2

The code for bim2 will be/is available from a [new github repository](https://github.com/djplaner/bim2). There's only the [README](https://github.com/djplaner/bim2/blob/master/README) there at the moment, however, as I progress I will be updating the repo.

I'm using github, because the experience with bim was just so simple and effective.

### Resources for Moodle 2 development

The first step is finding out just how different Moodle 2 module development is from Moodle 1.9. My vague understanding is that it isn't that different, however, I am planning to start from scratch with bim2, rather than port BIM into Moodle 2. The main reason for this is that I want to experiment with a better design for the structure of bim2.

What I'm really after is enough information to get a test/dummy Moodle 2 module up and going ASAP. The skeleton/foundation for bim2.

[Category:Moodle 2.0](http://docs.moodle.org/en/Category:Moodle_2.0) seems to be the place for an overview of available documentation.

As with my initial Moodle experience, I am finding it hard to get my head around the apparently disjointed collection of resources and insights on the moodle.org site. It appears that the [NEWMODULE.zip](http://docs.moodle.org/en/Development:NEWMODULE_Documentation) approach might work with Moodle 2.0. So, I'll move onto that.

### Initial coding steps for bim2

So, this has essentially become the process for following the NEWMODULE.zip readme and getting a dummy bim2 up and going.

1. Get all the files NEWMODULE.zip files into the bim2 directory.
2. Change _newmodule_ to _bim2_ in all the files.
3. Rename the lang/en\_utf8/newmodule.php file to bim2.php.
4. Log into Moodle as admin.
5. Remember about modifying version.php to have a version number that represents the current date.  
    Not sure I need this, at the moment, but I got bitten by this mistake with BIM.
6. Success "bim2" installed.
7. Let's add a course and see if I can add an activity?  
    Mmm, not liking the manual enrol for users in a course. No obvious save/submit/ok button when finished enrolling. I have to hit the close window widget, which (for me at least) suggests losing changes.
8. Yep, it's there, but error about database table modules. This matches the instructions in NEWMODULE.zip. Need to modify the module's tables. Ahhh, death by XMLDB....
9. The current plan is to re-use the existing BIM database tables. Let's see if I can brave XMLDB to do that. All done. Success.

That will do for now. Next step will be to start actively modifying the NEWMODULE stuff into bim2 specific code.