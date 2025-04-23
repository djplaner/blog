---
title: A work station in every home!
date: 2009-01-02 12:57:34+10:00
type: page
template: blog-post.html
---

See also: [[blog-home | Home]]

David Jones. A Workstation in Every Home!, Asia Pacific Information Technology in Education Conference, Brisbane, July 1994.

## Introduction

The Association for Computing Machinery's 1989 "Task Force on the Core of Computer Science" (Denning 89) reported that computer science consists of three major paradigms: theory, abstraction and design. In defining the three paradigms the task force emphasised that abstraction and design both contain a large practical component.

In their report the task force identified practical reinforcement of computing theory as an essential part of any studies in the computing field. As a result of this report computing departments have subsequently placed great importance on developing methods and applications that provide suitable practical reinforcement (Roberge 91; Hartley 92).

The Department of Mathematics and Computing at the University of Central Queensland (UCQ) faces the added problems of producing systems that provide the necessary practical reinforcement for distance computing students. The Department has a history of producing such systems (Balsys 91; Farrands 92). However the majority of this work has been for first year computing subjects.

A major problem faced by students undertaking distance study of third and honours year computing subjects is access to the computing resources necessary to gain practical application of the theory. In many cases advanced computing subjects require access to powerful computing platforms that many distance students cannot access.

Hence distance computing students are at a disadvantage during the final years of their course. This lack of resources has meant that academics must remove the practical portion that requires capabilities not available to the distance student. The dilemma is then to maintain equality or promote a dichotomy by enabling on-campus students to complete the activity while many distance students cannot.

To address this problem the Department is developing a computing system that provides distance students with most of the capabilities available to on-campus students.

Three possible solutions to this problem are:

- require off-campus students to attend vacation schools where they gain access to the necessary resources;
- make use of computer mediated communications (CMC) to access on-campus machines as proposed by the ADEnet project (Atkinson & Castro, 1991), or
- require that distance students gain access to a more powerful computing platform.

### Vacation Schools

The resource access problem means that vacation schools are a major part of many of the other courses offered for distance study by the University. Courses offered by the Departments of Chemistry and Physics are some examples.

The absence of vacation schools is a feature of the computing degree offered by UCQ. It makes the course accessible to students with families or careers who would find compulsory attendance at vacation schools impossible. The department's aim not to have vacation schools, regardless of other factors, means that this is not an acceptable solution.

### ADEnet and CMC

Distance students have complained about the problems involved in using CMC to connect to UCQ on- campus machines to do simple operations like reply to e-mail and read Usenet news (Oliver 1993). Using the same system to write, test and debug large multi-file and multi-program programming assignments is not possible for distance students with current affordable technology.

### A More Powerful Computing Platform

The third solution would be to replace the existing platform used by distance students with one that is able to perform the necessary functions. The best solution would do this with little extra cost to the student and the department. This is the solution being implemented at UCQ.

## What is wrong with the Current Platform?

The Department recommends that distance students have access to an IBM PC clone running the MS-DOS operating system. Since its introduction the capability of the hardware of this system has developed to a stage where the top-end machines are now in the workstation class. A machine with this level of hardware capability should be able to provide everything required for the study of advanced computing subjects. But it doesn't!

A computer system consists of three components hardware, operating system and application programs. The final power and capabilities of a computer are dependant on the characteristics of each of these three components and the ability of these components to interact. If any one of the components performs badly, or if the interaction between components is inefficient, then the entire computing platform performs badly.

While the hardware of the IBM-PC clone has increased in complexity (many times in some areas) the basic functionality of MS-DOS (the operating system) has not changed. Many distance students own computer systems with the hardware power of workstation class computer but with an operating system that cannot make use of this power.

The problem caused by MS-DOS is not unknown. It has lead to the development of a number of new commercial operating systems: Windows, OS/2, Windows NT, NeXT and various versions of Unix. The main aim of these new operating systems is to make full use of the capabilities of the hardware.

MS-DOS is the bottle neck of our recommended computing platform. By choosing to design our courses for MS-DOS we are placing our advanced distance computing students at a disadvantage.

## Replace the Operating System.

The solution being implemented at UCQ involves replacing MS-DOS with a new operating system. Logistical problems mean that changing the entire platform, hardware and operating system, is not an option. Current students would have to purchase new hardware and the Department would have to invest considerable resources to outfit lecturers with the new platform. The absence of any real alternative hardware platform was also a consideration.

To be of use in advanced computing subjects the replacement operating system would at a minimum have to be a 32 bit operating system providing pre-emptive multitasking, virtual memory, a graphical user interface and a large existing software base. To protect the investment in changing to the new operating system it should have a considerable user base.

Operating systems available for the IBM PC architecture, that meet the minimum criteria are Microsoft Windows NT, IBM's OS/2 and a Unix based operating system. There are numerous commercial Unix operating systems and two free ones (Linux and 386BSD). As most Unix operating systems are fairly similar only Linux is considered below.

## Hardware Requirements.

Each of the possible replacements requires a machine with the more advanced 386/486 or Pentium central processing units. The also have increased minimum memory and hard disk requirements. Table 1 outlines the minimum memory and hard disk requirements for each system.

| Operating System | Minimum Hardware | Preferred |
| --- | --- | --- |
| Windows NT | 8Mb Ram, 80Mb Disk | 12Mb RAM, 100Mb Disk |
|   OS/2 | 4Mb Ram, 60Mb Disk | 8Mb Ram, 80Mb Disk |
| Linux | 4Mb RAM, 50Mb Disk | 8Mb RAM, 80Mb Disk |

