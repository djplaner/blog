---
title: "Implementing a course barometer in Moodle: A kludge"
date: 2012-03-05 10:49:12+10:00
categories: ['edc3100', 'moodle', 'teaching']
type: post
template: blog-post.html
---
It's the start of the second week of the course I'm teaching. I'm directly responsible for 60 odd on-campus students and 130 or so online/distance students. That split reminds me a lot of my teaching at [CQU](http://www.cqu.edu.au/) in the mid-1990s. The deja vu continues in terms of getting a feel for how the students are going, how are they responding to the course, its model and content? Back at CQU the solution was inspired by [course barometer idea](/blog2/student-feedback-anonymity-observable-change-and-course-barometers/) from some University folk in Sweeden.

The original course barometer was a purpose-built application in Webfuse, an "LMS" used at CQU from 1996 through 2009. This post records an initial attempt to recreate something simliar using standard Moodle 1.9 modules.

### What?

The barometer is meant to be a simple form that allows the students to

- Indicate whether how they are feeling about the course at the moment: good, bad, or indifferent.
- Provide some free-text comments to supplement the feeling.

Preferably this is done anonymously - [previous research](/blog2/student-feedback-anonymity-observable-change-and-course-barometers/) has shown that anonymity isn't as important as doing something with the feedback - and would allow us to break up the students by campus/mode of study.

Some form of report should be generated to allow teaching staff to analyse student responses. One the nice list is a method for staff to respond.

### How?

Thanks to @markdrechsler and @mguhlin the Moodle tool possibilities (with links to Moodle 2.2 docs) are :

- [Choice](http://docs.moodle.org/22/en/Choice_module),  
    Appears that the choice module is limited to MCQs, but I do want the free text response.
- [Feedback](http://docs.moodle.org/22/en/Feedback_module),  
    Looks like this could be the one.
- [Questionnaire](http://docs.moodle.org/22/en/Questionnaire_module) (though apparently deprecated), and  
    Doesn't appear to be included in the [USQ](http://www.usq.edu.au/) Moodle instance.
- my original idea Quiz.  
    As Mark suggested, having the concept of a "right" answer built into the quiz means it's not great for the purpose of a barometer.

### Place with feedback

Time to get familiar with what the [Feedback module](http://docs.moodle.org/22/en/Feedback_module) can do. Add a new Feedback activity and the form provides (which seem the same as [those documented here](http://docs.moodle.org/22/en/Feedback_settings))

- Name and description.
- Timed release of the activity.
- An anonymous option - FTW.
- Allow the students to see the analysis.  
    There are two sides to this. Yes is good, allows students to get a sense for how others are going. No it is bad, because of the possibility of "bad" responses. I'll go with yes.
- Email notification of submissions.  
    Will turn this one, will help mitigate the risk of "bad" responses.
- Multiple submit - no.
- It does allow separate groups.  
    Wondering if this will provide the separation of students into the different modes.

Creating it's a fairly simple process. Add the questions. Create a template (allow use of these same questions in other feedback activities). Away we go.

I do wonder if USQ automatically create student groups based on mode of study? And yes they do. And the Feedback module allows separation of students into groups.

### Done

Fairly simple to set up and even before I'd formally announced it, one student has submitted their first bit of feedback.