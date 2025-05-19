---
categories:
- bam
date: 2009-07-28 15:48:14+10:00
next:
  text: The design and implementation of Webfuse - Part 1
  url: /blog/2009/07/29/the-design-and-implementation-of-webfuse-part-1/
previous:
  text: 'BAM into Moodle #6 - Planning and some real coding'
  url: /blog/2009/07/28/bam-into-moodle-6-planning-and-some-real-coding/
title: '"BAM into Moodle #7 - an eStudyGuide block"'
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: VRBones
      author_email: vrbones@hotmail.com
      author_ip: 115.64.241.18
      author_url: http://www.vrbones.com
      content: Did you settle on an IDE or are you using a text editor?
      date: '2009-07-29 18:46:32'
      date_gmt: '2009-07-29 08:46:32'
      id: '2669'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: davidtjones
      author_email: d.jones@cqu.edu.au
      author_ip: 59.154.24.147
      author_url: https://djon.es/blog/
      content: 'I''m a vi kind of guy.
    
    
        With the size of the code I''m developing, I don''t really see the need for an
        IDE.  But then I have a lot of tacit knowledge around vi and web development -
        so comfort level is high with that approach.'
      date: '2009-07-29 18:58:37'
      date_gmt: '2009-07-29 08:58:37'
      id: '2670'
      parent: '2669'
      type: comment
      user_id: '1'
    
pingbacks:
    - approved: '1'
      author: 'BAM into Moodle #8 &#8211; finishing the eStudyGuide building block &laquo;
        The Weblog of (a) David Jones'
      author_email: null
      author_ip: 72.233.96.141
      author_url: https://djon.es/blog/2009/07/30/bam-into-moodle-8-finishing-the-estudyguide-building-block/
      content: '[...] into Moodle #8 &#8211; finishing the eStudyGuide building&nbsp;block  The
        last post in this series described the start of a little project to learn more
        about PHP/Moodle programming [...]'
      date: '2009-07-30 11:39:06'
      date_gmt: '2009-07-30 01:39:06'
      id: '2671'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: BIM &#8211; Saving/manipulating RSS files &laquo; The Weblog of (a) David
        Jones
      author_email: null
      author_ip: 66.135.48.164
      author_url: https://djon.es/blog/2009/12/20/bim-savingmanipulating-rss-files/
      content: '[...] had originally found the magpie rss library. However, it now appears
        that Magpie is deprecated and SimplePie is [...]'
      date: '2009-12-20 18:03:46'
      date_gmt: '2009-12-20 08:03:46'
      id: '2672'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: The VLE model and the wrong level of abstraction &laquo; The Weblog of (a)
        David Jones
      author_email: null
      author_ip: 74.200.247.239
      author_url: https://djon.es/blog/2010/07/04/the-vle-model-and-the-wrong-level-of-abstraction/
      content: '[...] example of what I mean here is the CQU eStudyGuide Moodle block
        I played with last year. Some brief [...]'
      date: '2010-07-04 10:24:45'
      date_gmt: '2010-07-04 00:24:45'
      id: '2673'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The [last post](/blog/2009/07/28/bam-into-moodle-6-planning-and-some-real-coding/) provided an overview of what is required to put BAM into Moodle and generated a list of things I have to learn in order to implement it.

