---
title: Some reasons why business intelligence tools aren't the right fit
date: 2010-01-27 13:24:20+10:00
categories: ['indicators', 'information-systems']
tags: ['academicanalytics', 'analytics', 'knowledgemanagement']
type: post
template: blog-post.html
---
The following started as an attempt to develop an argument that business intelligence/data warehouse tools are not a perfect fit for what is broadly called academic analytics. In fact, as I was writing this post I realised that it's actually an argument that business intelligence tools aren't a perfect fit for what I'm interested in doing and that is **not** academic analytics.

The following is by no means a flawless, complete argument but simply an attempt to make explicit some of the disquiet I have had. Please, feel free, and I actively encourage you, to point out the flaws in the following. The main reasons for writing this are:

1. see what form the final argument might take;
2. see if I can convince myself of the argument; and
3. see if others can see some value.

### Background - the indicators project

Some colleagues and I are currently involved in some work we're calling [The Indicators Project](http://indicatorsproject.wordpress.com/) which

> aims to build on and extend prior work in the analysis of usage data from Learning Management Systems

In our [first paper](http://indicatorsproject.wordpress.com/2009/10/09/the-indicators-project-identifying-effective-learning-adoption-activity-grades-and-external-factors/) we presented some findings that contradicted some established ideas around LMS usage due to the differences in our student body, the breadth and diversity of the data we used.

The indicators project is especially interested in how what we can find out about LMS usage that can help improve learning and teaching. We're especially interested in what analysis across time, across LMS and across institutions can reveal that we don't currently know.

It's somewhat related to the idea of academic analytics

### Background - academic analytics

According to [Wikipedia](http://en.wikipedia.org/wiki/Academic_Analytics) academic analytics is "the term for business intelligence used in an academic setting". In turn, [business intelligence](http://en.wikipedia.org/wiki/Business_intelligence) is described as "skills, processes, technologies, applications and practices used to support decision making".

In an environment that is increasingly demanding techno-rational approaches to management, especially the requirement for universities to quantitatively prove that they are giving value for money, universities have started to go in for "business intelligence" in a big way. For most, this foray into "business intelligence" means setting up a data warehouse and the accompanying organisational unit to manage the data warehouse.

The "intelligence" unit is often located either within the information technology grouping or directly within the senior management structure reporting to a senior executive (i.e. a Pro or Deputy Vice Chancellor within an Australian setting). This location tendency arguably reveals the focus of such units on either the technology or servicing the needs of the senior executive they report to.

With the increasing use of technology (especially Learning Management Systems - LMS/VLE) to mediate learning and teaching there becomes available an increasing volume of data about this process. Data which may (or may not) reveal interesting insights into what is going on. Data which may be useful in decision making. i.e. Academic Analytics (aka business intelligence for learning and teaching) has arrived.

In those universities where data warehouses exist, an immediate connection is made between analysing and evaluating LMS usage data and the data warehouse. It is assumed that the best way to analyse this data is to put it into the data warehouse and allow the "intelligence" unit to do their thing.

I'm not convinced that this is the best approach and the following is my attempt to argue why.

### Business Intelligence != Data Warehouse

van Dyk (2008) describes "a business intelligence approach is followed in an attempt to take advantage ICT to enable the evaluation of the effectiveness of the process of facilitating learning" and argues that the context that leads to effective data for decision making "can only be created when a deliberate business intelligence approach if followed". The paper also contains a description of a data warehouse model that accomplishes exactly that. The framework is based on the work of Kimball and Ross (2002) and is shown below

[![The business intelligence framework](images/4307338825_5382f29880_m.jpg)](http://www.flickr.com/photos/david_jones/4307338825/ "The business intelligence framework (van Dyk, 2008), on Flickr")

As you can note this business intelligence framework includes as a core, and very important, part a data warehouse. Not surprising as it is based on a book about data warehouses.

However, drawing on the Wikipedia [business intelligence page](http://en.wikipedia.org/wiki/Business_intelligence) (my emphasis added)

> Often BI applications use data gathered from a data warehouse or a data mart. However, not all data warehouses are used for business intelligence **nor do all business intelligence applications require a data warehouse**.

I'm trying to develop an argument that a data warehouse, defined as a tool/system that sold as a data warehouse tool, may not be the best fit for supporting decision making based around LMS usage data. In particular, it may not be the best fit for the indicators project.

### But don't you need a data warehouse

In the early days of the indicators project we developed an image to represent what we were thinking the project would do. It's shown below.

\[caption id="" align="aligncenter" width="235" caption="Overview of indicators project"\][![Project Overview](images/3973651740_a069cd611d.jpg "Project Overview")](http://farm4.static.flickr.com/3440/3973651740_1cc3c62d6b_o_d.png)\[/caption\]

There is certainly some similarity between this image and the business intelligence framework above. Both images encapsulate the following ideas:

- You take data from somewhat, do some operations on it and stick it into a form you can query.
- You take some time to develop queries on that standardised data that provide insights of interest to people.
- You make that information available to folk.

So you're doing essentially the same thing. A lot of people have spent a lot of time on the math and the IT necessary to create and manage data warehouse tools. So why wouldn't you use a data warehouse? What's the point of this silly argument?

### The problems I have with data warehouses

My problem with data warehouses is that the nature of these systems and how they are implemented within organisations are a bad fit for what the indicators project wants to achieve. From above, the indicators project is especially interested in finding out what analysis of LMS usage data across time, LMS and institution can reveal beyond what is currently known.

The nature of data warehouses within universities and the tools and processes used to implement them are, from my perspective, heavy weight, teleological, proprietary and removed from the act of learning and teaching. These characteristics get in the way of what the indicators project needs to do.

#### Heavyweight and expensive

Institutions generally spend a lot of money on the systems, people and processes required to set up their data warehouses. Goldstein (2005) reports key findings from an ECAR study of academic analytics and suggests that more extensive platforms are more costly. When systems cost a lot they are controlled. They are after all an expensive resource that must be effectively managed. This generally means heavyweight processes of design and control.

While a significant amount of work has been done around evaluation LMS usage, there's still a lot to discover. The very act of exploring the data - especially when going cross institutional, cross LMS and cross time - will generate new insight that will require modification to how data is being prepared for the system and how it is being reported.

This level of responsiveness is not a characteristic of heavyweight processes and expensive systems. Especially when the systems main aim and use is focused at other purposes.

#### Not focused on L&T

Goldstein (2005) reports that few institutions have achieved both broad and deep usage of academic analytics with the most active users coming from central finance, central admissions and institutional research. In fact, the research asked respondents to evaluate their use of academic analytics within seven functional areas. **None** of those seven areas involved teaching and learning.

This seems to suggest that the focus of data warehouse use within universities is not focused on L&T. The expensive resources of the data warehouse is focused elsewhere. Which suggests that resources available to tweek and modify reports and data preparation for learning and teaching purposes will be few and far between.

#### Proprietary

Due to the expense of these systems universities will sensibly spend a lot of time evaluating which systems to go with. This will lead to differences in the systems chosen for use. Institutional differences will also lead to differences in the type of data being stored and the format in which it is stored.

The indicators project has an interest in going across institutions. Of comparing findings at different universities. While a data warehouse approach might work at our current institution, it probably won't be easily transportable to another institution.

This is not to suggest that it wouldn't be transportable, but that the cost of doing so might exceed what is politically possible within current institutions.

#### Not located within L&T

It is well known that the two most important factors contributing to the adoption (or not) of a piece of technology are:

- Ease of use; and
- Usefulness.

Academic staff at universities are not rewarded (by the institution) for spending more time on their learning and teaching. They do not received any, let alone significant, encouragement to change their practice. Academics are generally given enough freedom to choose whether or not they use a tool and always have the freedom to choose how they use a tool. i.e. if they are forced to use a tool that is not easy to use and/or useful, they will not use it effectively.

The reports and dashboards associated with data warehouse tools do not live within the same space that academic staff use when they are learning and teaching. E-learning for most university staff means the institutional LMS. Systems that are not integrated into the every day, existing systems used by academic staff are less likely to be used.

The usefulness of these reports will be governed by how well they are expressed in terms that can be understood by the academic staff. Goldstein (2005) reports on there being a two-part challenge in providing effective training for academic analytics. I'm going to divide those two into three challenges (in the original the last 2 in my list were joined into one):

1. help users how to learn the technology;
2. help users understand the underlying data; and
3. envision how the analytical tools could be applied.

To me, the existence of these challenges suggest that the technology being used is inappropriate. It is too hard or different for the users to understand and the information being presented is also too far removed from their everyday experience. i.e. if they need training in how to use it, then the tool is too far removed from their existing knowledge.

Given that Goldstein (2005) found these difficulties for the "sweet spot" of business intelligence (i.e. "business and finance", "budget and planning", "institutional research" etc.). Imagine the difficulties that will arise when attempting to apply the same technology to learning and teaching. Learning and teaching itself is inherently diverse, while the perspectives of learning and teaching held by the academics doing the teaching is several orders of magnitude more diverse.

The key point here is the "build it and they will come" approach of putting this data into a data warehouse will not work. The academic staff will not come. A large amount of work is required to develop insights into how to identify and integrate the knowledge that arises out of the LMS data in a form that encourages adoption.

Getting academic staff to meaningfully adopt and use this information to change - hopefully improve - their teaching is much more important, difficult and expensive than the provision of a data warehouse. The wrong tool - e.g. a data warehouse - will significantly limit this much more important task.

### So what

I believe any approach to use data warehouse tools to provide "dashboards" to coal face academics so they can see information about the impact of their teaching and their students learning, will ultimately fail, or at the very least be very expensive, difficult and be used in limited ways.

Is there any institution doing just this know that can prove me wrong?

### What's the solution?

That's for another post. But what I'm thinking of is :

- Much cheaper/simpler technology.
- Lightweight methodology.
- Research and coal-face informed development and testing of useful measures/information.
- Design of additions to institutional LMS and other systems that leverage this information.

### References

Goldstein, P. (2005). [Key Findings. Academic Analytics: The Uses of Management Information and Technology in Higher Education](http://www.educause.edu/ir/library/pdf/EKF/EKF0508.pdf). ECAR Key Findings, EDUCASE Center for Aplied Research: 12.

Kimball, R. and M. Ross (2002). The data warehouse toolkit: The complete guide to dimensional modeling, John Wiley and Sons.

van Dyk, L. (2008). ["A data warehouse model for micro-level decision making in higher education."](http://www.ejel.org/Volume-6/v6-i3/vanDyk.pdf) The Electronic Journal of e-Learning 6(3): 235-244.