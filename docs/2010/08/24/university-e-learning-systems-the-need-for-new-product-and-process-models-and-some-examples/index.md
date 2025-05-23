---
categories:
- chapter-5
- design-theory
- elearning
- highereducation
- phd
- psframework
- thesis
- webfuse
date: 2010-08-24 15:09:22+10:00
next:
  text: The end of management - lessons for universities?
  url: /blog/2010/08/24/the-end-of-management-lessons-for-universities/
previous:
  text: Oil sheiks, Lucifer and university learning and teaching
  url: /blog/2010/08/23/oil-sheiks-lucifer-and-university-learning-and-teaching/
title: '"University e-learning systems: the need for new product and process models
  and some examples"'
type: post
template: blog-post.html
---
I'm in the midst of the horrible task of trying to abstract what I think I know about implementing e-learning information systems within universities into the formal "language" required of an information systems design theory and a PhD thesis. This post is a welcome break from that, but is still connected in that it builds on what is perhaps fundamentally different between what most universities are currently doing, and what I think is a more effective approach. In particular, it highlights some more recent developments which are arguably a step towards what I'm thinking.

As it turns out, this post is also an attempt to crystalise some early thinking about what goes into the ISDT. So some of the following is a bit rough. Actually, writing this has identified one perspective that I hadn't thought of, which is potentially important.

### Edu 2.0

The post arises from having listened to [this interview](http://www.stevehargadon.com/2010/07/tonight-graham-glass-on-edu-20.html) with Graham Glass the guy behind [Edu 2.0](http://edu20.org/), which is essentially a cloud-based LMS. It's probably one of a growing number out there. What I found interesting was his description of the product and the process behind Edu 2.0.

In terms of product (i.e. the technology used to provide the e-learning services), the suggestion was that because Edu 2.0 is based in the cloud - in this case Amazon's S3 service - it could be updated much more quickly than more traditional institutionally hosted LMSs. There some connection here with Google's approach to on-going modifications to live software.

Coupled with this product flexibility was a process (i.e. the process through which users were supported and the system evolved) that very much focused on the Edu 2.0 developers interacting with the users of the product. For example, releasing proposals and screenshots of new features within discussion forums populated with users and getting feedback; and also responding quickly to requests for fixes or extensions from users. To such an extent that Glass reports users of Edu 2.0 feeling like it is "there EDU 2.0" because it responds so quickly to them and their needs.

### The traditional Uni/LMS approach is broken

In the thesis I argue that when you look at how universities are currently implementing e-learning information systems (i.e. selecting and implementing an LMS) the product (the enterprise LMS, the one ring to rule them all) and the process they use are not a very good match at all for the requirements of effectively supporting learning and teaching. In a nut shell, the product and the process is aimed at reducing diversity and the ability to learn, while diversity is a key characteristic of learning and teaching at a university. Not to mention that when it comes to e-learning within universities, it's still very early days and it is essential that any systemic approach to e-learning have the ability to learn from its implementation and make changes.

I attempted to expand on this argument in [the presentation](/blog/2009/10/05/lectures-and-the-lms-alternatives-and-experiments/) I gave at the EDUCAUSE'2009 conference in Denver last year.

### What is needed

The alternative I'm trying to propose within the formal language of the ISDT is that e-learning within universities should seek to use a product (i.e. a specific collection of technologies) that is incredible flexible. The product must, as much as possible, enable rapid, on-going, and sometimes quite significant changes.

To harness this flexibility, the support and development process for e-learning should, rather than be focused on top-down, quality assurance type processes, be focused on closely observing what is being done with the system and using those lessons to modify the product to better suit the diversity of local needs. In particular, the process needs to be adopter focused, which is described by Surry and Farquhar (1997) as seeing the individual choosing to adopt the innovation as the primary force for change.

To some extent, this ability to respond to the local social context can be hard with a software product that has to be used in multiple different contexts. e.g. an LMS used in different institutions.

### Slow evolution but not there yet

All university e-learning implementation is not the same. There has been a gentle evolution away from less flexible products to more flexible produces, e.g.

1. Commercial LMS, hosted on institutional servers.  
    Incredibly inflexible. You have to wait for the commercial vendor to see the cost/benefit argument to implement a change in the code base, and then you have to wait until your local IT department can schedule the upgrade to the product.
2. Open source LMS, hosted on institutional servers.  
    Less inflexible. You still have to wait for a developer to see your change as an interesting itch to scratch. This can be quite quick, but it can also be slow. It can be especially quick if your institution has good developers, but good developers cost big money. Even if the developer scratches your itch, the change has to be accepted into the open source code base, which can take some time if its a major change. Then, finally, after the code base is changed, you have to wait for your local IT shop to schedule the upgrade.
3. Open source LMS, with hosting outsourced.  
    This can be a bit quicker than the institutional hosted version. Mainly because the hosting company may well have some decent developers and significant knowledge of upgrading the LMS. However, it's still going to cost a bit, and it's not going to be real quick.

The cloud-based approach used by EDU 2.0 does offer a product that is potentially more flexible than existing LMS models. However, apart from the general slowness in the updating, if the change is very specific to an individual institution, it is going to cause some significant problems, regardless of the product model.

### Some alternative product models

The EDU 2.0 model doesn't help the customisation problem. In fact, it probably makes it a bit worse as the same code base is being used by hundreds of institutions from across the globe. The model being adopted by Moodle (and probably others), having plugins you can add, is a step in the right direction in that institutions can choose to have different plugins installed. However, this model typically assumes that all the plugins have to use the same API, language, or framework. If they don't, they can't be installed on the local server and integrated into the LMS.

This requirements is necessary because there is an assumption for many (but not all) plugins that they provide the entire functionality and must be run on the local server. So there is a need for a tighter coupling between the plugin and the LMS and consequently less local flexibility.

A plugin like [BIM](/blog/research/bam-blog-aggregation-management/) is a little different. There is a wrapper that is tightly integrated into Moodle to provide some features. However, the majority of the functionality is provided by software (in this case blogging engines) that are chosen by the individual students. Here the flexibility is provided by the loose coupling between blog engine and Moodle.

Mm, still need some more work on this.

### References

Surry, D., & Farquhar, J. (1997). Diffusion Theory and Instructional Technology. e-Journal of Instructional Science and Technology, 2(1), 269-278.