This post will tell at least some of the story of developing my first CQU Moodle block. Whether the block ever gets used in action, is beside the point. The main aim is to give me the opportunity to engage in a bit of [constructionism](http://en.wikipedia.org/wiki/Constructionist_learning). In particular, the block I've decided to have a crack at will help me learn answers to the following questions developed at the end of the [last post](/blog/2009/07/28/bam-into-moodle-6-planning-and-some-real-coding/).

- In Moodle/PHP, how do you retrieve remote documents over HTTP? Is there a LWP::Simple equivalent?
- In Moodle/PHP, how do you parse XML?

### Introducing the eStudyGuide block

[CQU](http://www.cqu.edu.au/) has a history that includes a significant investment in print-based distance education ("The institution" section in [this post](/blog/2009/07/26/build-it-and-they-will-come-starting-with-the-institution/) offers some background). That means that this year there are at least 10,500 students enrolled at CQU studying by distance education. For many of those students the primary scaffolding of their study, which occurs off-campus, is a study guide. A print based guide written by CQU staff that summarises what they should read and do each week.

For the last couple of years [CDDU](http://cddu.cqu.edu.au/) has been working on a [variety of innovations](http://cddu.cqu.edu.au/index.php/Print_material_innovation) around these study guides. Including developing a process that produces better quality versions of study guide in both hard copy and online. Some work has been done to integrate the online study guides with the VLEs used by CQU. However, the institution has now adopted Moodle and while there is a level of integration, it's not great.

The aim here is to develop a Moodle block (an eStudyGuide block) that allows the online version of a CQU study guide to be added to a course.

Strictly speaking the online study guide should be included in the main guts of the course home page, not as a block. But the aim here is learn more while producing something reasonably useful, without wasting too much time.

### Functionality

The eStudyGuide block will display a bit of HTML that will provide a list of links to each module/chapter of the study guide. The PDFs of the study guide will be stored on a remote web server. When the block is added to the course site it will need to:

- Identify the course, period and year associated with the current course.  
    I believe that CQU currently uses the format
    
    ```
    COIS20025_2092
    ```
    
    for Moodle courses. This translates into the Term 2, 2009 offering of the course COIS20025.
- Formulate the URL of the folder containing the e-study guide.  
    This will be
    
    ```
    $BASE_URL/Guides/$YEAR/$PERIOD/$COURSE/
    ```
    
- Check that the folder/URL exists.
- Retrieve and parse the XML file that details the study guide.  
    The XML file is produced by InDesign, the publishing system used to generate the guides. It contains information such as the number of chapters/modules, the names of the files, the titles of each module/chapter etc.
    
    The XML file will be protected by Basic AUTH so it will need to authenticate before getting the XML file.
    
- Generate a list of links to each module/chapter.  
    Initially these will be just straight URLs.

### The development process

The following tells the story of the process I used to put the block together, it may not be complete, but includes the following steps:

- Create a dummy eStudyGuide block that generates dummy HTML. **DONE**
- Add in a global configuration for the block for the BASE\_URL for the files. **DONE**
- Get it to parse the CQU Moodle course format and use the new URL in the static HTML generated. **DONE**
- Get it to retrieve the XML file.
- Get it to parse the XML file.
- Dynamically generate the HTML.

#### Getting a dummy eStudyGuide block

[BAM into Moodle post #5](/blog/2009/07/23/bam-into-moodle-5-coding-a-block/) details some of the mechanics for this process and it in turn draws heavily on [this page on the Moodle site](http://docs.moodle.org/en/Development:Blocks)

The process goes something like this:

- Create the dummy block\_estudy\_guide.html file using the template on the Moodle site.
- Login to Moodle, click on notifications, dummy estudy\_guide up and going, eStudyGuide block added to course
- No need to add configure options for the block, in real life the block will get the course code from some variables, there's nothing to configure.
- Add a specialization function to set the title.  
    Eventually the title will include the course code, which is set from variables. To set the title this way we need the specialization function. Set this to a constant for now. Will replace this with the real course code in a later stage.
- Add in the global configuration data.  
    In this case the BASE\_URL for the location of the eStudyGuides on the external website. Needs a file with the HTML/form for the configuration, at this stage BASE\_URL. **Done:** config is even saving from action to action.
    
    Had some trouble using the global configuration data in the instance, turned out I needed the
    
    ```
    global
    ```
    
    PHP statement to bring the
    
    ```
    $CFG
    ```
    
    variable into scope.
- Create HTML guide links  
    Going to do this by creating a hard coded associative array and a for loop. The idea being is that eventually the parsed XML will replace the hard coding.
- Convert to using block\_list - not done for now  
    Moodle's block abstraction includes a special case where the block is used to display a list. Where each item has it's own image. I don't have easy access to an image set. **Addition:** Talk to Rolley about the idea of a specific image.

#### Parse the CQU course format

The task here is to get the Moodle course ID/code, assume it's in CQU format and parse it into it's constitute parts.

- Where is the course variable?  
    I'm assuming this is a global variable which is discussed [here](http://dev.moodle.org/mod/resource/view.php?id=35) in the Moodle programming course. Ahh, there's a global $COURSE with
    
    ```
    $COURSE->id
    ```
    
    being the Moodle ID, but there's also entries for fullname, shortname. Assume id.
- Modify the block to use this in the title.  
    Ahh, id is the unique number id. What about shortname? That seems to be the one. At least until further confirmation.
    
    Need to look at REs etc in PHP. Okay, that's over. Difficult getting use to the slightly new approaches.
    
- Parse the format and stick in content variables - done.

#### Retrieving the XML file

Now the interesting stuff.

- Get the full path format for the XML file  
    Currently it's _BASE\_URL/Guides/YEAR/PERIOD/COURSE/eStudyGuide/COURSE.xml_
- Find out how to retrieve files over HTTP within Moodle/PHP  
    Well, using [xref](http://xref.moodle.org/) it's possible to see within lib **phpxml** - probably useful for XML parsing. Couldn't see anything else useful.
    
    Looking through existing modules might be useful. There's a flickr module that uses a class called RSSCache - which looks very interesting. Which is included as part of the [magpie RSS parser](http://magpierss.sourceforge.net/). This came with the default install of Moodle - so one problem solved for the broader BAM project.
    

And that's where I have to leave it. Haven't found the retrieval mechanism. But once I have it, should be straight forward.