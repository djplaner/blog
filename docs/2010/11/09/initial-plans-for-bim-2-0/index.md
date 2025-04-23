---
title: Initial plans for BIM 2.0
date: 2010-11-09 11:14:29+10:00
categories: ['bim']
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: Sarah
      author_email: sarahthorneycroft@me.com
      author_ip: 129.180.94.149
      author_url: http://teaspot.wordpress.com
      content: I haven't had a chance to read this fully yet, but one point did catch
        my eye, which is Moodle 2.0's ability to register external blog feeds. The way
        Moodle does this is still clunky atm, especially regarding association to a particular
        course for assessment purposes. To my mind it's not a replacement for BIM. Will
        have a more in-depth look and comment later on :).
      date: '2010-11-09 12:39:07'
      date_gmt: '2010-11-09 02:39:07'
      id: '3185'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: davidtjones
      author_email: davidthomjones@gmail.com
      author_ip: 124.187.41.86
      author_url: https://djon.es/blog/
      content: Thanks for the confirmation Sarah.
      date: '2010-11-09 14:49:04'
      date_gmt: '2010-11-09 04:49:04'
      id: '3186'
      parent: '3185'
      type: comment
      user_id: '1'
    - approved: '1'
      author: VRBones
      author_email: vrbones@hotmail.com
      author_ip: 118.208.191.118
      author_url: http://www.vrbones.com
      content: '&gt; Replace help pages with external wiki
    
    
        This what immediately sprang to mind when you mentioned a conglomeration around
        BIM usage itself. Maybe not an entire helpfile replacement, but gratuitious use
        of links down to the wiki could easily cover all those points. This way the absolute
        basics for people starting out are in a familiar format, but the meat of the information
        is only an ''edit'' away from collaboration.
    
    
        I''ve seen RSS embedding in wikis before, but even a wiki page where issues are
        discussed would be fine, and eventually linked to an actual github issue. This
        could also sidestep any contrib conversion issues later on.
    
    
        Personally I''d prefer access to a larger BIM community than any local support.
        For local support they could modify the basic help pages to indicate another help
        process if they wanted to.
    
    
        For combining into a moodle conglomeration of help may mean storing / hosting
        the wiki in a common moodle help area (a moodle site itself perhaps?), or simply
        gratuitous links to other moodle efforts.
    
    
        A Research page sounds very cool, and possibly supplimented with HowTo pages that
        demonstrate how to implement the various models within BIM would be ideal.'
      date: '2010-11-09 19:43:11'
      date_gmt: '2010-11-09 09:43:11'
      id: '3187'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: davidtjones
      author_email: davidthomjones@gmail.com
      author_ip: 124.185.183.42
      author_url: https://djon.es/blog/
      content: 'Thanks for the comments Tony.
    
    
        No promises on how much of this I can actually deliver.  Will wait and see.'
      date: '2010-11-09 22:57:39'
      date_gmt: '2010-11-09 12:57:39'
      id: '3188'
      parent: '3187'
      type: comment
      user_id: '1'
    
pingbacks:
    []
    
---

See also: [[blog-home | Home]]

I'm slowly getting out from under the thesis, which means I am starting to have some time to think about the next version of [BIM](/blog2/research/bam-blog-aggregation-management/). The following is an attempt to lay out some of the ideas I have for the next version of BIM. Beyond helping me gather my thoughts, I'm hoping it will generate some comments and ideas from others. I doubt I will be able to implement all of the suggestions, so I'm hoping to get a sense for what others think is most important.

Currently, I can think of the following categories of potential BIM improvements:

