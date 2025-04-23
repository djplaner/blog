---
title: "Web Information Systems Development: Some neglected aspects"
date: 2008-12-31 14:45:55+10:00
type: page
template: blog-post.html
---

See also: [[blog-home | Home]]

Shirley Gregor, David Jones, Teresa Lynch, A. Alison Plummer, Web Information Systems Development: Some neglected aspects, in Don Schwartz, Glen Earl (editors), Proceedings of the International Business Association Conference, Cancun Mexico, May 1999, pp 175-187

## Abstract

Although there is increasing development of Web-based information systems (WIS) for business and e-commerce applications, many of the lessons learned from previous information system development failures appear to have been neglected. This paper reviews the literature in the areas of interorganizational systems (IOS), organizational behavior, information system development (ISD), human computer interaction (HCI) and hypermedia to develop a synergistic view of past mistakes and future directions. It is suggested that when developing WIS, particular attention should be paid to the social and political aspects of interorganizational systems, to human-computer- interaction issues and usability guidelines, and to issues associated with the development of hypermedia systems.

## Introduction

An increasing number of information systems are being built based on World Wide Web technology and such systems can lead to high return on investments (Turban et al, 1999). As experience with these Web Information Systems (WIS) increase, it is of interest to reflect on the methods by which they are constructed. Questions of interest include; the extent to which methods used with more traditional systems can be applied or adapted, and the extent to which new and different methods must be found.

Isakowitz et al (1995), see WIS as encompassing four general types of system:

1. _Intranets_, to support the internal work of an organization;
2. _Web-presence_ sites that are marketing tools to reach consumers outside the organization;
3. _Electronic commerce_ systems that support consumer interaction, such as online shopping; and

5. _Extranets_, a blend of internal and external systems to support business-to-business operations.

These authors believe that WIS are different from traditional information systems (IS) in that they have the potential to reach a much wider audience, and they are usually a result of grass-roots efforts versus managerial edict. These differences introduce “managerial and technical challenges” and “require new approaches to design and development” (Isakowitz et al, 1998 p. 78).

Although WIS differ from IS, it appears unwise, however, to neglect areas where what has been learned in the past can give guidance in the development of successful WIS. For example, in spite of continued heavy resource expenditures by organizations to develop IS, a high percentage of these information systems still fail. Partly in response to this high rate of failure, Information Systems Development (ISD) research has become a major research area within the discipline of Information Systems. From this research, more participatory and user-oriented approaches have recently gained much attention in the ISD literature with their focus on organizational versus technical aspects and their potential to increase the likelihood of systems success. Even with the differences of WIS compared to IS, if organizational aspects are not taken into account in design and development, there is no reason to believe that WIS will have a higher success rate than any other type of system implementation.

Therefore, in this paper we examine the characteristics of WIS and argue that some particular lessons from the past should not be ignored, specifically the organizational context and development methodology. Important characteristics of WIS that have implication for development method and practice include but are not limited to:

- many WIS are _interorganizational_ systems (IOS) (or extranets);
- the WIS that are _intraorganizational_ (intranets) are likely to be organization-wide, and involve many different sub-units within an organization;

- users of a WIS are likely to have varied backgrounds and computer experience, and to be geographically and culturally dispersed;
- reliance on the underlying Internet platform, with accompanying technologies, standards, and tools;
- reliance on hypermedia for linkage mechanisms;
- the existence of common interface(s) in the form of Web browsers.

In the remainder of this paper we use the characteristics of WIS to show where experiences in the past can give guidance for the development of WIS under the headings:

1. system context;
2. relevant development methodologies (including human-computer interaction issues); and
3. hypermedia and implementation issues.

## WIS -- Organizational contextx

Many WIS, because of their base on the Internet, are actually interorganizational systems (IOS), that is; they are systems that involve information flow among two or more organizations. In addition, even WIS that are developed within one organization (intranets) are likely to be enterprise-wide and involve many different departments and sub-units within an organization. These intranets may share some of the characteristics of IOS as they may involve a number of groups with different agendas and interests, possibly even groups who feel in competition with each other. Thus, experiences in the past with the development of IOS should be reflected upon. There was considerable experience with IOS before the Internet gained in popularity, in many cases with systems running on value-added networks. The types of systems included in IOS are electronic data interchange (EDI), electronic funds transfer (EFT), electronic forms, integrated messaging, and shared databases (Turban et al., 1999). It is to be expected that lessons learned in the development of these IOS may yield guidance for the newer IOS based on the Internet.

Sprague and McNurlin (1993) list the distinguishing characteristics of IOS as:

- the cooperation of two or more partners in the development of the IOS;
- the use of standards for the external trading environment;

