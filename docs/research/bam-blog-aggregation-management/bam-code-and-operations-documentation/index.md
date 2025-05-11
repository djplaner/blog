---
date: 2009-04-07 14:47:04+10:00
title: BAM code and operations documentation
type: page
template: blog-post.html
---
The following page provides a summary of docs associated with the implementation of BAM

### Automatic allocation

Background: when a post is made to a student blog. BAM looks at the title and the content of the post in order to try and determine if it matches one of the questions that students have to answer. If there is a match, it allocates the post to that question.

This relies on the Mirror process, which is eventually done by BAM::BlogStatistics->DoMirror(). This object works either on a list (possibly only 1) of student feeds.

If an updated RSS feed is found, it calls "parseFeed"

In turn this creates a BAM::BlogElements object and then calls updateMarking which then

- get's the local copy of the XML feed
- uses BAM::BlogUnAllocated to get a list of all posts actively set to not allocated in the BAM\_BLOG\_MARKING table.
- foreach entry in the feed
    - stop if the item has already been set to unallocated
    - foreach question unanswered by this student
        - is the current entry a match for the current question? then
            - getRowData for question/entry
            - assign it
            - go to next entry
- if there were any allocations found, update the database, get the data again

webfuse/lib/BAM/support/reallocate.pl does this for given students.