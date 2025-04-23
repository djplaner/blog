---
title: FAQs for BAM
date: 2009-03-16 07:58:06+10:00
type: page
template: blog-post.html
comments:
    - approved: '1'
      author: Mark Pearson
      author_email: markp@earlham.edu
      author_ip: 159.28.7.95
      author_url: http://markpea.wordpress.com/
      content: "David,\nI don't know whether this is the right place to leave a couple\
        \ of bug reports, but here goes.\n1. I am running a modified moodle 1.9.7 (by\
        \ http://clamp-it.org) which uses the Simplepie RSS system. This is apparently\
        \ much less bug ridden than Magpie (or so I am told). The BIM RSS system severely\
        \ conflicts with this. Here's the error message upon running admin/cron.php:\n\
        [code]\nProcessing cron function for rss_client....&lt;br /&gt;\n&lt;b&gt;Fatal\
        \ error&lt;/b&gt;:  Cannot redeclare class SimplePie_Cache_MySQL in &lt;b&gt;/usr/home/markp/public_html/clamp-LAE/lib/simplepie_1.2/simplepie.inc&lt;/b&gt;\
        \ on line &lt;b&gt;9069&lt;/b&gt;&lt;br /&gt;\n[/code]\n\n2. Most if not all of\
        \ our system run with https. So any students blog will be served from a secure\
        \ server. This does give an error from within BIM:\n\nBlog that I know generates\
        \ a valid RSS feed : https://els.earlham.edu/markpea/weblog/rss/\nGet this error:\n\
        \n    Could not access the URL\n    Unable to access the URL you provided\n\n\
        \        https://els.earlham.edu/markpea/weblog/rss/\n\n    The error created\
        \ was\n    cURL error 60: SSL certificate problem, verify that the CA cert is\
        \ OK. Details: error:14090086:SSL routines:SSL3_GET_SERVER_CERTIFICATE:certificate\
        \ verify failed\n    Please try to change the student blog again.\n\nMore details\
        \ at http://www.earlham.edu/markp/millmiss/#%5b%5bBIM%20problems%5d%5d\n\nCheers\n\
        Mark Pearson"
      date: '2010-05-01 02:58:19'
      date_gmt: '2010-04-30 16:58:19'
      id: '2254'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: davidtjones
      author_email: d.jones@cqu.edu.au
      author_ip: 59.154.24.147
      author_url: https://djon.es/blog/
      content: 'G''day Mark,
    
    
        It looks like you''ve found the github site for bim, and in particular it''s issues
        list.
    
        http://github.com/djplaner/BIM/issues/
    
    
        I''m still working out exactly how to best support a bim community, I do think
        github looks good for problems, but we''ll see.
    
        I''m open to suggestions.
    
    
        I''ll answer your questions on github, but I think the short answers are
    
        1. BIM comes with its own copy of Simplepie which it uses by default.  That''s
        the source of the conflict, solution will be to get BIM using your sites version
        of Simplepie
    
        2. More complex, my understanding is that this should work.  Need to investigate.
    
    
        David.'
      date: '2010-05-01 08:30:05'
      date_gmt: '2010-04-30 22:30:05'
      id: '2255'
      parent: '2254'
      type: comment
      user_id: '1'
    
pingbacks:
    []
    
---

See also: [[blog-home | Home]]

This page acts as a repository for frequently asked questions for the [Blog Aggregation Management (BAM) project](/blog2/research/bam-blog-aggregation-management/).

A similar resource for BIM, is starting to grow on [BIM's github site](http://wiki.github.com/djplaner/BIM/)

Current FAQs include:

- Posts, marks and comments
- Not mirrored yet
- Copy detection?

### Posts, marks and comments

#### Question

When markers' comment and allocate a mark to a blog, who can see these comments and marks? Just the student?

#### Answer

There are two parts to this question, which is applicable depends on where the comment is being made:

1. within BAM; or  
    This is the most likely approach and more information is provided below.
2. on the student's blog.  
    It is possible to comment on a student's post by going to their blog and using the blog engine's comment feature. If you use this approach, then the comment will normally be viewable by anyone, just like the student's post. This is not normally how a marker would mark/comment on a post.

What follows only applies if you are using the BAM interface to mark and comment on the student's post.

The short answer is that, only someone who logs into a CQU website using the student's CQU username/password can see the comment and the mark. However, they can only see this, if the marked post has been released.

Currently, a post can only be released by David Jones.

**Background:** When a student makes a post to their blog, BAM creates a copy on a CQU server. It associates a "state" with the post. There are four possible states:

1. UNALLOCATED - this means BAM was not able to match the post with one of the specified questions that students have to answer.
2. Submitted - this means BAM could match it to one of the specified questions.
3. Marked - this means a staff member has awarded a mark to the post.
4. Released - in this state the mark and marker's comments have been released so the student can see them. Before the post is in the "released" state, students cannot see the markers comments or mark.

This set of states is a close match to what is used in the CQU OASIS (assignment submission) system. It is designed to enable the course coordinator of moderator the option of moderating markers' comments and marks before students can see them.

### Not mirrored yet

#### Question

What does "Not mirrored yet" mean on the student blog details page?

#### Answer

Every couple of hours BAM checks the RSS feed of each student's blog. If there have been any changes BAM creates an updated copy of the student's blog on a university computer. i.e. it mirrors the student's blog. (At this time BAM also checks the new posts to see if they are an answer to any of the required questions.

The "Student Blog Details" page of BAM manage (the first page you see when you login to BAM Manage) has a column "Last Post" that will show how long ago the student's last post was mirrored by BAM. This is shown in days e.g. "4 days ago".

Early in the term, this column may show "Not mirrored yet". It means that BAM has not been able to make a local copy of the student blog yet. There are two main reasons why this might occur include:

- The mirror process hasn't been run since the student registered their blog.  
    _Solution:_ If you wait a couple of hours this should disappear when BAM next tried to mirror all student blogs.
- There is some sort of problem that is preventing BAM from mirroring the student's blog.  
    _Solution:_ You need to contact [me](mailto:d.jones@cqu.edu.au) so the problem can be diagnosed.

### Is copy detection possible?

#### Question

Is it possible to run copy detection on the student blog posts?

#### Solution

Yes. It is fairly rudimentary and it is not automated, but it is possible.

Since it is currently not an automated process, let me know if you wish to have copy detection run. Please specify how often you would like it run (sorry, can't do it more than once a week at this stage).

_Limitations:_ currently the copy detection is only intra-corporal. i.e. it only checks student posts against other student posts. It doesn't yet check against external sources. Technically this could be added (as could automation etc.), however, from a resource perspective this is not likely during the first half of 2009.