---
title: "Does GPA make any difference to #moodle course usage?"
date: 2014-02-20 13:48:53+10:00
categories: ['elearning', 'indicators', 'learninganalytics-elearning']
tags: ['mav']
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: elketeaches
      author_email: elkeclarissa@hotmail.com
      author_ip: 124.189.216.206
      author_url: http://elketeaches.wordpress.com
      content: Interesting data
      date: '2014-02-21 06:11:14'
      date_gmt: '2014-02-20 20:11:14'
      id: '960'
      parent: '0'
      type: comment
      user_id: '0'
    
pingbacks:
    []
    
---
## Summary

In short, there is definitely a pattern. In fact, there are two patterns evident:

1. Students in higher GPA groups click on a range of different activities and resources at much higher rates than those in lower GPA groups.
2. A greater percentage of students in higher GPA groups will click on resources.

There are a few exceptions to this. Another less explored pattern is a drop off in usage as the semester progresses.

This is in the context of a single offering of a course I teach with all students (n=~100) enrolled as online students.

The pattern seems to exist across different types of resources from across the semester. Though there does appear to be a drop off toward the end of semester.

This aligns with findings from prior work such as Dawson et al (2008) and Beer et al (2009).

My next step is to see what reaction presenting this pattern to the next crop of students will have.

## Origins

In just over a week a new semester starts. Institutional requirements mean that course sites need to be available 2 weeks prior to the start of semester. Consequently there's already been some activity on the new site for the course I teach. In response, I observed

<blockquote class="twitter-tweet" lang="en"><p>2 weeks before semester start. Course sites available and the first keen <a href="https://twitter.com/search?q=%23edc3100&amp;src=hash">#edc3100</a> student engaging. Hope it’s a good sign.</p>— David Jones (@djplaner) <a href="https://twitter.com/djplaner/statuses/435214458500030464">February 17, 2014</a></blockquote>

To which @s\_palm replied

<blockquote class="twitter-tweet" lang="en"><p><a href="https://twitter.com/djplaner">@djplaner</a> By and large, it's the ones that aren't so keen that you need to worry about.</p>— Stuart Palmer (@s_palm) <a href="https://twitter.com/s_palm/statuses/435215401924849664">February 17, 2014</a></blockquote>

Which got me wondering. Is there a link between accessing the course site and GPA? Do "good" students use the LMS more? What happens if students are aware of this pattern?

With the [Moodle Activity Viewer installed](/blog2/2014/02/02/moodle-activity-viewer-mav-and-the-promise-for-bricolage/), I have one way to explore the usage question for a past course site. To be clear

1. This is just an initial look to see if there are any obvious patterns.
2. As @s\_palm has pointed out https://twitter.com/s\_palm/status/436287172358836224

To test this, I'm going to

1. Create some new groups on my old Moodle course site based on student GPA.
    
    I could also do this based on the final grade in this course, might be an interesting comparison.
    
    Glad I had access to the database, creating these groups through the Moodle interface would have been painful.
    
2. I can then use MAV's "select a group" feature to view how they've accessed the course site.
    
    MAV will show the number of clicks or number of students who have visited every link on a Moodle course site. I don't expect the number of students to reveal too much - at least not on the home page - as completing activities/resources is part of the assessment. Comparing the number of links is not going to be straight forward given the different numbers in each group (and MAV not offering anyway to normalise this).
    

## Explanation of the "analysis"

The quick and dirty comparison is between the following groups

- 6 GPA (n=11) - all students with a GPA of 6 or above.
- 5 GPA (n=49) - all students with a GPA of above 5, but less than 6.
- 4 GPA (n=35) - GPA above 4, but less than 5.
- Less than 4 GPA (n=28) - the remaining students, apart from a handful with a GPA of 0 (exemptions?)

The analysis will compare two usage "indicators" for a range of course resources/activities.

The "indicators" being compared are

- Clicks / Students - the total number of clicks on the resource/activity by all students in a group divided by the number of students in the group.
- Percentage - the percentage of students in that group who clicked on the activity/resource.

## Assessment and Study Schedule

The first resources compared are

- Assessment - a Moodle book that contains all details of the assessment for the course.
- Study Schedule - a page that gives an overall picture of the schedule of the course with links to each week's block.

| Group | Clicks / Student | % Students |
| --- | --- | --- |
| Study Schedule |  |  |
| 6 GPA | 4.2 | 100.0 |
| 5 GPA | 2.9 | 75.5 |
| 4 GPA | 2.8 | 74.3 |
| Less than 4 | 1.3 | 53.6 |
| Assessment |  |  |
| 6 GPA | 22.7 | 100.0 |
| 5 GPA | 12.2 | 75.5 |
| 4 GPA | 11.0 | 74.3 |
| Less than 4 | 8.2 | 64.3 |

The pattern is established early. The higher GPA groups access these resources more.

Unsurprisingly, the assessment information is used more than the study schedule.

## Forums

Next comparison is two forums. Each assignment has it's own forum. There is a general discussion forum. Finally, there are a range of forums used for specific learning activities during the semester. The two forums being compared here are

- Q&A forum - is a forum for general questions and discussion.
- Assignment 3 and Professional Experience Forum - assignment 3 is wrapped around the students' 3 weeks practical teaching period.

