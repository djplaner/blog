---
title: A Theory-Driven Design Framework for Social Recommender Systems
date: 2010-12-20 17:22:33+10:00
categories: ['thesis']
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: VRBones
      author_email: vrbones@hotmail.com
      author_ip: 118.208.180.4
      author_url: http://www.vrbones.com
      content: 'It seems that there is still a disconnect between SRS and personal recommendations
        in that personal recommendations come as part of a conversation, not left hanging
        out there as a general recommendation.
    
    
        I was mulling over this with steam''s <a href="http://www.gamasutra.com/view/news/31649/Valve_Launches_Game_Recommendation_Feature_For_Steam.php"
        rel="nofollow">attempt</a> at bringing in personal recommendations. I regularly
        discuss the games I''m playing with virtually anyone that will listen, but I don''t
        feel comfortable writing up a recommendation for public (or even friendly) consumption.
        I need to know where the person is up to in their game playing career and mould
        my story to adapt.
    
    
        It''s a conversation about the recommendation that''s important, not the one-way
        shovel SRS''s give you.
    
    
        Maybe they just need to implement a ''phone a friend'' button where it automatically
        sends out a request to your social network indicating that you want to buy/use
        a certain product and then gathers thumbs up/down responses? Still seems too slow
        compared to automated recommendations, and only a little step away from crowdsourcing
        anyway.
    
    
        I''d be interested in the results of stuff like this as an automated course recommender
        would be on the cards when courses get down to the 1-2 hour marks. There are others
        in the e-learning analytics group that are approaching it from the SRS angle.'
      date: '2010-12-23 08:10:16'
      date_gmt: '2010-12-22 22:10:16'
      id: '3215'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: davidtjones
      author_email: davidthomjones@gmail.com
      author_ip: 123.211.226.49
      author_url: https://djon.es/blog/
      content: 'Tony, your comment about the conversation captures and aspect of my reservations
        about SRS, analytics and other sorts of automated, compsci quantitative approaches.  i.e.
        I''m not sure how well the capture the reality of people and how they act, think,
        relate etc.
    
    
        I''m not convinced that all the mathematics and compsci can address this problem
        and I''m pretty sure that most of the math/compsci folk tend to focus more on
        the math than the people side. The people side gets too messy.
    
    
        I''m interested in how aspects of SRS, analytics and related stuff can be married
        with the behaviour change insights to produce systems the encourage and enable
        better learning and teaching.  Not in replacing people or automating tasks.
    
    
        I''m seriously considering participating in the analytics MOOC to see if I can
        test these nascent thoughts a bit.'
      date: '2010-12-23 16:30:40'
      date_gmt: '2010-12-23 06:30:40'
      id: '3216'
      parent: '0'
      type: comment
      user_id: '1'
    
pingbacks:
    []
    
---

See also: [[blog-home | Home]]

I'm becoming increasingly interested in how the design of e-learning systems can be improved through insights from behaviour change literature and related work (e.g. I think game design principles have some connections with behaviour change. A while ago I started some thinking about this. The following is a summary of/reflection on

