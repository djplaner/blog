---
categories:
- edc3100
date: 2014-02-03 15:22:35+10:00
next:
  text: Identifying some immediate changes to BIM
  url: /blog/2014/02/05/identifying-some-immediate-changes-to-bim/
previous:
  text: 'MAV, #moodle, process analytics and how I&#039;m an idiot'
  url: /blog/2014/02/03/mav-moodle-process-analytics-and-im-an-idiot/
tags:
- mav
title: Analysing EDC3100 using MAV
type: post
template: blog-post.html
---
Now that I have the [Moodle Activity Viewer (MAV)](/blog/2014/02/02/moodle-activity-viewer-mav-and-the-promise-for-bricolage/) working, I can [continue the analysis](/blog/2014/01/22/what-should-be-covered-in-edc3100/) of the course I teach, [EDC3100, ICTs and Pedagogy](http://www.usq.edu.au/course/synopses/2014/EDC3100.html). This post documents some reflections on the existing collection of activities and resources in the course informed somewhat by the insights provided by MAV.

[This rather long image](http://www.flickr.com/photos/david_jones/12259871663/sizes/o/) shows MAV's modification of the semester 1 course site for EDC3100. In the following I'll be focusing on the Semester 2 offering as its the latest and greatest version. The shortcoming of analysing this offering is that it's only taken by on-campus students.

I've only completed the first 2 weeks, I'll update this post as I work through the other weeks.

## Some additional background

91 students completed all of the assessment. Another 9 students did not complete the course. In the following I'll assume 91 as representing 100% of students.

The semester 2 course is divided into a structure similar to [what's shown in the S1 image](http://www.flickr.com/photos/david_jones/12259871663/sizes/o/) i.e.

1. Top of the course site divided into some generic links/information, an image that changes weekly, and direct links to the discussion forums.
2. Each topic/module of the course equates to a week of semester.
3. There's a navigation bar at the top to help students go straight to a particular week.

Completion of the all the provided activities and resources forms a small part of the assessment of the course, so I expect most students to have used most of the weekly activities and resources.

## Some user feedback on MAV

Misc. feedback/ideas on using MAV that have arisen during the following analysis

- Keeping MAV configuration specific to the browser window?
    
    In the following, I wanted to explore both the number of clicks and the number of students using each resource. I had two windows open, one configured to show clicks, one to show students. The problem is when I reloaded a page or visited another, MAV would use the configuration settings most recently set.
    
- And/Or, Having the MAV configuration link appear on all pages OR add it to the heat map legend.
    
    I know this is difficult. But part of the problem is when I'm viewing a book or a forum, I want to be able to switch between students/clicks. Perhaps the better solution is to add the configuration link to the heatmap legend.
    
- What's the relationship between all links associated with a resource/activity?
    
    e.g. let's say I have a Moodle book. There's one link into the book on the course page, but there are numerous links within the book. Going between different pages, chapters and also using various services (e.g. print the book).
    
    MAV shows some stats on the course page, what does these stats show? The total number of all usages of that resource, including all the internal links? Or, as I suspect, just the stats for that particular link? How might this influence usage? What happens if the students book mark a particular page within the book and use that?
    
- Would be useful to have heat maps generated based on activity completion - so I could see who has/hasn't at a glance.
- Have a roll over that reveals students who haven't completed/clicked on an activity/resource
- The idea of an abstract model for the MAV communication enabling a range of pluggable modules.
- Identifying the "geology" (as in [data geology, rather than data mining](http://dougclow.org/2013/04/08/lak13-monday-morning-discourse-centric-learning-analytics/)) for different pages.
- Having the groups work as either Union or Intersection.
    
    e.g. have groups based on a students GPA and groups based on their mode of study is a context where it would be useful to have an intersection of the two groups. i.e. all of the "6 GPA" + Online students.
    
- Adding the values "Clicks / student" and "% students" rather than just the raw counts.
    
    Allows slightly more valid comparisons between groups.
    
- The option to produce spreadsheets with the raw data to enable analysis.

## Top of the course

MAV only appears to pick up the normal Moodle links (those created when you add an activity or resource), many of the links in this section are manually entered into HTML so no immediate insight into their usage.

For the discussion forums, MAV reports

- News forum - announcements from me - 495 clicks by 62 students.
- General Q&A forum - 977 clicks from 76 students.
- Assignment 1 forum - 774 clicks from 92 students.
- Assignment 2 forum - 599 clicks from 86 students.
- Assignment 3 forum - 949 clicks from 86 students.

Given 100 students enrolled in the course at the end of semester, I wonder if the 8 students who didn't use the assignment 1 forum are those that didn't complete the course. Similarly, I wonder about the 5 students who didn't access the assignment 2 and 3 forums, did they pass the course? How well did they do?

The drop in use of the Assignment 2 forum is not a big surprise. Assignment 3 is directly tied to students going into schools to teach, this focused the mind somewhat. Assignment 1 has them creating an online artefact and is quite challenging. There are also queries about blogs and requirements. Would be useful to check these assumptions.

Can also grab stats for some of the other links (mostly "hidden" resources) via other means

- Study Schedule - Page (340 clicks, 93 students)
- Assessment - Book (1559 clicks, 97 students)
    
    A Moodle book containing all the assessment details for the course. Not surprising that it's one of the more heavily used resources/links.
    
    A nice thing about MAV is that it also produces the same "heat map" display on all links on all Moodle pages. e.g. if I click into this Moodle book I can then see all the other clicks that students have made within this book. For example, there are three separate pages for each assignment with the following stats: assignment 1 (741 clicks, 97 students), assignment 2 (755 clicks, 97 students), assignment 3 (848 clicks, 97 students)
    
- Professional Experience - Page (701 clicks, 94 students)
- On-campus material - Book (146 clicks, 59 students)
    
    This book contained recordings of on-campus lectures from S1. Doesn't appear to be heavily used. Do we need it?
    
- Meet the teaching team - Page (155 clicks, 95 students)
    
    Would appear they used it once at the start of semester, but were fine without it from then on. Is this the case? Should this stay here?
    
- Professional experience slides - File (64 clicks, 50 students)
    
    Powerpoint provided by others meant to summarise requirements for PE. Interestingly, amongst the lowest used resource.
    

Further questions/tasks

1. Can I get usage figures for the weekly navigation links?
2. Can I get usage figures for the Course Content block?
3. Are the at least 8 students who didn't visit the Assignment 1 forum those that ended up not completing the course?
4. Who and what happened to the 5 students who didn't access the assignment 2 or 3 discussion forums?
5. Can the weekly image be incorporated into each week's section?
6. Let the PE office know about the usage of the slides?
7. Are the 97 students who viewed the assessment book the core group? What happened to the apparent 6 students who looked at the assessment page, but didn't complete the course? Are there any students who passed the course who didn't look at the assessment page? What about the at least 3 students who did not look at the assessment page and failed the course?

## Course overview

This is intended as an orientation to the course. To be completed during O-Week. I don't necessarily expect all students to have completed these. It's not required.

Contents include the following (the word - e.g. Page - after the name of the activity/resource is the Moodle name for the type of activity/resource)

- Welcome to the course - Page 139 clicks, 91 students
    
    A bit of text and a pointer to a Vimeo video (lecture). Vimeo stats reveal 304 plays, but I believe I used this same video in S1. Vimeo reveals a peak of 26 and 28 views per week in July 2013. About the time S2 was getting underway. The content is not that useful. Limited in scope due to S1 implementation and not much being known about the course.
    
- How will the study desk be used this semester? - Page 130 clicks, 94 students
    
    Another page with some vimeo videos. Giving an overview of the study desk, it's construction and how it will work. Jesus the narration is crappy. Vimeo reveals 255 plays
    
- About the pedagogy used in this course - Page 152 clicks, 90 students
    
    Another brief page with a link to a YouTube video on the networked student. Need to link some of this more explicitly to the activities, assessments etc in the course.
    
- Meet the teaching team - Page - 155 clicks, 95 students
    
    Brief bio, photo and contact details for the staff.
    
- What you should do to prepare for this course - Page 166 clicks, 93 students.
    
    Four other tasks students should complete - blue card etc.
    

Further questions/tasks

1. All around the 90-95 student mark, was there any commonality in the students who didn't access this material? What happened to them in the course?
2. **S1, 2014** - redo the introductory video.
3. **S1, 2014** - redo the study desk video.
4. **S1, 2014** - link the "pedagogy" page more to what students will do in the course.
5. **S1, 2014** - Make a stronger case for the assumptions underpinning the design of the course (yea, they'll all read that!).
6. **S1, 2014** - make explicit connections to various professional standards etc.
7. **S1, 2014** - encourage students - where appropriate to get into the learning place?

## Week 1 - ICTs, PLNs and You

- Getting started

    - Introduction to the week - Page (177 clicks, 94 students)
        
        Simple intro
        
    - Setting up your tools: Diigo, a blog and Twitter Book (509 clicks, 97 students)
        
        4 page book outlining the tools that students will use during the semester for their learning: Diigo (452 clicks, 97 students), a blog (350 clicks, 97 students) and Twitter (158 clicks, 93 students). Interesting to see that the explicit "optional" tag for Twitter appears to have had an impact.
        
    - Register your blog Database (1211 clicks, 97 students)
        
        Where the students register their blog and also how they can view what other blogs are registered (encouraged to do this). Good to see that the clicks suggest that they were coming back to this. May hopefully be replaced by BIM.
        
    - Introduce yourself Book (384 clicks, 96 students)
        
        3 page block explaining the "intro" activity. 2nd page (280 clicks, 95 students), 3rd page (141 clicks, 94 students). Why the 140 click difference, but only 1 student? Were the instructions that difficult?
        
    - Share your introductions Forum (574 clicks, 96 students)
    
    Where the students are meant to post their introductions. This is where MAV is particularly interesting, so much so it sparked [another blog post](/blog/2014/02/03/mav-moodle-process-analytics-and-im-an-idiot/). In short, I need to revisit this activity.
    
- Overwhelmed? Toolbelt theory, PKM and reflection
    - PKM and Reflection Book (285 clicks, 94 students)
        
        5 page book introducing the core of what the students should be doing this semester. There is a drop off in clicks with each of the pages, but all 94 students visited each page. Suggesting that the PKM (332 clicks) is something students are coming back to. While at the other extreme "Using Theories" (196 clicks) is not.
        
    - Toolbelt theory Book (350 clicks, 94 students)
        
        11 page book (some of the pages in these books are a couple of paragraphs) introducing Toolbelt theory. i.e. trying to get students to actively engage with how ICTs are just tools that can help them solve problems. Applies this first to their own pracitce (e.g. Google scholar and the USQ library). Also introduces Diigo and has the students use this to annotate @irasocol's toolbelt theory blog post.
        
        Usage of the pages of the book trail off. 94 students down to 90 in the middle. 366 clicks down to 153 clicks. This is perhaps suggesting that Moodle's activity completion may be too straight forward for the Moodle book.
        
    - Seek, Sense, Feeds, Feed readers and blog posts Book (352 clicks, 89 students)
        
        7 page book getting students into using Feedly and following the blogs of other students. Decrease from 91 students down to 87 and 402 clicks down to 141.
        
- ICTs and Conclusions
    - What are ICTs? Book (276 clicks, 93 students)
        
        5 page book trying to get the students to identify what ICTs are. Going more broadly than computers. Includes a reading, a video and a "what have you used" question.
        
        93 students down to 90.
        
    - What ICTs did you see in Hello Kitty? Forum (308 clicks, 90 students)
        
        Students are asked to identify a list of all the ICTs they say in a "Hello kitty in space" video. A Moodle Q&A forum, they can't see the responses of others until they've shared their own.
        
        89 students, 93 replies and 406 clicks - will be interesting to explore this further - the difference between the different types of forum.
        
    - Finishing up for the week Book (274 clicks, 91 students)
        
        Mish mash of 4 page book. "Why would you use ICTs" a link to Assignment 1 and encouraging the students to think about why they would use ICTs. Encouragement to seek, sense, share and encouraging them to record all the ICTs they see as the semester progress. Lastly, get them to reflect on where they are up to using a frameworks of ICT usage.
        
        92 down to 91. 186 clicks down to 158.
        
    - How are you going with the course? Page (137 clicks, 90 students)
        
        A moodle page with a link to a course barometer.
        

Further questions/tasks

- **S1, 2014** Should we drop the mention of Twitter being optional. Don't make it part of assessment, but don't suggest it's optional?
- **S1, 2014** Will/can the register blog database be replaced with BIM?
- **S1, 2014** Redesign the introduction forum activity to encourage more connections between students (none really happening at the moment).
- Think about how PKM can be used to better scaffold blog posts etc.
- Explore if the Moodle activity completion for a book only requires clicking on the initial book, not reading all of the pages.
- **S1, 2014** Modify the Feeds and Feedly book based on whether BIM is used. Consider also whether this might be combined with the "introduction" activity.
- **S1, 2014** Reconsider the reading for the "What are ICTs" section to find something that engages with broader categories, is less academic and has more scope for creativity (easy right?).
- Do the different types of Moodle forums (different pedagogical intent usually) show different usage patterns?
- **S1, 2014** Can the "Where are you situated" query be moved to before the introduction and then integrated into it?
- **S1, 2014** The "why use ICTs" can perhaps be expanded?
- **S1, 2014** Can an activity be added to "seek/sense/share" an explicit prompt?
- **S1, 2014** Update the course barometer page with results from last year - perhaps do a comparison between the various offerings?

## Week 2 - ICTs and Pedagogy

- Getting started
    - Register for Scootle - Page (191 clicks, 93 students)
        
        Getting the students to register for Scootle.
        
    - Introducing week 2 - Book (198 clicks, 91 students)
        
        3 page book explaining the week. Includes them selecting a mind mapping tool that they'll use during the week. Fairly consistent usage, the mind map page has more clicks.
        
- ICTs and Change
    - Examples of how the world is changing - Book (205 clicks, 92 students)
        
        4 page book showing off various "did you know" type videos illustrating how the world has changed, in part due to ICTs.
        
    - Understanding technological change - a first step - Book (409 clicks, 93 students)
        
        8 page book with an activity based around Postman's 5 things to know about technology.
        
        Clicks down from 394 to 292. 91 students down to 89.
        
    - Examples of Postman's five things we need to know. - Forum (369 clicks, 91 students)
        
        Forum where students' share their examples of personal experience of one of Postman's 5 things.
        
        Students do tend to be sprinkled across the different "things". Not a lot of checking out the other "things". Students also tending to start their own threads which tends to dilute things.
        
- What is "ICTs and Pedagogy"?
    - The importance of pedagogy - Book (198 clicks, 93 students)
        
        6 page book aimed at some high level points about using ICTs and pedagogy. e.g. [this cartoon](http://doug-johnson.squarespace.com/storage/blended_cartoon.jpg), definition of pedagogy. No drop off in students. Some drop off in clicks. What is pedagogy gets the most!.
        
        Leads to an activity where the students are asked to share a pedagogical technique that they are aware of.
        
    - What is "pedagogy" in your teaching area? - Forum (249 clicks, 90 students)
        
        A forum where the students share their pedagogical knowledge as asked in the last book.
        
        Similar patterns to other forums. Lots of threads. Limited reading of other people's posts.
        
    - Approaches to ICTs for Learning - Book (344 clicks, 92 students)
        
        1 page book asking students to read and then share one example of ICT usage from the Luckin report.
        
    - Examples of ICTs for learning - Forum (342 clicks, 88 students)
        
        Forum with fixed number of threads. Where students have to share their example ICT usage from the previous book.
        
        Somewhat better replies/students ratio. 7 replies/24 students clicking on it. 26 replies/47 students. This is interesting. Suggests students are perhaps finding this useful or valuable.
        
    - ICTs and the Curriculum - Why and Digital Resources - Book (252 clicks, 91 students)
        
        Three page book linking with the Melbourne Declaration, Australian Curriculum and Scootle. They have to find a useful resource on Scootle as part of this book.
        
        Consistent use through out. Practical relevance?
        
    - Share your Scootle Resources - Forum (313 clicks, 84 students)
        
        Forum where students are asked to share the Scootle resource they found.
        
        Similar usage patterns to the introduction forum. Very similar.
        
- Assignment 1, Connections and Conclusions
    - Your online artefact - Assignment 1, Part 2 - Book (277 clicks, 92 students)
        
        4 page book looking at A1 questions. Drop off in clicks, but not students.
        
    - One process for planning an online artefact. - Book (247 clicks, 91 students)
        
        Example of creating an online artefact. Big drop off in clicks 247 down to 135. 91 to 87 students.
        
    - Following EDC3100 blog posts - Book (157 clicks, 87 students)
        
        More about following blog posts of other students.
        
    - Share your concept map - Forum (267 clicks, 70 students)
        
        Forum where students share their concept map. Each thread has more people looking at them. Tied to assignment, so students see value in checking out what others are thinking.
        
    - What's next? - Page (118 clicks, 86 students)
        
        Single page finishing up for the week. Another barometer.
        

Further questions and tasks

1. **S1, 2014** Should the Scootle registration be moved into the orientation/week 1 activities?
2. **S1, 2014** The last page of the "Examples" book needs to be updated to give some background on the apocryphal nature of the quotes used in the "What if?" video. Use this to lead into the whole "don't trust everything" I tell you spiel. Lead into mention of learning styles?
3. **S1, 2014** Design a better activity around Postman's 5 things. Some aims include: bringing considerations back to ICTs and Pedagogy; having students look at other "things"; and, having more checks on people's understandings of the "things". e.g. have the students respond to a post in another "thing" and comment on it.
4. **S1, 2014** Can the "how you use it that counts" page have an activity added to encourage the students to identify areas of their pedagogy that can be improved?
5. **S1, 2014** Extend the "sharing" pedagogy activity by asking students to find a technique offered by someone else and to suggest how ICTs might be used to help/modify it? Or perhaps combine it with the Luckin reading, e.g. connect one example/theme from Luckin with the pedagogy shared by another student.
6. Are the ratios of reply/student clicking reply/clicks potential indicators of a good/sharing discussion forum? Relationship with SNA?
7. Investigate why the ratio for the "Examples of ICTs" forum are better than others.
8. **S1, 2014** link the Melbourne Declaration - creative/productive use of ICTs to the toolbelt theory idea. Perhaps use this as a spark to do a @courosa lip-dub project. The lip dub idea could link to assignment 1 and artefact creation.
9. **S1, 2014** rework the share a Scootle resource forum. Maybe this becomes a resource to use in a later week. i.e. find someone else's resource and evaluate it with SAMR. Could do this via a Google spreadsheet/Moodle database?
10. **S1, 2014** move the "Following blog posts" to first week.
11. **S1, 2014** Fix spelling of "your" in concept map forum name. Think about re-design of this.

## Week 3 - Building your TPACK

- Getting started
    - It's not the technology, it's how you use it - Book (212 clicks, 92 students)
        
        5 page book, tail wagging the dog, law of instrument, edudoggy and redbubble. Essentially trying to make students aware of some of the limitations of how people think about technology.
        
        212 down to 169 clicks, maintain student numbers.
        
        Some of this is an introduction to this week. Much of this is the use of quotes and phrases to push a perspective, there's nothing in terms of activities to reinforce the point or even connect it to the student. It points to some articles about iPads, but doesn't have an activity around it. The RedBubble activity is almost an after thought - and doesn't require the students to share it.
        
    - Using and growing your PLN Book (217 clicks, 92 students)
        
        8 page book involving the weather photo activity and encouraging students to build their PLN. The weather photo activity links with a later cyber-safety activity. Is also used to talk about digital photography
        
        217 down to 128 clicks. 92 down to 91 students.
        
        Not much in the way of encouraging connections between students.
        
- More reasons for using ICTs
    - TPACK and SAMR - some models Book (284 clicks, 92 students)
        
        5 page book. Simple intros to TPACK and SAMR.
        
        284 down to 187 clicks.
        
        TPACK quote includes emphasis on "nexus of standards-based curriculum requirements, effective pedagogical practices, and available technologies' affordances and constraints". But doesn't go into detail about what these are. I'm not sure many students connect these terms with stuff that impacts them. Especially affordances.
        
        Again this book doesn't require the students to share their understandings of these concepts.
        
    - The ICT general capability and you Book (201 clicks, 90 students)
        
        9 page book covering the use of online resources, a touch of digital citizenship, the ICT capability in the Australian Curriculum and referencing requirements.
        
        201 clicks down to 127; 91 down to 83 students.
        
        Again, not many of these activities are getting the students to produce things in the open or make connections.
        
- Finishing up
    - Some general advice on assignment 1 Book (293 clicks, 91 students)
        
        6 page book on assignment 1, not surprisingly, used slightly more.
        

Further tasks/questions

- Why the drop off in students for the latter resources? What happened to those students?
- **S1, 2014** The initial book "It's not the technology" needs to include some activities/a redesign that helps the students.
- **S1, 2014** The TPACK/SAMR book needs to improved through the addition of exercises/activities that engage the students with the readings/videos/concepts. In particular, connect the students back to their example from the decoding learning report and get them to explicate the TPACK connections and perhaps do similar with SAMR. Alternatively, get them to do this with someone else's example.
- **S1, 2014** Start the TPACK/SAMR book with the mathematical imagery trainer video or some other concrete example.
- **S1, 2014** The idea of having them find a buddy to work with, not a strong group thing and perhaps only for specific weeks. Perhaps a random allocation? Do I want to bother?
- **S1, 2014** Strengthen the link with A1 from the "ICT general capability" book. Emphasise that the embedding the use of ICTs is also aimed at improving learning. Have some sort of Google spreadsheet/form where students grade their capability against the organising elements of the Oz curriculum
- **S1, 2014** Is there a link between the "referencing requirements for Assignment 1" in the "ICT general capabilty" book and assignment 1. i.e. include the requirements in the assignment page.
- **S1, 2014** The idea of each week having a "PLN"/regular tasks page that prompts students for engaging on their blog.
- **S1, 2014** Any good S2 assignment 1s to add to the samples?
- **S1, 2014** "The reasons" page from the assignment 1 book will need to be updated if I change the purpose of assignment 1.

## Week 4 - Effective planning

Apparently, An overview of unit planning and developing the context, stage 1 (learning constructs, essential questions) and part of stage 2 (assessment criteria) of your unit.

- Setting the scene
    - An EduDoggy reminder - Book (190 clicks, 91 students)
        
        3 page book. Draw a stickman, reading about what is success with ICTs in L&T.
        
    - How will you measure the success of ICT integration into your teaching? - Forum (193 clicks, 89 students)
        
        Students asked to post how they will measure success.
        
        One thread, 87 students made 339 clicks. Q&A forum, so couldn't see what others had posted, until they posted.
        
    - Introducing Module 2 Book (206 clicks, 91 students)
        
        6 page book, introducing the new module and assignment 2.
        
        Max 318 clicks on the sample assignments page, down to 143.
        
- First steps in planning your Unit of Work
    - Alignment and planning Book (215 clicks, 89 students)
        
        5 page book - backwards design etc.
        
        215 down to 158 clicks. Not much in the way of activity - is that next?
        
    - Getting started on your Unit of Work Book (271 clicks, 90 students)
        
        6 page book leading through the backwards design process.
        
        271 down to 152 clicks.
        
- Curriculum + Assessment
    - Content Descriptors and Learning Constructs Book (211 clicks, 90 students)
        
        4 page book. Identifying learning objectives for the UoW
        
    - Sharing "constructing knowledge" and "transforming knowledge" constructs Forum (286 clicks, 85 students)
        
        Students share a constructing and a transforming objective for their UoW.
        
        A few more students haven't done this task. There is a bit of looking at others. Again the assessment influence.
        
    - Australian Curriculum, ICTs and other resources Book (152 clicks, 90 students)
        
        4 page book on the Oz Curriculum. Fairly low clickage.
        
        Does it make sense for this to be here, after the last one? Is this really just about ICTs?
        
    - Finding your assessment criteria Book (184 clicks, 90 students)
        
        7 page book identifying the assessment criteria and rubric elements.
        
        Need to get the students to do something here.
        

Further work

- Student numbers per resource down from 92 to 91 (max) and go as low as 85. Who are the students not completing why? Assignment 1 is due around now, are these the students who have stopped already?
- **S1, 2014** Update "Draw a stickman" from "An Edudoggy reminder" for the new semester. More stuff around the text.
- **S1, 2014** "Introducing Module 2" - update "changes in assignment 2" on the intro page.
- **S1, 2014** Any good S2, 2013 assignment 2s to add?
- **S1, 2014** Rather than have the learning journals based on posts made during particular weeks, have them based on particular questions. Or allow the students to nominate the week that they are for? i.e. multiple posts per question.
- **S1, 2014** Link back to sample unit plans on the "Desired Results" page of the "Getting started on your UoW" book - and in other parts in this book
- **S1, 2014** Think about more activities for the UoW book that encourages connection/sharing?
- **S1, 2014** What about a self-marked quiz for students to test their understanding of constructing versus transforming objectives? Perhaps as a Q&A forum?
- **S1, 2014** The "Finding objectives" page needs to connect learning objectives back to driving questions and identifying an interesting unit.
- **S1, 2014** Should the "Oz Curriculum" book be earlier? How do students find the learning objectives without some of this guidance?
- **S1, 2014** SHould be more mention of ideas linking ICTs to learninig objectives, the Oz Curriculum, the general capability and more. Need to get the students thinking more about how they'll use ICTs. Link to TPACK - finding literature about the content area, also SAMR when analysing particular examples.
- **S1, 2014** Add an activity where the students have to establish a criteria for one of their selected learning objectives.

## Week 5 - Developing your learning plan

- Setting the scene
    - Where are we? Where are we going? Book (167 clicks, 92 students)
        
        2 page book - introduction/revision
        
    - Khan Academy and PCK Book (257 clicks, 91 students)
        
        Using Khan Academy to illustrate the PCK problem. i.e. Khan's videos aren't as good because he has less PCK.
        
        1 student drops off.
        
    - A little quiz (231 clicks, 88 students)
        
        A 3 question mathematics quiz testing simple math misconceptions. Of which less 50% of the S2 students got correct.
        
- Designing and sequencing learning experiences
- Learning experiences Book (247 clicks, 92 students)
    
    9 page book focused on helping the students develop learning experiences with ICTs embedded.
    
    247 down to 138 clicks. Down to 91 students
    
    Links back to sample assignments, discusses what a learning experience is. Two main parts? 1) Understand what is required for the unit plan. 2) Design good learning experiences.
    
- Sequencing learning experiences Book (173 clicks, 91 students)
    
    5 page book about sequencing learning experiences.
    
    Clicks drop away to 119.
    
    Mentions DoL and others.
    

- Additional material
    
    These are both "lectures" recorded by another member of staff.
    
    Originally used in the S1 offering, these don't seem to be as required now that the rest of the resources are up and going. Definite drop off in usage. Though might be some repeats
    
    - EDC3100 Module 2 Week 5 Lecture File (41 clicks, 31 students)
        
    - EDC3100 Module 2 Week 5 Tutorial File (20 clicks, 18 students)
- Finishing up for the week
    - How are you going with the course? Page (97 clicks)
        
        Link to the course barometer for this week.
        

Further work

- **S1, 2014** - fix the type in the topic heading.
- **S1, 2014** - fix up the phrasing on "The flipped classroom" from "Khan Academy". Generally needs some improvement. Also fix up the heading for the quiz activity on "A quick quiz"
- **S1, 2014** - look at using the results from "A little quiz" in activities around assessment and reporting and data manipulation. _some of this is done in the "Where are we and where are we going" book from Week 6_
- **S1, 2014** - add a summary and discussion of the results from prior results to "A little quiz" into the "Khan academy" book. This section of PCK needs to be improved and linked better with the reading.
- **S1, 2014** - Check and harvest the stuff tagged with PCK CONTENT on the diigo group and integrate it back into the materials - actually it's already there, but not in a great format. Consider if this should be done in a discusion forum (and/or blog) rather than diigo.
- Is the missing student from the "learning experiences" book a task corrupter? Result?
- **S1, 2014** - Revisit the "Learning experiences" book and make explicit the two steps 1) what is a learning experience, and 2) designing good ICT rich learning experience. Perhaps use a specific sample(s) from past assignments and use those as concrete examples for both steps. Make more explicit the sources of learning experiences - i.e. advance organiser. Have students analyse the samples with SAMR and TPACK. Have them make suggestions about how to improve. Or perhaps have them pick on something in this course. Have them consider/be aware of how the capabilities of ICTs can change the task. Add activities that encourage students to apply the "where ideas come from" to their own UoW and share the ideas. Add in an illustration of the connections between essential questions and a sample UoW - perhaps do the same for other samples. Explain about the use of SAMR etc on the padagogy wheel. Have the students share their examples/applications of the TIP model to their UoW
- **S1, 2014** Think about the location of the sequencing learning experiences. May go before the actual learning experiences section. Talk to students about it not being a fixed thing. Can more activities/feedback be given here?

## Week 6 - Finishing your UoW

- Getting started and some revision
    - Where are we and where are we going? Book (172 clicks, 89 students)
        
        7 page book. Situating where we are and what needs to be done.
        
        Usage remains somewhat consistent.
        
    - Yet another quiz (161 clicks, 88 students)
        
        The "larger" shape quiz.
        
    - Declarative and Procedural Knowledge Book (141 clicks, 88 students)
        
        8 page book - more examples of declarative and procedural knowledge.
        
        This will need to move back to week 4
        
    - What's your best ICT-rich learning experience? Page (199 clicks, 88 students)
        
        Just setting up the discussion forum. Where the students share their best ICT LE. Th idea is that they will revisit this at the end of the week and seek to improve it.
        
    - Share you best ICT-based learning experience Forum (750 clicks, 84 students)
        
        Interesting drop in student numbers, while an increase in clicks. Which is probably due to it being used twice. The number of clicks per idea, isn't high.
        
- Assessment
    - Assessment - tasks, criteria and descriptors Book (182 clicks, 87 student)
        
        6 page book that helps the students with the rubrics and assessment tasks.
        
        Only 87 students using it.
        
    - Week 8 Recording of combined lecture/tutorial focus File (67 clicks, 42 students)
        
        Another on-campus lecture recording, also tutorial.
        
- Finishing up
    - Enhancing your ICT-rich learning experiences Book (114 clicks, 72 students)
        
        13 page book trying to deepen the student's use of ICTs in learning experiences.
        
        Much of this is very down on student usage - only 72. One page - the link back to the discussion forum is used more.
        
        Much of it repeats some of what's gone before. Soem good stuff on "common stuff". Revisits most of the frameworks (SAMR, Decoding Learning)
        
    - The essay Book (118 clicks, 86 students)
        
        3 page book talking about the essay. Greater use than the previous book, but still a little low.
        

Further work

1. **s1, 2014** Update the "What does module 3 hold" ("Where are we and where are we going") mention of what weeks various stuff is happening.
2. **S1, 2014** update the quiz results discussion in "Where are we and.." Expand the analysis section - leading into spreadsheets?
3. **S1, 2014** Move the declarative book back to week 4
4. **S1, 2014** Prepare a labelled image for the sample rubric and the component identification. Perhaps based on the example on the next page. Make explicit what is meant by the "components" in the activity on that next page.
5. **S1, 2014** Modify the "enhancing your ICT-rich LEs" by having an artefact (Word doc/Google doc) that students have to fill in for their ICT learning experience. And include space for them to come up with suggestions for improvements based on each of these. Perhaps work in another student working with them on this. That student will critique their existing idea and/or comment on the evaluation. Do an example with the example at the end of the book.

## Week 7 - PE Expectations and Design

- Getting started
    - Where we've come from and where we're going Book (174 clicks, 90)
        
        4 page book. Intro to the module and to assignment 3 and this week.
        
- Professional Experience
    - Overview and expectations Book (223 clicks, 89 students)
        
        17 page book outlining what is required on Professional Experience.
        
        Observations page surprisingly down in numbers!
        
    - What do you know about Professional Experience Forum (204 clicks, 87 students)
        
        Q&A Forum where students are expected to show what they know about it.
        
    - Designing lessons and leadership Book (184 clicks, 88 students)
        
        10 page book talking more about what might be done on Professional Experience. i.e. designing lessons and leadership. The TIP Model page is accessed a lot - probably through references from other pages.
        
    - Water Warriors Book (77 clicks, 60 students)
        
        11 page book that describes a sample UoW produced by a previous student.
        
    - The actual "Water Warrior" resources Folder (30 clicks, 21 students)
        
        Contains resources from the sample UoW
        
- Finishing up
    - What else do you want to know? Book (104 clicks, 86 students)

Further work

- **S1, 2014**: Update the "Where we've come from" stuff that mentions specific weeks to reflect S1.
- **S1, 2014** Update the stuff about the 2013 PE book in Expectations of PE.
- **S1, 2014** Should the learning place stuff be moved/removed? Fix up the layout of the observations page. Update mentions of the PE handbook (more detailed breakdown) - add link to the handbook?
- **S1, 2014** the student's video used in "leadership" is no longer available. See if access can be gained or reframe this section. May want to broaden this into a bigger discussion/activities around what you can do within the constraints of PE. Perhaps bring in some of the sample reflection essays and what they found and make some points about the assignment and start pushing people to start thinking about how they will do the design. Push them to start thinking about Part B of A3.
- **S1, 2014** Has the TIP model already been introduced previously? If not it should be - brought into backwards design.
- **S1, 2014** The Herrington and Kervin work on authentic learning might be useful to push further.
- **S1, 2014** Bring in the YOTs like activity into this section based on a prior PE.
- **S1, 2014** Bring in sample assignments - including lesson plans - from prior students and supplement the water warriors. Perhaps even start with the Water Warriors stuff. Have the students using SAMR/TPACK/TIP etc to evaluate?

## Week 8 - Digital Citizenship

- Getting started Book (207 clicks, 88 students)
    
    5 page book that gets the students using the Connect.ed resources and revisit the idea of digital citizenship.
    
- Are you safe? Book (199 clicks, 87 students)
    
    Getting into the digital footprint question for pre-service teachers.
    
- Share your posts on the Connect.ed resources Forum (291 clicks, 73 students)
    
    Students share their thoughts on the resources forum (blog posts) here. Need to rethink this as part of standard forum limitations.
    
- It's more than safety Book (133 clicks, 86 students)
    
    8 page book trying to move beyond the safety aspect.
    

Further work

- **S1, 2014** Are the connect.ed links and resources still available?
- **s1, 2014** Fix the HTML on "This week" page in "Getting started"
- **S1, 2014** Add some contributing activity to the getting started thing prompt student engagement/reflection. Ideas for what they could do? What are the big issues in their contexts that might be of interest? How can they connect this to their curriculum? SOme of this is in a later book from this week.
- **S1, 2014** Any update on crunkbear? Add in an activity around memes? Update the "inadvertently sharing information" for me to show exactly where the image was taken. A google map. Add in an explicit link about this back to the weather activity from earlier in the semester.
- Update on some of the example in the last book