1. Work with Moodle 2.0;  
    This is the main driver for an upgrade. [Moodle 2.0](http://docs.moodle.org/en/Moodle_2.0_release_notes) will be out real soon now, and BIM will have to be modified to work with Moodle 2.0.
2. Maintaining BIM 1.0;  
    Not sure that everyone will be moving directly to Moodle 2.0. Suggests a need to maintain BIM 1.0 for a bit.
3. Get BIM into CONTRIB;  
    Good practice would see BIM in the Moodle contrib area.
4. Miscellaneous improvements;  
    Various [ideas](https://github.com/djplaner/BIM/issues) for how BIM can be improved have arisen from use of the current version. Would be good to action some of these.
5. Improving the code design; and  
    I'm shocked by just how spaghetti like the procedural code used in some of the Moodle modules (including BIM). It's so inflexible, gets in the way of reuse, and just basically ugly and error prone. Surely there are nicer ways to code a Moodle module. A MVC framework?
6. Scaffolding conglomerations.  
    This is perhaps where my main research interest resides. The interest comes from the thesis and the idea that e-learning systems need to improve. One suggestion for how this might be done is [scaffolding conglomerations](/blog2/2010/09/03/scaffolding-context-sensitive-conglomerations-in-e-learning-systems/). Borrowing ideas from [distributed cognition](/blog2/2010/10/06/making-the-lms-more-like-the-globe-theatre-distributed-cognition-the-extended-mind-and-moodle/) to move these systems from simple configuration interfaces into scaffolding that helps teachers and students teach/learn.

### Work with Moodle 2.0

Moodle 2.0 brings with it numerous changes to the various APIs which BIM relies upon. According to [release notes](http://docs.moodle.org/en/Moodle_2.0_release_notes#For_developers:_API_changes), looks like the changes that will need to happen include: database queries, file handling, and perhaps some display code.

There are also other sections of Moodle that BIM does (or could) rely upon which have also undergone changes. This may also suggest a need for updates. Possible areas of interest include:

- [Plagiarism prevention](http://docs.moodle.org/en/Plagiarism_Prevention);  
    Adding this support is one of the existing [issues for BIM](https://github.com/djplaner/BIM/issues#issue/6) and it appears that Moodle 2.0 might provide this service.
- [Backup and restore](http://docs.moodle.org/en/Moodle_2.0_release_notes#Backup_and_restore);  
    Apparently there is an entirely new format, improved interface etc. Suggests a need to update.
- [blogs](http://docs.moodle.org/en/Moodle_2.0_release_notes#Blogs);  
    Now includes support for external blog feeds. From scuttlebutt it sounds like this is done with SimplePie, which means BIM 2.0 probably won't need to include it. For some this native support within Moodle raises questions about the requirement for BIM. The difference is (I think) what BIM does with the feeds in terms of management and marking support. Something I don't think is done with Moodle 2.0, but should check.
- [Comments](http://docs.moodle.org/en/Moodle_2.0_release_notes#Comments);  
    Am wondering if this might offer an opportunity for students to comment within Moodle on other blog posts. Alternatively, as a way for staff to comment (mark) student blog posts, rather than BIM maintain its own record. This is probably the most questionable idea so far.

#### Installing and playing with Moodle 2.0

Much of the above is based on a skim of the Moodle 2.0 release notes. I'm sure to have missed important changes/additions and/or misunderstood the implications of other additions. **Feel free to point out implications I've missed or misunderstood.**

To remedy this I need to install Moodle 2.0 and start playing. Seems I already meet the [system requirements](http://docs.moodle.org/en/Moodle_2.0_release_notes#System_requirements). One less thing to do.


### Maintaining BIM 1.0

I'm guessing that at least some universities will be a bit slow in moving to 2.0. The final release of Moodle 2.0 is not yet out, it's supposed to be any day now. At least in Australia, that means most IT departments won't seriously consider it until March or April next year since most Australian Universities essentially shut down for summer and then rush to get the first term going. Which suggests for some, it will be June/July before any decision about running a Moodle 2.0 trial, perhaps over summer term 2011. So it is likely to be 2012 before some move to Moodle 2.0.

Which suggests a need to maintain and evolve BIM v1.0. Actually, this is somewhat connected to improving the code design. If done well, an improved BIM code design could make it much less effort to maintain the two different versions. But it still means extra work.

**At the moment, I'm leaning towards minimising updates to BIM 1.0 and focusing development on v2.0. If you think otherwise, let me know.**

### Get BIM into CONTRIB

All the best Moodle plugins are in [contrib](http://docs.moodle.org/en/Development:contrib). For various reasons I haven't followed through on getting BIM into contrib. This needs to change.

However, I'm going to lean towards producing code first. i.e. I plan to use the [BIM github area](https://github.com/djplaner/BIM) for development, work on getting v2.0 out, and along the way start the process of moving BIM into contrib.

**Are there negative implications of not being in CONTRIB that I'm unaware of? Should I push this a little harder?**

### Miscellaneous improvements

There are currently [13 open issues](https://github.com/djplaner/BIM/issues) (there is a 14th one which is migrate BIM to Moodle 2.0) associated with BIM v1.0. Most of these are ideas for improvement from folk using BIM or solutions to problems experienced. The following is a quick and dirty attempt at ranking/grouping those issues. Feel free to express dismay at the mis-categorisation of your favourite issue.

- Not required;  
    The [simplepie issue](https://github.com/djplaner/BIM/issues#issue/16) should not be required as I understand Moodle 2.0 includes Simplepie.
- Unimportant;  
    I just can't get excited about [the perceived need](https://github.com/djplaner/BIM/issues#issue/2) to open student blog posts in a new window.
- Nice and might happen;  
    - [Copy detection](https://github.com/djplaner/BIM/issues#issue/6) - as mentioned above Moodle 2.0 support for copy detection might enable this.
- Important improvements; and  
    - Support for ["deleting"](https://github.com/djplaner/BIM/issues#issue/8) student posts from BIM's consideration.
    - Better integration with the "Moodle way" - e.g. support for [grade scales](https://github.com/djplaner/BIM/issues#issue/3), better [integration with the gradebook](https://github.com/djplaner/BIM/issues#issue/25), and [support for groupings](https://github.com/djplaner/BIM/issues#issue/20)
    - Misc. additional BIM improvements: associate a [due date](https://github.com/djplaner/BIM/issues#issue/7) with a question; and, recording [who released a post](https://github.com/djplaner/BIM/issues#issue/27)
- Important interface improvements.
    - Re-design and expand the [student interface](https://github.com/djplaner/BIM/issues#issue/26)
    - Improve the [marker allocation](https://github.com/djplaner/BIM/issues/#issue/21) interface, including showing [missing allocations](https://github.com/djplaner/BIM/issues/#issue/32)
    - Improve the [marking interface](https://github.com/djplaner/BIM/issues/#issue/28)

### Improving the code design

The BIM code is ugly. This is partially (mostly?) due to me learning both PHP and "Moodle coding" during the implementation of BIM. But it is also due to the primitive procedural coding approach used by most Moodle plugins. Even for someone coming from using a [somewhat limited, home-grown MVC framework](/blog2/2010/06/07/the-wf-framework/), it was depressing and frustrating to have to step back to what I now see as the dark ages. Surely there has to be a better way?

It looks like it [has been talked about briefly](http://moodle.org/mod/forum/discuss.php?d=6842#p36429) and [not always well](http://moodle.org/mod/forum/discuss.php?d=66331) within the Moodle community. I recognise the difficulty of adopting such a radically different approach for Moodle as a whole. But I am wondering if anyone has done this within a plugin. I played [around with this](/blog2/2010/05/26/adding-multiple-visualisation-approaches-to-indicators-block/) earlier on and it seems to go okay. I guess performance would be one issue.

Will have to look at this further, but am likely to use an MVC approach within BIM v2.0. **Is this a good idea? A bad one? What have I missed in the Moodle community?**

### Scaffolding conglomerations

If I had to be doing more research, this is the area in which I'd be doing it. Just finished [another blog post](http://bit.ly/cEPm70) trying to re-explain the ideas behind scaffolding conglomerations. I'd really like to try and incorporate these ideas into BIM v2.0. What follows are some concrete ideas. Sadly, they are still early ideas and need to be thought through a bit more.

#### Making BIM help collaborative

One of the principles for [scaffolding conglomerations](/blog2/2010/11/09/scaffolding-context-sensitive-conglomerations-v2-0/) is

> Embed opportunities for collaboration and interaction into conglomerations

In the context of BIM, this doesn't mean what BIM already does in terms of blog posts etc. It has to do with how academics and students access help around using BIM.

BIM v1.0, like most Moodle plugins, includes some canned help pages. There are links to these pages in the BIM interface. Essentially these pages provide definitions/explanations (written by me) of basic BIM constructs and operations. These are not very good since I often write them as an after-thought and also because my familiarity with BIM (since I am its designer) almost certainly means that I see BIM very differently from other people. Nor do these help files enable any form of collaboration. They don't leverage the collection of people using BIM.

I'd like to expand/extend the help pages into some sort of collection of services that enables the complete collection of BIM users to collaborate. And by complete, I don't mean just within a Moodle instance. I mean across all Moodle instances that are using BIM.

Some possible examples:

- Replace help pages with external wiki/blog;  
    A wiki would allow anyone to edit the help pages or perhaps add comments. For some, going external might be seen as a problem. Might also confuse some people who are used to the standard process of using the institutional helpdesk.
- Integrate the issues page from github;  
    Provide some visible connection within the BIM interface to the BIM [issues list](https://github.com/djplaner/BIM/issues/#list). There's a problem here of balancing local institutional problem solving and assistance (being directed to an institutional helpdesk service) with the global BIM community.
- Supplement help pages with RSS feeds;  
    Rather than replace the institutional/Moodle help processes, supplement them with the addition of feeds from more global collaboration areas.
- Sharing designs; and  
    I wonder if it would be possible to implement an approach were BIM designs could be shared. Currently, this would be limited to just the questions. But later versions could include other configuration options. Not sure how useful this would be.
- Incorporate related literature.  
    There's a growing body of literature around the use of blogs in higher education. Would be useful to include links to this literature and reflections upon it within BIM. However, rather than hard-code this and make it something only I or some other technician can change. It would be more appropriate for it to be something people could collaborate around. Perhaps using functionality from [Mendeley](https://www.mendeley.com) or del.icio.us.

So, not easy. More thought given. **What other strategies are there for making the BIM help services more collaborative.**

#### Pro-active help

An existing [BIM issue](https://github.com/djplaner/BIM/issues/#issue/32) gives a concrete example. There are times when not all students using a BIM activity have been allocated a marker. BIM doesn't highlight this at the moment. If BIM were more pro-active, it would raise a warning or show a summary of the total number of students and the number that are allocated markers. This could be done via email or via the web interface. There are numerous other examples of similar common problems, including: students who haven't registered their blog, or posted a required post, or Markers who haven't used BIM yet.

A more complete approach might involve some type of [Moodle wizard](http://tomazlasic.net/2010/10/moodle-wizard/). A step by step process that guides the designer of the BIM activity through the decisions and trade-offs they have to make when setting up the activity.

#### Analytics

It looks like [analytics](/blog2/2010/09/04/light-weight-analytics-tools-as-part-of-scaffolding-context-sensitive-conglomerations/) (of some description) will play an increasing part in e-learning, especially in large classes. Analytics could form the basis for some form of scaffolding in BIM and not just for teachers. For example, some form of analytics that shows how the student is going with the BIM activity compared with other students. Potentially as some form of encouragement. e.g. the [progress bar block](http://www.sci.usq.edu.au/staff/deraadt/progressBar.html).

#### Conglomerations and conglomerations

This raises the question of how much should BIM do itself? Short answer is that BIM shouldn't reinvent the wheel. Where possible it should integrate with existing tools, like the progress bar. And this brings up the other aspect of conglomerations. A conglomeration is not meant to be just something like BIM. It's conceptualised as a combination of different services that are designed to act together.

So, someone who decides to use BIM, may not be aware of the progress bar block. BIM should perhaps actively inform them of that block (or other useful tools) and be able to work both with and without the progress bar block. Which raises the question of how/if BIM might use services provided by the progress bar block to provide scaffolding.

I think this is getting close to a problem I have with [stepwise refinement](http://it.toolbox.com/blogs/irm-blog/stepwise-refinement-25007) and which somewhat arises from the modular design of Moodle. If I focus too much on BIM, I miss the overall whole of Moodle. I miss the opportunities to work with the progress bar block.

However, it's more than me being aware of the whole of Moodle. It's the assumptions within the APIs etc of Moodle and the mindsets of the other plugin developers. If they are focused too much on stepwise refinement, they focus too much on what their module does. Not on what might be possible by enabling different plugins to leverage off each other.

This is an idea that needs further thought.