---
categories:
- design-theory
- elearning
- moodle
- phd
- thesis
- webfuse
date: 2011-02-13 17:24:50+10:00
next:
  text: '"bim2: Some more coordinator tabs"'
  url: /blog2/2011/02/13/bim2-some-more-coordinator-tabs/
previous:
  text: 'bim2: Starting on the coordinator models'
  url: /blog2/2011/02/13/bim2-starting-on-the-coordinator-models/
title: On the potential flexibility of open source LMS and its limits
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: davidtjones
      author_email: davidthomjones@gmail.com
      author_ip: 60.229.53.187
      author_url: https://djon.es/blog/
      content: "In response to the above @mylescarrick suggested some agreement with the\
        \ sentiment and also suggests that Universities are \"poorly positioned to tread\
        \ the innovation line effectively\".\n\nI agree. But I also think there's another\
        \ side effect - somewhat related - of the above and that is a loss of responsiveness.\
        \  The limited flexibility of an institutional LMS - especially to the little\
        \ tweaks - means that for staff and student users the LMS increasingly is seen\
        \ as being unresponsive to their needs. This subsequently leads to less than positive\
        \ feelings which in turn can prevent innovation.\n\nThe above example is not a\
        \ great example, but it will do. An advanced Moodle user can probably come up\
        \ with a workaround that requires them to perform some significant additional\
        \ manual work to achieve their goal using Moodle features. They might even feel\
        \ proud. But over time they will become frustrated that Moodle can't do this for\
        \ them.\n\nOn the other hand, a system which does and can respond to the small\
        \ problems that users have, helps create a more positive mindset about the system\
        \ and using it. It helps to start to develop a feeling of trust between the student/staff\
        \ users, the system and the folk that look after it. For me, this a much firmer\
        \ foundation on which to build innnovation.\n\nNot sure it's all that different\
        \ or I've made this point well.  The following quote from Behrens (2009) from\
        \ a user of a responsive system (the one on which my thesis is based) gives a\
        \ better sense of what I mean\n<blockquote>I remember talking to [a Webfuse developer]\
        \ and saying how I was having these problems with uploading our final results\
        \ into [the Enterprise Resource Planning (ERP) system] for the faculty. He basically\
        \ said, \u201CNo problem, we can get our system to handle that\u201D\u2026 and\
        \ \u2018Hey presto!\u2019 there was this new piece of functionality added to the\
        \ system\u2026 You felt really involved\u2026 You didn\u2019t feel as though you\
        \ had to jump through hoops to get something done.</blockquote>\n\nI've <a href=\"\
        https://djon.es/blog/2010/09/18/dilbert-as-an-expository-instantiation/\" rel=\"\
        nofollow\">used it before</a> making a similar point."
      date: '2011-02-14 10:41:26'
      date_gmt: '2011-02-14 00:41:26'
      id: '3253'
      parent: '0'
      type: comment
      user_id: '1'
    
pingbacks:
    - approved: '1'
      author: "Tweets that mention On the potential flexibility of open source LMS and\
        \ its limits \xAB The Weblog of (a) David Jones -- Topsy.com"
      author_email: null
      author_ip: 208.74.66.43
      author_url: http://topsy.com/davidtjones.wordpress.com/2011/02/13/on-the-potential-flexibility-of-open-source-lms-and-its-limits/?utm_source=pingback&utm_campaign=L2
      content: '[...] This post was mentioned on Twitter by Claire Brooks and Greg Bird
        (Birdy), David Jones. David Jones said: New post - http://bit.ly/hYc8d2 - On the
        potential flexibility of open source LMS and its limits #moodle [...]'
      date: '2011-02-14 11:40:08'
      date_gmt: '2011-02-14 01:40:08'
      id: '3254'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: Getting an overview of the term ahead &laquo; The Weblog of (a) David Jones
      author_email: null
      author_ip: 76.74.254.43
      author_url: https://djon.es/blog/2011/02/15/getting-an-overview-of-the-term-ahead/
      content: '[...] the long term, is another example of the problems facing institutional
        systems touched on briefly in the post around open source LMS. The IT folk at
        this institution are focused on package provision, not on the user. They will
        [...]'
      date: '2011-02-15 17:25:54'
      date_gmt: '2011-02-15 07:25:54'
      id: '3255'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
