---
categories:
- chapter-2
- design-theory
- elearning
- phd
- psframework
- thesis
- webfuse
date: 2011-01-06 10:43:11+10:00
next:
  text: Thesis acknowledgements version 0.5
  url: /blog/2011/01/07/thesis-acknowledgements-version-0-5/
previous:
  text: Progressing the student interface for bim2
  url: /blog/2010/12/30/progressing-the-student-interface-for-bim2/
title: A command for organisations? Program or be programmed
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: Maurice A. Barry
      author_email: maurice.a.barry@gmail.com
      author_ip: 24.222.32.1
      author_url: http://mauriceabarry.wordpress.com
      content: A very well laid out argument! No surprise, then that I find myself in
        agreement. A can even think of several cases where I have seen exactly that happen.
        LMS implementation is perhaps the best known example but I have also seen the
        same with SIS (Student Information Systems) implementation--insutead of matching/building
        a product to the need, one is purchased and people learn to work within its limitations
        and adopt its work flows--not an ideal situation at all.
      date: '2013-01-10 03:13:23'
      date_gmt: '2013-01-09 17:13:23'
      id: '3218'
      parent: '0'
      type: comment
      user_id: '0'
    
pingbacks:
    []
    
---
I've just finished the Douglas Rushkoff book [Program or be Programmed: Ten commands for a digital age](http://www.amazon.com/Program-Be-Programmed-Commands-Digital/dp/1935928155/). As the title suggests the author provides ten "commands" for living well with digital technologies. This post arises from the titular and last command examined in the book, Program or be programmed.

