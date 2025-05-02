---
title: The intervention - Webfuse design 1996-1999
date: 2009-07-27 14:13:34+10:00
categories: ['chapter-2', 'design-theory', 'elearning', 'phd', 'thesis']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: The design and implementation of Webfuse &#8211; Part 1 &laquo; The Weblog
        of (a) David Jones
      author_email: null
      author_ip: 66.135.48.204
      author_url: https://djon.es/blog/2009/07/29/the-design-and-implementation-of-webfuse-part-1/
      content: '[...] Chapter 4 is meant to tell the story of the first iteration of Webfuse
        from 1996 through 1999. The last section I posted describes the design guidelines
        that informed the implementation of Webfuse. This post and [...]'
      date: '2009-07-29 11:28:06'
      date_gmt: '2009-07-29 01:28:06'
      id: '2665'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: Thinking about evaluating Webfuse (1996 through 1999) &#8211; evaluation
        of an LMS? &laquo; The Weblog of (a) David Jones
      author_email: null
      author_ip: 74.200.245.187
      author_url: https://djon.es/blog/2009/07/31/thinking-about-evaluating-webfuse-1996-through-1999-evaluation-of-an-lms/
      content: '[...] worked my way through explaining the context (general context and
        (use of e-learning), the design guidelines and the implementation (parts 1, 2
        and 3). I&#8217;ve now reached the evaluation section, where [...]'
      date: '2009-07-31 13:45:07'
      date_gmt: '2009-07-31 03:45:07'
      id: '2666'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The previous couple of posts ([one](/blog2/2009/07/26/build-it-and-they-will-come-starting-with-the-institution/) and [two](/blog2/2009/07/27/use-of-e-learning-cqu-up-to-1996-or-so/)) described the context in which the Webfuse e-learning system was designed. This focused primarily on the context at CQU up to 1996 or so. These posts form the definition of the problem which Webfuse was meant to address.

This post begins a description of the intervention undertaken to address this problem. i.e. the early design of Webfuse. This post introduces the Intervention section, explains why it was decided to build another system and then outlines the design guidelines that underpinned Webfuse.

### Intervention

As described in the previous section, the problem to be addressed during 1996 was the development of a system, processes and resources to support the use of web-based learning in all of the courses offered by the Department of Mathematics and Computing (M&C) at Central Queensland University (CQU). The same system was also expected to support the operation of the organisational website for the Faculty of Applied Science to which M&C belonged. This section offers a description of the design and implementation of the intervention intended to address this problem.

The description starts with an explanation (Section 4.3.1) of why it was felt to build a CQU specific system rather than use one of the already existing systems. Next, the design guidelines established at the start of the intervention are explained (Section 4.3.2). Following is a detailed description (Section 4.3.3) of the overall design and implementation details of the resulting system – Webfuse – using the design guidelines as an organising structure. A part of the design and implementation section will be a summary of the functionality for e-learning provided by Webfuse during 1996 through 1999.

#### Why build another system?

By 1996, when this work commenced, there were already a number of existing systems offering support for web-based learning. Many of these systems themselves originated as solutions that arose at other universities for this exact problem. Still others were adaptations of CML-based systems to the Interent. For example, Web Educational Support Tools (WEST) was developed at the University College Dublin and during 1996 was being used at the University of Western Sydney (Nepean) (Pennell, 1996). The World-Wide Web Course Tool (WebCT) was developed at the University of British Columbia (Goldberg et al., 1996) and went on to be a successful commercial product used at many universities throughout the world. The decision to engage in the design and construction of a unique system at CQU could be seen as an example of the not invented here phenomenon resulting the reinvention of the wheel (Simon, 1991, p. 130). Which had been recognised as a growing problem with the development of multimedia learning resources (Bryant, 1998; Zelmer, 1996). This section explains how the mix of a number of different factors led to the decision to build another system.

The most obvious factor was the background and discipline mix with the Department of Mathematics and Computing. The computing, or information technology, side of the department included staff with interests and expertise in software development. Some of these staff, including the author, had a history of research interests in the Internet and the application of information technology to learning (Carter et al., 1995; Jones, 1994, 1995). In addition it was thought that the M&C context offered the chance of unique perspectives around e-learning based on a combination of on-campus, distance and international students and a student population with significantly greater computing expertise and access to technology (Jones & Buchanan, 1996). This was backed up existing experience that had already, within a limited time frame, identified features, approaches and ideas that had not yet been implemented in existing systems (Jones & Buchanan, 1996).

