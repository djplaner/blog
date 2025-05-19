---
categories:
- moodleopenbook
- oep
- site2016
date: 2016-03-26 03:23:14+10:00
next:
  text: Setting up the analysis of student submissions
  url: /blog/2016/03/29/setting-up-the-analysis-of-student-submissions/
previous:
  text: 'SITE&#039;2016: LATs, OER, and SPLOTs?'
  url: /blog/2016/03/26/site2016-lats-oer-and-splots/
title: LATs, OER, TPACK, and GitHub
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: First steps in integrating LATs OER into Moodle open book &#8211; The Weblog
        of (a) David Jones
      author_email: null
      author_ip: 192.0.100.44
      author_url: https://davidtjones.wordpress.com/2016/04/02/first-steps-in-integrating-lats-oer-into-moodle-open-book/
      content: '[&#8230;] been released as Open Educational Resources (OERs) by Hofer
        and Harris (2016). As outlined in a prior post my plan is to use these OERs as
        a test case for the Moodle open book project. The aim being [&#8230;]'
      date: '2016-04-02 11:48:09'
      date_gmt: '2016-04-02 01:48:09'
      id: '3331'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The following is an attempt to think about the inter-connections between [the paper "Open Educational Resources (OERs) for TPACK Development"](https://www.academicexperts.org/conf/site/2016/papers/49080/) presented by Mark Hofer and Judi Harris at SITE'2016 and [the Moodle OpenBook project](/blog/the-moodle-open-book-module-project/) and my own teaching.

First, is a description of what the open courses they've developed and what the students do. Second, is some early thinking of how this might link to EDC3100 and the Moodle open book project.

## Learning Activity Types as OER/open courses

The paper offers a rationale and description of the development of [two short, open courses](http://activitytypes.wm.edu/shortcourse/) designed to help primary and secondary pre-service teachers use [learning activity types](http://activitytypes.wm.edu/) (LATs) to develop their TPACK.

Hofer and Harris (2016) describe them this way

The asynchronous, online “short courses” for preservice teachers that we have created are divided into eight brief, sequential modules...Each module begins with an overview and learning goal for the segment, and is presented as video-based content that includes narrated slides, interviews with practicing teachers, imagery, and additional online resources. Each of the videos ranges from 2-8 minutes in length, and includes verbatim closed captioning.

In completing the courses the students

- Reflect on examples of ICT and pedagogy they've previously seen.
- Select three lesson plans from a curated collection of plans from pre-service teachers.
- Analyse those lesson plans: objectives, standards, types of learning activities, how learning is assessed, and the use of digital technologies.
- Practice replacing one ill-fitting activity types from another sample lesson with other types of activity type that better fit the learning goal.
- Consider substituting different technologies in the sample plan and discuss reasoning.
- Review portions of interviews with an experience teacher.
- Use selected plans from before to choose a LAT taxonomy and explore that taxonomy.
- Think about replacing activity types and technolgoies and discuss.
- Create their own lesson plan.
- Subject their lesson plan to two self-tests called "Is it worth it?"

Hofer and Harris (2016)

We consciously erred on the side of the materials being perhaps too prescriptive and detailed for more experienced and/or advanced learners, since we suspected that it would be easier for other users to remove some of the content than to have to create additional supports.

### Moodle open book and my course

In EDC3100 we cover similar ground and the content of these short courses could be a good fit. However, the model used in the course is a little different in terms of implementation. The short course content would need to be modified a bit. Something thought of by the Hofer and Harris (2016)

This is why we have released the courses in a modularized (easier-to-modify) format, along with an invitation to mix, remix, and otherwise customize the materials according to the needs of different groups of teacher-learners and the instructional preferences of their professors. The Creative Commons BY-SA license under which these short courses were released stipulates only that the original authors (and later contributors) are attributed in all succeeding derivatives of the work, and that those derivatives are released under the same BY-SA license

My course is implemented within Moodle. It uses the Moodle book module to host the content. The [Moodle open book project](/blog/the-moodle-open-book-module-project/) has connected the Moodle book module with [Github](https://github.com/). The aim being to make it easier to release content in the Moodle book out to broader audiences. To enable the sharing and reuse of OERs, just like these courses.

While the technical side of the project is basically finished (it could use some more polishing before official release) there's a large gulf between having a tool that shared Moodle book content via github and actually using it to share and reuse OERs, especially OERs that are actually used in more than one context. The LAT short courses appear to provide a perfect test bed for this.

Hofer and Harris (2016)

For teacher educators who would like to try the course “as is,” we have developed the content as a series of modules within the BlackBoard learning management system and have exported it as a content package file which can be imported into a variety of other systems. With either no changes or minor edits, the short courses in their current forms can be used within existing educational technology and teaching methods courses.

I'm assuming that the content package file will be able to be imported into Moodle, and perhaps even into the Book module.  It would be interesting to explore how well that process works and how immediately usable I (and others) think the content might be in EDC3100.

If I then make changes in response to the context and share them via the Moodle open book and Github, it would be interesting to see how useful/usable those changes and Github are to others. In particular, how useful/usable the Github version would be in comparison to the the LMS content package and the current "Weebly" versions of the courses.

I suspect that while Github provides enhanced functionality for version control (Weebly offers none), I'm not convinced that teacher educators will find that functionality accessible both in terms of technical knowledge, existing processes and practices around web content, and perhaps due to the contextual changes made.  Also, while GitHub handles multiple versions very well, the Moodle open book doesn't yet support this well.

Putting the LAT courses into the Moodle open book seems to provide the following advantages:

1. Provides a real test for the Moodle open book that will reveal its shortcomings.
2. Provide a useful resource (optional for now) for EDC3100 students and also potentially for related courses I'll need to develop in the future.
3. Enable the community around LATs and the short courses experiment with a slightly different format.

I think I've convinced myself to try this out with the secondary LAT course as an initial test case. Just have to find the time to do it.