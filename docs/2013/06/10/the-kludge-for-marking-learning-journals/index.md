---
title: The kludge for marking learning journals
date: 2013-06-10 11:08:53+10:00
categories: ['bim', 'edc3100', 'elearning']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: The network challenge to the LMS mindset | The Weblog of (a) David Jones
      author_email: null
      author_ip: 72.232.112.10
      author_url: https://djon.es/blog/2013/08/29/the-network-challenge-to-the-lms-mindset/
      content: '[&#8230;] docs or any one of the huge array of external services that
        are out there. An extreme example is my kludge for using BIM this year. Where
        I&#8217;m hosting a version of BIM on my laptop because for various [&#8230;]'
      date: '2013-08-29 06:30:13'
      date_gmt: '2013-08-28 20:30:13'
      id: '786'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: Learning journal, activity completion and nudge analytics | The Weblog of
        (a) David Jones
      author_email: null
      author_ip: 66.135.48.138
      author_url: https://djon.es/blog/2014/07/31/learning-journal-activity-completion-and-nudge-analytics/
      content: '[&#8230;] Week 2 of 2nd semester. Time to start checking how students
        are going and checking in with those that haven&#8217;t started yet. For EDC3100,
        this means putting in place the various &#8220;shadow systems&#8221; that bridge
        what&#8217;s provided by the institution and what I need in order to enact the
        practices I deem appropriate. What follows is a record of the ongoing evolution
        of this idea. [&#8230;]'
      date: '2014-07-31 11:06:18'
      date_gmt: '2014-07-31 01:06:18'
      id: '788'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: Preparing my digital &#8220;learning space&#8221; &#8211; The Weblog of
        (a) David Jones
      author_email: null
      author_ip: 192.0.101.161
      author_url: https://davidtjones.wordpress.com/2016/03/04/preparing-my-digital-learning-space/
      content: '[&#8230;] draft learning journal reports. [&#8230;]'
      date: '2016-03-04 13:33:52'
      date_gmt: '2016-03-04 03:33:52'
      id: '789'
      parent: '0'
      type: pingback
      user_id: '0'
    
---

See also: [[blog-home | Home]]

The following is a description of the kludge I put in place to mark the learning journals - see [here for a description](/blog2/2013/02/25/the-assessment-of-learning-journals-ideas-for-bim/) of initial thinking behind the journal - folk in the EDC3100 course this semester had to complete. It's meant to record what I did, provide some food for further development and offer an opportunity for some initial reflection.

### Final format

5% of each of the three course assignments contained a component titled the "learning journal". In this, the students were expected for the relevant weeks of semester:

- complete all the activities on the course site; and,
- post a sequence of reflective posts on their personal blog.

As outlined in the [ideas post](/blog2/2013/02/25/the-assessment-of-learning-journals-ideas-for-bim/) the student's mark was based on:

- what percentage of the activities they completed;
- how many posts per week (on average) they published;
- the word count of those posts;
- the number of posts that contained links; and,
- the number of posts that contained links to posts from other students in the course.

The intent was to encourage connections and serendipty and minimise students having to "reflect to order" in response to specific questions/criteria. Of course, that didn't stop many from seeking to produce exactly what was required to obtain the mark they wanted to achieve. 100 words per average means exactly that and also a bit of judicious quoting etc. Something for further reflection.

### Activity completion

Each week the course site had a number of Moodle activities and resources, all with activity completion turned on. This means that Moodle tracks who has fulfilled the necessary actions to complete e.g. read a page, post to a forum etc.

The reports of activity completion aren't particular helpful as I need to get the data into a Perl script, so the process is

1. Download the CSV file Moodle can export of activity completion.
    
    The CSV file for the course I just downloaded was 1.7Mb in size.
    
2. Delete the columns for the activities that don't belong to the required period.
3. Save it locally.

### Blogs

I've written some Perl scripts that will parse the BIM database, evaluate the student posts and then combine that with the data from the activity completion CSV and produce the report. This report is circulated to the markers who manually copy and paste the students result into their assignment sheet. I've also got a version of the script that will email all the students a copy.

Of course, to get to this stage I've had to make sure that all of the students' blogs are registered correctly with the version of BIM on my laptop. Then I need to

1. Run the BIM mirror process to ensure that BIM has the most recent student posts.
    
    Currently 335 students have registered blogs and there are 8550 posts mirrored. For an average of about 25 posts per student. In reality, there have been a number of students withdraw from the course for a number of reasons.
    
2. Dump the PHP BIM database and create a copy in the Perl database.
    
    Due to how I've got Perl and PHP installed they are using different MySQL database servers.
    
3. Run either script.

### The end result

Is a report that summarises results. But beyond this it's a lot of extra work in overcoming human error that would have been removed with a decent system. I've spent a fair chunk of the last week dealing with these errors that mostly arise from the absence of a system giving students immediate feedback of problems including

- Telling students they've registered a URL that is either not a URL or not a valid RSS feed.
    
    Earlier problems dealt with students making mistakes with registering their blog. BIM does this, but because BIM isn't installed on the institutional servers I had to make do with the Moodle database activity and then manually fixing errors.
    
- Warning students that their RSS feed is set to "summary" and not "full".
    
    To encourage visitors to the actual blog, some blog engines have an option to set the feed to "summary" mode. A mode where only the first couple of sentences of a post is shown in the feed. This is not useful for a system like BIM that assumes it's getting the full post. Especially when "average word count" is part of the marking mechanism.
    
    I've spent a few hours this week and more this semester helping recover this situation. BIM needs to be modified to [generate warnings](https://github.com/djplaner/moodle-mod_bim/issues/76) of this so recovery can happen earlier.
    
- Students editing posts.
    
    Currently, once BIM gets a copy of a post it doesn't change it. Even if the author makes a change. This caused problems because some students edited published posts to make last minute changes. This is okay but BIM's assumptions broke the practice.
    
    BIM does provide students with a way to view BIM's copy of their posts. I believe this feature helps the authors understand that the copy on BIM is different from the version on their blog. Reducing this error.
    
- Allowing students to see their progress.
    
    This week I've sent all students an email with their result. BIM does provide a way for students to see their progress/marks, but with no BIM the first the students knew of what the system knew of them was when their marked assignments were returned. BIM, properly modified for the approach I've used here, would allow the students to see their progress and do away with the need for the email. It would allow the nipping of problems in the bud. Reducing work for me and uncertainty for the students.
    

### Was it a success?

I've been wondering over the recent weeks - especially when I've been in the midst of the extra work that arose from having to fix the above problems - whether it was worth it. Did I make a mistake deciding to go with the blog based assessment for this course in the absence of appropriate tool support. Even if the institution had installed BIM, BIM itself didn't have all the tools to support the approach I've used this semester. BIM would have reduced the workload somewhat, but additional workload would have been there.

Was it worth it was a question I asked myself when it became obvious that at least some (perhaps many) **students did "write for the marks"**. I need to explore this a bit further. But it is obvious that some students made sure they wrote enough to meet the criteria. There was also some level of publishing the necessary posts in the day before the assignment was due. At least some of the students weren't engaging in the true spirit of the assessment. But I don't blame them, there were lots of issues with the implementation of this assessment.

Starting with the absence of BIM which created additional workload which in part contributing to less than appropriate scaffolding to help the students engage in the task more meaningfully. Especially in terms of better linkages to the weekly activities. I'm particularly interested, longer term, in how the assessment of the course and the work done by the markers can be changed from making submitted assignments to actively engaging with students blog posts.

On the plus side, there was **some evidence of serendipity**. The requirement for for students to link to others worked to [create connections](/blog2/2013/06/04/animation-over-time-of-links-between-student-posts/) and at least some of them resulted in beneficial serendipity. There's enough evidence to suggest that this is worthwhile continuing with. There does of course need to be some more formal evaluation and reflection about how to do this, including work on BIM to address some of the problems above.

I've also learnt that **the activity completion report in Moodle is basically useless**. With the number of students I had, the number of activities to complete, and apparently the browser I was using viewing the tabular data in the activity completion report in a meaningful way was almost useless. Downloading the CSV into Excel was only slightly more beneficial. In reality, the data needed to be manipulated into another format to make it useful. Not exactly a report located in "The Performance Zone" talked about at the end of [this post](/blog2/2013/06/07/learning-analytics-intervention-and-helping-teachers/). On the plus side, this is informing some further research.

This whole experience really does reinforce Rushkoff's (p. 128) point about Digital Technology

> Digital technology is programmed. This makes it biased toward those with the capacity to write the code.

Without my background in programming, developing e-learning/web systems and in writing BIM none of the above would have been possible. The flip side of this point is that what is possible when it comes to e-learning within Universities is constrained by the ideas of the people who wrote the code within the various systems Universities have adopted. Importantly, this may well be at least as big a constraint on the quality of University e-learning as the intentions of the teaching staff to use the tools and the readiness of the students to adopt to changes.

### References

Rushkoff, D. (2010). Program or be programmed: Ten commands for a digital age. New York: OR Books.