This belief that there were still discoveries to be made was based on the perception that the online learning environment was still fairly youthful and that there were new insights to be gained. In 1997, a year after this work commenced, Macpherson et al (1997) identified that experience in teaching and learning online continued to be fragmentary and that few teaching staff had the knowledge to fully assess the implications of online learning or realistically determine possible future applications. The same authors (Macpherson et al., 1997) discovered through experienced one such limitation with WEST (Pennell, 1996), one of the existing systems. The strictly sequential and linear course structure embedded in the system design required the designers to discover ways to subvert it in order to support the nonlinear design approach they were committed to (Macpherson et al., 1997).

For these reasons, it was felt that the design, implementation and use of another online learning environment within the M&C context would, as well as providing support for online learning by M&C staff and students, provide an opportunity to experiment with new services, enable a comparison to be drawn between different systems, identify mistakes to avoid and practices to replicate and hopefully identify unique possibilities for e-learning (Jones & Buchanan, 1996). Lastly, a key guideline for the design of Webfuse was to be "do not reinvent the wheel" (Jones & Buchanan, 1996).

#### Design guidelines

Design of a system, Webfuse, to support learning and teaching within the Department of Mathematics and Computing (M&C) and the broader website for the Faculty of Applied Science commenced in mid-1996. The design guidelines underpinning Webfuse and the associate rationale were outlined in publications written at the time (Jones & Buchanan, 1996; McCormack & Jones, 1997) and others reflecting back on that design after the fact (Gregor et al., 1999; Jones, 1999a, 1999b; Jones & Gregor, 2004, 2006). This section provides an overview of those design guidelines while the following section (Section 4.3.3) explains how those guidelines were implemented through the design and implementation of Webfuse.

**Webfuse will be a web publishing tool**

The problem definition required Webfuse to not only provide online learning services to the students and staff of M&C, but it also had to support the website for the Faculty of Applied Science (and later the Faculty of Informatics and Communication). This meant that from the start Webfuse was envisaged as a Web publishing tool. That is, a system that helps people create and maintain Web pages and Web sites. Webfuse was designed as a general Web publishing tool that also provided a number of specific tools and facilities to support the creation and maintenance of Web-based classrooms (McCormack & Jones, 1997, p. 362).

This is somewhat different to most of the other e-learning systems available at that time. Systems such TopClass and WebCT were designed only for learning and teaching. A consequence of this design was that these systems had a more pre-defined purpose and structure and a subsequent lack of flexibility. As a more general web publishing tool, capable of supporting an organisational website, Webfuse had to satisfy a broader set of requirements.

**Webfuse will be an integrated online learning environment**

It was intended that Webfuse would be a totally integrated online learning environment in that it should provide all of the features and systems required by both students and teachers using a consistent and easy-to-use interface (Jones & Buchanan, 1996). An integrated online learning environment encapsulates a set of tools, systems, procedures and documentation that supports any and all parts of the learning and teaching experience. The implication was that students and teachers could perform all necessary tasks, regardless of technology, via Webfuse.

As part of this e-learning was seen as more than converting lecture overheads and other course resources into HTML and placing them on the Web (Jones & Buchanan, 1996). An integrated online learning environment should provide support for tasks including, but not limited to, assignment submission, automated (self-)assessment, evaluation and both synchronous and asynchronous communication. As an integrated online learning environment Webfuse also had to provide appropriate support for non-Web e-learning. For example, by 1996 M&C was making increasing use of course mailing lists as a means of communication. Rather than require the use of mailing lists to cease, Webfuse should integrate with this use and preferably provide additional functionality.

**Webfuse will be eclectic, yet integrated**

The majority, if not all, of the e-learning systems available in 1996 were tightly integrated systems produced and supported by a single vendor. All additions and modifications to these systems had to be made by the single vendor. While the tightly, integrated nature of these tools meant they were reasonably easy to install, manage and use with the supplied documentation. It also meant that they were less than responsive to new developments from either the broader online community or the local context.