Table 1 - Minimum Hardware Requirements.

## Cost to the Student.

In moving to one of the new operating systems all students will have to obtain new software and most will have to upgrade the hardware of their machine. Table 2 summarises estimated costs to the student in moving to a new operating system.

The hardware figure is based on the following assumptions

- that by 1995 the majority of advanced level students will have access to a 386 based machine with at least 4Mb of RAM and 100Mb of disk
- students will use existing drive space (losing other data) and only upgrade RAM to the preferred level. (RAM price is $70 per Mb)

The basis for the software cost is the need for advanced UCQ computing students to have access to C++, Ada and Prolog programming environments. For both Windows NT and OS/2, the local computing dealer could not discover the status of Ada and Prolog environments for these operating systems. So only the C++ compiler cost is included. Public domain C++, Prolog and Ada compilers exist for Linux.

The basis of all costs are quotations provided by a retailer in February 1994. There may be cheaper sources.

| Operating System | Hardware | OS | Software | Total |
| --- | --- | --- | --- | --- |
| Windows NT | $560 | $245 | $245\* | $1050 |
| OS/2 | $280 | $100 | $200\* | $580 |
| Linux | $280 | NIL | NIL | $280 |

\* C++ compiler only, no Prolog or Ada Compiler.

Table 2 - Student Conversion Cost.

## Cost to the Department.

An academic should be able to access the platform used by the student at anytime. Adoption of either Windows NT and OS/2 would mean a substantial investment in software and hardware for the department. To provide this level of service for NT or OS/2 implies providing each academic with a copy on their machine.

Linux on the other hand would require no additional investment. The department already has a number of Linux and other Unix machines which academics can access from their desk. Each academic would not require a copy of Linux on their desk.

## Software Availability.

An operating system is no good without software that uses it. Linux is a full implementation of Unix so it can draw on the huge array of free software available for the Unix operating system. In addition Unix is the operating system used by a significant proportion of University computing departments and the computing industry. There is a huge collection of free software developed by and for the teaching of computer science.

NT and especially OS/2 suffer in comparison. Their relative youth means that there is not a similar large collection of software to draw upon (especially in the academic arena).

OS/2 also faces the white elephant syndrome. It is losing the sales race to the Windows stable and faces possible replacement with the Taligent operating system IBM is co-developing with Apple.

## Linux's Problems.

A solution based on Linux must deal with the following problems:

- Distribution and installation,  
    Current systems are not trivial to install. Extra documentation and assistance must be available to ensure distance students can install the system.
- Increased difficulty,  
    Using Unix can be more difficult than the other operating systems mentioned. Methods of making use simpler need to be developed and used.
- Lack of commercial packages,  
    Linux does not provide application programs with the polish of some commercial counterparts (e.g. word processors, spreadsheets). In a commercial environment this may make a significant difference but for the purpose of teaching advanced computing it is less so.
- Reluctance to use it.

## Conclusion

The UCQ solution will use the Linux operating system. The department will provide free of charge to students the Linux operating system, a graphical user interface (X-Windows based), compilers, a communications program, editors, other software and the data files required for their subjects.

The students will receive the distribution on either floppy disks or CD-ROM depending on their available resources. The system will cost the student nothing and will arrive at the same time as the other study materials provided by UCQ. The aim is that the student will be able to get the system installed and working prior to the semester starting so that they can then concentrate on learning.

Use of the Linux platform is not compulsory for all subjects. Linux and MS-DOS can live together on the same machine and under development at the moment are Linux programs that will enable Linux to execute MS-DOS and Windows programs.

The first test of the Linux based solution will take place with a limited number of distance students studying within the local Rockhampton area during second semester, 1994.

Current distance students suffer problems because they do not have access to a computing platform with the same capabilities as that enjoyed by on-campus students. This results in distance students (or sometimes both distance and on-campus students) missing out on important practical application of theoretical concepts from advanced computing subjects.

The capability of the hardware of the current base computer is equivalent to a small workstation. However this power is not available to the student because of the MS-DOS operating system.

In attempt to remove the resource access disadvantage suffered by distance students the Department of Maths & Computing at UCQ will be providing a distribution of the free Linux operating system to its distance students. This new operating system running (in some cases) on hardware already owned by the student provides them with similar computing capabilities as on-campus students.

The development of the UCQ solution is funded in part by a URG Seed Grant from the Centre of Open and Distance Learning.

## References

Atkinson, R. Castro, A. (1991). The ADEnet Project: Improving Computer Communications for Distance Education Students, In R. Atkinson, C. McBeath & D. Meacham (eds), _Quality in Distance Education: ASPESA Forum_, 11-19

Balsys, R. Clayton, D. LEARNDOS CAL/CML Software to Teach MS-DOS to Distance Students. in Godfrey, R. (ed)., _Simulation and Academic Gaming in Tertiary Education, ASCILITE Proceedings_, 7-16.

Denning, P. et al. (1989). Computing as a Discipline. _Communications of the ACM_, 32(1), 9-23

Farrands, P. Clayton, D. Orchard, R. Using Technology to Enhance the Efficiency and Effectiveness of Teaching Pascal, in Simms R. et al (eds)., _A Future Promised, ASCILITE Proceedings_, 71-77

Hartley, S.J. Experience with the Language SR in an Undergraduate Operating Systems Course.

Oliver, D. (1993) Software Engineering Project Work in Combined Distance and On Campus Modes, _11th Biennial ASPESA Forum_.

Roberge J., Suriano C., (1991). Embedding Laboratories within the Computer Science Curriculum. _ACM SIGCSE Bulletin_, 23(1), 6-10.