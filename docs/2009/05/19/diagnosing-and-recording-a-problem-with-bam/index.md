---
title: Diagnosing and recording a problem with BAM
date: 2009-05-19 13:14:31+10:00
categories: ['bam']
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: VRBones
      author_email: vrbones@hotmail.com
      author_ip: 150.101.181.34
      author_url: http://www.vrbones.com
      content: I like the sentiment of describing the thought process rather than just
        the fix / kludge, but once you are checking the code in 6 months time, what triggers
        you to look outside the code and onto this blog? Did you link this post back into
        the code or copy portions of it to the relevant comment blocks?
      date: '2009-05-20 09:44:45'
      date_gmt: '2009-05-19 23:44:45'
      id: '2513'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: davidtjones
      author_email: d.jones@cqu.edu.au
      author_ip: 138.77.2.131
      author_url: https://djon.es/blog/
      content: 'There''s no formal link.  The code is used by others as well.
    
    
        In this case, it will be my decision to look back at the blog.  The blog has a
        nice search engine, the post is tagged with BAM.  The plan is that when/if I have
        a problem with this bit of code, I can do a quick search on the blog and see if
        anything is relevant.
    
    
        It''s the age-old problem with documentation, which some have solved by having
        tight integration with docs and code.  I can''t do it, so I have to do it this
        more loosely coupled way.
    
    
        Given my beliefs, I prefer the loosely couple approach'
      date: '2009-05-20 09:53:53'
      date_gmt: '2009-05-19 23:53:53'
      id: '2514'
      parent: '2513'
      type: comment
      user_id: '1'
    - approved: '1'
      author: VRBones
      author_email: vrbones@hotmail.com
      author_ip: 150.101.181.34
      author_url: http://www.vrbones.com
      content: 'I''ve been fiddling with wikis for personal documentation of code, but
        more because they can just as easily document procedures, ideas, todo lists, etc.
        Personally I like having all the code and documentation in one place so that I
        can be confident that I can get back to it if needed (then promptly trash that
        project from my own memory). Still looking for a taggable solution that integrates
        with some sort of source repository because it seems like the perfect thing to
        tag up for future reference.
    
    
        I''ll be interested in how the blog markup goes ...'
      date: '2009-05-20 13:40:50'
      date_gmt: '2009-05-20 03:40:50'
      id: '2516'
      parent: '2513'
      type: comment
      user_id: '0'
    - approved: '1'
      author: davidtjones
      author_email: d.jones@cqu.edu.au
      author_ip: 138.77.2.131
      author_url: https://djon.es/blog/
      content: 'We''ll see.  Not sure my experiments will be all that valid.  It''s likely
        that any coding I do will be severely limited, so probably not a real test.
    
    
        I''ve been involved with groups over the years that have used mailing lists (+searchable
        web archives) and wikis.  Both worked okay, but the tools are only as good as
        how the people use them.'
      date: '2009-05-20 14:11:55'
      date_gmt: '2009-05-20 04:11:55'
      id: '2517'
      parent: '2513'
      type: comment
      user_id: '1'
    
pingbacks:
    - approved: '1'
      author: Another BAM problem &#8211; awarding mark of 0 &laquo; The Weblog of (a)
        David Jones
      author_email: null
      author_ip: 74.200.245.187
      author_url: https://djon.es/blog/2009/05/20/another-bam-problem-awarding-mark-of-0/
      content: '[...] BAM problem &#8211; awarding mark of&nbsp;0  Following on from yesterday&#8217;s
        start of using the blog to record fixes to software, here comes another [...]'
      date: '2009-05-20 12:33:42'
      date_gmt: '2009-05-20 02:33:42'
      id: '2515'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
Trying out a new approach to documentation of coding changes to [BAM](/blog2/research/bam-blog-aggregation-management/) - i.e. writing it up in a post.

### The problem

A large number of student blogs are being reported as "Not mirrored yet". BAM is meant to report the amount of time since an individual student blog was last updated (i.e. a student made a post) and mirrored.

### Diagnosing the problem

- Is mirroring still working?  
    Yes, student blogs are being mirrored as they updated. The copies of each student's RSS feed is being kept up to date.

- Are the new posts being "allocated" properly?  
    Yes, the student I'm checking has a RSS file with a file system time stamp of "May 14 20:43". This indicates when the file was mirrored from the student's blog.
    
    The BAM\_BLOG\_MARKING table has a DATE\_PUB time stamp for the most recent post for this student of "2009-05-14 10:43:11". This indicates that the allocation is working, when BAM mirrors a RSS file, it goes through each student post, any new ones it attempts to allocate.
    
    It appears that it is using the CQU system current time to allocate DATE\_PUB
    
    > **Small problem:** Strictly speaking it should be using the date published value for the post as stored in the RSS.
    
    **Actually**, this isn't what's happening, the student had actually made a post at that time.
- Is the "LAST\_POST" field being updated?  
    No, it's set to the 0 value. This is where the problem is starting. When the display code sees this 0 value, it assumes that the blog hasn't been mirrored yet.

Something in the allocation process is updating the LAST\_POST field in BAM\_BLOG\_STATISTICS incorrectly. Rather than put in the timestamp for the most recent post, it's setting it to 0.

### Locating the problem

The mirror/allocation process is

- BAM/support/mirror.pl creates BAM::Mirror object and calls DoMirror
- BAM::Mirror::DoMirror  
    For each course currently being mirrored , create BAM::BlogStatistics object and call DoMIrror
- BAM::BlogStatistics::DoMirror  
    For each student in the course mirrorFeed (get the latest copy of the RSS file for the blog) and then parseFeed.
- BAM::BlogStatistics::parseFeed
    - use XML::Feed to parse the local copy of the RSS file
    - use XML::Feed to get the lastModified timestamp for the blog
    - if there are more posts in the new file than the last one then
        - BAM::BlogElements->new for the student
        - updateMarking
- if mirrorFeed returns true then update NUM\_ENTRIES and LAST\_POST in BAM\_BLOG\_STATISTICS

It appears that the likely problem is

- the value for LAST\_POST is being set incorrectly in parseFeed, or
- the update of LAST\_POST is setting it to the wrong value.

My guess is that parseFeed is the source of the problem - though I wonder why it's happened all of a sudden.

#### Checking parseFeed

Will have to write a stand alone script using XML::Feed and an existing RSS file. Can't use the above as the mirror thing depends on a new post.

Well, it looks like the "modified" method for XML::Feed is not working. Why?

Okay, tried the same script on an "old" XML file. It seems that Wordpress - possibly for an external reason - has changed the format of the RSS that it generates. This has broken the method used to get the time the blog was last updated.

The change, in the XML, appears to have been a change from the tag "pubDate" to "modified".

### Solution

The current Perl/Webfuse-based instantiation of BAM is not likely to last long. Combine this with other contextual factors and the solution will have to be a kludge.

Essentially some additional checking has been inserted into the section that tries to get the lastModified timestamp for the blog. Very kludgy

Have also modified the return code check of the mirror process. Normally it only runs the parseFeed stuff if the return code is 200 i.e. there's been a change. Modified it (for short-term) to run parseFeed for 304 return codes - this will update the LAST\_POST value.

Running this on a whole course identified another kludge that was needed to get the modified date. That's done. Now to run the kludge script on all the current courses, remove the 304 check and then commit everything.