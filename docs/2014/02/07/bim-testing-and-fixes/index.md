---
categories:
- bim2
date: 2014-02-07 13:53:40+10:00
next:
  text: Needed updates to cc_attrib.pl
  url: /blog2/2014/02/15/needed-updates-to-cc_attrib-pl/
previous:
  text: Identifying some immediate changes to BIM
  url: /blog2/2014/02/05/identifying-some-immediate-changes-to-bim/
title: BIM testing and fixes
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Making BIM ready for Moodle 2.6 | The Weblog of (a) David Jones
      author_email: null
      author_ip: 66.155.9.47
      author_url: https://djon.es/blog/2014/05/19/making-bim-ready-for-moodle-2-6/
      content: '[&#8230;] I&#8217;m doing this so irregularly now it&#8217;s good that
        I actually documented this last time. [&#8230;]'
      date: '2014-05-19 13:39:20'
      date_gmt: '2014-05-19 03:39:20'
      id: '949'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
A journal of fixes and testing of BIM. Aim here is to address some minor issues with integration with my current institution's Moodle instance thereby providing a minimum working version for installation. As per [yesterday's planning](/blog2/2014/02/05/identifying-some-immediate-changes-to-bim/) the hope is to make further changes based on this foundation.

Result is a slightly tweaked version released [via Moodle contrib](https://moodle.org/plugins/pluginversions.php?plugin=mod_bim). This will be the foundation for some tweaks, though I can feel time slipping away.

## Latest version of BIM and PostgreSQL

The institutional Moodle instance uses Postgresql. Thanks to playing with MAV I know have a version of Moodle running with Postgresql (aka fred). The plan here is to install BIM on that instance and test it

1. What's the latest BIM?
    
    MOODLE\_25\_STABLE is the latest, but MOODLE\_24\_STABLE is what I need for this work, institutional Moodle version still at 2.4.
    
2. Install it on fred.
    
    Get the source
    
    \[code lang="sh"\] git clone https://github.com/djplaner/moodle-mod\_bim/ mv moodle\*bim bim cd bim git branch MOODLE\_24\_STABLE git pull origin MOODLE\_24\_STABLE \[/code\]
    
    Visit notifications as the admin user on fred and install of BIM successful.
    
    BIM not appearing in the list available in a course. A setting? No, there is an error? What error? Change ownership on the directory and all good.
    
3. Do some basic tests with that version of BIM.
    - Create BIM activity in old EDC3100 course. - DONE
    - Do some work as administrator.
        - Register a blog - DONE
        - Create a question - DONE
    - Create some teaching staff - fred already has some details for users. - DONE
        
        Need to address the absence of the auth plugin - my laptop doesn't have the institutional auth plugin, can I work around this?
        
        Need to create some new users.
        
        - examiner - david
        - marker - vick, rick
        - students - nerf, abe
4. Do a BIM restore from the S2, 2013 version of BIM - this will be complex given usernames? - DONE
    
    This worked surprisingly well. Taken a bunch of data from real life S2, 2013 and placed it into the institutional version of the course and it's worked all good.
    
5. Check the known institutional problems
    - [Bulk email](https://github.com/djplaner/moodle-mod_bim/issues/85) - fixed.
    - [User search](https://github.com/djplaner/moodle-mod_bim/issues/86).
        
        Stalling for some users. Works for others - having a registered feed may be a distinction?
        
        Having trouble identifying the cause. Wonder if it's purely a Postgresql problem. Try with another version of Moodle with MySQL.
        
        Works, but generates an error about curl:$count in lib/filelib.php - there is a call to SimplePie. - suggesting that the problem isn't Postgres, but the proxy configuration on the other Moodle server. Confirmed. This raises an issue with the timeout situation with curl (changed). But also about where this is being called - showing student details I imagine.
        
    - [All teaching staff are coordinators](https://github.com/djplaner/moodle-mod_bim/issues/87) - DONE
        
        Maybe due to how institutional roles are mapped to Moodle archetypes - examiner/teacher/moderator - editing teacher; tutor/non-editing teacher/marker - teacher.
        
        Vick Far - teacher (archetype editingteacher) - gets the coordinator view. Rick Nerf - marker (archetype teacher) - gets the marker view.
        

## Some new issues

As doing the above testing, am adding issues into GitHub associated with [a milestone](https://github.com/djplaner/moodle-mod_bim/issues?milestone=1&state=open). What follows is a record of dealing with those.

**[Undefined property warnings in locallib.php - 435](https://github.com/djplaner/moodle-mod_bim/issues/84)** - Fixed.

**[Ugly about messages](https://github.com/djplaner/moodle-mod_bim/issues/83)** - Fixed. Raises some potential to offer better support to folk around BIM.

## Share this with the world

These fixes need to be shared more broadly.

- Back to github
- Up to Moodle contrib

Done.