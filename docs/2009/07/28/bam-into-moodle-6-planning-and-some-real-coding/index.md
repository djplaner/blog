---
categories:
- bam
date: 2009-07-28 11:27:24+10:00
next:
  text: '"BAM into Moodle #7 - an eStudyGuide block"'
  url: /blog/2009/07/28/bam-into-moodle-7-an-estudyguide-block/
previous:
  text: The intervention - Webfuse design 1996-1999
  url: /blog/2009/07/27/the-intervention-webfuse-design-1996-1999/
title: '"BAM into Moodle #6 - Planning and some real coding"'
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: 'BAM into Moodle #7 &#8211; an eStudyGuide block &laquo; The Weblog of (a)
        David Jones'
      author_email: null
      author_ip: 66.135.48.208
      author_url: https://djon.es/blog/2009/07/28/bam-into-moodle-7-an-estudyguide-block/
      content: '[...] The Weblog of (a) David Jones Another voice in the blogosphere    &laquo;
        BAM into Moodle #6 &#8211; Planning and some real&nbsp;coding [...]'
      date: '2009-07-28 15:48:27'
      date_gmt: '2009-07-28 05:48:27'
      id: '2667'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: 'BIM #1: Working on the prototype &laquo; The Weblog of (a) David Jones'
      author_email: null
      author_ip: 66.135.48.209
      author_url: https://djon.es/blog/2009/08/11/bim-1-working-on-the-prototype/
      content: '[...] A previous post outlined a list of tasks users will have to perform
        with BAM. Each of these will have to be integrated into the prototype and decisions
        made about how it will be implemented. In the following the tasks are divided
        into students, coordinator and teaching staff. [...]'
      date: '2009-08-11 14:31:21'
      date_gmt: '2009-08-11 04:31:21'
      id: '2668'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The [previous post](/blog/2009/07/23/bam-into-moodle-5-coding-a-block/) in this series started me along the lines of actually coding something in Moodle. It was only a pretend thing but indicated that blocks are fairly simple to implement. That previous post also pondered about the need to do some planning. Which brings me to the two main tasks for today

1. Put some rough planning down on "paper".  
    I still don't know enough about Moodle and its model to get into detailed planning. This planning will be a rough outline of the major tasks that need to be done to give me a heads up.
2. Start some real coding.  
    I need to develop my PHP/Moodle skills and real life tasks are the best way to do this - isn't this in keeping with the social constructionism (or is that constructivism) at the heart of Moodle - so I'm looking for useful blocks I can produce that help me develop the skills I need for BAM.

### Big up front design

Traditional software projects love to promote their rationality through their use of Big Up Front Design (BUFD). i.e. they gather all the requirements, analyse all the tasks and then come up with the perfect design. At this stage they can pass the design over to the lowly technicians who will implement the design.

Far from being rational, I'm a strong believer from both a theoretical and practice perspective, that BUFD is irrational, it's plan stupid, even insane. It doesn't have any basis in the cognition of people nor the nature of complex systems. It's an approach that is certain to fail.

So anyone looking for BUFD (and there will be a few) in this project is going to be disappointed. Actually, there's a chance some might be pleased, because for them the absence of BUFD will indicate that I'm "cowboy" coding, that I'm not being rational.

To put it simply, I don't know enough about Moodle to engage in BUFD. I doubt there is anyone at my current institution who knows enough about Moodle, BAM and how academics might like to use BAM. The aim of the next bit of planning is to allow me to identify the necessary tasks I need to undertake to increase my level of understanding. So, that at within the last steps of the project, I'll be able to develop a BUFD.

For a related perspective, have to love Dilbert (click on the cartoon to see a version you can read).

!!! warning "Broken image link"

### Planning

Some "planning" points

- BAM will not be part of the Moodle assignment system, it will integrate with it.  
    Currently, BAM is used mostly for assignments. Students post to their blogs in order to be marked and receive feedback. However, BAM is not a part of the assignment submission system at CQU. It does integrate with that system, but it's not part of it. I plan to continue this approach.
- One Moodle module with many activities  
    My current assumption is that I'll be able to implement a single Moodle module that will be able to provide each of the activities required to implement BAM. I suspect this will be possible, given Moodle's strong modular nature, but I don't know for certain.
