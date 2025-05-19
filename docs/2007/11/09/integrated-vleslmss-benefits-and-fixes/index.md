---
categories:
- ple
- web-20-course-sites
date: 2007-11-09 00:03:41+10:00
next:
  text: Simplicity, e-learning and shadow systems
  url: /blog/2007/11/16/simplicity-e-learning-and-shadow-systems/
previous:
  text: PLEs (&quot;social media&quot;) and measuring/ensuring success
  url: /blog/2007/11/05/ples-social-media-and-measuringensuring-success/
title: Integrated VLEs/LMSs - benefits and fixes
type: post
template: blog-post.html
---
Niall Sclater is the Director of the Open University's (UK) VLE (UK acronym for LMS) Programme which is implementing Moodle ([some FAQs](http://conclave.open.ac.uk/ouvlefaq/)). Over the last few days he has made a couple of interesting posts:

- [Reinventing the wheel?](http://sclater.com/blog/?p=38); and
- [VLEs and the institutional control of students](http://sclater.com/blog/?p=41).

As you would expect from someone responsible for an institutional project implementing an integrated VLE both posts either defend or promote the characteristics of an integrated VLE.

I have an interest in moving towards a much more eclectic approach to providing the functionality required for e-learning within a university. However, I also don't think its without its problems or necessarily something that would happen quickly. Writing about these posts helps crystalise some of the issues.

I'll start with the first one.

### Problems and benefits of reinventing the wheel

The first post is essentially a list of the problems to be faced if the "blog" and "wiki" tools integrated into an LMS (in Niall's case Moodle) were to be replaced by open source alternatives like Wordpress or Mediawiki.

The post is interesting because these are real problems to be addressed if the idea of making greater use of Web 2.0 tools as part of an eclectic, but integrated, alternative to an LMS is going to happen.

The list includes the following. I've attempted to generalise beyond Moodle and the OU and then provide an alternate perspective. I'm not claiming that the alternate perspective is the stronger argument, just different.

1. An institution will already have internal expertise in the LMS they are using. Using external tools would require increased effort (read cost) to maintain knowledge of the functionality, code base and release cycles of open source software.  
    However, the pool of external expertise that an institution can draw upon to supplement or replace internal expertise will almost certainly be much larger for the external tool than the VLE/LMS. Of course, there is the question of "integrated knowledge". A Moodle expert would know all of the tools. But a lot of the Moodle tools are extensions, by 3rd parties which need to be learnt. But then I wonder if a PHP/Java/Web 2.0 expert would also have the same skills and capabilities but with a much broader collection of software to draw upon.
    
    Also if you were going to actually install the external blog/wiki tool onto a university's infrastructure you wouldn't need to know about multiple blogs/wikis. Just the one chosen to be installed. The major difference would be that the breadth of choice would be much greater if you were looking at generic tools than if you were looking at tools that would fit into a particular VLE.
    
2. Non-LMS products have widely differing user interfaces and have not been enhanced for accessibility and usability in the way that has been possible for Moodle tools.  
    This is a potential problem but then I'm not yet convinced that quality through consistency works effectively. If the interface is designed well, I'm not sure it really matters if the interface is different. This is something I'd love to research/investigate at some stage.
    
    I'd also suggest that an active open source product like Wordpress is always going to be able to have (or eventually develop) a better interface. Also, the majority of these systems are "skinnable" and thus, if really necessary, you could make the interface the same.
    
3. Single LMS integration allows easy transfer of data between applications within the LMS. Doing so with external applications would be a highly complex software engineering task.  
    I'm not so sure it would be that highly complex. The Webfuse system has been designed to integrate external applications. At least 5 years ago we integrated a discussion forum into the system. A fairly junior (but very capable) technical staff member took a few weeks to integrate. It took that long primarily because the discussion forum (and Webfuse) didn't really follow "good software engineering practice". Most of the more modern systems I've seen make this sort of thing much easier.
4. With an integrated LMS, the user only has to authenticate once. No need to replicate user databases, access permissions etc.  
    This to can be worked around and fixed. Especially as systems move towards single sign-on, openId and similar sorts of technology.
5. Easier to track usage within a single database rather than having several separate systems.  
    VLEs/LMSs and enterprise systems in general (e.g. Peoplesoft etc) are known to be really terrible at reporting. Most organisations are using business intelligence/data mining tools to track usage, trends etc. These types of tools are designed to bring disparate databases together.
6. A cut-down blog/wiki tool may not be as feature packed as a specialist tool but it may provide the necessary functionality for learning and teaching in an appropriately simple method.  
    There is an argument to be made here. But there's also an arguments to be made that generic tools can be "skinned" to achieve the same outcomes and that there is benefits to students in using real tools.