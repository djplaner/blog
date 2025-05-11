---
categories:
- bad
- design-theory
date: 2014-10-14 16:47:50+10:00
next:
  text: Some more tweaks to gradebook
  url: /blog2/2014/11/05/some-more-tweaks-to-gradebook/
previous:
  text: On the difference between &quot;rational&quot;, &quot;possible&quot; and &quot;desirable&quot;
  url: /blog2/2014/10/09/on-the-difference-between-rational-possible-and-desirable/
title: Fixing one part of the peoplesoft gradebook
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: Peter
      author_email: palbion@me.com
      author_ip: 123.211.240.227
      author_url: http://pamatravel.wordpress.com
      content: That really should be built into any sensible system but it's nice that
        you can make it happen regardless of the clunky system :-)
      date: '2014-10-14 20:41:49'
      date_gmt: '2014-10-14 10:41:49'
      id: '1142'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: David Jones
      author_email: davidthomjones@gmail.com
      author_ip: 123.211.65.75
      author_url: https://djon.es/blog/
      content: Sums up nicely the point of one of the ASCILITE papers.  The very nature
        of universities/organisations and the nature of the problem of e-learning (very
        broadly speaking) is such that they will always produce clunky systems.  The proposition
        is that the only way to get a non-clunky system is to enable this type of bricolage/digital
        renovation.
      date: '2014-10-15 10:58:30'
      date_gmt: '2014-10-15 00:58:30'
      id: '1143'
      parent: '1142'
      type: comment
      user_id: '1'
    
