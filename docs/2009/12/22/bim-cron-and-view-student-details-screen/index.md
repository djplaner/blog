---
title: BIM - cron and view student details screen
date: 2009-12-22 15:42:01+10:00
categories: ['bim']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: BIM &#8211; minor fixes to show student details &laquo; The Weblog of (a)
        David Jones
      author_email: null
      author_ip: 74.200.245.188
      author_url: https://djon.es/blog/2009/12/24/bim-minor-fixes-to-show-student-details/
      content: '[...] &#8211; minor fixes to show student&nbsp;details  This post follows
        on from the last post in doing some minor improvements to the show student details
        screen in BIM. This [...]'
      date: '2009-12-24 08:18:50'
      date_gmt: '2009-12-23 22:18:50'
      id: '2901'
      parent: '0'
      type: pingback
      user_id: '0'
    
---

See also: [[blog-home | Home]]

In the [last bit of BIM work](/blog2/2009/12/22/bim-creating-the-test-data-completing-dbase-design/) I'd successfully created some test data and laid out some rough plans for what is next.

The aim of this post is to document the bit of work done on the show details screen up and going. The initial work on the screen was [documented here](/blog2/2009/12/20/bim-savingmanipulating-rss-files/). This post draws on the test data, adds some support functions to manipulate it and improves the screen.

Should be fairly simple.

### What's to be done - testing the test data

First, things first. There's an error when I view a BIM as the old student I was using for testing. Perhaps it is time to test out one of the new students.

Choose one of the students enrolled in one of the courses, use the dummy password and we're away. Get into the course, click on the bim activity and get an "error getting feed for" error.

This error comes about because the feeds aren't getting automatically updated/mirrored yet. So the attempt to look at the local RSS file fails.

At this stage, I could probably kludge this up and/or write the section of BIM that should do the updating - i.e. run from cron. That's what we'll do.

### Moodle, activity modules and cron

So now begins the trawl through the Moodle resources to find out how to run/define cron activity from an activity.

The `version.php` file in each activity defines a cron value, which appears to identify how regularly to do something. The question is what?

This appears to be answered [here](http://moodle.org/mod/forum/discuss.php?d=139341) with the details being that this value specifies how regularly (in seconds) to run the _modulename_\_cron method defined in the lib.php file.

### What to do?

The `bim_cron` function basically has to check all the current bim activities that are being mirrored, for all registered student feeds, it has to attempt to do a mirror on the feed URL and the copy of the feed on disk. Some pseudo-code

```
$mirrored = get_mirrored_bims()
foreach ( $mirrored as $bim )
{
  $students = get_registered_feeds( $bim );
  foreach ( $students as $student )
  {
    mirror the feed;
  }
}
```

One of the problems in writing this is the testing of the code for the above. Running from cron complicates the testing, so I'm going to run it from the show student details screen while under development.

Most of that is all working. Just working on the question of doing the mirroring process.

### Implications

Looking into this has led me down the path of using the SimplePie caching mechanism for maintaining the local versions of the RSS files, rather than the original method. This has resulted in a few other changes in how the rss is retrieved, but it's all working.

As a result some of the necessary changes to the show details screen happen automatically.

### What's next

Some minor tasks related to the show details screen to do:

- Do something about the link between the question ID and the question name in both Marked answers and All posts sections.
- Double check the display of the "All posts".
- Add in the link to posts for Marked Answers.
- Re-do the interface to be Moodle like.