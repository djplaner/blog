---
title: BIM - Creating the test data, completing dbase design
date: 2009-12-22 11:29:59+10:00
categories: ['bim']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: BIM &#8211; cron and view student details screen &laquo; The Weblog of (a)
        David Jones
      author_email: null
      author_ip: 74.200.244.88
      author_url: https://djon.es/blog/2009/12/22/bim-cron-and-view-student-details-screen/
      content: '[...] The Weblog of (a) David Jones Another voice in the blogosphere    &laquo;
        BIM &#8211; Creating the test data, completing dbase&nbsp;design [...]'
      date: '2009-12-22 15:42:12'
      date_gmt: '2009-12-22 05:42:12'
      id: '2898'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The [last bit of BIM work](/blog2/2009/12/20/bim-savingmanipulating-rss-files/) resulted in getting the show student details screen up and going, mostly. Any more of these screens will draw on, at least in part, other data from other tables. Time to get those populated. This will be done using data from BAM currently being used.

### Creating the table

### Dummy data

Will need some good data for testing. So the plan is to convert some existing data from BAM into the BIM format. Here are the steps.

#### Get the BAM data

Need to update local versions of the BAM data as a first step. Getting some recent data likely to be most useful.

#### Complete the creation of all BIM database tables

Need to have these set up before I can convert all the data. Due to the linkages between tables, the conversion process will have to know something about these tables. Last one to be converted is bim\_questions. Back to the XMLDB editor. `bim_questions` will have the following fields (initially)

- id bigint(10)
- bim bigint(10)
- title varchar(255)
- body text
- min\_mark int(5)
- max\_mark int(5)

Done.

However, **Marker allocations:** is still a problem. BAM relies on a Webfuse database to track which markers are responsible for marking which students. My current institution is still figuring out/potentially changing how they do this. I could figure out how Moodle does this currently, however, not sure if that will change + it will take more work.

At this stage, the plan is:

- Convert the existing Webfuse `MARKERS_STUDS` database into a Moodle/BIM table.
- Write a support function or two that allows BIM to use (but not manipulate) the data in that table in a way that is independent of representation/format.
- Use those functions in BIM to get the data.
- At a later date, modify the support function(s) to work with whatever is decided.

So, `bim_markers_students` will have the fields:

- id bigint(10)  
    ID for the table.
- course bigint(10)  
    The course ID for uniquely identifying the Moodle course for which the marker allocations hold.
- marker bigint(10)  
    The user id for the marker.
- student bigint(10)  
    The user id for the student.

To populate `bim_markers_students` with the data from MARKERS\_STUDS will require the need to read MARKERS\_STUDS, expand out the place markers (ALL, campus names etc), get user ids from Moodle, combine the two into SQL. **DONE**

This will require the entry of student and staff information into Moodle for the staff/students associated with the courses being tested. This has been done with a bulk upload of a CSV file generated from Webfuse code.

#### Convert BAM into BIM data

Due to the various connections between the different data, this is probably not going to be straight forward. Here's a first attempt at the process I think I'll need to follow:

- Select the course offerings to bring over. I'm thinking at least 2 courses, currently only have permissions for 1 (but two different offerings of it).
- Create Moodle courses for those offerings.  
    I'm only talking about 2 to start with, so manual creation will do. Done.
- Create accounts for both the students and the markers.  
    This will involve a couple of hundred students. So will have to do the bulk upload thing. So, need to create a CSV file from local data. Here's an example from the help screen
    
    > username, password, firstname, lastname, email, lang, idnumber, maildisplay, course1, group1, type1  
    > jonest, verysecret, Tom, Jones, jonest@someplace.edu, en, 3663737, 1, Intro101, Section 1, 1  
    > reznort, somesecret, Trent, Reznor, reznort@someplace.edu, en\_us, 6736733, 0, Advanced202, Section 3, 3  
    
    Need to extract all student accounts from local data and have username=student number, contact data and populate the course information (**DONE**). Staff will be much the same but different username.(**DONE**).
    
- Enrol the accounts in the courses.  
    **DONE** as part of the bulk upload.
- Convert the BAM\_CONFIGURE (bim) data for the offerings I'm going to include. -- Actually, this will be creating bim activities in the courses.  
    **DONE**
- Convert the BAM\_QUESTIONS (bim\_questions) table.  
    **DONE**
- Convert the BAM\_BLOG\_STATISTICS (bim\_student\_feeds) table.  
    **DONE**
- Convert the BAM\_BLOG\_MARKING (bim\_marking) table.  
    Need to know the question ID for a given question in Moodle. i.e. translation from what question ID is currently in Webfuse and what has been created in Moodle. Hard code a hash will probably be the quickest way. Webfuse doesn't use ID, it uses the title of the question. So, somewhat of change there. **DONE**

### Where to now

So, I think that means I now have a good collection of test data on which to build the rest of the screens. The task now is to start working my way through those screens and getting them implemented/tested with the current data. Thinking the order should probably be:

- Get the show student details screen working as much as possible.
- Get the show posts and show details screens working for staff.
- Get the marking screen done.
- Get the re-allocation screen done.
- Get the configuration screen for coordinator done.

That should get BIM very close to completion.