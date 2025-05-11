---
categories:
- bim
date: 2009-09-08 15:42:15+10:00
next:
  text: How do you develop a cross-LMS usage comparison?
  url: /blog2/2009/09/09/how-do-you-develop-a-cross-lms-usage-comparison/
previous:
  text: Pedagogy - the centrality of the pedagogue and what they believe
  url: /blog2/2009/09/07/pedagogy-the-centrality-of-the-pedagogue-and-what-they-believe/
title: '"BIM#7 - Getting the prototype up"'
type: post
template: blog-post.html
---
[Last time](/blog2/2009/09/03/bim-6-learning-weblib-php/) I worked on [BIM](/blog2/research/bam-blog-aggregation-management/) I got to know weblib.php enough to get the first canned Moodle page generated. The [student details page](http://www.flickr.com/photos/david_jones/3882960287/) which lets the student see what BIM knows about their blog contributions for the current course.

The rationale for this prototype approach includes:

- let me get to know Moodle programming a bit slowly;  
    Last week was getting to know weblib.php a bit more. The week or so before it was activity modules and it won't be to long before I dive into that again.
- get a prototype working within Moodle so I can show folk and get feedback.

In terms of using the prototype, the current plan (i.e. it might change) is to: produce some screencasts using the prototype, create a discussion forum around the screencasts and encourage people to give feedback both online and offline.

The aim today is to get more of the student view of BIM put into the prototype. If I get lucky, I might even start on the academic's view.

### What the student will see

An [earlier post](/blog2/2009/08/20/bim5-getting-a-prototype-bim-going/) gave some details of the various screens/operations different users would be doing with BIM. The following is a simple list of what I need to do with students:

- the blog registration page;  
    
- the blog details page; **DONE**

Gee, I'm further along than I thought.

### Play with Moodle more

Given I'm a bit further along and because creating the blog registration page is very straight forward, this should allow me to play around with Moodle a bit more.

The blog registration page and the blog details page for the students should be the same link. Before the student has registered a blog with BIM, it should show the registration page. After they've registered, it should show the details page (possibly with an option to change the registration).

Rather than hard code this, let's play with the Moodle code so that it performs this check and displays the appropriate HTML. Based on this, I'm guessing I'll need to:

- Ensure that a database table is created that allows BIM to store that a student has registered their blog.
- Ensure that the show details page only appears for students.
- Have the code look at this table and display the appropriate fields. Sort of.
- When the registration page is submitted, have it update the table to "register the blog".  
    This could either be a dummy value or an actual registration. At this stage it won't do the checks that are necessary to determine if the URL entered by the student is actually a blog with a feed.
- Update the details page to allow a change in registration option.  
    Eventually this will have to be configured by the course coordinator. Yes the students can change their registration, or no they can't.

#### The database

Time to remind myself about the database tables I've created and how in Moodle to create/check these.

- Go to the admin page on my Moodle install.
- The XMLDB editor is used to create/edit databases and is under the Miscellaneous menu (I'd forgotten that and had to dig).

- Currently there is only the **bim** table. Matches the module name and is used to associate an instance of the activity with a course - and some other stuff.

What I want to do know is take the BAM\_BLOG\_STATISITCS table from BAM and put it into the Moodle "schema". The table stores information about a student blog. Currently its desc is

```
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `COURSE` varchar(10) NOT NULL DEFAULT '',
  `PERIOD` char(2) NOT NULL DEFAULT '',
  `YEAR` int(4) NOT NULL DEFAULT '0',
  `STUD` varchar(12) NOT NULL DEFAULT '',
  `NUM_ENTRIES` int(4) NOT NULL DEFAULT '0',
  `LAST_POST` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `BLOG_URL` text,
  `FEED_URL` text,
  `A_TITLE` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `COURSEIDX` (`COURSE`,`PERIOD`,`YEAR`),
  KEY `COURSESTUDIDX` (`COURSE`,`PERIOD`,`YEAR`,`STUD`),
  KEY `TermYearIdx` (`PERIOD`,`YEAR`)

```

The proposed translation shown in the following table

| BAM field | BIM field | Description |
| --- | --- | --- |
| ID | id bigint(10) unisigned) | Unique ID for this table |
| COURSE,PERIOD,YEAR,A\_TITLE | bim bigint(10) unsigned | In BAM this identifies a unique use of BAM. Within Moodle I believe this will be represented by the id from the bim table. The quiz engine seems to use a similar in mdl\_quiz\_attempts. |
| STUD | userid bigint(10) unsigned | Unique CQU stud number for BAM. userid in BIM. This should allow staff to register blogs as well. Potentially useful for other uses of BIM. Will likely have to allow coordinator to configure who can register a blog. |
| NUM\_ENTRIES | numentries mediumint(6) | The number of posts in the feed. Using a Moodle naming approach and the same type as used in quiz\_attempts |
| LAST\_POST | lastpost bigint(10) unsigned | The date time of the feed's last post. Going by quick look at other tables. Seems that Moodle uses bigint(10) for dates - UNIX timestamps? |
| BLOG\_URL | blogurl varchar(255) | URL for the blog, varchar(255) used for URL in user table |
| FEED\_URL | feedurl varchar(255) | See blog url |
| Keys |  | Only need the primary key. The other keys/indexes no longer make sense with the new fields. |

That seems okay and it's been created. God I hate the XMLDB editor.

The question now is how to get this update in play. That's right, just update the version number in version.php within the bim folder - that works.

#### Only "show details" for students

The idea is that only a user who is a student in the course that has the bim activity should see the "show details" HTML. Need to check that this is working.

- Create users of different types  
    I have three accounts - the admin account (admin), a teacher (fred) account and a student (david) account
- Login as each one and check.

Yep, that's all working as I'd expect.

#### Look for entry in table for student and change display

Okay, so now I have to check for the existence of an entry in the new bim\_student\_feeds for the current user and the current bim activity.

The [DML functions](http://docs.moodle.org/en/Development:DML_functions_-_pre_2.0) are what you're supposed to use to get information from the database. There's a nice set of links that points to [seeing if any records exist match a given a criteria](http://docs.moodle.org/en/Development:DML_functions_-_pre_2.0#Seeing_if_any_records_exist_match_a_given_criteria). Using the function

```
record_exists($table, $field1=, $value1=)
```

The forum code seems to use a collection of library functions in forum/lib.php to add additional checks, just not record exists. I think that's probably a good practice to follow. I can see view.php getting quite large. So we'll start there with a simple one

```
function bim_feed_exists( $bim, $userid ) {
  return record_exists( "bim_student_feeds", "bim", $bim, "userid" $userid );
}

```

Of course, have to get the bim and userid values in view.php and call the new function. No worries.

Seems to be all working, except I'm getting the message that the mdl\_bim\_student\_feeds table doesn't exist. And it doesn't. Bugger! I thought that was working.

I've made sure the XMLDBB stuff is saved. It is showing that the XML is storing it. The XML file has it there. I've updated the version number, run the "notifications" stuff, it is saying that the database has been updated. But no mdl\_bim\_student\_feeds table!!!

Is there something wrong with the naming? Is there a log telling me something I'm not looking at?

When in doubt, delete. That fixed it. But that will be annoying.

Okay, time to display the registration form

The obvious thing to come of this is that weblib.php stuff is not what should be used to create the form. formlibs.php is. Will have to start there I think.

### Summary and to do

Okay, I've got bim starting to read and react to content in the database. Started using the lib file. Different users are seeing the right information.

To do

- Use [formslib.php](http://docs.moodle.org/en/Development:lib/formslib.php_Usage) to handle the register process, this includes saving the data in the database - but not checking yet.
- Move onto the hard-coded prototype stuff for the teaching staff.