---
title: Planning changes to EDC3100 assignment 1
date: 2016-07-13 13:19:24+10:00
categories: ['bad', 'edc3100']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

In the first half of the year there was [a new assignment](/blog2/2016/03/10/setting-up-an-excel-checklist/) in EDC3100 designed to both enhance student learning, but also experiment with making the data produced by students and markers as part of the assessment process more accessible for manipulation by software. i.e. the students and markers entered data into a spreadsheet.

It's a new semester, time to reflect on that initial use and see what changes should and can be made.

## Student results

Let's start with student results. (Note: this is all a bit rough and ready)

Overall the average mark for the assignment was 13.8 (72%) out of 19 with a standard deviation of around 3.  But that's for both parts of the assignment.

Given current practice of using Word documents as assignment cover sheets, extracting out the specific marks for the checklist/spreadsheet assignment is difficult. But I have an Excel spreadsheet and I can run a script to get that data.

The average mark is about 9.5 (68%) out of 14, with a standard deviation around 2.

Let's dig a bit deeper into the three criteria that made up that mark. The three criteria were

1. Mark - students use a checklist to evaluate a lesson plan and its use of ICT and pedagogy.
2. Acceptable use - focused on students ability to identify a lesson plan they can use wrt copyright.
3. RAT - students use the RAT model to evaluate the use of ICT and pedagogy in the course

The following table compares cohort performance on the criteria and overall.

| Criteria | Average % | stdev % |
| --- | --- | --- |
| Overall | 68 | 15.8 |
| Mark | 75.2 | 17.2 |
| Acceptable Use | 63.2 | 16.7 |
| RAT | 59.3 | 17.8 |

The RAT question was where the students were least successful.  It's also (arguably) the more difficult question. The checklist was the highest mark.  Acceptable use is also quite low and needs some work.

Those last two is where the focus will go for now.

## Other thoughts and experiences

### Student feedback

Student feedback included the following comments related to the assignment

Some of the items we were required to assess in Assignment One could have been better explained

more guidance was required for Assignment 1. I didn't like the use of the Excel document

 The last point was connected to the issue of not being able to justify the interpretation, which links back to points raised elsewhere. The first point is one to ponder. The results above suggest that's not where the real need lays.

### Marker feedback

Feedback from markers included

- Identifying use of an IWB, when in fact it's just being used as a data projector.
- Little understanding of what constitutes: an _authentic problem_, and _connections beyond the classroom_
- Some surprise that even with 50 assignments to mark, there were few double ups of lesson plans.
- Another liked the format in that it gave students a better handle on what to look for in an ICT-rich lesson and the RAT model was useful for framing an evaluation.
- The wording and nature of the statements for the acceptable use and the RAT question need to be clarified - to confusing (for marker and student)

One aspect of the assignment that troubled one of the markers was that the lesson chosen by the student only had to include some form of ICT.  It didn't need to be rich nor effective ICT. This was actually one of the aims of the assignment, to allow students develop some appreciation for the breadth of what is possible and just how narrow use often is.

### Questions asked during semester

- Struggles to find a CC-licensed lesson plan.
- Clarity about what makes an acceptable lesson plan
    - e.g. Can an American lesson be used?
    - Linked to concerns about Q10 and distinguishing between an appropriate lesson plan and whether or not you can use it due to copyright
- Questions re: term of use and uploading
- What if I can't find any information about copyright?
- How can/should the lesson plan be put online?
- The distinction between what a student is using an ICT, and when the teacher is using it
- Explanation of how the checklist questions are marked - e.g. those that don't apply
- Reporting bugs in the formatting of the cells

### Personal thoughts

[Early reflections](/blog2/2016/05/30/early-thoughts-on-s1-2016-offering-of-edc3100/) on the semester included

The spreadsheet worked reasonably well. The checklist within the spreadsheet requires some refinement. As does some aspects of the rubric. The duplication of a Word-based coversheet needs to be removed.

 Other thoughts during the semester included:

- Students had a tendency to treat the free text questions as requiring an essay.
- The "pretend" context for the task wasn't clear enough.
- In particular, a problem about the exact legal status of ACME's server, links and making copies of files.
- Issues with specific questions and the checklist
    - The "web applications" option under "What is used" causing confusion about overlap with "web browser" question
    - Q16 includes mention of print material around ICT
    - Q26 mentions _embedded hardware_, a question of it and the connection with IWB
    - Appears to be strong connections between Q22 and A46
    - The purpose of Q10 is not clear enough, confusion with matching curriculum etc.
    - A feeling that there are too many questions and perhaps overlap
    - Criteria for RAT question isn't clear enough about the quality of the response
        - e.g. not mentioning all uses of ICT and Pedagogy
        - Missing out on themes
        - Incorrect identifying something as belonging to a theme
    - Suggestion for a drop down box around linkage of ICT to objectives: not related, somewhat related, essential, extends, transforms
- More explicit scaffolding/basic activities around the evaluation questions
    - e.g. Is ICT being used to Question, Scaffold, Lecture, in an authentic task

## Random suggestions

Due to institutional constraints (not to mention time) none of the changes to be made can be radical.  Keeping with that, some initial suggested changes to explore include:

1. Pre-submission checks
    1. What pre-submission checks should I run?
    2. Can they be run? How does that integrate with the Moodle assignment activity workflow?
2. Remove the cover sheet entirely, just use the spreadsheet
    1. Need to include the learning journal mark into the spreadsheet
    2. Would be nice to do this automagically
3. Tweaking the marking
    1. The criteria for Acceptable use and RAT questions need to be improved
    2. Look closely at each of the points about the questions
4. Student preparation
    1. Make clear the need not to write essays for the free text questions
    2. Finding CC licensed lesson plans
        1. Great difficulty in finding those that are CC licensed
        2. Provide a list of prior sites people have used
        3. Generate some sort of activity to test understanding of CC with a specific example
    3. RAT Model
        1. More activities in learning paths
        2. Better labeling on  the spreadsheet
    4. More questions/activities around specific terms and concepts within the checklist