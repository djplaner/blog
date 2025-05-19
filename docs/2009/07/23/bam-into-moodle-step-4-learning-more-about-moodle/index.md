---
categories:
- bam
date: 2009-07-23 13:12:14+10:00
next:
  text: '"BAM into Moodle #5 - Coding a block?"'
  url: /blog/2009/07/23/bam-into-moodle-5-coding-a-block/
previous:
  text: Improving CEQ Outcomes
  url: /blog/2009/07/23/improving-ceq-outcomes/
title: '"BAM into Moodle Step #4 - Learning more about Moodle"'
type: post
template: blog-post.html
---
In [the previous step](/blog/2009/07/21/bam-into-moodle-step-3-some-initial-development/) I got to know a bit more about the Moodle code base, libraries and idioms. Even got to modify a bit of code - nothing much more complex than hello world. Time to continue that journey.

### Roles and capabilities

Continuing my journey through [Unit 6](http://dev.moodle.org/mod/resource/view.php?id=43) of the Moodle Programming Unit. This time with roles and capabilities.

Apparently before v1.7 there were fixed roles. Gee, I learnt that in Webfuse in 1996 - sorry, writing historical chapters of the thesis, revisiting old ground and getting pissy about it all.

Main terms are:

- Contexts - hierarchical "spaces" in which "permissions" apply
    - 7 of them - from broadest to most specific: CONTEXT\_SYSTEM, CONTEXT\_PERSONAL, CONTEXT\_USER (spelled CONETXT in docs), CONTEXT\_COURSECAT, CONTEXT\_COURSE, CONTEXT\_MODULE, CONTEXT\_BLOCK.
    - Permissions not set within a context are inherited from a more general context.
    
    - Capacilities - a specific Moodle action that can be executed by a user
        - e.g. 'moodle/course:update' - updating course settings
        - e.g. 'moodle/course:viewhiddencourses' - guess?
    - Roles - a named set of all the capabilities with associated permissions (which ain't a great explanation)
        - e.g. student, forum moderator etc.
    - Permissions - describes the ability of a role to perform a certain capability (Que?)
        
        - permissions for a capbility are set within a context - e.g. course.
        - Four permissions available to be set for a capability of a role within a context:
            - CAP\_INHERIT - inherit permission from more general context
            - CAP\_ALLOW - guess
            - CAP\_PREVENT - deny the capability in the current context and more specific contexts, unless over-ridden
            - CAP\_PROHIBIT - deny a capability and don't allow it to be over-ridden.
        
        #### Functions for roles and capabilities
        
        - require\_login - require user to be logged in and perform some other checks
        - get\_context - returns a context instance object containing a context level and an instance id - e.g. CONTEXT\_COURSE and a course id. This is needed to do the next step.
        - require\_capability
        - has\_capability
        
        ### Documentation
        
        [PHPDoc](http://manual.phpdoc.org/) used for code documentation - another thing to learn.