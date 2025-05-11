---
categories:
- bim
date: 2010-02-11 13:33:50+10:00
next:
  text: BIM - Final Tidy up
  url: /blog2/2010/02/15/bim-final-tidy-up/
previous:
  text: Implications arising from the absence of the &quot;sameness of meaning&quot;
  url: /blog2/2010/02/11/implications-arising-from-the-absence-of-the-sameness-of-meaning/
title: BIM - Ideas for changes arising from user testing
type: post
template: blog-post.html
---
Today BIM was tested by an intelligent, but when it comes to BIM a clueless, user. I sat back and watched the assumptions and mistakes that were made because the system design was not well thought out enough or was missing some functionality. The following is a list of the ideas that arose from that session.

### Suspend student posts - DONE

Need the ability for the coordinator and perhaps marker to suspend a particular post so that it cannot be released.

Planned implementation:

- Add a suspend state into bim\_marking table.
- Show post details page needs to indicate suspension.
- Add entry for suspend states in Marking overview
- Add a suspend checkbox on the marking page.
    - Add the checkbox
    - Get it being set if suspended
    - Add notify box to reinforce that it is suspended.
    - Add the ability to change it
    - Ensure a suspended post is never set to mark by simple changes in mark
    - Make sure suspended is excluded from release
- ?? add a suspend checkbox on the allocate page? NO
- Allocate page does need to show that a post is suspended

### Show student details

- Trying to get last post to be colourful.
- Also - #entries is still 0, not being updated.  
    Should be set by process feed.

### Help and support

Identify the places and ideas for additional support and help resources that can be added into various screens to get folk going - ultimate aim to have it self sustaining.

Some functions from weblib.php might help here includeing :link\_to\_popup\_window, element\_to\_popup\_window, print\_heading\_with\_help, print\_box( $message, $classes ), print\_container( $message, $clearfix);, helpbutton, notice, notify (bold message in optional colour - $message, $style ='green'), page\_doc\_link( ), doc\_link(),.

- Marker - show student details
- Marker - show post details
- Marker - mark
- Marker - allocate
- Coord
    - mod\_form
    - Configure BIM
    - Manage questions
    - Allocate markers
    - Manage marking
    - Find student
    - Your students?

Modify the help file that shows links to all help files for BIM.

### See student report

Add a feature that allows markers to see exactly what one of their students sees when they visit BIM. Enables them to at least start from the same place in discussions.

### Mark post

- Next and previous student and post  
    This was in BAM. When marking an individual student post, have links to be able to go to the next or previous post for this student or for this question.
    
    This is a fairly major task, I think. In BAM when you were marking a student post there were the following :
    
    > For this student: previous post | next post  
    > For this question: previous student | next student
    
    Where the next/prev text were links that would take you to the next/prev post for the student or to the next/prev student's answer to the current question.
    
    Implementation for BIM should probably be:
    
    - Questions
        - bim\_get\_question\_hash returns list of questions, answerd by the student--- $marking\_details
        - find current question in that hash
        - get the id for next and prev (loop around at the end OR don't show?)
        - construct the URL based on those ids and the current student/bim
    - Students
        - Get a list of students who have answered the current question.
        - Find the current student in the list
        - Get ids for the next/prev
        - construct the URL.
    
    - Re-arrange some of the feedback when submitting so that it shows up more obviously and in places folk more likely to look.
    
    - Change some of the naming of "Answer" and "Submitted" etc into more action oriented easier to understand words.
    
    - Screen casts for help on marking.
    
    ### Student instructions for registering
    
    - Reduce the size of the hard-coded instructions for "how to register" to nothing.
    - NO Provide some initial default values for the "intro/about"
    - Include pointers to the screencast and other help documents for the student.
    - Change the label for the submit button to "register blog".
    - Make it clearer that once submitted, this is the detail you will see.
    - Add some advice about what to do if "question not allocated"
    - Give some indication of when the last "mirror" was and when the next one might be.
    - Add some additional links to explain specific terms.
    
    ### Some form of email group - DONE
    
    Mainly for unregistered students, some way of communicating with these students en mass to tell them to register. Some flexibility in what to send and where to send it.
    
    A fall back might be to simply show a list of email addresses for those students that can be cut and paste into an email client and/or a mailto link.
    
    ### Links for student and post details - DONE
    
    Re-work these navigation links to that they are situated more appropriately and more obvious in what they should do.
    
    ### Remove "change registration" for marker - DONE
    
    Only coordinator should be able to do this.
    
    ### Look at the ordering of the questions in columns
    
    Currently post details order of questions is somewhat arbitrary. Get it ordered on the question being entered?
    
    ### Roll overs? - NO
    
    Any chance of putting in place roll overs that provide some additional pointers on what a particular link will do.
    
    ### Show questions to users and markers?
    
    Let the students and the markers see the list of questions.