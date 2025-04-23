---
title: How do you teach Systems Administration?
date: 2008-12-08 12:30:55+10:00
type: page
template: blog-post.html
comments:
    []
    
pingbacks:
    []
    
---

See also: [[blog-home | Home]]

David Jones, How do you teach Systems Administration?, Presented at SAGE-AU'93, University of Melbourne, Melbourne.

## Abstract

Systems Administration is one of the more complex tasks a computing professional can be asked to undertake. To be a good Systems Administrator it is necessary to have knowledge from the fields of operating systems, programming languages, networks and computer communications, user education and general management and interpersonal skills.

Generally people who are not System Administrators do not see the complexity in the position. Consequently the education of administrators is generally not carried out in anything approaching a formal manner. However the increasing emphasis on efficient usage of expensive and complex computer systems has made business (and academia) aware of the importance of having fully trained, experienced System Administrators.

This paper will reflect on how System Administrators have been trained in the past. Discuss the development of a Univesity level course in Systems Administration at the University of Central Queensland and reflect on the future of Systems Administration education.

## Introduction

During the last two academic semsters an informal special topic subject in Systems Administration has been run for third year computing students (both computer science and information systems students) at the University of Central Queensland. Initial interest in the subject was caused by computing students reading job advertisements and noting the increasing requirement of Unix skills. As the University did not have any sort of decent advanced Unix subject the subject Systems Administration was created.

At the end of 1992 the Department of Mathematics and Computing held a two day long workshop aimed at redesigning the department's Computing degree. As well as academics from UCQ a number of invited local industry representatives attended and spoke on what they wanted from our graduates. EVERY industry representative commented on their decreasing (though still existant) requirement for straight programmers and the increasing requirement for graduates with the ability to manage and maintain their computer systems.

This trend is not limited to the Central Queensland area. You only need look at the position vacant advertisements in Tuesday's Australian to see the increased need for System Administrators, Network Managers and the like.

In response to this need the Departments new Computing degree will consists of two possible streams, a Software Engineering stream and a System Services stream. The System Services stream is aimed at fulfilling the industry requirement for someone to manage and maintain their computer systems. As part of this new System Services stream there will be a formal subject, 85321, Systems Administration.

The way in which the education of System Administrators has progressed from a haphazzard every one for themselves approach to a "formal" University education parallels the way in which code cutting has evolved into Software Engineering. As the discipline has become more complex and more financially important it has been recognised the formal training/education is essential.

## How do System Administrators Learn?

In the past there have been two basic methods by which new System Administrators learn how to fulfill their job description. These methods can be described as the **Apprenticeship**, the **Spare-timer** and the **Teritary Education Experience**.

### The Apprenticeship

This method is where the greenhorn System Administrator is put into the care of a gentle, hugely experienced guru who guides the appretices development from novice to master. In a perfect world this would possibly be the best manner in which to train System Administrators.

The apprentice gains experience from a real system as they are slowly weaned from easy tasks to the more difficult. Always with the fallback of being able to question the master if something goes wrong or they get stuck. Apprentices get to see a real working system in action and the problems and subtelties of such a situation and how they can be handled and solved.

Of course this method has problems

- By definition experience System Administrators are busy  
    The master must discover the apprentices basic knowledge. Discover and assign jobs which they can handle and learn from. Be available to fix problems and answer questions.
- Not everyone is a good teacher  
    
    Even though a Master System Administrator should be, not everyone has the ability to be a good teacher.
- Small sites often can't justify a Master and an apprentice  
    Some sites can't even justify one System Administrator.

### The Spare Timer

This is the professional who comes to work on Monday and finds 10 boxes labelled "Sun Sparcstation" sitting in their office. The boss pops their head around the corner, "Oh, by the way. Can you get those turned on and connected to the network by this afternoon? Thanks."

They then resort to manuals, reference books and commerical course to develop their Systems Administration skills.

### The Teritary Education Experience

The approach being used at UCQ is basically a formalised version of the Apprenticship scheme. The theory is presented and tested and then shown in operation on a "real" working system. The advantages over the Apprenticship scheme are

- the master's job is to teach Systems Administration
- they have experience and abilities in teaching (this is the theory anyway)

- sufficient resources have been provided solely for education

## What makes a good System Administrator?

Before any decision can be made about how to "teach" Systems Administration some idea must be formulated about what qualities and talents make a good Systems Administrator. As part of the initial preparation of this subject a message was posted to the newsgroup COMP.UNIX.ADMIN asking this and other questions. The following table lists the qualities specified by the respondees

