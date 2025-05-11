---
categories:
- edc3100
date: 2014-07-31 11:06:15+10:00
next:
  text: Emergence, improvisation and course design
  url: /blog2/2014/07/31/emergence-improvisation-and-course-design/
previous:
  text: A bit more exploration of identity
  url: /blog2/2014/07/29/a-bit-more-exploration-of-identity/
title: Learning journal, activity completion and nudge analytics
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    []
    
---
Week 2 of 2nd semester. Time to start checking how students are going and checking in with those that haven't started yet. For EDC3100, this means putting in place the various "shadow systems" that bridge what's provided by the institution and what I need in order to enact the practices I deem appropriate. What follows is a record of the ongoing evolution of [this idea](/blog2/2013/06/10/the-kludge-for-marking-learning-journals/).

Extending things a bit this semester is that EDU8117 will leverage some of the same system. So it will all have to be a bit more general. Also hoping to tweak it solve some issues from last semester.

### BIM backups - bring user details in

A request for backups of the BIM activities for the two courses brings the user data in I believe. Will need to do this once more.

### Figure out which users belong to a course

I'm kludging this with Perl. So no friendly Perl APIs. A kludge with groups perhaps - that's what was used last semester. So identify the groups that apply.

mdl\_groups: \[ id, courseid, name, description etc. \] mdl\_group\_members : \[ groupid, userid...\]

Courseids for

- EDC3100 - 4 - gives the right set of groups it appears. 46 is the group I'm after for EDC3100
- EDU8117 - 5 - only 1 group 68

There is also a role for dropped students that should perhaps be checked at some stage.

Given new use of MoodleUsers->new\_all( COURSE => "EDC3100", TERM => "2014\_S2" ) and then do the translation.

That's working.

### BlogStatistics

Relies on two classes. One is hard coded to the ID for the BIM activity. Both are. So same kludge as for the MoodleUsers. A simple hash to translate COURSE/TERM into a BIM activity.

Actually Marking only needs updating to take a BIM id.

Done. It's a bit of a bugger that Webfuse is dead. Quite like the flexibility of the class system. Perfect for bricolage/tinkering.

### Importing activity completion

It's currently done with activityCompletion/import.pl

1. Reads the CSV file with Activity Completion data,
    
    Biggest kludge here is the student ID number which is missing leading 00s.
    
2. Arbritarily creates a base course module ID for each activity starting from a common, hard-coded base.
3. Compares that data with the Moodle user data to get a match up, Currently done on USQ student number (ID).
4. Inserts the course completion data for each user into mdl\_course\_modules\_completion : \[ id, coursemoduleid, userid, completionstate, viewed, timemodified \]
    
    Currently does this by deleting all the data in mdl\_course\_modules\_completion - perhaps overkill.
    
    \[code lang="perl"\] foreach $student ( @enrolled ) { foreach $activity ( @csv\_activity\_records ) { # create a database record for course\_modules\_completion that activity push @rows, $activity } # insert into database } \[/code\]

Got that all fixed up. Finally.

### Identify the students slow getting going

Next step is to identify those students who have been a bit slow getting going.

Each week has a "learning path" of activities to complete. The idea is that given any particular week it would be useful to identify those students who are "slow".

Perhaps something like

1. Class that takes the course code, term and the week of term.
2. Generates a CSV file with student details (email address, name) and the percentage of activities that have been completed up until this week.
3. This can be manipulated with Excel and emails sent as a result.

Raising questions

- How to know which activities apply to which week?
    
    Current approach is to hard code the start and end pretend CMIDs for activities for a period. Could extend this to each week. ActivityCompletion class does something like this based on START/END for hard coded CMIDs.
    
    Convert this class to use COURSE PERIOD WEEK instead.
    

Done. And first email sent to students who have yet to complete 50% of the tasks from last week. A very primitive nudge.

Will need to send out a reminder about registering blogs so I can send out a learning journal report.