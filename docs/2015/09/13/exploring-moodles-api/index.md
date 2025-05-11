---
categories:
- bad
- e-learning
- elearning
date: 2015-09-13 16:24:59+10:00
next:
  text: What might a project combining LX Design and Analaytics look like?
  url: /blog2/2015/09/14/what-might-a-project-combining-lx-design-and-analaytics-look-like/
previous:
  text: What type of &quot;digital knowledge&quot; does a teacher need?
  url: /blog2/2015/09/10/what-type-of-digital-knowledge-does-a-teacher-need/
title: Exploring Moodle's API
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Helping teachers &#8220;know thy students&#8221; | The Weblog of (a) David
        Jones
      author_email: null
      author_ip: 192.0.100.175
      author_url: https://davidtjones.wordpress.com/2015/09/15/helping-teachers-know-thy-students/
      content: '[&#8230;] plan to continue the use of augmented browsing as the primary
        mechanism, and why I&#8217;ve started exploring Moodle&#8217;s API. It appears
        to provide a way to allow the development of a flexible and customisable approach
        to [&#8230;]'
      date: '2015-09-15 10:06:43'
      date_gmt: '2015-09-15 00:06:43'
      id: '1425'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
[![Biblia (German), f.40r, detail by CRC, University of Edinburgh, on Flickr](https://farm4.static.flickr.com/3682/10155924084_207fe9c6ba_m.jpg "Biblia (German), f.40r, detail by CRC, University of Edinburgh, on Flickr")](https://www.flickr.com/photos/crcedinburgh/10155924084/)  
[![Creative Commons Creative Commons Attribution-Noncommercial-No Derivative Works 2.0 Generic License](http://i.creativecommons.org/l/by-nc-nd/2.0/80x15.png "Creative Commons Creative Commons Attribution-Noncommercial-No Derivative Works 2.0 Generic License")](http://creativecommons.org/licenses/by-nc-nd/2.0/)   by  [](https://www.flickr.com/people/crcedinburgh/)[CRC, University of Edinburgh](https://www.flickr.com/people/crcedinburgh/) [](http://www.imagecodr.org/)

[API centric architecture](http://apigee.com/about/blog/technology/api-centric-architecture-all-development-api-development) is a coming thing in technology circles. It's the way vendors and central IT folk will build systems. It is also going to be manna from heaven for institutionalised people who are [breaking a little BAD](/blog2/2014/09/21/breaking-bad-to-bridge-the-realityrhetoric-chasm/).

Moodle has a growing [web services API](https://docs.moodle.org/dev/Web_services_API). The following documents some initial exploration of how and if you can "break BAD" with those APIs.

## Background

### Web services API

Moodle has a capability for plugins to define [a Web services API](https://docs.moodle.org/dev/Web_services_API). The question is, how many plugins provide this and how much of Moodle core has exposed APIs. It's likely to be quite large given APIs are increasingly used for mobile devices.

A quick check of my basic Moodle 2.9 install reveals \[code lang="bash"\] dj:moodle david$ find . -name services.php ./admin/mnet/services.php ./enrol/manual/db/services.php ./enrol/self/db/services.php ./lib/db/services.php ./message/output/airnotifier/db/services.php ./mod/assign/db/services.php ./mod/forum/db/services.php ./mod/lti/services.php\[/code\]

Not a huge number, but at least enough to start playing with (assign and forum are likely to be particularly useful) and there may well be more.

Of course, I should be looking to add a Web services API to [BIM](/blog2/research/bam-blog-aggregation-management/). [This page](https://docs.moodle.org/dev/Adding_a_web_service_to_a_plugin) will apparently help with that.

[That page](https://docs.moodle.org/dev/Adding_a_web_service_to_a_plugin) also includes a template with a test client. Could be useful later on.

### What about the Core APIs

Moodle defines a [number of Core APIs](https://docs.moodle.org/dev/Core_APIs) that are used within Moodle. Are these available via Web services? Some (all?) wouldn't make sense, but maybe...

### External functions API

The [external functions API](https://docs.moodle.org/dev/External_functions_API) apparently "allows you to create fully parameterised methods that can be accessed by external programs (such as Web services API)". Searching for evidence of that in my Moodle install is a little more heartening

\[code lang="bash"\] dj:moodle david$ find . -name externallib.php ./calendar/externallib.php ./cohort/externallib.php ./course/externallib.php ./enrol/externallib.php ./enrol/manual/externallib.php ./enrol/self/externallib.php ./files/externallib.php ./grade/externallib.php ./group/externallib.php ./lib/external/externallib.php ./lib/externallib.php ./message/externallib.php ./message/output/airnotifier/externallib.php ./mod/assign/externallib.php ./mod/forum/externallib.php ./notes/externallib.php ./user/externallib.php ./webservice/externallib.php\[/code\]

Just have to figure out if the presence of these implies connections with a Web services API and the ability to access from a client.

### Web Services

Which brings me to [the Web Services category page](https://docs.moodle.org/dev/Category:Web_Services). There's also [a web services forum](http://moodle.org/mod/forum/view.php?id=6971) and [a related FAQ](https://docs.moodle.org/29/en/Web_services_FAQ), which includes:

- [Details of where to see the available API](https://docs.moodle.org/29/en/Web_services_FAQ#Where_is_the_Web_Service_API_documented.3F) for your Moodle install.
- A pointer to the [Web services roadmap](https://docs.moodle.org/dev/Web_service_API_functions) which indicates that it's still a work in progress. It does give a list of what has been implemented. Bingo, activity completion data (at least in 2.9) is included.
- Includes details of how to create a new web service with the advice of using a local plugin. This might be a possible kludge where Moodle hasn't yet provided what might be needed.
- A pointer to [how to get a user token](https://docs.moodle.org/dev/Creating_a_web_service_client#How_to_get_a_user_token) for a script.

### Security

[External services security](https://docs.moodle.org/dev/External_services_security) outlines various ways services can be called and how security is handled.

## Using web services on my Moodle instance

As per [these instructions](https://docs.moodle.org/29/en/Using_web_services) and elsewhere

1. [Enabling web services.](https://docs.moodle.org/29/en/Using_web_services#Enabling_web_services)
[](https://docs.moodle.org/29/en/Using_web_services#Enabling_web_services)3. [](https://docs.moodle.org/29/en/Using_web_services#Enabling_web_services)[Enabling protocols](https://docs.moodle.org/29/en/Using_web_services#Enabling_protocols)
    
    Appears REST is enabled by default (don't think I did this earlier).
    

Explore - Site administration / Plugins / Web Services - and its range of options

1. Overview. Includes directions on steps for enabling web services for mobile devices and for external systems to control Moodle.
2. User. Need to allocate permission to use web services to specified users.
3. Add services to be used. Which web services can the user use. In this case, a range of "built-in services" were already enabled for "all users" (assuming they have the required capabilities). This might be interesting to test and explore. Includes a broad array of interesting functionality (mod\_assign\_get\_???) but not overly long.
    
    Adding a service requires specification of the functions to be enabled.
4. Each service can be configured to a particular user or multiple users.
5. Create a token - select a user and the service.
6. And then there's a test client embedded in Moodle. Which only allows testing of a small subset. Looks like having to write a client will be required. Tried a function via the test API. Got a security error. Added it to the functions in the service I'd set up, and hey presto it worked.

### Writing a client

There's a github repo with [sample-ws-clients](https://github.com/moodlehq/sample-ws-clients). I'll use the <a href="https://github.com/moodlehq/sample-ws-clients/tree/master/PHP-REST"PHP-REST code.

1. Clone the repository
2. Modify the token, URL, etc.
3. Use the API documentation to figure out the correct format for the request. Which was quite straight forward \[code lang="php"\] $functionname = 'moodle\_user\_get\_users\_by\_id'; $restformat = 'xml'; $userids = array( 489, 2 ); $params = array('userids' => $userids); \[/code\]
4. Change the format to json and it works just as well, but of course different format in the data returned.

The JSON option (from 2.2 onwards) means that planned use within the browser should work fine.

### Exploring functions of interest

In the short term, I'm particular interested in whether there are existing functions for the following tasks

- Get all enrolled users (and perhaps just students) in a course. course\_enrol\_get\_enrolled\_users( $course\_id ) Also accepts: \[code lang="php"\] options => array( withcapability => string, groupid => int, onlyactive => int, userfields => Array( string, string..), limitfrom => int, limitnumber => int ) \[/code\]
- Get a user's activity completion details. Appears to be implemented in 2.9. Will update my version and see if it appears. Yes. core\_completion\_get\_course\_completion\_status( int courseid ) Returns a list of statuses including: comment id (cmid), activity module name (modname), instance ID (instance), state (0 incomplete, 1 complete, 2 complete pass, 3 complete fail), timecompleted, tracking (0 none, 1 manual, 2 automatic) )
- Get information about status and results of assignments.
    - mod\_assign\_get\_assignments( array of course ids ) Returns a list of courses, but also a list of assignment details.
    - mod\_assign\_get\_grades( array of assignment ids ) Returns a list of assignments and a list of grades for each assignment. Grades include the userid, attemptnumber, timecreated, timemodified, grader and grade.
    - mod\_assign\_get\_submissions( array of assignment ids ) Similar to get grades but includes status, also submission plugin, list of files and additional information
    - mod\_assign\_get\_user\_flags( array of assignment ids ) Flags include workflowstate, allocated marker, and extension date.

### Some longer term services

Longer term some other areas of interest might include

- Adding web services to BIM.
    
    A job for me at a later date.
    
- core\_message - list of services around the messaging services, perhaps as a way to intervene?