[![Dougls Rushkoff](images/5263891846_6645a80563_m.jpg)](http://www.flickr.com/photos/kevinkrejci/5263891846/ "Dougls Rushkoff by Kevin Krejci, on Flickr")

This particular command was of interest to me for two reasons. First, it suggests that learning to program is important and that more should be doing it. As I'm likely to become a information technology high school teacher there is some significant self-interest in there being a widely accepted importance to learning ot program. Second, and the main connection for this post, is that my experience with and observation of universities is that they are tending "to be programmed", rather than program. In particular when it comes to e-learning.

This post is some thinking out loud about that experience and the Ruskoff command. In particular, it's my argument that universities are being programmed by the technology they are using. I'm wondering why? Am hoping this will be my last post on these topics, I think I've pushed the barrow for all its worth. Onto new things next.

### Program or be programmed

Rushkoff's (p 128) point is that

> Digital technology is programmed. This makes it biased toward those with the capacity to write the code.

This also gives a bit of a taste for the other commands. i.e. that there are inherent biases in digital technology that can be good or bad. To get the best out of the technology there are certain behaviours that seem best suited for encouraging the good, rather than the bad.

One of the negative outcomes of not being able to program, of not being able to take advantage of this bias of digital technology is (p 15)

> ...instead of optimizing our machines for humanity - or even the benefit of some particular group - we are optimizing humans for machinery.

### But is _all_ digital technology programmed?

In terms of software, yes, it is all generally created by people programming. But not all digital technology is programmable. The majority of the time, money and resources being invested by universities (I'll stick to unis, however, much of what I say may be applicable more broadly to organisations) is in "enterprise" systems. Originally this was in the form of Enterprise Resource Planning system (ERPs) like Peoplesoft. It is broadly recognised that modifications to ERPs are not a good idea, and that instead the ERP should be implemented in "vanilla" form (Robey et al, 2002).

That is, rather than modify the ERP system to respond to the needs of the university. The university should modify its practices to match the operation of the ERP system. This appears to be exactly what Rushkoff warn's against "we are optimizing humans for machinery".

This is important for e-learning because, I would argue, the Learning Management System (LMS) is essentially an ERP for learning. And I would suggest that much of what goes on around the implementation and support of an LMS within a university is the optimization of humans for machinery. In some specific instances that I'm aware of, it doesn't matter whether the LMS is open source or not. Why?

### Software remains hard to modify

Glass (2001), describing one of the frequently forgotten fundamental facts about software engineering, suggested that maintenance consumes about 40 to 80 percent of software costs, with 60% of the maintenance cost is due to enhancement. i.e. a significant proportion of the cost of any software system is adding new features to it. You need to remember that this is a general statement. If the software you are talking about is part of a system that operates within a continually changing context, then the figure is going to be much, much higher.

Most software engineering remains focused on creation. On the design and implementation of the software. There hasn't been enough focus on on-going modification, evolution or co-emergence of the software and local needs.

Take Moodle. It's an LMS. Good and bad like other LMS. But it's open source. It is meant to be easy to modify. That's one of the arguments wheeled out by proponents when institutions are having to select a new LMS. And Moodle and its development processes are fairly flexible. It's not that hard to add a new activity module to perform some task you want that isn't supported by the core.

The trouble is that Moodle is currently entering a phase which suggests it suffers much the same problems as most large enterprise software applications. The transition from Moodle 1.x to Moodle 2.0 is highlighting the problems with modification. Some folk are reporting difficulties with the upgrade process, others are deciding to delay the upgrade as some of the third-party modules they use haven't been converted to Moodle 2. There are even suggestions from some that mirror the "implement vanilla" advice for ERPs.

It appears that "we are optimizing humans for machinery".

I'm wondering if there is anyone doing research how to make systems like Moodle more readily modifiable for local contexts. At the very least, looking at how/if the version upgrade problem can be improved. But also, the ability to modify the core to better suit local requirements. There are aspects there already. One of the difficulties is that to achieve this you would have to cross boundaries between the original developers, service providers (Moodle partners) and the practices of internal IT divisions.

### Not everyone wants to program

One reason this will be hard is that not everyone wants to program. Recently, D'Arcy Norman [wrote a post](http://www.darcynorman.net/2010/12/29/on-breaking-away-from-hosted-silos/) talking about the difference between the geeks and folk like his dad. His dad doesn't want to bother with this techy stuff, he doesn't want to "program".

This sort of problem is made worse if you have an IT division that has senior management with backgrounds in non-IT work. For example, an IT director with a background in facilities management isn't going to understand that [IT is protean](/blog/2009/02/09/the-protean-nature-of-modern-technology-another-limitation-of-most-views-of-e-learning/), that it can be programmed. Familiar with the relative permanence of physical buildings and infrastructure such a person isn't going to understand that IT can be changed, that it should be optimized for the human beings using the system.

### Organisational structures and processes prevent programming

One of the key arguments in [my EDUCAUSE presentation](http://www.slideshare.net/davidj/alternatives-for-the-institutional-implementation-of-elearning-lessons-from-12-years-of-webfuse) (and my thesis) is that the structures and processes that universities are using to support e-learning are biased away from modification of the system. They are biased towards vanilla implementation.

First, helpdesk provision is treated as a generic task. The folk on the helpdesk are seen as low-level, interchangeable cogs in a machine that provides support for all an organisation's applications. The responsibility of the helpdesk is to fix known problems quickly. They don't/can't become experts in the needs of the users. The systems within which they work don't encourage, or possibly even allow, the development of deep understanding.

For the more complex software applications there will be an escalation process. If the front-line helpdesk can't solve the problem it gets handed up to application experts. These are experts in using the application. They are trained and required to help the user figure out how to use the application to achieve their aims. These application experts are expert in optimizing the humans for the machinery. For example, if an academic says they want students to have an individual journal, a Moodle 1.9 application expert will come back with suggestions about how this might be done with the Moodle wiki or some other kludge with some other Moodle tool. If Moodle 1.9 doesn't provide a direct match, they figure out how to kludge together functionality it does have. The application expert usually can't suggest using something else.

By this stage, an academic has either given up on the idea, accepted the kludge, gone and done it themselves, or (bravely) decided to escalate the problem further by entering into the application governance process. This is the heavy weight, apparently rational process through which requests for additional functionality are weighed against the needs of the organisation and the available resources. If it's deemed important enough the new functionality might get scheduled for implementation at some point in the future.

There are many problems with this process

- Non-users making the decisions;  
    Most of the folk involved in the governance process are not front-line users. They are managers, both IT and organisational. They might include a couple of experts - e-learning and technology. And they might include a couple of token end-users/academics. Though these are typically going to be innovators. They are not going to be representative of the majority of users.
    
    What these people see as important or necessary, is not going to be representative of what the majority of academic staff/users think is important. In fact, these groups can quickly become biased against the users. I attended one such meeting where the first 10/15 minutes was spent complaining about foibles of academic staff.
    
- [Chinese whispers](http://en.wikipedia.org/wiki/Chinese_whispers);  
    The argument/information presented to such a group will have had to go through chinese whispers like game. An analyst is sent to talk to a few users asking for a new feature. The analyst talks to the developers and other folk expert in the application. The analysts recommendations will be "vetted" by their manager and possibly other interested parties. The analysts recommendation is then described at the governance meeting by someone else.
    
    All along this line, vested interests, cognitive biases, different frames of references, initial confusion, limited expertise and experience, and a variety of other factors contribute to the original need being morphed into something completely different.
    
- Up-front decision making; and  
    Finally, many of these requests will have to battle against already set priorities. As part of the budgeting process, the organisation will already have decided what projects and changes it will be implementing this year. The decisions has been made. Any new requirements have to compete for whatever is left.
- Competing priorities.  
    Last in this list, but not last overall, are competing priorities. The academic attempting to implement individual student journals has as their priority improving the learning experience of the student. They are trying to get the students to engage in reflection and other good practices. This priority has to battle with other priorities.
    
    The head of the IT division will have as a priority of staying in budget and keeping the other senior managers happy with the performance of the IT division. Most of the IT folk will have a priority, or will be told that their priority is, to make the IT division and the head of IT look good. Similarly, and more broadly, the other senior managers on 5 year contracts will have as a priority making sure that the aims of their immediate supervisor are being seen to be achieved........
    

These and other factors lead me to believe that as currently practiced, the nature of most large organisations is to be programmed. That is, when it comes to using digital technologies they are more likely to optimize the humans within the organisation for the needs of the technology.

Achieving the alternate path, optimizing the machinery for the needs of the humans and the organisation is not a simple task. It is very difficult. However, by either ignoring or being unaware of the bias of their processes, organisations are sacrificing much of the potential of digital techology. If they can't figure out how to start programming, such organisations will end up being programmed.

### References

Robey, D., Ross, W., & Boudreau, M.-C. (2002). Learning to implement enterprise systems: An exploratory study of the dialectics of change. Journal of Management Information Systems, 19(1), 17-46.