- education of trading partners in technologies and procedures;
- the need for third parties such as communication carriers to link trading partners;
- the need to synchronize development effort among the trading partners, especially when standards require updating;
- the need to re-evaluate business practices to improve efficiency of operation among the organizations,
- the discovering of relationship issues that are often more complex than technical issues, requiring re-evaluation of practices by the trading partners;

- a perceived need for secrecy in development that is often counter-productive, as participating organizations must cooperate directly with each other and with industry groups.

WIS differ from the older forms of IOS in some ways. In the past, IOS often ran on value-added networks that were expensive to set-up and thus tended to be used more by larger companies. The value-added networks, however, provided capacity and security. With the use of the Internet as the carrier for IOS, barriers to entry such as cost and lack of expertise are reduced and many smaller organizations are able to participate.

The increasing participation of larger numbers of smaller firms could lead to even greater relevance of some of the characteristics of the older IOS – that is, the need for even more attention to issues that arise when many different parties with differing objectives need to cooperate. Security is of greater concern with use of the Internet as a carrier rather than value-added networks. This situation may lead to the development of an extranet - a network that links business partners to one another over the Internet by tying together their corporate intranets. The extranet uses the same basic infrastructure components, including servers, TCP/IP protocols, e-mail, and Web browsers as the Internet, but makes communication over the Internet secured. An extranet, like an intranet, is typically protected by a firewall and is closed to the public. It is open to selected suppliers, customers, and other business partners, who access it on a private wide-area network over the internet or on a virtual private network (VPN), which increases security and functionality (Turban et al., 1999).

There are not many case studies of development methods that are used for IOS. There appears to be some consensus about IOS being more _multi-faceted_ (Lyytinen, 1989), and _multi-functional_ than information systems (Konsynski, 1992; Hopper, 1990; Meier & Sprague, 1991). IOS are recognized as information systems where the many parties involved magnify traditional problems of politics, management expectations, and to some extent technical concerns, involved.

For example, Ramanath et al (1998), report a case study of an IOS development project in a multinational business organization. Requirements specification was an issue. Specifying and agreeing what was needed from the number of parties involved in this IOS in 4 to 5 weeks proved very difficult. This difficulty was explained partly by reduced trust inherent in IOS rising from the concerns of information security and the ownership and control of data.

Cameron (1996) reviews the use of EDI over a 20-year period and questions why, if EDI was so promising, it took so long for it to be adopted as a standard tool in international trade and transport. She concluded that even when the main macro-level inhibitors and constraints are removed, it is the micro level economic and market concerns of individual organizations throughout the trading chain that determine successful adoption of EDI. Government policy and assistance were less important at the micro-level than economic and business factors like cost/benefit and market forces. In addition, the management of collaborative projects is not well understood and the process requires collaboration, shared decision-making and joint activities like negotiation of contracts and changing business processes throughout the chain. Most private sector enterprises are competitors and are motivated by economic factors. Successful implementation of EDI and electronic commerce demands co-ordination of “volunteers” and all must achieve a win-win situation. To overcome these difficulties, there is a need for formal facilitation and experienced facilitators, funding, resourcing and commitment.

Vermeer and Veth (1998) consider the problems of interorganizational data integration and the development of a common data model across many interdependent network participants. After a study of over 10 different central database initiatives they found that almost all of them suffered from lack of support. They concluded there were two important reasons for the lack of success; first, political reasons such as _hidden agendas_ and _disruption of the balance of power_ and second, the _large number of data fields_ resulting in large data administration costs and lack of flexibility at a local level. Competitors had hidden agendas because they were not happy about sharing information. A large Dutch retailer, refused to participate in a central Dutch product database that registered merely no more than the EAN article number. The retailer feared that their largest competitor would be able to search the database for all of their home brand articles. Although this information could also be retrieved through walking into one of their retail outlets, this possibility was enough for them not to participate.

De and Ferratt (1998) report on the development of an innovative information system to share health care information among competing hospitals. They stressed the need to solicit views of all players during both system design and maintenance and to involve users in development (or at least to give them hands-on experience with prototypes). Leadership, organizational commitment, and coordination were not perceived to be major concerns in the project, though this may have been due to the establishment of a project taskforce with a clear authority structure. The authors consider that, in any system involving multiple organizations or different interest groups, particularly where conflicts are likely, issues of leadership and organizational commitment are critical and should be planned and dealt with carefully.

Overall, in terms of interorganizational WIS, there are many issues that arise when different parties with differing objectives need to cooperate. These issues include organizational issues, system development issues, and information issues. Organizational issues include such non-technical aspects as political considerations and management challenges, as well as issues of leadership and commitment to the project. System development issues include such things as adequate funding and ongoing resourcing and maintenance of WIS projects, the importance of user involvement, and the need for formal facilitation of the process. Finally, data issues of security and problems with integration must be addressed when developing interorganizational WIS. The next section of this paper looks at information system development methodologies (ISD) in general.

