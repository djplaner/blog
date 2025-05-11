---
categories:
- indicators
date: 2010-05-14 16:51:28+10:00
next:
  text: Is there more to communities of practice?
  url: /blog2/2010/05/16/is-there-more-to-communities-of-practice/
previous:
  text: Qualms about the alignment project
  url: /blog2/2010/05/14/qualms-about-the-alignment-project/
title: Some tweaks to the indicators block
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Moodle Block Development &laquo; Col&#039;s Weblog
      author_email: null
      author_ip: 66.135.48.157
      author_url: http://beerc.wordpress.com/2010/05/14/moodle-block-development/
      content: '[...] Block&nbsp;Development This is a quick response to David&#8217;s
        post today. We are endeavoring to collaborate on the development of a Moodle block.
        A more detailed [...]'
      date: '2010-05-14 19:33:44'
      date_gmt: '2010-05-14 09:33:44'
      id: '3048'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
Yesterday's [post](/blog2/2010/05/13/getting-started-with-cols-indicators-block/) introduced Col's initial work on the indicators block. This post reports on some minor tweaks I've been doing this afternoon, trying to find escape in something concrete.

### Setting the title

As reported in the last post, the block ended up having a title _\[\[Indicators\]\]_. This was because get\_string was being used to set the title but the necessary language file (from which to source the string) was not created.

First fix is to just hard code the title.

\[sourcecode lang="php"\] $this->title = "Indicators"; //get\_string('Indicators','block\_indicators'); \[/sourcecode\]

That works. But the proper solution would be to figure out where the "lang" file should go for a block. According to [this](http://moodle.org/mod/forum/discuss.php?d=41061), it should be lang/en/block\_BLOCKNAME.php. Small problem, that should be lang/en\_utf8, not lang/en (as per [here](http://moodle.org/mod/forum/discuss.php?d=149971)).

\[sourcecode lang="php"\] $this->title = get\_string("indicators","block\_indicators"); \[/sourcecode\]

Will commit those changes.

### How to distinguish user roles?

The block was using roleid=5 as a way to identify students. I believe this is a deprecated approach. So need to find a better way. In my wonderings, I came across an approach that users the has\_capability function along with some "legacy" capabilities for student, staff, guest and admin. The following is an early example from the block

\[sourcecode lang="php"\] if ( has\_capability( 'moodle/legacy:teacher', $context )) { print "This is a teacher<br />"; } else if ( has\_capability( 'moodle/legacy:student', $context )) { print "This is a student<br />"; $canview=0; } \[/sourcecode\]

### What's next

At least in my head, the plan is to enable different groups of users to see different sets of "indicators". Where an "indicator" is a single graphic. This means that we need an good way to:

- distinguish between different users;
- call different code to generate the indicators for the different users;
- distinguish which indicator a user wishes to see;
- call different code based on the indicator.

A nice structure to do that, might be next on the list. If I was in Perl, I'd be doing this with a factory class. Should we go OO in PHP?

Some other tasks:

- I'm getting errors when running the block as a teacher. \[sourcecode lang="bash"\] Table 'moodle.m\_course' doesn't exist
    
    select (count(\*)/count(distinct(userid))) from mdl\_log where course='4' and userid='3' and action in ('add discussion','add post','update post') and course in (select id from m\_course where idnumber like '%2010') and userid in ( select userid from m\_role\_assignments where roleid !='5' and contextid in (select id from m\_context where contextlevel='50')) line 686 of lib/dmllib.php: call to debugging() line 379 of lib/dmllib.php: call to get\_recordset\_sql() line 71 of blocks/indicators/block\_indicators.php: call to count\_records\_sql() line 317 of blocks/moodleblock.class.php: call to block\_indicators->get\_content() line 341 of blocks/moodleblock.class.php: call to block\_base->is\_empty() line 338 of lib/blocklib.php: call to block\_base->\_print\_block() line 276 of course/format/weeks/format.php: call to blocks\_print\_group() line 229 of course/view.php: call to require()
    
    Warning: Division by zero in /Applications/XAMPP/xamppfiles/htdocs/moodle/blocks/indicators/block\_indicators.php on line 80
    
    Warning: Division by zero in /Applications/XAMPP/xamppfiles/htdocs/moodle/blocks/indicators/block\_indicators.php on line 86 \[/sourcecode\]
- What should an admin user see when they view the block?
- Check the performance of the existing SQL code and think about how/what we might need to do to significantly reduce that.