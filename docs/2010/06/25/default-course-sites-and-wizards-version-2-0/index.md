---
categories:
- chapter-5
- elearning
- phd
- thesis
- webfuse
date: 2010-06-25 11:06:29+10:00
next:
  text: An integrated OLE
  url: /blog2/2010/06/26/an-integrated-ole/
previous:
  text: Webfuse as a web publishing tool - 2000 through 2004
  url: /blog2/2010/06/22/webfuse-as-a-web-publishing-tool-2000-through-2004/
title: Default course sites and wizards - version 2.0
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Default course sites and wizards &laquo; The Weblog of (a) David Jones
      author_email: null
      author_ip: 72.233.13.152
      author_url: https://djon.es/blog/2010/06/07/default-course-sites-and-wizards/
      content: '[...] course sites and&nbsp;wizards  There is now a version 2.0 of this
        [...]'
      date: '2010-06-25 14:28:11'
      date_gmt: '2010-06-25 04:28:11'
      id: '3108'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: The VLE model and the wrong level of abstraction &laquo; The Weblog of (a)
        David Jones
      author_email: null
      author_ip: 74.200.247.239
      author_url: https://djon.es/blog/2010/07/04/the-vle-model-and-the-wrong-level-of-abstraction/
      content: '[...] VLE is almost certainly going to be a component of my ISDT, of my
        model. This is exactly what the default course site approach attempted to do.
        Provide a much higher level of abstraction on top of the [...]'
      date: '2010-07-04 10:24:51'
      date_gmt: '2010-07-04 00:24:51'
      id: '3109'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
