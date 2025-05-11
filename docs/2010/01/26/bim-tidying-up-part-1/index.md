---
categories:
- bim
date: 2010-01-26 21:26:14+10:00
next:
  text: Some reasons why business intelligence tools aren't the right fit
  url: /blog2/2010/01/27/some-reasons-why-business-intelligence-tools-arent-the-right-fit/
previous:
  text: BIM - sending results to the gradebook
  url: /blog2/2010/01/26/bim-sending-results-to-the-gradebook/
title: BIM - Tidying up - Part 1
type: post
template: blog-post.html
---
Apart from some playing around with the gradebook, the new development for BIM is complete. What is left to do is the various cleaning up, double checking, documentation and other tasks necessary to turn BIM from essentially functional to something reasonably okay to install. This is the first post describing that process. It and the following ones will essentially be working through the [to do list](/blog2/research/bam-blog-aggregation-management/bim-to-do-list/).

### Created locallib.php

Theory is if you have a number of local functions in lib.php, you should move them to locallib.php - done.

### Fix coordinator mark page

Coordinator should be able to use the same code to generate a page to mark a post as used by the marker. Main difference is that the coordinator has some extra tabs. As it stands, any attempt to make a post displays the "Configure BIM" output. Fix it.

Diagnose the problem:

- URL is /mod/bim/view.php?id=71&screen=MarkPost&markingId=538
- However, because the use has the coordinator capability, this goes to coordinator/view.php:show\_coordinator.
- It appears that there should be a tab parameter in the URL
- Ahh, the tab parameter gets set in an if, based on the value of screen, but MarkPost wasn't included.
- Add that in, all fixed.

### Get auto-discovery working

This essentially means identifying the right PHP library to use to do this for me. Based on discussions in Moodle, it looks like [SimplePie](http://simplepie.org) is the go.

Got an initial script using SimplePie going.

And got the auto discovery think working. Looks like there is more work to do there. Also need to discover whether simplepie is now coming with Moodle or whether I'll need to include it in BIM, at least initially.