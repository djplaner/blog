---
title: Reflections and Implications from Webfuse - Domain languages
date: 2009-01-07 16:32:13+10:00
categories: ['paperideas', 'webfusereflectionsimplications']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

As I am currently [writing up the PhD](/blog2/research/phd-thesis/) I have banned myself from working on any new papers. However, as I work through the PhD I will get ideas for papers so rather than waste time writing them in full and even worse forget about them I'm going to try and write about them on the blog and categorise them appropriately. With the hope that post PhD I can come back and have a large collection of papers to write. Alternatively, I'll have a collection of dribble to laugh at.

First cab off the rank is the idea of a "webfuse reflections and implications" paper. To some extent this would come from the last chapter of my thesis and capture some of the lessons, reflections etc learned from the 12 or so years working on the thesis and Webfuse (the artifact that arose from/created the thesis).

In part the idea for this paper is to capture the messy bits that you have to solve in practice that are typically overlooked by researchers and the enterprise folk implementing e-learning. The hope is that these reflections/implications could spark off ideas for future research projects.

Some of the initial ideas which will be expanded upon include

- Domain langauges and the mismatch between enterprise software and institutional practice.
- The need for "loose joining" between e-learning systems and other institutional databases.
- Limitations of traditional IT governance and other forms of hierarchical division of labour and responsibilities.

### Domain languages and LMS mismatches

The idea for this one was sparked by [this post on iPhoto and Domain Languages](http://www.37signals.com/svn/posts/1507-iphoto-09-and-domain-language) and some [previous work](/blog2/publications/how-to-live-with-erp-systems-and-thrive/).

The definition of domain language [given on the 37signals blog](http://www.37signals.com/svn/posts/1507-iphoto-09-and-domain-language) is

> A domain language is the set of words that reflect the way you cut up a domain. It consists of the pieces you sliced and the names you chose to give them. This language defines an application and makes it special.

Universities have domain languages. Actually, university sectors in different countries have different domain languages and to some extent different universities within the same country can have different domain languages.

For example, in the mid-1990s the institution I worked at then had a domain language that consisted of the following terms

- Unit - an individual course/subject that a student enrols in (e.g. Programming I etc.)
- Course - a collection of units that make up a student's entire study for a degree (e.g. bachelor of information technology).
- Student number - the unique identifying number (actually combination of letters and numbers) for a particular student (e.g. C0101010X)

As the 37signals post suggests software applications have to encapsulate a domain language. The designers of those applications have to make choices about how they divide up the application space, what objects are sensible and what to call those objects.

Around the turn of the century the institution I worked with adopted the Peoplesoft enterprise resource planning (ERP) system for some aspects of its work, in particular its student administration system. Peoplesoft is from the North American university sector and had a domain language that made sense for that sector. It also originally started in the Human Resource management sphere and so aspects of its domain language showed its origins.

For example, the institution, its students and staff had to change the language they used from the above to the following

- Unit became Course.  
    This re-use of a term that meant something completely different in the previous domain language was particular confusing.
- Course became Program.
- Student number, while still used in normal conversation, became EMPLID (emploee ID) in the database and some aspects of the interface.

The change in domain language made the adoption of the software more difficult. It required significant changes to a broad array of practices and documentation that normally would not have been required. It also resulted in my institution (and the others who adopted Peoplesoft) started using a domain language that was different from many other Australian universities.

The Blackboard e-learning system we've been using over the last few years has also show this sort of problem. The main one has been the difference between the names given to teaching staff.