---
date: 2009-01-02 13:06:50+10:00
title: The design and construction of a simulated operating system
type: page
template: blog-post.html
---
Ron Chernich, David Jones. The Design and Construction of a Simulated Operating System, Asia Pacific Information Technology in Education Conference, Brisbane, July 1994.

## Introduction.

An advanced level computing subject covering the theoretical concepts of operating systems is an essential part of any computing degree (Denning, 1989). The study of computing has three essential paradigms: theory, abstraction and design (Denning 89). An operating systems subject is very heavy on the theory. In such a subject providing the abstraction and design paradigms to enable students to fully understand the theoretical principles involved is difficult (Hartley, 1992. Withers and Bilodeau, 1992. Goh, 1992. Christopher et al, 1993). The provision of these paradigms to distance students is considerably more difficult.

There have been various attempts to solve these problems. The 1992 offering of the operating systems subject of the Department of Maths and Computing at the University of Central Queensland (UCQ) made use of the Process and Resource Management System (PRMS) (Hays et al, 1990). The experience of using PRMS was not entirely successful.

The problems encountered during 1992 resulted in the decision to develop a replacement system, Ron Chernich's Operating System (RCOS) as a student project during 1993. The experiences gathered using PRMS formed the basis of the design. What has resulted is a simulated operating system that

- demonstrates graphically the theoretical concepts of operating systems,
- provides the student with the ability to easily investigate, compare and modify the different algorithms and data structures involved in implementing an operating system,
- demonstrates in a large program the software engineering practices taught in other subjects within a computing degree,
- offers a graphical user interface similar to Microsoft Windows,
- will run on the distance students recommended platform (IBM PC clone running MS-DOS), and
- can and has been transferred to other computer systems.

## Current Teaching Methods.

The study of operating systems involves gaining an understanding of both the responsibilities of an operating system, and the algorithms and data structures used in implementing these responsibilities. In addition a student must understand complex theoretical concepts like processes, mutual exclusion and interrupts and appreciate how changes in implementation can affect the design and performance of an operating system. Methods used to teach a subject in operating systems generally fall into one of four categories.

### Purely theoretical and text book based

This method introduces concepts and explanations with no practical application or demonstration. Many students never fully understand the relevance or meaning of the concepts and theory without the reinforcement and demonstration practical application provides. Many of the text books used in operating systems subjects follow this method (Stallings, 1992. Lister and Eager 1988).

### The use of separate unrelated projects

This method uses separate practical projects to demonstrate a number of the important concepts. The projects do not meld together in any way and generally don't deal directly with an operating system. This method tends to produce students with an understanding of each separate concept but without a grasp on how these concepts fit together to produce an operating system (Withers and Bilodeau, 1992). The students do however gain a good understanding of each particular concept.

### Use of a simulated or cut-down operating system

This method involves the use of a simulated operating system (either in full or in part) which demonstrates the theoretical concepts. Problems faced by this approach include the learning curve associated with the simulation. (Experience with PRMS showed this can be considerable). Additionally the simulation may not exhibit exactly the behaviour of a typical operating system (Withers and Bilodeau, 1992. Goh, 1992. Ramakrishnan and Lancaster,1993). As a result the student must perform the conceptual leap from the performance of the simulation to real operating system behaviour.

### Practical application using a complete operating system

In this method an entire operating system provides a demonstration of the theoretical concepts. Students are able to see a real system and its implementation details (no conceptual leap). However the students must climb an even steeper learning curve than that in the previous method (Kavka et al, 1991.).

In addition, real operating systems can be hard to use. An attempt by UCQ to use the Minix (Tanenbaum, 1987) operating system resulted in many distance students not being able to install Minix let alone observe it in action.

## Why RCOS?

UCQ's use of PRMS proved to be less than a success. On the whole, students appreciated the aims of PRMS but the implementation was disappointing. On the plus side PRMS did assist immensely in the demonstration and understanding of the process concept. The fact that PRMS could provide this assistance, even with its flaws, begged the question of what a more ambitious package could achieve.

Specific problems of PRMS included

- A lack of documentation on the inner workings of PRMS.  
    This meant that an unreasonable portion of the time spent modifying PRMS was learning what parts did what.
- No conceptual separation of the hardware and operating system concepts.  
    Operating systems are part of a close relationship between software and hardware and understanding the intimacy and boundaries of this relationship is important. PRMS made no such separation.
    
- Poor Design.  
    PRMS suffered from numerous bad software engineering techniques including:
    - The widespread use of global variables, a practice discouraged in every programming subject the students take.
    - The high coupling between separate components of the system meant that a slight change in one part of PRMS resulted in unknown changes in other parts.
    - "Hard-wiring" as opposed to relative placement of graphical objects
    - PRMS was not portable. The system made use of functions specific to the Borland C environment. This puts students not using this particular environment at a disadvantage.

## The Design of RCOS.

The decision to design and implement a replacement simulation for PRMS came about in late 1992. The current system is the result of a year long undergraduate project during 1993 with work being continued as an Honours project during 1994. The following list of design criteria is the result of experience using PRMS and consideration of the essential requirements for the subject

All PRMS functions are to be supported or enhanced The concepts PRMS demonstrated (the process life cycle and resource management) are essential concepts in the study of operating systems.

- System to be easily modifiable by the student  
    It is essential for students to be able to modify the code to test the behaviour of different algorithms and/or data structures. The modification of the code should be simple. The aim is to test the student's understanding of operating system concepts, not their programming skills.