It was recognised from the start of the Webfuse project that it would not be possible for M&C to provide all the necessary human resources to build and maintain a Web authoring tool (Jones, 1999b). A tightly integrated structure with M&C providing all tools would not be possible. M&C would run the risk of either retaining an out of date system because it was too expensive to replace, or having to throw away the investment in a system because it had not kept up with change (Jones & Buchanan, 1996). This was seen as a significant problem because of recent experience with the difficulty CQU and other institutions faced in moving from text-based, computer-mediated communications systems to the more recent Internet system, and also because on-going and rapid change was seen as a key characteristic of the Internet (Jones & Buchanan, 1996). In addition it was recognised that the broader community using the Web would be better able to develop a range of tools, such as web-based discussion or interactive chat systems and that it would be more efficient for M&C to re-use those systems, rather than reinvent the wheel.

Consequently, the focus of the integrated online learning environment would be on providing the infrastructure necessary to integrate existing and yet to be developed Internet and e-learning tools developed by the broader community (Jones & Buchanan, 1996). The M&C OLE would provide the management infrastructure and consistent interface to combine existing tools such as WWW servers, online quizzes, assignment submission, discussion forums and others into a single integrated whole (Jones & Buchanan, 1996). While some components would be developed specifically for the local context, the emphasis should be on integrating existing tools into the OLE (Jones & Buchanan, 1996).

**Webfuse will be flexible and support diversity**

From the start, an ability to handle the diversity and continual change inherent in web-based learning (Jones, 2004) was seen as the key requirement of any web-based learning system. Freedom of choice, for both staff and students, was seen as one of the important advantages provided by e-learning (Jones & Buchanan, 1996). This was in part a reaction to the necessary consistency inherent in large-scale print-based distance education. This need for consistency created a number of problems and issues due to the diversity present in the disciplines, courses, academics and students within the department (Jones, 1996a; Jones & Buchanan, 1996). Less than user-friendly consistency had also previously extended to requiring students to have and to use specific computer platforms while studying at CQU. Flexibility and the ability to change was also seen as important since one purpose of Webfuse was to enable research and experimentation with forms of e-learning. It was important that the design of Webfuse was not frozen before experience gained in using the system was able to inform on-going change.

To achieve the desired levels of flexibility and support for diversity a number of guidelines were adopted. These included (Jones & Buchanan, 1996):

1. do not specifically support any one educational theory;  
    There is a large variety of possible learning theories with different theories being more appropriate depending on the context and individuals involved (Leidner & Jarvenpaa, 1995). Rather than seek to embody the principles of a single learning theory, Wefuse should enable individual academics to use those theories they deem most suitable, and also handle change in preferred learning theories as experience and knowledge expand.
2. platform independence and standards; and  
    In an era of diverse and changing computer platforms placing artifical constrains on the computer platforms that could use Webfuse was seen as unnecessarily restrictive. Dependence on a single or limited number of platforms would restrict choice, limit the number of people that can use the system, and could influence future use of the system as platforms become dated. It was intended that the M&C OLE would use platform independent technologies such as scripting languages and broadly accepted standards.
3. provide the tools, not the rules.  
    Computer systems, unlike human organizations, are rigid and incapable of adaptation on their own and consequently tend to better support the regularities than the particularities of a situation (Harris & Henderson, 1999). For an activity like learning and teaching that is characterised by diversity, rigid computer systems that expect consistent, regular practices are less than appropriate. Strict procedures leave little room for the unique characteristics of individual disciplines, courses, academics and students (Jones & Buchanan, 1996). Where possible, Webfuse should aim to provide the tools to assist in the development of Web-based classrooms, but have sufficient flexibility to enable staff and students to adapt these tools to their personal situation (Jones & Buchanan, 1996).

**Webfuse will seek to encourage adoption**

In 1996, it was recognised that "if you build it, they will come" is not an approach likely to work within an academic environment where staff development and improvements in learning and teaching has been described as "herding cats" (Jones & Buchanan, 1996). It was recognised that once the system is built staff must be: encouraged to use the system, convinced of the system's usefulness, and provided with appropriate training and documentation (Jones & Buchanan, 1996). Design guidelines intended to help encourage use of the system included (Jones & Buchanan, 1996):

- consistent interface;  
    The eclectic, yet integrated guideline requires that Webfuse have a consistent interface and system metaphor for all tools. This should help ease-of-use and subsequently adoption.
- increased sense of control and ownership;  
    One rationale for requiring Webfuse to support diversity and flexibility was so that staff and students could adapt the system to their needs and subsequently encourage a greater sense of control and ownership.
