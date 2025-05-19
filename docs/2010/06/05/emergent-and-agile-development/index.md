---
categories:
- chapter-5
- design-theory
- elearning
- phd
- thesis
- webfuse
date: 2010-06-05 13:56:20+10:00
next:
  text: Object orientation and design patterns
  url: /blog/2010/06/07/object-orientation-and-design-patterns/
previous:
  text: The road not taken
  url: /blog/2010/06/05/the-road-not-taken/
title: Emergent and agile development
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Course websites and &#8220;libertarian paternalism&#8221; &laquo; The Weblog
        of (a) David Jones
      author_email: null
      author_ip: 72.233.96.144
      author_url: https://djon.es/blog/2010/06/08/course-websites-and-libertarian-paternalism/
      content: '[...] theory was/is that an appropriately skilled group, taking an adopter-focused
        and emergent development approach could develop a default course site that could
        effectively be used by a group [...]'
      date: '2010-06-08 09:28:39'
      date_gmt: '2010-06-07 23:28:39'
      id: '3081'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: Workarounds &laquo; The Weblog of (a) David Jones
      author_email: null
      author_ip: 76.74.255.38
      author_url: https://djon.es/blog/2010/06/13/workarounds/
      content: '[...] section of chapter 5 of my thesis. The aim here is to try and illustrate
        how the combination of the agile and adopted-focused development process of Webfuse,
        when combined with the design of Webfuse [...]'
      date: '2010-06-13 09:21:56'
      date_gmt: '2010-06-12 23:21:56'
      id: '3082'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The following is the second of the sections from my [thesis](/blog/research/phd-thesis/) that describe the various changes made to Webfuse and how it was implemented during the years 2000-2004 (and a bit beyond). It's a rough first draft. The [first section](/blog/2010/06/04/adopter-focused-development-and-diffusion-theory/) describes how the Webfuse development process came to be very focused on the potential adopters of Webfuse. This section describes why and how the Webfuse development process became more emergent/agile.

I continue to hold that the traditional development life cycles (i.e. not adopter focused and not agile) used to implement e-learning within universities are a major problem.

#### Emergent and agile development

Jones and Buchanan (1996) in describing the initial proposed design guidelines for Webfuse have the first guidline as "flexibility and the ability to adapt to change". This was based on the assumption that "the one unchanging characteristic of the Internet, and the computing field in general, is that it never stops changing" (Jones and Buchanan 1996). In describing how to "design for change" Jones and Buchanan (1996) focus on design factors (e.g. separation of implementation from interface and industry standards) and make no specific mention of development processes. As described in Chapter 4, the adoption of a traditional design process based around big up-front design and a long period of stable use significantly limited the flexibility and ability to adapt to change of Webfuse. The processes used to support and develop Webfuse had to change to address this limitation.

Initial moves to change the development process for Webfuse commenced with the development model proposed by Jones and Lynch (1999), in particular with its emphasis on design for repair, rather than replacement. This particular emphasis arose from increasingly familiarity with the design patterns literature (Coplien 1999) that was becoming well known at the time. A process by which system evolution was enabled by continual reflection and modification of the patterns and constructive templates by the development team (Jones and Lynch 1999). During 1999, however, additional ideas of how to modify the Webfuse design and support process arose from insights around emergent development (Truex, Baskerville et al. 1999), what would come to be known as agile development (Highsmith 2000; Highsmith and Cockburn 2001), and eXtreme Programming (Beck 1999; Beck 2000).

Based on those insights, Jones (2000) argues the need for the need to move e-learning system development to emergent develoment. This arugment is based on the long history of failed technology-based innovations in education (Reeves 1999), which fail due to innovators underestimating the consequences of new technologies (Sproull and Kiesler 1991) and a failure to accommodate environmental and contextual factors affecting implementation (Jonassen 1998). The attraction of emergent and agile develoment approaches is that they are based on the assumption that the system developers are continually striving to achieve alignment between the organisation and its information systems (duPlooy 2003).

