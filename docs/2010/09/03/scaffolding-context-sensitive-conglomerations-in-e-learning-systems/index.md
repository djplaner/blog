---
categories:
- chapter-5
- design-theory
- elearning
- phd
- thesis
- webfuse
date: 2010-09-03 12:48:16+10:00
next:
  text: Misc. reflections on reading about situated cognition
  url: /blog2/2010/09/03/misc-reflections-on-reading-about-situated-cognition/
previous:
  text: Situated shared practice, curriculum design and academic development
  url: /blog2/2010/08/30/situated-shared-practice-curriculum-design-and-academic-development/
title: Scaffolding, context-sensitive conglomerations in e-learning systems
type: post
template: blog-post.html
---
For the last week or so I've been attempting to bring together the principles that underpin the design theory for e-learning that will be the main contribution of my thesis. This post summarises one of the principles of form and function that is emerging from the last week or so. I using this blog post to escape the confines of PhD-ese and see if writing about it can generate some further refinement.

Am aiming for brevity and clarity in the following.

A design theory contains principles for form and function; and for implementation. The following is more form and function, while [the previous post](/blog2/2010/08/30/situated-shared-practice-curriculum-design-and-academic-development/) is more implementation. There is more to the ISDT than just these two posts.

### The problem

The functionality provided by most e-learning systems are in the form of low-level primitive tasks (e.g. upload a document, add a discussion forum, create a quiz). Most e-learning systems provide a fairly large collection of these low-level features. Many of these features, because they are designed for the general case, come with large numbers of options and configuration settings so that the task can be tweaked to the broadest collection of uses.

Consequently, achieving a high-level task (e.g. supporting a discussion forum that encourages student-to-student collaboration, or creating an educationally well-designed course website) requires a significant amount of knowledge, skills and time on the part of teaching academics. Some (perhaps much) of the time spent by teachers in leveraging these low-level, very general features is expended on bridging the gap between the generality of the feature set and the specifics of the context. Much of the time is spent trying to translate and wrangle what is known about good practice into the specifics required to implement it with the low-level feature set of the e-learning system.

I suggest that these difficulties limit the quality and quantity of how these feature sets are used. These difficulties appear to be one of the factors that contribute to the on-going fairly poor quality of most e-learning within formal education settings, especially universities.

### Scaffolding, context-sensitive conglomerations as a solution?

The idea is that an e-learning system should provide the ability to create "scaffolding, context-sensitive, conglomerations" of its low-level feature set.

#### Examples

An example of this is [the default course site](/blog2/2010/06/25/default-course-sites-and-wizards-version-2-0/) "conglomeration" used in the Webfuse system. This is the system I designed and forms the basis for my PhD. So you can see where the idea has come from. The default course sites conglomeration was aimed at making it very simple for academics to create a default course site. So simple, in fact, that if they wanted to, they didn't have to do anything.

Another possible example of a "conglomeration" from my own work could be the Moodle module [BIM](/blog2/research/bam-blog-aggregation-management/). BIM is a conglomeration of external blog engines (e.g. [Wordpress.com](http://wordpress.com/) and various Moodle features, especially the gradebook. The BIM "conglomeration" is designed to make it simpler for teachers to manage students using individual blogs for assessment and other purposes. It provides a bridge between the external blogs and Moodle's making/management features.

Moving further afield, the work being done by Desire2Learn with its [instructional design wizard](http://www.desire2learn.com/experience-it/) provide another approach to the provision of a conglomeration. The "Wizard" approach is used.

#### Conglomerations

In this context, a conglomeration is essentially a way to group together the existing low-level functionality provided by the e-learning system into something at a much higher level of abstraction. The term conglomeration has been chosen specifically to avoid terms like component, framework, package etc that, at least with some technical systems, refer to fairly specific ways of combining technology features. I'm trying to avoid these terms for a range of reasons, including:

- Non-specificity;  
    The aim of the ISDT (information systems design theory) is to provide broad guidance that is not specific to a particular approach or technology.
- Inclusivity;  
    Most of the technical approaches to grouping functional (e.g. component-based architectures) are not inclusive. i.e. if you're using architecture X, you can only group features that are implemented using architecture X. While recognising there's always going to be a practical need for something like this, with my ISDT I am trying to argue that for e-learning systems, the conglomeration mechanism needs to be as inclusive as possible (e.g. BIM's reliance on RSS/Atom feeds - loose coupling - rather than a specific API for a particular blog service).
- User focus.  
    As part of all this the conglomerations only have to group these features from the perspective of the user. It doesn't actually mean that they are technically grouped through the use of the same architecture. What's important is that the user experience with the conglomeration leads them to believe the different bits of low-level functionality are integrated and working together.

#### Context-sensitive

Context-sensitive implies that the conglomerations know something about and offer support for factors or knowledge that is specific to the context of the people using the conglomeration. i.e. it's not such a general purpose tool as to require the user to bridge the gap between their context and the tool.

For example, the default course site approach within Webfuse was designed to know about and integrate with as much of the local context as possible. The course synopsis, details about the assessment, staff details etc were automatically drawn from institutional databases and available within the conglomeration. In a more able and educationally enlightened context, the default course site conglomeration might have known about and offered specific support for the use of institutional graduate attributes or course learning outcomes.

#### Scaffolding

This aspect is still a work in progress and builds somewhat on the context-sensitive attributed. The term scaffolding was chosen because of the connection between this idea and situated/distributed cognition, cognitive apprenticeship etc. The idea is that the e-learning system should be designed in a way to help the teachers (and perhaps students) learn about using the system effectively.

The assumption is that for most teachers using the e-learning system to improve and/or change their teaching practice is a learning process. They haven't done this before. Rather than treat learning about how to make this change a separate professional development activity, the e-learning embodies/embeds the learning into its conglomerations. In some way, the system adopts an approach that includes situated modelling, coaching and fading.

Collins et al (1991) define it this way

> _When scaffolding is provided by a teacher, it involves the teacher in executing parts of the task that the student cannot yet manage_. A requisite to such scaffolding is accurate diagnosis of the student’s current skill level or difficulty and the availability of an intermediate step at the appropriate level of difficulty in carrying out the target activity. Fading involves the gradual removal of supports until students are on their own.

Am still considering the implications of this addition and how far to take it/interpret it. Potentially this could suggest that the system have a model of the teachers' abilities and be "intelligent". I don't see this as being a requirement. An equally plausible, and probably more likely, approach would be for this diagnosis to be performed by people.

Need to think this through some more and see how much more of the insights offered by the learning theories this idea is based on could/should be used.

### References

Collins, A., Brown, J. S., & Holum, A. (1991). Cognitive apprenticeship: Making thinking visible. American Educator(Winter), 6-11, 38-46.