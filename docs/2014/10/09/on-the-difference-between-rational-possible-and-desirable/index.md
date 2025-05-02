---
title: On the difference between \"rational\", \"possible\" and \"desirable\"
date: 2014-10-09 11:24:43+10:00
categories: ['bad', 'elearning', 'indicators']
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: M-H
      author_email: mhward@bigpond.net.au
      author_ip: 129.78.233.211
      author_url: null
      content: I don't disagree with anything here on the dangers of whole-of-institution
        approaches. But there are many other ways to use analytics, and I know people
        in my own institution who are being creative with the data from LMS sites. They
        are using aggregated quiz results, for example, to identify concepts that they
        aren't teaching well, that students are getting consistently wrong.They are looking
        at how students use the site, and changing its structure to meet that better.
        They are using LTIs and comparing levels of student use with the use of the LMS
        and adjusting their teaching accordingly. I'm not saying these are the majority
        of teaching staff, but they are finding good ways to use the data to improve teaching
        and learning. In the end, teaching isn't about LMSs, LTIs, lecture capture, image
        databases, streaming video or videoconferencing (all enterprise tools that we
        provide). It's about the engagement between staff members and students that those
        tools can enhance. Anything the institution does to describe or measure teaching
        is just a (faint) reflection of that.
      date: '2014-10-09 12:40:59'
      date_gmt: '2014-10-09 02:40:59'
      id: '1145'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: David Jones
      author_email: davidthomjones@gmail.com
      author_ip: 1.120.217.184
      author_url: https://djon.es/blog/
      content: 'Looks like we''re in broad agreement. I''m not arguing that there isn''t
        useful applications of analytics. But it''s almost invariably going to be within
        the specifics of the learning experience. Aggregated quiz results work well in
        a learning design that includes quizzes.  What I''m increasingly seeing however
        is a focus on the "do it to/for" path which requires a whole of institution approach,
        rather than a "do it with" path that focuses on helping discover and leverage
        how learning analytics can help.
    
    
        The problem isn''t that teachers don''t want to use the available data to improve
        student learning and their own teaching. It''s often that it''s too hard to leverage
        the data.  For example, "looking at how students use the site".  <a href="https://djon.es/blog/2014/09/21/breaking-bad-to-bridge-the-realityrhetoric-chasm/#MAV"
        rel="nofollow">This section</a> from another ASCILITE''14 paper talks about the
        difficulties (and a solution) at one institution of performing this task.'
      date: '2014-10-10 11:41:52'
      date_gmt: '2014-10-10 01:41:52'
      id: '1146'
      parent: '1145'
      type: comment
      user_id: '1'
    
pingbacks:
    []
    
