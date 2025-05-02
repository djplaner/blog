---
title: BIM for Moodle 2.5
date: 2013-11-06 14:50:19+10:00
categories: ['bim', 'bim2']
type: post
template: blog-post.html
---
Earlier this week @sthcrft asked https://twitter.com/sthcrft/status/397143586178756608

Talk about good timing. My shiny new Mac laptop arrived the same day and I'd been waiting on its arrival to explore whether or [not BIM](http://bit.ly/bambim) was Moodle "2.5ish happy". It turns out that there are a few tweaks required and some improvements made possible. The following is records those tweaks.

## Current status

BIM seems to be working on Moodle 2.5.

I have made a minor change so that there is now a [branch of BIM specific](https://github.com/djplaner/moodle-mod_bim/tree/MOODLE_25_STABLE) to Moodle 2.5. Will probably become the master branch in coming days.

Tested the changes with my current course's use of BIM - about 100 students - but have yet to add this to the Moodle plugin database.

## Crashing on tabs

It was looking quite good for BIM on Moodle 2.5. Installed without a problem and appeared to be basically working. Some of the interface tweaks helped the unmodified BIM look a bit nicer.

But then I tried to "Find a student". At which stage it appears to crash/stall/hang. Sit's there never completing (or at least not for a very long time).

A bit of exploration of what's happening suggests that the problem is with `print_tab` which appears to be deprecated from Moodle 2.5 onwards. A quick translate to the new alternative still left the same problem. The tabs work for all of the pages, but not on the submission of "Find Student".

And back to this on the next day.

After a lot of wasted time - you idiot - I haven't setup the http proxy on my server and that's causing the delay. And again, you idiot.

### Other tests

Tests as other users all seemed to work fine.

### Layout issues

Some of the more "busy" pages for the coordinator (some overlap with the marker) don't display very well. Never have really, but the current default theme emphasises those problems. Let's change to another theme and see.

- The text editor for comments on MarkPost overlaps a bit

These are minor issues and after a quick look, can't see any quick way to solve it beyond a broader re-working of the interface.

## Nested tabs

The move to tab tree apparently gives scope for nested tabs, that could solve one of the (many) uglies in BIM. i.e. the coordinators ability under "Your students" to view details and mark posts. Implementing these as nested tabs could be useful. An exploration.

That seems to work surprisingly easily. Now to remove the old kludge.