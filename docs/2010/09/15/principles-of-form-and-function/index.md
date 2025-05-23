---
categories:
- chapter-5
- design-theory
- elearning
- information-systems
- phd
- thesis
- webfuse
date: 2010-09-15 08:49:07+10:00
next:
  text: Alan Kay and some reasons why the educational technology revolution hasn't
    happened
  url: /blog/2010/09/16/alan-kay-and-some-reasons-why-the-educational-technology-revolution-hasnt-happened/
previous:
  text: Portfolios often implemented poorly
  url: /blog/2010/09/14/portfolios-often-implemented-poorly/
title: Principles of form and function
type: post
template: blog-post.html
---
The aim of my [thesis](/blog/research/phd-thesis/) is to formulate an information systems design theory for e-learning. Even though I have a [publication](/blog/publications/the-formulation-of-an-isdt-for-e-learning/) or two that have described early versions of the ISDT, I've never been really happy with them. However, I'm getting close to the end of this process, at least for the purposes of getting the thesis submitted.

The following is a first draft of the "Principles of form and function", one of the primary components of an ISDT as identified by [Gregory and Jones (2007)](http://aisel.aisnet.org/jais/vol8/iss5/1/). I'll be putting up a draft of the principles of implementation in a little while (**UPDATE** [principles of implementation](/blog/2010/09/17/principles-of-implementation/) now up). These are still just approaching first draft stage, they need a bit more reflection and some comments from my esteemed supervisor. Happy to hear thoughts.

By the way, the working title for this ISDT is now "An ISDT for emergent university e-learning systems".

### Principles of form and function

Gregor and Jones (2007) describe the aim of the principles of form and function as defining the structure, organisation, and functioning of the design product or design method. The ISDT described in Chapter 4 was specifically aimed at the World-Wide Web as shown in its title, "An ISDT for web-based learning systems". Such technology specific assumptions are missing from the ISDT described in this chapter to avoid technological obsolescence. By not relying on a specific technology the ISDT can avoid a common problem with design research - the perishability of findings – and, enable the on-going evolution of any instantiation to continue regardless of the technology.

The principles of form and function for this ISDT are presented here as divided into three groupings: integrated and independent services; adaptive and inclusive architecture; and, scaffolding, context-sensitive conglomerations. Each of these groupings and the related principles are described in the following sub-sections and illustrated through examples from Webfuse. The underlying aim of the following principles of form and function is to provide a system that is easy to modify and focused on providing context-specific services. The ISDT's principles of implementation (Section 5.6.4) are designed to work with the principles of form and function in order to enable the design of an emergent university e-learning information system.

#### Integrated and independent services

The emergent nature of this ISDT means that, rather than prescribe a specific set of services that an instantiation should provide, the focus here is on providing mechanisms to quickly add and modify new services in response to local need. It is assumed that an instantiation would provide an initial set of services (see principle 4) with which system use could begin. Subsequent services would be added in response to observed need.

An emergent university e-learning system should:

1. _Provide a method or methods for packaging and using necessary e-learning services from a variety of sources and of a variety of types._  
    For example, Webfuse provided two methods for user-level packaging services: - page types and Wf applications – and also used design patterns and object-oriented design for packging of implementation level services. The types of services packaged through these means included: information stored in databases; various operations on that data; external services such as enterprise authentication services; open source COTS; and, remote applications such as blogging tools.
2. _Provide numerous ways to enable different packages to interact and integrate._  
    Webfuse provided a number of methods through which the packaging mechanisms described in the previous point could be integrated. For example, Wf applications provided a simple, consistent interface that enabled easy integration from numerous sources. It was through this approach that Wf applications such as email merge, course list, and course photo album were integrated into numerous other services. To allow staff experience what students say on StudentMyCQU, the ViewStudentMyCQU application was implemented as a wrapper around the StudentMyCQU application.
3. _Provide a packaging mechanism that allows for a level of independence and duplication._  
    Within Webfuse, modifications to page types could be made with little or no effect on other page types. It was also possible to have multiple page types of the same type. For example, there were three different web-based discussion forums with slightly different functionality preferred by different users. Similarly, the use of the Model-View-Controller design pattern in Wf applications enabled the same data to be represented in many different forms. For example, class lists could be viewed by campus, with or without student photos, as a CSV file, as a HTML page etc.
4. _Provide an initial collection of services that provide a necessary minimum of common e-learning functionality covering: information distribution, communication, assessment, and administration._  
    The initial collection of services for Webfuse in 2000 included the existing page types and a range of support services (see Section 4.4.3). These provided an initial collection of services that provided sufficient services for academics to begin using e-learning. It was this use that provided the opportunity to observe, learn and subsequently add, remove and modify available services (see Section 5.3).
5. _Focus on packaging existing software or services for integration into the system, rather than developing custom-built versions of existing functionality._  
    With Webfuse this was mostly done through the use of the page types as software wrappers around existing open source software as described in Chapter 4. The BAM Wf application (see 5.3.6) integrated student use of existing blog engines (e.g. http://wordpress.com) into Webfuse via standardised XML formats.
6. _Present this collection of services in a way that for staff and students resembles a single system._  
    With Webfuse, whether users were managing incidents of academic misconduct, finding the phone number of a student, responding to a student query on a discussion forum, or uploading a Word document they believed they were using a single system. Via Staff MyCQU they could access all services in a way that fit with their requirements.
7. _Minimise disruption to the user experience of the system._  
    From 1997 through 2009, the authentication mechanism used by Webfuse changed at least four times. Users of Webfuse saw no visible change. Similarly, Webfuse page types were re-designed from purely procedural code to being heavily object-oriented. The only changes in the user interface for page types were where new services were added.

#### Adaptive and inclusive architecture

Sommerville (2001) defines software architecture as the collection of sub-systems within the software and the framework that provides the necessary control and communication mechanisms for these sub-systems. The principles for integrated and independent services described in the previous section are the "sub-systems" for an emergent university e-learning system. Such as a system, like all large information systems, needs some form of system architecture. The major difference for this ISDT is that traditional architectural concerns such as consistency and efficiency are not as important as being adaptive and inclusive.

The system architecture for an emergent university e-learning system should:

1. _Be inclusive by supporting the integration and control of the broadest possible collection of services._  
    The approach to software wrappers adopted as part of the Webfuse page types, was to enable the integration of any external service at the expense of ease of implementation. Consequently, the Webfuse page types architecture integrated a range of applications using very different software technologies including a chat room that was a Java application; a page counter implemented in the C programming language; a lecture page type that combined numerous different applications; and, three different discussion forums implemented in Perl. In addition to the page types, Webfuse also relied heavily on the architecture provided by the Apache web server for access control, authentication, and other services. The BAM Wf application (Section 5.3.6) used RSS and Atom feeds as a method for integrating disparate blog applications. Each of these different approaches embody very different architectural models which increase the cost of implementation, but also increase the breadth of services that can be integrated and controlled.
2. _Provide an architecture that is adaptive to changes in requirements and context._  
    One approach is the use of an architectural model that provides high levels of maintainability through fine-grained, self-contained components (Sommerville 2001). This was initially achieved in Webfuse through the page types architecture. However, in order to achieve a long-lived information system there is a need for more than this. Sommerville (2001) suggests that major architectural changes are not a normal part of software maintenance. As a system that operated for 13 years in a Web-environment, Webfuse had to undergo major architectural changes. In early 2000, performance problems arose due to increased demand for dynamic web applications (student quizzes) resulting in a significant change in Webfuse architecture. This change was aided through Webfuse's reliance on the Apache web server and its continual evolution that provided the scaffolding for this architectural change.

The perspective for this ISDT is that traditional homogenous approaches to software architecture (e.g. component architectures) offer numerous advantages. However, there are some drawbacks. For example, a component architecture can only integrate components that have been written to meet the specifications of the component architecture. Any functionality not available within that component architecture, is not available to the system. To some extent such a limitation closes off possibilities for diversity – which this ISDT views as inherent in university learning and teaching - and future emergent development. This does not rule out the use of component architectures within an emergent university e-learning system, but it does mean that such a system would also be using other architectural models at the same time to ensure it was adaptive and inclusive.

#### Scaffolding, context-sensitive conglomerations

The design of e-learning in universities requires the combination of skills from a variety of different professions (e.g. instructional design, web design etc), and yet is often most performed by academics with limited knowledge of any of these professions. This limited knowledge creates significant workload for the academics and contributes to the limited quality of much e-learning. Adding experts in these fields to help course design is expensive and somewhat counter to the traditional practice of learning and teaching within universities. This suggests that e-learning in universities has a need for approaches that allow the effective capture and re-use of expertise in a form that can be re-used by non-experts without repeated direct interaction with experts. Such an approach could aim to reduce perceived workload and increase the quality of e-learning.

An emergent university e-learning information system should:

1. _Provide the ability to easily develop, including end user development, larger conglomerations of packaged services._  
    A conglomeration is not simply an e-learning service such as a discussion forum. Instead it provides additional scaffolding around such services, possibly combining multiple services, to achieve a higher-level task. While many conglomerations would be expert designed and development, offering support for end-user development would increase system flexibility. The Webfuse default course site approach (Section 5.3.5) is one example of a conglomeration. A default course site combines a number of separate page types (services), specific graphical and instructional designs, and existing institutional content into a course website with a minimum of human input. Another form of conglomeration that developed with Webfuse was Staff MyCQU. This "portal" grew to become a conglomeration of integrated Wf applications designed to package a range of services academics required for learning and teaching.
2. _Ensure that conglomerations provide a range of scaffolding to aid users, increase adoption and increase quality._  
    There is likely to be some distance between the knowledge of the user and that required to effectively use e-learning services. Scaffolding provided by the conglomerations should seek to bridge this distance, encourage good practice, and help the user develop additional skills. For example, over time an "outstanding tasks" element was added to Staff MyCQU to remind staff of unfinished work in a range of Wf applications. The BAM Wf application was designed to support the workload involved in tracking and marking individual student reflective journals (Jones and Luck 2009). A more recent example focused more on instructional design is the instructional design wizard included in the new version of the Desire2Learn LMS. This wizard guides academics through course creation via course objectives.
3. _Embed opportunities for collaboration and interaction into conglomerations._  
    An essential aim of scaffolding conglomerations is enabling and encouraging academics to learn more about how to effectively use e-learning. While the importance of community and social interaction to learning is widely recognised, most professional development opportunities occur in isolation (Bransford, Brown et al. 2000). Conglomerations should aim to provide opportunities for academics to observe, question and discuss use of the technology. Examples from Webfuse are limited to the ability to observe. For example, all Webfuse course sites were, by default, open for all to see. The CourseHistory Wf application allowed staff to see the grade breakdown for all offerings of any course. A better example would have been if the CourseHistory application encouraged and enabled discussions about grade breakdowns.
4. _Ensure that conglomerations are context-sensitive._  
    Effective integration with the specific institutional context enables conglomerations to leverage existing resources and reduce cognitive dissonance. For example, the Webfuse default course site conglomeration was integrated with a range of CQU specific systems, processes and resources. The Webfuse online assignment submission system evolved a number of CQU specific features that significantly increased perceptions of usefulness and ease-of-use (Behrens, Jamieson et al. 2005).

### References

Behrens, S., Jamieson, K., Jones, D., & Cranston, M. (2005). _Predicting system success using the Technology Acceptance Model: A case study._ Paper presented at the Australasian Conference on Information Systems'2005, Sydney.

Bransford, J., Brown, A., & Cocking, R. (2000). _How people learn: brain, mind, experience, and school_. Washington, D.C.: National Academy Press.

Gregor, S., & Jones, D. (2007). The anatomy of a design theory. _Journal of the Association for Information Systems, 8_(5), 312-335.

Jones, D., & Luck, J. (2009). _Blog Aggregation Management: Reducing the Aggravation of Managing Student Blogging_. Paper presented at the World Conference on Education Multimedia, Hypermedia and Telecommunications 2009. from [http://www.editlib.org/p/31530](http://www.editlib.org/p/31530).

Sommerville, I. (2001). _Software Engineering_ (6th ed.): Addison-Wesley.