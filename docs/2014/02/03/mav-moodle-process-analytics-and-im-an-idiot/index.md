---
categories:
- edc3100
- elearning
- indicators
- irac
date: 2014-02-03 13:24:40+10:00
next:
  text: Analysing EDC3100 using MAV
  url: /blog/2014/02/03/analysing-edc3100-using-mav/
previous:
  text: '#moodle Activity Viewer (MAV) and the promise for bricolage'
  url: /blog/2014/02/02/moodle-activity-viewer-mav-and-the-promise-for-bricolage/
tags:
- mav
title: '"MAV, #moodle, process analytics and how I''m an idiot"'
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: Charles Schaefer (@charlesschaefer)
      author_email: charlesschaefer@twitter.example.com
      author_ip: 186.213.92.22
      author_url: http://twitter.com/charlesschaefer
      content: 'MAV is great. I didn''t know it. It is really a great tool to increase
        the power of teachers.
    
    
        It''s also a great news to see people using the data they have to increase the
        knowledge and get more insights about students and their habits.
    
    
        Thanks!
    
    
        Charles Schaefer
    
        http://www.eadbuilder.com.br/'
      date: '2014-02-04 09:55:43'
      date_gmt: '2014-02-03 23:55:43'
      id: '945'
      parent: '0'
      type: comment
      user_id: '0'
    
