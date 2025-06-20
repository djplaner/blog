---
categories:
- bim
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
date: 2012-12-18 22:09:46
next:
  text: Bug fix and to do for BIM
  url: /blog/2012/12/28/bug-fix-and-to-do-for-bim/
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
previous:
  text: Why Moneyball is the wrong analogy for learning analytics
  url: /blog/2012/12/17/why-moneyball-is-the-wrong-analogy-for-learning-analytics/
template: blog-post.html
title: '"BIM: another restart?"'
type: post
---
The following is essentially an activity log/diary or the first steps of getting back into work on [BIM](/blog/research/bam-blog-aggregation-management/). I'm hoping to have it ready to work with some [course redesign](/blog/2012/12/14/4668/) I'm working on, but timelines may make that difficult.

The aim of this is to get the current version of BIM for Moodle 2.x up and running with Moodle 2.4+. The next step will be to determine what work needs to be completed on BIM and what new features might be useful.

In summary, it's surprisingly functional as is, much more than I remembered.

## Download and install Moodle 2.4

Moodle 2.4+ [downloaded from here](http://download.moodle.org/)

Stick it in an m24 directory under xampp and [follow the instructions](http://docs.moodle.org/24/en/Installing_Moodle).

All installed.

## Installing bim2

And now to get bim2 off [github](https://github.com/djplaner/BIM/tree/bim2). Mm, 8 months since I worked on the code. Not good.

```bash
mkdir bim 
cd bim 
git clone https://github.com/djplaner/BIM.git 
mv BIM/\* . 
mv BIM/.git . 
rm -rf BIM 
```

**Task:** I really need to look into the naming of that folder and using of git so there's no need to play with the file structure.

Visit the local Moodle website, picks up BIM ready to install. Oops, error.

> Plugin "mod\_bim" is defective or outdated, can not continue, sorry.  
> Debug info: Missing mandatory en language pack. Error code: detectedbrokenplugin

That's because I didn't clone the bim2 branch

```bash
sudo git clone -b bim2 https://github.com/djplaner/BIM.git
```

And that has updated successfully. Now does it actually work?

## Testing it out

Ohh, pretty new interface for Moodle 2.4. Looks like the BIM icon will need to updated to work with the slightly bigger and different design for the module icons. (Click on the following images to see bigger versions)

<figure markdown>
<a data-flickr-embed="true" href="https://www.flickr.com/photos/david_jones/8284658119/" title="Add a BIM activity"><img src="https://live.staticflickr.com/8352/8284658119_07c5bc4fb9_c.jpg" width="683" height="764" alt="Add a BIM activity"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
</figure>


After adding the activity you need to enter the basic configuration details

<figure markdown>
<a data-flickr-embed="true" href="https://www.flickr.com/photos/david_jones/8285717244/" title="Filling in some BIM details"><img src="https://live.staticflickr.com/8083/8285717244_1392ba8f41_c.jpg" width="800" height="609" alt="Filling in some BIM details"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
</figure>


Add some questions that the students will blog in response to.

<figure markdown>
<a data-flickr-embed="true" href="https://www.flickr.com/photos/david_jones/8285717244/" title="Filling in some BIM details"><img src="https://live.staticflickr.com/8083/8285717244_1392ba8f41_c.jpg" width="800" height="609" alt="Filling in some BIM details"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
</figure>


What about allocating markers to mark the influx of posts?

<figure markdown>
<a data-flickr-embed="true" href="https://www.flickr.com/photos/david_jones/8284657843/" title="BIM markers screen"><img src="https://live.staticflickr.com/8198/8284657843_49f2103fe8_c.jpg" width="800" height="194" alt="BIM markers screen"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
</figure>


No users allocated to the course, so nothing there. Nice to see I'd thought of this condition. Time to allocate some students and teaching staff. So staff enrolled in the course. Can I manage marking now?

<figure markdown>
<a data-flickr-embed="true" href="https://www.flickr.com/photos/david_jones/8285798776/" title="No groups"><img src="https://live.staticflickr.com/8063/8285798776_d940cacfab_c.jpg" width="800" height="313" alt="No groups"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
</figure>

Not yet. I need to create some groups for the course. Markers aren't allocated individual students within BIM. They are allocated groups.

<figure markdown>
<a data-flickr-embed="true" href="https://www.flickr.com/photos/david_jones/8285799732/" title="Groups"><img src="https://live.staticflickr.com/8065/8285799732_758277e547_c.jpg" width="759" height="471" alt="Groups"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
</figure>

So with groups allocated, I can allocate a marker. Can I manage the markers? The coordinating teacher can see a list of all the markers and what they have (or haven't) marked yet.

<figure markdown>
<a data-flickr-embed="true" href="https://www.flickr.com/photos/david_jones/8285799460/" title="Manage marking has an error"><img src="https://live.staticflickr.com/8070/8285799460_e2bec760f1_c.jpg" width="800" height="399" alt="Manage marking has an error"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
</figure>


Oops, that's the first error in the code. Will have to revisit that.

Can I see the students I have to mark as a marker? This is the overview. It shows which of my students have registered their blogs (and for which I can mark something) and which haven't yet.

<figure markdown>
<a data-flickr-embed="true" href="https://www.flickr.com/photos/david_jones/8285798614/" title="Your students"><img src="https://live.staticflickr.com/8479/8285798614_772b7a2d7b_c.jpg" width="800" height="633" alt="Your students"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
</figure>


Now, let's see if I can do some marking.

<figure markdown>
<a data-flickr-embed="true" href="https://www.flickr.com/photos/david_jones/8285799322/" title="Mark posts"><img src="https://live.staticflickr.com/8081/8285799322_76ce1acc84_c.jpg" width="800" height="335" alt="Mark posts"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
</figure>


Not really because none of the posts from this single student have been allocated to one of the set questions. I'll need to allocate one of his posts to a question using the "allocate question" screen.

<figure markdown>
<a data-flickr-embed="true" href="https://www.flickr.com/photos/david_jones/8284740141/" title="Allocating posts"><img src="https://live.staticflickr.com/8224/8284740141_183caf08d1_c.jpg" width="800" height="712" alt="Allocating posts"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
</figure>

Now I should be able to mark that allocated question

<figure markdown>
<a data-flickr-embed="true" href="https://www.flickr.com/photos/david_jones/8285799122/" title="Marking a post"><img src="https://live.staticflickr.com/8076/8285799122_8e83204da7_c.jpg" width="800" height="696" alt="Marking a post"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
</figure>

### Student perspective

So, does it work from the student's perspective. Does the activity show up when they login to the course?

<figure markdown>
<a data-flickr-embed="true" href="https://www.flickr.com/photos/david_jones/8284692223/" title="Course view"><img src="https://live.staticflickr.com/8060/8284692223_fcf0ab4f40_w.jpg" width="378" height="200" alt="Course view"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
</figure>

Can the register their blog?

<figure markdown>
<a data-flickr-embed="true" href="https://www.flickr.com/photos/david_jones/8284692093/" title="Register the blog"><img src="https://live.staticflickr.com/8065/8284692093_b993397227_w.jpg" width="400" height="194" alt="Register the blog"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
</figure>

Does it actually work as expected?

<figure markdown>
<a data-flickr-embed="true" href="https://www.flickr.com/photos/david_jones/8285751550/" title="Successful registration"><img src="https://live.staticflickr.com/8503/8285751550_f2488d02b5_w.jpg" width="400" height="351" alt="Successful registration"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
</figure>

## What's next?

Time for a road trip. So no progress for a few days, after that it will be revisiting what outstanding tasks are left to make this truly useful. Gradebook integration is probably the top of the list. Backup/restore may be the next step.
