---
categories:
- bad
- netgl
date: 2015-08-18 16:40:40+10:00
next:
  text: github and the Moodle - Step 3
  url: /blog2/2015/08/20/github-and-the-moodle-step-3/
previous:
  text: Why should a teacher know how to code?
  url: /blog2/2015/08/18/the-role-of-coding-in-learning-and-teaching/
title: Visualising locations of students etc
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Refining a visualisation | The Weblog of (a) David Jones
      author_email: null
      author_ip: 192.0.83.14
      author_url: https://davidtjones.wordpress.com/2015/08/21/refining-a-visualisation/
      content: '[&#8230;] to refine the visualisation of students by postcodes started
        earlier this week. Have another set of data to work [&#8230;]'
      date: '2015-08-21 13:36:45'
      date_gmt: '2015-08-21 03:36:45'
      id: '1395'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
I've been set a task (asked nicely really) by my Head of School if it is possible to produce a map that will allow all and sundry to see the geographic spread of our students.

I vaguely remember doing something like this previously with Google maps, but I didn't think it "visual" enough. @palbion identified a couple of GIS experts in another school who could probably do it. I still don't know whether I can do it, but I'm using this as an opportunity to test the adage from Connectivism that

> The capacity to know is more critical than what is actually known (Siemens, 2008)

Can I use my "capacity to know" to solve this problem?

### Making a connection

Just over an hour ago I tweeted out a plea

https://twitter.com/djplaner/status/633502273172144128

Within minutes @katemfd tweeted and introduced me to "the Fresh Prince of Visualisation of Things on Maps"

https://twitter.com/KateMfD/status/633503201526808576

Who replied very quickly with this advice

https://twitter.com/cbhorley/status/633504046351908864

### Making many more connections

Now all I have to do is to grok [@cartodb](https://cartodb.com/) and produce a map.

But first, perhaps check [pricing and functionality](https://cartodb.com/pricing/). Looks like the free version will work. The small wrinkle is the absence of "private datasets". In the last week we've had a couple of serious emails make the rounds about student privacy. Will have to keep that in mind.

I should filter the data a bit more, but let's give it a go.

1. Drag and drop data onto the page
2. Nice interface to manipulate the data once uploaded.
3. First problem is geo-referencing the data. Postcodes are in the data, but not sure if this is sufficient. Need to look at the support. Looks like I might need to add country details. That's it.

First version done. Time to filter. At this stage, I'm not going to show the visualisations given the worry about privacy.

Oh nice, the platform automatically creates different visualisations including a heat map and has wizards to modify further.

That's produced a reasonable first go. Will need to refine it more, but enough to send off to the HoS.

That took no more than 20 minutes.

### So which is more important?

The original quote is

> The capacity to know is more critical than what is actually known

The above experience is actually a combination of both. The network I've built on Twitter - especially the brilliant @katemfd (performing as what Barabasi would call a network hub) - has provided the "capacity to know". It helped me access someone for whom @cartodb was "actually known".

But wouldn't Google have worked just as well?

A couple of weeks ago I had performed a quick Google search and didn't find @cartodb. I didn't "actually know" about it and so I had to spend too much time figuring out how "to know".

But even making the connection with @cbhorley wasn't sufficient. In order to use @cartodb effectively I used a range of stuff that I already "know".