---
title: 30% of information about task performance
date: 2010-08-08 14:00:56+10:00
categories: ['c2d2', 'chapter-5', 'design-theory', 'elearning', 'highereducation', 'phd', 'reflectivealignment', 'thesis', 'webfuse']
type: post
template: blog-post.html
---
Over on the Remote Learner blog, Jason Cole has [posted](http://info.remote-learner.net/) some information about a keynote by Dr Richard Clark at one of the US MoodleMoots. I want to focus on one key quote from that talk and its implications for Australian higher education and current trends to "improve" learning and teaching and adopt open source LMS (like Moodle).

It's my argument that this quote, and the research behind it, has implications for the way these projects are conceptualised and run. i.e. they are missing out on a huge amount of potential.

### Task analysis and the 30%

The quote from the presentation is

> In task analysis, top experts only provide 30% of information about how they perform tasks.

It's claimed that all the points made by Clark in his presentation are supported by research. It appears likely that the support for this claim comes from Sullivan et al (2008). This paper address the problem of trying to develop procedural skills necessary for professions such as surgery.

The above quote arises due to the problems experts have in describing what they do. Sullivan et al (2008) offer various descriptions and references of this problem in the introduction

> This is often difficult because as physicians gain expertise their skills become automated and the steps of the skill blend together \[2\]. Automated knowledge is achieved by years of practice and experience, wherein the basic elements of the task are performed largely without conscious awareness \[3\]. This causes experts to omit specific steps when trying to describe a procedure because this information is no longer accessible to conscious processes \[2\]

Then later, when describing the findings of their research they write

> The fact that the experts were not able to articulate all of the steps and decisions of the task is consistent with the expertise literature that shows that expertise is highly automated \[2,3,5\] and that experts make errors when trying to describe how they complete a task \[3,6,7\]. In essence, as the experts developed expertise, their knowledge of the task changed from declarative to procedural knowledge. Declarative knowledge is knowing facts, events, and objects and is found in our conscious working memory \[2\]. Procedural knowledge is knowing how to perform a task and includes both motor and cognitive skills \[2\]. Procedural knowledge is automated and operates outside of conscious awareness \[2,3\]. Once a skill becomes automated, it is fine-tuned to run on autopilot and executes much faster than conscious processes \[2,8\]. This causes the expert to omit steps and decision points while teaching a procedure because they have literally lost access to the behaviors and cognitive decisions that are made during skill execution \[2,5\].

### The link to analysis and design

A large number of universities within Australia are either:

1. Changing their LMS to an open source LMS (e.g. Moodle or Sakai), and using this as an opportunity to "renew" their online learning; and/or
2. Busy on broader interventions to "renew" their online learning due to changes in government policies such as quality assurance, graduate attributes and a move to demand funding for university places.

The common process being adopted by most of these projects is from the planning school of process. i.e. you undertake analysis to identify all relevant, objective information and then design the solution on that basis. You then employ a project team to ensure that the design gets implemented, and finally you put in a skeleton team that maintains the design. This works in terms of information systems (e.g. the selection, implementation and support of a LMS) or broader organisational change (e.g. strategic plans).

The problem is that the "expert problem" Clark refers to above means that it is difficult to gather all the necessary information. It's difficult to get the people with the knowledge to tell all that they know.

A related example.

### The StaffMyCQU Example

Some colleagues and I - over a period of almost 10 years - designed, supported, and evolved an information system call Staff MyCQU. An early part of it's evolution is described in the "Student Records" section of [this paper](/blog2/publications/how-to-live-with-erp-systems-and-thrive/). It was a fairly simple web application that provided university staff with access to student records and range of related services. Over it's life cycle, a range of new and different features were added and existing features tweaked, all in response to interactions with the system's users.

Importantly, the systems developers were also generally the people handling user queries and problems on the "helpdesk". Quite often, changes to the system would result in tweaks and changes. Rather than being designed up front, the system grew and changed with people using it.

The technology used to implement Staff MyCQU is now deemed ancient and, even more importantly, the system and what it represents is now politically tainted within the organisation. Hence, for the last year or so, the information technology folk at the institution have been working on replacement systems. Just recently, there's been some concrete outcomes of that work which has resulted in systems being shown to folk, including some of the folk who had used Staff MyCQU. On being shown a particular feature of the new system, it soon became obvious that the system didn't include a fairly common extension of the feature. An extension that had actually been within StaffMyCQU from the start.

The designers of the new system, with little or no direct connection with actual users doing actual work, don't have the knowledge about user needs to design a system that is equivalent to what already exists. A perfect example of why the strict separation of analysis, design, implementation and use/maintenance that is explicit in most IT projects and divisions is a significant problem.

### The need for growing knowledge

Sullivan et al (2008) suggest cognitive task analysis as a way to better "getting at" the knowledge held by the expert, and there's a place for that. However, I also think that there is a need, especially in some contexts, for recognition that the engineering/planning method is just not appropriate for some contexts. In some contexts, you need more of a growing/gardening approach. Or, in some cases you need to include more of the growing/gardening approach into your engineering method.

Rather than seeking to gather and analyse all knowledge separated from practice and prior to implementation. Implementation needs to be designed to pay close attention to knowledge that is generated during implementation and the ability to act upon that knowledge.

### Especially for wicked problems and complex systems

Trying to improve learning and teaching within a university is a [wicked problem](http://en.wikipedia.org/wiki/Wicked_problem). There are many different stakeholders or groups of stakeholders, each with a different frame of reference which leads to different understanding of how to solve the problem. Simple techno-rational solutions to wicked problems rely on the adoption of one of those frames of reference and ignorance of the remainder.

For example, implementation of a new LMS is seen as an information technology problem and treated as such. Consequently, success is measured by uptime and successful project implementation. Not on the quality of learning and teaching that results.

In addition, as you solve wicked problems, you and all of the stakeholders learn more about the problem. The multiple frames of reference change and consequently the appropriate solutions change. This is getting into the area of complex adaptive systems. Dave Snowden has a [recent post](http://www.cognitive-edge.com/blogs/dave/2010/08/humans_are_not_ants_agents_or.php) about why human complex adaptive systems are different.

### Prediction

Universities that lean too heavily on engineering/planning approaches to improving learning and teaching will fail. However, they are likely to appear to succeed due to the types of indicators they choose to adopt to as measurements of success and the capability of actors to game those indicators.

Universities that adopt more of a gardening approach, will have greater levels of success, but will have a messier time of it during their projects. These universities will be where the really innovative stuff comes from.

### References

Sullivan, M., A. Oretga, et al. (2008). "[Assessing the teaching of procedural skills: can cognitive task analysis add to our traditional teaching methods.](http://www.usc.edu/dept/education/cogtech/publications/sullivan_etal_cta.pdf)" The American Journal of Surgery 195: 20-23.