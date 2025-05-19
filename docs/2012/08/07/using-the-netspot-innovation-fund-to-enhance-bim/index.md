---
categories:
- bim
date: 2012-08-07 09:23:47+10:00
next:
  text: Lessons for the meta-level of networked learning?
  url: /blog/2012/08/13/lessons-for-the-meta-level-of-networked-learning/
previous:
  text: 'Enabling academics to apply learning analytics to individual pedagogical
    practice: how and with what impacts?'
  url: /blog/2012/07/25/enabling-academics-to-apply-learning-analytics-to-individual-pedagogical-practice-how-and-with-what-impacts/
title: Using the NetSpot Innovation fund to enhance bim
type: post
template: blog-post.html
---
So the [2013 NetSpot Innovation Fund](http://netspot.com.au/innovationfund.html#Register12interest) has been announced. You can read more on that prior link but my summary is that NetSpot will contribute their human resources (with significant expertise around Moodle development, QA etc.) to improving an existing innovation with the aim of making it more sustainable. In the words of the [guidelines](http://netspot.com.au/NetSpot%20Innovation%20Fund%20Guidelines%202013.pdf)

> it is essentially a software development project

It sounds like a perfect opportunity to enhance [BIM](/blog/research/bam-blog-aggregation-management/) - Blog Aggregation Management Into Moodle - plugin. The following provides soem ideas for what shape that expansion/enhancement might take and serves the purpose of seeing if there's broader buy in for some of this work and also make suggestions that I've missed.

If you are interested in this, let me know.

### The foundation

The assumption here is that I have finished porting BIM into Moodle 2.x. This would form the starting point for any work the NetSpot folk might do. From this foundation, I can see two broad categories of work

1. The enhancements.  
    These improve or expand the functionality of BIM but keep it within the fairly traditional paradigm of a teacher led/managed process for assessment purposes.
2. The expansion.  
    Intended to move serve as a basis for an exploration of different - more "networked/connectivism" type - paradigms.

Yes, I'm aware that there could be significant questions about how you could explore different paradigms within the constraints of an institutional LMS. There are inherent constraints.

[Leigh Blackall](http://www.leighblackall.com/) and I [had this conversation a while ago](/blog/2010/04/25/inside-out-outside-in-or-both/). There are minuses in this approach, but there are some plusses as well and there aren't many opportunities of getting access to some experienced developers the other way.

### The enhancements

- A general QA check and associated improvements.  
    My initial port to Moodle 2.x will have flaws. Having the NetSpot crew double check this and make improvements where possible makes it more likely for institutions to feel safe adopting BIM.
- Interface enhancements.  
    This could be as simple as adding support for the more advanced types of tables that Moodle supports. mainly to improve handling large lists of students details.
- Copy ("plagiarism") detection.  
    There are some issues around this, but I know that there are folk in large classes for whom the ability to run copy detection over blog posts would be a plus.
- The question of "multiple activities" ?  
    When you create a BIM activity at the moment, you can have multiple posts that the students need to complete. The one link to this activity occurs once in the Moodle course design. Which can cause some issues in courses where the teaching staff want to remind students of what they should be doing this week. Someway to have multiple links to the activity, or group together multiple BIM activities into one management interface seems to be needed.
- Activity completion.  
    This follows on from the above. Linking BIM with the new activity completion features in Moodle could be useful.
- Private posts?  
    I'm still somewhat uncertain about this one. But there are an increasing number of Allied Health folk asking students to keep journals while on prac. And BIM's a good fit. But they want the information restricted. So, why not use a Moodle blog? Some way to support the aggregation of private blog posts might be useful.
- Support for groupings.  
    As per [this request](https://github.com/djplaner/BIM/issues/20)
- And addressing [other known issues](https://github.com/djplaner/BIM/issues) for BIM
- A complete collection of unit tests etc.  
    Perhaps improving sustainability could be enhanced by having a complete collection of testing for BIM. So that changes could be made more quickly and with greater confidence.
- Enable students to allocate posts.  
    A BIM activity generally as a sequence of writing prompts/questions that students are meant to respond to on their blog. BIM will attempt to automatically associate a student post with the particular prompt/question. It also allows staff members to associate manually. Allowing students to allocate posts **and** allowing them to allocate multiple posts to a particular prompt/question would allow approaches where students are gathering or providing evidence against a particular standard, KPI etc.
- Mirroring of embedded media.  
    One of the perceived advantages of BIM is that it keeps a copy of what the student posts on a university server. Assuaging fears about losing data but at the same time allowing the student to have their own space. However, it only keeps a copy of what is in the feed, which in terms of blog posts is just the text. Any embedded media is not copied onto the institutional server, hence more fears about losing data. Though this does tend to rise the issue of resource consumption.
- Closer examination of BIM functionality and Moodle core.  
    Theoretically, Moodle 2.x allows the integration of an external blog for users. There's some apparent overlap there. At the moment, I don't believe it goes anywhere near serving the same purpose or the same functionality. But a closer examination and discussion of this with people who know - especially with any future plans for the Moodle core - could be useful.

### The expansion

This is where my own interests lay and I need to think more about these as I'm still too stuck in the traditional education mindset.

The following are leaning more to adding features to support more connectivist/social constructivist pedagogies

- Significant improvements to the feed forward functionality in BIM.  
    At the moment, it's pretty much limited to an OPML file that lists all the feeds for students allocated to a staff member. There's a lot more scope here, some possibilities
    - Aggregated RSS feeds, rather than OPML, where aggregation is very flexible and configurable: e.g. aggregate all posts that have been given a certain mark, that are responses to a certain question, from certain students or groups of students, posted within certain date ranges.
    - Modifying the posts before aggregation.  
        Rather than aggregating exact copies of the blog posts there might be some plusses in modifying the posts. e.g. anonymising the source.
- Tracking and distribution of comments some how.  
    As students are encouraged to comment on other blog posts (on the actual blogs) the ability to track or mirror those within BIM, perhaps to support some form of marking.
- Allows student comments on posts within BIM.  
    
- Self and peer assessment.  
    Starting to tread on the toes of other systems, but allowing students and their peers evaluate each others work has some value and would build on some of the earlier features.
- Allow student creation of prompts/questions.  
    Rather than have the prompts set by teaching staff, allow
- Construction of learning paths/concept maps from aggregated posts.  
    This is moving beyond BIM, I think. But the idea that any user could construct a visual representation of a collection of posts (including some derived from other sources e.g. diigo feeds etc) encapsulating their view of a particular topic. A visual representation that could be used by others.

The following are some ideas intended to explore how e-learning systems can be improved by embedding more explicit cognitive support for the designer (i.e. teaching academic) into the system. These are probably really starting to get outside the scope of the NetSpot innovation fund - at least in the short term - but a solid BIM being widely used might help spread this type of work.

- SNAPP-like visualisations.  
    [SNAPP](http://research.uow.edu.au/learningnetworks/seeing/snapp/index.html) produces network visualisations of interactions in LMS discussion forums. A similar feature in BIM might be useful and could be used by teaching staff (or students themselves) to understand what is going on and take action.
- Analytics?  
    Which leads to the broader consideration of how to gather and display useful analytics and visualisations of what's going on in a BIM activity.
Embedded galleries of BIM use.  
A method by which uses of BIM can be shared between all users of BIM and that is embedded within BIM itself.- A "game-like" introduction interface.  
    Not gamification itself (that will get a mention later) but rather something [more like I talked about here](/blog/2011/09/23/can-e-learning-tools-be-more-like-plants-vs-zombies/). Designing a good BIM activity is hard. The current interface doesn't really help. Large-scale computer games are hard. But you can often get going in the game without referring to a manual. Can we design something for BIM that gives the same sort of learning experience for staff (and students?).
- Badges.  
    There are some minuses with this idea. But integrating BIM with a badging infrastructure (e.g. [Mozilla's Open Badges](http://openbadges.org/en-US/)) might open up some space for interesting experiments.
- Pedagogical "skins".  
    In it's default state, the BIM interface is mostly focused on tool configuration. It doesn't really embed a great deal of pedagogical support. The academic using BIM has to translate their pedagogical aims into configuration options in BIM. This is difficult. A pedagogical "skin" could act as a re-imagining of the BIM interface to offer direct scaffolds for a particular pedagogical view.