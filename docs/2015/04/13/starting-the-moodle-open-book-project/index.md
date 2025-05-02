---
title: Starting the \"Moodle open book\" project
date: 2015-04-13 22:09:57+10:00
categories: ['bad', 'moodleopenbook', 'openbook']
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: Rolley
      author_email: r.tickner@cqu.edu.au
      author_ip: 138.77.36.77
      author_url: http://rolleys.wordpress.com
      content: 'Great idea, and great project.  The first series of thoughts I have about
        using the Moodle Book module to do this, is; do you think it might be worth providing
        some affordances or improvements in the content creation process in part of this
        project?
    
    
        I think something might have to be done to improve with the way many people author
        their content in Moodle Books - at my institution most of the MBooks I''ve seen
        have content pasted in from Word, or other sources, and each page is full of junk
        HTML (to the point of even some times single letters of every word being wrapped
        in span tags!), they''re also almost always devoid of any proper semantics, with
        no real HTML structure at all (headings put in as paragraphs, or headings and
        paragraphs under a single paragraph tag, so on).  Problems associated with content
        authors not really knowing much about HTML.
    
    
        Maybe your process, or software, can take care of that for people, so that they
        don''t need to know anything about HTML semantics, but the process might allow
        them to identify structure to their content (in terms of where defining sections
        to articles, proper nested heading structure and so on), and it might apply the
        formatting and mark-up behind the scenes automatically?  I feel like it might
        lead to a better end product, and it might also make part of the technical aspects
        for redistribution, sharing and reuse a bit more streamlined.  Not sure. What
        do you reckon?'
      date: '2015-04-14 11:35:57'
      date_gmt: '2015-04-14 01:35:57'
      id: '1242'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: David Jones
      author_email: davidthomjones@gmail.com
      author_ip: 101.177.129.87
      author_url: https://djon.es/blog/
      content: "G'day Rolley,\n\nThanks for taking the time to comment.  Really useful\
        \ to get different perspectives, especially from different institutions and from\
        \ people with different backgrounds and perspectives.  Much appreciated.\n\nIs\
        \ the book module used much up there?  Might be interesting to see if my analysis\
        \ can be expanded to include your institution. May have to talk to you guys some\
        \ more.\n\nYou've identified one of the areas of contention and for further thought.\
        \ Also forces me to think a bit more about the \"philosophy\" of the approach\
        \ I'm taking.\n\nI'm trying to adopt a version of <a href=\"http://www.faqs.org/docs/artu/ch01s06.html\"\
        \ rel=\"nofollow\">the Unix Philosophy</a> in the design of the ecosystem.\n\n\
        I'm starting - somewhat strangely for many contexts - with the Moodle book because\
        \ that fits my context.  From there the plan is to - where ever possible - enable\
        \ the book module to take input from other programs and pass output to others.\n\
        \nIn this case the \"universal interface\" is likely to be HTML, JSON and related\
        \ technologies.\n\nBased on this approach, the current plan (which is likely to\
        \ change) is that for the book module to get better at importing HTML.  That was\
        \ the first change I made and it still needs some work.\n\nAt the moment, I'm\
        \ writing my HTML in vi with some classes to indicate chapters and sub-chapters.\
        \  That works for me, but won't scale beyond that as most people are going to\
        \ use Word.\n\nWhich does raise the two questions you've identified\n<ol> <li>\
        \ How do avoid/deal with the \"junk\" in some HTML? </li>\n  <li> How do you get\
        \ people to specify the various components of their \"books\"? </li>\n</ol>\n\n\
        These are perhaps some of the big problems facing this type of authoring process.\n\
        \n<h3>Current book solution</h3>\n\nAt the moment, the book import process supports\
        \ the import of a zip file that contains either a collection of separate HTML\
        \ files or separate folders.  The idea is that the separate files/folders become\
        \ the chapters and sub-chapters in the book.\n\nCurrent the book module doesn't\
        \ keep any sense of order for what's imported.  What you wrote as the first chapter\
        \ could be imported as the last chapter.  This was the thing I've tried to fix\
        \ first.\n\nMy current \"round-trip\" authoring process is\n<ol>\n  <Li> Create\
        \ the \"book\" as a HTML file on my computer using some specific classes to indicate\
        \ chapters and sub-chapters; </li>\n  <li> Run a Perl script locally the splits\
        \ the HTML files into separate files (in order) and creates a zip file to import\
        \ into the book module; </li>\n  <li> Import the zip file into the book module;\
        \ </li>\n  <li> Make ad hoc changes to the book during term in the book module;\
        \ </li>\n  <li> Next term, use the \"print this book\" option to produce a HTML\
        \ version of the book; </li>\n  <Li> Run the script over this HTML file to produce\
        \ a version of the HTML file from Step #1 - return to step #1 </li>\n</ol>\n\n\
        This will be the starting point.\n\n<h3>Potential evolution?</h3>\n\nSome potential\
        \ changes to this might include\n<ul>\n  <li> Being able to link the book module\
        \ to a github repository which becomes the holder of the authoritative source\
        \ for the book. </li>\n  <li> Write \"import processes\" for other authoring approaches.\n\
        \       <p>e.g. a Word template that chapters and sub-chapters (really just nested\
        \ pages).</p> </li>\n  <li> Add some sort of \"filter\" to the HTML import of\
        \ the book module to clean the HTML.\n       <p>The intent would be to use an\
        \ existing tool to do this and connect the book module to it.</p> </li>\n  <Li>\
        \ Add some sort of \"organise\" tool to the book module to allow people to specify\
        \ where the chapters/sub-chapters should go.\n       <p>This is essentially what\
        \ you've suggested in the last para. Not something I'd thought about previously.\
        \ Perhaps because this liable to be relatively difficult to implement from scratch\
        \ (and I don't need it personally), so it would be good if there was an existing\
        \ approach/tool to doing this.</p>\n      <p>It's an important step, because the\
        \ quality of the HTML coming in is going to be influence the quality of the ePub,\
        \ mobi etc format that's produced at the next step.</p>\n </li>\n  <Li> Add an\
        \ option to export the book in ePub or other \"book\" formats.\n        <p>Again,\
        \ the aim isn't to write the code for this, but for the book Module to be able\
        \ to produce the \"output\" that can be fed into an existing tool that will do\
        \ this.</p> </li>\n  <li> A broader tool to create collections of books that can\
        \ be exported.\n       <p>My course has 60+ books.  Most are quite small.  They\
        \ are probably better described as chapters or sections of chapters, than books.\
        \ At some stage, it would be useful to be able to group some or all of these chapters/sections\
        \ together as a single book.  Which means having a course level tool that could\
        \ allow me to specify which Moodle books to include and how to sequence them.\
        \  Once that's done pass them off to github or the epub producing tool</p>\n</ul>"
      date: '2015-04-14 17:29:12'
      date_gmt: '2015-04-14 07:29:12'
      id: '1243'
      parent: '1242'
      type: comment
      user_id: '1'
    