## WIS -- Relevant development methodologies

This section looks at ISD with a view to understanding problems that have occurred in the past so that we may avoid them in the future. As this paper does not aim to cover the whole area of system development methodologies, which is a very large topic with the discipline of information systems, the authors recommend works such as Hirschheim, Klein and Lyytinen (1995), Avison and Fitzgerald (1997), Pressman (1997) for additional background on the topic.

In spite of continued heavy resource expenditures by organizations to develop information systems, a high percentage of these information systems still fail. Organizations cannot afford to tolerate the high failure rates of systems especially in view of the fact that modern organizations demand more sophisticated information and technological advancements in order to stay competitive. Partly in response to this high rate of failure ISD research has become a major research area within the discipline of Information Systems. More user-oriented and participatory approaches have recently gained much attention in the ISD literature with their focus on organizational versus technical aspects and their potential to increase the likelihood of systems success. These aspects, which so heavily influence information systems outcomes, are difficult to define and measure and include intangible concepts such as power, politics and personalities. However, it has become clear that ignoring the organizational and people issues greatly adds to the risk of failure of any project (Davenport, 1994; DeLone & McLean, 1992; Guinan et al, 1998; Lyytinen, 1988; Markus, 1983; Sauer, 1993; Southon et al, 1997; Warne & Hart, 1996).

A recent study in the United Kingdom, reported in Jackson (1995), found that around 40% of information technology systems developments failed or were abandoned. The problem appears to lie, not with the technology, but rather with the lack of attention paid to the needs of people who have to use the technology. The systems fail, the report suggests, because, amongst other reasons, most investments are technology led and users do not usually have any major influence on system development.

Software development methodologies (SDM) have been developed to assist software developers build systems that meet their clients' needs. SDM are generally formalized procedures or protocols to guide development. Clearly, there are problems with these SDM considering so many systems fail. It has been suggested (Russo & Stolterman, 1998) that many developers currently do not even follow SDM when developing software systems. They suggest that there is currently a 'misfit' between existing methodologies and the needs of developers. They believe that this is due to the fact that, in recent years, the types of systems that are developed have changed, from more technical systems, that were developed for a few specially trained users, to more user-focused systems, that are developed for users who may have limited computer skills. Additional evidence showing that formal methodologies are not always is provided by Fitzgerald (1998), who found that 60 percent of respondents were not using a development methodology, with only 6 percent reporting that they followed a methodology rigorously.

Standing & Bavington's 1995 study of a structured approach to ISD suggests that although ISD has been generally regarded as a technical process, it appears upon critical investigation to be mostly a non-technical process. The results of their study also suggest that to be successful, a methodology depends upon social and political factors as much as technical factors. This finding supports the growing body of research in this area.

There are currently several approaches that aim to better capture the needs of the users and the role that the software will play in the structure of the organization as a whole. Avison and Fitzgerald (1995) and Hirschheim, Klein & Lyytinen (1995) discuss aspects of these newer approaches. Approaches that appear useful to assist development of software for organizations include: Mumford's Effective Technical and Human Implementation of Computer-based Systems (ETHICS) (Mumford, 1996), Checkland's Soft Systems Methodology (SSM) (Checkland, 1981; Checkland and Scholes, 1990), and finally, the Multiview approach (Avison & Fitzgerald, 1997) which is influenced by aspects of SSM, ETHICS and more traditional development methodologies.

The participatory approach is linked to Checkland’s SSM “as it acknowledges cultural, political and social perspectives and, through innovative and meaningful and structured and collaborative debate between accommodating stakeholders, seeks to create an environment where appropriate action can be taken” (Jackson & Sulaksono, 1998 p. 41). Furthermore, SSM acknowledges that problems are often not well defined and builds this fuzziness about the problem into the methodology. A hard systems approach, on the other hand, focuses more on the certain and the precise and looks at the problem from one viewpoint (Avison & Fitzgerald, 1997). One possible way to improve the adoption of information systems is to develop information systems using information systems methodologies that focuses on the needs of the user - that is, a more participatory approach to software development such as SSM.

From the preceding sections it appears that interorganizational WIS need even more emphasis on non-technical aspects and a methodology that reflects this. This view is congruent with that of Ramanath et al. (1998) in comparing the development of IOS with other IS. They argue that the technical or “hard product” approach of more traditional SDM is inadequate for the development of more recent ‘softer’ systems such as IOS.

