---
date: 2009-01-02 02:04:52+10:00
title: Teaching Systems Administration II
type: page
template: blog-post.html
---
David Jones, Teaching Systems Administration II, SAGE-AU’95, Wollongong.

## Abstract

The Department of Maths & Computing at Central Queensland University has offered a subject in UNIX Systems Administration since 1992 (Jones 1993). Recently the subject has been adopted as a core subject in CQU's Bachelor of Information Technology. This paper will describe the development undertaken to prepare the subject for delivery to students geographically located anywhere in the world. It will provide an overview of the subject's curriculum, delivery and assessment methods and discuss the experiences during the most recent offering of the subject.

## Introduction

The Department of Maths & Computing at Central Queensland University (CQU) has offered its subject in Systems Administration five times since 1992. The aim of the subject is to provide students with a practical introduction to the profession of Systems Administration and provide students with an appreciation of the difficulties of looking after a multi-user computer system. By the end of the subject it is hoped that students should meet the requirements of a junior Systems Administrator as listed in the SAGE (Systems Administrators Guild) job descriptions (http://www.sage.usenix.org/sage/jobs/jobs-descriptions.html).

While the topic of Systems Administration is platform independent it is essential that students receive some practical grounding. For this reason the UNIX operating system is used to provide the practical application of theory. UNIX was chosen because

- of its industry importance,
- to expand the experience of CQU students who have previously been restricted to MS-DOS, and
- it can provided to the students cheaply.

Since 1993 the major development in the subject has been the offering of the subject by distance study (by correspondence). This change has meant that a number of modifications in the delivery, assessment and running of the subject. This paper discusses the enhancements made to the subject since 1993, the development of the subject for delivery at a distance, the experience gained during the most recent offering of the subject and the plans for future development.

## Background Information

To understand the development of the subject it is important to know about

- the structure of CQU's Bachelor of Information Technology,
- the concept of distance study,
- the hardware requirement of CQU's distance students,
- the aims of the subject, and
- the quality of the students

### CQU's Bachelor of Information Technology

The Department of Maths & Computing at Central Queensland University offers a three year Bachelor of Information Technology (BIT) degree. The BIT is divided into two streams, a traditional Software Engineering stream and a System Services stream. The Systems Services stream is designed to produce students with experience and ability in system support and administration. The Systems Administration subject is one of the core subjects in the System Services stream. Table 1 describes the subjects that make up the System Services stream.

| Year | Semester 1 | Semester 2 |
| --- | --- | --- |
| One | Programming A | Programming B |
|  | Conceptual Foundations of Computing A | Conceptual Foundations of Computing B |
|  | Human Issues in Computing | FOCT (Hardware) |
|  | Elective | Elective |
| Two | Data Systems A | Operating Systems |
|  | Programming in C/C++ | Human Computer Interface |
|  | TQM/Elementary Statistics | Elective - Computing |
|  | Elective | Elective |
| Three | Data Communications | Professional Issues |
|  | Systems Administration | Networks |
|  | Elective - Computing | Elective - Computing |
|  | Elective | Elective |

Table 1 - CQU Bachelor of Information Technology (System Services Stream).

### Distance Study

One of the key characteristics of subjects offered by the Department of Maths & Computing is that all subjects must be available via distance study. Distance students can be located any where in the world and are not required to attend lectures or tutorials on campus.

As a result distance students traditionally have little or no direct contact with the lecturer. Instead distance students rely on study guides, text books and resource materials for their learning.

The first full on-campus and distance offering of 85321 (February to June, 1995) had an enrolment of eighty students. Fifty of those students were distance students and were located in all parts of Australia, Singapore and one student in Cyprus (an Australian Federal policemen with the United Nations Peace-Keeping force in Cyprus).

### Minimum Hardware Requirement

It is obvious that computing students must gain some form of practical application of the concepts they are introduced to in their subjects. For on-campus students this access is provided by the computer labs at CQU's five campuses. Distance students, on the other hand, generally can't gain access to CQU's campuses due to geographic constraints.

For this reason distance students studying the BIT are required to have access to an IBM PC computer. The Department's current recommended minimum is a machine with 1Mb RAM, VGA and 40Mb of hard disk space. In practice most distance students have machines with considerably more power. A result of this requirement is that all subjects offered by the Department must be designed so that they can be completed on this minimum computing platform (with some bending of the rules allowed).

### The Students

Students taking the Systems Administration subject are generally in the third year of their computing degree and have completed subjects in operating systems, data communications and are reasonably proficient with C++ (as of next year C++ will be CQU's first year programming language).

Students generally have little or no UNIX knowledge. Their only exposure to UNIX is a six week of introductory UNIX course in their first year. By the time they reach their third year most students have completely forgotten this work. Students do not have any access to a UNIX machine during their degree as the computer used for student email is a VMS machine.

The quality of the average on-campus student is generally lower than that of more established Universities. The brighter students are usually attracted by the bright lights of Brisbane and the University of Queensland, Griffith University and the Queensland University of Technology. On the other hand the distance students are usually of a higher quality. The majority of distance students are professionals studying towards a University qualification in computing.

### Subjects Aims

CQU's teaching semesters last for 13 weeks and an average student will have to invest a minimum of 10 hours per week to pass most subjects. That provides a total of 130 hours (just over 3 working weeks) in which to produce capable Systems Administrators. 130 hours is not sufficient to produce gurus.

85321, Systems Administration aims to provide students with experience of Systems Administration. The hope is that if the students become Systems Administrators they have a grounding in the area that will enable them to quickly become useful. If the students don't become Systems Administrators at the very least they will have an understanding of the complexities and requirements of the position and will be more understanding of Systems Administrators throughout their professional careers.

The subject aims to produce students who are capable of fulfilling a majority of the requirements of a Junior Systems Administrators position as described in the SAGE Job Descriptions booklet.

### Required skills:

Strong inter-personal and communication skills; capable of training users in applications and UNIX fundamentals, and writing basic documentation.

High skill with of most UNIX commands/utilities. Familiarity with most basic system administration tools and processes; for example, can boot/shutdown a machine, add and remove user accounts, use backup programs and fsck, maintain system database files (groups, hosts, aliases). Fundamental understanding of a UNIX-based operating system; for example, understands job control, soft and hard links, distinctions between the kernel and the shell.

### Required background

One to three years of system administration experience.

### Desirable

- A degree in computer science or a related field.
- Familiarity with networked/distributed computing environment concepts; for example, can use the route command, add a workstation to a network, and mount remote filesystems.
- Ability to write scripts in some administrative language (Tk, Perl, a shell).
- Programming experience in any applicable language.

### Appropriate responsibilities

Administers a small site alone or assists in the administration of a larger system. Works under the general supervision of a system administrator or computer systems manager.

## Development Problems

Prior to 1994 the subject was only offered to on-campus students. The adoption of the subject as a core subject for the Systems Services stream meant that as of 1995 it had to be offered to both on-campus and distance students. During 1994 development was undertaken to modify the subject so that it could be offered at a distance.

In developing the subject as a full distance subject a number of problems had to be overcome, including

- providing access for all students to the root password of a UNIX machine,
- finding a text book that covered the required material at the right level,
- providing sufficient feedback to all students in an attempt to simulate the master/apprentice relationship.

### Providing Root Access

To complete a subject on UNIX Systems Administration it is essential that students have access to the root password of a UNIX machine. The only way to fully understand the theory is to be able to experiment on a local machine. Very few students could be expected to be obtain access to a local UNIX machine, let alone convincing the administrator to hand over the root password.

It was obvious that the Department would have to discover some method of supplying a UNIX machine to the students. The Department's requirement that all subjects be delivered on a IBM PC compatible platform meant that Linux and FreeBSD were prime candidates for providing students with access to the root password of a UNIX machine.

Experiments with both operating systems were carried out in early 1993. At that time Linux proved to be the easier to install and was subsequently the operating system of choice. Since that time the decision has been made to stay with Linux because of the large established user base Linux has gathered and also because the author has significant experience with Linux. Moving to another operating system would mean learning a new collection of tricks and tips.

Students studying 85321 were provided with the root password of a UNIX machine by

- setting up a lab of 486DX2-66 machines running Linux for on-campus students,
- providing a distribution of Linux to all students (on-campus and distance) that could be installed onto their personal machines.

For the on-campus lab an order was placed in mid-January 1995 with Osborne for four 486DX2-66 machines. As the machines were required by the end of February it was thought six weeks would be sufficient time for them to arrive. It wasn't! The machines finally arrived in late March four to five weeks into the semester.

During semester the 30 on-campus students shared five 486DX2-66 machines running Linux. The class was divided into groups of 6 students. Each group was given the responsibility of looking after a particular machine. Most groups were allowed to add a number of users during the semester.

In early January 1995 all distance students enrolled in Systems Administration received a letter explaining the subjects requirement of having access to the root password on a Unix machine. The students were given the following options

- obtain the required access through a UNIX machine locally,
- obtain a version of Linux either from the Internet or from any of the Australian commercial providers,
- purchase a copy of Linux from the Department.

For $25 the Department would provide students with

- a copy of Linux on either 35 high density, 31/2 inch floppy disks or on CD-ROM,
- a disk containing a number of useful utilities, and
- a locally produced installation manual.

Of the 52 distance students enrolled in the subject 33 purchased the CD-ROM version of Linux, 11 purchased the floppy disk version and 8 were able to obtain the required access locally.

At least two students used the necessity to have Linux as an excuse to purchase either a CD-ROM drive or a new computer with a CD-ROM drive (they were both married).

The majority of the problems encountered with installing of Linux was due to combinations of hardware that either the author or Linux were familiar with. This included

- CD-ROM drives that Linux didn't support,
- A problem solved by the students using MS-DOS to copy the installation software from CD-ROM onto their MS-DOS hard drive and then installing off the hard drive.
- sound cards with SCSI CD-ROM controllers,
- Simple solution was to specify the correct boot parameters as documented in the Linux HOW-TO documents on the CD-ROM.
- some of the students who are not computing experts and who made silly mistakes, and
- a couple of cases of corrupt floppy disks.

Eventually, and not without heartache, all students were able to install Linux onto their machines. A survey that is currently under way is attempting to determine the specific problems the students faced and how long it took them to install Linux.

### Finding a Textbook

While on-campus students can attend lectures, distance students rely on text based study material as their primary source of information. The study material for the subject during 1995 included a Resource Materials book containing a number of photocopied articles and a textbook. The textbook used in the subject was written by the author specifically for this subject. The reasons for undertaking the development of a new textbook included

- the inability to find a suitable text that provided coverage of the right topics at the right level,
- the need to have something that covered Linux, and
- the desire to make the text available via WWW.

Early in the development of the subject, a conscious decision was made to make significant use of Internet technology in the subject. One of the methods used was to make all subject information, including the textbook, available via the World-Wide Web. This could not be achieved with a commercial text.

The adoption of Linux as the standard operating system for the subject meant that it was desirable to use a book that contained some Linux specific information. The fact that Linux uses a combination of SysV and BSD conventions makes it harder to find a suitable text from currently available texts.

In the previous four offerings of the subject, students were required to purchase two texts. One of the texts was an introductory text on using UNIX including coverage of shell programming and the other was a Systems Administration text.

The shell programming text used in all offerings has been

- Stephen Kochan, Patrick Wood, _UNIX Shell Programming_ Revised Edition, Hayden Books, 490pp, ISBN 0-672-48448-X

The Systems Administration texts that have been used in past offerings of the subject have included

- Evi Nemeth, Garth Snyder, Scott Seebass, _UNIX System Administration Handbook_, Prentice-Hall, 1989, 593 pp, ISBN 0-13-933441-6
- Dave Fiedler, Bruce Hunter, Ben Smith et al, _UNIX System V Release 4 Administration_ 2nd edition, 1991, 436pp, ISBN 0-672-22810-6
- Levi Reiss, Joseph Radin, _UNIX System Administration Guide_, Osborne McGraw Hill, 1993, 640pp, ISBN 0-07-881951-2

The Nemeth book was dropped because of two reasons

- it was becoming outdated, a problem that has recently been solved with the release of the second edition, and
- some CQU students found it to be a little to difficult.

The Fiedler text was used in an offering of the subject where the students used a SVR4 machine. While the text was liked by the students it did not provide enough coverage in a number of important areas.

The Reiss text was used in 1994 and was chosen in a moment of weakness. In hindsight it was a bad decision. It offers a gentle introduction to the art of Systems Administration that is tainted by its brevity

One of the really annoying habits of the book is that it is littered with "meticulously crafted scripts" and "valuable source code....for adding and removing users....and performing daily system administration tasks". No mention is made of public domain tools that perform the same tasks better and some of the scripts are horrible.

Purchasing two books for one subject is a significant cost ($100+) especially for students. It was not possible to find one text that covered the required topics nor was it possible to find a Systems Administration text that was at the right level.

The development of the subject's text book is discussed below.

### The Master/Apprentice Relationship

One of the biggest problems with distance study is the lack of effective feedback. Students find it very difficult to discover whether or not how they understand a concept is actually correct. There isn't a great deal of interaction with other students or the lecturer that would usually highlight a misconception.

This lack of feedback is particularly crucial in a field like Systems Administration where the best method of learning the craft is in a Master/Apprentice scheme. It was planned to make use of email, including a subject mailing list, to attempt to foster interaction and discussion between the students and the lecturer and also amongst the students themselves (especially the distance students).

Some of the basic mistakes made during the final exam have shown that this scheme was not as successful as it could've been.

## Writing a Textbook

The aim of the text was to

- cover the necessary introductory UNIX knowledge including shell programming,
- cover the required Systems Administration topics,
- provide a collection of problems and solutions to those problems,
- include coverage of Linux specific information, and
- to make it available via the WWW

The text was written using Word for Windows (a source of many problems in itself) during 1994 and published by CQU's publishing unit in early 1995. The final version is 330 pages long and was sold to students for $25. The text was converted to HTML and is available on the WWW under the subjects home page at the URL

http://cq-pan.cqu.edu.au/mc/lect/david-jones/85321/85321.html

## Topics to be covered

Choosing the order in which to present topics in an introductory Systems Administration subject is difficult.

Table 2 lists the topics covered and the order in which they were discussed in the most recent offering of 85321. Each section is explained below.

### Foundations and Basic UNIX

During week one of the semester the students are provided with an introduction to the role and responsibilities of a Systems Administrator. Hopefully this gives the students some idea of what a Systems Administrator does and why they are important. In addition basic concepts regarding operating systems, justification for using UNIX, a brief history of UNIX and a brief introduction to the vi editor are also covered. Also examined are the UNIX command format, the role of the shell, file and directory manipulation, various UNIX commands and the UNIX manual pages.

### Shell Programming

It is expected in this subject that the students become proficient Bourne shell programmers. The Bourne shell was chosen because it is the common shell for the root user.

| Week | Topic |
| --- | --- |
| 1 | Introduction to Systems Administration and some basic UNIX |
| 2 | UNIX Shell Programming |
| 3 | Advanced UNIX Use |
| 4 | Systems Administration Theory and Users |
| 5 | File Systems and Backups _**Class Test #1**_ |
| 6 | Starting Up and Shutting Down |
| 7 | Terminals and Printers |
| 8 | Unix Network Basics |
| 9 | More Networking |
| 10 | Security |
| 11 | The Kernel |
| 12 | cron, Accounting and Quotas |
| 13 | Professional Issues _**System Emergency Week**_ |

Table 2 - 85321, Systems Administration Topics

### Advanced Unix Use

During week 3 more advanced topics including advanced shell programming, more advanced commands including awk, sed and regular expressions are covered. Other command languages such as Tcl/Tk and Perl are mentioned but there is not sufficient time to provide detailed information or practical experience.

### Systems Administration Theory, Users and Accounts

Finally the start of the "real" Systems Administration material. Week 4 examines some of the generic, hardware independent tasks that a Systems Administrator must perform including management, policies, procedures, communication with the users, and most importantly documentation.

The second portion of the week examines the concepts, files and commands involved in creating user accounts on a UNIX machine. This is the first week in which on-campus students are provided with the root password to the on-campus machines.

### File Systems and Backups

During week 5 the students look at the methods UNIX uses to store and retrieve information from disk drives. In addition they also examine what might be the most important task that a Systems Administrator is responsible for backups.

### Starting Up and Shutting Down

In this section the students examine the process a UNIX machine goes through when it boots and when it is being shut down.

### Terminals and Printers

During this week the students examine how to connect terminals and printers to a UNIX box. Included in this is the examination of the print systems for both BSD and SysV, termcap, terminfo and printcap.

### Unix Network Basics

Networking forms two weeks of the course. During the first week the concepts covered include an introduction to TCP/IP and basic concepts including hostnames and addresses, routing and name resolution.

### More Networking

The second week of networking examines the r commands, NFS, the process for adding a machine to a network and methods for diagnosing simple problems.

### Security

This section examines all the security problems and issues related to the Unix environment and provides solutions and tips on how to solve them.

### The Kernel

During this week students examine the kernel, its responsibilities, how it can be configured, recompiled and installed.

### cron, Accounting and Quotas

This is the last week of the "hard" systems administration topics and ties together coverage of cron, accounting, disk quotas and syslog.

### Professional Issues and Revision

The last week is spent covering a variety of professional issues including ethics, professional bodies and other sources of information. The week is also spent doing revision of all previous material.

## Assessment

One of the major aims in designing the assessment for the subject was to prevent the "wait until two days before the exam" approach that most students have towards to study. This subject introduces a great deal of new information that students will not understand unless they use it throughout the semester.

Tables 3 and 4 summarise the assessment methods for both on-campus and distance students.

| Title | Due | Worth |
| --- | --- | --- |
| Class Test 1 | During week 5 | 10% |
| Tutorial Sheets | Through out semester | 10% |
| System Emergency | During week 13 | 10% |
| Log Book | end week 13 | 10% |
| User Documentation | end week 13 | 20% |
| Final Exam |  | 40% |

Table 3 - On-Campus Student Assessment

<td> 40%

| Title | Due | Worth |
| --- | --- | --- |
| Assignment 1 | end week 4 | 10 % |
| Assignment 2 | end week 9 | 10% |
| Assignment 3 | end week 13 | 10% |
| Log Book | end week 13 | 10% |
| User Documentation | end week 13 | 20% |
| Final Exam |

Table 4 - Distance Student Assessment.

The assessment for on-campus students takes advantage of the fact that they have direct access to the lecturer. For distance students the assessment has to be modified to take into account that students must complete it without supervision.

The on-campus class test and the first assignment for distance students concentrates on shell programming and basic UNIX questions. The aim is to ensure that students have mastered these concepts before progressing onto the Systems Administration topics.

Assignments 2 and 3 for distance students and the tutorial questions for on-campus students are designed to force the students to complete the work during semester. As part of the tutorial questions on-campus students, as part of a small group, must design and construct an automated add user script.

The most enjoyable piece of assessment (for the lecturer) is the Systems Emergency session that on-campus students are subjected to during the final week of semester. During Systems Emergency week each student is given an hour to diagnose and remedy a problem on the machine they administer. The systems emergencies are an individual exercise. Systems emergencies provide students with a simulated real-world incident and also provides them a way to demonstrate their understanding of the theory. A recent article in the SAGE-AU newsletter describes the system emergency week in more detail (Jones 95).

The final assignment for both on-campus and distance students has two parts, a log book and a piece of user documentation. Students are expected to maintain a log book throughout the semester that records the work that they carry out. A variety of guidelines to what makes a "good" log book are introduced in Chapter 5 of the text book. Marks for the log book are given on the basis of the amount of work recorded in the log book and the ability for a new Systems Administrator to use the log book to come up to speed with the particular system.

For the user documentation the students are free to pick a topic of their choice, some suggestions include an introduction to awk or vi. The students are then expected to produce good quality user documentation explaining that concept. The quality of the documentation ranges from the very good to pitiful right through to plagiarism.

The final piece of assessment is a closed book, two hour exam that is worth 40% of the assessment. The exam is used to ensure that students actually do know the material. It is closed book because it aims to test knowledge that every systems administrator should know (and because the author writes very easy open book exams).

Students must pass the exam to pass the subject.

While the subject's assessment can provide a good indication of a student's competency with the knowledge of Systems Administration. It does not test whether the student has a the characteristics that make a good Systems Administrator including patience, dedication, curiosity, experience, responsibility, inventiveness, adaptability and creativity.

## Plans for the Future

Plans for the future include

- increasing the use of Internet technologies in the teaching of the subject,
- increasing the interaction between students and more experienced Systems Administrators in an attempt to simulate the master/apprentice relationship,
- modifying the text book to remove a variety of mistakes and to place greater emphasis on Linux specific information,
- streamline and improve the process of distributing, installing and removing Linux, and
- develop the subject as an open learning subject.

While the process for distributing Linux started almost 6 weeks before the start of semester a number of students were still attempting to install Linux in week 2 of semester. For the next offering the letter explaining the need for Linux will be distributed to all students in mid-December, two months before the start of semester. In addition the accompanying installation documentation will be improved and will have material on removing Linux added to it.

One of the major problems that has come to light while marking the exams, especially those from distance students, is the way in which basic concepts have been misunderstood. It is thought that these misunderstandings are caused by

- the absence of effective feedback from an experienced Systems Administrator, and
- the lack of sufficient practical application of the theory.

To solve these problems it is planned to increase the interaction between students and experienced Administrators using the Internet. In addition the assessment will be modified to force students to complete more practical exercises.

### Internet Technologies and Open Learning

Use of Internet technologies promises to revolutionise the way in which distance education is delivered. Plans for 85321 include

- the use of World-Wide Web for the distribution of materials,
- the use of email for the submission and return of assignments,
- the development of a Moo in which to hold virtual tutorials,
- organising guest "lecturers" from the ranks of industry based Systems Administrators (any volunteers?).

The eventual aim is to develop the subject so that it can be offered as an open learning subject. Open learning means that the subject can be started at any time, by anyone, located anywhere and can be completed at any pace. Development of the subject along these lines is being undertaken in conjunction with OpenNet.

### Textbook Modifications

The textbook currently provides coverage of topics for both SysV and BSD versions of UNIX. A number of students have commented on the fact that this leads to some confusion. Due to this confusion and the use of Linux as the major operating system, the text book will be modified to concentrate on Linux information only.

The textbook will also be modified to fix a number of other more mundane problems including

- providing more exercises, questions and their solutions,
- fixing a number of simple typos, and
- also fixing some larger mistakes and a number of oversights.

## Conclusions

The Department of Maths & Computing offers a subject in Systems Administration as part of its Bachelor of Information Technology (System Services stream). The subject has been offered five times and in its latest offering it had an enrolment of 80 students from throughout the world.

The subject is designed to provide students with experience of the field of Systems Administration that they can take into their careers as computing professionals. The curriculum is designed so that students completing the subject should meet SAGE's description of a Junior Systems Administrator.

## Bibliography

Jones, D. (1993). _How do you teach Systems Administration?_ SAGE-AU'93 Conference, Melbourne 1993.

Jones, D. (1995). _Revenge is sweet._ The Australian Systems Administrator, Volume 2, Issue 2.