pingbacks:
    []
    
---
Back in February I shared [shared some thoughts](/blog2/2015/02/10/framing-an-open-book-as-situated-social-distributed-and-protean/) about some ideas for [grants for producing an "open textbook"](http://www.usq.edu.au/learning-teaching/excellence/landtgrants/OpenTextbooks) at my current institution. In the end, these thoughts were translated into an application which has just been officially announced as being successful. The following is my first attempt to get my head back into the project and outline

- what the project is about;
- the method being used;
- the likely product(s) to be produced;
- the aims and timelines; and,
- some other research that I hope might happen.

There's also an initial [project page](/blog2/the-moodle-open-book-module-project/).

## About the project

Rather use the funds to write an (is it at the stage of "yet another") open textbook. The project aims to develop a framework to enable the re-purposing of existing course materials as Open Educational Resources (OERs). In this context, "framework" is defined as "a collection of technologies, processes, and practices". The idea is to create and test a framework that others may be able to use to create their own OERs as part of producing their course websites.

[![1895 Duryea Horseless Carriage by pecooper98362, on Flickr](https://farm6.static.flickr.com/5510/11143803725_11c75a8ddc_m.jpg "1895 Duryea Horseless Carriage by pecooper98362, on Flickr")](https://www.flickr.com/photos/29261037@N02/11143803725/)  
[![Creative Commons Creative Commons Attribution-Noncommercial 2.0 Generic License](http://i.creativecommons.org/l/by-nc/2.0/80x15.png "Creative Commons Creative Commons Attribution-Noncommercial 2.0 Generic License")](http://creativecommons.org/licenses/by-nc/2.0/)   by  [](https://www.flickr.com/people/29261037@N02/)[pecooper98362](https://www.flickr.com/people/29261037@N02/) [](http://www.imagecodr.org/)

While this project has an initial focus on producing an "open textbook". I'm hoping the project will move beyond the limitations of the "book" metaphor. For me, an open textbook makes about as much sense as a horseless carriage. In fact, one of the aims of the project is to provide support in the framework for moving beyond an open textbook. For example, enabling the sharing of small bits of the "book", for that "sharing" to include more than just re-using the finished product, and move more into co-authoring etc.

The starting point (perhaps even core) of the framework will be the [Moodle book module](https://docs.moodle.org/22/en/Book_module). Moodle is the LMS used by my institution. As such it's the tool I use to teach a course that now consists of 60+ Moodle books. The framework will make it easier for me (and hopefully others) to use the Moodle book within the confines of a Moodle course and to produce OERs.

The framework is required because

1. the Moodle book module produces material that is not open; and,
    
    i.e. it only produces resources available from within Moodle. At my institution, this means that only students currently enrolled at the University and at some stage enrolled in the course can access the resources. I've had a couple of past students want to access material from the course, but beyond this the content can't easily be open and generate all the benefits that is meant to bring.
    
    Beyond getting access to the material the authoring model for the book module is not readily made open. It's hard to have the collection of books in EDC3100 benefit from the [residue of experience](/blog2/2014/08/15/joining-the-swarm-what-a-course-might-be/#residue) of past students. Currently, I attempt to modify the books based on questions and feedback from students. Would be useful to allow them to do it themselves.
    
    Beyond the students it would be useful for the material to benefit from the expertise of folk outside the course and to be used by them.
    
    From a slightly more institutionally insular perspective, it would also be useful for books to be easier to share and collaborated on between courses.
    
2. the Moodle book module could be enhanced.
    
    Round trip authoring with the Moodle book module [has some space for improvement](/blog2/2015/02/10/how-to-help-improve-the-moodle-book-module/).
    
    Even when students can still access the Moodle course site, [there are issues](/blog2/2014/08/15/joining-the-swarm-what-a-course-might-be/) around finding the information again. There is no search function. This is a frustration for students (and staff) at the moment.
    
    There's limited support for collections of Moodle books. For example, each week in my course takes the form of a "learning path". The Moodle books - typically at least 4 or 5 a week - outline the path. The current print function can only print a single chapter or all the chapters in a single book. There is no easy way to print a collection of books. Yes some students still want a print version of the information, even though much of it is in a form not conducive to print.
    
    Currently no apparent simple process for students (or teaching staff) to track student progress through books. At the moment, I'm advising students to bookmark the current page in a book if they have to do something else and haven't finished the book.
    

## Breaking BAD - the method

The project - like most of what I do - will be use an approach informed by a [BAD mindset](/blog2/2014/09/21/breaking-bad-to-bridge-the-realityrhetoric-chasm/#badset). That is:

- **B**ricolage;
    
    The focus is on solving existing problems with the tools at hand. i.e. the aim isn't to identify all the possible requirements, identify some wonderfully perfect future solution drawing on all the latest whiz-bang technology that requires radical transformation of existing practice. Instead, the aim is to address problems facing people right now with the tools that are available. Hence starting with the Moodle book module.
    
    There's questions to be asked about whether Moodle is the best place to start this type of project. There's questions to be asked whether the Moodle book module is the best Moodle module to base this project on. From a context-free perspective, the answers to these questions is almost certainly "no".
    
    However, the production of OERs is not a context-free task. From the context within which I set, the Moodle book module is the best place to start. How well it suits others we'll see. But chances are work on the Moodle book module will be useful to people already using Moodle and the book module.
    
- **A**ffordances; and,
    
    There are two parts to this. First, there's the more prosaic idea of leveraging the affordances offered by a range of available technologies to provide useful functionality. e.g. forging a link between the Moodle book module and github to offer version control functionality. Second - and perhaps more interestingly - is to harness the protean nature of digital technologies to modify the Moodle book module and its products to ensure that it's easier for any and all to remix it.
    
    I'm particularly interested in exploring how the protean nature of digital technologies can be merged with David Wiley's [Remix Hypothesis](http://opencontent.org/blog/archives/3813)
    
    > The Remix Hypothesis states that changes in students outcomes occurring in conjunction with OER adoption correlate positively with faculty remixing activities.
    
    Both in terms of the more standard - the project makes it easier for people (not just faculty) remix OER - but also the more interesting and challenging - the project makes it easier for people to remix the tool used to produce/remix the OER.
    
- **D**istribution.
    
    How the project might break down the hierarchical walls that inhibit remixing and learning will also potentially take many forms. Providing support for moving beyond the traditional hierarchical distinction between author and readers is one. Breaking down the hierarchical client/server abstraction behind Moodle (and most/all LMS) is another.
    

## Product(s)

The project will likely produce at least the following products:

1. software and documentation - under the GPL;
    
    This will most likely be mainly focused on changes to the Moodle book module (or something related). But may involve additional software. It will also include the necessary documentation etc. to support its use.
    
2. an open book/OERs based on the EDC3100 course material; and,
    
    The aim is that the software the project develops will enable the conversion of the course material (based on Moodle books) into OERs of various forms. The question of context specific information in the course material and how generic to make that information will be interesting to explore.
    
    It should also help the on-going maintenance of the material and perhaps lead to change in pedagogy.
    
3. presentations and publications.
    
    At the very least there will be a presentation proposed for [Moodlemoot'AU 2015](https://mootau15.moodlemoot.org/) reporting on initial analysis of Moodle book usage and functionality (see aim #1 in the next section), identifying potential changes, and asking for feedback and critique. There will also be required presentations at my current institution as part of the requirements of the grant.
    
    Beyond this there will be other research publications exploring various areas of interest (see a bit below).
    

## Aims and timelines

The project comes with four main aims with some associated timelines:

1. April to July 2015 - Explore the affordances and limitations of the Moodle book module for developing and maintaining OERs.
2. August to January 2016 - Develop a framework to enhance the affordances provided by the Moodle book module for developing and maintaining OERs.
3. December 2015 - Test the framework enhance the existing EDC3100 learning materials and produce an open book.
4. April to January 2016 - Commence and support the integration of this framework into the USQ and Moodle communities.

The timelines are specific to the grant. In reality, much of this is intended to continue post the grant. If only because I will be using the framework in my own teaching. Some details of what might be done to achieve each of the aims follow.

### Explore the affordances and limitations

The aim here is explore what people using the Moodle book module are missing and what they enjoy from the module. Also involves becoming more aware of the affordances that are available for producing an OER/open book in terms of broader technologies and practices.

1. Document the current process for producing EDC3100 "book".
2. Analysis of current USQ usage of Moodle book.
3. Exploration of Moodle book awareness and usage by USQ staff.
4. Exploration of usage of the Moodle book module amongst the broader Moodle community using a survey and analysis of existing discussions.
5. Analyse findings to identify broad areas for development.
6. Present findings at MoodleMoot'AU 2015 and at USQ and encourage feedback.

### Develop the framework

1. Identify and work with appropriate USQ stakeholders about the project and how to best achieve its aims.
2. Prioritise areas for change and commence development of the framework.

### Test the framework

Throughout the second half of 2015 the plan is to use the modified version of the book module in the courses that I'm responsible for. EDC3100 is a course I've been teaching for 4 years and has a range of existing resources. EDS4406 is a new course that is about to be developed and taught in the second half of 2015 for the first time. EDS4406 will be using much the same design as EDC3100 and is being developed by a course writer with some oversight.

Exactly how and what can be tested will depend on local negotiations. The main barrier will be if and how the latest version of the modified Moodle book module can be harnessed in a course that is being offered. There are good reasons why this will probably involve some workarounds to ensure minimum disruption.

By the end of 2015 the plan is to have at least the EDC3100 material (and hopefully EDS4406) available in ePub/mobi/PDF formats.

### Working with communities

1. Engage and contribute to the appropriate Moodle forums.
2. Present findings from the "explore affordances" aim at MoodleMoot'AU 2015. [Proposals](https://mootau15.moodlemoot.org/mod/page/view.php?id=35) due on 6th May.
3. Contribution of any changes the Moodle book module to the community.
4. Share project progress via social media and online development tools.
5. Presentation at USQ L&T grants showcase.
6. Production of final report, open book based on EDC3100 material, and materials for S1, 2016 offering of EDC3100.
7. Artifacts disseminated through the PLAS website and continue discussion regarding institutional-wide adoption of the framework

## Other research

Beyond seeking to make it easier to develop OERs via the Moodle book the project is also an opportunity to do a bit of small scale research into broader questions about the implementation of e-learning in universities and OERs. Some of the questions I want to explore

### What's the right balance between course specific and generic?

The EDC3100 books are specific to the course and its context. It references Moodle, assignments, Professional Experience and other concepts/practices etc that are specific to the institution. These limit the usability and usefulness of the OERs for people not withing that context.

What's the right balance between course specific and generic? Can you ever be generic? What implications would have course materials openly available have for pedagogy, for students, for the institution?

### Who is making changes to the LMS and why?

The Moodle book has been around for quite some time. I'm wondering how much its functionality has evolved over that time. Why? Who made the changes to the Moodle book module? What might be learned from answers to those questions about the evolution and practice of e-learning within Universities?

### How can you break BAD with the LMS? What's the impact and value of doing so?

We argued in [in this paper](/blog2/2014/09/21/breaking-bad-to-bridge-the-realityrhetoric-chasm/) that "teenage sex" problem with institutional e-learning is caused by the overwhelming use of the SET mindset to drive its implementation. This project is explicitly trying to use a BAD mindset to help. Can it be done? Or is as we identified in the paper, the overwhelming assumption of a SET mindset too strong to overcome? If it can be, does the BAD mindset help or hinder? What works, what doesn't? Why?

### Can the "remix hypothesis" and the 4Rs be applied to the systems, not just OERs?

The 4R framework (again from [David Wiley](http://opencontent.org/blog/archives/1123)) says that with OER you should be free to

> 1. Reuse - the right to reuse the content in its unaltered / verbatim form (e.g., make a digital copy of the content)
> 2. Revise - the right to adapt, adjust, modify, or alter the content itself (e.g., translate the content into another language or modify a learning activity)
> 3. Remix - the right to combine the original or revised content with other content to create something new (e.g., incorporate the content into a mashup)
> 4. Redistribute - the right to share copies of the original content, your revisions, or your remixes with others (e.g., give a copy of the content to a friend)

The technologies currently being used by institutions to implement e-learning - even open source systems like Moodle - are implemented in ways that limit use against the 4Rs. e.g. my experience is that if you **revise** the HTML generated by the LMS using JQuery or Greasemonkey you run the risk of being accused of being "dodgy" or "breaking policy". Instead of being open and protean, the digital technologies universities are using are closed (even if they are open source) and concrete in terms of what teachers and students are allowed to do with them.

I want break the concrete and explore the benefits of being protean.