pingbacks:
    - approved: '1'
      author: Analysing EDC3100 using MAV | The Weblog of (a) David Jones
      author_email: null
      author_ip: 192.0.82.170
      author_url: https://djon.es/blog/2014/02/03/analysing-edc3100-using-mav/
      content: '[&#8230;] to post their introductions. This is where MAV is particularly
        interesting, so much so it sparked another blog post. In short, I need to revisit
        this [&#8230;]'
      date: '2014-02-03 15:22:47'
      date_gmt: '2014-02-03 05:22:47'
      id: '944'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: 'MAV, #moodle, process analytics and I''m an idio...'
      author_email: null
      author_ip: 89.30.105.121
      author_url: http://www.scoop.it/t/elearning-stuff/p/4015377360/2014/02/05/mav-moodle-process-analytics-and-i-m-an-idiot-the-weblog-of-a
      content: '[&#8230;] I&#039;m currently analysing the structure of a course I teach
        and have been using @damoclarky&#039;s Moodle Activity Viewer to help with that.
        In the process, I&#039;ve discovered that I&#039;m an idiot in having missed the
        much more interesting ...&nbsp; [&#8230;]'
      date: '2014-02-05 16:31:05'
      date_gmt: '2014-02-05 06:31:05'
      id: '946'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: 'Looking for a new &#8220;icebreaker&#8221; for #edc3100 | The Weblog of
        (a) David Jones'
      author_email: null
      author_ip: 207.198.101.64
      author_url: https://djon.es/blog/2014/02/18/looking-for-a-new-icebreaker-for-edc3100/
      content: '[&#8230;] mentioned previously the simplistic (lazy) introductory forum
        for #edc3100 didn&#8217;t achieve it&#8217;s ill-defined [&#8230;]'
      date: '2014-02-18 10:05:57'
      date_gmt: '2014-02-18 00:05:57'
      id: '947'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
I'm currently analysing the structure of a course I teach and have been using @damoclarky's [Moodle Activity Viewer](/blog/2014/02/02/moodle-activity-viewer-mav-and-the-promise-for-bricolage/) to help with that. In the process, I've discovered that I'm an idiot in having missed the much more interesting and useful application of MAV than what I've mentioned previously. The following explains (at least one example of) how I'm an idiot and how MAV can help provide a type of process analytics as defined by Lockyer et al (2013).

## Process analytics

In summary, Lockyer et al (2013) define process analytics as one of two broad categories of learning analtyics that can help inform learning design. Process analytics provide insight into "learner information processing and knowledge application ... within the tasks that the student completes as part of a learning design" (Lockyer et al, 2013, p. 1448). As an example, they mention the use of social network analysis of student discussion activity to gain insights into engaged a student is with the activity and who the student is connecting with within the forum.

The idea is that a learning analytics application becomes really useful when combined with the pedagogical intent of the person who designed the activity. The numbers and pretty pictures by themselves are more valuable in combination with teacher knowledge.

## A MAV example - Introduction discussion forum

I'm currently looking through the last offering of my course, trying to figure out what worked and what needs to be changed. As part of this, I'm drawing on MAV to give me some idea of how many students clicked on particular parts of the course site and how many times they did click. At this level, MAV is an example of a very primitive type of learning analytics.

Up until now, I've been using MAV to look at the course home page as captured in this [large screen shot](http://www.flickr.com/photos/david_jones/12259871663/sizes/o/). When I talk about MAV, this is what I show people. But now that I actually have MAV on a computer where I can play with it, I've discovered that MAV actually generates an access heat map on any page produced by Moodle.

This includes discussion forums, as shown in the following image (click on it to see a larger version).

[![Forum students by David T Jones, on Flickr](http://farm4.static.flickr.com/3733/12280500854_2b378f6777_m.jpg "Forum students by David T Jones, on Flickr")](http://www.flickr.com/photos/david_jones/12280500854/)

This is a modified (I've blurred out the names of students) capture of the Introduction discussion forum from week 1 of the course. This is where students are meant to post a brief introduction to themselves, including a link to their newly minted blog.

With a standard Moodle discussion forum, you can see information such as: how many replies to each thread; who started the thread; and, who made the last post. What Moodle doesn't show you is how many students have viewed those introductions. Given the pedagogical purpose of this activity is for students to read about other students, knowing if they are actually even looking at the posts is useful information.

MAV provides that information. The above image is MAV's representation of the forum showing the number of students who have clicked each link. The following image is MAV's representation of the number of clicks on each link.

[![Forum clicks by David T Jones, on Flickr](http://farm6.static.flickr.com/5486/12280227853_525e140eb5_m.jpg "Forum clicks by David T Jones, on Flickr")](http://www.flickr.com/photos/david_jones/12280227853/)

What can I derive from these images by combining the "analytics" of MAV with my knowledge of the pedagogical intent?

- Late posts really didn't help make connections.
    
    The forum is showing the posts from most recent to least recent. i.e. the posts near the top are the late posts. This forum is part of week 1, which was 15th to 19th of July, 2013. The most recent reply (someone posting their introduction) was made in Oct. Subsequent posts are from 7th to 10th August, almost a month after the task was initially due (the first assignment was due 12th August, completing this task contributed a small part of the mark for the first assignment).
    
    These late posts had really very limited views. No more than 4 students viewing them.
    
- But then neither did many of them.
    
    Beyond the main thread started by my introduction, the most "popular" other introduction was clicked on 41 times by 22 students (out of 91 in the course). Most were significantly less than this.
    
    Students appear not to place any importance on reading the introductions of others. i.e. the intent is not being achieved.
    
- Students didn't bother looking at my Moodle profile.
    
    The right hand column of the images shows the name of the author and the time/date of the last post in a thread. The author's name is also a link to their Moodle profile.
    
    MAV has generated an access heat map for all the links, including these. There are no clicks on my profile link. This may be because the course site has a specific "Meet the teaching team" page, or it maybe they simply don't care about learning more about me.
    
- It appears students who posted in a timely manner had more people looking at their profiles.
    
    This is a bit of stretch, but the folk who provided the last post to messages toward the bottom of the above images tend to have higher clicks on their profile than those later in the semester. For example, 19, 22, and 12 for the three students providing the last posts for the earliest posts, and, 1, 1, and 7 for the students providing the last post for the more recent posts.
    
- Should I limit this forum to one thread?
    
    The most popular thread is the one containing my introduction (549 clicks, 87 students). Many students posted their introduction as a reply to my introduction. However, of the 122 replies to my post, I posted 30+ of those replies.
    

In short, I need to rethink this activity.

## Implications

I wonder if the networks between student blog posts differs depending on when they posted to this discussion forum? Assuming that posting to this discussion forum on time is an indicator of engagement with the pedagogical intent?

If the aim behind an institutional learning analytics intervention is to improve learning and teaching, then perhaps there is no need for a complex, large scale enterprise (expensive) data warehouse project. Perhaps what is needed is the provision of simple - but currently invisible information/analysis - via a representation that is embedded within the context of learning and teaching and thus makes it easier for the pedagogical designer to combine the analytics with their knowledge of the pedagogical intent.

Answering the questions of what information/analysis and what representation is perhaps best understood by engaging and understanding existing practice.

@damoclarky needs to be encouraged to do some more writing and work on MAV and related ideas.

## References

Lockyer, L., Heathcote, E., & Dawson, S. (2013). Informing Pedagogical Action: Aligning Learning Analytics With Learning Design. American Behavioral Scientist, 57(10), 1439–1459. doi:10.1177/0002764213479367