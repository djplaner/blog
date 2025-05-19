---
categories:
- design-theory
date: 2008-12-03 02:17:53+10:00
next:
  text: Accept the fact that we have to treat almost anybody as a volunteer - implications
    for learning and teaching
  url: /blog/2008/12/05/accept-the-fact-that-we-have-to-treat-almost-anybody-as-a-volunteer-implications-for-learning-and-teaching/
previous:
  text: Selecting a tripod
  url: /blog/2008/11/29/selecting-a-tripod/
tags:
- helpdesk
title: A time to rethink enterprise helpdesk systems and management
type: post
template: blog-post.html
---
As part of my current work I provide support to academic staff using a learning management system. The reactive part of this support is funneled though an organisational helpdesk that is run along fairly common IT helpdesk processes and uses a fairly common enterprise helpdesk application.

For me the reactive part of this sort of support involves solving peoples' problems. In most part, it is a communication problem requiring helping the person understand how the reality of the system and how it operates does not match what they understand and what they are trying to do. In some of these instances, the people who are having these problems are stressed and frustrated.

Something they thought was going to be simple, didn't work. Possibly that something is important to them and they fear negative ramifications if it doesn't work (e.g. a teaching staff member in charge of a large course where assignment submission has just gone down). Perhaps their best laid plans are now in tatters.

All of this brings me to the view that the act of providing this type of helpdesk support is a communication activity. A critical success factor is how well you communicate with the client in a way that puts them at ease, assuages their fears and frustration, and solves their problem. It is primarily an act of communication between two people.

Which makes me wonder why the current IT helpdesk application I'm forced to use actively makes effective communication horrendously difficult? Why does this application provide so little support for ensuring that the communication is effective and more importantly is perceived by the client to be positive?

### Purpose

My current explanation is that the folk who select and implement these helpdesk systems are central IT units. Generally, IT units that have been infected by the [ITIL](http://en.wikipedia.org/wiki/Information_Technology_Infrastructure_Library) disease and all the burdens that brings with it. Point of order - it might be argued that Itil isn't all that bad, perhaps, but the way most IT units implement it is. They tend to end up focused on stats, SLAs and management of client dissatisfaction rather than on actively helping the client.

Because of this focus, the helpdesk application vendors know that they have to provide support for what the IT units want. After all, it's the IT units that will make the decision to purchase. Since the IT unit places emphasis on stats and management of the helpdesk, that's what the IT applications place emphasis on.

### Example

An example of this emphasis is the amount of screen space on the interface that is set aside for communication activities as opposed to management activities. On the web interface of the system I'm looking at there are two boxes with about 20 characters for a summary of and the details of the problem reported by the client. The rest of the page is taken up with "management" stuff. This includes 10 or tabs to related pages that contain "management" stuff.

If the client attaches various files to their original email (e.g. screenshots) you have to visit one of these additional tabs, select the appropriate file, click on view and have a Microsoft application to be able to view it. It takes more work to view the information provided by the client.

What's worse, the way the system is configured the client gets canned, badly formatted email messages as the default form of communication. Emails that come from the helpdesk system and make it incredibly difficult for the client to know with whom they are talking. In addition, if I use my web browser most of the content of what I send is sent without any line breaks.

I compare this experience with a commercial helpdesk system with my experience with an [open source system](http://bestpractical.com/rt/) (RT). The vast majority of the interface with this system was devoted to showing the communication and it made communication easy.

### Implications

There looks like there is scope to do research around the importance of communication to client satisfaction with helpdesk systems and support. Flowing from that, how well do existing helpdesk system support this and how should would you design a better, more appropriate helpdesk system. Would such a system also require changes to processes and management of this process by IT units? Would such changes bring benefits? What are the information systems design theories that could be developed from this?