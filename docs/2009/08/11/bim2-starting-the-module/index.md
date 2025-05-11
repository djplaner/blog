---
categories:
- bam
date: 2009-08-11 15:20:00+10:00
next:
  text: '"BIM #3: Getting the module work, making some progress?"'
  url: /blog2/2009/08/13/bim-3-getting-the-module-work-making-some-progress/
previous:
  text: 'BIM #1: Working on the prototype'
  url: /blog2/2009/08/11/bim-1-working-on-the-prototype/
title: '"BIM#2 - Starting the module"'
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: 'BIM #3: Getting the module work, making some progress? &laquo; The Weblog
        of (a) David Jones'
      author_email: null
      author_ip: 74.200.246.66
      author_url: https://djon.es/blog/2009/08/13/bim-3-getting-the-module-work-making-some-progress/
      content: '[...] The Weblog of (a) David Jones Another voice in the blogosphere    &laquo;
        BIM#2 &#8211; Starting the&nbsp;module [...]'
      date: '2009-08-13 11:31:25'
      date_gmt: '2009-08-13 01:31:25'
      id: '2710'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
As outlined in the [last BIM post](/blog2/2009/08/11/bim-1-working-on-the-prototype/) the aim here is to take the "template" NEWMODULE and start creating a BIM module. Initially, this will contain hard-coded HTML or perhaps some initial non-functioning forms, we might progress onto some canned examples and finally to the real thing.

### The NEWMODULE template

The aim here is copy this code into a "bim" module directory and update it a bit to get it working, but not doing anything useful.

The NEWMODULE module is part of the contrib code for Moodle and is essentially a template for all the stuff a new module should cover. There are some issues, it appears, about whether or not it has kept up to date with version of Moodle. I guess there's only one way to find out.

Here's what I did:

- Create a directory ~/moodle/mod/bim  
    This is where I think the bim code will live.
- Copy the contents of NEWMODULE over into bim.
- Go into Moodle and see if that's changed anything.  
    Apparently, modules/blocks when first installed can take additional installation steps via the web interface.
- Nothing there, but that is expected as the instructions for NEWMODULE suggest that I have edit the files to replace NEWMODULE with bim.
- Go to Notifications as the admin via the web interface and yes, the databases for the module get created.
- At this stage, bim should be showing up in the list of installed activities --- but no, it's not!
- At least not in the administration section, there is a new \[\[modulename\]\] in the "Add an activity" in a course site. Looks like this might have been missed.
- Ahh, it's not in the main list that appears in the navigation menu, however, if I head into "Manage Activities" it is there. So it would appear it can be added, for some reason. Maybe I need to write a bit of code.
- Ahh, looking at the code I find that if the version variable is set to 0, then it will not be installed. That needs to be set to the typical timestamp format that Moodle uses.
- Having set that, it appears there's a need to re-visit notifications to get it installed. Some warnings as the dbase already installed. In fact, it reports upgrading failed. Looks like we're in an endless loop now. The problems are due to "bim" rows inserted into the log. So, I've deleted those entries and dropped the bim table.
- At this stage, there's a complaint about bim needing upgrading and the table mdl\_bim not existing. Seems to imply there's another entry for bim in another table, probably need to delete that.
    
    ```
    delete from mdl_modules where name='bim';
    
    ```
    
- So that is working, but still bim only appears in the "Manage activities" not in the list of activities. Something else missing? There are other activities that aren't showing up as well

Gotta love a positive place to stop.