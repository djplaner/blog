---
title: "BIM #3: Getting the module work, making some progress?"
date: 2009-08-13 11:31:16+10:00
categories: ['bam']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: 'BIM #4: Re-jigging how BIM works &laquo; The Weblog of (a) David Jones'
      author_email: null
      author_ip: 72.233.96.151
      author_url: https://djon.es/blog/2009/08/17/bim-4-re-jigging-how-bim-works/
      content: '[...] #4: Re-jigging how BIM&nbsp;works  The last post in this series
        saw me struggling &#8211; the long way around &#8211; to the realisation that
        the implementation [...]'
      date: '2009-08-17 09:07:51'
      date_gmt: '2009-08-16 23:07:51'
      id: '2711'
      parent: '0'
      type: pingback
      user_id: '0'
    
---

See also: [[blog-home | Home]]

The story of trying to get BAM into Moodle (BIM) continues, today's saga continues on from the [last post](/blog2/2009/08/11/bim2-starting-the-module/) which had progress stalled. The NEWMODULE template module was put in place, I had thought most of the necessary steps were being taken, however, the module name is not showing up as expected.

First, I'll try and solve that problem, then make some moves on starting to put in some initial functionality into the BIM module to get it working as a prototype.

### Getting NEWMODULE BIM working

Summary of steps taken to move forward:

- Perhaps I didn't change all the NEWMODULE labels into BIM.  
    Nope, that wasn't it. Only a couple minor left overs in some HTML. Changing those, still no movement.
- Before the next step, perhaps we'll do a restart of Apache, the last resort of the clueless - the big red button.  
    That was too much to hope for.
- New thought, have I changed all the filenames?  
    Nope, the language file was still newmodule. Okay, that hasn't solved the problem, but the wrong filename could have screwed up installation?
- Uninstall and try again?  
    There's a delete option in the "Manage activities" page, let's try that. Okay, it looks like it only deletes the database stuff, doesn't touch the files. Though it does give advice to remove those. Let's try to reinstall.
- Reinstall.  
    Ok, reinstallation of dbase tables works fine. But still not added to the list. Perhaps time to look at the Moodle forums and see what common mistake I've made.
- First, let's identify the write Moodle language to use.  
    "Site adminstration block" is the name for the "block" in the left hand menu where the bim name is not appearing.
