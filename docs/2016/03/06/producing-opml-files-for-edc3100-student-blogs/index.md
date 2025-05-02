---
title: Producing OPML files for EDC3100 student blogs
date: 2016-03-06 10:32:19+10:00
categories: ['bad', 'edc3100']
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: fleeslearningblog
      author_email: fleakam@yahoo.com.au
      author_ip: 120.22.58.211
      author_url: http://fleeslearningblog.wordpress.com
      content: I really wish I understood that entire blog. More reading to do! Thank
        you
      date: '2016-03-07 07:57:43'
      date_gmt: '2016-03-06 21:57:43'
      id: '3308'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: David Jones
      author_email: davidthomjones@gmail.com
      author_ip: 139.86.69.33
      author_url: https://djon.es/blog/
      content: You really don't need to understand the task I had to complete to produce
        the OPML files. Being aware of some of the requirements might help you understand
        the way the course is organised/implemented. But it probably won't help you make
        better use of ICT and Pedagogy.
      date: '2016-03-07 08:12:52'
      date_gmt: '2016-03-06 22:12:52'
      id: '3309'
      parent: '3308'
      type: comment
      user_id: '1'
    - approved: '1'
      author: fleeslearningblog
      author_email: fleakam@yahoo.com.au
      author_ip: 120.22.58.211
      author_url: http://fleeslearningblog.wordpress.com
      content: Ok thank you for clarifying that. But is this not some of what would be
        required in the future? In understanding how much has developed in the las year
        alone, I feel that details along these lines are where the future is going. ?
      date: '2016-03-07 08:16:03'
      date_gmt: '2016-03-06 22:16:03'
      id: '3310'
      parent: '3309'
      type: comment
      user_id: '0'
    
pingbacks:
    []
    
---
EDC3100 tries to get students engaged with writing their own blogs and following the blogs of others via a feed reader. Yes, just a bit old fashioned.

But then one of the problems with doing something a bit different is that it takes a fair bit of extra work to implement. Once you automate this bit of extra work it creates a bit of inertia that prevents change. Not only because I don't want to lose the effort that went it into automating the process. But also because I know that if I did something different that was more modern, I'd have to invest more time in automating that process (i.e. working around the limitations of the current institutional learning environments.

So documenting the process.

### Students create and register their blog on the LMS

About 250 have done this so far. Another 100 to go.  But can't wait, need to get the OPML files out to students so they can start making connections.

### Get the data that identifies students by specialisation

By default the institutional learning environment doesn't provide this. That's why I had to spend Friday [doing this](/blog2/2016/03/04/preparing-my-digital-learning-space/).

Though I do now have to update the data

- Get the most recent participants.
- Get the most recent registered blogs.
- Double check "can't find data" students.
    - Find a buggy example
    - Check the local course enrolment - shows up
    - Check users\_extras - not there.  That's the problem. Don't have the extra data from student records for students who weren't enrolled a couple of weeks before the start of semester.

### Run the script

Once the data is available, I can configure and run a script that will produce the OPML files.

- Fix the configuration settings
- Do something with the NOPLAN students
- Modify the script to handle change in data format and the dirty data

### Test the OPML files

All appears to be good.

### Write the instructions for students

That's the next task.