---
title: BIM - Manage Marking
date: 2010-01-17 10:25:40+10:00
categories: ['bim']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: BIM &#8211; manage marking &#8211; view and release &laquo; The Weblog of
        (a) David Jones
      author_email: null
      author_ip: 76.74.255.67
      author_url: https://djon.es/blog/2010/01/17/bim-manage-marking-view-and-release/
      content: '[...] The Weblog of (a) David Jones Another voice in the blogosphere    &laquo;
        BIM &#8211; Manage&nbsp;Marking [...]'
      date: '2010-01-17 22:20:38'
      date_gmt: '2010-01-17 12:20:38'
      id: '2914'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
We come to the main last collection of functionality required of BIM to be operation (a major tidy up is needed after this, but it's getting there). That last collection is currently going under the label "Manage Marking". It covers the functionality required by the teacher in charge of a course to manage the marking being done by other staff, this includes the following tasks:

- Track the marking progress of other staff.
- Be able to quickly find and view the progress, marks and comments associated with a particular student (i.e. when they complain to the marker).
- Eventually this might include some sort of advice/suggestions around what is going wrong for the student (mostly around their feed and its subscription).
- The ability to manage the release of marks and comments.  
    By default, a marker can only mark a student post. In this state, the student cannot see the mark or comments. The coordinator is meant to moderate the mark/comments and then, when ready, release them.

Additional discussion of this collection of functionality was [in an earlier post](/blog2/2010/01/09/bim-design-of-manage-marking-and-other-features-for-coordinators/)

This post is an attempt to boil that basic overview into some more detailed plans for the implementation of this functionality and possibly discussion of how it has been implemented.

### Implementation plan

Aim to have the more comment task on the first page, immediately accessible, including:

- Button/link to release all current marked posts.
- Button/link to view all current marked posts.
- List of markers/groups and the stats on their progress
- The stats should probably include a list of all questions for this BIM activity. For each column have a link to release all marked posts for those questions and also for those markers.
- Each of the "stats" in the table should be a link to drill down the details of just those students that fit the stats.  
    In turn, on this "drill down" page, have the links to release all marked posts of various types, including checkboxes to select individual students.
- Search box to enter part of student username or name and see details about them.

This requires two fairly general methods/screens to:

1. Release results; (**op=release**)and  
    The idea here is that given a subset of student posts (represented in someway) that are currently in the Marked state, they need to modified into the Released state. Based on current designs the methods will be
    - Release all marked posts - **no parameters**
    - Release all posts for a given week (regardless of marker) - **question=$qid**
    - Release all posts for a marker (regardless of question) - **marker=$qid**
    - Release all posts for a marker for a given week - **marker=$qid&question=$qid**
2. Display lists of students (**op=view**).  
    Going to be 3 different parameters: marker, question and status. Use similar structure to release in implementation. i.e. construct SQL based on parameters passed in and then display them.

### Implementation questions

- Need to consider how the gradebook generates its [look and feel](http://docs.moodle.org/en/Image:gradebook_normal_mode.png) and see if I can borrow useful stuff.

### Required data

Data required to implement this initial screen includes:

- List of all markers associated with the BIM.
- Details of the markers.
- List of all students associated with those markers.
- Statistics for those students for each marker.
- Probably a list of all the questions for the bim.

### Get the data

#### List of all questions

Re-use the bim\_get\_question\_hash

#### Markers and students

bim\_get\_markers\_students - gets all student details for a given marker in the course. Now just have to find out who all the markers are? I wonder if this is getting into the realm of capabilities, roles and other complications. And perhaps start to have questions connected with the [gradebook/grades module](http://docs.moodle.org/en/Grades)

Ok, this looks like it will be done via groups and may involve some local CQU customisation which I need to discover. In the meantime, I'll stick with writing functions that will essentially work, but initially use some kludgey database tables I've added for this purpose. This will be one of the big things to discover.

So, add function `bim_get_all_markers_students`. It will get all the markers, then call bim\_get\_markers\_students.

At this stage, we will need:

- \# Submitted, # Marked, etc for each marker (i.e. all their students).  
    Most of these figures can be taken straight from bim\_marking, but won't have details about those who haven't been marked. Will need to use the above function.
    
- Will also need #submitted etc per question.

Implement `bim_get_all_marker_statistics`:

- Take the markers\_students array
- Get list of all markers students ids (keys students)
- SQL statement group num students in each status by question
- Use that to populate group based array

### Show the data

Rather than a form, I think this display will just be a table of some description. Rather than buttons, use links that can be processed. Will development this in a progressive sort of way:

- Show list of markers, with overall stats.
- Show the list of questions for the unit as columns in rows for each marker.

The data is being shown. Just need to add the links to release and view and this part will be done. Do release and view in a separate post.

To do this need to:

- Show "release" link, when there is something to release for:
    - Each marker  
        Which implies I need to know the overall status stats for each marker. `bim_get_all_marker_stats` is the obvious place to do this. Add an entry `Total`
    - Each marker and question
    - Each question  
        `bim_get_question_response_stats` does this. Use that
- Show "view" link, when there are students to view for each status for each marker **DONE**

### What's been done

I'm cutting this a little short in order to get onto other things. Currently the screen is showing a table that gives a summary of marker progress. It provides links to release results (where appropriate) and to drill down to specific student details (where appropriate).

### What hasn't been done

The main thing that needs to be done is the addition of the search box for a specific student. Though that should probably be provided for the normal marker as well?

### What's next?

Time to implement the "release" and "view" operations associated with manage marking.