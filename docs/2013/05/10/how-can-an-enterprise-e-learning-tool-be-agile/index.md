---
categories:
- bim
- elearning
date: 2013-05-10 16:05:53+10:00
next:
  text: '"Moodle, BIM, reflective journals and TPACK: Suggestions for moving beyond"'
  url: /blog2/2013/05/12/moodle-bim-reflective-journals-and-tpack-suggestions-for-moving-beyond/
previous:
  text: Everything old is new again
  url: /blog2/2013/05/04/everything-old-is-new-again/
title: How can an "enterprise" e-learning tool be agile?
type: post
template: blog-post.html
---
I have a problem. If I'm really lucky, [BIM](/blog2/research/bam-blog-aggregation-management/) will get added to my institution's version of BIM for Semester 2 and I will be able to use it. Based on my experience this semester - where I've used an approach that depends on BIM - there has been limitations and workload issues. Having BIM installed in the "enterprise LMS" will help significantly reduce these problems. It will also severely limit my ability to learn.

That limitation will arise from the nature of being an "enterprise" LMS. i.e. not at all agile. Instead a lumbering behemoth that takes a while to turn around. Getting the "enterprise" installation of BIM changed in anyway will involve going through a governance process that will have numerous steps. During these steps the expense of changing BIM will have to compete for the scarce resources available to change the "enterprise" LMS with other requirements. Requirements that are likely to be significantly more important than the couple of hundred students in the 2 or 3 courses I teach.

This causes problems because while BIM has been used at other institutions. It's typically been supported just like most "enterprise" LMS. i.e. if there are any problems or limitations with the tool it is learners and teachers who are aware of it first. These folk will either ignore/workaround the problem (and blame the &^%%## technology) or they will ask for help. The people they ask for help will be either IT helpdesk folk or L&T staff development/training folk. If they are lucky these folk will actually know how to use the particular tool that has the problem without having to quickly read the manual. In the worse case scenario, they'll have to do a quick read of the manual/Google search (which theoretically the learner/teacher could have done in the first place). Either way the only options open to the support folk are

1. Here's where you went wrong and how you fix the problem.
2. You have just discovered one of the known problems with that tool, there's nothing we can do about it.

Either response often involves the learner/teacher engaging in a large laborious manual process to workaround the limitation of the tool.

### A different situation

When I'm using BIM, I'll be in a slightly different situation. I designed and wrote BIM. When there's a problem or limitation with BIM, I can generally change BIM to fix it. For example, earlier this week I discovered that one of the main pages wasn't displaying individual student posts in order of time published. Five minutes later it did.

The fact that BIM has been around for 3/4 years and this problem still existed in the code is a nice piece of evidence of the limitations of the "enterprise" approach, even if it is based on open source technology.

The trouble is, I was able to make and use this fix because I'm currently running BIM on my laptop. Next semester, when (or if) it is installed on the "enterprise" LMS it is very unlikely that a change like this would ever get installed on the "enterprise" LMS in any reasonable time frame. Perhaps ready for next semester, if I'm lucky.

This is a real problem because next semester I will have a real opportunity to do some really interesting experimentation and development with BIM. Activities that will be somewhat curtailed by the constraints of the enterprise process.

How can I work around this?

### Some possibilities

Two short-term possibilities are

1. The backup/restore shuffle.
    
    This is where the students interact with the enterprise version of BIM. I then back that data up and restore it on my laptop. This is where I have the agile version of BIM that I can play with. If I make any change to the data, I then have to shuffle the data back the other way. In reality, the round trip of taking data from the agile version to the enterprise version probably isn't going to work in any consistent and safe way.
    
    This approach also doesn't help enable some of the ideas where the changes to BIM will enable students to do new and interesting things with BIM. Perhaps a version of BIM installed on an outside server the students could interact with might work. But it raises all sorts of other issues.
    
2. The client-side scripting workaround.
    
    This is where I create browser/client based scripts that modify how BIM works. Each student/staff member would need to install the scripts on their browser to get the functionality.
    
    Perhaps I could make changes to the BIM code to make this sort of workaround more effective and simpler?
    

The other possibility is to explore how the enterprise approach could be changed to be more agile. At the very least this would involve building a better relationship with the institutional IT folk, but even then there are limitations.

Are there other possibilities?

### The grammar of enterprise IT

[The grammar of school](/blog2/2009/04/24/models-of-growth-responding-to-the-grammar-of-school/) is an idea to explain why reforms of education have failed to take root. Especially the use of ICTs. The rationale is that any proposed reform is so different from the accepted mindsets of schooling (the grammar) that it is seen as nonsensical, as ungrammatical. i.e. it gets rejected or ignored in much the same way a nonsensical sentence.

I suggest that there is also a "grammar of enterprise IT". Ideas such as

1. Wanting to make rapid, unplanned changes to a piece of software; or,
2. Trusting a member of the Education Faculty to make those changes.

would simply be seen as nonsensical and rejected. Changing that grammar is going take a lot longer.

Even in writing this post, I run the chance that someone in enterprise IT will see how this is an attempt to break the grammar of enterprise IT. A perception that could lead to additional constraints on the development and use of BIM. Shall be interesting to see how it develops.