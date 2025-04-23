---
title: Major (Moodle) requirements for BIM 2.0
date: 2012-12-29 10:41:35+10:00
categories: ['bim']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Major (Moodle) requirements for BIM 2.0 &laquo; The Weblog of (a) David
        ... | elearning stuff | Scoop.it
      author_email: null
      author_ip: 89.30.105.121
      author_url: http://www.scoop.it/t/elearning-stuff/p/3892997068/major-moodle-requirements-for-bim-2-0-the-weblog-of-a-david
      content: '[...] The next step in the development of BIM 2.0 is identifying the list
        of major (Moodle) requirements that need to be implemented. BIM is a Moodle activity
        module. Moodle has a range of expectations that such modules are meant ...&nbsp;
        [...]'
      date: '2012-12-30 03:56:03'
      date_gmt: '2012-12-29 17:56:03'
      id: '545'
      parent: '0'
      type: pingback
      user_id: '0'
    
---

See also: [[blog-home | Home]]

The next step in the development of [BIM 2.0](/blog2/research/bam-blog-aggregation-management/) is identifying the list of major (Moodle) requirements that need to be implemented. BIM is a Moodle [activity module](http://docs.moodle.org/dev/Activity_modules). Moodle has a range of expectations that such modules are meant to meet. The following is an attempt to identify what needs to be done.

It has resulted in a renewed effort to use the github [issue list](https://github.com/djplaner/BIM/issues) to record and manage what needs to be done. Not only have I started adding issues for BIM 2.0, I've also been through the old issues and decided which apply to BIM 2.0

In short, some major work to be done to get backup/restore migrated. Some minor tweaks (it appears) to get gradebook integration working. Logging is working as is.

## Summary of the requirements

A summary of what was found follows. It includes some compulsory/important type requirements:

- [Back up](http://docs.moodle.org/dev/Backup_2.0_for_developers) and [restore](http://docs.moodle.org/dev/Restore_2.0_for_developers).
- [Gradebook API](http://docs.moodle.org/dev/Gradebook_API).
- New icons for [Moodle 2.4](http://docs.moodle.org/dev/Moodle_icons_2.4)  
    
- Logging.  
    Need to check that the [logging API](http://docs.moodle.org/dev/Logging_API) hasn't changed dramatically and think about what additional/different logging needs to be added.

And also some that would be nice future additions:

- New icons for [Moodle 2.4](http://docs.moodle.org/dev/Moodle_icons_2.4)  
    
  
This appears to require some changes to the question data. i.e. the due date is associated with each questions rather than perhaps the BIM activity.- Use of the [message API](http://docs.moodle.org/dev/Message_API)
- [Activity completion](http://docs.moodle.org/dev/Activity_completion_API).
- [Conditional availability](http://docs.moodle.org/dev/Conditional_activities_API)
- The [RSS API](http://docs.moodle.org/dev/RSS_API) is used to generate "secure" RSS feeds by modules. Theoretically this could be useful for merging various feeds. I wonder what "secure" means? Obscurity?
- [Unit test API](http://docs.moodle.org/dev/Unit_test_API)
- [Advanced grading](http://docs.moodle.org/dev/Advanced_grading_API) which is meant to support rubrics. It's still a bit early for this to be finalised.
- [Plagiarism checking](http://docs.moodle.org/dev/Plagiarism_API) including how to add it to [an activity module](http://docs.moodle.org/dev/How_to_add_support_for_a_Plagiarism_Plugin_to_my_activity_module)
- Even a chance that the questions should be managed via the [question API](http://docs.moodle.org/dev/Question_API)
- Should also revisit the [Moodle coding style](http://docs.moodle.org/dev/Coding_style) to ensure BIM isn't a great departure. There are now some tools to check code available.
- Not to mention the [guidelines for CONTRIB code](http://docs.moodle.org/dev/Guidelines_for_contributed_code).

## What has changed?

Now to find out what has changed in the requirements that have to be addressed now.

### Backup and restore

This has definitely been changed. It's listed in the [migrating CONTRIB code document](http://docs.moodle.org/dev/Migrating_contrib_code_to_2.0).

backuplib.php is now replaced with a backup directory. It also appears to be a more OO-based approach. Some major re-work to be done here. Will leave this to another post.

### Gradebook

This isn't working. Any attempt to turn on the BIM gradebook integration generates an error on line 313 of lib.php due to a problem with a database insert

> Debug info: Column 'grademax' cannot be null INSERT INTO mdl\_grade\_items

The question will be whether this is a problem in BIM or evidence that the Gradebook API has changed significantly.

According to the [Gradebook API](http://docs.moodle.org/dev/Gradebook_API) there should be a mod/bim/grade.php file. Certainly not one in BIM 1.0. But then the forum module doesn't have one either and yet it does use the gradebook, so it would appear to be optional.

grademax can be changed in the gradebook, but the help text located there suggests it should be set on the activity settings page. i.e. I need to add the ability to set grademax on the BIM config screen.

This has identified that the problem is because the existing BIM code is does not have a value for the grademax field for the gradebook. It appears that the Moodle 2.x code has required that this be not null.

Actually, the BIM 1.0 code doesn't seem to have this set. A mystery change? Perhaps some boilerplate with a search and replace I put in place when setting up BIM 2.0? Moodle 1.9 doesn't seem to have required a grademax value. So what does grademax imply?

Common sense would seem to imply the maximum value that can be entered into the gradebook for this component. BIM currently asks for maximums for each question, so a grademax could be calculated. The problem is that BIM only uses the maximums to generate a warning, it doesn't enforce it. If the gradebook enforces grademax, then this could create some dissonance with BIM's operation.

As it happens the hard coding of grademax to 10 results in gradebook integration. Or at least the activity being added to the gradebook. When I try to release some results (which includes adding marks to gradebook) I get a coding error which I'll need to fix. Have added this to the to do list.

Will leave working on this until later.

It also suggests that in lib.php the bim\_supports function should report that it has FEATURE\_GRADE\_HAS\_GRADE. I'll add that for now.

There are also a few examples that provide some extra code missing from BIM. Will add that as well.

### Logging

The logging API in Moodle is likely to be replaced in a [little while](http://docs.moodle.org/dev/Logging_2) as part of an increasing importance of logging, analytics etc. The new work includes some references which could be used to inform a rethinking about BIM logging. This is one of my areas of interest.

But at the moment, the current BIM logging is working. At least there are BIM entries being added into the dummy course that I've been testing with.