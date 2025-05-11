---
categories:
- chapter-4
- design-theory
- elearning
- phd
- thesis
- webfuse
date: 2009-07-29 16:52:02+10:00
next:
  text: The design and implementation of Webfuse - Part 3
  url: /blog2/2009/07/29/the-design-and-implementation-of-webfuse-part-3/
previous:
  text: The design and implementation of Webfuse - Part 1
  url: /blog2/2009/07/29/the-design-and-implementation-of-webfuse-part-1/
title: The design and implementation of Webfuse - Part 2
type: post
template: blog-post.html
---
This post continues the description of the design and implementation of Webfuse started with [this post](/blog2/2009/07/29/the-design-and-implementation-of-webfuse-part-1/).

### Webfuse will be an integrated online learning environment

The idea of Webfuse as an integrated online learning environment encapsulated three main ideas: there would be a consistent, easy-to-use interface; all tools and services would be available via that interface; and that the system would, where possible, automate tasks for the teachers and students. The design of Webfuse as a web publishing system based on hypermedia templates was designed to achieve this goal.

The primary interface for Webfuse was the web. All services provided by Webfuse were managed and accessed through a Web browser. All services were provided by web pages implemented through hypermedia templates. Templates that could, where appropriate, provide additional support by automating tasks (e.g. the Lecture page type described in Table 4.3). The interface to create, modify and manage the websites was provided by the page update process and the hypermedia templates using the same consistent model.

### Webfuse will be eclectic, yet integrated

The focus of this requirement was to achieve a system that could be more responsive to changes in requirements and the external context through the inclusion of existing services and tools. The eclectic, yet integrated structure of Webfuse was informed by a combination of concepts including: micro-kernel architecture for operating systems, hypermedia templates, and software wrappers. The following provides more detail of this design and how it was implemented and finishes with a complete listing of the functionality provided by Webfuse in the period from 1996 through 1999.

#### Micro-kernel architecture

The kernel of an operating system is the part that is mandatory and common to all software, the idea of a micro-kernel is to minimize the kernel in order to enforce a more modular system structure and make the system more flexible and tailorable (Liedtke, 1995). The micro-kernel approach helps meet the need to cope with growing complexity and integrate additional functionality by structuring the operating systems as a modular set of system servers sitting on top of a minimal micro-kernel (Gien, 1990). The micro-kernel should provide higher layers with a minimal set of appropriate abstractions that are flexible enough to allow implementation of arbriatry services and allow exploitation of a wide range of hardware (Liedtke, 1995).

The initial design of Webfuse included the idea of establishing a core "kernel" of abstractions and services relevant to the requirements of web publishing. These abstractions were built on underlying primitives provided by a basic Web server. Continuing the micro-kernel metaphor, the Webfuse page types were the modular set of system servers sitting on top of the minimal micro-kernel. The initial set of Webfuse "kernel" abstractions were implemented as libraries of Perl functions and included:

- authentication and access control;  
    The services of identifying users as who they claimed to be and checking if they were allowed to perform certain operations was seen as a key component of a multi-user web publishing system. The functionality was built on the minimal services provided by web servers and supplemented with institution specific information, for example, the concepts of courses.
- validation services;  
    In the early days of the Web the primitive nature of the publishing tools meant that there was significant need for validation services such as validating that correctness of HTML and the search for missing links.
- presentation;  
    This encapsulated the Webfuse style functionality that allowed the representation of pages to be changed independent of the content.
- data storage; and  
    Content provided by content experts was a key component of the Webfuse publishing model. Page types needed to be able to store, retrieve and manipulate that content in standard ways.
- page update.  
    The page update process was the core of the Webfuse publishing model. It involved how the content experts provided and managed content and how that content was then converted into a web pages. A part of this aspect of the Webfuse architecture was a specification of how the Webfuse page types would communicate and interact.

#### Hypermedia templates as software wrappers

The simple "TableList" page type discussed above and used to produce the web page shown in Figure 4.1 and the page update form in Figure 4.2 was written entirely by the Webfuse developers. A key aspect of the design of Webfuse was the recognition that there would not be sufficient Webfuse developer time available to allow implementation, from scratch, of all the necessary page types. Especially those page types necessary for more complex functionality, such as synchronous, interactive chat rooms. The idea of implementing hypermedia templates as software wrappers around commercial-off-the-shelf (COTS) software – mostly open source software - was adopted to address this problem.

