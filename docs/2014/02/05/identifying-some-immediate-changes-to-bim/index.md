---
title: Identifying some immediate changes to BIM
date: 2014-02-05 15:35:29+10:00
categories: ['bim', 'bim2']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: BIM testing and fixes | The Weblog of (a) David Jones
      author_email: null
      author_ip: 66.155.9.119
      author_url: https://djon.es/blog/2014/02/07/bim-testing-and-fixes/
      content: '[&#8230;] Moodle instance thereby providing a minimum working version
        for installation. As per yesterday&#8217;s planning the hope is to make further
        changes based on this [&#8230;]'
      date: '2014-02-07 13:53:44'
      date_gmt: '2014-02-07 03:53:44'
      id: '948'
      parent: '0'
      type: pingback
      user_id: '0'
    
---

See also: [[blog-home | Home]]

I have until the 21st of February to get [BIM](/blog2/research/bam-blog-aggregation-management/) tested and ready for installation into the institutional Moodle instance. The following is some initial planning of what I'd like to get done in that time frame. A list that will then need to be further whittled away to what I can get done in that time frame. There are three categories of changes

1. Changes to better support the pedagogy I'm currently using.
2. Changes from the BIM issues list.
3. Changes to ensure correct functioning.

## Better support the pedagogy

The pedagogy/learning design that informed the initial design of BIM is fairly limiting. The learning design/pedagogy I'm currently using isn't directly supported by BIM. I found myself last year doing a range of programming kludges to get it to work. This won't work in the second half of this year when a non-technical academic takes over as course coordinator. BIM better fitting the current learning design saves me time and enables other people to use this approach.

- [Allow more than one post to be allocated to a question](https://github.com/djplaner/moodle-mod_bim/issues/60)
    
    Already had this as an issue. Would allow "questions" to be though of as modules (in EDC3100 speak) or time periods.
    
- Allow student allocation of posts to a question.
    
    Mentioned in [this issue](https://github.com/djplaner/moodle-mod_bim/issues/26) (amongst other extensions).
    
- The student interface would also need to be changed to handle the display of multiple posts to a question.
- Have BIM generate statistics about length of posts, number of links and number of links to other student posts. Display this to the student and generate a CSV file for the marker.
- Also seems to suggest some sort of auto mark generation based on the statistics.
- Have a default allocation of posts to questions/topics based on the date OR just have it set to a particular value (i.e. all posts should now be allocated - by default - to Module 1).

The basic idea behind these changes is that students are required to make a number of posts per Module in the course (one module = about 3 weeks). Students mark for the posts for each module is based solely on the number of posts and that the posts meet a certain set of statistics (length of posts, links etc). These marks are added as part of the bigger assignment that is associated with the module.

Students need to be able to see their progress. Markers need to be able to access the statistics to mark assignments.

Changes required would likely include

1. Changes to student interface
    1. Show question allocation as a row (not a column).
    2. Replace the "Status" column with a "Statistics" column that includes the number of words, links etc statistics
    3. What options exists with parsing HTML and extracting links in PHP and in Moodle.
    4. Show unallocated posts together in a separate set of rows - perhaps even a special form - where the questions allocation drop box is available.
2. Changes to the coordinator interface
    1. Configuration option for multiple questions
        
        **database change required**
        
    2. Change the default allocation of posts.
    3. Some how deal with questions that aren't questions.
    4. How to specify statistics for auto marking.
    5. What if any changes are required for the "Manage Marking" page.
        
        May not need it. As this page simply shows counts. With multiple posts to a question, the count should still work.
        
    6. What to do about the workflow and the idea of marked/suspended/released if posts aren't being marked, simply analysed.
3. Changes to the marker interface
    1. "Mark posts" will still need to be used to allocate posts (or should this feature be added to "View student details") even though "marking" may not make sense.
    2. "Mark posts" cell with a question would need to show the number of posts for that question implying no way to mark directly. Or perhaps list each post? **Needs thought here**
    3. "Allocate posts" page will need to retain all question names in the "Choose one" drop box.
    4. "Allocate posts" page should also have an additional heading to group multiple posts to the one question -- this may enable doing without the database change for the new configuration option.
    5. May need to add to "Allocate posts" a link to "mark this post" so that "Mark posts" page can point to a list of posts and one can be chosen for marking. Mmmm.
    6. One of these pages should have a link to export a CSV file containing marks for students against posts.

## From the BIM issues list

The BIM source code is [hosted on github](https://github.com/djplaner/moodle-mod_bim/) and I've been using the associated [issue list](https://github.com/djplaner/moodle-mod_bim/issues?labels=bim25&state=open) to record any ad hoc improvements/fixes. The following are the issues that would be nice

- [No response to find student](https://github.com/djplaner/moodle-mod_bim/issues/81) - a bug, has it been fixed yet?
    
    Seems to specific to Moodle 2.5, so not directly applicable to the institutional context.
    
- [Warn of summary feeds](https://github.com/djplaner/moodle-mod_bim/issues/76)
    
    Problem from last year, blogs configured to just showing the first few lines of posts, not the whole post.
    
- A couple of issues about updating posts - allow students/markers to update posts stored in BIM (mostly to fix errors or recent changes).

## Correct functioning

- Check out any and all warnings being generated by BIM now.
- Bulk email
    
    Used in a number of places. This is not working. Either on mootest or my box. A missing parameter. Not sure when this cropped up.
    
- User search
    
    Search for a student within BIM isn't working on mootest, it does work on my box. My initial guess is some SQL type queries in BIM that are MySQL specific.
    
- All teaching staff are coordinators
    
    The distinction between coordinator and marker isn't kicking in as it should.