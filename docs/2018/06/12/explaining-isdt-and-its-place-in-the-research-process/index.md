---
categories:
- design-theory
date: 2018-06-12 12:08:56+10:00
next:
  text: Contextual ramblings on learning analytics
  url: /blog/2018/11/30/contextual-ramblings-on-learning-analytics/
previous:
  text: Random meandering notes on "digital" and the fourth industrial revolution
  url: /blog/2018/05/26/random-meandering-notes-on-digital-and-the-fourth-industrial-revolution/
title: Explaining ISDT and its place in the research process
type: post
template: blog-post.html
---
The following is an initial, under-construction attempt to explain (first to myself) how/what role an Information Systems Design Theory (ISDT) places in the research process. Working my way toward a decent explanation for PhD students.

It does this by linking the components of an ISDT with one explanation of a research project. Hopefully connecting the more known concept (research project) with the less known (ISDT). It also uses as an example the ISDT for emergent university e-learning that was developed as part of [my PhD thesis](http://djon.es/blog/research/phd-thesis/).

## Anatomy of an ISDT?

The following uses Gregor and Jones (2007) specification of a design theory as summarised in the following table adapted from (Gregor & Jones, 2007, p. 322). Reading the expanded descriptions of each of the components of an ISDT in Gregor and Jones (2007) will likely be a useful companion to the following.

 
| Component | Description |
| --- | --- |
| **Core components** |  |
| Purpose and scope (the causa finalis) | “What the system is for,” the set of meta-requirements or goals that specifies the type of artifact to which the theory applies and in conjunction also defines the scope, or boundaries, of the theory. |
| Constructs (the causa materialis) | Representations of the entities of interest in the theory. |
| Principle of form and function (the causa formalis) | The abstract “blueprint” or architecture that describes an IS artifact, either product or method/intervention. |
| Artifact mutability | The changes in state of the artifact anticipated in the theory, that is, what degree of artifact change is encompassed by the theory. |
| Testable propositions | Truth statements about the design theory. |
| Justificatory knowledge | The underlying knowledge or theory from the natural or social or design sciences that gives a basis and explanation for the design (kernel theories). |
| **Additional components** |  |
| Principles of implementation (the causa efficiens) | A description of processes for implementing the theory (either product or method) in specific contexts. |
| Expository instantiation | A physical implementation of the artifact that can assist in representing the theory both as an expository device and for purposes of testing. |

## Problem and question

This explanation assumes that all research starts with a problem and a question. It's important (as for all research) that the problem/question be interesting and important. The [book "Craft of research"](https://rampages.us/univ200watson/wp-content/uploads/sites/7575/2015/06/The-Craft-of-Research-From-Topics-to-Questions-by-Wayne-C.-Booth.pdf) talks about identifying your research question.

[![Problem](images/27875032127_7841632fc2.jpg)](https://www.flickr.com/photos/david_jones/27875032127/in/dateposted-public/ "Problem")
<script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

An ISDT is generated through design-based research (DBR), which for me at least that it tends to deal with "how" research questions. For example, the research question from my thesis

> How to design, implement and support an information system that effectively and efficiently supports e-learning within an institution of higher education?

The challenge here is to develop some knowledge that helps answer this type of question. Baker (2014) talks a bit more about research questions in DBR.

Hopefully the question driving my thesis research is clear from the above. The thesis includes additional background to establish that the related problem (developing IS for e-learning in higher ed) is an important one worthy of research)

## You want to help someone/many people do something?

DBR aims to help someone do something. The aim of an ISDT is to provide guidance to someone to build an information system that solves an identified problem. But you're not interested in the technology?

Avison and Eliot (2006) suggests that in comparison to other IT-related disciplines (e.g. computer science, computer science engineering) the information systems discipline is focused more on the focuses on the application of technology and the subsequent interactions between people/organisations (soft issues) and the technology. It's not just focused on the technologies. They include the following quote from Lee's (2001) editorial in MISQ

> that research in the information systems field examines more than just the technological system, or just the social system, or even the two side by side; in addition, it investigates the phenomena that emerge when the two interact...the emergent soci-technical phenomena

By answering the research question, you're hoping that people can develop an information system.

[![Problem & solution (IS)](images/27875031697_044712488c.jpg)](https://www.flickr.com/photos/david_jones/27875031697/in/dateposted-public/ "Problem & solution (IS)")
<script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

## But you're not a consultant

The problem with the last image is that it's a bit like what a consultant does. Someone has a problem, you come in and create something that solves their problem. DBR is not consultancy. It aims to develop generalised knowledge that can inform the development multiple different information systems. Different people in different contexts should be able to develop information systems appropriate to their requirements.

[![Problem & multiple solutions](images/42694848052_4a26e3e878.jpg)](https://www.flickr.com/photos/david_jones/42694848052/in/dateposted-public/ "Problem & multiple solutions")
<script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

## How do they know how to do that?

What's missing in the last diagram is the knowledge that people will use to develop any information system. This knowledge is the answer to the research question/problem that you aim to develop. This is where the ISDT enters the picture. It is a representation of that knowledge that people use to develop an appropriate information system.

[![Problem and how](images/27875031367_1433eedf9b.jpg)](https://www.flickr.com/photos/david_jones/27875031367/in/dateposted-public/ "Problem and how")
<script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

The ISDT encapsulates knowledge about how to build a particular type of information system that effectively answers the research question/problem. i.e. it encapsulates knowledge that serves a particular purpose and scope

But an ISDT is not just a black/grey box. It has components as outlined in the table above.

## Purpose and scope

Johanson and Hasselbring (2018) argue that one of the problems with computer scientists and software engineers is that they wished to focus on general principles at the cost of specific principles. Hence such folk develop artifacts like [the software development life cycle](https://en.wikipedia.org/wiki/Systems_development_life_cycle) (and lots more) that are deemed to be general ways to develop information systems. See Vessey (1997) for more on this, including the lovely quote from Plauger (1993)

> If you believe that one size fits all, you are living in a panty-hose commercial

Assuming that your research question/problem is not terribly generic, it should be possible for you to identify the _purpose and scope_ for your ISDT. For example, here's the summary of the purpose and scope from my ISDT for emergent university e-learning

> 1. Provide ICT functionality to support learning and teaching within a university environment (e-learning).
> 2. Seek to provide context specific functionality that is more likely to be adopted and integrated into everyday practice for staff and students.
> 3. Encourage and enable learning about how e-learning is used. Support and subsequently evolve the system based on that learning.

Your research started with a problem (turned into a question). That problem should have defined something important for someone. Something important that your ISDT is going to provide the knowledge they need to solve by building an information system. i.e. something that is not just hardware and software, but considers those elements, the associated soft issues and the interactions between them.

Your ISDT - in the form of _purpose and scope_ - overlaps/connects with your research question/problem

[![Problem and purpose](images/27875031267_75ef271471.jpg)](https://www.flickr.com/photos/david_jones/27875031267/in/dateposted-public/ "Problem and purpose")
<script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

But as illustrated by the example research question and _purpose and scope_ used here they are different. My original research question is fairly generic. The purpose and scope has a fair bit more detail. Where did that detail come from?

## Justificatory knowledge informs purpose and scope

An ISDT should include justificatory knowledge. Knowledge and theory from the natural, social or design sciences that inform how you understand and respond to the research problem. The example purpose and scope in the previous section includes explicit mention of 'context specific functionality' and 'integrated into everyday practice' (amongst others). Each of these narrow the specific purpose and scope. This ISDT is not just about developing a system that will support L&T in a tertiary setting. It's also quite explicit that the system should also encourage adoption and evolution.

This particular narrowing is informed by a variety of theoretical insights that form part of the justificatory knowledge of my ISDT. Theoretical insights drawn from end-user development and distributed cognition. One of the reasons why my ISDT is for _emergent_ university e-learning.

This gives some insight into how a different ISDT for university e-learning could take a different approach (informed by different justificatory knowledge). e.g. I'd argue that current approaches to university e-learning tacitly have the purpose (perhaps priority) of being efficient and achieving institutional goals, rather than encouraging adoption, contextual functionality, and emergence.

Design research aims to make use of existing knowledge and theory to construct artefacts that improve some situation (Simon, 1996). How you understand the "some situation" should be informed by your justificatory knowledge.

[![Justificatory knowledge](images/42694847322_948566dca1.jpg)](https://www.flickr.com/photos/david_jones/42694847322/in/dateposted-public/ "Justificatory knowledge")
<script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

## But what do they do?

You want your ISDT to help people design effective/appopriate information systems. But how do people know what to do to develop a good information system? Where's that knowledge in the ISDT to help them do this?

This is where the design principles enter the picture. There are two sets of design principles:

1. principles of form and function; and
    
    i.e. what are you going to build? What features does it have?
    
2. principles of implementation.
    
    i.e. how should you build it? What steps should you follow to efficiently and effectively put the IS in place?
    

These principles should be abstract enough that they can inform the design of different information systems. They should also be directly connected to your ISDT's justificatory knowledge. You don't just pull them out of the air, or because that's they way you do it. [![Principles](images/40933373880_d19b63ff32.jpg)](https://www.flickr.com/photos/david_jones/40933373880/in/dateposted-public/ "Principles")
<script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

For the emergent university e-learning ISDT there were 13 principles of form and function organised into three groups with explicitly links to justificatory knowledge

1. Comprehensive, integrated and independent services - software wrappers
2. Adaptive and inclusive system architecture - system of systems; best of breed; service orientated architectures; end-user development; micro-kernel architecture
3. Scaffolding, context-sensitive conglomerations - constructive templates; end-user development; distributed cognition.

And there were 11 principles of implementation organised into another 3 groups, again, each explicitly linked to justificatory knowledge

1. Multi-skilled, integrated development and support team - job rotation; multi-skilling; organisational learning; situated learing/action; communities of practice; knowlege-based theory of organisational capability
2. An adopter-focused, emergent development process - emergent/ateleological development;
3. A supportive organisational context - organisational fit; strategic alignment; bricolage; mindfull innovation

## What can they expect to happen?

The premise of an ISDT is that if someone is able to successful follow the design principles then they should be able to expect that they will develop an IS that solves the particular problem in a way that is better in some way than other systems.

If people follow these principles, based on your justificatory knowledge you are claiming that certain things will happen. These are the testable propositions

[![propositions](images/42694846832_7ddc889a9d.jpg)](https://www.flickr.com/photos/david_jones/42694846832/in/dateposted-public/ "propositions")
<script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

The ISDT for emergent university e-learning has five testable propositions

1. Be able to provide the functionality and services necessary to support university e-learning.
2. Over time provide a set of functionality that is specific to the institutional context.
3. Over time show increasing levels and quality of adoption by staff and students.
4. Better enable and encourage the university, its e-learning information systems, and its staff and students to observe and respond to new learning about and insight into the design, support and use of university e-learning.
5. Through the combination of the above, provide a level of differentiation and competitive advantage to the host institution.

Each of these are based in some way on justificatory knowledge as instantiated by the design principles.

The first testable proposition is essentially that the resulting IS will be fit for purpose/address the necessary requirements. The remaining propositions identify how the resulting IS will be better than others. Propositions that can be tested once such an IS is instantiated.

## How do you/they know it works/

Just because you can develop a theory, doesn't mean it will work. However, if you have a working version of an information system designed using the ISDT (i.e. an instantiation of the ISDT) then it becomes a bit easier to understand. An instantiation also helps identify issues with the ISDT which can be refined (more on this below). An instantiation can also help explain the ISDT.

[![Constructs](images/27875030497_f298d0abe0.jpg)](https://www.flickr.com/photos/david_jones/27875030497/in/dateposted-public/ "Constructs")
<script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

In the above the arrows between instantiation, the design principles, and the testable propositions are intended to indicate how the instantiation should be informed/predicted by the principles and propositions, but also how the experience of building and using the instantiation can influence the principles (more of this below) and propositions.

In spite of the argument above, not everyone assumes that an instantiation is necessary (it's listed as an additional components in the ISDT specification). As the previous paragraphs suggest I think an instantiation is a necessary component.

The emergent university e-learning ISDT was based on a system called Webfuse used at a particular University from 1996 through 2010 (or so).

## Important concepts

The research problem (and scope) and the justificatory knowledge all embody a particular perspective on the world. Rather than trying to understand everything about and every perspective on the research problem (beyond the scope of mere mortals) an ISDT focuses attention on a particular view of the research problem. There are certain elements that are deemed to be more important and more interesting to a particular ISDT than others. These more interesting elements become the _constructs_ of the ISDT. They define the meaning of these interesting elements. They become some of the fundamental building blocks of the ISDT.

The following image perhaps doesn't capture the importance of constructs. [![ISDT and research process](images/42027150704_a21eaa2740.jpg)](https://www.flickr.com/photos/david_jones/42027150704/in/dateposted-public/ "ISDT and research process")
<script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

The following table summarises the constructs from the ISDT for emergent university e-learning

 
| Construct | Definition |
| --- | --- |
| e-learning | The use of information and communications technologto support and enhance learning and teaching in higher education institutions (OECD, 2005c) |
| Service | An e-learning related function or application such as a discussion forum, chat room, online quiz etc. |
| Package | Mechanism through which all services are integrated into and managed within the system. |
| Conglomerations | Groupings of services that provide scaffolding and context-specific support for the performance of high-level e-learning tasks. (e.g., creating a course site with a specific design; using a discussion forum to host debate; using blogs to encourage reflection) |

## What happens next?

Lee's (2001) quote above mentioned "emergent soci-technical phenomena". The idea that when technology meets society something different emerges and keeps on emerging. Not just because of the combination of these two complex categories of interest, but also because digital technology itself is protean/mutable. While digital technologies show rapid change due to the evolution of the technology, digital technologies are also inherently protean. They can be programmed.

The importance of this feature means that _artifact mutability_ - how you expect IS built following your ISDT will/should/could change - is a core component of an ISDT.

[![Mutability](images/28870737798_61c2a776d0.jpg)](https://www.flickr.com/photos/david_jones/28870737798/in/dateposted-public/ "Mutability")
<script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

As an ISDT for _emergent_ e-learning artifact mutability/what happens next was a key consideration described as

> As an ISDT for emergent e-learning systems the ability to learn and evolve in response to system use is a key part of the purpose of this ISDT. It is actively supported by the principles of form and function, as well as the principles of implementation.

i.e. mutability was a first order consideration in this ISDT. It actively tried to encourage and enable this in a positive way through both sets of principles.

## How do you do it? (Research approach)

The above has tried to explain the components of an ISDT by starting with a typical research question/problem. It doesn't address the difficult question of how "how do you formulate an ISDT?". In particular, how do you do it with some rigor, practical relevance etc. Answering these questions are somewhat independent from the components of an ISDT. Whatever research approach you use should produce appropriately the various components, but how you develop it is separate from the ISDT.

My thesis work followed the iterative action research process from Markus et al (2002)

[![Iterative action research for formulating ISDT](images/27836290847_c022d9b510_z.jpg)](https://www.flickr.com/photos/david_jones/27836290847/in/dateposted-public/ "Iterative action research for formulating ISDT")
<script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

A related but more common research process within design-based research out of the education discipline is Reeves (2006) approach. I'll expand upon this one, but there are overlaps.

[![DBR cycle](images/15250772546_ba90f6ff90_z.jpg)](https://www.flickr.com/photos/david_jones/15250772546/in/photolist-peEcmf-bE8C7L "DBR cycle")
<script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

As Reeve's image sugestions, these aren't four distinct, sequential phases. Instead, they can tend toward almost to concurrent tasks that you are stepping back and forth between. As you engage in iterative cycles of testing and refinement (3rd phase) you learn something that modifies understanding of the practical problem (1st) and perhaps principles (2nd) and perhaps highlights something to reflect.

However, at least initially, I'm wondering if you should have spent some time developing an initial version of your ISDT (and all its components) fairly early on in the research cycle. This forms the foundation/mechanism by which you move backward and forward between the different stages.

i.e. as you develop a specific solution (instantiation) of your ISDT you might find yourself having to undertake a particular step or develop a particular feature that isn't explained by your existing design principles.

[![Approach](images/27875029947_7967f67f58.jpg)](https://www.flickr.com/photos/david_jones/27875029947/in/dateposted-public/ "Approach")
<script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

Similarly, you might be observing an instantiation in action by gathering/analysing data etc (Phase 3) or perhaps you might be reflecting upon what's happened and realise that a particular issue isn't covered, or that your initial assumptions were wrong. Leading to more refinement.

That refinement may in turn lead to changes in the instantiation(s) and thus more opportunities to learn and refine.

## References

Avison, D., & Eliot, S. (2006). Scoping the discipline of information systems. In J. L. King & K. Lyytinen (Eds.), Information systems: the state of the field (pp. 3–18). Chichester, UK: John Wiley & Sons.

Bakker, A. (2014). Research Questions in Design-Based Research (pp. 1–6). Retrieved from [http://www.fi.uu.nl/en/summerschool/docs2014/design\_research\_michiel/Research Questions in DesignBasedResearch2014-08-26.pdf](http://www.fi.uu.nl/en/summerschool/docs2014/design_research_michiel/Research Questions in DesignBasedResearch2014-08-26.pdf)

Gregor, S., & Jones, D. (2007). The anatomy of a design theory. Journal of the Association for Information Systems, 8(5), 312–335.

Johanson, A., & Hasselbrin<, W. (2018). Software Engineering for Computational Science: Past, Present, Future. Computing in Science & Engineering. https://doi.org/10.1109/MCSE.2018.108162940

Markus, M. L., Majchrzak, A., & Gasser, L. (2002). A design theory for systems that support emergent knowledge processes. MIS Quarterly, 26(3), 179–212.

Reeves, T. (2006). Design research from a technology perspective. In J. van den Akker, K. Gravemeijer, S. McKenney, & N. Nieveen (Eds.), Educational Design Research (pp. 52–66). Milton Park, UK: Routledge.

Simon, H. (1996). The sciences of the artificial (3rd ed.). MIT Press.

Vessey, I. (1997). Problems Versus Solutions: The Role of the Application Domain in Software. In Papers Presented at the Seventh Workshop on Empirical Studies of Programmers (pp. 233–240). New York, NY, USA: ACM. https://doi.org/10.1145/266399.266419