Although few case studies have been done to research the problems associated with developing WIS, the following studies illustrate the points we have identified in the literature. Balasubramanian & Bashian’s (1998) case study of the development of a large scale WIS for a major financial management institution described their use of a systematic design methodology. The study compared the often-chaotic process of the development of the WIS to the nonsensical tea party in Lewis Carroll’s “Alice in Wonderland”. This comparison proved to underscore the importance of trying to establish a systematic process when undertaking such a complex endeavor. “Although the Web has simplified information delivery, WIS development is equally, if not more, challenging than traditional IS development. IS managers and users generally do not recognize this fact” (p. 113). In addition to the technical complexity, Balasubramanian and Bashian also discovered that political and cultural issues can confound the best laid plans for WIS projects, “Despite all our systematic efforts, our initial perception is the system is now less-than-successful due to non-technical factors” (p. 114).

Also significant is Romm and Wong’s 1998 case study of a WIS. Romm and Wong’s research builds on the initial WIS case study work by Jarvenpaa & Ives, 1996. Once again, Romm and Wong declare “The introduction of a Web technologies project to an organization is a far more complex process than is commonly assumed” (p. 67).

Romm and Wong achieved dissimilar results from Jarvenpaa and Ives in studying WIS projects. They attributed the differences to the political, organizational and culture variables involved. Although the few case studies have confirmed the political, organizational and technical complexity of WIS, it is clearly area for future investigation.

## Human-Computer Interaction

A number of characteristics of WIS suggest that particular attention should be paid to human-computer interaction (HCI) issues in the design of WIS. These characteristics include the distributed nature of WIS, leading to a high likelihood that users of a WIS will have a wide range of backgrounds – in terms of education, prior computer experience, culture, and availability of training and support. In addition, WIS are likely to be highly interactive and in fact interactivity is viewed as one of the desirable features of WIS used for marketing (Sterne, 1995). An additional characteristic of WIS that is relevant is that the ubiquitousness of popular Web browsers provides a uniform style that users appear to learn fairly quickly and easily, and provides a base for other WIS. Furthermore, in many cases the users of WIS will not be a “captive” audience. For example, with direct marketing via the Web, the user chooses whether or not to use the WIS. If it is hard to use or unappealing they may choose to go elsewhere.

The discipline of HCI provides many guidelines for the design of interactive computer systems – guidelines that have developed from theory and practice over a number of years. Comprehensive coverage of the area can be found in Dix et al. (1993), Preece et al. (1994), and Shneiderman (1992). Guidelines that apply particularly to human-computer interaction in the World Wide Web context can be found in Neilsen (1995, 1999) and Sterne (1995). Sterne points out that in the Web environment particular attention should be paid to issues associated with navigation, use of large graphics, response time, and design of search tools. In addition, Sterne points to underlying principles of marketing that should be taken into account, such as the need to add value and to keep attention focused on your own site. In a recent article, Nielsen (1999) warns of the dangers of neglecting the lessons learned from the many years of study of the design of interactive systems and the chaos that will possibly result in use of the Internet if these lessons are ignored.

From the above it appears that design methods that have proved useful in the area of human-computer interaction may prove particularly useful in the design of WIS – systems that are inherently interactive in nature and where ease-of-use features are particularly important. One approach that appears worthy of further investigation in the WIS context is termed _user-centered design_ (Preece at al., 1994). User-centered design focuses on usability, and means that (i) there is a focus on users and their tasks early in the design process, (ii) reactions of users are measured by using prototypes of manuals, interfaces and other simulations of the system, (iii) design is iterative (that is, previous steps are redone), and (iv) all usability factors are considered together, with one control group responsible for them. Note that this approach appears similar to some of the approaches used in the development of WIS that are referred to loosely as “experimental” or “prototyping” approaches (Turban et al., 1999) without reference to any formal methodology.

## WIS -- Hypermedia and implementation issues

Applications using hypermedia features allow the user to add, access and navigate links in textual and multimedia information. Such applications can be easier and more effective to use than traditional applications (Bieber & Vitali, 1997). The World-Wide Web is currently the most successful hypermedia system in part due to the simplicity of its standards, protocols and hypertext model (Berners-Lee et al, 1994; Ladd et al, 1997). However, it is by no means the first hypermedia system. Research and development of hypermedia environments has been carried out since at least the 1960s (Engelbart & English, 1968). In that time, the hypermedia research community has developed a body of research about the features, systems, guidelines, frameworks and theories about structuring, presenting and accessing interrelated information (Bieber et al, 1997).

In this section we examine the aspects of this area of research that have been forgotten in the implementation of WIS. We start by examining the features of hypermedia systems that are missing from the Web and how their addition can improve the Web. We then discuss how these features when combined with other practices from the hypermedia community can improve the authoring and design of WIS.