- Ability to run on the platform used by UCQ's distance students  
    The Department of Maths and Computing recommends that student must have access to an IBM PC (running MS-DOS) with at least 20Mb of hard drive space and EGA/VGA graphics. The department also recommends that students use the Borland range of compilers.
- The package should be compiler and hardware independent.  
    It is essential that RCOS be able to moved easily to different platforms since some students do not use the recommended platform. Additionally in the next three to five years the recommended platform is likely to change. The fact that RCOS is portable guarantees the large investment of time and effort that has gone into its construction.
- Implemented in C++  
    C++ not only assists in some of the other aims (easily modifiable, portable) it is also a very important language in the commercial environment. By providing students with greater experience in using C++ we are helping their job prospects.
- Ability to perform as a real operating system  
    Rather than be a simulation that only demonstrates part of an operating system RCOS is a complete working operating system. The programs RCOS executes are compiled with an accompanying Pascal-like compiler (based in the native operating system e.g. MS-DOS). Students may write Pascal programs. compile them, and then observe their execution under RCOS.
- Separate hardware concepts from operating system concepts  
    This lack of separation was one of the flaws of PRMS that resulted in generating some student misunderstanding of concepts.
- Emulate a micro-kernel design and device drivers  
    Micro-kernel design is the current favourite method for assembling an operating system. It is important that RCOS mirror the current research and commercial trends.
- The display should not be to "busy" and provide a helpful animation system of operating tasks.  
    The PRMS screen contains a great deal of information. This results in the students having difficulty in following the animation and understanding what is being represented because of an overload of information. RCOS solves this problem by separating related information out into separate screen displays.

## The Final Result.

The resulting system, RCOS, comprises a portable, message driven, multi-tasking operating system that executes programs compiled by an accompanying, portable Pascal-like compiler. The use of specific software design strategies helps to achieve the design goal of both host platform and compiler system independence.

As a pedagogic tool, RCOS is designed as an extensible and flexible tool able to provide animated illustration of internal operating system services, software component relationships and inter program communication. The difficulty of providing a design that can be modified by students to refine aspects of behaviour is addressed by the high degree of modularity provided by C++ objects, along with the extremely low level of coupling provided by a message driven system.

With an almost total absence of global variables, each component is inherently complete, so to modify a part, only that part and the messages it must respond to need be understood by a student. The C++ code implemented uses a type calculus known popularly as "Hungarian Notation". Study of the source code thus has the side-benefit of providing an exposure to this widely used convention.

RCOS will currently work under the MS-DOS or Unix environments. Under MS-DOS the latest compiler from either Borland, Microsoft or Symantic is necessary. The Unix version requires X-Windows and a C++ compiler.

[![RCOS CPU Scheduling screen](images/3155575043_734881cd22_m.jpg)](http://www.flickr.com/photos/david_jones/3155575043/ "RCOS CPU Scheduling screen by David T Jones, on Flickr")

Figure 1 - The CPU Scheduler Screen from RCOS.

## Conclusion

The practical application of theoretical concepts in the teaching of computing is important. The significant amount of work in developing systems for providing this application in a number of computing subject areas, including operating systems, reflects this importance. Through personal experience the authors have viewed the problems and pitfalls of the provision of this experience, especially to distance students. The design and development of a system to provide this practical application in a standard operating systems subject was the response to these bad experiences.

The result is RCOS. A portable, multi-tasking operating system capable of executing programs compiled with a provided Pascal-like compiler and provides a graphical animation of the internal data structures of an operating system. The design of RCOS enables students to replace and experiment with different algorithms and data structures and as a result increases their understanding of operating systems.

## Bibliography.

Christopher, W.A., et al. (1993). _The Nachos Instructional Operating System_. Proceedings of the Winter 1993 Usenix Technical Conference, pp 481-489.

Denning P., et al. (1989). _Computing as a Discipline_. Communications of the ACM, 32(1), pp 9-23

Goh, A. (1992). _An Operating Systems Project_. ACM SIGCSE Bulletin, 24(3), pp 29-34.

Hartley, S.J. (1992). _Experience with the Language SR in an Undergraduate Operating Systems Course._ ACM SIGCSE Bulletin, 24(1), pp 176-180

Hays, J. et al. (1990). _Simulation of Process and Resource Management in a Multiprogramming Operating_ _System._ Proceedings of the 21st ACM Technical Symposium on Computer Science Education, pp 125-

Kavka, C. et al. (1991). _Experiencing Minix as a Didactical Aid for Operating System Courses._ ACM Operating Systems Review, 25(3).

Lister, A.M. Eager, R.D. (1988). _Fundamentals of Operating Systems (fourth edition)_. London: Macmillan Education Ltd.

Ramakrishnan, S. Lancaster, A. (1993) _Operating System Projects: Linking Theory, Practice and Use._ Proceedings of the 24th ACM Technical Symposium on Computer Science Education, pp 256-260.

Tanenbaum, A. S. (1987) _Operating Systems: Design and Implementation._ Englewood Cliffs, NJ: Prentice Hall.

Stallings, W. (1992). _Operating Systems._ New York: Macmillan Publishing.

Withers, J.M. Bilodeau, M.B. (1992). _An Examination of Operating Systems Laboratory Techniques._ ACM SIGCSE Bulletin, 24(3), pp 60-64