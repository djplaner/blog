---
categories:
- bam
- chapter-5
- design-theory
- elearning
- plescquni
- thesis
date: 2009-03-10 15:37:10+10:00
next:
  text: Cooked course feeds - An approach to bringing the PLEs@CQUni, BAM and Indicators
    projects together?
  url: /blog2/2009/03/11/cooked-course-feeds-an-approach-to-bringing-the-plescquni-bam-and-indicators-projects-together/
previous:
  text: How to improve L&#038;T and e-learning at universities
  url: /blog2/2009/03/09/how-to-improve-lt-and-e-learning-at-universities/
title: Getting feeds out of BAM - the first steps
type: post
template: blog-post.html
---
The [Blog Aggregation Management (BAM) project](/blog2/research/bam-blog-aggregation-management/) is an attempt to be a bit more Web 2.0/SaaS in the implementation of e-learning within a University. BAM works by students creating and using their own blog on one of a number of freely available external blogging services and registering it with BAM. BAM provides some management infrastructure that integrates these external services with university information and also offers support for staff to mark and track student posts. The staff interface is primarily via a web interface.

Recently, I've been [thinking about](/blog2/2009/03/02/some-potential-updates-to-bam-a-step-towards-breaking-the-lmscms-orthodoxy/) changes to enable teaching staff to use RSS readers as their primary interface. This post details some initial steps towards achieving this.

### What's been done

A fairly simple addition has been made to BAM. The ability for an individual staff member to download an [OPML file](http://en.wikipedia.org/wiki/OPML). The OPML file contains pointers to the blogs for that staff member's students. Many CQUni courses have large numbers of staff teaching large numbers of students.

The OPML file can then be imported into a newsreader and used to track the posts students are making to their blogs. Without a need to visit the university supplied web interface.

The following screencast is intended to help CQUniversity staff make use of this feature. It also illustrates the why and what of the process.


!!! warning "Outdated content no longer available"

    Presentation from Slideshare no long available


### The next step

The feeds within the OPML file are the "raw" files from the student blogs. i.e. they only contain the students raw blog posts. There is no additional "cooking" of the feeds from the individual student blogs to add additional value. Some examples of "cooking" could include:

- Addition to each post of links back to the BAM web interface (e.g. a link to the interface that staff use to record a mark for each post).
- Addition of information about the student - their name, student number etc.

The aim is to get this initial "raw" feed feature out to the staff and see how they go with it. If all goes well, the "cooked" feed feature will come out later.