pingbacks:
    - approved: '1'
      author: Some more tweaks to gradebook | The Weblog of (a) David Jones
      author_email: null
      author_ip: 192.0.82.101
      author_url: https://djon.es/blog/2014/11/05/some-more-tweaks-to-gradebook/
      content: '[&#8230;] is a development log of a few additions to the recent fixes
        to the Peoplesoft gradebook. The following documents attempts to implement the
        [&#8230;]'
      date: '2014-11-05 11:12:48'
      date_gmt: '2014-11-05 01:12:48'
      id: '1144'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The following is a development log of an attempt to fix one aspect of the Peoplesoft gradebook used at my current institution.

# Why and what?

### The problem

At the end of semester all assignment marks end up in the Peoplesoft gradebook. An old school web information systems that the academic in charge of a course has to use to do some last minute checks and changes. One of those changes is to change the grade for students who are within 0.5 of grade level. e.g. a student with a mark of 49.6 shouldn't get an F, they should get a C (which is the pass mark).

Peoplesoft won't do this. The academic has to manually scroll through the list of students (ordered alphabetically by student name) looking for those that in this range. Once found the new grade has to be manually entered into a textbox. This is a problem, especially if your class has a couple of hundred students.

### The solution

The solution developed below is a Greasemonkey script that will automate this process. It will, once installed

1. Detect that the peoplesoft gradebook is being displayed.
2. Look for any students within 0.5 of a grade level.
3. For each of these students found
    - Change the background for that row to red.
    - Place the upgraded grade in the appropriate textbox.
4. Look for any students who have already been upgraded, change the background of their row to green.

# How?

### Identifying the gradebook

First initial problem is that the Peoplesoft gradebook is using iframes. Which complicates things a little. Especially in identifying the appropriate iframe and then getting the script to only activiate when the appropriate document is loaded. Not to mention no great surprise that we're talking some really ugly HTML here.

The actual data for each student is spread over a row with XXX main cells each with div elements with specific ids (the $0 appears to increment per student)

- win0divHCR\_PERSON\_NM\_I\_NAME$0 - span HCR\_PERSON\_NAM\_I\_NAME$0 contains the name
- win0divSTDNT\_GRADE\_HDR\_EMPLID$0 - span STDNT\_GRADE\_HDR\_EMPLID$0 - contains the EMPLID
- win0divSTDNT\_GRADE\_HDR\_GRADE\_AVG\_CURRENT$0 - span STDNT\_GRADE\_HDR\_GRADE\_AVG\_CURRENT$0 - has the result.
- win0divSTDNT\_GRADE\_HDR\_COURSE\_GRADE\_CALC$0 - span STDNT\_GRADE\_HDR\_COURSE\_GRADE\_CALC$0 - has the grade
- input text box with id STDNT\_GRADE\_HDR\_CRSE\_GRADE\_INPUT$0 is where the changed grade might get entered.

It appears to be part of a form with the URL ending in SA\_LEARNING\_MANAGEMENT.LAM\_CLASS\_GRADE.GBL and appearing in an IFRAME with id ptifrmtgtframe - which I assume is a generic iframe used on all the pages.

So the plan appears to be for the script to

1. Only respond for the broad URL associated with the institutional gradebook. Done via the standard Greasemonkey approach.
2. Only kick into action on the loading of the iframe with id ptifrmtgtframe. This appears to work. \[code lang="javascript"\] var theFrame; theFrame = document.getElementById('ptifrmtgtframe'); theFrame.addEventListener( "load", my\_func, true ); \[/code\]
3. Check to see if the form SA\_LEARNING\_MANAGEMENT.LAM\_CLASS\_GRADE.GBL OR perhaps the presence of the ids from the table above Have modified the above to pass the frame in and was using that to determine the presence of the textbox. The problem is that there is a further complication to the interface. Jumping to the specific page in the gradebook (there are three) is being done by a "javascript:submitAction\_win0(document.win0.....)". This isn't showing up as an on load for the frame.
    
    Found [this post](http://danielkibler.blogspot.com.au/2010/11/using-javascript-in-peoplesoft-proxy.html) which talks about one potential solution but also points to someone who's been doing this for much longer and in more detail.
    
4. Have they included the number of students in the HTML? - no, doesn't look like it.

A rough attempt to understand what is going on

1. Faculty centre loads with list of courses. The standard entry into gradebookFix is run at this stage - alert is shown. And then the iframes load.
2. Click on gradebook icon trigger the current iframe load event and shows the three different gradebook icons. The _my\_func_ function is run via an event listener for onLoad for the _ptifrmtgtframe_ iframe. But this is only run the once as....
3. Click on the "cumulative grades" doesn't load a new iframe, calls the javascript:submitAction\_win0 method.

The aim is to modify the click on the particular link so that something else happens. How about

1. Modify onload to look for that link and add a onclick event. The id for the link is DERIVED\_SSR\_LAM\_SSS\_LINK\_ANCHOR3. The problem is that attempting to add an event listener to this is not working. i.e. a call to getElementById is not working. Aghh, that's because these things aren't normal Javascript type objects, but special Greasemonkey wrapped stuff. \[code lang="javascript"\] var theLink = theFrame\["contentDocument"\].getElementById('DERIVED\_SSR\_LAM\_SSS\_LINK\_ANCHOR3');
    
    theLink.addEventListener( "click", function(){ alert( "CLICK ON LINK CUMULATIVE" ); }, false ); \[/code\]
2. Have a function that is called on click. The struggle here will be that the click is actually the start of a query that results in the content being changed. But not necessarily recognised by Greasemonkey.
    
    Perhaps a timeout and then another bit of code like this might work. This could be tested simply be re-adding the on-click. This will sort of work, but again, is only set when the iframe loads for the first time. If any other navigation happens it won't re-add any changes in.
    
    Have added it to the other two main links for gradebook. Possible this will be a sufficient kludge for now.
3. Looks like we need to capture the _submitAction\_win0_ method after all. Nope, have figured a kludge

### Identifying the student rows

The following code segment will change the background/font color of the first student's name \[code lang="javascript"\] function updateResults(element) { var name = element.getElementById('win0divHCR\_PERSON\_NM\_I\_NAME$0'); name.style.backgroundColor = 'red'; name.style.color = 'white'; } \[/code\]

Above specifies the names of the different student fields. The difference is the number after the dollar sign - 0 up to the last.

Steps required here

1. Identify how many students are on the page. Will be useful for a for loop to go through each. xpath might offer a possibility? JQuery? A simple while loop could also do the trick. Will go with that.
2. Determine what to change Plan is
    - RED - need attention i.e. marks that should be over-ridden with suggested override in place.
    - GREEN - those that have already been over-ridden previously.
    - no colour/change - correct as is.

All done. Seems to work.