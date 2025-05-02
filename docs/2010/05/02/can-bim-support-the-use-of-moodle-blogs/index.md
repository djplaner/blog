---
title: Can BIM support the use of Moodle blogs?
date: 2010-05-02 16:56:18+10:00
categories: ['bim']
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: Mark Pearson
      author_email: markp@earlham.edu
      author_ip: 159.28.7.95
      author_url: http://markpea.wordpress.com/
      content: 'I think that this is a very sensible approach. IMHO the Moodle blogs notion
        is a chimera -- personally I switch it off completely on Earlham''s moodle site.
        Blogging by it''s very nature is open and RSS feeds rely on open access and  as
        far as I''m aware there is not even a standard available for ''secure'' RSS feed.
        It seems to me that there are 3 options for those who would like to use Moodle
        blogs:
    
        1. Use Moodle blogs with open RSS (but it may be that the Magpie RSS feed generation
        is broken)
    
        2. If privacy is essential then use a discussion Forum or online Assignment.
    
        3. Rustle up resources to commission a Moodle blog BIM equivalent.
    
        By bringing external blog feeds into Moodle in a manageable way BIM in it''s current
        form admirably fits the ''Outside in'' (https://djon.es/blog/2010/04/25/inside-out-outside-in-or-both/)
        paradigm.'
      date: '2010-05-06 02:20:58'
      date_gmt: '2010-05-05 16:20:58'
      id: '3026'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: davidtjones
      author_email: d.jones@cqu.edu.au
      author_ip: 138.77.2.133
      author_url: https://djon.es/blog/
      content: 'G''day Mark,
    
    
        I agree with your comments re: blogging in Moodle.
    
    
        And as far as I know, there is no standard for a secure RSS feed.  I had been
        hoping that some sites would just use basic HTTP auth - the type which pops up
        a box for username/password - because I could code BIM to support that.  Some
        RSS readers support this, but sadly Wordpress (as one example) don''t.
    
    
        David.'
      date: '2010-05-06 13:16:42'
      date_gmt: '2010-05-06 03:16:42'
      id: '3027'
      parent: '3026'
      type: comment
      user_id: '1'
    
pingbacks:
    []
    
---
### Problem

[BIM](/blog2/research/bam-blog-aggregation-management/) is a Moodle activity module that helps academic staff manage the use of individual student blogs, where those blogs are hosted on the students' choice of blog service (e.g. Wordpress.com etc.). An in-built assumption/limitation in how BIM works is that each student's blog must be open to the world. If access to the blog is restricted, BIM can't mirror it.

For many folk this is not a problem. However, there are occasions where teaching staff want students to use individual blogs, but what the students post should be kept private, to some extent.

### One Solution?

It's [been suggested](http://github.com/djplaner/BIM/issues#issue/13) that allowing students to register their Moodle blog with BIM might get around this problem. This post is an attempt to explore that option.

### Potential constraints

I don't have a lot of time to spend on this, so it has to be simple and not involve major modifications to BIM. In addition, I'm reluctant to add to BIM special support for Moodle blogs. The aim of BIM is to encourage and enable the use of real tools through reliance on "standards" i.e. RSS and ATOM feeds. I don't want to add special support for any particular blog.

The Moodle blog itself is not much of a blog and is likely to change soon.

### The Moodle blog

Focusing on 1.9, I can find out the following:

- Site configuration for blogs.  
    Each Moodle site can configure its policies around blog visibility. Options range from turning the blog facility off entirely through to all site users being able to see all blog entries and everyone being able to see entries specified as world readable.
- Users can also configure entries for just them to see.
- RSS security by obsufucation, not real security.  
    My understanding is that Moodle blog's can generate RSS, and that restrictions are based on the location of the RSS being secret as opposed to really secure.
- As per [this post on Moodle.org site](http://moodle.org/mod/forum/discuss.php?d=134612) the Moodle site needs to have RSS enabled at the site level via: Admin blog > Server > RSS > Enable RSS

#### Moodle Blog RSS

With RSS enable at the site level, an RSS icon is displayed on a user's blog. If they click on that they get an RSS feed with the URL not being all that private. i.e. confirming above, you have to know somethings to work it out, but it can be worked out.

In terms registering a Moodle blog feed, you can't rely on auto-detect as Moodle doesn't use the right "HTML". You actually have to register the RSS feed.

But now I have another problem. I can't seem to get the Moodle blog to add posts/items to the RSS feed.

### Conclusions

I'm going to leave this investigation now without having worked it out. The reasons are:

- If you can get RSS being generated from the Moodle blog you should be able to register it with BIM, as long as the permissions are set correctly.
- If you can do this, then the students' RSS feeds are only going to be very slightly more secure than those on Wordpress.com or similar.
- It will be very easy for other students within the course to see each other posts, so not a lot of privacy.