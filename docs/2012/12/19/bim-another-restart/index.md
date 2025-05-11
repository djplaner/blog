---
categories:
- bim
date: 2012-12-19 08:09:46+10:00
next:
  text: Bug fix and to do for BIM
  url: /blog2/2012/12/28/bug-fix-and-to-do-for-bim/
previous:
  text: Why Moneyball is the wrong analogy for learning analytics
  url: /blog2/2012/12/17/why-moneyball-is-the-wrong-analogy-for-learning-analytics/
title: '"BIM: another restart?"'
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: Stephen Downes
      author_email: stephen@downes.ca
      author_ip: 156.34.62.205
      author_url: http://downess.wordpress.com
      content: Do you really think you need 14 (I counted) separate CC licenses for your
        own images on your own post? Licenses run amok!
      date: '2012-12-21 11:53:30'
      date_gmt: '2012-12-21 01:53:30'
      id: '542'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: David Jones
      author_email: davidthomjones@gmail.com
      author_ip: 118.208.64.188
      author_url: https://djon.es/blog/
      content: Probably not. Started using imagecodr on another post with someone else's
        photo.  Found it easier than the standard flickr process and a bad habit formed.
      date: '2012-12-23 06:43:17'
      date_gmt: '2012-12-22 20:43:17'
      id: '543'
      parent: '542'
      type: comment
      user_id: '1'
    
pingbacks:
    - approved: '1'
      author: Bug fix and to do for BIM &laquo; The Weblog of (a) David Jones
      author_email: null
      author_ip: 74.200.247.110
      author_url: https://djon.es/blog/2012/12/28/bug-fix-and-to-do-for-bim/
      content: '[...] work on getting BIM 2.0 up and going. In this post I&#8217;m trying
        to continue the work from a week or so ago. The main aim is to fix a bug with
        the manage marking [...]'
      date: '2012-12-28 11:22:02'
      date_gmt: '2012-12-28 01:22:02'
      id: '544'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The following is essentially an activity log/diary or the first steps of getting back into work on [BIM](/blog2/research/bam-blog-aggregation-management/). I'm hoping to have it ready to work with some [course redesign](/blog2/2012/12/14/4668/) I'm working on, but timelines may make that difficult.

The aim of this is to get the current version of BIM for Moodle 2.x up and running with Moodle 2.4+. The next step will be to determine what work needs to be completed on BIM and what new features might be useful.

In summary, it's surprisingly functional as is, much more than I remembered.

## Download and install Moodle 2.4