> Ofer Arazy, Nanda Kumar, Bracha Shapira (2010), [A theory-driven design framework for recommender systems, Journal of the Assocation for Information Systems](http://aisel.aisnet.org/jais/vol11/iss9/2/), 11(9):455-490

This might sound a bit too specific, however, the following from the abstract has me interested

> We enhance Walls et al.'s (1992) IS Design Theory by introducing the notion of "applied behavioral theory" as a means of better linking theory and system design. Our second objective is to apply our theory-driven design methodology to social recommender systems, with the aim of improving prediction accuracy. A behavioral study found that some social relationships (e.g., competence, benevolence) are most likely to affect a recipient's advice-taking decision.

Aspects of recommender systems resonate with the task facing e-learning systems, especially some of the work around academic analytics. i.e. an attempt to recommend approaches/information that can help teachers and students.

The following starts with a overview of what I took from the paper. This is followed by a summary of the major sections of the paper.

In the end, not quite as interesting as I hoped. But still sufficient to spark some thinking.

### Overview

Two main aims

1. Show how design research can be improved through filling the gap between kernel theories in an ISDT and the subsequent design principles with an applied behavioural model.  
    i.e. a traditional behavioural model/theory that tries to better approximate the design need/problem.
2. Illustrate how social recommender systems (with specific example within movie recommendations) can be improved using this type of approach.

They suggest that this is just one approach to bridging this gap. I tend to agree that this is an area of some complexity. But I also think this complexity is the source of value of design research. It is the interesting solutions within this problem area that arise from creativity that create research value. I would hope that there would be many different approaches, some of which can't be captured in a sequence of steps.

Another way of looking at this is that they are simply suggesting the more formal development of an improved kernel theory that will be used to inform system design. Not sure it is necessary that this be yet another component of an ISDT.

There is an interesting point here about how the design principles/ISDT can in turn influence the kernel theories, or at least the interpretation of these into the "gap filler".

There are some interesting insights from the advice-taking literature that could be useful in e-learning system design. For example

> Work dating to Pelz and Andrews (1966), Mintzberg (1973), and Allen (1977) indicates that people prefer to turn to other people, rather than to documents, when seeking information. Recommendations often are received through word-of-mouth, and such communication tends to flow through interpersonal channels based on shared interests and friendship (Arndt, 1967), both offline and online (Cross and Sproull, 2004).

So, an e-learning system that attempted to connect people (teachers and students) to other people, rather than help documents, might offer some interesting outcomes.

### Introduction

Introduces what recommender systems are.."reducing information overload by providing users with relevant information and a key component of successful online stores". References literature, talks about two approaches to recommender design and the three sequential steps: identify sources for user; analysis of user's profile; generation of recomendations

SRS == Social Recommender Systems. Introduce classification of SRS. Research on SRS using relationship information in early phases with inconclusive results, modest accuracy improvement in limited sets of cases. _Limitation_ suggested that under-specification of the nature of social relations, ad-hoc design and limited use of behavioural theory is the cause.

Two primary objectives

- Develop an applied theoretical model;  
    i.e. this is used to link kernel theories in ISDT and the design principles. The model is a behavioural framework.
- Improve the design of social recommender systems.

### Design problem: sources in SRS

Collaborative filtering systems associate sources based on similar consumption profiles. Presents mathematical formula.

Social-network-enhanced RS have arisen from people prefering what their friends like and the availability of open social networks. Another mathematical formula. References literature showing limited improvements from this approach.

Argues this is because the discussion of social relationships in SRS has lacked theoretical grounding.

### Grounding systems design in behavioural theory

This is where they attempt to argue the need for an extra component in ISDTs to link kernel theories and principles of design. Interestingly they don't like the use of theory for these principles.

Use Venable (2006) and Kuechler et al (2007) as evidence that the explication of the theoretical basis for make design effective is often not there. _I wonder about how strong the evidence for this is, where it comes and how well the following recommendations address that problem._

_In particular, am interested in the suggestion that Gregor and Jones (2007) don't necessarily see the case for grounding design in behavioural theory. It's my recollection that we argued that it is possible for design principles to work without knowing why (e.g. science of aeronautics arising after people were flying), but that have theory to ground principles in is still a good/preferable thing to have. After all, justifactory knowledge is included as one of the core components of an ISDTAnd I quote

> The sixth component of justificatory knowledge needs to be added, to provide an explanation of why the design works.

._

It was also argued that both IT and human behavioural knowledge is required

> To further define terms as they are used in this paper, an IS design theory shows the principles inherent in the design of an IS artifact that accomplishes some end, based on knowledge of both IT and human behaviour.

The point about the connection between kernel theories and design principles not always being explained well, is a valid one. One that has been made elsewhere.

Authors argue that engineering has solved this problem and uses the example of wing design being based on aerodynamics. This only happened after some time. Also uses HCI as an example of a field being driven by kernel theories.

Now propose four challenges in briding the gap between kernel behavioural theories and system design

1. Difficulty in finding relevant kernel theories for a specific design problem;  
    Drawing on Walls et al (2004) they suggest that one of the problems here is the disconnect between behavioural and design researchers.
2. Kernel theory scope is too narrow, with no single theory accounting for all constructs relevant to a design problem.
3. Granularity of constructs in kernel theories don't math requirements of design problem.
4. Kernel theories specify the direction of effects, where design requires consideration of the effects' magnitude

Talk about Card and Newell's work (1983 and 1985) that addresses these problems by developing applied pyschological theoretical models (called "engineering-style theory") rather than borrowing existing kernel theories. It's from there that they deisgn interfaces. Some criticism of the work, including Carroll and Kellog (1989) "It may be simplistic to imagine deductive relations from science to design, but it would be bizarre if there were no relation at all"

_This is perhaps part of my problems so far with this paper. Part of the reason I think there aren't clear guidelines for linking kernel theories and design is that creating these linkages is the major creative aspect of design research. While it may be possible to identify some common processes or steps this remains a creative exercise. Perhaps more in common with abductive logic than deductive or inductive?_

however, the authors think that the Card and Newell approach can provide some benefit to design research. And essentially argue that this applied behavioural model can be added in.

### Linking behavioural theory to systems design

Specify steps to be used with this extension to address the four challenges listed above. Done with the context of social recommender systems.

- determine whether the application of psychological or social theories is warranted in a particular design problem;  
    Suggests SRS is an obvious fit given the large stream of literature from social theory. Suggests the the collaboration in HCI and CSCW communities may serve as a model.
- survey the relevant theoretical domain to identify constructs that map well to the design goals;  
    
- specify an applied theoretical model that is based on kernel theories;  
    Identify factors that would be antecedents of the dependent variable in the applied theoretical model and important to achieving the design goal. A mapping between design factors and theory based constructs. Issue of scope becomes critical. The question of competing, complimentary, multiple kernel theories.

The applied theoretical model is developed using standard behaviourla methods. i.e. a set of links between explaining and outcome variables. _The following sounds strange to me_ This model can be useful for udnerstnding the complex relationship between constructs, but may be too complicated for guiding design decisions. ???? In this example, they had to move from a multi-stage path model to a simpler one-step regression model due to the difficulty of getting data for all the constructs within the context of a SRS.

### Kernel theoris of advice taking

This is the section where they review kernel theories from advice literature and derivce some key constructs for SRS.

Reference one of the authors earlier papers that identify the types of social data available online and suggest that these map onto several theoretical constructs: homophily, tie-strength, trustworthiness. Then from a synthesis of advice-taking literature they develop some central variables for an applied theoretical model to understand the recipients willingness to accept a source's advice: cognitive homophily, tie strength, and competence- and benevolence-based trustworthiness.

Some of the insights from this literature

- People prefer to ask people, rather than use documents.
- Strong ties between people impact willingness to accept a recommendation, important conduit of useful knowledge.
- Weak ties useful as sources of novel information, instrumental in the diffusion of ideas and receipt of work-related advice
- Tie strength is multi-dimensional: closeness/emotional intensity, time
- Trust and tie strength are different.
- Perceived trustworthiness is closely related, but different to trust.
- Trusting relationships lead to greater knowledge exchange.
- Trustworthiness is multi-dimensional: benevolence, integrity, competence.
- Homophily is different to tie strength
- homophily can impact advice taking through the mediating role of tie strength
- homophily has two dimensions: socio-demographic and cognitive
- Cognitive homophily is "presumed to shape our orientation to future behaviour
- Socio-demographic homophily is seen as an antecedent of cognitive homophily

### Applied theory of advice taking to guide SRS design

This is where they developed the model from the above that will guide their system design. It shows the path model, the evaluation and then a simplified linear regression model to directly inform system design.

This consists of a range of hypotheses, e.g.

> H 1a: Cognitively similar individuals will maintain relationships that are longer temporally  
> H 1b: Cognitively similar individuals will interact more frequently.

which are then brought together in the multi-path model.

Then describes a survey methodology to test the hypotheses. Applied to 116 undergraduate students. PLS data analysis. Result fairly good, with some not supported.

Then tested with Hopophily + one of the other relational constructs. Since design of a system would need to be simpler.

### Design principles for SRS

Use the model from the last section to develop a Walls et al ISDT for SRS

### Recommender system evaluation

A prototype implemented to test some aspects. Same set of students. Lots of stats. Result...

> Simulation results demonstrate that alternative types of social relationship data impact recommender system accuracy differently. While some relationships (namely competence and benevolence-based trustworthiness) enhance accuracy, other relationships (i.e., interaction duration and frequency) add noise and impede system performance.