This is the second version of an [earlier post](/blog2/2010/06/07/default-course-sites-and-wizards/). As I wrote more of the chapter I felt the need to revisit and expand the idea (though the following is still at a rough draft stage). The following describes the rationale and implementation behind the implementation of the default course sites approach within Webfuse. This approach was used at [CQU](http://www.cqu.edu.au/) from 2001 through 2009. It has similarities with what Mark Smithers [calls a minimium online presence policy (MOPP)](http://www.masmithers.com/2010/05/16/the-problem-with-mopps/), though (I think) my take on the value of MOPP differs a little from Mark's. Not surprising given the following.

As part of writing the [thesis](/blog2/research/phd-thesis/) I am having to abstract out what I felt was good/important/interesting about the Webfuse work. The "default course site" approach, at least in terms of the principles behind it rather than the specific implementation, is probably going to be part of that. I still have to work on this some more, hopefully in coming weeks, but I've put some early [thoughts](/blog2/2010/06/14/academics-course-websites-and-power-laws/) out there.

Hopefully I can work on this argument soon.

### Default course sites and wizards

As described in chapter 4, the initial assumptions built into Webfuse was that a course website would simply be an empty page. From this single, empty page it was assumed that each individual teaching staff member would then draw on the variety of page types (hypermedia templates) provided as course website building blocks by Webfuse to construct their course website. The majority, if not all, Learning Management Systems (LMS), are built upon the same assumption. This assumption matches the purpose of CQU's initial adoption of an official LMS, described by Sturgess and Nouwens (2004) as

> to enable teaching staff to develop and manage online courses with little professional support.

The assumption is that the quality of the LMS application is such that teaching staff can create course websites on their own, with a minimum of support. The early Webfuse experience described in Chapter 4 illustrated that only a very small percentage of academic staff engaged significantly in this task.

The majority of academic staff did not have qualifications in teaching and limited experience in the use of technology to improve learning and teaching. In addition, few had large amounts of time to invest in learning these skills due to other work demands, particularly research. In addition, it became obvious that a significant percentage of the tasks associated with creating a course website were fairly low-level tasks, often involving reuse of information and resources already provided. Some of these tasks (e.g. uploading 12 weeks of lectures or study guide chapters) require repetitive manual work increasing the chance of human error. Lastly, there was little or no integration of institutional practice with Webfuse. For example, CQU has a fixed semester schedule where specific weeks occur on specific dates. Initially, academic staff would have to manually enter these dates into course websites when they used them. Another example would be the institutional production of print-based study guides not providing a good set of PDF files, let alone automatically integrating it into the course website.

These observations led to the Webfuse practice where support staff created initial default course sites by manually editing the initial empty course sites and uploading standard information (e.g. course synopsis, staff contact details etc). However, these course sites were of limited quality, failed to encourage further enhancement from academic staff, and required significant workload from faculty administrative staff. It is within this context that it became necessary to:

- better support the concept of a course; and  
    At this stage, a Webfuse course site was created through the combination of page types that were also useful for general web publishing, the only exceptions being the assignment management and quiz page types. As a result, the page types did not assume or use any knowledge of CQU courses and associated data. For example, the home page for a course site was initially implemented by a general purpose information distribution page. If it was felt good practice to include the course synopsis on the course home page it had to be manually entered by a person.
- encourage greater engagement with course sites from academic staff.  
    As described in Section 5.3.1, the assumptions behind the initial Webfuse course site creation process were more developer focused. It was assumed that provision of a collection of tools would result in a majority of academics learning the new skills and effectively engaging in the additional task of the design and creation of a course site.

During 1999 an initial attempt at addressing these problems was commenced as the "Wizard" project. Briefly described in Jones and Lynch (1999) the Wizard project planned to provide an interface based on the Wizards common to Widows programs of the late 1980s. Such an interface would walk the academic through a series of questions about their course, the provided answers would be combined with the Webfuse page types to create a course site. A particular focus of this plan was an adopter-focused development approach, however, due to organisational uncertainty and limited development resources, this project did not move beyond the prototype and planning stage.

The next attempt to address this problem was the creation of an automated and expanded default course site approach for the second term of 2001. This coincided with the broader roll out of CQU's new student records system. This new default course site approach was made possible by the expanded Infocom web team, the improvements in the Webfuse process and code-base described in previous sections, and was the primary task of the author during the first half of 2001. The automated and expanded default course site approach evolved to consist of a number of components or capabilities that are described in more detail in the following sub-sections. The components or capabilities included:

- An expanded default course site;  
    As described in more detail below, the single empty page default course site was replaced with a much expanded site consisting of five separate sections, containing a range of course related data and services within a re-designed interface. Each offering of every course offered by Infocom would have a new default course site.
- Course specific page types;  
    Once the default course site structure was designed, specific page types were developed to implement the functionality required for each individual page. These page types – described in more detail below – were told which course offering the course site were for and from there drew on existing data sources to provide the necessary services.
- Automatic creation;  
    The creation and population of all default course sites was performed by running a script that, given the details of a specific term and year, would existing information, Webfuse page types, and related scripts and create default course sites for all courses offered by Infocom.
- A copying process;  
    Teaching staff could further modify the default course site by adding additional course information and services. Rather than re-add these additional features for each subsequent term a copying process was developed by which staff could specify what they would like to copy to the new course site.
- Support for a real course site; and  
    There continued to be a number of teaching staff who wished to create their own course website with other tools. Each default course site had support for an optional "real" course site This added another area of the default course site in which the staff member could place their own course site.
- Support for on-going changes.  
    While initially implemented with a single default course site for all Infocom courses, the default course site approach provided a platform for on-going change.

#### Expanded default course site

The starting point was the design of a common default course site that would be used for all courses. The default course site would use the same structure and look, however, the course site page types would insert information and services relevant to the specific course. The initial default site used a simple hierarchical structure represented in Figure 5.1. A course home page formed the top of the hierarchy with five sub-sections and the hierarchical structure could continue under each of these sub-sections.

[![Webfuse default course site structure](images/4731898674_b6dbba983d_m.jpg)](http://www.flickr.com/photos/david_jones/4731898674/ "Webfuse default course site structure by David T Jones, on Flickr")

The five sub-sections were:

1. Updates;  
    The updates section provided a function that allowed teaching staff to provide and store course wide updates or announcements. The titles and post dates of the most recent updates were also visible from the home page.
2. Study schedule;  
    This section provided a week by week breakdown of the course, its topics, content and assessment.
3. Assessment;  
    Provided access to details about the course assessment. By default this would summarise for each assessment item, the title, due date and percentage of the overall assessment.
4. Resources; and  
    All remaining course resources and services were made available via this section. By default this included a link to the course profile (syllabus) document, details of the course textbook(s) (including a link to the university bookshop, and, if used, a discussion forum or mailing list.
5. Staff.  
    This provided both the personal details of the staff teaching the course as well as an area restricted to the teaching staff used for discussion or sharing resources. The personal details of teaching staff included name, contact details and where available a photo.

The initial look and feel for the default course sites is shown in Figure 5.2, which is the home page for one of the course sites from July 2001. The course home page, like each page in the default course site, had three main sections:

1. header;  
    A common header for an entire course site that would show a range of navigation links, branding and administrative information. Navigation links included breadcrumbs to indicate current location and links to other common institutional services such as the student portal, the faculty home page and services such as search, help and feedback. Branding information included common colours and the name of the institution and faculty. Administrative information included the months during which the period ran and the name of the course.
2. body; and  
    The main area of a page and intended to include information specific to the page type. The CourseHome page included a course synopsis and the most recent course updates.
3. footer.  
    A small area for various administrative information such as the Webfuse page update link, details of when and how last updated the page, various disclaimers, and generic contact details.

[![Webfuse default course site home page](images/4677807498_7720a2a08d_m.jpg)](http://www.flickr.com/photos/david_jones/4677807498/ "Webfuse default course site home page by David T Jones, on Flickr")

#### Course page types

For each of the pages identified in the initial design of the default course site and shown in Figure 5.1 a new Webfuse page type was created. These page types were designed to use and provide greater support for the concept of the course and provide services of value to staff and students. When used, each page type would be provided with the course, period and year and draw on existing institutional data sources to provide the necessary content for the body of the page. The following describes the details of what each course page type was designed to produce.

The CourseHome page type was not only responsible for producing the home page for a course as shown in Figure 5.2. It also provided the teaching staff with three additional services. These services were:

1. some control over the course site;  
    When initially created a course site would consist only of the home and updates page. This was necessary as not all course information was initially available due to existing institutional timelines. Once the other required information was ready, the complete course site could be built. This could be done automatically by the Infocom web team or by the teaching staff via the CourseHome page type.
2. access to information about course enrolments; and  
    The staff portal described in section 5.3.6 was not developed until 2002. Prior to this, academic staff could use the CourseHome page type to find out how many students were enrolled in a course and at which campuses.
3. the ability to add students.  
    Students and staff were allocated to a course site based on institutional databases such as the student records system and the Webfuse teaching responsibilities database. Occasionally, these systems – especially the Peoplesoft system during 2001 - were not up to date or staff may wish to provide access to the course site for additional students. The CourseHome page type allowed staff to temporarily enrol students, at least in the Webfuse database.

The RSSUpdates page type provided the ability for the teaching staff to create and maintain a list of course wide updates or announcements. As well as generating HTML representations of the announcements on the Course Updates and Course Home pages, the page type also generated an RSS file that students could access via a newsreader. The student portal also used the RSS file to show students all of the most recent updates in all of their courses.

The CourseSchedule page type provided support for managing a simple study schedule. For each week, the academic could specify the study material, tasks and content the students would be using. Such schedules were a common part of CQU practice and all course profiles (aka course syllabi) contained such a schedule. It was planned for the CourseSchedule page type to use this existing data source to generate the course schedule. However, access to this data was not possible – initially because profiles were produced manually as Word documents and then because Webfuse was not allowed to access the profile system – and consequently course schedules had to be re-created manually.

The CourseAssessment page type would produce a table containing information about all approved assessment items for the course. This information was pulled from a database and included the name, due date and percentage contribution to final grade of each item. Initially, this information was manually transcribed from the course profiles (in Word documents) into a Webfuse database. Eventually, this information was available from a central database. In addition, academics could choose to add a "sub-page" for each assessment item. This item page was used to provide additional details about the assessment item.

The CourseResources page type was designed to provide students with access to all course related resources and services. Some of these resources, such as a link to the course profile and details about any set course texts, were automatically generated. The remaining resources were manually added, deleted and moved by the teaching staff using the page update process.

The CourseStaff page type produced a page that provided a list that included personal details of each teaching staff member associated with the course. This list would include, where available, a photo of the staff member, a link to their home page, and their contact details. The page would also automatically create a "staff only" section underneath the staff page. This "staff only" section was automatically restricted to teaching staff and was used to share information and services restricted to staff.

#### Automatic creation

Prior to the default course sites, Webfuse courses sites within Infocom were created through manual editing of pages by faculty administrative staff. To remove this workload, and prevent it simply being transferred to academic staff, it was envisaged that the default course sites would be automatically created. The implementation for this automatic creation depended on two artefacts: a collection of identified data sources; and the CourseList page type to create the course sites.

The identified data sources were a collection of databases and files that provided all of the necessary information required to construct the default course sites. This include a range of information including: which staff were teaching which course, the name of the course and where it was being offered, the weeks that made up the term, where the course profile PDFs were located, information about individual assignment items, information about selected textbooks, staff websites and photos, and a range of other information. This information was spread across a variety of institutional systems (e.g. Webfuse itself, student records system etc) and some of the information was not in a machine-readable format. A ever-changing range of workarounds were necessary to convert this information into a format that could be accessed by Webfuse. The inability to access some of this information remained the largest limit on the ability to extend the default course sites.

The CourseList page type was used to automatically create the default course sites and produce a collection of web pages pointing to the course sites. Once the necessary data for a new term was available through the identified data sources, creating the default course sites involved creating a new CourseList page, providing the period and year, and submitting the page. This would display a list of the available courses and provide options about how the sites would be created. After the options were chosen, another submission of the page would result in the creation of the matching default course sites.

#### A copying process

After a number of terms of using the default course site, it became evident that many courses were made up of the default course site, plus some additional material and services added by the teaching staff. This additional material often remained the same from term to term with only minor changes. Rather than expect academics to use Webfuse to recreate this additional material, it became more efficient to provide a copy process. A process by which academics could specify which parts of the additional material from an old course site they wished to copy to the new course site, and the actual copying of that material.

#### Support for real course site

The default course site process did create some initial and on-going disquiet around questions of academic independence, consistency and institutional identity. This was particularly a problem for academic staff wanting to create their own course sites, typically using a variety of web or HTML editors or applications commonly used to create websites. This was a particularly common practice amongst academic staff from the multimedia discipline. The ability for an academic to create their own course site was often important in terms of the academics professional identity, but also because of the need for the site design to demonstrate principles associated with the course content.

This raised an interesting and difficult question of how to balance the faculty's needs to ensure a minimum standard of online presence, with the individual academics' disciplinary and identity needs. The solution adopted by Webfuse was to add the notion of a real course site to the default course site. The CourseHome page type was modified to include a check box, which when selected would create a real course site. The real course site was essentially an empty directory under the home page of the default course site. The academic could then upload whatever they wished into this directory as the real course site. The default course site would then provide an additional link to the real course site in its header. Staff using the real course site facility would often supplement this link with additional pointers. Figure 5.3 shows the home pages for both the default course site and the real course site for a single course from 2002.

| [![Default course site home page](images/4731899882_99e4eb42b9_t.jpg)](http://www.flickr.com/photos/david_jones/4731899882/ "Default course site home page by David T Jones, on Flickr") | [![Real course site home page](images/4731255497_d46117b271_t.jpg)](http://www.flickr.com/photos/david_jones/4731255497/ "Real course site home page by David T Jones, on Flickr") |
| --- | --- |

#### Support for on-going change

The default course site approach provides an abstraction that allows significant flexibility in responding to on-going change. Change was enabled by a range of features, including:

- automatic creation and updating of the course sites;  
    The CourseList page type and other support services can be used to both create new and update existing course sites. For example, it was Infocom practice to retain old course sites for past students and administrative purposes. At the end of term, to avoid students confusing old course sites with new course sites, all the pages of old course sites were modified to include a clear warning that this is an old course site.
- the addition of page types and styles; and  
    Default courses sites were produced by combining available Webfuse page types with existing Webfuse styles. The creation of new Webfuse page types or styles could be used to implement new and different default course sites.
- support for different groups of default course sites;  
    It was possible for different groups of courses to use different default course sites.

These features were used by Webfuse to implement changes to the default course sites in response to both top-down and bottom-up changes. In terms of top-down or management driven changes, the specification of the default course site provided a guaranteed minimum level of service to students. It was a standard that could be changed at the direction of management. For example, the inclusion of a course barometer (described in Section 5.3.6) in the initial default course site was an attempt to increase formative feedback from students and subsequently improve the quality of learning and teaching (Jones 2002). Post 2004 the barometer was removed from the faculty default course site, again due to an institutional decision.

Bottom-up changes to the default course sites also arose from the adopter-focused, emergent development process used by Webfuse. Such changes arose first from simple changes in the context. For example, when the CQU bookshop started providing a website with details of set texts for courses, the CourseResources page was modified to include a link to the appropriate page on the bookshop website. Such changes also arose from supporting and observing the use of the default course sites. For example, in 2004 a LectureRepository page was added to make it simple for staff to upload and distribute lecture slides. The LectureRepository example also illustrates the flexibility provided by the addition of new Webfuse page types.

From the initial development of the default course site approach in 2001, through to the the final use of Webfuse for course sites in 2009, there was only ever one standard default course site. The site did change slightly over time in terms of appearance and structure, however, it was used by essentially all default course sites. The two main different default course sites were implemented in 2007 when the author was no longer with the faculty or the web team. The home pages for these two different default course sites are shown in Figure 5.4 and Figure 5.12. The default course site in Figure 5.12 has a different look, but a fairly common structure. The default course site shown in Figure 5.4 was radically different and was refered to as the "Web 2.0" course site.

While the "Web 2.0" course site was implemented as a default site using Webfuse page types, none of the functionality – i.e. discussion, wiki, blog, portfolio and resource sharing - were implemented by Webfuse. Instead, freely available and externally hosted Web 2.0 tools and services provided all of the functionality. For example, each student had a portfolio and a weblog provided by the site http://redbubble.com. The content of the default course site was populated by using BAM (discussed in section 5.3.6) to aggregate RSS feeds (generated by the external tools) which were then parsed and displayed by Javascript functions within the course site pages. Typically students and staff did not visit the default course site, as they could access all content by using a personal news reader to view the RSS feeds.

[![Home page for Web 2.0 course site](images/4677968716_99cc6a2cd0_m.jpg)](http://www.flickr.com/photos/david_jones/4677968716/ "Home page for Web 2.0 course site by David T Jones, on Flickr")

### References

Jones, D. (2002). Student Feedback, Anonymity, Observable Change and Course Barometers. World Conference on Educational Multimedia, Hypermedia and Telecommunications, Denver, Colorado, AACE.

Sturgess, P. and F. Nouwens (2004). "Evaluation of online learning management systems." Turkish Online Journal of Distance Education 5(3).