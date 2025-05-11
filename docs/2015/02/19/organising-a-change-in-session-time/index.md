---
categories:
- edc3100
date: 2015-02-19 07:19:03+10:00
next:
  text: '"Contradictions in adjectives: You can''t be consistent and optimal"'
  url: /blog2/2015/02/25/contradictions-in-adjectives-you-cant-be-consistent-and-optimal/
previous:
  text: Initial rationale and ideas for &quot;continuous improvement&quot; of learning
    and teaching
  url: /blog2/2015/02/18/initial-rationale-and-ideas-for-continuous-improvement-of-learning-and-teaching/
title: Organising a change in session time
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: Peter
      author_email: palbion@me.com
      author_ip: 139.86.2.15
      author_url: http://pamatravel.wordpress.com
      content: 'Your post reminded me that a Moodle message I sent to my Toowoomba group
        on Monday may not have reached them. That message was about arranging a meeting
        during O-Week because I''ll be absent during the first week of classes. I set
        up a schedule of possible times in whenisgood.net to capture student responses
        about availability.
    
    
        I''ve just extracted the text of my message from the message record of one of
        the relevant students in the Moodle participants list and sent that by email using
        the facility in the Faculty Centre of PeopleSoft. That allows me to select all
        or some of the students in a class group (Toowoomba on-campus in this case) and
        send them a group email message.'
      date: '2015-02-19 08:34:23'
      date_gmt: '2015-02-18 22:34:23'
      id: '1228'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: David Jones
      author_email: davidthomjones@gmail.com
      author_ip: 60.231.80.148
      author_url: https://djon.es/blog/
      content: I'd forgotten about the Peoplesoft email feature, I'd just settle for it
        being configured to do its actual job properly. Thanks for sharing your approach,
        a good example of there being more than one way to do any task.
      date: '2015-02-19 10:59:54'
      date_gmt: '2015-02-19 00:59:54'
      id: '1229'
      parent: '1228'
      type: comment
      user_id: '1'
    
pingbacks:
    []
    
---
The next iteration of the ICT and Pedagogy course I teach is about to start. We've struck a small problem with one of the campuses, the person being employed to run sessions on that campus can't make the scheduled time. I need to ask the students when would be the best time to reschedule the session. The following summarises how I'll do this with [Doodle](http://doodle.com/) and various other tools.

I'm posting this on my blog to share what I've learned about this task. Making this explicit illustrates to the folk in the course one way to make use of blogging. Share your learning, no matter how small or simple you may think it. It may also be of use to some of my colleagues at the institution. It's also to help demonstrate a process of creatively combining ICT to help with an aspect of learning/teaching.

Two other important points the following illustrates

1. The digital environment in which teachers (of all types) is littered with [concrete lounges](/blog2/2014/12/18/concrete-lounge/).
2. How we live with those concrete lounges (how we do things with digital technologies) is going to be very different and dependent on our environment, skills, and the available tools (and the affordances we perceive).
    
    I don't there are many people that would have completed this particular task the way I have.
    

The limitation of this example is that it is more a "classroom management" task, rather than a learning/teaching task. A learning/teaching task would involve the application of more pedagogical knowledge in the skills step.

## The TEST framework

Over the last couple of years we've adopted/adapted [Socol's Toolbelt theory and TEST framework](http://speedchange.blogspot.com.au/2011/01/toolbelt-theory-test-and-rti.html) as a way of thinking about this sort of problem. Rachel - a past student - has a post that summarises some of the intent behind this approach.

In figuring out how to do this, I'm going to be thinking about the following

1. Task - what needs to be done?
2. Environment - where must this be done? What are the constraints?
3. Skills - what do I know/have that can be applied to this task.
4. Tools - what tools allow me (with my skills), in the environment I'm in, complete the task?

## Task

Three main steps to this task

1. Inform the students about the need for a change.
2. Gather their responses about which time best suits.
3. Inform them of the chosen time.

In a perfect world, step #2 should also perhaps include the ability for the students to see and perhaps talk about their responses and related factors.

## Environment

This is a course being offered at the institution that employs me. There's a Moodle course site to which the students are enrolled. There are also a few other related tools.

It's still a week and a half from the start of semester. So no face-to-face discussions are possible as the students aren't on campus yet (generally). There will also be the question as to whether the students are checking their institutional email accounts yet. Plus, I'm at another campus.

## Skills

Probably the main relevant skill is some capability to use a range of digital technologies.

## Tools

### Moodle messaging

Moodle will be one. It should have some messaging capability that I can use to contact the students (though of course such contact will be limited to their institution email or any forwards they have set up). Can I find that tool and discover it's affordances?

Nothing is obvious from the institutional Moodle interface. So fall back on Google "moodle messaging" (Of course, I if I wasn't already aware of this feature and this particular term, I'd now officially be in trouble).

That Google search gets me to [the Using Messaging page](https://docs.moodle.org/24/en/Using_Messaging). It appears this is using Moodle "instant messaging", not 100% clear that this will email the students. Ahh, [the FAQ](https://docs.moodle.org/24/en/Messaging_FAQ#When_are_messages_sent_via_email.3F) seems to suggest that messages are only sent as email when the individual have configured their preferences to have messages sent. I wonder whether this can be changed at the institutional level, and whether or not my institution has?

So, not a great fit due to the reliance on students being in Moodle. Can I get a list of student email addresses?

### Student records

The institutional student records system does allow me to download a spreadsheet containing student data. The should have email address as part of it.

Ahh, no. Name, ID number, information about the grading basis for the course (which is all the same for all students at this institution and information I already know, why is that included), program, year level, citizenship status, and a column that contains the word "View Student Details". On the web version this is a link to detailed information about the individual. In the spreadsheet, it's just the word.

Now that's real useful. An example of a [concrete lounge](/blog2/2014/12/18/concrete-lounge/) if I ever saw one.

That spreadsheet seems to be designed as is, rather than for the purposes of teaching staff.

### Moodle participants list

Okay, struggling now. Student email addresses are included in Moodle and visible through the participants lists to teacher. In theory you can choose which groups to view. The groups should include campus. Yes it does.

But it doesn't look like I can download the list of participants to a spreadsheet, or easily extract the email address.

Ahh, and now the super slow response times from Moodle are commencing.

So, my solution is to copy and paste from the HTML page into a text file and use the following ed/vi command (sorry this is really, really nerdy) to extract just the email addresses. \[code lang="sh"\] :.,$s/^.\* (\[^ \]\*)@(\[^ \]\*) .\*$/1@2/ \[/code\]

I can then stick that list of addresses into my mail client and send an email.

### Doodle

I used [Doodle](http://doodle.com/) a couple of years ago. But I couldn't remember the name. So a quick Google for "scheduling meeting" and hey presto, Doodle is the #1 hit I get back. There appear to be others, but I'll stick with what I know.

Doodle is aimed at making the process of scheduling events easy. You can set up an online poll, send people the link, and they make their choice.

I could have done this with the Moodle quiz tool. However, Doodle is quicker to use and also I don't have to add Doodle to the Moodle course site. This could cause some confusion as it's only relevant to a subset of students, but also because doing so would break the design I've used on the course site.

Set up the quiz, time to send the email......there have been 6 responses since the poll was released yesterday afternoon.