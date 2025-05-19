---
categories:
- chapter-4
- design-theory
- elearning
- indicators
- lmsevaluation
- phd
- thesis
date: 2009-08-05 13:14:48+10:00
next:
  text: Automating calculation of LMS/CMS/VLE feature usage - a project?
  url: /blog/2009/08/05/automating-calculation-of-lmscmsvle-feature-usage-a-project/
previous:
  text: How do you measure success with institutional use of an LMS/VLE?
  url: /blog/2009/08/05/how-do-you-measure-success-with-institutional-use-of-an-lmsvle/
title: Factors related to the breadth of use of LMS/VLE features
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Automating calculation of LMS/CMS/VLE feature usage &#8211; a project? &laquo;
        The Weblog of (a) David Jones
      author_email: null
      author_ip: 74.200.246.66
      author_url: https://djon.es/blog/2009/08/05/automating-calculation-of-lmscmsvle-feature-usage-a-project/
      content: '[...] The Weblog of (a) David Jones Another voice in the blogosphere    &laquo;
        Factors related to the breadth of use of LMS/VLE&nbsp;features [...]'
      date: '2009-08-05 13:57:19'
      date_gmt: '2009-08-05 03:57:19'
      id: '2690'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: External factors associated with CMS adoption &laquo; The Weblog of (a)
        David Jones
      author_email: null
      author_ip: 66.135.48.210
      author_url: https://djon.es/blog/2009/08/05/external-factors-associated-with-cms-adoption/
      content: '[...] factors associated with CMS&nbsp;adoption  This post follows on
        from a previous post and continues an examination of some papers written by Malikowski
        and colleagues examining the [...]'
      date: '2009-08-05 14:35:18'
      date_gmt: '2009-08-05 04:35:18'
      id: '2691'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
As a step towards thinking about how you judge the success of an LMS/VLE, this post looks at some work done by [Steven Malikowski](http://malikowski.org/). Why his work? Well he is co-author on three journal papers that provide one perspective on the usage of features of an LMS, including one that proposes a model for research into course management systems. A list of the papers in the references section.

This post focuses on looking at the 2008 paper. On the whole, there seems to be a fair bit of space for research to extend and improve on this work.

### Factors related to breadth of use

The abstract of this paper (Malikowski, 2008) is

> A unique resource in course management systems (CMSs) is that they offer faculty members convenient access to a variety of integrated features. Some featurs allow faculty members to provide information to students, and others allow students to interact with each other or a computer. This diverse set of features can be used to help meet the variety of learning goals that are part of college classes. Currently, most CMS research has analyzed how and why individual CMS features are used, instead of analyzing how and why multiple features are used. The study described here reports how and why faculty members use multiple CMS features, in resident college classes. Results show that nearly half of faculty members use one feature or less. Those who use multiple features are significantly more likely to have experience with interactive technologies. Implications for using and encouraging the use of multiple CMS features are provided.

Suggests that cognitive psychology is the theoretical framework used. In particular, the idea that there are discrete categories of learning goals ranging from simple to complex and that learners that don't master the simple, first, will have difficulties if they attempt the more complex. An analogy is made with the use of a CMS, there are simple features that need to be learned before using complex features.

In explaining previous research on adoption of features of an LMS (mostly his own quantitative evaluations) the author reports that the college/discipline an academic is in explains most variation.

#### How to use these findings

The point is made that a CMS is used to transmit information more than twice as much as it is used for anything else. Also, that there are cheaper and better ways to transmit information.

The suggestion is then made that

> Instructional designers, researchers, and others interested in increasing effective CMS use can use the research just summarized to emphasize factors that are related to the use of uncommon CMS features and deemphasize factors that are not related to increased use.

But the best advice that is presented is that if you wish to promote use X, then encourage it in discipline Y first since they have shown interest in related features. Then, after generating insight, seek to take it elsewhere.......??

#### Use of multiple features

Only a small number of studies have focused on use of multiple features. Most achieved by asking academics how they use the CMS. Suggests that a second way is to visit course sites and observe which features are used. Suggests that observing behaviour is more accurate than asking them how they behave.

**IMPLICATION: the approach Col and Ken are using for Blackboard and what I'm using for Webfuse is automated. Not manual. A point of departure.**

#### Methodology

Three bits of data were used

1. Usage of 6 common CMS features
    - Random sample of 200 staff at US institution using D2L were asked to participate - 81 chose to participate.
    - 154 D2L sites were analysed as staff teach more than one course a semester
    - 2 research team members visited and manually analysed each course site - repeating until no discrepancies.
2. External factors: class size, the college/discipline and class level (1st, 2nd year etc)  
    Gathered manually from the course site.
3. 10 internal factors focused primarily on the faculty members' previous experience with technology.  
    Gathered by surveying staff.

**Limitation:** I wonder if D2L has any adaptive release mechanisms like Blackboard. Potentially, if the team member visiting each course site has an incorrectly configured user account, they may not be able to see everything within the site.

Purpose was to determine if internal or external factors were related to adoption of multiple CMS features. Established using a regression analysis with the dependent variable being the number of features adopted and the independent variables being the 3 external and 10 internal factors.

#### What is adoption?

This is a problem Col and I have talked about and which I've mentioned in some early posts looking at Webfuse usage. The definition Malikowski used in this study was

> In this study, adopting a feature was defined as a situation where a D2L Web site contained enough instances of a feature so this use was at or above the 25th percentile, for a particular feature. For example, if a faculty member created a D2L Web site with 10 grade book entries, the grade book feature would have been adopted in this Web site, since the 25th percentile rank for the grade book feature is 7.00. However, if the same Web site contained 10 quiz questions, the quiz feature would not have been adopted since the 25th percentile rank for quiz questions is 12.25

I find this approach troubling. Excluding a course from adopting the quiz feature because it has only 10 questions seems harsh. What if the 10 questions were used for an important in class test and was a key component of the course. What if there are a few courses that have added all of the quiz questions provided with the textbook into the system.

**Implication:** There's an opportunity to develop and argue for a different - better - approach to defining adoption.

#### Sample of results

- 36% of sites used only 1 feature
- 72% of sites used 2 or less features
- 0% of sites used all 6 features
- Only four of the external/internal factors could be used to predict the number of CMS features adopted
    1. Using quizzes
    2. College of social science
    3. Using asynchronous discussions
    4. Using presentation software (negative correlation)

#### Discussion

Suggests that the factors found to predict multiple feature use can be used to guide instructional designers to work with these faculty to determine what works before going to the others.

**Limitation:** I don't find this a very convincing argument. I start to think of the technologists alliance and the difference between early adopted and the majority. The folk using multiple LMS features are likely to be very different than those not using many. Focusing too much on those already using many might lead to the development of insight that is inappropriate for the other category of user.

**Implication:** There seems to be some research opportunities that focuses on identifying the differences between these groups of users by actually asking them. i.e. break academics into groups based on feature usage and talk with them or ask them questions designed to bring out differences. Perhaps to test whether they are early adopters or not.

### References

Malikowski, S., Thompson, M., & Theis, J. (2006). External factors associated with adopting a CMS in resident college courses. Internet and Higher Education, 9(3), 163-174.

Malikowski, S., Thompson, M., & Theis, J. (2007). A model for research into course management systems: bridging technology and learning theory. Journal of Educational Computing Research, 36(2), 149-173.

Malikowski, S. (2008). Factors related to breadth of use in course management systems. Internet and Higher Education, 11(2), 81-86.