In software engineering, the term wrapper refers to a type of encapsulation whereby a software component is an encased within an alternative abstraction and it is only through this alternative interface that clients access the services of the wrapped component (Bass et al., 1998, p. 339). A wrapper leaves the existing code of the encapsulated component as is, however, new code is written around it to connect it to a new context (Sneed, 2000). In the case of Webfuse, the hypermedia templates – in the form of Webfuse page types – were used to encapsulate a variety of existing open source software applications and connect them to the Webfuse and CQU context.

Sneed (2000) identifies the introduction of the concept of wrappers with Dietrich, Nackman and Gracer (1989) and its use to re-use legacy applications within an object-oriented framework. Wrappers have also been used in reverse and re-engineering (Sneed, 2000) and security. Wrappers were also one method used by the hypermedia community to integrate complex hypermedia systems with the World-Wide Web (e.g. Bieber, 1998; Gronbaek & Trigg, 1996). Wrappers were also used to integrate third-party applications into open hypermedia systems that emphasize delivery of hypermedia functionality to the applications populating a user's computing environment (e.g. Whitehead, 1997).

In the case of Webfuse the intent was that the Webfuse wrappers would wrap around commercial-off-the-shelf software (COTS) products, mostly in the form of open-source applications. In the mid to late 1990s there was, in part because of the spiraling cost of custom-developed software, a shift on the part of government from discouraging the use of commercial software to encourage its use (Braun, 1999). Increasingly solutions were built by integrating COTS products rather than building from scratch (Braun, 1999). By 2001, Sommerville (2001, p. 34) describes it as more normal for some sub-systems to be implemented through the purchase and integration of COTS products.

Boehm (1999) identifies four problems with the integration of COTS products: lack of control over functionality and performance; problems with COTS system interoperability; no control over system evolution; and support from COTS vendors. The use of software wrappers to encapsulate COTS products into the CQU context and the general reliance on using open source COTS products was intended to help Webfuse address these issues. Another issue that arises when using a diverse collection of COTS products is the significant increase in the diversity and duplication in the user and management interfaces for each of the COTS products. It was intended that the Webfuse page types, in their role as software wrappers, would also be designed to provide Webfuse users with a consistent user interface. A user interface, where possible, which made use of CQU terms and labels rather than those of the COTS product.

Harnessing hypermedia templates, software wrappers and COTS products allowed Webfuse to combine the benefits of hypermedia templates – simplified authoring process, increased reuse, and reduced costs (Catlin et al., 1991; Nanard et al., 1998) – with the benefits of the COTS approach - shorter development schedules and reduced development, maintenance, training and infrastructure costs (Braun, 1999). While the use of open source COTS products provided access to source code and removed the influence of a commercial vendor (Gerlich, 1998), it did increase the level of technical skills required.

One example of the type of COTS product included into Webfuse through the use of software wrappers is the MHonArc email to HTML converter (Hood, 2007). As mentioned previously M&C courses were already making increasing use of Internet mailing lists as a form of class communication. An obvious added service that Webfuse could provide was a searchable, web-based archive of these mailing lists for use by both staff and students. Rather than develop this functionality from scratch a Email2WWW page type was written as a wrapper around MHonArc. The Email2WWW page type also integrated with the Webfuse styles system to enable automatic modification of appearance and was connected with the mailing list system used at CQU and so was able to regularly and automatically update the web-based archives of course mailing lists.

#### Functionality

The complete functionality provided by Webfuse is a combination of the services provided by the Webfuse "micro-kernel" (described above) and the functionality implemented in each of the available Webfuse page types. This section seeks to provide a summary of the functionality available in the Webfuse page types as at the end of 1999 – the end of this action research cycle. The initial collection of page types was designed on the basis of the four major tasks required of a Web-based classroom identified in McCormack and Jones (1997, p. 367): information distribution, communication, assessment, and class management.

The original purpose of the Web was to enable the distribution and access to research information, which means that the Web can be extremely useful for the distribution of information (McCormack & Jones, 1997, p. 13). By the end of 1999 Webfuse had a collection of 11 page types providing information distribution related services. Table 4.3 provides a summary of these page types, their purpose and what, if any, COTS products the page types used for implementation of their purpose. The FAQ page, like a number of other page types, was written by a project student (Bytheway, 1997).