Wrong NEWMODULE?  
By [this issue](http://tracker.moodle.org/browse/CONTRIB-1075) in the Moodle tracker it appears that I might have the wrong NEWMODULE. Yep, looks like the version in the contrib code is for version 2.0. The issue includes a link to a version for 1.9, which is what I'm currently working with. Oh dear, time to start again.

### Reflection on the experience so far

It's been a few weeks now trying to get my head into Moodle. Some reflections on the experience so far:

- The context in which I'm trying to do this is far from ideal, so that may influence some of the experience.
- Trying to get an overview of Moodle, how it works, its structure, its terminology etc. has been really hard. I'm yet to find a clear, concise overview of this in any of the documentation. The different versions, while understandable, adds to the problems. The half-finished nature of some of the beginners documentation also doesn't help (yes, I know the point of an open source community is that if you have an itch, you scratch - but I don't have the time nor energy at the moment, perhaps later). This is perhaps, the biggest problem I've faced so far.
- The developers' community on the forums seems to be quite active and very good. Perhaps the biggest plus that Moodle has. But there's also a limit to how much you want to rely on folk.
- Some of the ideas in the Moodle design are quite good, perhaps limited somewhat by the implementation language, but it's also an advantage - there's no single right answer there. However, while only a little way into understanding, there does appear to be some "ad hoc'ness" to some aspects of the design. But then you get that in any long-term software product.

But then perhaps I'm just being overly critical because I'm making newbie mistakes.

### Starting over with the 1.9 NEWMODULE

Here we go again:

- Save the old version, just in-case.
- Delete it from the Moodle instance.
- Copy the new NEWMODULE across and start following the instructions in README.  
    These are instructions are a bit different and possibly better.
- One of the differences is that this one suggests you use XMLDB (the apparently hated web-based XML/dbase editor in Moodle).  
    Yep, the bim db stuff shows up. What the hell, let's bring the old BAM tables across now.
- Maybe, just add the BAM\_CONFIGURE table  
    That works well. If you put in a duplicate of a table that already exists, it errors and then loses your data! Similar happens in other places. I'm beginning to see why people hate this thing. I'll leave it at just this one table.
- Saving the changes?  
    There's a cryptic (for a newbie like me) directive in the README to make sure you use the SAVE link on the XMLDB main page. It's cryptic because I can't see a SAVE link on the page I'm on and can't really see an obvious indication of where the "XMLDB main page" might be in relation to where I am.
    
    Ahh, there's a "back" link at the end of a list of other, very different links. But no "save" on that page, but wait, there's a "Back to main" link in much the same place, again at the end of long list of unrelated links.
    
    Okay, this must be the main XMLDB page, but there's no save link operational. Does this mean that the save has already been done? The install.xml still seems to have the same timestamp.
    
    Ok, there's a point about the link not being active because the apache user doesn't have permission. Yep that's the problem.
    
    Would've thought there would be an error message if the file couldn't be written to!
    
- Okay, next step is notifications. Yep that worked.
- Does it appear in the site adminstration block?  
    Bugger (and other more serious words), no it doesn't. We're back at the same place. It's in the list of activities shown when viewing the long list, but it doesn't appear in the site administration block.
- Is this a permission problem?  
    Nope all looks the same.
- Check the courses. Ahh, can add bim now as an activity. Okay. This must mean that you only get in the Site Administration block based on something else that I haven't done yet.

That was a bit of time wasted, wasn't it?

I'm guessing the killer was the permissions and perhaps the different version of NEWMODULE for 1.9 and my lack of understanding about the site administration block.

### Putting in some initial BIM code

If I try to add a new bim activity, it simply uses some default forms from the NEWMODULE template. I'll want to be changing this at a latter date. However, first, I think I'll look at how I'll be providing two different activities within BIM:

1. Staff BIM.  
    This allows staff to track, mark and manage BIM. The coordinator (what's the Moodle equiv) will have something slightly different.
2. Student BIM.  
    Where they can register and track progress with marking on BIM.

The Assignments activity is the only one that appears to have multiple different activities to add, so I guess I'm off to look at that code.

First, the NEWMODULE readme.txt suggests looking through the lib.php, index.php and view.php files. The following summarises what I find about each of the three files, including some insight from [here](http://docs.moodle.org/en/Development:Modules):

- index.php - a page to list all instances in a course  
    This one should be fairly simple/straight forward extension of what's already here.
- view.php - a page to view a particular instance  
    More complex in terms of what BIM will do, but fairly straight forward (I hope)
- lib.php - any/all functions defined by the module should be in here  
    Standard set of functions called by Moodle to perform things (e.g. create an instance of the activity). This is a bit of where getting into the Moodle mindset will be interesting.

#### Multiple activities - learning from assignment

view.php for assignment appears to implement a simple equivalent of the "factory" pattern. Given an assignment id, determine the type and then call a library that is specific that assignment type.

The "types" are implemented in a type directory, where each sub-directory matches an assignment type (offline, online, upload, uploadsingle) within each of those directories is an assignment.class.php file that extends a base class defined in lib.php. This is where the assignment type specific stuff is implemented.

How does the module get the multiple entries in the "Add an activity" menu? "Advanced uploading" and "Assignments" are some of the phrases it produces. Where are they used? Well, that's a bit of a problem. I'm not finding everything I think I need.

Ahh, perhaps assignment, as one of the core ones, is using config/libraries from elsewhere - outside the module. Yes, the language file that defines strings is outside in the main lang directory.

modulenameplural typeoffline typeonline typeupload typeuploadsingle are strings used for assignment related to the "add an activity" menu. Where did those get used in the code?

- lib.php::assignment\_get\_types  
    Seems to be it. Uses a thing called MOD\_CLASS\_ACTIVITY and returns an array of those. Yep, that's the one. Added a "HELLO" and it shows up.

### Time for lunch

So, I've identified where the function in the assignments module lib.php that creates the array of "objects" necessary to update the "Add an activity" drop menu. I need to figure out how this function is called by Moodle.

Bugger, it's in the ~/moodle/tags file. A "system" level type thing.....bugger.

Might have to think about a single activity. Not worth the hassle.