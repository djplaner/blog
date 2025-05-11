---
categories:
- chapter-5
- design-theory
- elearning
- moodle
- phd
- thesis
- webfuse
date: 2010-06-07 08:31:56+10:00
next:
  text: The Wf Framework
  url: /blog2/2010/06/07/the-wf-framework/
previous:
  text: Emergent and agile development
  url: /blog2/2010/06/05/emergent-and-agile-development/
title: Object orientation and design patterns
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Workarounds &laquo; The Weblog of (a) David Jones
      author_email: null
      author_ip: 76.74.255.38
      author_url: https://djon.es/blog/2010/06/13/workarounds/
      content: '[...] combination of the agile and adopted-focused development process
        of Webfuse, when combined with the design of Webfuse enabled the rapid development
        of &#8220;workarounds&#8221; that enabled the system to adapt to [...]'
      date: '2010-06-13 09:22:05'
      date_gmt: '2010-06-12 23:22:05'
      id: '3083'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The following is the third in a sequence of sections from chapter 5 of [my thesis](/blog2/research/phd-thesis/). These sections are describing the changes made in the development and support of Webfuse from 2000 through 2004 (and a bit beyond). This post very briefly describes the adoption a design patterns influenced, OO design.

The biggest challenge I faced in moving from Webfuse to Moodle was returning to a procedural approach to software development. Not just the movement from OO back to procedural, but from a system where I was deeply familiar with 900+ classes that provided a lot of low level and high level services for "e-learning" to a collection of procedural, spaghetti code where there was no clean separation of services, no easy way of finding which part did what. Of course, part of this difficulty was simply my newness to Moodle.

I am wondering what the implications might be for Moodle if it were to have been based on a "better" OO design.

#### Object orientation and design patterns

While the initial design rationale for Webfuse (Jones and Buchanan 1996) mentions that object-orientation is one of a number of approaches known to maximise adaptability the initial Webfuse implementation did not make use of object orientation. The key ideas of object-orientation arose during the 1960s, but it was the early 1990s before Fichman and Kemerer (1993) argued the object-orientation was the leading candidate to become "tommorow's dominant software process technology". With object-oriented design, system designers analyse and design in terms of objects or "things" - instead of operations or functions – with an executing system made up of interacting objects that maintain state and provided operations that manipulate that state information (Sommerville 2001). Proponents argue that object-orientation is an approach that helps avoid the labour intensive need to build all code from scratch due to its support for constructing software systems through the assembly of previous developed components (Fichman and Kemerer 1993). The independent encapsulation of state and operations enables this reuse and reduces design, programming, and validation costs and also reduces risk (Sommerville 2001).

However, programming with objects is complex and in the case of large and complex systems some of the ramifications are not yet fully mastered or understood (Szyperski 1999). Recognition of this problem contributed to significant interest in the identification, abstraction and use of design patterns to the problem of designing object-oriented systems. In perhaps the most important book on design patterns, Gamma et al (1995) argue that design patterns make it easier to reuse successful designs an architectures by expressing proven techniques in ways that are more accessible to developers and by allowing choice between design alternatives. A pattern is ‘a generic approach to solving a particular problem that can be tailored to specific cases. Properly used, they can save time and improve quality' (Fernandez 1998). Sommerville (2001) argues that while patterns are a very effective form or reuse, they do have a high cost of introduction in that they can only be used effectively by experienced developers. Given a particular object-oriented design issue, a design pattern will name, abstract and identify key aspects of a common design structure, describe when it might or might not apply given other constraints, and discuss the consequences and trade-offs of the pattern (Gamma, Helm et al. 1995).

The use of object-oriented design and design patterns in Webfuse consisted of the following inter-related uses:

1. Object-oriented wrapper around database operations;  
    Differences in how data is structured makes the transfer of data between relational databases and objects creates significant complexity (Fowler 2003). A solution to this complexity is a layer of software that isolates the two schema, a layer commonly called a data mapper (Fowler 2003). Work on the Webfuse "data mapper" began in 1999 and became a foundation for many of the remaining applications of object-oriented design.
2. University classes;  
    A number of classes were created to match common objects within the University which Webfuse had to manipulate. For example, the People::Campus class provided state and operations around CQU's various campuses.
3. Support classes for Webfuse page types;  
    As the first part of a planned move to convert the Webfuse page types to a complete object-oriented based approach, a range of support classes were implemented. These classes replaced the use of procedural code within new page types. The length of an average page type was reduced from 1000+ lines of code to less than 250 lines. The move to an object-oriented page type process was never completed due to a focus on other developments. The OO page type process was intended to provide the ability for a single web page to be produced by a combination of multiple page types, thus addressing the first lesson identified in Chapter 4.
4. Dynamic web applications;  
    To address the second lesson identified in Chapter 4 a framework for developing dynamic web applications was developed based on a model-view-controller framework. This work is described in more detail in the next section.

By 2010, the Webfuse code-base included 900+ classes, 65 dynamic web applications and a 190+ test harnesses. The test harnesses were mostly developed from 2001 through 2003 when the combination of the Webfuse agile development process, the increasing use of object-orientation, and a resourced Infocom web team enabled the adoption of test-driven development. Most importantly, the design patterns influenced adoption of object-oriented design provided the ability for the Webfuse adopter-focused, agile development process that resulted in the following developments.

### References

Fernandez, E. B. (1998). Building Systems Using Analysis Patterns. Third International Workshop on Software Architecture, Orlando, Florida, Association for Computing Machinery.

Fichman, R. and C. Kemerer (1993). "Adoption of software engineering process innovations: The case of object orientation." Sloan Management Review **34**(2): 7-22.

Fowler, M. (2003). Patterns of Enterprise Architecture. Boston, Addison-Wesley.

Gamma, E., R. Helm, et al. (1995). Design Patterns: Elements of Reusable Object-Oriented Software. Reading, Massachusetts, Addison-Wesley.

Jones, D. and R. Buchanan (1996). The design of an integrated online learning environment. Proceedings of ASCILITE'96, Adelaide.

Sommerville, I. (2001). Software Engineering, Addison-Wesley.

Szyperski, C. (1999). Component software: Beyond object-oriented programming. New York, Addison-Wesley.