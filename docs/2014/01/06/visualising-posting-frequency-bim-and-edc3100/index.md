---
title: "Visualising posting frequency: BIM and EDC3100"
date: 2014-01-06 11:37:00+10:00
categories: ['bim2']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Evaluating EDC3100 in 2013 &#8211; step 1 | The Weblog of (a) David Jones
      author_email: null
      author_ip: 192.0.83.83
      author_url: https://djon.es/blog/2014/01/13/evaluating-edc3100-in-2013-step-1/
      content: '[&#8230;] look at what happened in the course and the course site. Something
        I&#8217;ve already started with this post trying to visualise blog post [&#8230;]'
      date: '2014-01-13 10:05:20'
      date_gmt: '2014-01-13 00:05:20'
      id: '918'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The following describes an attempt to develop a visualisation of the frequency with which students in [the course I teach](http://www.usq.edu.au/course/synopses/2014/EDC3100.html) posted to their blogs during two offerings of the course in 2013. A few reasons for doing this

1. Confirm my gut feel that some students (for a variety of reasons) treated blogging pragmatically and only posted just before due dates.
    
    Only some evidence of this.
    
2. Explore if there's any visual correlation between this behaviour and their final grade in the course and other factors.
    
    Some suggestion of this.
    
3. Help think about whether or not a visualisation like this might be something to include in the next version of BIM.
    
    That might be difficult given time-frames and other constraints, but I'll be exploring how to create some of these manually and use them during the coming semester.
    

Cut to the chase (you may have to be patient for these visualisations to come up in your browser - and I can't be sure they'll work for everyone)

- [Visualisation of semester 2 posts (n=100 students)](https://dl.dropboxusercontent.com/u/14025788/magicTable/sem2_table.html).
    
    The visualisation for the smaller semester works better.
    
- [Visualisation of semester 1 posts (n=303 students)](https://dl.dropboxusercontent.com/u/14025788/magicTable/sem1_table.html).

More description of what and how follows.

## The first plan

A table. Columns represent days of the semester. Each row is a student. Colour the cells where a post occurs. Show the due dates by running a line through the table. Group the rows via various external factors including: GPA, result in the course, sector.

Google Chart's [magic table](http://magic-table.googlecode.com/svn/trunk/magic-table/google_visualisation/example_1.html) looks like a good tool for a first run. So here goes.

### Test out magic tables

Well, the example code for [Data::Google::Visualization::DataTable](http://search.cpan.org/dist/Data-Google-Visualization-DataTable/lib/Data/Google/Visualization/DataTable.pm) is truly broken. But using it will generate Javascript array that will slot straight into the MagicTable visualisation.

### Doing it with BIM data

So bring in some of the BIM code, read the database and generate the data structure required by the MagicTable code and you get the following as a first stab (click on it to see a larger version). Each row of this figure represents an individual student blog. Each column represents a day of the semester. Any cell that is shaded a particular colour represents a day when some posts were added to the student's blog.

The fish-eye view in the above is overing over one student who definitely seems to have left things to the last minute - 16 posts on the one day. A day that happens to be toward the end of the semester.

The prevalence of green squares earlier in the semester represents days with 6 to 8 posts.

If you want to be more interactive, you can see the [full working HTML page here](https://dl.dropboxusercontent.com/u/14025788/magicTable/version_0.html). The table itself has a size of 1403x1315.

What's missing/wrong from this view?

1. The first few columns don't seem to be getting set correctly - NaN?
2. Need more signposting of the various semester dates. e.g. when are the 3 assignments due? When's the Professional Experience period? When are the semester holidays?
    
    On the [HTML page](https://dl.dropboxusercontent.com/u/14025788/magicTable/version_0.html) it's possible to see a pattern where there are fewer posts later in the semester. As it happens, the last 5 weeks of the teaching period for this semester included 2 weeks of holidays and 3 weeks of Professional Experience (where the students are out teaching in schools).
    
3. Include some indication of student results - e.g. final grade, GPA, assignment result or even the result for the learning journal (the marks given for the blog).
    
    [This example](http://www.grvisualisation.50webs.com/volsExample.html) of a magic table uses the idea of column/row headers which could be useful in doing this.
    

### Next step

If I move directly to generating the Javascript from Perl for magic table it appears I have a bit more control. I can set a row and column header so that you can see some detail about the column (e.g. the data) and row (e.g. GPA, student name, grade etc). I have that working. Now I need to get some extra student data into the database.

It is moments like this that I detest working in an environment where there is not decent data infrastructure. Having to waste time to fix up some of the data I'm working with.

Ok, now let's sort by grade and here is [the finished product](https://dl.dropboxusercontent.com/u/14025788/magicTable/sem2_table.html). The page itself offers some more description of what is shown.

I don't have the time to explore what's going on here in detail. So, some quick observations, none of which tell you very much without further exploration

- There is an early student with "no grade" (indicating a withdrawal from the course) that has apparently posted consistently throughout the semester.
- All of the other "no grade" students don't post after the 15th August (when the first assignment is due).
- There's a group of 5 students with the lowest passing grade who blogged consistently throughout the semester but started later than other groups of students.
- There are a few students with the top grades who are quite obviously blogging just before the assignment due dates.

However, it does reinforce an existing opinion that the blogging in this course is not yet introduced sufficiently well for the students to get real value from it.

### Semester 1

The semester 1 offering of the course had three times as many students and was the first time the blogs were used in this course. The semester 1 offering also included 3 groups of on-campus students as well as online students (semester 2 was only offered online). I'm thinking that the semester 1 map should show evidence of more "pragmatic" blogging.

Let's find out.

A rough first run at the [semester 1 view](https://dl.dropboxusercontent.com/u/14025788/magicTable/sem1_table.html).

Some quick comments

- The magic table widget breaks down with the a table this size. Difficult to see the row/column labels as the page scrolls.
- At least for me, you can see the shape of the semester. Assignment 1 due - break. Assignment 2 due - Professional Experience (no blogging), then assignment 3 due.
- THere's at least one C student who appears to be blogging just about every day and often more than one post. What's with that?
- There's a group of C students who appear to be very pragmatic.
- There seems to be a general increase in posting regularity and intensity as you get to the HD students.
    
    At least this is how it looks to me.
    

Would be interesting to explore further. Does mode in semester 1 make a difference? Amongst many more.

### What's next?

Wonder how difficult this would be to incorporate into BIM in a usable way?

At this stage, I'm thinking I'll produce a couple of these visualisations during the coming semester for students to think about where they are with their practice.

May also prove an interesting indication of how changes in the scaffolding and support of the blogging process works out.

The visual representation is interesting, but needs easier ways to manipulate and explore the data more. e.g. some representation of the size, content, number of links, and quality (?) of the blog posts etc.