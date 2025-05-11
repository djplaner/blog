---
categories:
- indicators
- moodle
date: 2010-05-17 10:07:02+10:00
next:
  text: How curriculum mapping in Moodle might work
  url: /blog2/2010/05/19/how-curriculum-mapping-in-moodle-might-work/
previous:
  text: Is there more to communities of practice?
  url: /blog2/2010/05/16/is-there-more-to-communities-of-practice/
title: Moving the indicators Moodle block to a factory class
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: The Wf Framework &laquo; The Weblog of (a) David Jones
      author_email: null
      author_ip: 66.135.48.150
      author_url: https://djon.es/blog/2010/06/07/the-wf-framework/
      content: '[...] You can see the impact of this experience in the development practices
        I&#8217;m bringing to my work in PHP and Moodle. There are early glimmers of MVC
        and the Wf Framework in BIM and the indicators block. [...]'
      date: '2010-06-07 10:04:48'
      date_gmt: '2010-06-07 00:04:48'
      id: '3049'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The following reports on some work on the [indicators block](/blog2/2010/05/13/getting-started-with-cols-indicators-block/) to move it towards using some object-orientation and the [factory design pattern](http://en.wikipedia.org/wiki/Factory_method_pattern).

### Why?

One of the requirements we've talked about for the indicators block was the ability to show many different "indicators" (visualisations of something important about learning and teaching within a Moodle course). The idea is that the individual user could either scroll through the different visualisations or they could configure it to show a subset that they are interested in. Some examples of indicators that are already out there which might be included are:

- An effort meter;  
    This is what the block currently shows. It's closely related to the [Moodle meter idea](http://lewiscarr.co.uk/node/12) of [Lewis Carr](http://lewiscarr.co.uk/). To the extent that both the meter and the current indicator both use Google's chart API for the graphics. Though the meter appears to place users into four groups. The indicators block currently uses a straight numeric scale.
- Traffic lights;  
    Purdue University has [used traffic lights](http://www.ecampusnews.com/technologies/tech-helps-students-adopt-good-study-habits-2/) to represent students' standing in a class. This is a little bit like [Michael de Raadt's](http://www.sci.usq.edu.au/staff/deraadt/index.html) Moodle [progress bar block](http://www.sci.usq.edu.au/staff/deraadt/progressBar.html), at least in terms of helping students visualise their progress, this time within a course.
- Network visualisations of connections;  
    The [SNAPP](http://ceit.uq.edu.au/content/snapp-group) project is the main example of this I know. Visualise the network of interactions between participants in a discussion forum.
- Waterfall visualisation;  
    This comes [from work](http://opencontent.org/blog/archives/1286) done by David Wiley and his students. It's connected to the traffic lights/progress bar idea, but is focused more on showing student progress to the teacher. Allowing the teacher to see which students are struggling or not.

The last one is somewhat connected to a visualisation that Col has been working on. He describes the rationale and the approach in [this blog post](http://beerc.wordpress.com/2010/05/14/using-the-indicators-project-data-to-identify-at-risk-students/). More on that later.

Are there any other ideas for visualisations?

### What?

Given the aim is to include multiple visualisations and we do want people to be able to add their own to the block, we need to have a clean way of separating the code for the different indicators. This is what the factory design pattern does.

The idea of the factory pattern is that you want the code for the different indicators to be separated out. These indicators are different, but they all do essentially the same task (look at the LMS data and generate some visualisation). The decision about which of the indicators you want to show to the user is a fairly complex decision. In terms of the indicators this decision will eventually need to consider:

- What type of user is this?  
    Students and staff will be able to see different indicators.
- How has the user configured the indicators block?
- Based on the above, which indicator should we show?

The initial version of the block had the decision about which indicator to show and the code for both indicators (staff and student) combined into the one function. A bit messy with two. Have 6 or 7 and it would've been a nightmare.

With the factory design pattern, the guts of the block's main function looks like this.

\[sourcecode lang="php"\] // get details about the context $context = get\_context\_instance(CONTEXT\_COURSE, $SESSION->cal\_course\_referer);

// create the correct indicator $indicator = IndicatorFactory::create($context); // use the indicator to generate the HTML to put in the block $this->content->text = $indicator->generateText(); \[/sourcecode\]

There's a class called `IndicatorFactory` which when given the current context decides which indicator should be used. The factory then constructs the right indicator and returns it.

All indicators simply generate the "text" that is placed in the block. So we call the indicators generateText function and we're done.

All the `IndicatorFactory` class does at the moment is look at the type of user. If the user is a teacher, then it creates an object of the class `staffActivity`. If it is a student, it creates an object of class `studentActivity`

\[sourcecode lang="php"\] if ( has\_capability( 'moodle/legacy:teacher', $context ) || has\_capability( 'moodle/legacy:editingteacher', $context ) ) { require\_once( $CFG->dirroot.'/blocks/indicators/staff/staffActivity.php'); return new staffActivity; } else if ( has\_capability( 'moodle/legacy:student', $context ) ) { require\_once( $CFG->dirroot.'/blocks/indicators/student/studentActivity.php'); return new studentActivity; } \[/sourcecode\]

Both the "activity" classes contain the SQL statements, a bit of maths and the call to the Google charts API that was necessary to generate the particular visualisation. Both of the "activity" classes extend the abstract class `Indicator`. The idea is that for each of the above indicators we implement, each one will have its own class that extends the `Indicator` class.

### What's next

This has laid the foundation for having multiple indicators for each user category. The next step might include:

- How will users move between different indicators?  
    One idea is that there are left and right arrows at the bottom of the indicators that allow the user to scroll through the available indicators. Have other Moodle blocks done this? How? Does this mean a refresh of the entire page or do we do some HTML trickery?
    
    Alternatively, do we randomly (or sequentially) show the indicators everytime the page is refreshed? Do we build some smarts into the Indicators block so that at certain times or based on certain events it shows specific indicators first? For example, in the day or two leading up to an assignment due date it might show the percentage of students who have submitted and those that haven't.
    
- How will users be able to configure which indicators they are interested in?  
    Eventually (not right now) we may want to allow the users to configure which ones they are interested in.
- Can we improve the current indicators?  
    For example, some of the SQL for the student activity indicator users "roleid=5" to indicate a student. I think this is deprecated.
- Do we need to and how will we "cache" the data required for the indicators?  
    At the moment, both indicators query the database every time the block is shown. In a large installation this could lead to some performance problems. Eventually, we will need to look at an approach to "caching" to reduce the performance hit.
- Do we need to move to a model/view pattern for the indicators?  
    Are we going to want the one set of data around an indicator to be visualised in many different ways? SNAPP already does this with the different types of network visualisation it supports. If so, we may wish to split the indicators into a model (calculate the data) and view (visualise it) objects.
- How do we support bigger indicators?  
    SNAPP visualisations are probably not going to fit within a block. Especially if we're talking about building on SNAPP by enabling visualisations of discussion forums across a range of courses, not just the current one. How do support indicators that need quite large areas? A popup? A new page? What's the Moodle way? What's the cool way?
- Are there other visualisation tools?  
    The Google chart API looks like a good, low impact way of doing visualisations. But it might not provide everything we need. Are there other alternatives?