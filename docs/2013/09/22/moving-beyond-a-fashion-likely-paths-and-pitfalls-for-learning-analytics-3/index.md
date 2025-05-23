---
categories:
- elearning
- indicators
- irac
- learninganalytics-elearning
date: 2013-09-22 11:50:35+10:00
next:
  text: Data mining with Weka - Class 2 - Evaluation
  url: /blog/2013/09/22/data-mining-with-weka-class-2-evaluation/
previous:
  text: Getting started with Weka
  url: /blog/2013/09/21/getting-started-with-weka/
title: '"Moving beyond a fashion: Likely paths and pitfalls for learning analytics"'
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Moving beyond a fashion &#8211; Blended Learning 2013 | The Indicators Project
      author_email: null
      author_ip: 66.135.48.201
      author_url: http://indicatorsproject.wordpress.com/2013/09/18/moving-beyond-a-fashion-blended-learning-2013/
      content: '[&#8230;] A blog post attempting to capture what was said in the presentation
        is now available. [&#8230;]'
      date: '2013-09-22 11:55:20'
      date_gmt: '2013-09-22 01:55:20'
      id: '857'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: 'Avoiding the learning analytics fad: Forgotten insights and example applications
        | The Indicators Project'
      author_email: null
      author_ip: 72.232.114.3
      author_url: http://indicatorsproject.wordpress.com/2013/09/23/avoiding-the-learning-analytics-fad-forgotten-insights-and-example-applications/
      content: '[&#8230;] is also a blog post that expands on this earlier [&#8230;]'
      date: '2013-09-26 13:18:52'
      date_gmt: '2013-09-26 03:18:52'
      id: '858'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: 'Learning analytics implementation: System types and assumptions | Col&#039;s
        Weblog'
      author_email: null
      author_ip: 76.74.255.5
      author_url: http://beerc.wordpress.com/2014/04/15/learning-analytics-implementation-system-types-and-assumptions/
      content: '[&#8230;] am currently working up a paper for ASCILITE2014 that is based
        on a couple of presentations and a workshop that David and I prepared last year.
        The paper is talking about the gathering hype [&#8230;]'
      date: '2014-04-15 10:49:37'
      date_gmt: '2014-04-15 00:49:37'
      id: '859'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: Using the PIRAC &#8211; Thinking about an &#8220;integrated dashboard&#8221;
        | The Weblog of (a) David Jones
      author_email: null
      author_ip: 192.0.83.195
      author_url: https://davidtjones.wordpress.com/2015/01/30/using-the-pirac-thinking-about-an-integrated-dashboard/
      content: '[&#8230;] view that has risen out of both experience and research. For
        example, the following is a slide from this invited presentation. There&#8217;s
        also a a paper (Beer, Jones, &amp; Tickner, 2014) that evolved from that [&#8230;]'
      date: '2015-01-30 15:49:16'
      date_gmt: '2015-01-30 05:49:16'
      id: '860'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The following is a "webified" version of an invited presentation at the [Blended Learning 2013 Summit](http://www.blended-learning.com.au/). This version is largely an experiment with this medium/approach to sharing the talk. The slides from the talk are shown below with a written version of what I might have hoped to have said during the talk.

Click on the images if you wish to see them larger. The slides from the talk and also from a 2 hour workshop [are also available](http://indicatorsproject.wordpress.com/2013/09/18/moving-beyond-a-fashion-blended-learning-2013/).

### Update - feedback on the presentation

The conference organisers have provided feedback on the presentation.

"Rating" out of a possible 5 as a speaker

|  | Excellent | Very good | Good | Fair | Poor | Responses | Average |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Content | 13 | 35 | 11 | 1 | 0 | 60 | 4 |
| Presentation | 12 | 37 | 12 | 2 | 0 | 63 | 3.94 |

And comments that were provided

- At last a few interesting and thought provoking ideas
- This session was very informative
- Best of the conference...grounded, intelligent, insightful

### The "presentation"

[![Slide01](images/9861633443_2d6f8d2b61_n.jpg)](http://www.flickr.com/photos/david_jones/9861633443/)

Being a talk about learning analytics at a conference on blended learning it appears appropriate to start with gathering some data. Attendees were asked to take out their smart phones and participate in a poll around the question "What percentage of your institution's online courses are good?". Where "good" was defined as "you wouldn't be embarrased when showing them to external folk".

Using Poll Everywhere the actual slide showed live updates of the poll with the final data being used in a later slide. You can see related information [in this image](http://www.flickr.com/photos/david_jones/9827347453/in/photostream/). In summary, the majority response was less than 20% of online courses were deemed good.

[![Slide02](images/9861633683_f1fb82b472_n.jpg)](http://www.flickr.com/photos/david_jones/9861633683/)

Welcome to the gold rush. That's certainly what learning analytics feels like at the moment. In fact, our argument is that it's almost certainly going to end up as yet another management fashion or fad with little significant impact on the quality of learning and teaching in Universities. The aim of this talk is to examine some of the paths institutions might take with harnessing learning analytics, to identify some of the pitfalls associated with those paths and make an argument that one of these paths is under-represented and essentially if the aim is to avoid the fad dead end.

[![Slide03](images/9861633423_68658a38bd_n.jpg)](http://www.flickr.com/photos/david_jones/9861633423/)

Let's start with the obvious. Making decisions based on available data is obvious. There isn't anyone out there saying, "No I will not make decisions based on data", but then there are folk doing exactly this all of the time. In terms of e-learning a contributing factor is that most people aren't getting good data about what is going on, making it hard to base decisions on absent data. Making it more likely that decisions are based on prejudices and other biases.

[![Slide04](images/9861525764_28e937aab0_n.jpg)](http://www.flickr.com/photos/david_jones/9861525764/)

Which is where learning analytics enters the picture. It promises to offer access to data upon which to base decisions. It promises to help penetrate the complexity around learning and teaching within higher education. Which would obviously appear to be a good thing.

[![Slide05](images/9861548636_c0f723f9b2_n.jpg)](http://www.flickr.com/photos/david_jones/9861548636/)

The trouble is that like "blended learning", "e-learning" and any of a number of other "innovations" it appears that learning analytics is fast become a fad, a management fashion. The very obviousness of making decisions based on evidence or data and the absence of it from the practice of university e-learning has (along with a range of other factors such as commercial vendors, management consultants and researchers) create a normative pull around learning analytics. If you aren't doing something around learning analytics at the moment as a university you are almost seen as strange. You have to be doing it.

[![Slide06](images/9861525274_8db4dcbee1_n.jpg)](http://www.flickr.com/photos/david_jones/9861525274/)

This is leading learning analytics into become yet another fad. Many of you may well remember another recent information and information systems related fad to spread through higher education - Enterprise Resource Planning (ERP) systems. About 15 years ago Australian higher education underwent a similar normative pull to adopt ERP systems as they promised to reduce costs, enhance innovation, and provide the basis for data-based decision making for the organisation. Anyone who has lived through the last 15 years in Australian higher education knows how well that turned out for us.

Fad cycles in higher education isn't new. In terms of fad or hype cycles I much prefer Birnbaum's fad cycle (published about the same time as the rise of ERPs) to the more widely known Gartner hype cycle. I dislike the Gartner Hype cycle because it is - as you would expect from a management consultancy firm - inherently optimistic about fads. It assumes that all fads have a plateau of productivity. On the other hand Birnbaum's suggests that fads end with the "resolution of dissonance" - which is typically the blaming of the teaching staff for not buying into the vision - before the next big thing starts the cycle all over again.

[![Slide07](images/9861525374_470123121a_n.jpg)](http://www.flickr.com/photos/david_jones/9861525374/)

Enough preface, let's get to the guts of our argument.

[![Slide08](images/9861524744_0864230bc9_n.jpg)](http://www.flickr.com/photos/david_jones/9861524744/)

The argument is not that learning analytics is bad. As someone teaching a course with 300+ students I see learning analytics as providing a range of potential benefits to both myself and the folk taking my course.

[![Slide09](images/9861630953_3c89852c23_n.jpg)](http://www.flickr.com/photos/david_jones/9861630953/)

The argument is that almost without exception that the way universities will implement learning analytics will be bad. Bad in terms of not really improving the quality of learning and teaching within the institution. Instead it will suffer as yet another management fashion upon which (potentially) vast amounts of money and time are expended for little reward.

[![Slide10](images/9861627503_ac2b3d1967_n.jpg)](http://www.flickr.com/photos/david_jones/9861627503/)

The aim of our talk is to avoid the peaks and troughs of the management fashion and instead.

[![Slide11](images/9861520884_78b3b402e1_n.jpg)](http://www.flickr.com/photos/david_jones/9861520884/)

Move directly to a productive state where learning analytics are actually making a difference to the quality of learning and teaching within universities.

[![Slide12](images/9861627533_46e828321d_n.jpg)](http://www.flickr.com/photos/david_jones/9861627533/)

And here's how we plan to do it. We're going to start by talking about we (as in the authors of this talk) think we know about learning analytics. This is important because how you understand or represent learning analytics will influence how you go about designing how your institution will attempt to harness learning analytics.

We're then going to describe the three likely paths that we think universities are likely to take with learning analytics. We're going to argue that all three are necessary, but that the emphasis will be almost entirely on the first two paths and that this will lead to the faddish (i.e. unsuccessful) use of learning analytics. Our argument is that the "do it with" path is the esssential path for something like learning analytics as it currently stands.

We'll then offer some conclusions.

To repeat, we're not suggesting that there is any one path to be taken. There needs to be a mixture of all three. However, there needs to be a much greater focus on the "do it with" path than most institutions will adopt.

[![Slide13](images/9861627403_2ae77121dc_n.jpg)](http://www.flickr.com/photos/david_jones/9861627403/)

So, what do we know about learning analytics?

[![Slide14](images/9861519914_e99f851e62_n.jpg)](http://www.flickr.com/photos/david_jones/9861519914/)

Well there is strong evidence of it being a fad.

Back in 2010 the Horizon Report's Technology Outlook for the Australian and New Zealand higher education sector made no mention of learning analytics. The closest it go was something called "visual data analysis" listed in the 4 to 5 year time frame.

In the next outlook in 2012, "learning analytics" has appeared from nowhere to be the second technology listed in the "1 year or less" time frame. The normative pull had commenced. This year's outlook as "learning analytics" as number 1 in that same time frame. Every Australian university has felt the need to do something about learning analytics and is currently doing something about it.

[![Slide15](images/9861625753_0dbc6215ce_n.jpg)](http://www.flickr.com/photos/david_jones/9861625753/)

But this stuff isn't new. This the header from a script that started our collaboration around learning analytics back in 2008. Working in a central learning and teaching division we were responsible for looking after the institutional Blackboard LMS. What amazed me is that when the semester started and course sites were made available to students, no-one in the institution had any idea about the quality of the courses or if they were even ready.

This was amazing to me because I was coming from a system that automatically produced an acceptable minimal standard course website without any input from the academics. This meant we were confident that at go live there was something minimally useful for the students. We'd been doing this since 1997/1998. The idea that 10 years later you would be releasing course sites with no idea of what was there was just plain dumbfounding.

Especially given that we would receive all the common complaints from students (e.g. "the site is pointing to last year's information") and have to deal with them after go live. That was dumb. So we began writing an "Indicators" script that would examine the Blackboard database and generate a set of traffic lights indicating how ready/how good a course site was with the plan that this would be shown to the respective Associate Deans Learning and Teaching who would then take action.

For various reasons they didn't like this idea - we were seen to be over-reaching our responsibilities. Apparently, data-based decision making wasn't that important. So we started the [Indicators Project](http://indicatorsproject.wordpress.com/) and wrote some papers that to this day have had little or no positive impact on the practice of learning and teaching at that institution.

[![Slide16](images/9861518794_4f402d1c95_n.jpg)](http://www.flickr.com/photos/david_jones/9861518794/)

Of course, we'd been doing "learning analytics" for some time. Back in the last century we had a bit of open source software that would generate a weekly report about requests on our e-learning website. Each Monday we'd go over that report looking for patterns - good and bad - and making decisions about what might need to be done. Gaining insights from that data to drive our decision making.

[![Slide17](images/9861625443_2a4e29a9d0_n.jpg)](http://www.flickr.com/photos/david_jones/9861625443/)

The script even generated lovely visualisations to help.

[![Slide18](images/9861538975_eae2ccd26f_n.jpg)](http://www.flickr.com/photos/david_jones/9861538975/)

Let's return to the present. This is George Siemens, President of the [Society for Learning Analytics Research](http://www.solaresearch.org/) and well-known speaker on the topic (and others). Many of you may have heard George speak over recent weeks as he's been touring Australia. Given his involvement in learning analytics if anyone would know of an institution that is successfully implementing learning analytics it would be him.

The quote on this slide is from an email George sent in the last week or so to a learning analytics mailing list asking for examples of such institution. To his knowledge, much of what is being done is in specific research projects or small deployments. There aren't successful institutional examples we can draw upon.

[![Slide19](images/9861539345_cf4b69251a_n.jpg)](http://www.flickr.com/photos/david_jones/9861539345/)

I know there will be some who will point to the data warehouse as a counter point. Many Australian Universities have had data warehouses for quite some time. I know of a few that were put in place because the multi-million dollar ERP system didn't fulfil its promise. Only in turn for the data warehouse to also fail because hardly anyone was using the data produced. Beyond perhaps generating some data to hand over to the federal government every year.

This is finding backed up from the research from the Information Systems field. Australia Higher Education isn't alone in having failures around data warehouse systems.

[![Slide20](images/9861540736_6ba0106542_n.jpg)](http://www.flickr.com/photos/david_jones/9861540736/)

In fact, there are indications that all the very fashionable "bid data" and "business analytics" projects are failing as well.

Now, the information systems field has identified that the definition of failure (or success to take the positive perspective) is multi-faceted and subjective. But if the great obvious benefit of these systems is data-based decision making, then the systems not being used suggests an "absence of data-based decision making" which suggests fairly strongly at failure.

[![Slide21](images/9861538025_49a352a5c4_n.jpg)](http://www.flickr.com/photos/david_jones/9861538025/)

And of course this links to the broader, much written about (but nothing really successful done about) problem of information systems development failure. Large IS development projects fail. The larger they are, the more likely they are to fail.

Chances are that large scale, institution-wide adoption of learning analytics involving the multi-million dollar purchase of "Vendor X's" business intelligence platform will fail.

[![Slide22](images/9861540146_578ae182fb_n.jpg)](http://www.flickr.com/photos/david_jones/9861540146/)

Which brings us back to the Birnbaum's fad cycle as the most likely outcome. But actually, I think Birnbaum was being an optimistic, or at least didn't fully capture the complete story of fads and fashions.

The fad cycle didn't stop with the resolution of dissonance. At least not for the management consultancy firms and the vendors enabling these fads. These organistions have a profit margin to think of so they did the smartest thing. Once a fad had failed in one sector.

[![Slide23](images/9861537375_e8bc85b922_n.jpg)](http://www.flickr.com/photos/david_jones/9861537375/)

The moved onto the next sector. It's not that hard to track the movement of ERP systems from industrial manufacturing companies (where the ERP system arose) into the broader commercial business sector, then into government, then into higher education and then over the last couple of years into the K-12 education sector. It was interesting for me to observe the Queensland government's Education department employing all the same promises and visions around their adoption of an ERP system 10+ years after the same messages were employed in the Australian higher education sector.

[![Slide24](images/9861515794_91a4afdf66_n.jpg)](http://www.flickr.com/photos/david_jones/9861515794/)

We do know that learning analytics is diverse. The list here shows all of the disciplines that had something to contribute to the Learning Analytics and Knowledge conference in 2012. It represents how learning analytics draws upon a wide array of disciplines and tries to bring those together. Clow's description of the field has it picking and choosing tools and techniques from these disciplines.

[![Slide25](images/9861516024_55e511c028_n.jpg)](http://www.flickr.com/photos/david_jones/9861516024/)

We also know that higher education, technology, teaching and learning analytics all operate in an environment of change. The cliche, "the only thing certain is change" sums it up. Everything is change.

But beyond that, the field of Decision Support Systems (DSS) - a research field with a history going back 40+ years - has identified a range of fundamental principles for the design of information systems intended to support the decision making process (like learning analytics). One of those fundamental principles is evolutionary development. i.e. the development of these systems needs to be forever changing.

[![Slide26](images/9861621873_058b77f41f_n.jpg)](http://www.flickr.com/photos/david_jones/9861621873/)

At a fundamental level, learning analytics examines the data you have gathered about what you currently do, applies a range of analysis methods to that data, and hopes to reveal insights about the future. Almost by definition it is "evaluating what exists in data". The quality of this evaluation depends both on the analysis methods you use, but also the quality of the data and how effectively it captures what was being done.

This reliance on the past creates a tension between analytics and innovation, but it also creates other problems.

[![Slide27](images/9861621103_308b55fced_n.jpg)](http://www.flickr.com/photos/david_jones/9861621103/)

What value is there in learning analytics if the data you are capturing arises from poor practice. As the results of our quick survey reveals what passes for institutional e-learning is seen by ourselves as not being all that good.

In the presentation this was meant to show the live responses via the Poll Everywhere app. It didn't work as expected, but the results were captured.

In response to the question, "What percentage of your institution's online courses are good?" there were 29 responses

1. Less than 20% - 16 (55%)
2. Between 20% and 50% - 10 (34%)
3. Between 50% and 70% - 2 (7%)
4. Greater than 70% - 1 (3%)

89% of the respondents thought that at least 50% of their institution's online courses were not good.

What does this mean about the quality of the insights that can be gained from learning analytics based on data arising from this practice? What does it mean for what the purposes of learning analytics should be?

!!! warning "Broken image link"

As it happens, this isn't a new observation. In fact, Professor Mark Brown (who was also presenting at this conference and was in the room during this presentation) was quotes in a New Zealand paper on the weekend as suggesting that e-learning is a bit like teenage sex. What is being done - must less than what is being talked about - is not very good.

As it happens, I shared Mark's thoughts via Twitter and his metaphor was usefully extended by a range of folk.

[![Slide29](images/9861534895_d0cb0be7fb_n.jpg)](http://www.flickr.com/photos/david_jones/9861534895/)

Fumbling in the dark suggests that learning analytics might be able to shed some light on the practice. Perhaps reveal just how messy it is and perhaps identify that the e-learning environment in universities is far from idea.

[![Slide30](images/9861515484_99b7ace0c8_n.jpg)](http://www.flickr.com/photos/david_jones/9861515484/)

Imagine trying to analyse an act being done by people who have no idea and using data from that analysis to guide future practice.

[![Slide31](images/9861534465_350c13e46d_n.jpg)](http://www.flickr.com/photos/david_jones/9861534465/)

Not only is our current practice of e-learning somewhat ignorant, but so also is our use of learning analytics to assist teachers in improving the practice of e-learning. We don't really know yet how best to do this, no-one has really studied it.

[![Slide32](images/9861513144_9bc635e42c_n.jpg)](http://www.flickr.com/photos/david_jones/9861513144/)

In fact, as Dyckhoff and collaborators suggest even the bleeding edge research learning analytics tools aren't providing answers to the types of questions that teachers ask. Let alone the types of tools currently available within our institutional e-learning environments.

[![Slide33](images/9861536026_081a54c4b2_n.jpg)](http://www.flickr.com/photos/david_jones/9861536026/)

Which leads us to the purpose of learning analytics. There are any number of definitions of learning analytics. Rather than try distinguish between academic analytics and learning analytics etc. the definition we'll use is based on Clow's (2013). The "analysis and representation of data about learners in order to improve learning". The focus is on improving learning. If it isn't being **used** to improve learning, then learning analytics is a failure.

We also like the Elias definition to tools and processed aimed at improving learning and teaching and the subsequent observation that to achieve this, those processes and tools need to integrated into the practice of teaching and learning. Hopefully you'll see the connection between this definition of learning analytics and the rest of this presentation.

[![Slide34](images/9861535126_036bcaafed_n.jpg)](http://www.flickr.com/photos/david_jones/9861535126/)

Which brings us to the three paths and the first "Do it to"

[![Slide35](images/9861535576_47a89d7cd7_n.jpg)](http://www.flickr.com/photos/david_jones/9861535576/)

To illustrate the three paths we're going to use this model of university teaching from Trigwell (2001). The idea is that student learning (the focus) is impacted by the strategies adopted by teachers, which in turn is influenced by the planning of the teacher, their thinking about learning and teaching and finally all are impacted by the context or environment in which learning and teaching takes place.

[![Slide36](images/9861535366_daef4f3fce_n.jpg)](http://www.flickr.com/photos/david_jones/9861535366/)

The "do it to" path usually starts with very smart and senior people getting together to think about strategic directions for the institution. i.e. they've noticed the management fashion and recognised that it's important for the institution to react. They will engage typical techno-rational/strategic management techniques.

[![Slide37](images/9861533846_71be8a965c_n.jpg)](http://www.flickr.com/photos/david_jones/9861533846/)

As a result they will make changes to the context in which learning and teaching takes place. Usually in the form of strategic and policy changes. Perhaps setting up of formal projects with visible senior management buy in, appropriate KPIs, user groups etc.

[![Slide38](images/9861531735_210306374e_n.jpg)](http://www.flickr.com/photos/david_jones/9861531735/)

The assumption is that those changes will impact the thinking of teachers.

[![Slide39](images/9861510364_09d4ea68a2_n.jpg)](http://www.flickr.com/photos/david_jones/9861510364/)

Which in turn will modify how they go about planning.

[![Slide40](images/9861617093_a9dc29ba38_n.jpg)](http://www.flickr.com/photos/david_jones/9861617093/)

Which in turn results in new L&T strategies

[![Slide41](images/9861532906_c1f02d8d5c_n.jpg)](http://www.flickr.com/photos/david_jones/9861532906/)

Which in turn results in changes (hopefully improvements) to student learning.

However, in reality this type of top down change is generally so far removed from the "zone of proximal development" of the teaching staff that it never has any chance to change their thinking. After all, changing thinking is about learning and sorry, but top-down strategic change has never done a real good job at engaging staff in learning for a whole range of reasons.

Especially when confronted with an activity like learning analytics where

- No institution is actually doing it successfully.
- Where our prior attempts in the area have failed.
- Where the field itself is incredibly diverse.
- And we're planning to use a technology/approach that is under-going rapid change in an environment that is itself undergoing rapid change.
- Especially when the aim is to improve learning and teaching - which seems to rely significantly on the strategies/planning/thinking of individual academics - and we don't really know how to do this with learning analytics yet.

[![Slide42](images/9861530265_a79aaf8ff4_n.jpg)](http://www.flickr.com/photos/david_jones/9861530265/)

So, in response, the most likely outcome of the "do it to" path is that the thinking and planning of academics is by passed. In some cases this is a conscious decision. For example, most of what is being done around learning analytics at the moment is retention. Retention projects - usually run by central student administration or related areas - that are avoiding engagement with academics at all and going directly to the student. In many cases, teaching staff are completely ignorant of the work being done at the institutional level and are almost certainly ignorant of the interactions between their students and the institutional actors engaged in the retention activity,

In other cases, the teaching staff will recognise the gulf between the top-down changes and what they do and either reject it as nonsensical (at least as seen by them, but also perhaps because it is nonsensical) or workaround it because it doesn't fit with their thinking or with what is possible for them to plan and implement.

[![Slide43](images/9861529845_28fcf988e0_n.jpg)](http://www.flickr.com/photos/david_jones/9861529845/)

Beyond this outcome, there are range of other pitfalls associated with the "do it to" path. These are but some of them and I'm not going into these in any great detail.

This presentation is based on a talk given at the Australian SolarFlare workshop last year at which I spent more time going into these pitfalls, leaving less time for the "do it with" path. Today I'd like to focus on the "do it with" path more so I'll not cover many of these pitfalls.

[![Slide44](images/9861508624_6f23efb1b1_n.jpg)](http://www.flickr.com/photos/david_jones/9861508624/)

I will instead focus on what I think is a fundamental problem for Australian higher education, the almost complete ignorance that there are two main ways to view process.

Over recent years Australian higher education has adopted a myopic view of process that is ignorant of the broader management literature. Australian higher education has become enamoured and focused on top-down, strategic planning processes - essentially yet another management fashion. Australian higher education and its managers have become entirely focused on the planning school of process through. Also known as the exploitation view of process or teleological design.

What they are ignorant of is that the management literature has had a long and on-going debate between two different schools of thought on process. Characterised here as the terms "planning" and "learning". The ideas isn't that either school of thought is the one true view, neither is a silver bullet. Both have their weaknesses, both have their strengths. The ideas is that depending on your context and aims you should be using different approaches to process.

When you are in a fixed environment where you can clearly know and articulate the goals of your projects. When you know there is one right answer that is better than all others and you can successfully engage all stakeholders in that one right answer, then you use the planning approach.

However, when you are in a complex environment with a wicked problem. A situation where there is never going to be one right answer and even worse there is no way for you to even identify what the right answer is. Not to mention that you can't engage all the stakeholders successfully in a right answer (even if you could identify it). Then you should use a learning approach to process.

Which type of approach do you think is appropriate for learning analytics within Australian higher education?

[![Slide45](images/9861529236_bc6242fef0_n.jpg)](http://www.flickr.com/photos/david_jones/9861529236/)

This is not some crackpot understanding. This is not some new, ground-breaking insight. It is well established in the literature, here are just some of the fol who have written about it and the terms they have used for the "planning" and "learning" approach to process.

[![Slide46](images/9861506324_a301b54de4_n.jpg)](http://www.flickr.com/photos/david_jones/9861506324/)

Just to reinforce the point, here's a quote from James March (a big name in the field) arguing that an over empahsis on either approach leads to an unproductive state. A state Australian higher education finds itself in today. A state I hope we don't find ourselve in with learning analytics (who am I kidding).

[![Slide47](images/9861526685_9ff10aaf27_n.jpg)](http://www.flickr.com/photos/david_jones/9861526685/)

So, onto the "do it for" path.

[![Slide48](images/9861506274_4f9e4b3e6f_n.jpg)](http://www.flickr.com/photos/david_jones/9861506274/)

So again you have some smart people within the organisation. These folk probably aren't as important as the "do it to" folk and these folk may even be getting together at the behest of the "do it to" folk. These are typically central learning and teaching folk, the Associate Dean's Learning and Teaching, perhaps some innovative teaching staff and if they are really lucky the university Information Technology folk.

[![Slide49](images/9861504394_0f7cb44187_n.jpg)](http://www.flickr.com/photos/david_jones/9861504394/)

Knowing about learning analytics and it can help the teaching staff they will make changes to the context for the academic staff. This might be in the form of running some seminars on learning analytics. They might invite George Siemens to give a talk to the staff. They might select and install some learning analytics software in the LMS or elsewhere. They might upskill themselves in learning analytics so they can help teaching staff.

[![Slide50](images/9861527866_d627e99017_n.jpg)](http://www.flickr.com/photos/david_jones/9861527866/)

The idea is that - like the "do it to" path - these changes in the context will lead to changes in the thinking, planning and strategies of the teaching staff and subsequently improvement in the student learning experience.

[![Slide51](images/9861525285_530974be13_n.jpg)](http://www.flickr.com/photos/david_jones/9861525285/)

Of course, anyone who has worked for central learning and teaching - like both of us have - know that this isn't what happens. Instead, only a very small percentage of the teaching staff ever engage with the changes made to the L&T context. Almost certainly the teaching staff that attended those sessions were the ones that didn't really need to attend. So your impact is lessened.

But then at each level through this model the impact reduces further. The greater rewards from research, the dissonance between what the LMS tool does and the pedagogy of the teacher and other reasons all contribute to a diminution of the impact of the changes made to the L&T context.

[![Slide52](images/9861524785_cebb760927_n.jpg)](http://www.flickr.com/photos/david_jones/9861524785/)

As with the "do it to" path, the "do it for" path has a range of pitfalls. We're going to focus on three only.

[![Slide53](images/9861503114_7cdc02e5c8_n.jpg)](http://www.flickr.com/photos/david_jones/9861503114/)

The first is drawn from work by Geoghegan from 1994 around instructional technology in American universities. It has insights which I think still apply today. His general observation is that instructional technology never clears the chasm that exists between the early adopters and the majority. i.e. as identified above the "do it for" path really only impacts the early adopters.

[![Slide54](images/9861524845_60704b532e_n.jpg)](http://www.flickr.com/photos/david_jones/9861524845/)

Geoghegan identified four reasons for this.

The first is the assumption that all academics are the same. When they are demonstrable not. We'll return to this.

The second is that the folk making many of these decisions form a self-reinforcing clique - the technologists alliance. i.e. the folk who make the decisions about what changes to make as part of the "do it for" path are mostly early adopters and boosters of technology (by the way the "IT" in "IT staff" above means instructional technology). They see the world differently.

This ends up in approaches that don't match the experience and conceptualisations of the mainstream and because of this it fails to provide the majority a compelling reason for them to adopt what ever is being decided for them.

[![Slide55](images/9861609393_053c4094e2_n.jpg)](http://www.flickr.com/photos/david_jones/9861609393/)

Convery captures a large part of this in these quotes. The technologists alliance have a much larger say about what will happen and through this the connection with the lived experience of the majority gets ignored leading to a failure to cross the chasm.

[![Slide56](images/9861502244_a7a86dfb95_n.jpg)](http://www.flickr.com/photos/david_jones/9861502244/)

To illustrate the distinction between the early adopters and the majority, Geoghegan draws on Moore's original work which in turn was based on the diffusion of innovations work from Rogers. This work clearly demonstrates that there is a significant difference between the early adopters and the early majority. The "do it to" and the "do it for" paths fail to engage with this diversity and subsequently fail to make any large scale or long term impact.

But it's even worse that this. There's a lot to criticise about the diffusion of innovations work, but perhaps the most applicable criticism here is that it under plays the diversity between teachers. It's just not two groups with significant differences. Within each of these groups there is significant difference.

[![Slide57](images/9861608413_349ecb4556_n.jpg)](http://www.flickr.com/photos/david_jones/9861608413/)

To take another task lets look at how the "do it for" approach typically works in terms of changing learning and teaching. This approach typically treats the actual teaching of a course as a black box (in this case yellow). What goes on inside that box is ignored by the "do it for" approach.

Instead any attempts to re-design a course is done before the course is taught. Once those changes are done, the course is taught with little additional focus on that experience, until at the end out pops a range of outputs, student results and satisfaction survey responses. These outputs are then used as inputs to the re-design phase before yet another black box offering of the course.

Central L&T is largely ignorant of the actual experience of teaching a course. The assumption is that the design is done outside the course offering. The assumption is that design can be, at some level, general and abstract.

This is why a lot of institutional learning analytics projects focus on measures like retention. It's too complex to look inside a course and respond to the diversity of experience that is there.

[![Slide58](images/9861523966_0d3c64ec12_n.jpg)](http://www.flickr.com/photos/david_jones/9861523966/)

Which brings us back to the observation about learning analytics, that there are dearth of studies figuring out how to use learning analytics within that black box. We don't know how to do it well yet.

[![Slide59](images/9861522155_38056578ac_n.jpg)](http://www.flickr.com/photos/david_jones/9861522155/)

Which brings us to the "do it with" path. As you have probably guessed this is the path which I think will be the most fruitful and interesting in identifying how to harness learning analytics to improve learning and teaching. However, I don't think it's the only path, it does need to be supported by and inform the other paths. My problem is that this path will largely be ignored and its absence will result in learning analytics becoming yet another management fashion.

[![Slide60](images/9861500614_426233e4cc_n.jpg)](http://www.flickr.com/photos/david_jones/9861500614/)

This path starts with a group of people working with teaching staff inside the black box that is teaching the course. At the level of the teachers' strategies. The idea is to develop an understanding of the lived experience - in all its diversity and difficulty - and figure out uses of learning analytics (and other tools) that can help make a difference.

[![Slide61](images/9861521215_a3acd022c8_n.jpg)](http://www.flickr.com/photos/david_jones/9861521215/)

That insight is used to make changes at the level of strategy in response to what is actually going on. Due to the diversity of what happens at this level there will problems as to what you address. It will be very subjective, very different, there will be no-one silver bullet. So it won't be large scale changes you're making.

[![Slide62](images/9861607423_09b15616d3_n.jpg)](http://www.flickr.com/photos/david_jones/9861607423/)

But by making those changes you learn. You understand what worked and what didn't and you start making changes to student learning (without a long-term, large scale project where nothing happens for a long time) and by working with teachers you are helping change how they plan because they have new tools and approaches that respond to their needs.

[![Slide63](images/9861520265_df13be83f8_n.jpg)](http://www.flickr.com/photos/david_jones/9861520265/)

If you're lucky and you do it well this process may in turn lead to changes "up the ladder", but those changes will take some time to happen and will require some work.

There is no simple, easy solution.

[![Slide64](images/9861521816_146e9d5226_n.jpg)](http://www.flickr.com/photos/david_jones/9861521816/)

It is important to recognise that you are doing a lot of these interventions quickly and learning from them all. This isn't a one off process. Each time you try some interventions you gain new insights - you and other actors learn - and you apply that learning to make further improvements and start upon a cycle of on-going learning and change.

[![Slide65](images/9861604683_4610a37fa5_n.jpg)](http://www.flickr.com/photos/david_jones/9861604683/)

A cycle that goes on. Remember, you also operate in an environment of change with technology that is also changing. All this requires your organisation to be able to change in response.

[![Slide66](images/9861519965_33ab2be74d_n.jpg)](http://www.flickr.com/photos/david_jones/9861519965/)

By now I'm hoping you can see which school of thought around process we're leaning towards as being most appropriate for learning analytics within higher education.

[![Slide67](images/9861520646_0c396460b1_n.jpg)](http://www.flickr.com/photos/david_jones/9861520646/)

In part, this is based on the view of the teacher as a primary change agent. But it's also in recognition that learning and teaching in a modern university is increasingly complex and requires this type of approach.

[![Slide68](images/9861603503_d1f8c62fa9_n.jpg)](http://www.flickr.com/photos/david_jones/9861603503/)

It's also influence by the growing observation that workload for teaching staff in universities is increasing. We believe this is largely due to the fact that there's been an over emphasis on the do it to and for paths and not enough with. The people who are driving institutional e-learning are ignorant of the complexity of teaching and are providing tools, policies and approaches that are inappropriate.

[![Slide69](images/9861496014_629fbc5f60_n.jpg)](http://www.flickr.com/photos/david_jones/9861496014/)

It also comes back to the common insights about learning analytics where knowledge of the context in which learning and teaching takes place is essentially to deploying learning analytics.

[![Slide70](images/9861496134_c9dac93554_n.jpg)](http://www.flickr.com/photos/david_jones/9861496134/)

And that any institution-wide approach to learning analytics must be based on a thorough knowledge of the context.

[![Slide71](images/9861517675_f8efa53c27_n.jpg)](http://www.flickr.com/photos/david_jones/9861517675/)

A common argument against this type of bottom up approach is that it doesn't provide the type of large-scale, strategic advantage - the competitive difference - that senior management demand for their organisation. This is of course an ignorant claim based on a lack of knowledge of the reality of gaining strategic advantage from information technology.

You do not gain strategic advantage or competitive difference by adopting the same enterprise business intelligence/data warehouse system from the same vendor as all your competitors and then following what is the best-practice advice with large scale enterprise systems (as followed by all university information technology divisions) and implement those systems as vanilla. This approach removes all distinction between organisations.

We know from the information systems research that competitive advantage from ICTs only comes for organisations that are able to convert those systems into unique, practical and situated knowledge for action. In fact, it's this type of knowledge from which the original "strategic information systems" arose, not from buying an enterprise tool from a vendor.

[![Slide72](images/9861602023_7bb8fef000_n.jpg)](http://www.flickr.com/photos/david_jones/9861602023/)

And now to some frameworks that are a bit more specific to learning analytics and can provide some more insight into how you implement learning analytics in ways that avoid faddism.

[![Slide73](images/9861516465_842f3176fb_n.jpg)](http://www.flickr.com/photos/david_jones/9861516465/)

This is a model of analytics published by George Siemens in his 2013 journal article. It's a fairly standard representation of the cycle of learning analytics. In doing so we think it suffers from the same over-emphasis that much of learning analytics suffers from. We think this over emphasis is bad if your aim with learning analytics is improving student learning.

We're in the process of developing the IRAC framework ([an early paper](http://indicatorsproject.wordpress.com/2013/09/22/the-irac-framework-locating-the-performance-zone-for-learning-analytics/) explaing IRAC) which we hope/think will help. We're going to use this framework to outline the shortcomings of the common thinking about learning analytics.

[![Slide74](images/9861495394_4e6c0a8f4f_n.jpg)](http://www.flickr.com/photos/david_jones/9861495394/)

The I in IRAC stands for information. This involves the gathering, normalising and analysis of the data and information your institution has. This is the foundation of learning analytics, without information and its analysis you can't generate insights. This is perhaps why so much of learning analytics is focused at this stage. More than 3/4 of George's model focuses on this stage. While this stage is important, we think this over emphasis gets in the way of using learning analytics to improve learning and teaching.

[![Slide75](images/9861601573_e54c001194_n.jpg)](http://www.flickr.com/photos/david_jones/9861601573/)

The R in IRAC stands for representation. Once you've gathered and analysed your information you have to represent the findings in ways that people will understand them. This is often where most of the analytics literature stops. We think this is lazy and short-sighted and it's good to see George's model has more that follows representation.

We also think that about of thinking and work that goes into representation is too limited. It's almost as if once we have a dashboard, it's all good. By the way, we think dashboards suck.

[![Slide76](images/9861517176_8373ca7433_n.jpg)](http://www.flickr.com/photos/david_jones/9861517176/)

The A in IRAC stands for Affordances. Very little of the learning analytics literature considers this. George's model does include the notion of action. i.e. you need to undertake some sort of action based on the insights that were represented as a result of your analysis of the information.

We argue that in order to encourage appropriate action it is essential that both the learning analytics applications and the broader institutional context need to offer affordances for that action. i.e. they need to make it easier and more obvious for learners and teachers to take the appropriate action.

There's much more to learning analytics than dashboards.

[![Slide77](images/9861600413_82f7e37eea_n.jpg)](http://www.flickr.com/photos/david_jones/9861600413/)

The C in IRAC is change. George's analytics model captures this through its cyclical nature. Once you've carried out some action you will get more information that you have to analyse, represent and that will inform new action. A cycle that goes on and on.

While change is there in George's model it is implicit. It's not clearly stated in the diagram in the same way that "Action" is (for example). We believe an understanding of the need for on-going change is so central to harness learning analytics that we make it an explicit part of the framework.

Change will come in many different forms. At the very least, the Information, Representation and Affordances offered by your institution's learning analytics applications will need the capacity to change. This change should not just be first order change, it should enable and support second order change. The changing of underlying assumptions and conceptions.

After all the argument here is that we need to take a learning approach to learning analytics and this involves conceptual change.

[![Slide78](images/9861600393_0d8a21d8f8_n.jpg)](http://www.flickr.com/photos/david_jones/9861600393/)

Just briefly, as argued above we thinking that much of the learning analytics literature as the various weights of the different parts of the IRAC framework wrong.

Information is foundation/central to learning analytics. But the gathering and analysis of that information is only a very small part of the process of improving learning and teaching with learning analytics.

There needs to be a much greater focus on the representation, affordances and change components of the IRAC framework. An organisation needs to invest much more time on the R, A and C components if they are to actually make significant and on-going improvements to learning and teaching.

[![Slide79](images/9861516886_9e38d100dc_n.jpg)](http://www.flickr.com/photos/david_jones/9861516886/)

Earlier on in the presentation you saw parts of an email George Siemens sent asking about examples of systemic approaches to learning analytics. On the screen you can see excerpts from a reply to George's email. A reply that encapsulates much of what we've argued here.

A top-down systemic approach is only going to alienate folk. It's also going to limit you to very broad (and poor) indicators of learning - GPA and retention rates.

Instead, you need to provide a foundation of resources that will enable a range of approaches to develop in ways that acknowledge (and leverage) the idiosyncrasies of learning and teaching.

[![Slide80](images/9861513895_d5366f28a3_n.jpg)](http://www.flickr.com/photos/david_jones/9861513895/)

So some conclusions.

[![Slide81](images/9861598043_9817a5b25a_n.jpg)](http://www.flickr.com/photos/david_jones/9861598043/)

A couple of weeks ago I watched an online video of a talk given by Brett Victor. A smart guy, ex-Apple engineer who is doing some really great stuff with technology. In this talk Brett assumed the persona of a software developer giving a talk in the early 1970s - he used an OHP and slides for period authenticity. The talk was aimed at highlighting a few interesting technical breakthroughs from the last 1960s/early 1970s that promised to revolutionise how software was developed. None of that revolution has happened.

Throughout his talk Brett showed how - even folk as technically proficient as software developers - resist technological change.

[![Slide82](images/9861492364_0abcc80e73_n.jpg)](http://www.flickr.com/photos/david_jones/9861492364/)

Amongst his reflections/conclusions was the observation that while technology changes quickly, people change their minds about how to use that technology very slowly. Even the most technically proficient of people - the people developing technology - show this.

I'd like to add that organisations - where you're talking about groups of people changing their minds - change even more slowly. Perhaps this is why University IT systems are still focusing on single systems and hierarchical command and control while the world has moved into networked ways of being.

[![Slide83](images/9861514756_57dfb7984e_n.jpg)](http://www.flickr.com/photos/david_jones/9861514756/)

It is perhaps why Australian universities are ignorant of the learning school of thought around process.

[![Slide84](images/9861514036_c16f8f2f83_n.jpg)](http://www.flickr.com/photos/david_jones/9861514036/)

Brett's second point (or at least the 2nd one I took away) was that as a creative person, the most dangerous though you can have is that you know what you are doing. Similarly, I would argue that this is the most dangerous thought an Australian university can have about learning analytics and e-learning more generally.

The trouble is that the over-emphasis on the planning approach to process is based on the this very assumption. That the institution knows what is doing. This approach by its very nature will limit the impact of learning analytics or any form of innovation.

[![Slide85](images/9861491854_f8146a8971_n.jpg)](http://www.flickr.com/photos/david_jones/9861491854/)

This is why the "do it with" approach is so essential. It acknowledges that we don't know what we're doing when it comes to learning analytics and thus opens us up to all sorts of possibilities that will arise from productive engagement with the reality of learning and teaching.

[![Slide86](images/9861596533_0079d8a887_n.jpg)](http://www.flickr.com/photos/david_jones/9861596533/)

As part of this process, we think that getting the information right is a good first step, but that it is the step on which we should spend the least amount of time and energy. That representation, affordances and on-going change should consume a lot more attention and resources.

Because in the end we don't know much about learning analytics and its important that we question everything and learn as much as we can.

[![Slide87](images/9861513986_729e8149b8_n.jpg)](http://www.flickr.com/photos/david_jones/9861513986/)

### References

Abrahamson, E., & Fairchild, G. (1999). Management fashion: Lifecycles, triggers and collective learning processes. _Administrative Science Quarterly_, _44_(4), 708–740.

Arnott, D., & Pervan, G. (2005). A critical analysis of decision support systems research. _Journal of Information Technology_, _20_(2), 67–87. doi:10.1057/palgrave.jit.2000035

Birnbaum, R. (2000). _Management Fads in Higher Education: Where They Come From, What They Do, Why They Fail_. San Francisco: Jossey-Bass.

Bright, S. (2012). eLearning lecturer workload: working smarter or working harder? In M. Brown, M. Hartnett, & T. Stewart (Eds.), _ASCILITEÕ2012_. Wellington, NZ.

Ciborra, C. (2002). _The Labyrinths of Information: Challenging the Wisdom of Systems_. Oxford, UK: Oxford University Press.

Clow, D. (2012). The learning analytics cycle. _Proceedings of the 2nd International Conference on Learning Analytics and Knowledge - LAK  Õ12_, 134–138. doi:10.1145/2330601.2330636

Clow, D. (2013). An overview of learning analytics. _Teaching in Higher Education_, (August), 1–13. doi:10.1080/13562517.2013.827653

Dawson, S., Bakharia, A., Lockyer, L., & Heathcote, E. (2011). _ÒSeeingÓ networks : visualising and evaluating student learning networks Final Report 2011_. _Main_. Canberra.

Dyckhoff, a. L., Lukarov, V., Muslim, A., Chatti, M. a., & Schroeder, U. (2013). Supporting action research with learning analytics. In _Proceedings of the Third International Conference on Learning Analytics and Knowledge - LAK  Õ13_ (pp. 220–229). New York, New York, USA: ACM Press. doi:10.1145/2460296.2460340

Elias, T. (2011). _Learning Analytics: Definitions, Processes and Potential_. _Learning_.

Geoghegan, W. (1994). Whatever happened to instructional technology? In S. Bapna, A. Emdad, & J. Zaveri (Eds.), (pp. 438–447). Baltimore, MD: IBM.

Goldfinch, S. (2007). Pessimism, computer failure, and information systems development in the public sector. _Public Administration Review_, _67_(5), 917–929.

Lockyer, L., Heathcote, E., & Dawson, S. (2013). Informing Pedagogical Action: Aligning Learning Analytics With Learning Design. _American Behavioral Scientist_, _XX_(X), 1–21. doi:10.1177/0002764213479367

Lodge, J., & Lewis, M. (2012). Pigeon pecks and mouse clicks : Putting the learning back into learning analytics. In Mark Brown, M. Hartnett, & T. Stewart (Eds.), _Future challenges, sustainable futures. Proceedings ascilite Wellington 2012_ (pp. 560–564). Wellington, NZ.

March, J. (1991). Exploration and exploitation in organizational learning. _Organization Science_, _2_(1), 71–87.

Mor, Y., & Mogilevsky, O. (2013). The learning design studio: collaborative design inquiry as teachersÕ professional development. _Research in Learning Technology_, _21_.

Sharples, M., Mcandrew, P., Weller, M., Ferguson, R., Fitzgerald, E., & Hirst, T. (2013). _Innovating Pedagogy 2013: Open University Innovation Report 2_. Milton Keynes: UK.

Siemens, G. (2013). Learning Analytics: The Emergence of a Discipline. _American Behavioral Scientist_, (August). doi:10.1177/0002764213498851

Siemens, George, & Long, P. (2011). Penetrating the Fog: Analytics in Learning and Education. _EDUCAUSE Review_, _46_(5).

Suthers, D., & Verbert, K. (2013). Learning analytics as a middle space. In _Proceedings of the Third International Conference on Learning Analytics and Knowledge - LAK  Õ13_ (pp. 2–5).

Swanson, E. B., & Ramiller, N. C. (2004). Innovating mindfully with information technology. _MIS Quarterly_, _28_(4), 553–583.

Trigwell, K. (2001). Judging university teaching. _The International Journal for Academic Development_, _6_(1), 65–73.