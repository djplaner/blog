---
categories:
- bad
- edc3100
- teaching
date: 2014-06-14 10:39:46+10:00
next:
  text: Designing a course on "Networked and Global Learning" - scope, thoughts and
    call for suggestions
  url: /blog/2014/07/07/designing-a-course-on-networked-and-global-learning-scope-thoughts-and-call-for-suggestions/
previous:
  text: Making BIM ready for Moodle 2.6
  url: /blog/2014/05/19/making-bim-ready-for-moodle-2-6/
title: Tracking task corruption with Moodle activity completion
type: post
template: blog-post.html
---
The following documents a quick kludge required for the assessment for a course I teach. It's primarily a document to help me think through the task and document what was done and why.

### Background

A small percentage of the overall mark in this course is generated by completing a weekly list of activities on the course site. Each student's completion of of these activities is tracked using Moodle's activity completion feature.

The activities are (in theory) designed to enhance student learning and are aligned with the other course assessment. Obviously they are so well designed and the students so well motivated that they complete the tasks as intended - of course not. There is growing evidence of [task corruption](/blog/2009/03/04/task-corruption-in-teaching-university-negative-impact-of-place/#corruption) and in particular of simulation.

In response, I should be exploring why this is the case and modifying the course, but that will have to wait until later. Right now with the looming end of semester I've decided I need to ensure that those engaging in simulation are not rewarded for completion. My rationalisation for doing this is to provide some little reward for those students who engage with the tasks.

### Design

Moodle activity completion is one way (apparently). Once a student completes the activity it is recorded in the database and displayed to the student and the staff. There doesn't appear to be anyway to change the status of this activity completion to "not finished". Essentially a reset button.

The marking for this aspect of the assessment is done via a perl script. That script draws on the fact that I have a local version of Moodle into which I'm importing the activity completion data from the institutional system. The plan here is to modify the marking script so that it draws on data of the form "student X did not complete activity Y" when calculating the mark of individual students.

I don't want to modify the Moodle database structure. Even though it's a local copy this is probably too much effort for this type of kludge. So it appears the easiest approach is to create a new data structure in the script of the form

\[code lang="perl"\] my %simulation = ( "studentX" => ( "Checking your understanding of some models, frameworks...." => 1 ), "studentY" => ( "Share your posts on the Connect.ed resources" => 1, "Share what you already know about lesson planning" => 1 ) ); \[/code\]

A hash keyed on student ID which points to a hash keyed on activity names.

As the script is calculating the mark for each student it will check this hash for entries for the student and modify the mark accordingly.

### Implementation

**Will those keys work?**

The student ID will work, though there will be some manual work identifying it for each student. The question is whether the activity name can be used as an ID. Is it stored in the local database?

Activity completion is kept in mdl\_course\_modules\_completion. It doesn't store the activity name. Do I store it elsewhere? Nope, not storing that information.

Is there a table for it? For the life of me (or at least this early on a Saturday morning) I can't find where this information should be stored in the Moodle tables.

The import script I use can easily insert data into a table linking the activity id with the activity name. But for the immediate kludge dumping a Perl data structure might do. In fact there's a variable already to dump.

Now what about the students and the activities they've simulated? What I currently have is their name and the name of any simulated activities. The student ID being used is Moodle user id. Only a half-dozen students, so some manual SQL will do, implementing the above idea

\[code lang="perl"\] my $SIMULATION = { 283 => { "Share your posts on the Connect.ed resources" => 1, "Share what you already know about lesson planning" => 1 }, 149 => { "Checking your understanding of some models, frameworks…." => 1 } }; \[/code\]

**Re-calculating mark**

The completion data is taken from the database via a class. That same class generates a PERCENT completion figure for each student. That seems a sensible place to stick the code to re-calculate the mark. Use case something like

\[code lang="perl"\] $completion->reCalculate( %activityMapping, $SIMULATION ); \[/code\]

The hash from above is passed into recalculate which then (surprise, surprise) recalculates the grades. This way I don't have to modify any of the script code. Good plan.

Of course, the module is actually getting SQL to do the calculation rather than Perl. So this implies a rewriting of the module to

- Get all rows of completion data for the BIM activity.
- Have Perl generate an array for each user with the number they've completed based on START/STOP, actual completion and the data in SIMULATION.

All that's done and seems to be working

**Modifying the report**

With the data changed, now need to update the report to include mention of this simulation. The function calculateLearningPath seems the best bet.

All done.