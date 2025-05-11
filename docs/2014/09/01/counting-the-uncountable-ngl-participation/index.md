---
categories:
- edu8117
date: 2014-09-01 14:21:27+10:00
next:
  text: Signing up for Connected Courses
  url: /blog2/2014/09/02/signing-up-for-connected-courses/
previous:
  text: Personality and other factors in education
  url: /blog2/2014/08/28/personality-and-other-factors-in-education/
title: Counting the uncountable - NGL participation
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Explanation of the &#8220;draft automated analysis&#8221; email | An experiment
        in Networked &amp; Global Learning
      author_email: null
      author_ip: 66.155.9.41
      author_url: http://netgl.wordpress.com/2014/09/01/explanation-of-the-draft-automated-analysis-email/
      content: '[&#8230;] a post on my blog that briefly describes the creation of the
        program that does this analysis. The [&#8230;]'
      date: '2014-09-01 15:44:38'
      date_gmt: '2014-09-01 05:44:38'
      id: '1057'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: Some thoughts on links and assessment | An experiment in Networked &amp;
        Global Learning
      author_email: null
      author_ip: 66.155.10.55
      author_url: http://netgl.wordpress.com/2014/09/07/some-thoughts-on-links-and-assessment/
      content: '[&#8230;] Here&#8217;s what the script does (you can see the process I
        used to develop this here) [&#8230;]'
      date: '2014-09-07 11:28:42'
      date_gmt: '2014-09-07 01:28:42'
      id: '1058'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The following documents the writing of a script to perform simple counts of what the [NGL participants](http://netgl.wordpress.com/) have been doing on their blog. Another post on the course blog will offer an explanation of the emails that will be sent to participants real soon now.

### What?

There are 10+ participants in NGL. The indicators of participation being looked for are

- Number of posts.
- Average word count per post.
- % of posts with links to blog posts from other participants.
- % of posts with links to other online resources.
- % of posts from the blog that appear on the blog first (out of all participants).

### Starting point

Will start with the EDC3100 script and modify from there. That script currently calculates the following relevant

- Posts per week - not needed, but total posts will be available
- average word count
- \# of links
- \# of links to other participants

### Changes

Remove activity completion

Get Moodle user information - are we only including currently enrolled students, is now.

What about blog posts? Yep.

Calculate the stats for each participant

- NUM\_POSTS - done.
- (AVG\_)POST\_LENGTH - done.
- POSTS\_WITH\_STUDENT\_LINKS - done.
- POSTS\_WITH\_LINKS - done.
- LINKS\_HERE\_FIRST - to do.
    
    This is the more difficult task. The requirement here is for each link (not to another participant blog) made in a blog, check to see if it's the first time the link has appeared in a participant post.
    
    At the moment the function counting links does have the timepublished for the blog post. It also creates array containing a hash for each link. But that's all links, but maybe that doesn't matter.
    
    What we need here is probably a hash with key on the link and the value being a reference to the hash about the post (which has timepublished).
    
    With each student object having this, BlogStatistics object can then generate stats for LINKS\_HERE\_FIRST.
    
    DoTheLinks updated to do this in Marking.pm
    
    \-- See below --

Assign a standard and show the report

- NUM\_POSTS - DONE
- (AVG\_)POST\_LENGTH - DONE
- POSTS\_WITH\_STUDENT\_LINKS - DONE
- POSTS\_WITH\_LINKS - DONE
- LINKS\_HERE\_FIRST

Currently the report only assigns percentages for each stat, need to translate that into a mark for the assignment. This would have to

- average the percentage for each descriptor for a criteria. The current descriptors/criteria relationship is
    - Posts (10 marks)
        - \# posts
        - \# words per post
    - Connections (5 marks)
        - % posts with links to other participant blog posts
    - Other links (5 marks)
        - % posts with links to other resources
        - % of posts where links occur first - not calculated yet
- calculate the mark per criteria
    
    The above are stored in a hash where the key is the unique id for the descriptor
    
    - LENGTH = # words per post
    - NUM\_POSTS = # posts
    - LINKS = % posts with links to other resources
    - STUDENT\_LINKS = % posts with links to other participant blog posts
- add them up

# Calculating first blogs

The task here is for each student, calculate the percentage of links included in their blog posts that appear there first (amongst all the other student blogs)

What we need here is probably a hash with key on the link and the value being a reference to the hash about the post (which has timepublished).

There is a function createBlogMapping that loops through each post for each student and creates a hash ref MAPPING that maps out who links to who.

A similar function that only works on external links (or perhaps all links) and uses the timepublished to create the necessary hashref.

Perhaps something like \[code lang="perl"\] $whenShared->{$link} = { EARLIEST => "unix timestamp when published", POST => $link\_to\_blog\_post\_in\_data structure }; \[/code\]

This hash would allow a loop for each student that would count the number of times a the POST value is the user's post.

Exclude any link that isn't to the student's actual post, the first link to another student's post is counted the same as a link elsewhere

So we're looking at two methods

1. constructWhenShared - create the hash ref
2. calculateEarliestPercent - add to {MARKING}->{STATS} the percentage of links first here.