- The main BAM activities  
    The following are a summary of the main activities that users will perform with BAM
    - Configure BAM for a course - Coordinator  
        The first step in using BAM is configuring it. This requires the coordinator to provide the following information:
        - Can students register their blog?
        - Should the student blogs be mirrored?
        - For each question the students have to respond to: question title, question body. _Addition:_ include some dates about when the question should be answered??
    - [Register blog with BAM](http://www.flickr.com/photos/david_jones/3268716454/in/set-72157608613577424/) - student  
        Having created a blog, the student provides a copy of their blog URL to BAM. BAM checks that it can find an RSS feed associated with that blog and also that the student hasn't made some common mistakes (e.g. registered the Wordpress home page/blog, rather than their individual blog)
    - Check progress - student  
        Visiting this page allows the student to check their progress with BAM on two fronts. First, what posts from their blog has BAM matched with the required questions (_Addition:_ maybe a good idea for BAM to show the questions). Second, they can see the marks and comments made by the markers. (_Addition:_ would be nice for the marks/comments to be able to be posted back to the students blog as comments - perhaps a step too far at the moment.
    - [Check progress](http://www.flickr.com/photos/david_jones/3268716654/in/set-72157608613577424/) - staff  
        Staff can see a page that lists all of their students and gives an indication of if they've registered their blogs, how many entries, when the last post was and a link to the live blog.
    - [Check student posts](http://www.flickr.com/photos/david_jones/3268716836/in/set-72157608613577424/) - staff  
        Similar to the above, but this one gives an overview of all the required questions and the status of the student's responses to those questions. This is the main starting place for the marking process.
    - [Mark a student post](http://www.flickr.com/photos/david_jones/3267891725/in/set-72157608613577424/) - staff  
        Usually linked to from the previous page (_Addition:_ would be good to provide a cooked RSS feed of student posts for markers. Each cooked item could include a link back to the mark a post activity. Would allow markers to use an RSS reader to keep up with student posts and then mark them from there)
    - Mirror blog entries - cron  
        At a configured time interval visit each the RSS feed for each individual student blog and, if updated save a new copy of the RSS feed on the Moodle server.
    - Modify student blog feed/posts - staff member  
        While BAM tries to match student posts to the required questions, it doesn't always work. This interface is for the marker to handle these problems. Essentially displays a list of all the student posts and whether or not they have been allocated to a question. Allows the marker to "de-allocate" a post or allocate it as the answer to a question.
    - Manage marking - coordinator  
        The coordinator of a course, based on CQU practice, needs to be able to manage if and when marks/comments are returned to the student. Depending on how Moodle works, the coordinator may also need to be able to manage which staff are marking which students. Personally, I'd like to avoid doing this.
    - Integrate with assignments - coordinator  
        Provide some form of control/management over how the data within BAM is integrated with assignments in Moodle.

### Functionality uncertainty

The following is an attempt to take the major user activities listed above and summarise the major functionality required to implement these as currently used in the Webfuse version of BAM. The point is that I probably don't know how to implement this functionality in Moodle/PHP or if it can be implemented. i.e. it's the stuff I need to learn.

- Configure BAM for a course  
    This will be a fairly standard web application. Present a form, allow the user to modify the form, store the data in a database. I don't see this being all that difficult. **Probably a good place to start with BAM coding.**
- Register blog with BAM  
    Fairly standard web application, however, once the blog URL is inserted/changed there are some additional tasks including:
    - Is the URL valid?
    - Does it exist? Can it be retrieved?
    - Does it have an attached RSS/Atom feed?  
        In Perl this is done using [LWP::Simple](http://search.cpan.org/search?query=LWP%3A%3ASimple&mode=all) to retrieve the file and [XML::Feed](http://search.cpan.org/search?query=XML%3A%3AFeed&mode=all) to check the resulting file to see if it has an attached feed and to discover what the URL for that feed is.
- Check progress - student  
    A simple web application, given the student's details, retrieve information from the database and display it for the student.
- Check progress - staff  
    Same as the above
- Check student posts  
    Same as the above
- Mark a student post  
    Same as the above
- Mirror blog entries  
    This is perhaps the most difficult one. It goes through each student blog in courses that are currently being mirrored and
    - Compares the feed against the one saved on disk. If no change, stop now. Otherwise
    - Parse the XML of the feed into internal data structures
    - Look through all the posts in the feed looking for new ones.
    - Compare each new post against the unanswered questions, if there's a match stick details in the marking database, ready for the marker.
- Modify student blog posts/answers  
    This one is also difficult as it shares a need to parse XML with Mirror and needs to compare that with the data in the database. Needs the XML parsing functionality.
- Manage marking - coordinator  
    Fairly straight forward web application. Need to identify if there are already ways in Moodle for storing this information.
- Integrate with assignments  
    Currently, this is essentially
    
    - Apply a formula to translate marks for each answer to a single mark result.
    - Copy that result to the assignment system database table.
    
    Need to find out how this works (the assignment database) in Moodle.
    

### Where to know?

Some specific technical questions to answer

- In Moodle/PHP, how do you retrieve remote documents over HTTP? Is there a LWP::Simple equivalent?
- In Moodle/PHP, how do you parse XML?
- Can a Moodle module support multiple activities?
- How does "integration" with the Moodle assignment system work?
- Exactly how do you code up a fairly standard database-backed web app/form in Moodle/PHP?

Have to come up with projects that let me learn the answers to those questions.