| patience | dedication | curiosity |
| --- | --- | --- |
| steady under pressure | anal retentiveness | patience |
| experience | good diagnostic skills | willingness to help others |
| responsibility | patience | inventiveness |
| problem solving skills | adaptability | ability to learn |
| solid knowledge of unix | creativity | patience |

**Table 1. 
What makes a good System Administrator.**

As well as these basic personal attributes a System Administrator should also have strength in numerous technical areas. Just what these areas are and their relative importance are will be discussed later.

The students who take 85321 are shown the following list of attributes of a good system administrator

- Knows where everything is and how everything works. If they don't they can find out.

- Loves people and computers and can talk to both
- Never gives up, never gets angry and never hates users
- Has at least two or three years experience

Once it is known what must be produced it is just a simple task of working out how we provide all these attributes, skills and qualities in a 13 week, one semester subject.

**How should students be taught to become System Administrators?**

The following quote offers some insight into one perspective (Asbell, 1992)

> "Training is no substitute for experience."  
> "Good judgement comes from experience. Experierence comes from bad judgement."

Good Systems Administrators are not made from listening to 26 hours of lectures. They are produced from a good introduction to the concepts followed by repeated and wide ranging real-life experience. This is the basic thought behind the way in which 85321 is taught.

## The Old Way

The first two offerings of the subject were characterised by

- A small, motivated enrollment
    
    During the first semester there were 5 enrolled students, during the second there were 8. These students were generally brighter and better motivated than the rest of the student population.
    
    This was a definite advantage which meant less supervision of individual students was needed and more direct feedback was possible.
    
- An informal presentation
    
    The small numbers and the fact that the subject was being taught in addition to a normal teaching load meant that the presentation was less formal than other subjects.
    
    Both a disadvantage and an advantage. Informality meant that some topics were not emphasised enough but it also produced students able to learn by themselves.
    
- Students had root privilege from the start.
    
    The students had the root password on a number of machines from the start of the semester (with which to hang themselves).
    
    A disadvantage. Students were able to experiement with things that they were not fully aware of. Often with disastarous results.
    

- Students were also group administrators.
    
    The student administrators worked as a group and were responsible for deciding who would what and when.
    
    This extra managerial responsibility combined with the problem of learning the basic concepts tended to overload the students. A disadvantage.
    
- User accounts were provided for informal use.
    
    Other students were given accounts on the machines for informal use.
    
    A disadvantage. The users didn't require the accounts to complete any academic task which meant they had little reason to use the accounts. This meant that account usage was low and consequently the student Adminsitrators did not have the pressure of keeping the machine ticking over for users.
    

## The New Way

Past experience and changing conditions mean that when the subject is offered next semester there will be a number of changes. These changes include

- An increased enrollement.  
    
    Current figures indicate about 25 students taking the subject. This means the subject loses its informality and should produce more technically competent administrators.
    
- A formal presentation.
- Students will not have the root password (at the start).  
    Students will be given increased access as they learn how to and how not to use it. The sudo command will be used to restrict access until the students are given full root access.
- "Real" users will be using the machines.  
    
    At least one of the machines that the student administrators will be managing will have users who are doing regular, important work with their accounts. This should stress the importance of being careful and respecting users. It will also introduce another level of complexity.
- Students will not be group managers.  
    The students will still carry out work as members of a group but the burden of group managment will be lightened a great deal. Providing the students the experience of group work with out the organisational hassles.

There are a number of restrictions in which the subject must operate

- The students are assumed to have absolutely no knowledge of Unix.  
    
    There is half of a first year subject which provides a brief introduction to Unix. By the start of second year the students have forgotten everything. The subject is also taken by Information Systems students from the Faculty of Business who have only just grasped the concept of files and directories.
- Students (people) generally don't fulfill all the qualities listed in Table 1  
    Does anyone have these qualities now. Let alone when they were twenty or twenty-one.
- There isn't time in 13 weeks to cover every possible topic  
    For Systems Administration there is a total of fifty-two hours contact per semester in which concepts have to introduced, reinforced and assessed. You can't do everything.

- The student's knowledge must be assessed.  
    There must be something to show people at the end of semester to justify the grade given to a student.

Given the fact that you can't perform miracles the aim of the Systems Administration subject at UCQ is not to produce a master System Administrator. Rather the aim is to produce apprentices who have the attributes, potential and the required knowledge to become master System Administrators given the experience.

## What topics should be covered?

