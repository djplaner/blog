---
categories:
- chapter-2
- elearning
- lmsevaluation
- lmsreview
- thesis
date: 2008-11-17 11:29:28+10:00
next:
  text: '"PLEs@CQUni: Origins, rationale and outcomes so far"'
  url: /blog/2008/11/17/plescquni-origins-rationale-and-outcomes-so-far-2/
previous:
  text: '&quot;Big&quot; systems - another assumption &quot;PLEs&quot; overthrow'
  url: /blog/2008/11/16/big-systems-another-assumption-ples-overthrow/
tags:
- lms
title: The dissonance gap in systems and LMS evaluations
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Evaluating an LMS by understanding the underpinning &#8220;model&#8221;
        &laquo; The Weblog of (a) David Jones
      author_email: null
      author_ip: 72.233.2.76
      author_url: https://djon.es/blog/2008/11/18/evaluating-an-lms-by-understanding-the-underpinning-model/
      content: '[...] approach is based somewhat on some previous ramblings and is based
        on the assumption that an LMS is a piece of information technology. Consequently,
        it [...]'
      date: '2008-11-18 10:32:32'
      date_gmt: '2008-11-18 00:32:32'
      id: '1885'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
Ania Lian writes in the paper [Knowledge transfer and technology in education: toward a complete learning environment](http://www.ifets.info/journals/3_3/lian.html)

> It is argued that technology itself is neither liberating, empowering nor enabling one to be with other people but that it will serve whichever goals motivate its incorporation.

In a couple of papers (e.g. [this one](/blog/publications/the-teleological-reason-why-icts-limit-choice-for-university-learners-and-learning/)) I've paraphrased this as

> Technology is not, of itself, liberating or empowering but serves the goals of those who guide its design and use (Lian, 2000).

This posts tries to explain why this is the case and also to explain what relevance this has to an institution when it attempts to evaluate and select a new learning management system.

### Why is this the case?

A learning management system is a piece of information technology. As a piece of information technology it has been designed by a [small group of expert designers](/blog/2008/11/15/expert-designer-another-assumption-ples-question/). Typically a company or open source community (individual).

This group of expert designers analyse the problem, identify some sort of solution and then turn that solution into code. They do not do this is a purely sequential nor objective manner. Their past experiences, lessons learned and new knowledge all impact on this process.

However, at some stage they must eventually design and implement algorithms, data structures and interfaces. These artifacts will all embody the view of the world they have formed during the above process. This view of the world will impact upon the final system.

For example, a system designed with an emphasis on being "enterprise ready", on being "scalable" will have a very different set of facilities, structure and "feel" than a system designed with an emphasis on a particular educational approach.

This influence of the world view of the designers is present at all levels in a system. Not just the high level perspective of the system. For example, the Peoplesoft ERP had its origins as a human resource management system. As such one of the early and important identifiers for that system was "EMPLID" i.e. employee identifier. In a HR system you have employees.

Later on Peoplesoft entered the field of providing ERPs to universities. As part of this they had to add a student records database. In part, to record things like which courses a student was enrolled in.

To achieve this you have to have some form of unique identifier for each student. Most universities do this through a unique student number. I've seen other student records system give the student number labels like STUD, STUD\_NUM etc.

Guess what label Peoplesoft uses? (Remember it's origins and the impact of the original designers). Yep, that's right. EMPLID - employee id.

### What relevance does this pose?

When a university is seeking to select a new learning management system it is selecting an enterprise information system. As such any selection will have embedded in it a certain world view. Even the notion of an LMS embodies a certain world view. That of the ["big" system](/blog/2008/11/16/big-systems-another-assumption-ples-overthrow/). This world view brings certain positives and negatives. The impact of the original designers will play a part in how effective the choice is, it will limit or enable what learning and teaching can occur, what staff and students can do.

#### Discussion forums in Blackboard

As one example, let's take the Blackboard LMS (version 6.3). Like any LMS it provides support for discussion forums. The model, or at least my current understanding of the model, is that a course website can have

- One "Course Conference" for the course.  
    A course conference can consist of many separate discussion forums. This "course course conference" is usually used for everyone in the course. For many [CQU](http://www.cqu.edu.au/) courses, this is the only course conference used.
- Each group of students/staff can have a course conference.  
    Blackboard allows you to create groups of students and staff. Each of these groups can have a single course conference. Again the single course conference can contain many different discussion forums, but they are all located in the single course conference.

So what are the limitations of this approach? Essentially, it doesn't support each group having multiple course conferences.

One of the designs by an instructional designer at CQU had each group having a part of the blackboard course site that contained a number of rooms. Sections of their group site set aside specifically for different activities, topics or times during the term. Each room might include a number of services including a discussion forum, a wiki, sharing of resources etc.

The design made sense from the perspective of keeping everything associated with a particular activity in the one place.

This could not be done with Blackboard. The discussion forums would have had to be within the single course conference allowed for each group. Taking students out of the activity into another part of the course site.

#### Assignment submission in Blackboard

The assignment submission process in Blackboard 6.3 allows students to submit any type of file, performs no checking of the files and provides only ad hoc support for marking staff.

Conseqently, it is well known that you would be really stupid to use the Blackboard assignment submission system for a class with more than about 20 students. To do so is opening you up for a huge amount of extra work.

#### Dissonance

A dissonance between the needs of a systems users and its embedded world view lead to a number of problems. The dissonance becomes a gap between the users and the system. A gap that prevents the adoption of certain approaches or which creates additional workload as people attempt to work around the gap.

Eventually, this dissonance gap will lead users to attempting to use alternate means. Of creating [shadow systems](/blog/2008/10/31/between-the-idea-and-the-reality-falls-the-shadow/).

#### Understand the gap as part of the valuation

Consequently, it seems to be sensible for any evaluation of new systems would include an attempt to actively identify the models and purpose underpinning the different systems and attempting to understand the size of the dissonance gap.

All things being equal (and there's a real good chance that they won't be), this is something we'll be attempting over the next few days as CQU attempts to move from Blackboard to either Sakai or Moodle.