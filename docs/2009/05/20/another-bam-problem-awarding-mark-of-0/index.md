---
title: Another BAM problem - awarding mark of 0
date: 2009-05-20 12:33:24+10:00
categories: ['bam']
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: VRBones
      author_email: vrbones@hotmail.com
      author_ip: 150.101.181.34
      author_url: http://www.vrbones.com
      content: 'What about setting the initial value to something other than a valid mark,
        like -1 or null? Once you get to reporting or checking if all marks have been
        entered you''re probably going to hit the same issue: No distinction between a
        to-be-entered mark and a valid mark of 0.'
      date: '2009-05-20 13:09:04'
      date_gmt: '2009-05-20 03:09:04'
      id: '2518'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: davidtjones
      author_email: d.jones@cqu.edu.au
      author_ip: 138.77.2.131
      author_url: https://djon.es/blog/
      content: 'I''d considered that but it would have required broader changes to the
        code and also checking/changing existing entries in the database.
    
    
        BAM, in it''s current technology format, has a limited lifespan i.e. it will be
        lucky to see out the year. Additionally, I have a PhD to work on. Hence, the emphasis
        is on quick and dirty when figuring out how to solve problems.'
      date: '2009-05-20 13:13:18'
      date_gmt: '2009-05-20 03:13:18'
      id: '2519'
      parent: '2518'
      type: comment
      user_id: '1'
    
pingbacks:
    []
    
---

See also: [[blog-home | Home]]

Following on from [yesterday's start](/blog2/2009/05/19/diagnosing-and-recording-a-problem-with-bam/) of using the blog to record fixes to software, here comes another one.

### Problem

Awarding a student a mark of 0 for a post, doesn't work

### Identify the cause

First, re-create the problem, log in and try and give the student a mark of 0 - yep doesn't work.

Check the database, there is a mark of 0 recorded. However the textbox in which the mark should be displayed, is empty.

Let's try changing it to a non-zero mark and then back again - I'm wondering if 0 is the default mark. Ahh, giving the student a mark of 5 and then changing it back to 0 results in the 0 appearing in the box. Seems to be some screwy code.

Looking further it seems that the following is happening

- A post's database entry starts with a mark of 0 and a status of Submitted.
- When displaying this type of entry the 0.000 in the database is modified to the empty string by the view code.  
    I'm assuming this is to stop the marker thinking that a mark of 0 has already been awarded.
- The code processing the submitted form (i.e. I've entered a mark of 0 and hit submit) is comparing fields in form to data in database. If a mark of 0 is awarded in the form it will equal the default value in the database and hence not spark a change.

### Solution

If the mark in the form is 0 and not empty, then a change must be made.