To some extent, it can be argued that the template based structure of Webfuse provided good support for the goals of emergent development described by Truex et al (1999) as being continual analysis; dynamic requirements negotation; useful, incomplete specifications; continuous redevelopment; and the ability to adapt. However, it was not until late 2000, when the author took on the lead role of an expanded Infocom web team, that concrete steps were taken to adopt emergent development. In part this was done by adopting many of the practices specified by extreme programming (Beck 2000). Adopted practices included the planning game, small releases, system metaphor, simple design, continuous testing, refactoring, continuous integration, coding standards and collective code ownership. Pair programming was used where possible but this was not often. Since not all of the practices of extreme programming were adopted it cannot be (strictly) claimed that the Webfuse development process was extreme programming (Beck 2000). Additionally, there are numerous examples where the development team was unable to maintain the discipline extreme programming requires. However, it is argued in Jones (2003) that an emphasis on code reuse, flexibility, closeness to the user, a test-driven coding style and various other practices provided Webfuse with an agile development process.

Important Webfuse developments that enable this more agile or emergent development process included:

1. Object orientation and design patterns;  
    As described in Section 5.3.3 a new object-oriented design for the Webfuse code, heavily influenced by the design patterns literature, was developed. This change made it significantly easier to adapt and continuously redevelop Webfuse as the Webfuse code became the incomplete specifications.
2. The wf framework;  
    A significant part of the new OO architecture was the wf framework (described in detail in Section 5.3.4) which provided the system metaphor for the development of interactive web applications.
3. Minimum course websites;  
    The minimum course websites (describe in detail in Section 5.3.5), as well as addressing problems of adoption, also provided an important part of the system metaphor.
4. Webfuse's existing architecture, and.  
    The Webfuse "micro-kernel" architecture and its use of hypermedia templates (as described in Chapter 4) provides the foundation for many of the above enablers. The ability to add and modify templates independently significantly enables the ability to design for repair, not replacement.
5. Support of the faculty Dean.  
    At the simplest level, the faculty Dean enabled the adoption of this emergent process through the provision of resources necessary to expand the Infocom web team. More importantly, as described in his writings (Marshall 2001; Marshall and Gregor 2002), the emergent development approach matched his beliefs about the higher education environment and how to proceed within it.

Section 5.3.6 describes a series of workarounds that were made possible by the adopter-focused, emergent development approach for Webfuse between 2000 and 2004.

### References

Beck, K. (1999). "Embracing change with extreme programming." IEEE Computer **32**: 70-77.

Beck, K. (2000). Extreme Programming Explained: Embrace Change, Addison-Wesley.

Coplien, J. (1999). "Reevaluating the architectural metaphor: Toward piecemeal growth." IEEE Software **16**(5): 40-44.

duPlooy, N. F. (2003). Information systems as social systems. Critical Reflections on Information Systems: A Systematic Approach. J. Cano. Hershey, IDEA Group Inc.

Highsmith, J. (2000). Adaptive software development: A collaborative approach to managing complex systems. New York, NY, Dorset House Publishing.

Highsmith, J. and A. Cockburn (2001). "Agile software development: Business of innovation." IEEE Computer **34**(9): 120-122.

Jonassen, D. (1998). Designing Constructivist Learning Environments. Instructional Theories and Models. C. M. Reigeluth. Mahwah, NJ, Lawrence Erlbaum.

Jones, D. (2000). Emergent development and the virtual university. Learning'2000. Roanoke, Virginia.

Jones, D. (2003). How to live with ERP systems and thrive. 2003 Tertiary Education Management Conference, Adelaide.

Jones, D. and R. Buchanan (1996). The design of an integrated online learning environment. Proceedings of ASCILITE'96, Adelaide.

Jones, D. and T. Lynch (1999). A Model for the Design of Web-based Systems that supports Adoption, Appropriation and Evolution. First ICSE Workshop on Web Engineering, Los Angeles.

Marshall, S. (2001). Faculty level strategies in response to globalisation. 12th Annual International Conference of the Australian Association for Institutional Research. Rockhampton, QLD, Australia.

Marshall, S. and S. Gregor (2002). Distance education in the online world: Implications for higher education. The design and management of effective distance learning programs. R. Discenza, C. Howard and K. Schenk. Hershey, PA, USA, IGI Publishing: 21-36.

Reeves, T. (1999). A Research Agenda for Interactive Learning in the New Millennium. Proceedings of EdMedia'99, Seattle, Washington, AACE.

Sproull, L. and S. Kiesler (1991). Connections: new ways of working in the networked organization. Cambridge, MIT Press.

Truex, D., R. Baskerville, et al. (1999). "Growing systems in emergent organizations." Communications of the ACM **42**(8): 117-123.