### The Web's Deficiencies and Useful Hypermedia Features

The Web's simple design, while leading to a successful and useful system, has a number of deficiencies which have contributed to many of the problems, such as the "missing link" and "lost in space" problems, now being experienced on the Web. The simplicity of the Web's design has also contributed to the absence of a number of standard hypermedia features, such as guided tours and structured searching. In the following we discuss these deficiencies and missing features.

A major deficiency of the Web is its link model. While its implementation of links provide advantages including, ease of implementation, scalability in a networked environment and the ability to edit links in place (Andrews, 1996), it also has a number of limiting characteristics including:

- Links are uni-directional.  
    The forward only nature of Web links makes it difficult to construct local maps to aid navigation and also contributes to the "missing link" syndrome that plagues the Web. Making links bi-directional by storing both source and destination end points, helps address these problems.

- Addressing is by location rather than identity.  
    The Web's addressing mechanism, universal resource locaters (URLs), specify the physical location of page rather than its identity. An identity based addressing scheme would enable pages to be moved at will, without suffering the "dangling link" problem, and also enable the automatic mirroring of high demand pages to address network bottlenecks (Andrews 1996).
- There are no attributes.  
    Links on the Web are not associated with any semantic information such as creator, owner or type. Such semantic information lends additional context for readers and helps authors to organise information more effectively (Bieber et al, 1997). It also aids in the development of services such as automatic link management, creation of local maps, use of templates, computed and personalised links and structure-based queries (Bieber et al., 1997).
- Links are embedded in documents.  
    Since web links are embedded into web documents you can only add links if you have write permission for that document. This makes it impossible to link from legacy or non-hypermedia applications, documents on CD-ROM or those owned by other people (Andrews, 1996; Bieber et al, 1997). The absence of this ability makes it difficult to implement personal annotations which are thought to be a basic right for hypermedia readers and a basic tool for collaboration and exchange of ideas (Bieber et al, 1997). Enabling annotations and allowing Web information systems to be used for communication and cooperation will help increase the systems success (Andrews 1996). Maintaining external link bases enables such services as link and view customization, guided tours, trails, bi-directional links, link typing, individual access permissions and guaranteed consistency (Bieber et al, 1997).

Possibly the largest current problem with the Web is difficulty in effectively handling the enormous amount of information on the Web (Marchiori, 1998). The presence of metadata, that is, information about the documents on the World-Wide Web, addresses this problem by aiding in the provision of search and visualisation features. Consequently there are numerous proposals to incorporate suitable metadata sets with HTML (Marchiori, 1998). Even with standard metadata sets there is no guarantee that the majority of the objects on the Web will ever be properly classified via metadata (Marchiori 1998).

### Authoring on the Web

The hypermedia environment provided by the World-Wide Web is primitive and analogous to second-generation computing languages and provides only very low-level functionality (Bieber et al, 1997). The additions of the previously mentioned features in combination with certain practices offer the possibility of improving the current authoring process. This process is usually carried out without a defined process, lacks suitable tool support, does little to separate content, structure and appearance (Coda et al, 1998), makes limited reuse of previous work (Rossi et al, 1997) and requires better group access mechanisms and online editing tools (Andrews, 1996).

Next, we will briefly look at these issues and possible solutions. We start by discussing how the difficulty of current Web authoring leads to the need for expensive, centralized management of Web sites. Next we examine design methodologies which can aid formalizing the design and authoring process. Lastly, we examine the steps that are being taken towards reusing hypermedia design and authoring outputs.

### Distributed versus centralized authoring

The difficulty of authoring on the Web leads to a number of problems with the creation and maintenance of web sites. It leads to the management of content for a web site being assigned to one person who becomes the bottleneck for maintenance (Thimbleby, 1997). This is especially important when maintenance is an essential component of Web site development. Nielsen (1997) suggests as a rule of thumb that the annual maintenance budget for a website should be at least 50 percent of the initial cost of building the site (preferably the same). Additionally, most of the Web is read-only with a strict distinction between authors and readers. Better support for authoring will enable communication and collaborative work which will aid system success (Andrews, 1996).

One approach to addressing these problems is the concept of hypermedia templates (Catlin et al, 1991). Hypermedia templates aid the creation of hypermedia collections by simplifying the authoring task and aid authors in applying information design principles. This enables content experts to be responsible for placing information onto the Web which can aid in avoiding the bottleneck problem. The creation of templates is performed by designers familiar with good information design principles and practice.

### Design methodologies

Hypermedia authoring consists of at least two major tasks:

- Authoring-in-the-small.  
    The development of the contents of the nodes which is strongly dependent on the tools and medium being used.

- Authoring-in-the-large.  
    The specification and design of global and structural aspects of the hypermedia application which is to some extent independent from the tools and medium being used. (Garzotto et al, 1993)

