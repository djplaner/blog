---
title: Webfuse as a web publishing tool - 2000 through 2004
date: 2010-06-22 14:18:39+10:00
categories: ['chapter-5', 'design-theory', 'elearning', 'phd', 'thesis', 'webfuse']
type: post
template: blog-post.html
---
This is the second post containing a part of the evaluation section of chapter 5 of my [PhD thesis](/blog2/research/phd-thesis/). It looks at how much/well Webfuse acted as a web publishing tool during 2000-2004. There's not much here, as this is not the focus.

### A web publishing tool

As described in Chapter 4, the original design of Webfuse included a specific aim that Webfuse be able to act as a general web-publishing tool. This ability of Webfuse was then used from 1997 through 1999 to manage and publish a range of large, often multi-author websites (see Table 4.13). Experience with Webfuse, the shortcomings of this focus on publishing static web documents, and the adoption of an adopter-focused development process (Section 5.3.1) meant that increasingly the focus of Webfuse development was on services and tasks that were specific to the Infocom and CQU context. In particular, there was a focus on the provision of interactive, web-based applications (Sections 5.3.4 and 5.3.6 ) that provided learning and teaching related services specific to Infocom and CQU. While the development of the default course sites approach (Section 5.3.5) built on Webfuse's ability as a web publishing platform, use of Webfuse for website management was reduced during 2000-2004 and there were only small and incomplete attempts to address Webfuse's limitations as a web publishing platform.

During the period 2000 through 2004 Webfuse was only used to manage the personal website of the author and the organisational website for Infocom. This was mostly due to the fact that at this point in time, CQU did not have any institutional system or process for publishing faculty websites. The Infocom website was by far the largest site managed using Webfuse. Table 5.8 breaks the Infocom website into a number of categories. It lists the number of documents accessed during 2004 for each category and the total number of requests for those documents. The definition of document used in Table 5.8 excludes images and CSS files.

Table 5.8 - Infocom web site categories, documents and requests (2004)
| Category | Requests | Documents | Description |
| --- | --- | --- | --- |
| Teaching | 1,062,909 (49%) | 68,659 (60.7%) | Course websites and other pages used in teaching |
| Home | 262,005 (12.1%) | 1 | The website home page |
| Mailing lists | 191,563 (8.8%) | 11,966 (10.6%) | Archives of misc. non-teaching mailing lists |
| Staff | 163,449 (7.5%) | 2218 (2%) | Home pages for faculty staff |
| Student support | 55,090 (2.5%) | 762 (0.7%) | Information to help students studying within the faculty (not directly teaching related) |
| Research | 37,819 (1.7%) | 570 (0.5%) | Faculty research pages |
| Publicity | 37,816 (1.7%) | 338 (0.3%) | Information about studying |
| Tech support | 18,774 (0.9%) | 508 (0.4%) | Support for using all technology in faculty |
| Administration | 6421 (0.3%) | 608 (0.5%) | Intranet, meeting minutes and other administrative uses |
| Community | 1707 (0.1%) | 59 (0.1%) | Various community related projects |

As shown in Table 5.8, teaching was by far the largest category in terms of number of documents (49% of all requests) and requests (almost 61% of all documents). Staff home pages were amongst the most visited per document.

In terms of acting as a general purpose web publishing tool, there were two lessons or limitations identified from the use of Webfuse from 1997 through 1999:

- An inability to use multiple Webfuse page types to contribute different information to a single web page.
- A lack of integration between pages managed by Webfuse and more widespread web publishing or editing tools and practices.

As described above, early and uncompleted work was commenced to address both these problems. This work commenced with the move of the Webfuse page type mechanism to a design patterns-based, object-oriented architecture. An initial phase of this work was completed and was used to create page types for the default course sites. The next planned phase would have enabled the output of multiple Webfuse page types to be mixed and matched within a single Web page, including web pages produced using HTML editors. If complete, this work would have addressed both these limitations.

Another set of incomplete changes to Webfuse was aimed at addressing the second limitation – improving integration with more widespread publishing tools. At this time most Web pages were being produced using GUI\_based HTML editors that did not require users to know HTML. While normal practice did not require knowledge of HTML, taking full advantage of the Webfuse publishing process did. Since Webfuse's page types used a standard HTML form interface, the entry of text was initially limited to the use of a textarea HTML form component. This required users to understand HTML if they wished to move beyond simple text. As described above the use of available Javascript-based applications that turned a textarea HTML form component into a mini-GUI HTML editor was commenced but never entered production.