Moodle 2.4+ [downloaded from here](http://download.moodle.org/)

Stick it in an m24 directory under xampp and [follow the instructions](http://docs.moodle.org/24/en/Installing_Moodle).

All installed.

## Installing bim2

And now to get bim2 off [github](https://github.com/djplaner/BIM/tree/bim2). Mm, 8 months since I worked on the code. Not good.

\[code lang="bash"\]mkdir bim cd bim git clone https://github.com/djplaner/BIM.git mv BIM/\* . mv BIM/.git . rm -rf BIM \[/code\]

**Task:** I really need to look into the naming of that folder and using of git so there's no need to play with the file structure.

Visit the local Moodle website, picks up BIM ready to install. Oops, error.

> Plugin "mod\_bim" is defective or outdated, can not continue, sorry.  
> Debug info: Missing mandatory en language pack. Error code: detectedbrokenplugin

That's because I didn't clone the bim2 branch

\[code lang="bash"\]sudo git clone -b bim2 https://github.com/djplaner/BIM.git\[/code\]

And that has updated successfully. Now does it actually work?

## Testing it out

Ohh, pretty new interface for Moodle 2.4. Looks like the BIM icon will need to updated to work with the slightly bigger and different design for the module icons. (Click on the following images to see bigger versions)

[![Add a BIM activity by David T Jones, on Flickr](http://farm9.static.flickr.com/8352/8284658119_07c5bc4fb9_m.jpg "Add a BIM activity by David T Jones, on Flickr")](http://www.flickr.com/photos/david_jones/8284658119/)  
[![Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License](http://i.creativecommons.org/l/by-nc-sa/2.0/80x15.png "Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License")](http://creativecommons.org/licenses/by-nc-sa/2.0/)  by  [David T Jones](http://www.flickr.com/people/david_jones/) [](http://www.imagecodr.org/)

After adding the activity you need to enter the basic configuration details

[![Filling in some BIM details by David T Jones, on Flickr](http://farm9.static.flickr.com/8083/8285717244_1392ba8f41_m.jpg "Filling in some BIM details by David T Jones, on Flickr")](http://www.flickr.com/photos/david_jones/8285717244/)  
[![Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License](http://i.creativecommons.org/l/by-nc-sa/2.0/80x15.png "Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License")](http://creativecommons.org/licenses/by-nc-sa/2.0/)  by  [David T Jones](http://www.flickr.com/people/david_jones/) [](http://www.imagecodr.org/)

Add some questions that the students will blog in response to.

[![Questions being added by David T Jones, on Flickr](http://farm9.static.flickr.com/8077/8284657421_127c73e260_m.jpg "Questions being added by David T Jones, on Flickr")](http://www.flickr.com/photos/david_jones/8284657421/)  
[![Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License](http://i.creativecommons.org/l/by-nc-sa/2.0/80x15.png "Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License")](http://creativecommons.org/licenses/by-nc-sa/2.0/)  by  [David T Jones](http://www.flickr.com/people/david_jones/) [](http://www.imagecodr.org/)

What about allocating markers to mark the influx of posts?

[![BIM markers screen by David T Jones, on Flickr](http://farm9.static.flickr.com/8198/8284657843_49f2103fe8_m.jpg "BIM markers screen by David T Jones, on Flickr")](http://www.flickr.com/photos/david_jones/8284657843/)  
[![Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License](http://i.creativecommons.org/l/by-nc-sa/2.0/80x15.png "Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License")](http://creativecommons.org/licenses/by-nc-sa/2.0/)  by  [David T Jones](http://www.flickr.com/people/david_jones/) [](http://www.imagecodr.org/)

No users allocated to the course, so nothing there. Nice to see I'd thought of this condition. Time to allocate some students and teaching staff. So staff enrolled in the course. Can I manage marking now?

[![No groups by David T Jones, on Flickr](http://farm9.static.flickr.com/8063/8285798776_d940cacfab_m.jpg "No groups by David T Jones, on Flickr")](http://www.flickr.com/photos/david_jones/8285798776/)  
[![Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License](http://i.creativecommons.org/l/by-nc-sa/2.0/80x15.png "Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License")](http://creativecommons.org/licenses/by-nc-sa/2.0/)  by  [David T Jones](http://www.flickr.com/people/david_jones/) [](http://www.imagecodr.org/)

Not yet. I need to create some groups for the course. Markers aren't allocated individual students within BIM. They are allocated groups.

[![Groups by David T Jones, on Flickr](http://farm9.static.flickr.com/8065/8285799732_758277e547_m.jpg "Groups by David T Jones, on Flickr")](http://www.flickr.com/photos/david_jones/8285799732/)  
[![Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License](http://i.creativecommons.org/l/by-nc-sa/2.0/80x15.png "Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License")](http://creativecommons.org/licenses/by-nc-sa/2.0/)  by  [David T Jones](http://www.flickr.com/people/david_jones/) [](http://www.imagecodr.org/)

So with groups allocated, I can allocate a marker. Can I manage the markers? The coordinating teacher can see a list of all the markers and what they have (or haven't) marked yet.

[![Manage marking has an error by David T Jones, on Flickr](http://farm9.static.flickr.com/8070/8285799460_e2bec760f1_m.jpg "Manage marking has an error by David T Jones, on Flickr")](http://www.flickr.com/photos/david_jones/8285799460/)  
[![Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License](http://i.creativecommons.org/l/by-nc-sa/2.0/80x15.png "Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License")](http://creativecommons.org/licenses/by-nc-sa/2.0/)  by  [David T Jones](http://www.flickr.com/people/david_jones/) [](http://www.imagecodr.org/)

Oops, that's the first error in the code. Will have to revisit that.

Can I see the students I have to mark as a marker? This is the overview. It shows which of my students have registered their blogs (and for which I can mark something) and which haven't yet.

[![Your students by David T Jones, on Flickr](http://farm9.static.flickr.com/8479/8285798614_772b7a2d7b_m.jpg "Your students by David T Jones, on Flickr")](http://www.flickr.com/photos/david_jones/8285798614/)  
[![Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License](http://i.creativecommons.org/l/by-nc-sa/2.0/80x15.png "Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License")](http://creativecommons.org/licenses/by-nc-sa/2.0/)  by  [David T Jones](http://www.flickr.com/people/david_jones/) [](http://www.imagecodr.org/)

Now, let's see if I can do some marking.

[![Mark posts by David T Jones, on Flickr](http://farm9.static.flickr.com/8081/8285799322_76ce1acc84_m.jpg "Mark posts by David T Jones, on Flickr")](http://www.flickr.com/photos/david_jones/8285799322/)  
[![Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License](http://i.creativecommons.org/l/by-nc-sa/2.0/80x15.png "Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License")](http://creativecommons.org/licenses/by-nc-sa/2.0/)  by  [David T Jones](http://www.flickr.com/people/david_jones/) [](http://www.imagecodr.org/)

Not really because none of the posts from this single student have been allocated to one of the set questions. I'll need to allocate one of his posts to a question using the "allocate question" screen.

[![Allocating posts by David T Jones, on Flickr](http://farm9.static.flickr.com/8224/8284740141_183caf08d1_m.jpg "Allocating posts by David T Jones, on Flickr")](http://www.flickr.com/photos/david_jones/8284740141/)  
[![Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License](http://i.creativecommons.org/l/by-nc-sa/2.0/80x15.png "Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License")](http://creativecommons.org/licenses/by-nc-sa/2.0/)  by  [David T Jones](http://www.flickr.com/people/david_jones/) [](http://www.imagecodr.org/)

Now I should be able to mark that allocated question

[![Marking a post by David T Jones, on Flickr](http://farm9.static.flickr.com/8076/8285799122_8e83204da7_m.jpg "Marking a post by David T Jones, on Flickr")](http://www.flickr.com/photos/david_jones/8285799122/)  
[![Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License](http://i.creativecommons.org/l/by-nc-sa/2.0/80x15.png "Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License")](http://creativecommons.org/licenses/by-nc-sa/2.0/)  by  [David T Jones](http://www.flickr.com/people/david_jones/) [](http://www.imagecodr.org/)

### Student perspective

So, does it work from the student's perspective. Does the activity show up when they login to the course?

[![Course view by David T Jones, on Flickr](http://farm9.static.flickr.com/8060/8284692223_fcf0ab4f40_m.jpg "Course view by David T Jones, on Flickr")](http://www.flickr.com/photos/david_jones/8284692223/)  
[![Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License](http://i.creativecommons.org/l/by-nc-sa/2.0/80x15.png "Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License")](http://creativecommons.org/licenses/by-nc-sa/2.0/)  by  [David T Jones](http://www.flickr.com/people/david_jones/) [](http://www.imagecodr.org/)

Can the register their blog?

[![Register the blog by David T Jones, on Flickr](http://farm9.static.flickr.com/8065/8284692093_b993397227_m.jpg "Register the blog by David T Jones, on Flickr")](http://www.flickr.com/photos/david_jones/8284692093/)  
[![Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License](http://i.creativecommons.org/l/by-nc-sa/2.0/80x15.png "Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License")](http://creativecommons.org/licenses/by-nc-sa/2.0/)  by  [David T Jones](http://www.flickr.com/people/david_jones/) [](http://www.imagecodr.org/)

Does it actually work as expected?

[![Successful registration by David T Jones, on Flickr](http://farm9.static.flickr.com/8503/8285751550_f2488d02b5_m.jpg "Successful registration by David T Jones, on Flickr")](http://www.flickr.com/photos/david_jones/8285751550/)  
[![Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License](http://i.creativecommons.org/l/by-nc-sa/2.0/80x15.png "Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License")](http://creativecommons.org/licenses/by-nc-sa/2.0/)  by  [David T Jones](http://www.flickr.com/people/david_jones/) [](http://www.imagecodr.org/)

## What's next?

Time for a road trip. So no progress for a few days, after that it will be revisiting what outstanding tasks are left to make this truly useful. Gradebook integration is probably the top of the list. Backup/restore may be the next step.