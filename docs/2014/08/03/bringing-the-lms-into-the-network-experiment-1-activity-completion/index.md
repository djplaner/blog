---
title: "Bringing the LMS into the network - Experiment # 1 - Activity completion"
date: 2014-08-03 22:46:59+10:00
categories: ['bad', 'bricolage']
type: post
template: blog-post.html
---
The following is the first step in an attempt to modify the [Moodle Activity Viewer](http://damosworld.wordpress.com/2013/08/30/the-moodle-activity-viewer-mav-heatmaps-of-student-activity/) (or at least a local instance). I'd like a modified version of MAV to allow me to

1. find out how students are progressing with activity completion.
    
    Rather than use clicks (as MAV does currently) to track student usage, use activity completion. I use this in EDC3100, however, activity completion isn't even turned on at the Moodle level at the other institution.
    
2. Easily display additional information about students as a roll-over/popup for any links to a student profile page.

The following is an initial exploration of how MAV works and what changes I'll need to kludge it to work within the local constraints.

It starts with a description of how this is going to work, follows with some initial explorations getting MAV to work within my browser, an exploration of how MAV actually does this and some initial explorations of the changes I'll have to make. It finishes with some suggestions for the next step.

### All as a local instance

First constraint is that this is all being done as a local instance. I'll be the only one who can see it when I'm using my laptop. It will work something like this

- I have MAV installed on a version of the Firefox browser.
- When I visit one of my institutional Moodle course sites MAV will recognise this and as a result will
    - Send a query to a web server running on my laptop asking for activity completion (and other) data for all, some or one student.
    - The web server on my laptop will query a database on my laptop that contains a copy of the activity completion data for my courses and send a reply back to Firefox/MAV.
    - On receipt of the reply Firefox/MAV will update the display of my course site to colour code the activities based on how many student(s) have completed the activity.

The reliance on my laptop and a local database is due to the difficulty of making connections to the institutional servers/data.

From a "theoretical" perspective, this is part of our argument that the LMS is not a full fledged member of networked learning. It's too hard to make new connections to the LMS to enable new learning. MAV and local databases are an attempt to make it easier to connect to the LMS and its large number of individual parts. The theory is that by making this easier, it is easier to innovate and encourage the development of more interesting learning that is more used.

### MAV recognising institutional LMS page

First some documentation on MAV and how it works

The local mav code is /usr/local/www/mav and /usr/local/www/smarty

MAV has to separate servers it knows about

- balmiServer - this will be my local laptop
- Moodle Server - this is the institutional LMS
    
    **POINT:** Would be interesting to see if this could be multiple servers? e.g. when I want it to work on both my local Moodle server and the institution one
    

These are set in ~/mav/gmdocs. Set it to http://usqstudydesk.usq.edu.au/m2

Go to this link http://localhost/fred/mav/gm/moodleActivityViewer.user.js and install the updated version of MAV

That seems to working. Getting at least some information dumped into the console. Seems to be breaking on a call to balmi.getLoggedInUserIDNumber() --- moodleActivityViewere.user.js 1199

Ahh, seems the USQ study desk has an extra bread crumb in the list that breaks the code. Modify the code in balmi.user.js and all is good.

**getMoodleLinks**

balmi.user.js has a function getMoodleLinks that extracts all the Moodle type links from the page. This includes setting up some regular expressions to do the extraction.

_Change:_ the RE needs to be updated for my institutional Moodle. Also another RE replacement a little further down for link name.

### How does MAV work?

Try to nut out the process MAV uses and identify what possible changes I'll need to make for both the activity completion and also the student information idea.

The client runs the GreaseMonkey script ~/mav/gmdocs/moodleActivityView.user.js installed on Firefox. It starts off and calls.

- balmi.getCoursePageLink - Will only run MAV is the page is a valid Moodle page.
    
    Looks for the Moodle breadcrumbs and extracts the course id.
    
    **CHANGE:** this is where I could hard code the detection of my courses and also do the translation between the course ID on the USQ Moodle server and the course ID on the Moodle server on my laptop.
    
    If not what MAV is looking (getCoursePageLink returns NULL) for MAV exits.
    
- moodleActivityView.user.js - does a range of set up prep. Adding the MAV interface etc.
    
    **CHANGE:** Some of these will need to change based on what I want to be able to do.
    
- Adds mavUpdatePage function as a listener for the load page event - i.e. this is what updates the page.
- mavUpdatePage does some debug stuff and then calls
- generateJSONRequest - generate the particular request to send to the MAV server in JSON
    - balmi.user.js - balmi.getCoursePageLink() - _A duplicate call_
    - balmi.user.js - balmi.getMoodleLinks
        
        get's all the links that are part of a Moodle course page. This is for the activity tracking.
        
        returns data of the form
        
        > "/mod/forum/view.php?id=12345": \["forum","view.php?id=12345"\]
        
        **CHANGE:** For activity completion the aim here will be to return the links only for value Moodle activities.
        
        **CHANGE:** For the user details option, looking at returning the links to user details.
        
    - Filters out a range of links that shouldn't be included
    - calls requestData - actually makes the request
- updatePage - takes the data returned from the MAV server and updates the links. Either through increasing font size of changing the background colour of the links.
    
    **CHANGE:** the activity completion will be closest to a version of the number of students. Rather than the number of students who clicked on the link, it will be the number of students who completed the activity.
    
    Has a loop that goes through all the links in the page. If they link matches something that's come back from the MAV server, then make the change.
    

The server is implemented using ~/mav/phpdocs/api/getActivity.php - processes the request

- decodes and logs the request
- getCourseIdFromCourseHomePageLink - extracts the course id which is used to query the Moodle database
- SQL to count # student in course
    
    **CHANGE:** Not needed for the student ID stuff.
    
- Checks to see if the user wants # clicks or # students and whether just for an individual student, a group(s) or all.
    
    **CHANGE:** Again not needed for student details.
    
- Calls ~/mav/lib/generateSQLQuery'generateSQLQuery - just a wrapper around a fairly standard PHP template for dynamically generated SQL.
    
    The template is in ~/mav/lib/getActivityQueryTemplate.php This uses a range of PHP code to generate the appropriate SQL query to extract the stats per link
    
    **CHANGE:** the activity completion modifications could be implemented in here. Fairly similar to the S approach, but using activity completion rather than the Moodle log tables.
    
- Processes the query for each link, placing the results into a data structure
- Constructs the JSON object to send back to the browser.
    
    **CHANGE:** This is where my kludge will have to translate the student and activity ids returned by the SQL into the values that are being used on the USQ Moodle server and are thus what the browser will find embedded in the HTML.
    

### Approach for changes

Separate clients and servers for the two approaches. Perhaps modify the existing for activity completion, but still do this separate from the existing MAV stuff so I have a clean copy? Definitely have to put this under git.

Questions

1. What's the format for links to the student profile? Does it use the Moodle user id?
    
    Basically a link to the script _user/view.php_ with the user's id and the course id as parameters.
    
    ```html <a href="~/user/view.php?id=USERID&course=COURSEID">Fred Nerf</a> ```
2. How do you distinguish activity links from other links in Moodle?
    
    Looks like a list element with a class of _activity_ is a good first start. If it in turn contains a span of class _autocompletion_ that's another good sign.
    
    Above, that with the activity completion you're only looking for stuff within the _course-content_ div, or below that the _weeks_ unordered list.
    
```html
 <li class="activity book modtype\_book " id="module-263678"> <div> <div class="mod-indent-outer"><div class="mod-indent"></div> <div> <div class="activityinstance"> <a class="" onclick="" href="..mod/book/view.php?id=263678"><img src="" class="iconlarge activityicon" alt=" " role="presentation" /> <span class="instancename">Setting up your tools: Diigo, a blog and Twitter<span class="accesshide " > Book</span></span> </a> </div> <span class="actions"> <span class="autocompletion"><img title="Completed: Setting up your tools: Diigo, a blog and Twitter" alt="Completed: Setting up your tools: Diigo, a blog and Twitter" class="smallicon" src="" /></span> </span> </div> </div> </div> </li> 
```

3. How am I going to get map the USQ Moodle activity and user ids with the ids used on my local server?
    
    A simple script to parse the HTML file for the course home page should be able to extract the ids for each of the activities on the USQ server and also the associated name. The above HTML shows that the id is in the id of the list element. Already have the names of the activities with a hard coded sequential idea in the local database. Can do the mapping that way.
    

### To do

Misc tasks to do

- Think through how this kludge is going to be done. Likely possibilities include
    1. Separate javascript plugins and servers for the activity completion and the user details.
    2. Modify the existing plugins and servers to handle the additional requests.
    3. Integrate activity completion into the existing MAV, but have user details separate
        
        Mainly because activity completion is largely the same as the existing display work that MAV does.
        
- User detail display
    - Investigate what's the best way to pass the data back to the browser - just data with the HTML generated by the browser or as HTML generated by the server and simply inserted by the
    - Chat with Rolley and see whether the rollover/popup idea can be implemented with the same HTML stuff used by the rest of MAV.
- Extract the activity id data from the USQ server.
- Find out if there is a report that Moodle will generate a list of all the users in a course so I can extract user ids from the USQ Moodle server to create a mapping to the local user ids.
    
    The activity participation report will generate a list of all students with a link that includes user id and their name.
    
- Get the MAV code base into git.
- Implement the separate user details version of MAV might be the first major change to do.