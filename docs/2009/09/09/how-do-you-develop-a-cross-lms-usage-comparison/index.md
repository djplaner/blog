---
title: How do you develop a cross-LMS usage comparison?
date: 2009-09-09 15:59:10+10:00
categories: ['chapter-5', 'design-theory', 'elearning', 'evaluation', 'indicators', 'lmsevaluation', 'phd', 'thesis']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

I [recently posted](/blog2/2009/08/28/comparisons-between-lms-the-need-for-system-independence/) about the need to develop an approach that allows for the simple and consistent comparison of usage and feature adoption between different Learning Management Systems (aka LMS, Virtual Learning Environments - VLEs - see [What is an LMS?](/blog2/2009/08/21/what-is-an-lms/)). That [last post on the need](/blog2/2009/08/28/comparisons-between-lms-the-need-for-system-independence/) didn't really establish the need. The aim of this post is to explain the need and make some first steps in identifying how you might go about enabling this sort of comparison.

The main aim is to get my colleagues in this project thinking and writing about what they think we should and how we might do it.

### What are you talking about?

Just to be clear, what I'm trying to get at is a simple method by which University X can compare how its staff and students are using its LMS with usage at University Y. The LMS at University Y might be different to that at University X. It might be the same.

They might find out that more students use discussion forums at University X. More courses at University Y might use quizzes. The could compare the number of times students visit course sites, or whether there is a correlation between contributions to a discussion forum and final grade.

### Why?

The main reason is so that the university, its management, staff, students and stakeholders have some idea about how the system is being used. Especially in comparison with other universities or LMSes. This information could be used to guide decision making, identify areas for further investigation, as input into professional development programs or curriculum design projects, comparison and selection processes for a new LMS, and many other decisions.

There is a [research project](http://ceise.iscap.ipp.pt/lmsproj/) coming out of Portugal that has [some additional questions](http://ceise.iscap.ipp.pt/lmsproj/index.php?option=com_content&view=article&id=49&Itemid=53) that are somewhat related.

The main reason is that there currently appears to be no simple, effective method for comparing LMS usage between systems and institutions. The different assumptions, terms and models used by systems and institutions get in the way of appropriate comparisons.

### How might it work?

At the moment, I am thinking that you need the following:

- a model;  
    An cross-platform representation of the data required to do the comparison. In the [last post](/blog2/2009/08/28/comparisons-between-lms-the-need-for-system-independence/) the model by Malikowski et al (2007) was mentioned. It's a good start, but has doesn't cover everything.
    
    As a first crack the model might include the following sets of information:
    
    - LMS usage data;  
        Information about the visits, downloads, posts, replies, quiz attempts etc. This would have to be identified by tool because what you do with a file is different from a discussion forum, from a quiz etc.
    - course site data;  
        For each course, how many files, is there a discussion forum, what discipline is the course, who are the staff, how many students etc.
    - student characteristics data;  
        How were they studying, distance education, on-campus. How old were they?
- a format;  
    The model has to be in an electronic format that can be manipulated by software. The format would have to enable all the comparisons and analysis desired but maintain anonymity of the individuals and the courses.
- conversion scripts; and  
    i.e. an automated way to take institutional and LMS data stick it into the format. Conversion scripts are likely to be based around LMS and perhaps student records system. e.g. a Moodle conversion script could be used by all the institutions using Moodle.
- comparison/analysis scripts/code.  
    Whatever code/systems are required to take the information in the format and generate reports etc. that help inform decision making.

#### Format

I can hear some IT folk crying out for a data warehouse to be used as the format. The trouble is that there are different data warehouses and not all institution's would have them. I believe you'd want to initially aim for a lowest common denominator, have the data in that and then allow further customisation if desired.

When it comes to the storage, manipulation and retrieval of this sort of data, I'm assuming that a relational database is the most appropriate lowest common denominator. This suggests that the initial "format" would be an SQL schema.

### How would you do it?

There are two basic approaches to developing something like this:

- big up front design; or  
    Spend years analysing everything you might want to include, spend more time designing the perfect system and finally get it ready for use. Commonly used in most information technology projects and I personally think it's only appropriate for a very small subset of projects.
- agile/emergent development.  
    Identify the smallest bit of meaningful work you can do. Do that in a way that is flexible and easy to change. Get people using it. Learn from both doing it and using it to inform the next iteration.

In our case, we've already done some work from two different systems for two different needs. I think discussion forums are shaping up as the next space we both need to look at, again for different reasons. So, my suggestion would be focus on discussion forums and try the following process:

- literature review;  
    Gather the literature and systems that have been written analysing discussion forums. Both L&T and external. Establish what data they require to perform their analysis.
- systems analysis;  
    Look at the various discussion forum systems we have access to and identify what data they store.
- synthesize;  
    Combine all the requirements from the first two steps into some meaningful collection.
- peer review;  
    If possible get people who know something to look at it.
- design a database;  
    Take the "model" and turn it into a "format".
- populate the database;  
    Write some conversion scripts that will take data form the existing LMSes we're examining and populate the database.
- do some analysis;  
    Draw on the literature review to identify the types of analysis/comparison that would be meaningful. Write scripts to perform that role.
- reflect on what worked and repeat;  
    Tweak the above on the basis of what we've learned.
- publish;  
    Get what we've done out in the literature/blogosphere for further comment and criticism.
- attempt to gather partners.  
    While we can compare two or three different LMS within the one institution. The next obvious step would be to work with some other institutions and see what insights they can share.

The knowledge and experience gained this for "discussion forums" could then be used to move onto other aspects.

### What next?

We probably need to look at the following:

- See if we can generate some outside interest.
- Tweak the above ideas to get something usable.
- Gather and share a bibliography of papers/work around analysing discussion forum participation.
- Examine the discussion forum data/schema for Blackboard 6.3 and Webfuse.

That's probably enough to be getting on about.

### References

Malikowski, S., M. Thompson, et al. (2007). "A model for research into course management systems: bridging technology and learning theory." Journal of Educational Computing Research 36(2): 149-173.