---
title: "Webfuse: An integrated, eclectic Web authoring tool"
date: 2009-01-01 13:36:38+10:00
type: page
template: blog-post.html
---

See also: [[blog-home | Home]]

David Jones, Webfuse: An integrated, eclectic Web authoring tool, Proceedings of EdMedia’99, Betty Collis, Ron Oliver (editors), June, 1999, pp 1799-1801

## Introduction

Webfuse (McCormack and Jones, 1997 p362) is an authoring tool for the World-Wide Web designed and constructed at Central Queensland University to aid in the development of Web-based learning (Jones and Buchanan, 1996). Webfuse has been used in the construction and maintenance of numerous websites for online learning (Jones, 1998) and commercial purposes (http://www.broncos.com.au/). It is currently the primary web authoring platform for the Faculty of Informatics and Communication of Central Queensland University and is used by almost 100 staff to maintain a Web site with over 150 units and over 100,000 separate web pages.

A University developing a system for the support of online learning is not new with systems such as WebCT (http://www.webct.com/webct) having similar origins. In fact, a number of Webfuse's characteristics are similar to these other systems. While this paper briefly describes these familiar characteristics it concentrates on the features of Webfuse which differ from similar tools. In particular it will examine how Webfuse draws on the lessons gathered from the fields of hypermedia and operating systems to arrive at a structure which attempts to ease the authoring bottleneck while providing the extensibility and adaptability required to keep up with the Web.

## The Familiar Characteristics of Webfuse

Some of the familiar characteristics of Webfuse include

- server-based,  
    The only software requirement to author a Web site with Webfuse is a Web browser. The browser provides the interface between the user and the collection of CGI scripts and other software residing on a Web server that provide all of Webfuse's functionality.
- server and client platform independence,  
    Webfuse authors are able to use any computer platform since Web browsers are available on almost all computer platforms. Additionally the Webfuse server software currently runs on both Windows and UNIX platforms and adapting it to the Mac platform is possible.
- standard functionality.  
    Webfuse provides functionality common to most other systems including information distribution, asynchronous and synchronous communication, assignment submission and management, online quizzes, authentication and access control.

## Why Webfuse is Different:

The major differences between Webfuse and other systems are the use of hypermedia templates and an eclectic and integrated structure. The following section describes the importance of these differences.

### Hypermedia Templates

Web authoring is usually carried out without a defined process, lacks suitable tool support, does little to separate content, structure and appearance (Coda et al, 1998), makes limited reuse of previous work (Rossi et al, 1997) and requires better group access mechanisms and online editing tools (Andrews, 1996). The difficulty of authoring on the Web often leads to the management of content for a web site being assigned to one person who becomes the bottleneck for maintenance (Thimbleby, 1997). This can be a major problem in online learning where simple, rapid and cheap maintenance of a site is essential for its on-going usefulness.

Hypermedia templates (Catlin and Garret, 1991) are an approach to simplifying the authoring process while still ensuring the application of good information design principles. Hypermedia templates enable content experts to be responsible for maintaining Websites and thus increases ownership, decreases costs and addresses the authoring bottleneck problem. Hypermedia templates also aid in reuse which is a strategic tool for reducing the cost and improving the quality of hypermedia design and development (Nanard, Nanard and Kahn, 1998).

### An eclectic and integrated structure

It was recognised from the start of the Webfuse project that it would not be possible for a small collection of part-time individuals to build and maintain a Web authoring tool. Not only would the amount of work required to initially construct a useful system be onerous but a much larger task would be to continue upgrading the system in response to changing requirements and changes in the Web.

To address this problem Webfuse draws on the micro-kernel architecture approach used in many modern operating systems. The advantages of the micro-kernel approach include a more modular system structure and a system which is more flexible and tailorable (Liedtke, 1995).

The Webfuse "kernel" is a collection of abstractions and services including authentication, access control, HTML validation, presentation and data storage. These abstractions and services are drawn upon by a collection of hypermedia templates and other higher level services which are used by authors to develop web sites.

At any time a new hypermedia template can be written to provide Webfuse with added functionality. New templates generally wrap around new software or technology (e.g. a Java based chat room, a Web-based mailing list manager etc) as it becomes available. It is significantly easier to create a new hypermedia template than to create the software from scratch.

Usually the use of a large collection of software created by different people would increase the authoring complexity due to the large amount of variety and duplication in user interfaces. Webfuse addresses this problem via the Webfuse "kernel" which provides a single common administrative interface used by all hypermedia templates. The "kernel" integrates the eclectic templates behind a common interface.

All of the existing Webfuse hypermedia templates are written around either existing open source software (e.g. MHonarc, Ewgie, WebBBS) or applications written specifically for use at CQU (e.g. an assignment submission tied to CQU's student database system). The hypermedia template approach allows the quick integration of most Web-based software into a common management framework. The eclectic and integrated approach has been particularly useful in allowing Webfuse to draw on the large collection of open source software for the Web. This ability to use almost any open source software has further increased the ability of Webfuse to adapt to changes and provide additional functionality.

## Using Webfuse

A new Webfuse web site starts with an author being given a user account and a URL. The URL is usually a single empty Web page which the new author can visit. The only content on such a page is usually a title and a small "edit" link. The author can modify the page by clicking on the "edit" link at which time they are asked for a valid username/password. Once such details are checked the author is presented with a CGI form. This form provides the common management interface including sections which are specific to the particular hypermedia template associated with the current page.

Once the author enters the appropriate data via the CGI form the hypermedia template converts that information into a Web page. Some hypermedia templates and other services allow the author to create new Web pages which are structured by Webfuse into a hierarchical structure to aid navigation and maintenance.

Another feature of Webfuse is that it separates the content of a page, specified via hypermedia templates, from the presentation, specified via style sheets and colour schemes. Having the content and presentation separated allows an author to modify the look and feel of a page independently of the page's content. The logical extension of this approach is to allow the visitor to the Web site to choose the presentation which best suits them.

## Experience

Initial development on Webfuse commenced in the latter half of 1996 (Jones and Buchanan, 1996). Since then Webfuse has been used in the construction and maintenance of a number of Websites, both educational and commercial. This experience has shown that Webfuse provides sufficient functionality for Web authoring. The adaptability of Webfuse has also been shown by its ability to adapt to the changes in the Web since 1996. Amongst the changes in the Web since 1996 has been the introduction of new technology such as cascading style sheets, metadata and XML all of which are being incorporated into Webfuse.

Examples of Websites constructed with Webfuse include

- http://www.infocom.cqu.edu.au/  
    The Website for the Faculty of Informatics and Communication at Central Queensland University.

- http://www.infocom.cqu.edu.au/85321/  
    The Website for the unit 85321, Systems Administration.
- http://webfuse.cqu.edu.au/  
    The main Webfuse web site which includes copies of Webfuse.

## Conclusions

The creation and management of Websites is a difficult task which can suffer from a bottleneck as authoring responsibility is restricted to a few individuals. Hypermedia templates are an approach which allow content experts to become responsible for creating and managing websites. Webfuse uses hypermedia templates to ease the authoring bottleneck. Hypermedia templates, in conjunction with a collection of support services, also enable Webfuse to have an integrated and eclectic structure which enables it to adapt quickly to changes in requirements and the Web.

## References

Andrews, K. (1996). Applying hypermedia research to the World Wide Web, Workshop on Hypermedia Research and the World Wide Web, Hypertext'96 Conference, Washington, \[http://www.iccm.edu/apphrweb\].

Catlin, K.S. and Garret, L.N. (1991). Hypermedia Templates: An Authors Tool, Proceedings of Hypertext'91, ACM, 147-160.

Coda, F., Ghezzi, C., Vigna, G. and Garzotto, F. (1998). Towards a Software Engineering Approach to Web Site Development, Proceedings of the 9th International Workshop on Software Specification and Design, Isobe, Japan

Jones, D. and Buchanan, R. (1996). The Design of an Integrated Online Learning Environment. Making New Connections. Proceedings of ASCILITE'96. Christie, A., James, P. and Vaughan, B. (eds), pp 331-345

Jones, D. (1999). Solving some problems with University Education: Part II. to appear in the Proceedings of Ausweb'99, Balina, Australia.

Liedtke, J. (1995). On Micro-Kernel Construction. Operating Systems Review. 29(5), pp 237-250.

McCormack, C. and Jones, D. (1997). Building a Web-based Education System. John Wiley & Sons.

Nanard, M., Nanard, J. and Kahn, P. (1998). Pushing reuse in hypermedia design: golden rules, design patterns and constructive templates, Proceedings of the 9th ACM Conference on Hypertext and Hypermedia, ACM Press, 11-20.

Rossi, G., Schwabe, D. and Garrido, A. (1997). Design reuse in hypermedia applications development, Proceedings of the 8th ACM conference on Hypertext, ACM Press, 57-66.

Thimbleby, H. (1997). Distributed Web Authoring, Proceedings of WebNet'97, Association for the Advancement of Computing in Education, 1056-1083.