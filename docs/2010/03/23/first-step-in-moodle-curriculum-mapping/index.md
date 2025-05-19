---
categories:
- curriculummapping-cddu
date: 2010-03-23 14:13:24+10:00
next:
  text: The suffocating straightjackets of liberating ideas
  url: /blog/2010/03/24/the-suffocating-straightjackets-of-liberating-ideas/
previous:
  text: Why is University/LMS e-learning so ugly?
  url: /blog/2010/03/23/why-is-universitylms-e-learning-so-ugly/
title: First step in "Moodle curriculum mapping"
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Moodle curriculum mapping &#8211; Step 2 &laquo; The Weblog of (a) David
        Jones
      author_email: null
      author_ip: 74.200.244.84
      author_url: https://djon.es/blog/2010/03/30/moodle-curriculum-mapping-step-2/
      content: '[...] exploration of an idea for enhancing Moodle to enable curriculum
        mapping. It carries on from the first step and is part of a broader [...]'
      date: '2010-03-30 09:46:23'
      date_gmt: '2010-03-29 23:46:23'
      id: '2983'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: Moodle curriculum mapping &#8211; Step 3 &laquo; The Weblog of (a) David
        Jones
      author_email: null
      author_ip: 74.200.244.41
      author_url: https://djon.es/blog/2010/04/02/moodle-curriculum-mapping-step-3/
      content: '[...] outlined earlier there are some elements of a Moodle course site
        to which you can&#8217;t map outcomes. The outcomes [...]'
      date: '2010-04-02 13:58:49'
      date_gmt: '2010-04-02 03:58:49'
      id: '2984'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: How curriculum mapping in Moodle might work &laquo; The Weblog of (a) David
        Jones
      author_email: null
      author_ip: 76.74.255.104
      author_url: https://djon.es/blog/2010/05/19/how-curriculum-mapping-in-moodle-might-work/
      content: '[...] is being done as part of the alignment project and picks up from
        some earlier examination of Moodle&#8217;s existing outcomes [...]'
      date: '2010-05-19 21:05:33'
      date_gmt: '2010-05-19 11:05:33'
      id: '2985'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
This is perhaps the first concrete step in a [project](/blog/research/curriculum-mapping/) that is aiming to look at how the act of curriculum mapping can be embedded into the, increasingly, most common task and tool used by academics. That is, how can an LMS (like [Moodle](http://moodle.org/)) be used/modified to make curriculum mapping a part of what academics do, both in terms of maintaining the mapping, but more importantly using the mapping in interesting and useful ways.

As [outlined in a previous post](/blog/2010/03/10/moodle-outcomes-metadata-and-curriculum-mapping/) it appears that Moodle (the institutional LMS at my [current institution](http://www.cqu.edu.au/)) already has functions that offer some basic level of support for curriculum mapping. However, they are mostly used/intended for tracking student outcomes/performance. This post documents an initial foray into using these functions to implement some form of curriculum mapping. The plan is:

- Use existing functions to map a course or two and find out how that works and how it might be made better.
- Use the data of the mapping to generate some applications that use the data.

Turned out, due to having to fight other fires, that today's work was limited. Only small progress.

### The courses and the people

I'm working with 2/3 courses. Two from in and around public relations and one from psychology. More detail on these later.

### The set up

The plan is to perform this project on a copy of Moodle running on my laptop. i.e. it's separate from any systems people rely upon and allows me the freedom to code. I'll be taking backups of the live course sites for the above course, restoring them on my laptop's Moodle and mapping the courses.

My first problem was to restore the backups. I had an old version of libxml which meant the restore process in Moodle wasn't handling the HTML code all that well. So new install of xampp and Moodle - some wasted time. Really didn't like the new Nazi password approach that is now default in the version of Moodle I'm using. More passwords to write down. ;)

### Getting outcomes up and going

I'd had outcomes working on the old version of Moodle. My next barrier was getting outcomes to appear on the new. It wasn't happening simply and I was running out of time, so it sat for a bit. Here's what I've done to get it working:

- As the Moodle administrator, turn on outcomes under "General Settings"  
    Just typing "outcome" in the Moodle adminstrators block was the quickest way to find it.
- Create some outcomes  
    Either in the Admin box under grades or inside an individual course.
- Possibly add site wide outcomes to the course.  
    Outcomes option in course modify box.

Having completed those tasks the theory is that everytime you edit an activity or resource you will have an option to view and select appropriate outcomes.

### Outcomes

An outcome has the following data associated with it:

- Full and short name.
- Standard outcome - is it available site wide.
- Scale - which existing scale to use with the outcome.
- Description - textual description

Outcomes can be imported using as csv file. This could be useful as you could create a set of outcomes for a particular discipline in a CSV file and make them available for anyone to use. Folk at other institutions could import them and have a consistent set of outcomes.

Also, you may not want all discipline outcomes to be available site wide. Could annoy the mathematicians if they kept seeing outcomes from psychology etc. Having outcomes as a CSV would allow these to be imported at a course level. But maybe not...

### Checking when outcomes appear

Interested in seeing if the outcomes appear for all activities/resources. Doing a quick test with a couple of courses and reporting where it works. It works for

- Forums
- Resource
    - Web page
    - Link to file or web page

Doesn't work for

- Labels  
    Means of inserting text/HTML into the topics. Used by some to specify readings. Might want to have outcomes on these.
- Summary

### Reflections

As I was doing the above test, a few thoughts arose:

- What outcomes would you have for a course synopsis?  
    For some resources/activities they are too global, too high level to specify a list of outcomes/attributes etc. What do you do with these?
    
    Given that one of the aims might be to highlight "coverage", there are some things you wouldn't allocate anythign to.
    
- Why wouldn't you have outcomes associated with labels?
- The obvious question which has been bugging me for a while - not all activities/resources for a course are likely to be in the course site. Any curriculum mapping based on the LMS site is not going to be complete. Unless there is some change in practice on the part of the academics. Not a straight forward thing to do.