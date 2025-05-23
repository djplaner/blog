---
categories:
- bad
- edc3100
- herding-cats
date: 2014-03-31 16:08:07+10:00
next:
  text: Staff need to be using the same tools they use to teach to also learn
  url: /blog/2014/04/02/staff-need-to-be-using-the-same-tools-they-use-to-teach-to-also-learn/
previous:
  text: 'Some areas of improvement for #edc3100'
  url: /blog/2014/03/28/some-areas-of-improvement-for-edc3100/
title: BIM and BAD
type: post
template: blog-post.html
---
This post arises from two events today

1. The [ASCILITE'2014](http://ascilite2014.otago.ac.nz/) call for papers came out today and I'm thinking about a paper I might submit.
2. The first #edc3100 assignment is due today and my use of BIM has struck a unique problem that I need to solve.

The third is that I'm a touch fried from answering queries about "I submitted my assignment the wrong way" (the main problem with these queries is that they mean I have to engage with a horrible online assignment submission system) that I need to engage in something else.

### The paper

The working title for the paper I'm thinking of is "The story of BIM: Being BAD as a way to bridge rhetoric and reality".

BAD is an acronym that captures what I think is missing from the institutional approach to university e-learning

1. **B**ricolage - the LMS as Enteprise Systems doesn't allow or cater for bricolage.
2. **A**ffordances - resulting in an inability to leverage the affordances of technology to improve learning and teaching.
3. **D**istribution - the idea that knowledge about how to improve L&T is distributed and the implications that has for the institutional practice of e-learning.
    
    i.e. current methods rely on the single, unified view of learning and teaching. A view that is expressed most concretely in the form of the LMS.
    
    This component will draw on a range of related "network" type theoretical perspectives including connectivism, Complex Adaptive Systems, embodied cognition and ANT - to name but a few.
    

The idea is if institutional e-learning is to get better, it needs to be BAD (more BAD?).

The following is an example of how the reality of using [BIM](/blog/research/bam-blog-aggregation-management/) in action supports the idea that it needs to be BAD. Or at least it's a very small step. It captures the messiness (the distribution) of e-learning in a typical university course. A messiness that isn't captured properly by PRINCE II and other methodologies, hierarchical organisational structures, appropriately total quality assured forms and processes and "theory" based abstractions like adopter categories.

And yes, there is some strong connection (repetition) with earlier perspectives/frameworks of mine. If at first you don't succeed, try, try again.

### Background

300+ students in EDC3100 are currently using their own blogs to reflect on their learning journey (to varying levels of engagement). Their blog posts contribute almost 15% of their final result in the course.

BIM is being used to keep a track of what they are sharing. The students create their blogs on Wordpress.com (or anywhere they like) and register them with BIM. BIM then keeps a copy of all their posts.

But BIM's capability don't match the learning design I'm using in this course. BIM was originally designed to have student posts made in response to specific prompts/questions and then have the posts marked manually be human markers. In EDC3100, the students blog about anything they want. We offer some prompts, but they can ignore them. Student posts aren't marked, instead students have to post a certain number of posts (on average) every week, the posts have to average a certain word count, and a certain number have to contain links to online resources and the blog posts of other students.

This analysis of student posts and the subsequent mark they get is done by a program I wrote. A bit of bricolage that takes bits and pieces of information extracted (with some difficulty) from various institutional systems and makes use of them in a way that solves my problem.

With a bit of bricolage each of the 300+ students have received an email recently telling them what the system knows about their progress. This gives them sometime to tick all the boxes prior to the first assignment being due (yep, still have due dates, haven't travelled too far from the well-worn paths).

### The problem

One student has reported a problem with what the system knows about their blog. The system says that only one of the posts links to another student post, but the student's blog actually has two posts that link to other student posts. This is confirmed.

But no-one else is reporting the problem. There's something unique about this student's blog that has picked up a bug in the system.

The uniqueness of this bug appears to me as one of the problems associated with the failure of institutional systems to deal with the Distribution aspect of BAD. In a complex, distributed knowledge network there is no one view. But the trad approach can only ever respond to one view. This argument needs a bit of work.

Typically this problem is because the author of the post has used a link other to the other student's blog. The program I wrote knows the URLs for all the student blogs. It checks all the links in a post against the known student posts.

I've visually checked the students blog posts in BIM and they are showing valid links to student blogs.

Argghh.

### The solution - Chrome is too smart - it's distribution

This is what I see when I look at the blog post using the Chrome browser

[![Chrome by David T Jones, on Flickr](http://farm8.static.flickr.com/7433/13530718753_60b06aeaa9_b.jpg "Chrome by David T Jones, on Flickr")](http://www.flickr.com/photos/david_jones/13530718753/)

The link that is shown is to the blog of another student. The program should pick this up and count it as a link.

Here's what I see when I view it under the Firefox browser

[![Firefox by David T Jones, on Flickr](http://farm3.static.flickr.com/2861/13530937114_2829553b5d_b.jpg "Firefox by David T Jones, on Flickr")](http://www.flickr.com/photos/david_jones/13530937114/)

See the difference?

The student appears to have used some form of URL shortener. Looks like a Wordpress tool. While this shortened URL does point to the post of another student. My little system doesn't know how to convert a shortened URL into a full URL. So it doesn't count it.

It appears that I must have a plugin installed on Chrome (or perhaps Chrome is smart enough on its own) to automatically expand out the wp.me shortened URL into the full link and change what is shown to the user.

I as the user is ignorant of this change happening.

Not a bad example of Distribution. How cognition/smarts/learning is distributed amongst all of the tools. Change on bit of the network and the outcome changes.