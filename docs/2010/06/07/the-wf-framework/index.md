---
categories:
- chapter-5
- design-theory
- elearning
- phd
- thesis
- webfuse
date: 2010-06-07 10:04:23+10:00
next:
  text: The confusion of small and big changes
  url: /blog2/2010/06/07/the-confusion-of-small-and-big-changes-input-versus-output-and-types-of-systems/
previous:
  text: Object orientation and design patterns
  url: /blog2/2010/06/07/object-orientation-and-design-patterns/
title: The Wf Framework
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Some rough Webfuse usage statistics &#8211; 2001 through 2009 &laquo; The
        Weblog of (a) David Jones
      author_email: null
      author_ip: 76.74.255.31
      author_url: https://djon.es/blog/2010/06/17/some-rough-webfuse-usage-statistics-2001-through-2009/
      content: '[...] of the major developments in Webfuse from 1999/2000 was the development
        of the Wf framework which provided the basis for &#8220;Webfuse&#8221; interactive
        web applications. There were a broad [...]'
      date: '2010-06-17 14:10:01'
      date_gmt: '2010-06-17 04:10:01'
      id: '3084'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
Yet another section from Chapter 5 of [the thesis](/blog2/research/phd-thesis/) describing the various changes made to Webfuse in the period from 2000 onwards. This one (very briefly) describes the Webfuse framework for dynamic web applications.

You can see the impact of this experience in the development practices I'm bringing to my work in PHP and Moodle. There are early glimmers of MVC and the Wf Framework in [BIM](/blog2/research/bam-blog-aggregation-management/) and the [indicators block](/blog2/2010/05/17/moving-the-indicators-moodle-block-a-factory-class/).

#### The Wf Framework

The absence of support for dynamic web applications is the second lesson identified in Chapter 4 from the development and use of Webfuse from 1997 through 1999. Rather than just being a publishing environment the Web was becoming an application development environment. An external consultancy during 1999 that required the development of a web-based helpdesk interface, led to the development of the Wf framework for Webfuse. The Wf framework was based on the Model-View-Controller (MVC) framework, made use of the data mapper pattern described in the previous section, and was used to develop 65 dynamic web applications.

Originally proposed during the 1980s for the development of graphical user interfaces, the MVC framework allows a single object to be presented in multiple ways with each presentation having a separate style of interaction (Sommerville 2001). Gamma et al (1995) describe MVC as a triad of classes used to build user interfaces in Smalltalk-80 and draws on a number of patterns including Strategy, Factory, Observer, Composite and Strategy. The MVC architectural pattern has since become widespread through its use in a number of web application frameworks.

All dynamic web applications using the Wf framework used a URL of the format

http://hostname/object/objectName/method/methodName/?param=value

For example, the URL for the "Staff MyCQU" application's course history method for the CQU course COIS12073 was accessed using the following URL

https://webfuse.cqu.edu.au/wf/object/StaffMyCQU/method/CourseHistory/?COURSE=COIS12073

To parse and handle this URL the Apache web server was configured to use a Perl module. That module used the WebfuseFactory class to identify and call the appropriate application controller (i.e. matching the objectName – StaffMyCQU - from the URL) and calls the appropriate method (i.e. matching the methodName – CourseHistory – from the URL) of that controller class. Any parameters (e.g. COURSE=COIS12073) would be passed to that method and the controller would also perform authentication and access control checks to ensure that the user had permission to perform the requested method. The method in turn would normally consist of creating a model class (CourseHistory), a view class (CourseHistory\_View), passing the model to the view, and using the view to generate the HTML to send back to the browser.

Sommerville (2001) argues that the inherent complexity of frameworks mean that it takes time to learn how to use them and that this can limit their use. Experience within Webfuse in the early 2000s reinforced this perspective as new developers, familiar with the simpler coding approaches of web "scripting" common at this time, took some time to grasp and see the value of this complexity. The consistent metaphor provided by the Wf framework also clashed somewhat with the Perl (the scripting language used to implement Webfuse) ethos of "There is more then one way to do it" and the tendency for Perl developers to "do it their way" (Jones 2003). However, as shown below (especially in Section 5.3.6 on Workarounds), the consistent metaphor and other advantages provided by this additional, initial complexity provided an important part of the ability of Webfuse to respond quickly and effectively to organisational requirements and changes.

### References

Gamma, E., R. Helm, et al. (1995). Design Patterns: Elements of Reusable Object-Oriented Software. Reading, Massachusetts, Addison-Wesley.

Jones, D. (2003). How to live with ERP systems and thrive. 2003 Tertiary Education Management Conference, Adelaide.

Sommerville, I. (2001). Software Engineering, Addison-Wesley.