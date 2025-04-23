---
title: Making BIM ready for Moodle 2.6
date: 2014-05-19 13:39:10+10:00
categories: ['bim']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

The very nice folk from my institution's ICT group warned me back in March that

> I have started work on the moodle 2.6 upgrade that will be happening midyear and have come across some deprecation warning from BIM. Just giving you plenty of notice that an updated version will be needed before release.

That was just as my first use of [BIM](/blog2/research/bam-blog-aggregation-management/) on the institution's servers was getting underway. That's gone reasonably well and it will be continuing (and hopefully expanding as I learn more about what's required and possible with the approach) next semester, so I better get BIM playing nicely with 2.6. That's what this post is reporting on.

BIM for Moodle 2.6 (and also 2.5) is available from [the BIM plugin database entry](https://moodle.org/plugins/pluginversions.php?plugin=mod_bim) and also [from GitHub](https://github.com/djplaner/moodle-mod_bim).

### Get Moodle 2.6 running

Let's get the latest version of Moodle 2.6 - 2.6.3 - and install that.

So that's [the first change](http://docs.moodle.org/26/en/admin/environment/php_setting/opcache.enable). PHP setting for caching. Not that I'll need that for testing. Looks like I can ignore it for now.

### Get BIM installed

I'm doing this so irregularly now it's good that I actually documented this [last time](/blog2/2014/02/07/bim-testing-and-fixes/).

That all appears to be working. Ahh, but I haven't turned the debugging all the way up to annoying yet.

That's better

> get\_context\_instance() is deprecated, please use context\_xxxx::instance() instead.

And about this stage it was always going to be time to....

### Check the Moodle 2.6 release notes

The [Moodle 2.6 release notes](http://docs.moodle.org/dev/Moodle_2.6_release_notes) and then the developer notes. Nothing particularly related to this warning.

### Do it manually

As outlined in [this message](https://github.com/marxjohnson/moodle-block_quickfindlist/issues/10) it appears that this particular usage has been deprecated for a few versions. The deprecatedlib.php suggests this gets removed in 2.8.

So the changes I'm doing appear like this \[code language="javascript"\] #$context = get\_context\_instance( CONTEXT\_COURSE, $course->id ); $context = context\_course::instance( $course->id ); \[/code\]

I can see this is needed in the following

- ./coordinator/allocate\_markers.php
- ./coordinator/find\_student.php
- ./index.php \*\*done?\*\*
- ./lib/groups.php
- ./lib/locallib.php
- ./marker/view.php
- ./view.php - this one had actually been done earlier #$context = get\_context\_instance( CONTEXT\_MODULE, $cm->id ); $context = context\_module::instance( $cm->id );

That all seems to be working.

### Do a big test

Will back up a large BIM activity with a temp course from my Moodle 2.5 instance and restore it under Moodle 2.6.

### Some more issues

print\_container() is deprecated. Please use $OUTPUT->container() instead. Done