---
title: Moodle, outcomes, metadata and curriculum mapping
date: 2010-03-10 10:21:33+10:00
categories: ['curriculummapping-cddu']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: First step in &#8220;Moodle curriculum mapping&#8221; &laquo; The Weblog
        of (a) David Jones
      author_email: null
      author_ip: 72.233.96.138
      author_url: https://djon.es/blog/2010/03/23/first-step-in-moodle-curriculum-mapping/
      content: '[...] outlined in a previous post it appears that Moodle (the institutional
        LMS at my current institution) already has functions that [...]'
      date: '2010-03-23 14:13:34'
      date_gmt: '2010-03-23 04:13:34'
      id: '2957'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
This summarises some [continued investigation](/blog2/2010/03/09/outcomes-and-moodle/) of Moodle support for outcomes as part of preparing for the [curriculum mapping project](/blog2/research/curriculum-mapping/).

Current summary of what I think I've learned is that Moodle 2.0 will have significant support for progress tracking, which involves connecting student progress with outcomes etc. This draws on very similar "infrastructure" as would be required by curriculum mapping. Curriculum mapping, however, requires different "reporting" mechanisms. It appears a fruitful marriage may be possible. Need to learn more.

### Moodle resources

Moodle resources talking about these topics

- [Thread on outcomes/competencies/goals/metadata](http://moodle.org/mod/forum/discuss.php?d=63577)  
    Mostly from 2007. Ideas of collaboration with Sakai, various modules that are meant to do aspects of this as well as some of the original discussion with the origins of the outcomes stuff.
    
    Seems the technical solution to this is the application of metadata to activities/resources etc.
    
- [Goal management tools for Sakai](http://confluence.sakaiproject.org/display/GM/Goal+Management+Tools)  
    Mentioned in the last thread. A sakai tool that does aspects of this.
- [Outcomes in 1.9](http://moodle.org/mod/forum/discuss.php?d=78074)  
    General discussion early in the availability of outcomes in version 1.9.
- [Site wide & course outcomes](http://moodle.org/mod/forum/discuss.php?d=125957)  
    Single post from June 2009 outlining a problem not being able to see the site-wide outcomes a student has completed.
    
    Based on my very limited knowledge, this would require a report to be written and included in the right place?
    
- [Unsolved issue about long lists of outcomes becoming unmanageable?](http://tracker.moodle.org/browse/MDL-18919)
- [Progress tracking feature for Moodle 2.0](http://docs.moodle.org/en/Development:Progress_tracking) - planning docs. Much more on this below.
- The [tables](http://docs.moodle.org/en/Development:Grades#grade_outcomes) used for grade outcomes.
- [Moodle and assessment thread](http://moodle.org/mod/forum/discuss.php?d=62979)  
    Talks about the [Blackboard outcomes system](http://www.blackboard.com/Teaching-Learning/Learn-Capabilities/Outcomes-Assessment.aspx) and has some mentions of similar projects. As always thought, the Blackboard system could be useful to learn some lessons from. Would be interesting to talk to organisations, and the people within, that have been using it seriously.

### Some reflections on pedagogy and Moodle

Found [this page on pedagogy](http://docs.moodle.org/en/Pedagogy) on the Moodle site. One of the simplest descriptions of the [Moodle model](http://docs.moodle.org/en/Pedagogy#Moodle_in_three_short_paragraphs) I've seen so far - Moodle has courses which contain activities and resources.

Suggests the power of Moodle is sequencing activities, of learning paths. This raises some interesting questions about the suitability (from a pedagogical perspective) of a "course template" that has been created locally. The template makes a course look more like a traditional website divided into sections - resources, assessment etc. i.e. it would appear to break the idea of "paths"

The [Social constructionism as a referent](http://docs.moodle.org/en/Pedagogy#Social_Constructionism_as_a_Referent) outlines 5 points used to describe the connection with social constructionism and Moodle. Some of these can be made to link nicely with some of the ideas around the curriculum mapping project. Here's a first attempt

- All of us are potential teachers as well as learners - in a true collaborative environment we are both.  
    In terms of teaching staff being aware of what is going on in other courses, Moodle isn't a collaborative environment. At least in terms of how it is implemented in most institutions. The idea from the curriculum mapping project to use the outcomes, graduate attributes etc to allow teaching staff to navigate into other courses and see examples of how they met them could help provide this.
    
    It could also go further, from one perspective curriculum designers have to help some academics prepare the curriculum map. i.e. the designer is the teacher of curriculum mapping, the teacher is the student. In some cases, the curriculum designer can do it for the student. Reducing learning. Having something more under the control of the learner than the teacher might help address this.
    
- We learn particularly well from the act of creating or expressing something for others to see.  
    Links to the previous point, but also at a more fundamental level is that most teaching staff don't think/see the connections between attributes, outcomes etc and the activities/resources in their course. Using the curriculum mapping project information to modify the interface to show them this connection (or its absence) and generate it as part of what they are doing, could be a good thing.
- We learn a lot by just observing the activity of our peers.  
    This links back to the idea above as well.
- By understanding the contexts of others, we can teach in a more transformational way (constructivism)  
    Curriculum mapping, as I've seen it practiced, is often divorced from the context of teaching. It's done with a tool that is not part of the teaching process, often done at a time divorced from the act of teaching and generally doesn't fit well within the context in which teaching occurs. The point of this project is to get curriculum mapping happening within the context of teaching, not apart from it.
- A learning environment needs to be flexible and adaptable, so that it can quickly respond to the needs of the participants within it.  
    This point has interesting implications for the notion of constructive alignment - or at least one form of how it is practiced - that is embedded in some practice of curriculum mapping.

It also [mentions the importance of about metadata and outcome statements](http://docs.moodle.org/en/Pedagogy#Metadata_and_outcome_statements) which are becoming more important in Moodle 2.0. This is where the curriculum mapping stuff links in. More and more it appears that the project will be more about building useful blocks/activities/reports on top of this infrastructure. Something which is talked more about in the [progress tracking](http://docs.moodle.org/en/Development:Progress_tracking) development docs.

### Progress tracking

The [progress tracking development doc](http://docs.moodle.org/en/Development:Progress_tracking) talks about planning/work on incorporating this into Moodle 2.0. It links to IMS standards on [definition of competency or educational objective specification](http://www.imsglobal.org/competencies/index.html) and [learning information](http://www.imsglobal.org/profiles/index.html).

Progress tracking seems to have a different focus than curriculum mapping. Tracking focuses on the progress of the student. It does need the same sort of information about competencies, but uses it for a different purpose.