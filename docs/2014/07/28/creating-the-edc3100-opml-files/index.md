---
title: Creating the EDC3100 OPML files
date: 2014-07-28 16:59:49+10:00
categories: ['edc3100']
type: post
template: blog-post.html
---
Just documenting the process I use to create a collection of OPML files for distributing the details of EDC3100 student blogs (because I didn't document it last semester).

### Background

Each semester students in EDC3100 create [their own blog](https://www.google.com.au/search?q=edc3100+blog&ie=utf-8&oe=utf-8&aq=t&rls=org.mozilla:en-US:official&client=firefox-a&channel=sb&gfe_rd=cr&ei=VNzUU5OLGuLC8geFl4GoCQ) on their choice of service. They then register the blog with the course website via [the BIM module](/blog2/research/bam-blog-aggregation-management/) for Moodle.

For the current semester 63 students have registered their blog, 47 are yet to do so. The students are almost entirely pre-service educators ranging from the Early Childhood all the way up to VET sector. The task here is to produce a range of OPML files containing feeds for each sector.

The data I have to play with includes

- the OPML file produced by BIM that provides feeds for all students; and,
    
    Each OPML item contains the blog URL/feed and the student's name and the short student number.
    
- the spreadsheet from the institutional system that specifies which sector each student is associated with.
    
    Includes a range of student data, including the short student number as part of the email address, however, the sector is not always standardised. For example, the Secondary students, HPE and VET students can have a strange variety of labels.
    

### The process

1. Read the CSV file data.
2. Normalise the sector names.
3. Read the OPML file.
4. Produce separate OPML files for each sector.

The above was done with quite a liberal smattering of manual work. Got it down to a Perl script with a bit of manual stuff at the end.

### Implications

Biggest problem is the sector names. It doesn't appear that the institutional system has adopted a common approach to this so there are half a dozen special cases. It's this sort of thing that makes it extra difficult to do productive stuff with the provided technology/information.

Wonder if BIM can be modified to allow the uploading of additional information about users and then use that to produce OPML files (and other actions). Suppose the Moodle group functionality would be the default means for that. Would still have to be manual.