---
A couple of weeks ago @kateMfD wrote a post asking ["What next for the LMS?"](http://musicfordeckchairs.wordpress.com/2014/09/27/what-next-for-the-lms/). (one of a raft of LMS posts doing the rounds recently). Kate's point was in part that

> The LMS is specifically good at what universities need it to do. Universities have learning management systems for the same reason they have student information systems: because their core institutional business isn’t learning itself, but the governance of the processes that assure that learning has happened in agreed ways.

The [brief comment](http://musicfordeckchairs.wordpress.com/2014/09/27/what-next-for-the-lms/#comment-2604) I shared on Kate's post shared some discussions @beerc and I had 6 or 7 years ago. Back then we were responsible for helping academic staff use the institution's LMS. I was amazed at how manual the process was and how limited it was in its use of standard checks. For example, it was quite common for a new course site to be pointing to last year's course profile/synopsis (a PDF). This wasn't being picked up until a student or two complete all of the following steps

1. Actually bothered use the link to the course profile form the course site.
2. Figured out that it was pointing to last year's course profile.
3. Was bothered enough by this problem to report it to someone.

Rather than be reactive, it seemed sensible to write a Perl script or two that would "mine" the Blackboard database and identify these types of problems very early in the semester so we could proactively fix them.

At that stage, "management" couldn't grasp the value of this process and it never went anywhere. I never could understand that.

### Fear of management rising

Not long after that - as the learning analytics fad started to rise - Col and I were worried about what management would do once they joined the band wagon. In particular, we wondered when they might identify the problems that ideas like "Web 2.0 tools" (blogs, Second Life etc) or Personal Learning Environments (another fad [we were playing](/blog2/publications/ples-framing-one-future-for-lifelong-learning-e-learning-and-universities/) with at the time) would pose for learning analytics. i.e. to run "learning analytics" you need to have access to the data and a University generally won't have access to the data from tools that are personal to the learner and external to the institution.

Given Kate's identification of management's purpose around learning - "governance of the processes that assure that learning has happened in agreed ways" - Col and I have been waiting to hear of Universities banning the use of external/personal tools for learning/teaching because it broke their "learning analytics". Around the same time as Kate's post, I heard that on southern University was indeed going down that route, and [that's the comment](http://musicfordeckchairs.wordpress.com/2014/09/27/what-next-for-the-lms/#comment-2604) I made on Kate's post.

### Why is this a problem?

This morning @drwitty\_knitter [replied to my comment](http://musicfordeckchairs.wordpress.com/2014/09/27/what-next-for-the-lms/#comment-2604) with

> I would think this is quite common. Universities like to be able to track where money is being spent and what the outcomes are for students. Unless tools have some way to report what students are doing, and how that relates to their curricular goals, it would be hard to justify their use.

And I agree, I think it will becoming increasingly common. But I also still think it's a really, really bad idea. @beerc, @damoclarky and offered one explanation why this is a bad idea in [this ASCILITE'2012 paper](http://www.ascilite.org.au/conferences/wellington12/2012/images/custom/beer%2ccolin_-_analytics_and.pdf) i.e.

> Insight gained over the last four years exploring learning analytics at one university suggest that the assumptions embodied by managerialism may be an inappropriate foundation for the application of learning analytics into tertiary learning environments

In short, in order to believe it is possible to use analytics to connect what students are doing with their curricular goals can only occur if you make a range of assumptions about the nature of people, learning, and universities that fails to engage effectively with reality. No matter how complex the learning analytics algorithms and systems used, the only way you can achieve the stated purpose is to attempt to reduce the variability of learning and teaching to fit the limitations of the capabilities of the technology.

Which is exactly what is happening when institutions ban the use of personal or external tools.

This won't be enough. As we show in the ASCILITE paper, even if you limit yourself to the LMS, the diversity of learners and learning; and, the chasm between what happens in the LMS and actual student learning is such that there will still be huge questions about what the analytics can tell you. This will lead to at least two likely outcomes

1. Management will believe what the analytics tells them and plan future action on this poor foundation; and,
2. Management won't believe the analytics and thus will further reduce the variability of learning and teaching to fit the limitations of the capabilities of the technology.

The last option contributes to the problem that Chris Dede identifies [in this clip](https://dl.dropboxusercontent.com/u/14025788/dede.mp3):

> that the very, very best of our high-end learning environments have less variety than a bad fast food restaurant

### The three paths

In an [ASCILITE'2014 paper](/blog2/2014/09/05/three-paths-for-learning-analytics-and-beyond-moving-from-rhetoric-to-reality/) we identify three paths that might be followed with learning analytics

1. Do it to.
2. Do it for.
3. Do it with.

Our argument is that almost all of the learning analytics work (and increasingly much of what passes for learning and teaching support activities) is following the first two paths. We also argue that this will end badly for the quality of learning and teaching and will contribute to learning analytics being yet another fad.

The "Do it to" path is completely rational if your task is to ensure the quality of learning across the institution. But it's only possible if you assume that there is no diversity in learning and teaching and that "learning" is the data captured in digital trials left in institutional databases. I don't think it is either possible or desirable, hence I don't think it's rational. YMMV.