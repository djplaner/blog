---
categories:
- chapter-5
- design-theory
- information-systems
- thesis
date: 2010-09-13 14:35:04+10:00
next:
  text: Portfolios often implemented poorly
  url: /blog/2010/09/14/portfolios-often-implemented-poorly/
previous:
  text: Back into the thesis
  url: /blog/2010/09/13/back-into-the-thesis/
title: How strict a blueprint do ISDTs provide?
type: post
template: blog-post.html
---
Am working on the final ISDT for the thesis. An Information Systems Design Theory (ISDT) is a theory for design and action. It is meant to aim to provide general principles that help practitioners design information systems. Design theory provides guidance about how to build an artifact (process) and what the artifact should look like when built (product/design principles) (Walls, Widmeyer et al. 1992; Gregor 2002). Walls et al (1992) see an ISDT as an integrated set of prescriptions consisting of a particular class of user requirements (meta-requirements), a type of system solution with distinctive features (meta-design) and a set of effective development practices (meta-design). Each of these components of an ISDT can be informed by kernel theories, either academic or practitioner theory-in-use (Sarker and Lee 2002), that enable the formulation of empirically testable predictions relating the design theory to outcomes (Markus, Majchrzak et al. 2002).

#### My question

I've just about happy with the "ISDT for emergent university e-learning systems" that I've developed. A key feature of the ISDT is the "emergent" bit. This implies that the specific context within which the ISDT might be applied is going to heavily influence the final system. To some extent there is a chance that aspects of the ISDT should be ignored based on the nature of the specific context. Which brings me to my questions:

1. How far can the ISDT go in saying, "ignore principle X" if it doesn't make sense?
2. How much of the ISDT has to be followed for the resulting system to be informed by the ISDT?
3. If most of the ISDT is optional based on contextual factors, how much use is the ISDT?
4. How much and what sort of specific guidance does an ISDT have to give to be useful and/or worthwhile?

#### Class of systems

One potential line of response to this is based on the "class of systems" idea. The original definition provided by Walls et al (1992) for the meta-design component indicates that it "Describes a class of artefacts hypothesized to meet the meta-requirements" and not a specific instantiation. van Aken (2004) suggests that rather than a specific prescription for a specific situation (an instantiation), the intent should be for a general prescription for a class of problems. van Aken (2004) arrives at this idea through the use of Bunge's idea of a technological rule.

van Aken (2004) goes onto explain the role of the practitioner in the use of a technological rule/ISDT

> Choosing the right solution concept and using it as a design exemplar to design a specific variant of it presumes considerable competence on the part of practitioners. They need a thorough understanding both of the rule and of the particulars of the specific case and they need the skills to translate the general into the specific. Much of the training of students in the design sciences is devoted to learning technological rules and to developing skills in their application. In medicine and engineering, technological rules are not developed for laymen, but for competent professionals.

This seems to offer some support for the idea that this problem, is not really a problem.

#### Emergent

It appears that the idea of "emergent" is then just an increase in emphasis on context than is generally the case in practice. There is, I believe, a significant difference between emergent/agile development and traditional approaches, it's probably worthwhile making the distinction in a mild way when introducing the ISDT and then reinforcing this in the artifact mutability and principles of implementation section.

#### The first stab

The following paragraph is a first draft of the last paragraph in the introduction to the ISDT. It starts alright, but I'm not sure I've really captured (or understand) what I'm trying to get at with this. Is it just an attempt to signpost perspectives included below? Need to be able to make this clearer I think.

It is widely accepted that an ISDT - or the related concept of technological rule – are not meant to describe a specific instantiation, but instead to provide a general prescription for a class of problems (Walls, Widmeyer et al. 1992; van Aken 2004). The ISDT presented here is intended to offer a prescription for e-learning information systems for universities. In addition to this general class of problems, the ISDT presented here also includes in its prescription specific advice – provided in the principles of implementation, and artifact mutability components of the ISDT – to be more somewhat more general again. This is captured in the use of the word "emergent" in the title of the ISDT and intended in the sense adopted by Truex et al (1999) where "organisational features are products of constant social negotiation and consensus building….never arriving but always in transition". This suggests the possibility that aspects of this ISDT may also be subject to negotiation within specific social contexts and subsequently not always seen as relevant.

#### References

Gregor, S. (2002). Design Theory in Information Systems. Australian Journal of Information Systems, 14-22.

Markus, M. L., Majchrzak, A., & Gasser, L. (2002). A Design Theory for Systems that Support Emergent Knowledge Processes. MIS Quarterly, 26(3), 179-212.

van Aken, J. (2004). Management research based on the paradigm of the design sciences: The quest for field-tested and grounded technological rules. Journal of Management Studies, 41(2), 219-246.

Walls, J., Widmeyer, G., & El Sawy, O. A. (1992). Building an Information System Design Theory for Vigilant EIS. Information Systems Research, 3(1), 36-58.