Next semester the following list of topic areas will be covered in the subject. They are listed in roughly the order they are presented. The relative lateness of backups may surprise. The main reason for this are two-fold

1. because of available equipment all backups must be done over the network. Which means some prerequisite knowledge must be imparted first.
2. the nature of assessment means that some topics (e.g. software porting) must be covered earlier rather than later.

During the weeks leading up to when backups are formally covered the students will be expected to perform and existing backup stragtegy as operators (no knowledge of how or why). Right from the start of the semester the importance of backups is stressed.

| Topics Covered in 85321 |
| --- |
| Introductory Unix and Administration Procedures   System startup and shutdown   User administration    Installing devices   Disk drives and file systems   Networking   Software management and porting   Backups   Security    Accounting, quotas, daemons and crontab   Professional ethics and self-teaching    |

**Figure 2.**

This list of topics has developed from a combination of suggestions from the Internet (Administrators and SAGE-EDU), topics out of Adminstration texts and experience over the last two semesters. It is by no means finalised or perfect and it will no doubt be modified in the future.

## How do you know someone is a good Systems Administrator?

It was recognised from the start that the traditional tertiary subject format of lecture, tutorial, assignment and exam is far from the ideal method to train or assess System Administrators. A hundred percent on a three hour, closed-book exam does not demonstrate an ability as a Systems Administrator. This means that some new methods of assessment must be used to test a students abilities.

Assessment methods which have and will be used include

- written assignments  
    
    A two thousand word report on some technical or relate topic designed to show an understanding of the subject and an ability to communicate ideas.
- software porting and installation  
    Porting, installing and preparing the user documentation on a/many software packages.
- verbal reports  
    Presentations to staff, students and the Administration group on various topics.

- system emergencies and group problem solving sessions  
    Practical sessions on the computer attempting to solve induced system emergencies and problems. Designed to demonstrate group and individual, analytical and problem solving skills.
- tutorials and class tests  
    Used to reinforce understanding of concepts and theory.
- log books  
    
    Used to record the amount and type of work carried out by the student through out the semester.
- personal interviews  
    Individual interviews with students to assess their knowledge as well as their thoughts on other members of their groups.
- lecturer observations  
    Observations made during semester of student progress and contribution to the subject.

## What do people think?

Is University education of System Administrators a good idea? That would appear to be the important question. The answer to the question depends on who you are and what you do.

### Students

Simply love the subject. It is a subject which they see as relevant to the real world and enjoyable and so they usually have no trouble in getting motivated to learn. They enjoy the variety and complexity of problems, the human contact and also the feeling of ownership of there machine ("that's my baby.").

Every student who has completed the subject has said they would rather be a System Administrator than a straight programmer. This is shown in the grades they achieve.

The intelligent and hardworking students continue to get the good grades they attain in other subjects. The intelligent but unmotivated (lazy) students are motivated by the subject and obtain much improved grades. While the students with less ability tend to show a slight improvement in their grades.

### Academics

Once the complexity of the job of a System Administrator is explained and words like problem-solving, group work and human communication are mentioned academics tend to see the usefullness in the subject. Some still shudder at the mention of that four letter word, Unix.

### System Administrators

The responses received from administrators on the Internet and locally can be generalised by the following.

- surprise  
    _"Really? Wow! I'm impressed; most university curricula (...) are woefully short on such 'real world' material"_
- jealousy  
    
    _"I didn't know much when I started (except vi and where the manuals were)"_
- congratulatory  
    _"An excellent idea.."_  
    _"Hmm, this sounds like a good way of getting unpaid lab assistants 8-)."_

## What happens in the future?

All the formal subjects offerred by the Maths and Computing Department at UCQ must be offerred both to internal on-campus students and to external distance students. In 1994 selected external computing students will be allowed to enroll in Systems Administration.

There are two major problems to be overcome in offering this subject at a distance

- root access to a Unix box  
    Very few of our students will have this kind of access and the subject cannot be properly taught without such access. This means the Department must provide this access. Since our students are required to own an IBM PC clone we will be making available the free 386 based operating systems Linux and 386BSD.
- lack of group interaction  
    
    Modems and other forms of communication will hopefully reduce this problem.

## Conclusion

There are obvious parallels between the development of the Software Enginering profession and the continuing development of System Administration. With the increasing economic importance and the complexity of proper systems administration the current trend to the formalising of the education of Systems Administrators will keep growing. In fact with the development of professional bodies like SAGE and SAGE-AU it is not unforseeable that people wanting to enter the System Administration field will be required to have formal qualifications.