The absence of systematic design models for developing Web applications, particularly for authoring-in-the-large, has caused information management problems in the Internet and intranet environments of large corporations (Balasubramanian et al, 1997). The available hypermedia design models include HDM (Garzotto et al, 1993), RMM (Isakowitz et al, 1995), and OOHDM (Schwabe et al, 1996). The formal modeling of entities and relationships, which are an essential component of these approaches, can make it difficult to apply them in unstructured domains. The ”data driven” approach of these models means that they do not always address usability problems which are being addressed in methodologies such as WSDM (De Troyer & Leune, 1998).

The advantages of using these methodologies include:

- A method for concisely describing hypermedia applications.  
    This aids communication between the actors in the development of a Web site including designer, implementor and user. It also aids in discussions where Web sites and development methodologies are compared and contrasted.
- Construction of design tools.  
    A design model can be used as the basis of design tools that automatically generate a hypermedia application based on a formal design.
- Aiding the author in conceptualising a given application.  
    Design models and design tools help remove the author from implementation details and allow full concentration on the analysis of the application domain.
- Increasing reuse  
    Formal design models enable the partial reuse of the structure of hypermedia applications (Garzotto et al, 1993).

### Reuse

Reuse is a strategic tool for reducing the cost and improving the quality of hypermedia design and development (Nanard et al, 1998). While some interest has been shown in reuse in hypermedia field most hypermedia systems are built from scratch (Rossi et al, 1997). Even though existing design approaches enable the first steps towards reuse (Garzotto et al, 1993) they are not effective in helping designers reuse existing hypermedia structures (Rossi et al, 1997).

The hypermedia literature has identified three types of reuse:

1. Information reuse (Garzotto et al, 1996).  
    The reuse of a hypermedia data in different parts of the same application.
2. Software component reuse (Gronbaek & Trigg, 1996).  
    The reuse of a piece of code in different contexts or systems (Garzotto et al, 1996).

4. Design reuse (Rossi et al, 1997) (Nanard et al, 1998).  
    The reuse of a hypermedia designer's know-how and experience.

Design reuse, in particular, is difficult due to the lack of support for reuse in many existing design approaches. Design patterns, which are a recent trend in software engineering (Gamma et al, 1994), are adapted from urban planning and building architecture (Alexander, 1977). Design patterns offer an approach to documenting and supporting the reuse of design which is finding favor in hypermedia (Rossi et al, 1997; Nanard et al, 1998).

The technical environment in which WIS must be implemented, the World Wide Web, is a primitive hypermedia system where the authoring process is made more difficult by a lack of functionality. The addition of features identified by the hypermedia research community enable additional functionality for both authors and readers, increased usability and decreased cost in the maintenance of WIS. The design and development of WIS can be further aided by the use of hypermedia design methodologies, especially those that focus on resuse of information, software and design.

## Conclusions

Based on the review of mistakes and progress in the various areas of IS research covered in this paper that can be applied to WIS, it is clear that it would be unwise not to heed lessons from the past that appear relevant to WIS development and implementation. It is important to remember that many WIS are actually IOS. Therefore, developers need to be aware of the extra complexity involved in such systems and be sensitive to the non-technical issues revolving around politics and the control of information. Furthermore, when designing WIS, it is important to consider methodologies that include the social and political aspects. In addition, it is suggested that particular attention should be paid to development methods that focus on human-computer interaction issues and usability, and build on the work done in developing hypermedia systems. As there are few published case studies of WIS development as yet, we suggest further research in this area.

## References

Alexander, C., Ishikawa, S., and Silverstein, M. (1977). _A Pattern Language: Towns, Buildings, Construction_, Oxford University Press.

Andrews, K. (1996). Applying hypermedia research to the World Wide Web, _Workshop on Hypermedia Research and the World Wide Web_, Hypertext'96 Conference, Washington, \[http://www.iccm.edu/apphrweb\].

Avison, D., and Fitzgerald, G. (1997). _Information Systems Development: Methodologies, Techniques and Tools_ (2nd ed.). McGraw-Hill, London.

Avison, D.E., & Wood-Harper, A.T. (1990). _Multiview: An Exploration in Information Systems Development_. Oxford: Blackwell Scientific.

Balasubramanian, V., Bashian, A. and Porcher, D. (1997). A large-scale hypermedia application using document management and Web technologies, _Proceedings of the 8th ACM conference on Hypertext_, 134-145.

Balasubramanian, V., Bashian, A. (1998). Document Management and Web Technologies: Alice Marries the Mad Hatter. _Communications of the ACM_, 41(7), 107-115.

