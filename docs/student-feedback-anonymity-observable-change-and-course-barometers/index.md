---
date: 2012-03-04 23:08:58+10:00
title: Student feedback, anonymity, observable change and course barometers
type: page
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Helping teachers &#8220;know thy students&#8221; | The Weblog of (a) David
        Jones
      author_email: null
      author_ip: 192.0.100.175
      author_url: https://davidtjones.wordpress.com/2015/09/15/helping-teachers-know-thy-students/
      content: '[&#8230;] Student feedback, anonymity, observable change and course&nbsp;barometers
        [&#8230;]'
      date: '2015-09-15 10:06:32'
      date_gmt: '2015-09-15 00:06:32'
      id: '250'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
David Jones, Student feedback, anonymity, observable change and course barometers, World Conference on Educational Multimedia, Hypermedia and Telecommunications, Denver, Colorado, June 2002, pp. 884-889.

## Abstract

A Course Barometer (Svensson, Andersson, Gadd, Johnsson, 1999) is a method for addressing the loss of informal feedback in a distance education setting. Originally proposed and used at the University of Trollhattan Uddevella this paper describes how the idea of a course barometer has been adopted and adapted at Central Queensland University. The paper examines the role implementation decisions, anonymity and observable change had on use of the barometer by students. Based on usage statistics and feedback from staff and students reflects on the use of the course barometer and offers suggestions for improvement.

## Introduction

Collis and Oliver (1999) report in their analysis of the papers submitted to EdMedia'99 that the majority of papers report on prototype development and evaluation with few ideas going beyond this stage. One of those papers (Svennsson, Andersson, Gadd, Jaohnsson, 1999) described the initial development and evaluation of the course barometer. A course barometer is a web-based application designed to provide students a simple, anonymous method for providing informal feedback about their feelings toward a course while it is being taught. This paper reflects on the use of the course barometer idea within the Faculty of Informatics and Communication (Infocom) at Central Queensland University (CQU).

The absence of informal, in-term feedback is a major problem within Infocom since most courses are taught with a large number of part-time staff via both print-based distance education and in a face-to-face mode at 13 sites spread through out Australia, Fiji and South-East Asia. The course barometer concept within Infocom was initially intended for a course taught by the author in the second half of 1999. The potential and obvious need for in-term feedback from students has led to the course barometers contributions being received in 67 different course offerings since then.

The paper starts by offering a brief overview of the course barometer concept followed by a description of the data sources used to examine Infocom's barometer experience. Two stories are then provided which show how a course barometer has made a positive difference for both staff and students. The paper then examines the connection between implementation choices, anonymity, observable change, and the level of student contributions to the course barometers.

## Barometer design and implementation

There have been three versions of the course barometer concept. Two versions, alpha and beta, have been implemented at the University of Trollhattan (Svensson and Sorenson, 2001) and the Infocom version described here. All three barometers provide a mechanism by which a student can indicate their current mood and provide a small textual comment about a course. All three provide a statistics page where staff and students can view the atmosophere of the course. Minor differences between the barometers include changes in the interface design, moods that can be expressed, administrative mechanisms, and the implementation environment.

A more significant difference between the Trollhattan barometers and the Infocom barometer is the number of times per week students could make contributions. At Trollhattan students could make as many contributions as they wanted, whenver they wanted. In an attempt to increase the value placed on barometer contributions the Infocom barometer restricted students to one contribution per week per course. The intent was to encourage students to be more thoughtful in their contributions. This limitation also prevents the possibility of the barometer taking on an unbalanced view due to large numbers of repeat contributions from a small number of students. Lowder and Hagan (1999), writing about another web-based anonymous feedback system, report on a student using the ability to make multiple postings as a nuisance technique.

To implement this restriction it was necessary to be able to identify which student was making a contribution. This violates the aim of providing an anonymous environment where students need not fear repercussions for making negative comments. Recognising the negative impact this may have upon student participation the implementation of the password protection system aimed to make it as difficult as possible to identify which student made a specific contribution.

Additionally, teaching staff have never been provided with any access to information connecting students to contributions and a special effort was made to communicate this information to students. A positive side-effect of the password requirement was to address another problem. Infocom course websites generally are not password protected. In the past this has led to non-CQU students misusing facilities that allow for visitor contributions.

The alpha and beta barometers at Trollhattan were used over a four week period in a single course during two different terms. There was a total of 213 submissions for the alpha and 308 for the beta barometer (Svennson and Sorenson, 2001). The Infocom barometers have been used for the entire 12 weeks of 5 different terms and contributions received for 67 different course offerings. For all but the last term the Infocom course barometers were only included at the request of the course coordinator. In the last term of 2001 the course barometer was made a standard part of the default web site for all Infocom courses. In this term there was a total of around 100 courses with default web sites. Barometer contributiosn were only received in 46 of these courses.

## Data sources

Information about all student contributions to the Infocom course barometer were stored in two database tables. One table stored the course, week, feeling (good, bad or indifferent) and any comments. The other table stored student number, course, and week. It was this second table that was used to prevent students making more than one comment per course, per week.. The data in these tables has been used to identify simple statistics about students and their contributions. The student comments on the Trolhattan alpha-barometer underwent content analysis. Due to time and resource limitations such an analysis has not yet been performed on the Infocom data.

Logs from the Infocom website have been archived since early 1997. These logs record the date, time and web page of every visit to the Infocom website. The webserver logs have been used to compare the number of visitors to course barometers with the number of people making contributions.

To gather more information about student feeling toward the course barometers a 15 question survey was placed on the Web toward the end of 2001. The survey contained 8 likert style questions and 7 short answer questions. An email message announcing the survey was sent to all students enrolled in Infocom courses during the second half of the year. CQU's student record system contained email addresses for 948 of these students. 350 of those email addresses suffered from a number of problems which prevented delivery. A week after the first email initial results were released on the web and another email sent informing students and reminding them about the survey.

61 responses to the survey were received giving a response rate of 10.2%. 70% of the students who responded to the survey knew about the course barometer. 58% of respondents agreed or strongly agreed with the statement "The course barometer is a useful feature". While responses to the survey are a useful guide to student feeling there is some bias in the sample. The type of students who had correctly entered an email address into CQU's student records system and completed an online survey during the final stages of a term are more likely to make use of an online resource like the course barometers.

An email message about the course barometers was distributed on the Infocom staff mailing list early in the second half of 2001. Of the 60+ course coordinators within Infocom, many of whom had previously never used or known of the course barometer facility, there were 6 replies. In some cases there was on-going discussion between the author and individual staff.

## Statistics, trends and potential reasons

Over three years of use 1188 student contributions were made via the Infocom course barometers. The average length of a comment on the Infocom barometers was 120 characters. Over the 5 terms of year the average number of contributions per course offering was less than 18. However, three of these terms had significantly higher levels of contributions. The three busy terms had an average of 40 contributions per course offering. While the two slow terms had an average of 7 contributions per course offering. The defining difference between these two groups of terms was the motivation and involvement of the course coordinators in encouraging and responding to barometer contributions.

In the last main term for 2001 the course barometers were, for the first time, a compulsory part of every Infocom course website. However, staff were not required to encourage students to contribute to the course barometers. In this term 448 contributions in 46 different course offerings were made for an average of 9.7 per course. Only 16 (24%) of courses in this term had greater 10 contributions. This does not include the over 60 courses which had course barometers with no contributions from students.

29.5% of the Trollhattan alpha-barometer submissions included comments (Svennson, et al, 1999) while 71.7% of the Infocom submissions included comments. Trollhattan contributions showed overall student feelings of 57% bad, 10% indifferent, and 33% good. The Infocom breakdown was 29% bad, 20% indifferent and 51% good with the 1188 student contributions being made by 538 different students. The most prolific student made 50 contributions over 6 courses during two terms in 2001.

If you accept that the one comment, per week, per course increased the effort placed into the Infocom barometer contributions this may help explain why the number of contributions with comments at Infocom is almost the inverse of that at Trollhattan, 29.5% to 71.7%. It may also explain the switch in reported feelings from 33% good at Trollhattan to 51% good within Infocom. Especially given the observation that both the Trolhattan and Infocom barometers have been used primarily in courses with staff interested in improving the students' experience.

The number of contributions per week for almost all courses follows a common trend. There is an initial spike early in the term when the course barometer is first discovered. Followed by a gradual drop off until some minimum level is found and maintained until the last week or so of term. At this stage there is usually a small increase in contributions due to the end fo term. Any exceptions to this trend are caused by specific events which encourage students to contribute.

## Two stories

While the overall level of contributions to the Infocom course barometers has been limited there have been a number of specific incidents where they have played an important role in improving the experience of both students and staff. The first story takes place during the first term in which the Infocom course barometers were used. In the second week of the term a serious student complaint was made about a relatively new staff member. The complaint was very critical of the staff member's lecture style. The week after the complaint was raised the number of comments on the course's barometer was over four times the average. Almost all contributions directly addressed the topic of the initial complaint and all were very positive. For example,

> After hearing XXXX talk about the student who pretty much is jeopardizing his job, I feel really bad for him. He is a GREAT lecturer and the way he has summed up Programming A in just a matter of weeks I understand the concepts a lot better.

As a result both the staff member and his supervisors were much relieved.

The second story comes from the last main term in 2001 and demonstrates how the course barometer was able to contribute towards an improvement in the student's experience. Many of Infocom's courses are delivered via video-conferencing between four regional campuses. Such presentations are usually made as traditional lectures originating from CQU's Rockhampton campus where most course coordinators currently work. In 2001 a new lecturer located on the Bundaberg campus was given responsibility for a course that had to be delivered by video conferencing. During the first three weeks the course barometer shows an increasingly negative feeling from students about the course. Most of the comments related to the quality of the lecture delivery. It should be noted that contributions in these early weeks involved less than 10% of the students attending these lectures.

> Lecturers voice fades, notably at the end of sentences. There were technology problems as well, but lecturing techniques need to be improved....

72% of the comments in those first three weeks came from students at the Rockhampton campus (11% Bundaberg, 16% Mackay). Many of the Rockhampton students would have been on the receiving end of a video-conferenced lecture for the first time. The difference in viewpoints between campuses became more obvious during the following weeks.

> You people in Rockhampton are pathetic. You complain that the lecturer was late. I know for a fact that he was not........  
>   
> Well I think the students in bundy should think before they speak or in this case write.....

Often problems such as this would have continued thoughout the term with little or no change. However, in this case the problems raised were addressed in a variety of ways and from week 4 onwards the overall student feeling on the barometer was positive.

> The lecture was far different than last week, the voice of the lecturer was much better.....

## What don't students contribute

Since 1999 there has been an average of just less than 18 barometer contributions per course offering. This raises concern about why more students are not making contributions to course barometers. This section draws on data from web logs, student barometer comments and responses to the student survey to examine this issue further.

Of the students surveyed who knew about the course barometer 7% never read the contributions, 21% read them once, 36% every now and then, 17% once every couple of weeks, and 19% once a week. Of the students surveyed who read contributions 57% never made a contribution, 34% made a comment every now and then. Only 9% of students surveyed made a contribution every week. Using web logs it is possible to determine that during the three busy terms 6% of the people looking at a course barometer made a comment. During the last term of 2001, where all Infocom courses had barometers, only 1.5% of visitors made a contribution.

When asked why they didn't make a contribution the most popular student responses included: having no complaints or strong opinions to contribute, having a preference for using another medium, and the belief that there would be no change if a contribution was made. Other reasons given included a lack of other comments, didn't want to repeat an existing comment and having no time.

When asked why they made contributions the most common reasons included: the importance of giving feedback in order for change to happen, having strong feelings about an issue and supporting a lecturer against negative comments. Other reasons given included agreeing with a comment, disagreeing with a comment and because the lecturer asked.

69% of survey respondents agreed or strongly agreed with the statement, “If visible changes were made because of comments to the course barometer I would be more likely to add comments to the course barometer”. Student comments to various survey questions include

> Because the lecturer \*really \* wanted feedback – asked every week. I though it was worth the trouble to help improve the course for the future......
> 
> Does it get back to the Dean or Head of school? It's no use going to the lecturer. If the barometer will serve to fix slackness then yes it will be useful
> 
> It is just another mouthpiece for the University not to take into consideration. It is the same as the evaluations. None of them are ever taken into consideration.
> 
> Any changes that were made came to late for the majority of the class. In fact, when the changes were made they advantaged the few and disadvantaged the majority of the class.
> 
> I don't think I saw any changes. I did however notice in one nameless subject that I did this semester, that at the start there were some very negative comments about it (that I totally agreed with) but when nothing changed the use of the barometer just died.....

The lack of anonymity was not given by any student as a reason for not contributing. However, a barometer contribution did show that at least one student had a problem with the apparent lack of anonymity.

> I suppose you think that if no-one submits a comment, then everyone must be going ok. Not! Just maybe, its the fact that the submission doesn't appear to be anonymous when your asked for your student details to submit your comments.I have lots of concerns and would like to pass comments to the course barometer, but am concerned that its the messenger that will be shot and not the message addressed.

Other students expressed concern about anonymity when answering the survey question “What didn't you like about the course barometer?”.

> While realising the need to prevent malicious access, it was disconcerting to need username and password to access an anonymous site.
> 
> When you submit you need to logon. This gives the feeling that who is responding is being recorded instead of it being anonymous

Some students appear to have believed that the course barometer was anonymous. Responses to the survey question “What did you like about the course barometer?” included

> students can feel safe in that it is anonymous, so they won't be attacked for their opinion.
> 
> Allows student who do not wish to be named to provide any kind of feedback without fear of it being held against them come marking time.

Some students, usually when supporting a lecturer against negative contributions, defeated the supposed anonymity of the barometer contribution by including their name, for example.

> I do not feel the need to make my comments anonymously, so here goes....Linda

Though this practice was given other interpretations by other students

> ....It is amazing how some students say they don't need to be anonymous about their comments and then piss in the lecturers pocket and attach their name

Some students perceived that the anonymity provided by the course barometer was actually a negative attribute.

> .....I would approach the lecturer/Co-ordinator directly. I believe that the barometer restricts/reduces open communication with the source of the problem
> 
> Often I noticed other students use anonymity to feel OK about not bothering to construct appropriate arguments and blurt out unconstructive criticism.

Other students suggested that knowledge of the contributors identity should be used

> Force student ID, student number would suffice, so that course organisers can follow up true complaints
> 
> Very good thing, maybe every time somebody votes, they get an entry into a prizepool to win something, maybe a textbook refund or something simple like that.

While the apparent lack of anonymity was a problem for some students it appears it is not as important a factor as the lack of observable change. Students do not wish to give feedback if there is no visible response.

## Staff impact and views

Only a small number of motivated staff have made significant use of the course barometers. As a result all of these staff see the potential benefits that the barometer can provide.

> ..the Course Barometer is an excellent tool, and staying "in the green" all term is a good challenge for teaching staff. At a glance, you can see how some students are going. And because there is no way for teaching staff to see who made which comment, students can say how they are going without fear of recriminations.

However, they have also experienced a number of problems including: unconstructive feedback, inability to help students with problems directly, and frustration caused by negative feedback when trying their best.

> Because the tool keeps students anonymous, the feedback tends to attract occasional students who want to have a little rant or hissy fit without any chance of people finding out who they were. So, instead of these students seeking help or doing something really useful, they vent their frustrations. We need to reach these students and help them, but instead they hide behind anonymous feedback
> 
> ......So, maybe this student is looking at the slides for the wrong subject, or simply cannot put two and two together, or else has some severe fundamental misunderstandings, or is on another planet, or something. In any case, I cannot find out who they are or contact them or help them, and this is a real shame.
> 
> Comments made on the feedback barometer can be incredibly frustrating because the students who make them can sometimes need urgent help or assistance, but they have chosen the barometer to make their comments, and this keeps them anonymous, so we have no chance to find out who they are or help them. This is incredibly frustrating. I want to help these students, but my hands are completely tied - unless they also decide to email me or contact me in some other way which sadly, does not seem to happen. These students seem to replace email with the feedback barometer, so they seem to use one instead of the other.

## Conclusions

A course barometer is a method for addressing the loss of informal feedback in a distance education setting. While the use of course barometers within Infocom has been done in an ad hoc manner with limited contributions by students there have been a number of situations where its presence has helped students, staff and the organisation.

The small number of contributions on the Infocom barometers can be explained by a number of factors. It appears that a combination of staff promotion of the concept and observable change in response to student feedback are amongst the most important factors for promoting student contributions. It appears that the lack of anonymity provided by the Infocom implementation of course barometers, while an issue for some, is not of prime concern and some students and staff actually see it as a negative influence over the quality of contributions.

In the future tools such as the course barometer will be of increasing importance to Infocom. Recent moves to increase the importance of quality assurance within the Australian University environment is one factor. Infocom's increasingly complex mix of distributted campuses and distance education also increase the importance of having a simple, heavily used student feedback mechanism.

As a result the Infocom barometer concept is likely have an expanded role with a number of planned changes to improve the level of student contributions. In particular, it is likely that responsibility for promoting student contributions and ensuring changes are seen to happen will be given to a position seen as being independent and separate from teaching staff. Another likely change is the combination of the course barometer idea with the anonymous threaded discussion functionality described in Lowder and Hagan (1999). This would allow discussions and responses to develop around a particular student contribution. This would provide a place where change can be seen and also encourage further learning (Lowder and Hagan, 1999) and facilitate informal student interaction.

The work described here is still in the stage of early investigation. More research is required to further test and clarify some the observations and conclusions that have been made. As the use of the course baromter concept expands and groups it will become increasingly important to investigate how the course barometer fits in with and related to other mediums used to support teaching and learning. However, course barometers remain a positive and useful tool.

## References

Collis, B., Oliver, R., (1999), Preface, In Proceedings of EdMedia'99, Betty Collis, Ron Oliver (eds), Seattle, Washington.

Svensson, L., Andersson, R., Gadd, M., Johnsson, A., (1999), Course-Barometer: Compensating for the loss of informal feedback in Distance Education, In Proceedings of EdMedia'99 , Seattle, Washington, pp 1612-1613.

Svensson, L., Sorensen, C., (2001), Designing Community Atmosphere Barometers, In Proceedings of ECIS 2002, Gdansk, Poland.

Lowder, J., Hagan, D., (1999), Web-based Student Feedback to Improve Learning, ACM SIGCSE Bulletin, Proceedings of ITiCSE'99 Conference, pp 151-154.