Today a mate [posted to his blog](http://beerc.wordpress.com/2011/02/13/start-of-a-small-project/) about a small project he's involved with. The context of this project seems to be a good opportunity to comment on the potential flexibility of open source LMS and the limits of that flexibility within an institutional context. It's also an attempt to link it back to the design theory described in [my thesis](/blog2/research/phd-thesis/) (if you want more of the theory behind the following, look at the thesis).

The following uses Moodle as an example, but I believe that similar limitations exist regardless of the open source LMS. This is in part because a significant limit on the flexibility is not the LMS, but instead the institutional governance processes and associated factors..

### The need

In this case, the need is to send students an email with a link to a survey. The link has been personalised based on the students' membership of Moodle groups. They survey asks them to answer questions based on their experience of a group task.

My initial thought would be that this sounds like something Moodle should be able to do. Given the increasing emphasis on group related work I doubt that this is a novel requirement. So, there might be something in Moodle that can do this, however, based on my limited knowledge of Moodle I can't think of anything off the top of my head.

I believe that there might be the functionality within Moodle to do each of the components of this task. There is probably a way to send emails to members of a group. There might even be a way to customise that email to some extent (there is a [bulk email facility](/blog2/2010/05/28/one-potential-approach-to-provide-a-moodle-email-merge-facility/) in Moodle 1.9, but, from memory, it seems somewhat limited). There is also probably a way to do a group-based survey (a MCQ might be the obvious solution).

But I doubt that there is an easy way to combine these separate functions so that the group email can automatically include the link to the group's MCQ/survey.

### Doing it outside of Moodle

There is another interesting and related comment in [post describing this project](http://beerc.wordpress.com/2011/02/13/start-of-a-small-project/)

> hile not ideal in that it is a separate system from the LMS, it is hoped that this trial will help inform the development of a Moodle module that will perform the same function albeit in a more integrated and seamless way

Over 6 months ago, I used to work at the institution being described. Based on that out-of-date experience, my initial guess is that "doing it outside of Moodle" is deemed to be easier than engaging with Moodle and the institutional IT department.

### Two limits of open source LMS flexibility

Drawing on the above examples, I'd like to propose at least two, somewhat related limits on the flexibility of open source LMS:

1. Inflexible institutional structures and processes.
2. The difficulty of producing/the absence of scaffolding conglomerations.

#### Inflexible institutional structures and processes

Modifying an enterprise implementation of Moodle effectively and efficiently is hard. You don't want your institution's Moodle instance to be unavailable to students and staff because a code change has broken something drastically. The Moodle code-base is itself quite difficult to get a handle on. Not overly difficult, but a non-Moodle developer can't simply front-up and start making changes quickly. They need to be enculturated into the Moodle way, to learn what works and what doesn't. Such a requirements means that someone who is able to modify Moodle is often a scarce and expensive resources. Especially within most universities who often don't have someone dedicated as a Moodle developer.

To address this difficulty and also to [CYA](http://en.wikipedia.org/wiki/Cover_your_ass) (some might argue that CYA is the major reason) institution's spend a lot of time and effort setting up appropriate governance structures. The theory being that these are objective and rational ways to manage the difficult process and the expensive and scarce resource.

The trouble is that the difficulty and expense involved means that it becomes difficult for such processes to effectively engage in "small" problems like this one. i.e. problems that don't actually require development of any significantly new functionality or large-scale modules. It just needs a few minor changes or wrappers around existing functionality. For example, the requirement above could possibly be solved (the following is an example description given off the top of my head without any investigation as to whether this would work) by

- Modifying the Moodle quiz function to populate a database table linking groups to URLs for group specific quizzes.
- Modifying the existing Moodle bulk-email facility (or perhaps adding a wrapper around it like [I did with bim](/blog2/2010/05/30/2933/)) to use this database table to send personalised emails to group members.
- Perhaps add a new quiz report that allows viewing/comparing within/across groups.

For a variety of reasons traditional institutional LMS policies and processes are too heavy-weight to respond to this sort of need. Instead, in order for something like this to be considered, it has to be blown up into some institutional priority. e.g. a system to support peer and group-based assessment for the entire institution. A project that will require a significant amount of time doing a needs analysis,........

A big project that requires lots of resources is expensive enough to be efficiently considered by the governance and related processes. Small projects are too cheap to be efficiently considered by the expensive institutional processes.

In the hardware/operating systems field, this is a problem known as [starvation or indefinite postponement](http://books.google.com.au/books?id=QRoOAAAAQAAJ&lpg=PA100&ots=pkj0XZ9S0y&dq=indefinite%20postponement%20starvation&pg=PA117#v=onepage&q=starvation&f=false). The situation where a task is forever ignored because of a flaw in the priority mechanism.

So, I'm proposing that the institutional implementation of open source LMS end up suffer from the **"starvation limit"** on flexibility.

#### The need for rapid development of scaffolding conglomerations

The need in this case, at least to me, sounds like an example of what I termed [scaffolding, context-sensitive conglomerations](/blog2/2010/11/09/scaffolding-context-sensitive-conglomerations-v2-0/). Rather than necessarily requiring a brand new Moodle module or block, this problem sounds like something that actually needs to combine the functionality from a number of existing Moodle services. Something that conglomerates the lower-level functionality provided by Moodle into something that better meets this higher-level need.

A large part of the popularity of Moodle arises from its modularity. A feature that allows for the easy development of lots of new functionality. Something that increases the flexibility of Moodle.

The problem is that this flexibility arises, in part, from keeping these different modules separate. It's the separation that makes it easy to add a new function without (theoretically) worrying about how it will effect the other modules. They are meant to be independent. The current problems moving to Moodle 2.0 is an example of the problems that arise from dependency. All the third-party modules depend on the Moodle core, so when the Moodle core changes all the third-party modules have to change.

A strict separation between modules makes it more difficult to combine parts of these different modules into a scaffolding conglomeration.

So, I'm proposing that open source LMS have an "over reliance on module independence" that limits their flexibility.

### It's really all about balance

I can already here proponents of traditional institutional IT governance processes or strict software engineers bemoaning the problems of not having institutional governance or of module dependence. And I do agree. There are dangers and problems. I'm not suggesting that they should necessarily be done away with.

I do, however, think that too often the balance has gone too far one way. There needs to be more recognition of a need for balance the other way. A bit less of a focus on the objective, best ways of technical implementation, and a bit more on the subjective, best ways to improve learning and teaching.