Berners-Lee, T., Cailliau, R., Luotonen, A., Nielsen, H. and Secret, A. (1994). The World-Wide Web, _Communications of the ACM_, 37(8), 76-82.

Bieber, M., Vitali, F., Ashman, H., Balasubramanian, V. and Oinas-Kukkonen, H. (1997). Fourth generation hypermedia: some missing links for the World Wide Web, International _Journal of Human-Computer Studies_, 47, 31-65.

Bieber, M. and Vitali, F. (1997). Towards Support for Hypermedia on the World-Wide Web, _IEEE Computer_, 30(1), 62-70.

Cameron, J. (1996). EDI in Australian International Trade and Transport. In N. Terashima & E. Altman (Eds.), _Advanced IT Tools_ (pp. 235-248). London: Chapman & Hall.

Catlin, K.S. and Garret, L.N. (1991). Hypermedia Templates: An Authors Tool, _Proceedings of Hypertext'91_, ACM, 147-160.

Checkland, P. (1981). _Systems Thinking, Systems Practice_. Chicester: John Wiley & Sons.

Checkland, P., & Scholes, J. (1990). _Soft Systems Methodology in Action_. Chichester: John Wiley & Sons.

Coda, F., Ghezzi, C., Vigna, G. and Garzotto, F. (1998). Towards a Software Engineering Approach to Web Site Development, _Proceedings of the 9th International Workshop on Software Specification & Design_, Isobe, Japan.

Davenport, T. H. (1994). Saving IT's Soul: Human Centered Information Management. _Harvard Business Review, March-April_, 119-131.

De, P. and Ferratt, T. W. (1998). An information system involving competing organizations, _Communications of the ACM,_ 41(12), Dec., 90-98.

DeLone, W. H., & McLean, E. R. (1992). Information Systems Success: The Quest for the Dependent Variable. _Information Systems Research, 3_(1), 60-95.

De Troyer, O. and Leune, K. (1998), WSDM: a user Centered design method for Web sites, _Proceedings of WWW'7_, Computer Networks and ISDN Systems, 30, 85-94

Dix, A, Finlay, J., Abowd, G., and Beale, R. (1993). _Human-computer interaction,_ Prentice Hall, New York.

Engelbart, D. C. and English, W. (1968). A research center for augmenting human intellect, _AFIPS Conference Proceedings_, Fall Joint Computer Conference, Vol. 33, 395-410.

Fitzgerald, B. (1998). An empirical investigation into the adoption of systems development methodologies. _Information Management_, _34_(6), 317-328.

Gamma, E., Help, R., Johnson, R., and Vlissides J. (1994). _Design Patterns: Elements of Reusable Object-Oriented Software_, Addison-Wesley.

Garzotto, F., Paolini, P. and Schwabe, D. (1993). HDM - a model-based approach to hypertext application design, _ACM Transactions on Information Systems_, 11(1), Jan. 1993, 1-26.

Garzotto, F., Mainetti, L. and Paolini, P. (1996). Information reuse in hypermedia applications. _Proceedings of the 7th ACM Conference on HyperText_, ACM, 38-47.

Gronbaek, K., and Trigg, R. (1996). Towards a Dexter-based model for open hypermedia: Unifying embedded references and link objects, _Proceedings of Hypertext'96_, ACM Press, 116-128.

Guinan, P. J., Cooprider, J. G., & Faraf, S. (1998). Enabling Software Development Team Performance During Requirements Definition: A Behavioral Versus Technical Approach. Information Systems Research, 9(2), 101-125.

Hirschheim, R., Klein, H.K., & Lyytinen, K. (1995). _Information Systems Development and Data Modeling - Conceptual and Philosophical Foundations_. Cambridge: Press Syndicate.

Hopper, M. (1990). Rattling SABRE – New ways to compete on information. _Harvard Business Review,_ 68, May-June, 118-125.

Isakowitz, T., Stohr, E., and Balasubramanian, P. (1995). RMM: A Methodology for Structuring Hypermedia Design, _Communications of the ACM_, 38(8), 34-44.

Jackson, B., & Sulaksono, S. (1998). Going soft on information systems evaluation. AJIS, 5(2), 41-50.

Jackson, M.C. (1997). Critical systems thinking and information systems development. Paper presented at the 8th Australasian Conference on Information Systems, Adelaide, South Australia.

Jarvenpaa, S. L., Ives, B. (1996). Introducing Transformational Information Technologies: The Case of the World Wide Web Technology. _International Journal of Electronic Commerce_, 1(1), 95-106.

Konsynski, B. (1992). Issues in design of interorganizational systems. In Cotterman, W. and Senn, J. (Eds.). _Challenges and strategies for research in systems development,_ John Wiley & Sons, Chichester, 43-63.

