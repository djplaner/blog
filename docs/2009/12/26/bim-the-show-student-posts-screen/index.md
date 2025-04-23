---
title: BIM - the show student posts screen
date: 2009-12-26 13:08:02+10:00
categories: ['bim']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: BIM &#8211; Allocate questions screen &laquo; The Weblog of (a) David Jones
      author_email: null
      author_ip: 72.233.96.166
      author_url: https://djon.es/blog/2010/01/07/bim-allocate-questions-screen/
      content: '[...] The Weblog of (a) David Jones Another voice in the blogosphere    &laquo;
        BIM &#8211; the show student posts&nbsp;screen [...]'
      date: '2010-01-08 17:18:08'
      date_gmt: '2010-01-08 07:18:08'
      id: '2908'
      parent: '0'
      type: pingback
      user_id: '0'
    
---

See also: [[blog-home | Home]]

This post describes the initial implementation of show student posts screen. IT builds on the format/process used in the [show student details screen](/blog2/2009/12/24/bim-staff-show-details-screen/).

### Required data

There should be some similarity with the show student details screen. The first three match.

- Which students the marker is responsible for.
- User details for those students.
- Student details from student feeds
- Split students into registered and unregistered.
- Student details from bim\_marking.
- List of questions for the bim.

### Implementation questions

- Main question appears to be how to call this screen.  
    Probably need an additional parameter to specify which of the operations that the teacher can call: ShowPostsDetails AllocatePosts MarkPost.
    
    Yep, that seems to work. Using `screen as the parameter. If empty, defaults to show student details.`
    
`- There's also the question of including both bimId and courseId in the view.php for bim.       Currently it is only including the course id. This means that a course can only have one BIM. A limitation.       Actually, this is an example of my limited, but hopefully growing, knowledge of Moodle. The id passed in is for the course_module table which holds information about the combination of course and activity/module. So this is not a worry.`

``   ### Get the data  The first four points from above are duplicated from the show student details screen. Easy.  List of questions - uses existing bim_get_question_hash.  Student details from bim_marking. Given a list of student ids (from $registered) get the appropriate details. Very similar to `bim_get_feed_details`. So create `bim_get_marking_details`  ### Show the data  This should be very similar to show student details. Simply showing some additional fields in the table. Tasks are  - Show the unregistered students first. **Done**       This is intended to be annoying so as to encourage the markers to get the students registered. Of course, this may back fire for students who have stopped the course early. - Show the registered students.**Done**       Bit of work, but is going. Have to look at the sorting of columns in flexible_table. Actually, that's down to the test data. Will leave it for now.  ### What's left to do  Tasks left to do on this screen and subsequent screens include:  - General improvement in look and feel. - The sorting isn't working as expected. flexible_table not quite set up properly yet. This will effect the details screen as well. - The tab interface for details/posts screens needs to be set up.       Some initial attempts have proven to be somewhat less than successful. - There are now links to the AllocatePosts screen - but it's not working.       Function in place, but just displays message. - There are now links to the MarkPost screen - but it's not working.       Function in place, but just displays message. - Question of sorting on the question columns (by mark, submit and not submit) - The # of functions per screen is getting quite large, getting to the stage of needing to break it out into support libraries.   ``