| Group | Clicks / Student | % Students |
| --- | --- | --- |
| Q&A Forum |  |  |
| 6 GPA | 19.3 | 90.9 |
| 5 GPA | 7.9 | 65.3 |
| 4 GPA | 7.3 | 54.3 |
| Less than 4 | 1.6 | 35.7 |
| A3 and PE forum |  |  |
| 6 GPA | 16.0 | 100.0 |
| 5 GPA | 8.4 | 73.5 |
| 4 GPA | 5.5 | 68.6 |
| Less than 4 | 1.2 | 35.7 |

The pattern continues. Particularly troubling is the significant reduction in use of the forums by the "Less than 4 GPA" group. Only about a third of them use the forums as opposed to over half accessing the study schedule and even more accessing the assessment.

I wonder how much of this percentage difference is due to students who have dropped out early?

## Week 1 activities

In week 1 of the semester the students have to undertake a range of activities including the three compared here

- Register their blog - they are required to create and use a personal blog throughout the semester. This activity has them register and be able to view the registered blogs of other students.
- Share introductions - post an introduction of themselves and look at others. An activity that has been [recently revisited](/blog2/2014/02/18/looking-for-a-new-icebreaker-for-edc3100/) for the coming semester.
- PKM and reflection - a Moodle book introducing Personal Knowledge Management and reflection through a range of external resources. These two processes are positioned as key to the students' learning in the course.

| Group | Clicks / Student | % Students |
| --- | --- | --- |
| Register your blog |  |  |
| 6 GPA | 12.9 | 100.0 |
| 5 GPA | 9.2 | 75.5 |
| 4 GPA | 10.8 | 77.1 |
| Less than 4 | 6.6 | 60.7   |
| Share introductions forum |  |  |
| 6 GPA | 6.6 | 100.0 |
| 5 GPA | 4.6 | 75.5 |
| 4 GPA | 5.6 | 77.1 |
| Less than 4 | 2.2 | 57.1   |
| PKM and reflection |  |  |
| 6 GPA | 3.8 | 100.0 |
| 5 GPA | 2.3 | 75.5 |
| 4 GPA | 2.1 | 74.3 |
| Less than 4 | 1.4 | 53.6 |

Generally the pattern continues. The "4 GPA" group bucks this trend with the "Register your blog" activity. This generates at least two questions

- Are the increased clicks / students due to troubles understanding the requirements?
- Or is it due to wanting to explore the blogs of others?

Given that the percentage of students in the "4 GPA" group also bucks the trend, it might be the former.

## Late semester resources

Finally, three resources from much later in the semester to explore how folk are keeping up. The three resources are

- Overview and expectations - a Moodle book outlining what is expected of the students when they head out on their Professional Experience. There is still four weeks of theory left in the course, followed by 3 weeks of Professional Experience.
- Your two interesting points - a Moodle forum in the last week of new content. The last week before the students go on Professional Experience. The students are asked to share in this forum the two points that resonated most with them from the previous reading that was made up reflections of prior students about Professional Experience.
- Pragmatic advice on assignment 3 - another Moodle book with fairly specific advice about how to prepare and complete the 3rd assignment (should generate some interest, you'd think).

| Group | Clicks / Student | % Students |
| --- | --- | --- |
| Overview and expectations |  |  |
| 6 GPA | 1.7 | 90.9 |
| 5 GPA | 2.4 | 75.5 |
| 4 GPA | 1.6 | 65.7 |
| Less than 4 | 0.8 | 50.0 |
| Your two interesting points |  |  |
| 6 GPA | 1.2 | 63.6 |
| 5 GPA | 1.0 | 55.1 |
| 4 GPA | 0.6 | 34.3 |
| Less than 4 | 0.2 | 14.3 |
| Pragmatic A3 advice |  |  |
| 6 GPA | 1.5 | 90.9 |
| 5 GPA | 1.4 | 73.5 |
| 4 GPA | 1.0 | 60.0 |
| Less than 4 | 0.6 | 42.9 |

The established pattern linking GPA with usage largely remains. However, the "5 GPA" students buck that pattern with the "Overview and Expectations" book. The "gap" between the top group and the others is also much lower with the other two resources (0.2 and 0.1 click / student) compared to some much larger margins with earlier resources.

There is also a drop off in groups toward the end of semester as shown in the following table comparing the main Assesment link with the pragmatic A3 advice.

| Group | Assessment |  | Prag A3 advice |  |
| --- | --- | --- | --- | --- |
|   | C / S | % studs | C / S | % studs |
| 6 GPA | 22.7 | 100.0 | 1.5 | 90.9 |
| 5 GPA | 12.2 | 75.5 | 1.4 | 73.5 |
| 4 GPA | 11.0 | 74.3 | 1.0 | 60.0 |
| Less than 4 | 8.2 | 64.3 | 0.6 | 42.9 |

Some "warnings". The 10% drop for the "6 GPA" group represents 1 student. There's a chance that by the end of semester, the students have worked out they can print out a Moodle book (can be used to produce a PDF). So they visit it, save the PDF and refer to that. This might explain the drop off in clicks / students.

## References

Beer, C., Jones, D., & Clark, K. (2009). The indicators project identifying effective learning, adoption, activity, grades and external factors. Same places, different spaces. Proceedings ascilite Auckland 2009. Auckland, New Zealand. Retrieved from http://www.ascilite.org.au/conferences/auckland09/procs/beer.pdf

Dawson, S., McWilliam, E., & Tan, J. P. L. (2008). Teaching smarter: How mining ICT data can inform and improve learning and teaching practice. Melbourne. Retrieved from http://www.ascilite.org.au/conferences/melbourne08/procs/dawson.pdf