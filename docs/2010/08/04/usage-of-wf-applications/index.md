---
categories:
- chapter-5
- design-theory
- elearning
- phd
- thesis
- webfuse
date: 2010-08-04 10:28:02+10:00
next:
  text: Usage of dynamic web applications by staff and students
  url: /blog/2010/08/05/usage-of-dynamic-web-applications-by-staff-and-students/
previous:
  text: Innovation in L&#038;T - where is the evidence
  url: /blog/2010/08/04/innovation-in-lt-where-is-the-evidence/
title: Usage of Wf applications
type: post
template: blog-post.html
---
Have spent the last day or so doing some more data munging of access logs trying to determine the level of usage of Wf applications within Webfuse. Wf was the framework for developing dynamic web applications within Webfuse - the topic/outcome of my [PhD](/blog/research/phd-thesis/). The following is an initial summary of that munging with some initial reflection. This will get further polished and re-worked for inclusion in chapter 5 of the thesis.

### Users and requests

The following table splits people using the Wf applications into students and staff. It shows the number of users of each type using Wf applications and the number of requests they made.

| Year | Students |  | Staff |  |
| --- | --- | --- | --- | --- |
|   | Users | Requests | Users | Requests |
| 2000 | 538 | 1888 | 2 | 31 |
| 2001 | 3361 | 27,936 | 96 | 4139 |
| 2002 | 4210 | 39,805 | 298 | 57,864 |
| 2003 | 6115 | 206,884 | 575 | 164,274 |
| 2004 | 8664 | 491,136 | 633 | 260,657 |
| 2005 | 9937 | 461,999 | 782 | 311,080 |
| 2006 | 11,994 | 1,033,619 | 1159 | 656,609 |
| 2007 | 10,810 | 820,847 | 1289 | 748,107 |
| 2008 | 12,085 | 777,522 | 1234 | 880,015 |
| 2009 | 12,342 | 900,870 | 1169 | 1,157,987 |

### History and comments

The following is simply a collection of comments seeking to offer some meaning, context and reflection on the statistics in the above table.

#### 2000

The first Wf application was the standard dynamic application of any e-learning system, "take quiz". The application students use to take an online quiz. It was developed in 2000, based on some earlier work, that was modified to fit within a mod\_perl development environment to deal with the increased system load created by all those students taking the quiz at the same time, at the last minute.

The only staff use of Wf applications was experiments taking a quiz. Staff wanting to know what the students would see.

#### 2001

2001 saw the development of the first staff specific Wf application, the results upload app. This app allowed staff teaching a course to upload a CSV containing the final student results for entry into the institution's students records system. It was developed after a particularly inefficient solution was proposed by the project implementing Peoplesoft at the institution. The results upload application was responsible for 53.4% of the staff requests in 2001. The other staff applications included:

- various quiz management features - 15.4%;
- an early online assignment submission system - 12.2%;
- an app to download a course class list - 9%; and
- an app to restrict access to portions of a class site - 6.9%.

For students, the take quiz application accounts for over 99% of the student requests.

#### 2002

This is where the staff "portal" applications: Staff MyInfocom and Staff MyCQU are developed. Both are extensions of the class list, results upload applications initially developed in 2001. The top 4 Wf applications based on staff requests (and accounting for almost 83% of staff Wf application requests) are:

1. Staff MyInfocom - 41.3%;
2. Online assignment management - 33.5%;
3. Quiz management applications - 4.5%;
4. Results upload - 3.5%.

It is this year that online assignment management really starts being used heavily.

For students, the take quiz application still accounts for over 99.5% of the Wf requests.

#### 2003

In 2003 a student "portal", and a number of other Wf applications for students, were developed. The major Wf applications by student use in 2003 were:

- Student MyInfocom (the "portal") - 55.5%;  
    The portal includes the mechanisms by which students submit online assignments.
- Take quiz - 43%;
- The timetable generator - 1.1%.

For staff, the "Staff MyCQU" portal - used by staff outside the original Webfuse faculty - starts to get heavy use. The top Wf applications by staff usage are:

- Staff MyInfocom - 40%;
- Staff MyCQU - 28.9%;
- Assignment management - 15.9%;
- Results upload - 4.3%;
- Informal review of grade - 3%;
- Quiz management - 2.9%.

It is interesting to see the decreasing proportion of use of the quiz management facilities.

#### 2004

Webfuse was developed within a particular faculty. 2004 is the year where usage by staff outside that faculty, starts to exceed usage by staff within that faculty. Webfuse is becoming an institutional system, at least in use. It takes another couple of years before it is official.

In terms of staff usage, the top Wf applications are:

- Staff MyCQU - 41.1%;
- StaffMyInfocom - 30.5%;
- Assignment management - 15.9%;
- Quiz - 4.8%.

For students it is:

