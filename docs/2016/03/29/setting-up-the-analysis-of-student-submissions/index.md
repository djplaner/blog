---
categories:
- bad
- edc3100
date: 2016-03-29 14:32:58+10:00
next:
  text: Some simple analysis of student submissions
  url: /blog2/2016/03/30/some-simple-analysis-of-student-submissions/
previous:
  text: LATs, OER, TPACK, and GitHub
  url: /blog2/2016/03/26/lats-oer-tpack-and-github/
title: Setting up the analysis of student submissions
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: Anne de Bruin
      author_email: u1058477@umail.usq.edu.au
      author_ip: 118.208.165.199
      author_url: http://jennarose2015.wordpress.com
      content: Sounds complicated! I really hope it's not mine that is causing you grief!
        Good luck with the marking!
      date: '2016-03-29 19:47:47'
      date_gmt: '2016-03-29 09:47:47'
      id: '3332'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: David Jones
      author_email: davidthomjones@gmail.com
      author_ip: 101.179.114.187
      author_url: https://djon.es/blog/
      content: I've been in contact with those who may have problems, so if you haven't
        heard from me, should be all good.
      date: '2016-03-30 05:31:54'
      date_gmt: '2016-03-29 19:31:54'
      id: '3333'
      parent: '3332'
      type: comment
      user_id: '1'
    
pingbacks:
    - approved: '1'
      author: Some simple analysis of student submissions &#8211; The Weblog of (a) David
        Jones
      author_email: null
      author_ip: 192.0.101.135
      author_url: https://davidtjones.wordpress.com/2016/03/30/some-simple-analysis-of-student-submissions/
      content: '[&#8230;] last post outlined the process for extracting data from ~300
        student submissions. This one outlines what was [&#8230;]'
      date: '2016-03-30 11:16:52'
      date_gmt: '2016-03-30 01:16:52'
      id: '3334'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
A couple of weeks ago I wrote [this post](/blog2/2016/03/10/setting-up-an-excel-checklist/) outlining the design of an Excel spreadsheet EDC3100 students were asked to use for their first assignment. They'll be using it to evaluate an ICT-based lesson plan. The assignment is due Tuesday and ~140 have submitted so far. It's time to develop the code that's going to help me analyse the student submissions.

## Aim

The aim is to have a script that will extract each students responses from the spreadsheet they've submitted and place those responses into a database. From there the data can be analysed in a number of ways to help improve the efficiency and effectiveness of the marking process; and, explore some different practices ([the earlier post](/blog2/2016/03/10/setting-up-an-excel-checklist/) has a few random ideas).

The script I'm working on here will need to

1. Be given a directory path containing unpacked student assignment submissions.
2. Parse the list of submitted files and identity all the spreadsheets
3. Exclude those spreadsheets that have already been placed into the database. Eventually this will need to be configurable.
4. For all the new spreadsheets
    1. Extract the data from the spreadsheet

At this stage, I don't need to stick the data in a database.

## Steps

1. Code that when given a directory will extract the spreadsheet names
2. Match the filename to a student #id.
3. Parse an individual Excel sheet
    1. Rubric
    2. About
    3. What
    4. How
    5. Evaluation
    6. RAT
4. Mechanism to show the values associated with question number in the sheet. Look at a literal data structure.
5. Implement a test sheet
6. See which student files will give me problems.

### Extract spreadsheet names

 

This is where the "interesting" naming scheme by the institutional system will make things interesting. The format appears to be

**_SURNAME_ _Firstname_\__idnumber_\_assign****submission\_file\__whateverTheStudentCalledTheFile.extension_**

Where

- _SURNAME Firstname_ Matches the name of the student with the provided case (e.g. "JONES David")
- _idnumber_ Appears to be the id for this particular assignment submission.
- assignsubmission\_file\_ Is a constant, there for all files.
- _whateverTheStudent..._ Is the name of the file the student used on their computer. It appears likely that some students will have been "creative" with the naming schemes.  Appears at least one student has a file name _**something**_**.xlsx.docx**

### Match the filename to a student id

This is probably going to be the biggest problem area. I need to connect the file to an actual unique student id. The problem is that the filename doesn't contain a unique id that is associated with the student (e.g. the Moodle user id for the student, or the institutional student number).  All it has is the unique id for the submission.

Hence I need to rely on matching the name.  This is going to cause problems if there are students with the same name, or students who have changed their name while the semester is under way. Thankfully it appears we don't currently have that problem.

### Test with 299 submitted files

Assignment due this morning - let's test with the 299 submitted files.

Ahh, issues with [people's names](https://developers.slashdot.org/story/16/03/26/2017231/names-that-break-computers): apostrophe

### Problem files

Apparently 18 errors out of 297 files.  Where did the other 2 go?

"Bad" submissions include

1. 10 with only 1 file submitted; All 10 only submitted the checklist. Not the cover sheet or the lesson plan.
2. 26 with only 2 files submitted (3 total required)
    1. 25 - Didn't submit the lesson plan
    2. 1 - Didn't submit the checklist
    3. 0 - Didn't submit the coversheet
3. 18 files that appear to have the bad xlsx version problem from below.

That implies that some of the people who submitted 3 files, didn't submit an excel file?

Oh, quite proud in a nerdy, strange way about this

 

\[code lang="bash"\] for name in \`ls | cut -d\_ -f2 | sort | uniq -c | sort -r | grep ' 3 ' | sed -e '1,$s/^.\*\[0-9\] //'\` do files=\`ls \*$name\*\` echo $files | grep -q ".xls" if \[ $? -eq 1 \] then echo "found $name" fi done \[/code\]

I'm assuming there will be files that can't be read. So what are the problems.

Seem they are all down to Microsoft's "Composite Document File V2 Format".  These files will open in Excel, but challenge the Perl module I'm using.

Out of the 297 submitted so far, 18 have this problem.  Going to leave those for another day.