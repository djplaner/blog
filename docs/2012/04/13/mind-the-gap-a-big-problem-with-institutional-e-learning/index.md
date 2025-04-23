---
title: Mind the gap - a big problem with institutional e-learning
date: 2012-04-13 13:14:00+10:00
categories: ['elearning', 'thesis']
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: Justin (@grubbypandas)
      author_email: grubbypandas@twitter.example.com
      author_ip: 110.174.29.163
      author_url: http://twitter.com/grubbypandas
      content: Our university in Sydney has recently moved away from the moodle model
        and has moved to a custom version. The previous moodle version that was used most
        courses used the online submission as a back up only if their initial copy of
        the assessment was lost. This included all of my IT related courses I kid you
        not. I've even had examples where i have submitted an incorrect code file in the  submission
        and they have not even noticed it as they don't even run it. Now with this new
        online version, most courses don't even use the facility to submit electronically,
        let alone marking online.
      date: '2012-04-13 14:37:46'
      date_gmt: '2012-04-13 04:37:46'
      id: '341'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: Peter Albion (@palbion)
      author_email: palbion@twitter.example.com
      author_ip: 121.223.33.93
      author_url: http://twitter.com/palbion
      content: 'If you are using EASE then for some allocation patterns it is possible
        to have the system allocate to markers automatically. I have even managed, by
        scripting over the top, to allocate to markers dictated by a list in a spreadsheet.
        I also have a script that attaches feedback files to the web form without my doing
        it manually. You are welcome to both if they are likely to be of any use, even
        as a starting point for your own solution.
    
    
        I agree that the system never seems to do quite what we need. In part that is
        because it has been developed and tweaked to meet needs of others that are not
        quite the same as mine.'
      date: '2012-04-13 20:31:47'
      date_gmt: '2012-04-13 10:31:47'
      id: '342'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: David Jones
      author_email: davidthomjones@gmail.com
      author_ip: 124.186.109.100
      author_url: https://djon.es/blog/
      content: 'G''day Justin, It appears you''re not the only student <a href="http://tallynwarner.edublogs.org/2012/04/12/assignment-submissions/"
        rel="nofollow">having some problems</a> around assignment submission.
    
        The Moodle system always appeared less than functional. I think some current work
        may address that. But then there''s the question of change around academic practice.
        David.'
      date: '2012-04-14 10:43:15'
      date_gmt: '2012-04-14 00:43:15'
      id: '343'
      parent: '341'
      type: comment
      user_id: '1'
    - approved: '1'
      author: David Jones
      author_email: davidthomjones@gmail.com
      author_ip: 124.186.109.100
      author_url: https://djon.es/blog/
      content: I'm not sure the system really suits anyone, at least not anyone with large
        courses. Will gladly take you up on the scripts. Catch up next week.
      date: '2012-04-14 10:44:26'
      date_gmt: '2012-04-14 00:44:26'
      id: '344'
      parent: '342'
      type: comment
      user_id: '1'
    
pingbacks:
    []
    
---

See also: [[blog-home | Home]]

The almost 300 students in the course I'm teaching have their first assignment due on Monday. I'm currently laying the ground work to help the small course team to mark those assignments. Actually I'm busy procrastinating about the task by writing this blog post. Mainly because it is more work than it needs to be and it is this way because of one of the fundamental flaws of how universities are currently implementing e-learning systems.

A flaw which means they can never ever bridge the gap between what people actually need to do with the system and what the system does. For many the gap won't be large, but when you are marking 100+ assignments within a couple of weeks what was once a small gap grows quite significantly. A situation where forewarning of the gap isn't sufficient, it should be filled.

!!! warning "Broken image link"

I'm going to illustrate my point with the current online assignment submission system I'm working with. There may well be a range of contextual reasons why this system is designed the way it is, and it is a step up from some I've seen. But those contextual reasons are part of my point, the context within which e-learning systems - like an LMS - are supported and operate is not conducive to bridging the gap (let alone doing something innovative). The point is broader than online assignment submission.

### Manual distribution

For example, there are three people who will mark these assignments. They will be marking different cohorts. The system has been told which cohorts they will be responsible for marking.

I assumed that as students submitted their assignments these markers would be able to access those assignments. i.e. the system would automatically allocate them to the marker. No.

Instead a human being need to be involved to manually allocate. Always fun to do with 300 assignments.

### Marking

The students have created a page in Mahara. They are submitting the URL, which is one of the options in the system. The marker sees a page that lists each student they are marking. For each student there is the link they submitted, some space to add a comment, add a mark, and space to upload a file. In our case, we're going to use an Excel spreadsheet to give feedback.

This means that for each student the marker will have to manually make a copy of the spreadsheet for this student, enter the student's number and name into the spreadsheet, click on the link, mark the submission, copy the grade created by the spreadsheet into the form, and upload the spreadsheet.

If you're marking 10, not a big problem. When you're marking 100+....

### Filling the gap

There are many ways to fill this gap. The approach I'm going to use (I hope) is to write a script that will allow me to give each marker a zip file. The zip file will contain a collection of Excel spreadsheets. The file name of each spreadsheet will match the name and number of one of the students they will mark. Each spreadsheet will include the student's name, number and the URL for their Mahara page. Without entering the submission system, the marker can work through the spreadsheets, click on the URLs and mark the assignments.

It's just a pity the marker can't zip up the spreadsheets and upload them into the system in one go.

### A new system will solve it

There seems to be interesting work being done around Moodle's assignment submission/management system. My institution will probably move to that at some stage. The move will be promoted as solving all sorts of problems.

But it won't solve the problem of filling the next gap. With the new system there will be some gap that is identified. Some new practice that would be really good. The trouble is that how e-learning systems are implemented and supported within most institutions means that this gap/new practice will not be implemented. It will have to wait until the next grand, new system. During that time huge amounts of staff and student time will be wasted jumping over the gap, filling it in, or worse, ignoring it.

### Big deal?

Using an approach better suited to filling the gaps we implemented an online assignment management system that had filled many (but not all) these types of gaps almost 10 years ago. A system that was [well received by its users](http://djon.es/blog/wp-content/uploads/2008/12/oasissubmit_v3.pdf).

For almost 10 years there have been institutions of higher education using online assignment submission systems that are wasting time and money. And this is just one of those boring, administrative jobs at the current core of higher education. Imagine all the other unfulfilled gaps and opportunities that have been missed.

A more in-depth extension of this argument and one proposed solution forms the [foundation of my thesis](/blog2/research/phd-thesis/).