- StudentMyInfocom - 78%;
- Take Quiz - 20.4%;
- Timetable generator - 1.3%.

#### 2005

This is the first year I was no longer officially involved with Webfuse. It's also the year that the direction of Webfuse is officially being set more by faculty management. This is evident in the rise of the Academic Misconduct Database (AMD). A system for tracking incidents of academic misconduct by students.

For staff the top Wf applications by usage in 2005 were:

- StaffMyCQU - 46%;
- StaffMyInfocom - 26.3%;
- Assignment management - 12.3%;
- AMD - 8.1%.

For students:

- Student MyInfocom - 88.6%;
- TakeQuiz - 9.6%;
- Timetable generator - 1.2%.

#### 2006

This is the year when an organisational restructure encouraged the broader adoption of Wf applications within the institution as parts of the faculty where Webfuse originated were broken up and spread around. You could say the infection that was Webfuse, spread. An example of this organisational restructure is the retirement of the "MyInfocom" brand. The faculty "Infocom" no longer existed and the brand morphed into MyCQU.

For staff, the top Wf applications were:

- StaffMyCQU - 71.1%;
- Assignment management - 11.1%;
- Plagiarism - 10.5%;
- Results upload - 1.4%;

This is also the year in which the timetable generator no longer existed, so the top student applications were:

- StudentMyCQU - 92.2%;
- Take quiz - 6.1%.

#### 2007

I believe this is the year Webfuse and the Wf applications officially became institutional systems as the Webfuse team moved from sitting in a faculty into the central IT division. I found it interesting to see the emergence of the mail merge facility as an top staff application.

The top applications by staff usage were:

- StaffMyCQU - 73.7%;
- Plagiarism - 9% ;
- Assignment management - 7.6%;
- Extension system - 1.6%;  
    This was a system by which students could request an extension for an assignment, and that request would be managed and tracked by staff.
- Results upload - 1.6%;
- Mail merge - 1.4%.

2007 is also the year which the Topic Allocation Nomination System became heavily used. Used in only 1 course, the TANS allowed students to select topics they would use for assessment.

The top applications by student usage were:

- Student MyCQU - 88.1%;
- take quiz - 7.8%;
- Topic Allocation system - 2.9%.

#### 2008

This is the first year in which staff requests are greater than student requests. This is probably a factor of students being increasingly served by other systems (another student portal was well underway by now), and the increasing number of applications aimed specifically at staff.

Top applications by staff usage were:

- Staff MyCQU - 77.6%;
- Assignment management - 7.4%;
- Plagiarism - 4.6%;
- Extension - 2%;
- Mail merge - 1.7%;
- Results upload - 1.5%:

For students:

- Student MyCQU - 84.9%;
- Take Quiz - 6.3%;
- TANS - 5%;
- Barometer - 1.4%;
- Extension system - 1.3%;
- BAM - .5%

Amongst the student numbers, it is interesting to see the appearance (admittedly in a small way) of the barometer and BAM. I believe the barometer appears because of an institutional project aimed at encouraging more feedback from students. BAM appears because of it's broader use, especially in a large course or two, and the availability of a method for students to track and see their progress.

#### 2009

2009 was essentially the final year of Webfuse. Though, the Wf applications continue to live on for a while in 2010, they will eventually disappear. Even though this is the first year in which staff usage of Wf applications breaks the million request barrier.

Most interestingly for me amongst the staff usage, is the rise of BAM. The top applications by staff usage were:

- Staff MyCQU - 79.8%;
- Assignment management - 7.1%;
- Plagiarism - 3.3%;
- BAM - 2.4%;
- Extension system - 1.4%;
- MailMerge - 1.4%;
- Results upload - 1.2%

For the students, BAM continues to rise and the barometer drops (note: this is a comparison in percentage terms, but the overall number of student requests increased between 2008 and 2009, so it's a real change). It is my understanding that the "push" to use the barometer was not continued in 2009 and its use was left up to the academic staff, hence the drop. This mirrors lessons learned in [earlier work with the barometers](https://djon.es/Publications/barometer_2.pdf).

For students, the top used Wf applications were:

- Student MyCQU - 86.8%;
- Take Quiz - 5.5%;
- BAM - 2.8%,
- TANS - 2.6%;
- Extension system - 1.4%;
- Barometer - 0.9%.

#### What's with the student portal?

From about 2006/2007 CQU had an official student portal, so why does StudentMyCQU still account for such a large percentage of student usage of Wf applications?

The simple answer is that the StudentMyCQU application also embodies the interface students use to submit online assignments. For example, of the 781,705 requests of the Student MyCQU application made in 2009, at least 76% of the requests were submitting, checking or viewing online assignments.

Combining the student usage with the staff usage, and online assignment submission and management was amongst one of the most used features of Webfuse.