- minimise new skills; and  
    Even in 1996, the students and staff with M&C brought existing experience with computers, software and the Internet. For example, many students already had email accounts and associated email programs. Academics were already using mailing lists and other aspects of the Internet. Rather than reinvent the wheel and force these people to learn new skills and tools, Webfuse should leverage these existing skills, software and processes to minimise the need for new skills and reduce workload.
- automate.  
    Where possible the system should automate those tasks possible while maintaining a balance with other guidelines. This would include both support or administrative services specific to the Web (e.g. HTML validation and link checking) and other higher level tasks such as creating an initial course website.

### References

Bryant, S. (1998). _Overcoming the 'Not Invented Here' Syndrome - Experience with Sourcing Education Multimedia Developed Elsewhere._ Paper presented at the Proceedings of ASCILITE'98.

Carter, B., Lockwood, J., O'Kelly, S., Parry, C., Atkinson, S., Manderson, T., et al. (1995). _CQ-PAN: Putting schools into cyberspace._ Paper presented at the Information On-Line and On-Disk'95, Sydney.

Goldberg, M., Salari, S., & Swoboda, P. (1996). World-Wide Web - Course Tool: An environment for building WWW-based courses. _Computer Networks and ISDN Systems, 28_, 1219-1231.

Gregor, S., Jones, D., Lynch, T., & Plummer, A. A. (1999). _Web information systems development: some neglected aspects._ Paper presented at the Proceedings of the International Business Association Conference, Cancun, Mexico.

Harris, J., & Henderson, A. (1999). _A better mythology for system design._ Paper presented at the SIGCHI conference on Human factors in computing systems: the CHI is the limit, Pittsburgh, Pennsylvania.

Jones, D. (1994). _A workstation in every home!_ Paper presented at the Asia Pacific Information Technology in Education Conference, Brisbane.

Jones, D. (1995). _1000 users on a 486._ Paper presented at the SAGE-AU'95, Wollongong.

Jones, D. (1996). _Computing by distance education: Problems and solutions_. Paper presented at the Integrating Technology into Computer Science Education.

Jones, D. (1999a). _Solving some problems with university education: Part II._ Paper presented at the Ausweb'99, Balina, Australia.

Jones, D. (1999b). _Webfuse: An integrated, eclectic web authoring tool._ Paper presented at the Proceedings of EdMedia'99, World Conference on Educational Multimedia, Hypermedia & Telecommunications, Seattle.

Jones, D. (2004). The conceptualisation of e-learning: Lessons and implications. _Best practice in university learning and teaching: Learning from our Challenges.  Theme issue of Studies in Learning, Evaluation, Innovation and Development, 1_(1), 47-55.

Jones, D., & Buchanan, R. (1996). _The design of an integrated online learning environment._ Paper presented at the Proceedings of ASCILITE'96, Adelaide.

Jones, D., & Gregor, S. (2004). _An information systems design theory for e-learning._ Paper presented at the Managing New Wave Information Systems: Enterprise, Government and Society, Proceedings of the 15th Australasian Conference on Information Systems, Hobart, Tasmania.

Jones, D., & Gregor, S. (2006). _The formulation of an Information Systems Design Theory for E-Learning._ Paper presented at the First International Conference on Design Science Research in Information Systems and Technology, Claremont, CA.

Leidner, D., & Jarvenpaa, S. (1995). The use of information technology to enhance management school education: A theoretical view. _MIS Quarterly, 19_(3), 265-291.

Macpherson, C., Bennett, S., & Priest, A.-M. (1997). _The DDCE Online Learning Project._ Paper presented at the ASCILITE'97, Perth.

McCormack, C., & Jones, D. (1997). _Building a Web-Based Education System_. New York: John Wiley & Sons.

Pennell, R. (1996). _Managing online learning_. Paper presented at the AUSWEB'96. from [http://ausweb.scu.edu.au/aw96/educn/pennell/index.htm](http://ausweb.scu.edu.au/aw96/educn/pennell/index.htm).

Simon, H. (1991). Bounded rationality and organizational learning. _Organization Science, 2_(1), 125-134.

Zelmer, A. C. L. (1996). _The more things change...memoirs of a computer-based educator._ Paper presented at the ASCILITE'96, Perth.