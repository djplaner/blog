---
categories:
- bim
date: 2009-12-20 18:03:32+10:00
next:
  text: Supporting curriculum mapping?
  url: /blog2/2009/12/21/supporting-curriculum-mapping/
previous:
  text: BIM - Getting &quot;show student details&quot; working
  url: /blog2/2009/12/17/bim-getting-show-student-details-working/
title: BIM - Saving/manipulating RSS files
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: BIM &#8211; Creating the test data, completing dbase design &laquo; The
        Weblog of (a) David Jones
      author_email: null
      author_ip: 76.74.255.67
      author_url: https://djon.es/blog/2009/12/22/bim-creating-the-test-data-completing-dbase-design/
      content: '[...] &#8211; Creating the test data, completing dbase&nbsp;design  The
        last bit of BIM work resulted in getting the show student details screen up and
        going, mostly. Any more of these screens [...]'
      date: '2009-12-22 11:30:07'
      date_gmt: '2009-12-22 01:30:07'
      id: '2896'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: BIM &#8211; cron and view student details screen &laquo; The Weblog of (a)
        David Jones
      author_email: null
      author_ip: 74.200.244.88
      author_url: https://djon.es/blog/2009/12/22/bim-cron-and-view-student-details-screen/
      content: '[...] the bit of work done on the show details screen up and going. The
        initial work on the screen was documented here. This post draws on the test data,
        adds some support functions to manipulate it and improves the [...]'
      date: '2009-12-22 15:42:17'
      date_gmt: '2009-12-22 05:42:17'
      id: '2897'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
In the [last post](/blog2/2009/12/17/bim-getting-show-student-details-working/) I'd gotten started having the show student details screen actually getting data from the database. One data source this screen needs is not in the database, it's in the RSS file from the student's blog that is mirrored on the Moodle site. This post talks about the process about how BIM will be saving, reading and using that RSS file in its operation.

There will be at least two parts:

1. Identifying the location for the RSS file (and putting some dummy ones there).
2. Manipulating the RSS files.

### Location

As discovered [in the last post](/blog2/2009/12/17/bim-getting-show-student-details-working/) Moodle works with a directory referred to as moodledata as the file system store. Each course has its own area in a sub-directory based on the course id.

So, the obvious plan would be to put a `bim` directory in the course sub-directory. Since there may be the case that more than one BIM activity could be added to a course, I'll put another layer of sub-directories in place based on the bim id. At that stage, we can use the userid, actually, I'm going to go with username (I'm still of the opinion that a support person may still look at the file structure and that the username - which @ my institution is the student number - will be more meaningful than the uid) as the filename and put a `.xml` extension on the end.

So, the path for my test user (username=david) on my test course (cid=4) and my test BIM activity (bim id=1) would be

> `$CFG->dataroot/4/1/david.xml`

Which means I can put some test data into the file.

### Manipulating RSS

Sadly, at this stage, the RAW book I've been using only has information about using a Moodle API for constructing RSS files from scratch. For BIM, we need to be able to use existing RSS files (also ATOM and other type of feeds) from existing blogs. So I don't think this is appropriate. Need to find what alternatives exist within the Moodle community.

I had [originally found](/blog2/2009/07/28/bam-into-moodle-7-an-estudyguide-block/) the magpie rss library. However, [it now appears](http://tracker.moodle.org/browse/MDL-7946) that Magpie is deprecated and [SimplePie](http://simplepie.org/) is preferred. So, looks like I'll use that.

This won't be the only place I'll have to manipulate a student's feed. So I should abstract this out. Straight procedural and into a library? Or, go object oriented? All my recent experience has been OO, but new to PHP. Might stick with procedural for now.

Next problem is getting SimplePie to parse the [feed](/blog2/blog-home.md) for this blog as a test. It appears that SimplePie doesn't like control characters in a feed. The problem here. Remove those and it works fine. **To do**: Figure out how to handle these cleanly. Need to make this robust.

The [SimplePie API](http://simplepie.org/wiki/reference/start) is documented online. It has a `get_feed_tags` function that should fulfill one of the needs for the registration process.

### Current status

The show student details screen is now almost fully working - sans any of the normal sanity checking and a few bits to tidy up. Some progress being made.