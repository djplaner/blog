---
title: "BAM into Moodle - Step #2: configuration and questions"
date: 2009-07-21 11:27:59+10:00
categories: ['bam', 'moodle']
type: post
template: blog-post.html
---
It's Tuesday, so must be time to take the next step in getting BAM into [Moodle](http://moodle.org/). [Last time](/blog2/2009/07/16/installing-moodle-first-step-in-bammoodleam/) I got up to having Moodle checked out from CVS and PHP/Apache and MySQL all working nicely together.

This step will need to focus on:

- Answering the question, "Should I be using Moodle 1.9.X or 2.0.X to do this development?"
- Getting Moodle configured and working.

### Which Moodle version?

Apparently Moodle 2.0 is coming out soon. My institution is running version 1.9.5. I'm told that there are some changes between the two code-bases. Potentially these changes could mean that I will have to waste time once 2.0 comes out. Have to spend some time to put some bones on these impressions.

#### What is Moodle 2.0 coming out?

BAM into Moodle has to be completed and operational for T1, 2010 - i.e. Feb 2010. In order for my current institution to move to Moodle 2.0, I would imagine that it would have to be released before the end of 2009....a question to ask.

The Google planning spreadsheet for Moodle 2.0 is listing another 600 days of work to go. Discussion on the developer forums suggest early 2010 as a guess.

At the moment, given this information, I can't see CQU implementing Moodle 2.0 for Feb 2010.

#### Moodle Roadmap

Let's try the [Moodle Roadmap](http://docs.moodle.org/en/Roadmap) that should probably have something to say on the issue, or perhaps at least a pointer. From my quick skim of the roadmap there doesn't seem to be anything that indicates a radical change in how modules/blocks are intergrated or written. Theoretically, this suggests a module developed in 1.9.x should work reasonably well with 2.0. However, some of the APIs that a module might use are changing. This has implications.

#### Go with 1.9.X

#### 

Based on the above, I'm sticking with 1.9.x. I have, however, asked for some indication from the CQU IT division if they have any insights to share.

### Configuring Moodle

Back to the [Intro to Moodle programming course](http://dev.moodle.org/mod/resource/view.php?id=28) which in turn points to the [Moodle installation page](http://docs.moodle.org/en/Installing_Moodle).

Have to do some playing around with paths etc to get to XAMPP

It would be interesting for someone with no background in UNIX/source control/Web dev to be installing Moodle. The docs aren't always really useful, but sufficient if you have the necessary knowledge.

Actually, that's gone surprisingly easy. All set up. Need to create a course and a few other bits. But it's time to pick up the new laptop.