Table 4.3 - Webfuse information distribution related page types - 1999
| Page Type | COTS Product | Purpose |
| --- | --- | --- |
| Lecture, Lecture Slide | Webify (Ward, 2000) for Postscript conversion to slides.   SoX (SoX, 2009) for conversion of audio into various formats   raencoder (RealNetworks, 1996) for audio conversion into Real Audio format    | Convert Postscript file of a lecture (usually generated by Powerpoint) into an integrated collection of lecture slides. Each lecture slide could have audio converted into any one of four available formats. |
| Study guide, STudy guide chapter | None | Conversion of a study guide into chapters of online material broken up into individual pages, single chapter print versions and the production of table of contents and index |
| PersonContent, PersonDetails | None | Display information about teaching staff |
| FAQ (Bytheway, 1997) | None | Creation and management of lists of frequently asked questions |
| Content | None | Enable simple management of HTML content |
| File upload | None | Allow most people to upload files to the web site |
| TableList, Index, ContentIndex | None | Provide mechanisms to create index and associated child nodes in a hierarchical web structure |
| Search | htdig ((The ht://Dig group, 2005) | Search content of site |

Communication is an essential part of the learning experience and a task for which the Web offers a number of advantages and supports through a number of forms (McCormack & Jones, 1997, p. 15). Table 4.4 provides a summary of the five different communication related page types provide by Webfuse by the end of 1999. This list of page types illustrates two points: there are fuzzy boundaries and overlap between these categories and the Webfuse eclectic, yet integrated structure meant it was possible to have multiple page types performing similar roles.

The FormMail page type listed in Table 4.4 could be used as a form of communication but was generally used to perform surveys that could fit under the Assessment category below. Table 4.4 also shows that there were two page types providing web-based discussion boards. Within a few years a third would be added. Each additional discussion board was added as it improved upon the previous functionality. However, it was not necessary to remove the other previous discussion boards and there were instances where this was useful as some authors preferred the functionality of the older versions.

Table 4.4 - Webfuse communication related page types - 1999
| Page Type | COTS Product | Purpose |
| --- | --- | --- |
| EwgieChat | Ewgie (Hughes, 1996) | An itneracitve chat-room and shared whiteboard system |
| WWWBoard | WWWBoard (Wright, 2000) | Web-based asyncrhonous discussion board |
| WebBBS | WebBBS (AWSD, 2009) | Web-based asyncrhonous discussion board |
| Email2WWW | MHonArc (Hood, 2007) | Searchable, web-based archives of mailing list disussions |
| FormMail | FormMail (Wright, 2002) | HTML form to email gateway, implementation of surveys |

Assessment is an important part of every course, it is essential for knowing how well students are progressing (student assessment) and also for being aware how well the method of instruction is succeeding (evaluation) (McCormack & Jones, 1997, p. 233). Table 4.5 provides a summary of the four Webfuse page types associated with assessment that were in place by the end of 1999. Two of these page types (online quiz and assignment submission) are connected with student assessment, while the other two (UnitFeedback and Barometer) are associated with evaluation. The FormMail page type mentioned in Table 4.4 was also primarily used for evaluation purposes and is somewhat related to the far more CQU specific UnitFeedback page.

Table 4.5 - Webfuse assessment related page types - 1999
| Page Type | COTS Product | Purpose |
| --- | --- | --- |
| Online quiz | None | Management and delivery of online quizzes - multiple choice and short answer |
| Assignment submission | None | Submission and management of student assignments |
| UnitFeedback | None | Allow paper-based CQU course survey to be applied via the Web |
| Barometer | No software, but concept based on idea from Svensson et al (1999) | Allow students to provide informal feedback during a course |

Class management involves the clerical, administrative and miscellaneous support tasks necessary to ensure that a learning experience operates efficiently (McCormack & Jones, 1997, p. 289). Table 4.6 summarises the three Webfuse page types associated with class management by the end of 1999. There is some overlap between this category and that of assessment in terms of the management and marking of student assignments.

Table 4.6 - Webfuse class management related page types - 1999
| Page Type | COTS Product | Purpose |
| --- | --- | --- |
| Results management | None | Allows the display and sharing of student progress and results |
| Student tracking | Follow (Nottingham, 1997) | Session analysis of student visits to course web pages |
| TimetableGenerator | None | Allow students and staff to generate a personalised timetable of face-to-face class sessions |

### References

AWSD. (2009). WebBBS.   Retrieved 29 July, 2009, from [http://awsd.com/scripts/webbbs/](http://awsd.com/scripts/webbbs/)

Bass, L., Clements, P., & Kazman, R. (1998). _Software Architecture in Practice_. Boston: Addison-Wesley.

Bieber, M. (1998). _Hypertext and web engineering._ Paper presented at the Ninth ACM Conference on Hypertext and Hypermedia, Pittsburgh, Pennsylvania.

Boehm, B. (1999). COTS integration: plug and pray? _IEEE Computer, 32_(1), 135-138.

Braun, C. L. (1999). _A lifecycle process for the effective reuse of commercial off-the-shelf (COTS) software._ Paper presented at the 1999 Symposium on Software Reusability, Los Angeles.

Bytheway, S. (1997). FAQ Project Report.   Retrieved 29 July, 2009, from [http://web.archive.org/web/19990503041438/webfuse.cqu.edu.au/People/Developers/Scott\_Bytheway/Report/index.html](http://web.archive.org/web/19990503041438/webfuse.cqu.edu.au/People/Developers/Scott_Bytheway/Report/index.html)

Catlin, K., Garret, L. N., & Launhardt, J. (1991). _Hypermedia Templates: An Author's Tool._ Paper presented at the Proceedings of Hypertext'91.

Dietrich, W. C., Nackman, L. R., & Gracer, F. (1989). _Saving legacy with objects._ Paper presented at the Object-oriented programming systems, languages and applications, New Orleans, Louisiana.

Gerlich, R. (1998). _Lessons Learned by Use of (C)OTS._ Paper presented at the 1998 Data Systems in Aerospace, Athens, Greece.

Gien, M. (1990). Micro-kernel architecture: Key to modern operating systems design. _UNIX Review, 8_(11).

Gronbaek, K., & Trigg, R. (1996). _Toward a Dexter-based model for open hypermedia: unifying embedded references and link objects._ Paper presented at the Seventh ACM Conference on Hypertext, Bethesda, Maryland.

Hood, E. (2007). MHonArc: A mail-to-HTML converter.   Retrieved 10 January, 2008, 2007, from [http://www.mhonarc.org/](http://www.mhonarc.org/)

Hughes, K. (1996). EWGIE - Easy Web Group Interaction Enabler.   Retrieved 29 July, 2009, from [http://www.alts.net/Java/Ewgie/docs/](http://www.alts.net/Java/Ewgie/docs/)

Liedtke, J. (1995). On micro-kernel construction. _Operating Systems Review, 29_(5), 237-250.

McCormack, C., & Jones, D. (1997). _Building a Web-Based Education System_. New York: John Wiley & Sons.

Nanard, M., Nanard, J., & Kahn, P. (1998). _Pushing Reuse in Hypermedia Design: Golden Rules, Design Patterns and Constructive Templates._ Paper presented at the Proceedings of the 9th ACM Conference on Hypertext and Hypermedia.

Nottingham, M. (1997). Follow 1.5.1.   Retrieved 29 July, 2009, from [http://www.mnot.net/follow/README](http://www.mnot.net/follow/README)

RealNetworks. (1996). Release notes: RealAudio encoder 2.0 for UNIX.   Retrieved 29 July, 2009, from [http://service.real.com/help/encoder/unix2.0/how\_to.html](http://service.real.com/help/encoder/unix2.0/how_to.html)

Sneed, H. (2000). Encapsulation of legacy software: A technique for reusing legacy software components. _Annals of Software Engineering, 9_(1-4), 293-313.

Sommerville, I. (2001). _Software Engineering_ (6th ed.): Addison-Wesley.

SoX. (2009). SoX - Sound eXchange - Home page.   Retrieved 29 July, 2009, from [http://sox.sourceforge.net/](http://sox.sourceforge.net/)

Svensson, L., Andersson, R., Gadd, M., & Johnsson, A. (1999). _Course-Barometer: Compensating for the loss of informal feedback in distance education._ Paper presented at the EdMedia'99, Seattle, Washington.

The ht://Dig group. (2005). ht://Dig - Internet search engine software.   Retrieved 29 July, 2009, from [http://www.htdig.org/](http://www.htdig.org/)

Ward, S. (2000). Webify: Build web presentations from postscript.   Retrieved 29 July, 2009, from [http://www.fnal.gov/docs/products/webify/webifydoc/](http://www.fnal.gov/docs/products/webify/webifydoc/)

Whitehead, E. J. (1997). _An architectural model for application integration in open hypermedia environments._ Paper presented at the Eighth ACM Conference on Hypertext, Southhampton, UK.

Wright, M. (2000). WWWBoard.   Retrieved 29 July, 2009, from [http://www.scriptarchive.com/wwwboard.html](http://www.scriptarchive.com/wwwboard.html)

Wright, M. (2002). FormMail.   Retrieved 29 July, 2009, from [http://www.scriptarchive.com/formmail.html](http://www.scriptarchive.com/formmail.html)