Ladd, B.C., Capps, M.V. and Stotts, P.D. (1997). The World Wide Web: what cost simplicity? _Proceedings of Hypertext'97_, ACM Press, 210-211.

Lyytinen, K. (1988). Stakeholders, Information Systems Failures and Soft Systems Methodology: An Assessment. _Journal of Applied Systems Analysis, 15_, 61-81.

Lyytinen, K. (1989). New challenges of systems development: A vision of the 90s, _Database,_ Fall-Winter, 1-12.

Marchiori, M. (1998). The limits of Web metadata, and beyond, _Proceedings of WWW'7_, Computer Networks and ISDN Systems, 30, 1-9

Markus, M.L. (1983). Power, politics, and MIS implementation. _Communications of the ACM_, _26_(6), 430-444.

Meier, J. and Sprague, R. (1991). The evolution of interorganizational systems_, Journal of Information Technology,_ 6(3/4) 184-191.

Mumford, E. (1996). _Systems Design - Ethical Tools for Ethical Change_. Houndmills: MacMillan Press.

Nanard, M., Nanard, J. and Kahn, P. (1998). Pushing reuse in hypermedia design: golden rules, design patterns and constructive templates, _Proceedings of the 9th ACM Conference on Hypertext and Hypermedia_, ACM Press, 11-20.

Neilsen, J. (1995). _Multimedia and hypertext the Internet and beyond,_ AP Professional: Boston.

Nielsen, J. (1997), _Top Ten Mistakes of Web Management_, http://www.useit.com/alertbox/9706b.html.

Nielsen, J. (1999), User Interface Directions for the Web, _Communications of the ACM,_ 42(1), 65-72.

Preece, Y., Rogers, Y., Sharp, H., Benyon, D., Holland, S., and Carey, T. (1994). _Human-computer interaction,_ Addison-Wesley, Wokingham.

Pressman, R. (1997). _Software Engineering A Practitioner’s Approach,_ (4th ed.), McGraw-Hill, New York.

Ramanath, A. M., Paul, R. J., and MaCredie, R. (1998). Understanding Interorganizational Systems Development. Paper presented at the 6th European Conference on Information Systems, Aix-en Provence, France.

Romm, C. T., Wong, J. (1998). The Dynamics of Establishing Organizational Web Sites: Some Puzzling Findings. _AJIS,_ 5(2), 60-68.

Rossi, G., Schwabe, D. and Garrido, A. (1997). Design reuse in hypermedia applications development, _Proceedings of the 8th ACM conference on Hypertext_, ACM Press, 57-66.

Russo, N. L., & Stolterman, E. (1998). Uncovering the assumptions behind information systems methodologies: implications for research and practice. Paper presented at the 6th European Conference on Information Systems, Aix-en Provence, France.

Sauer, C. (1993). Why Information Systems Fail: A Case Study Approach. Henley-on-Thames: Alfred Waller.

Schwabe, D., Rossi, G. and Barbosa, S.D.J. (1996). Systematic Hypermedia Application Design with 00HDM. _Proceedings of Hypertext '96_, ACM Press, 116-128.

Shneiderman, B. (1992). _Designing the user interface: Strategies for effective human-computer interaction,_ 2nd ed., Addison-Wesley, reading, MA.

Southon, G., Sauer, C., & Dampney, C. N. G. (1997b). Information Technologies in Complex Health Services: Organizational Impediments to Successful Technology Transfer and Diffusion. _Journal of the American Medical Informatics Association, 4_, 112-124.

Sprague, R. H. and McNurlin, B. C. (1993). _Information Systems Management Practice (3rd ed.)._ Englewood Cliffs: New Jersey.

Standing, C., & Bavington, A. (1995). A systems perspective using a structured information systems development methodology. Paper presented at the Australian Systems Conference, Perth, Australia.

Sterne, J. (1995). _World Wide Web Marketing: Integrating the Internet into your Marketing Strategy,_ Wiley: New York.

Thimbleby, H. (1997). Distributed Web Authoring, _Proceedings of WebNet'97_, Association for the Advancement of Computing in Education, 1056-1083.

Turban, E., McLean, E. and Wetherbe, J. (1999). _Information Technology for Management,_ (2nd ed.), John Wiley & Sons, New York.

Vermeer, B. H. P. J., and Veth, T. F. L. (1998). Interorganizational Data Integration: Theory and Practice. Paper presented at the 11th International Bled Electronic Commerce Conference. Bled, Slovenia.

Warne, L., & Hart, D. (1996). The Impact of Organizational Politics on Information Systems Project Failure - A Case Study. Paper presented at the Proceedings of the 29th Annual Hawaii International Conference on Systems Sciences- 1996, Hawaii.