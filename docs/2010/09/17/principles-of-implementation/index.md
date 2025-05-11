---
categories:
- thesis
date: 2010-09-17 11:00:35+10:00
next:
  text: Justificatory knowledge
  url: /blog2/2010/09/17/justificatory-knowledge/
previous:
  text: Alan Kay and some reasons why the educational technology revolution hasn&#039;t
    happened
  url: /blog2/2010/09/16/alan-kay-and-some-reasons-why-the-educational-technology-revolution-hasnt-happened/
title: Principles of implementation
type: post
template: blog-post.html
---
The following is the other main component of the ISDT for e-learning I'm working on. A [prior post](/blog2/2010/09/15/principles-of-form-and-function/) focused on the principles of form and function (i.e. the structure of an information system, the product), the following focuses the principles of implementation (i.e. the process).

While both these posts are based on a bit of prior work, the current formulation of the principles are very much a first draft (not only the principles themselves, but the expression as well). I'll be coming back to them and welcome feedback.

The biggest worry I have at the moment with the following is that it doesn't express strongly enough the need for "end-user development" (i.e. enabling academics/students to do much of this themselves), while balancing that with a need (or perhaps the point) of having a specific support team. Need to work on this.

Much of the following is based on experience, but there are also theoretical justifications, that's another section that is coming.

### Principles of implementation

As defined by Gregor and Jones (2007) the principles of implementation specify "the means by which the design is brought into being". The previous iteration of this ISDT described in Chapter 4 was extremely limited in terms of principles of implementation. This represented the implicit and naïve use of traditional software development methodologies during the initial implementation of Webfuse from 1997 through 1999. As described in this chapter a significant amount of work associated with Webfuse after 1999 has been aimed at developing more appropriate principles of implementation for university e-learning. The result is a rejection of more traditional, plan-driven approaches to information systems implementation, and, instead a set of implementation principles that are founded heavily on the ideas of adopter-focused and emergent approaches to information systems development. The following principles of implementation for the "ISDT for emergent university e-learning systems" are grouped and described in the following three sub-sections.

#### Multi-skilled, integrated development and support team

An emergent university e-learning information system should have a team of people that:

1. _Is responsible for performing the necessary training, development, helpdesk, and other support tasks required by system use within the institution and contains an appropriate combination of technical, training, media design and production, institutional, and learning and teaching skills and knowledge._  
    The merging of these tasks into a single integrated unit avoids problems that arise when such responsibilities are spread across different organisational units. For example, the Infocom web team (the group supporting Webfuse from 2000 through 2004) was responsible for all these tasks and were co-located within a single building. This enabled significant opportunities for knowledge sharing and team building. It also meant that people providing training and support for the system were generally developers of the system with a much greater understanding of what was possible and what could be changed.
2. _Integrated into the everyday practice of learning and teaching within the institution and cultivates relationships with system users, especially teaching staff._  
    Being regularly involved with teaching staff in their daily practice enables the building of trust through shared problem-solving and greater insight into the problems and experience of system users. A necessary foundation on which to implement an adopter-focused and emergent development approach. For example, the Infocom web team provided services, including helpdesk, that were used throughout the learning process and, as a result, they interacted with academic staff and students everyday.
3. _Are empowered to make small-scale changes to the system in response to problems, observations, and lessons learned during system support and training tasks rapidly without needing formal governance approval._  
    The ability to make visible changes to systems in response to user problems or requests that provide a sense of user-involvement and lead to feelings of trust. Traditional governance processes can slow down and even prevent small-scale changes ever happening. The Infocom web team was free to make minor changes to Webfuse as soon as possible given other workload constraints. In many cases the developers would make these changes in order to prevent repeated helpdesk queries about the issues. Behrens (2009) quotes a manager in CQU's IT division describing the types of changes made to Webfuse as "not even on the priority radar" due to traditional IT management techniques and quotes a Webfuse user as saying "You felt really involved".
4. _Actively examines and reflects on system use and non-use – with a particular emphasis on identifying and examining what early innovators - to identify areas for system improvement and extension;_  
    While the Webfuse default course site approach provided an initial structure for course sites, this structure could be significantly modified through use of the page types or real course sites (Section 5.3.5). Observing what changes were being made, typically by innovative users, was a useful way of identifying improvements. For example, the addition of a study schedule page to the default course site arose from observing its use in non-default course sites.
5. _Plays a significant part of the governance process. This enables the governance process to harness the detailed insight into user experience with the system to inform decisions about system evolution._  
    For example, governance of Webfuse was, for a short period of time, implemented using a representative committee of faculty staff that met each month. At those meetings, the Infocom web team would present a summary of what it had done in the previous month and, based on directions given by senior management (top-down) and insights gained from observation of system use (bottom-up), present a draft plan for the next month. Members of the governance group would comment and suggest changes to the plan.

#### An adopter-focused, emergent development process

Software development performed as part of an emergent university e-learning information system should:

1. _Adopt the goals, perspectives and techniques associated with alternate information systems development perspectives and methodologies such as emergent development (Truex, Baskerville et al. 1999), ateleological design (Introna 1996), and agile development methodologies (Highsmith and Cockburn 2001)._  
    As described in Sections 5.3.2, from 2000 onwards Webfuse development was increasingly informed by an emergent development approach using practices associated with eXtreme programming (Beck 1999).
2. _Use in-depth knowledge of the human, social and interpersonal aspects of the institutional context to inform the design and dissemination of new system features with the intent of encouraging greater levels of adoption by users._  
    As outlined in Section 5.3.1, Webfuse development was informed by an adopter-focused approach.
3. _Maximise the ability of the system to be tailored for and by the users of the system._  
    End-user development is perhaps the ultimate adopter-based development process as end-users develop applications in response to their own needs and perspectives. However, even with systems that enable end-user development there remains a need for effective and appropriate interaction between end-users, system owners and system developers (Eriksson and Dittrich 2007).
4. _Seek to establish a balance between the internal emergent process and external plan-driven processes._  
    The title and the majority of the principles of this ISDT suggest that e-learning should adopt an emergent process. This ISDT seems to be heavily in what Clegg (2002) describes as the "learning school" of thought around process (see Section 2.4.1 for a discussion of the two predominant views on process). However, as shown in Section 2.4.2 the majority of processes within universities continue to adopt, or at least espouse, a heavy emphasis on plan-driven processes. While these perspectives represent divergent ways of understanding process, there are risky extremes inherent in both approaches that need to be avoided (Jones, Luck et al. 2005). An instantiation should seek to achieve an appropriate synthesis between the two approaches that enables adaptability and inclusiveness within an appropriately efficient and sufficiently resourced framework that is moving towards institutional goals.

#### A supportive organisational context

The organisational context in which an emergent university e-learning information system is used should:

1. _Have senior management and an organisational culture that understands, accepts, and actively enables and encourages an emergent approach to e-learning._  
    As briefly described in Section 5.5 the emergent development of Webfuse was most effective when the faculty Dean recognised and supported and the benefits of emergent development and what is means and requires. A leader or organisational culture that places significant value on consistency, efficiency and more plan-based processes will not value the characteristics of emergent development.
2. _Use an approach to governance that encourages decentralised control while maintaining an appropriate, but minimal, level of top-down control._  
    A description of the governance process used by Webfuse is provided in

### References

Beck, K. (1999). Embracing change with extreme programming. _IEEE Computer, 32_, 70-77.

Clegg, S. (2002). _Management and organization paradoxes_. Philadelphia, PA: John Benjamins Publishing.

Eriksson, J., & Dittrich, Y. (2007). Combining tailoring and evolutionary software development for rapidly changing business systems. _Journal of Organizational and End User Computing, 19_(2), 47-64.

Gregor, S., & Jones, D. (2007). The anatomy of a design theory. _Journal of the Association for Information Systems, 8_(5), 312-335.

Highsmith, J., & Cockburn, A. (2001). Agile software development: Business of innovation. _IEEE Computer, 34_(9), 120-122.

Introna, L. (1996). Notes on ateleological information systems development. _Information Technology & People, 9_(4), 20-39.

Jones, D., Luck, J., McConachie, J., & Danaher, P. A. (2005). _The teleological brake on ICTs in open and distance learning._ Paper presented at the Conference of the Open and Distance Learning Association of Australia'2005, Adelaide.

Truex, D., Baskerville, R., & Klein, H. (1999). Growing systems in emergent organizations. _Communications of the ACM, 42_(8), 117-123.