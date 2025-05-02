---
title: Some thinking on analysing Webfuse usage
date: 2010-03-07 14:21:41+10:00
categories: ['chapter-4', 'chapter-5', 'design-theory', 'elearning', 'indicators', 'phd', 'thesis', 'webfuse']
type: post
template: blog-post.html
---
I've been back working at the PhD thesis, hopefully down to months before submission. At this stage, I need to work on the 2 chapters that are reflecting on the usage of Webfuse during two periods: 1996 through 1999 and 1999 through 2004 (and a bit later). In doing some, the main tasks I need to achieve are:

- Show the difference in usage between the first and second stages.
- Show how usage in the second stage is, hopefully, different and "better" than that reported elsewhere.

Now, I could do this in the same way I've been doing it in the past, an ad hoc collection of Perl scripts and spreadsheets. The benefit of this approach is most of them already exist. The drawback is, however, that this makes it more difficult to compare usage with other systems. This is a problem that [the indicators project](http://indicatorsproject.wordpress.com/) is attempting to address. It might make sense to start thinking about something a little more platform independent.

The following is an attempt to think about what I might be able to do that would progress both the PhD and the indicators project. It eventually morphs into some rough initial design ideas of how I can implement something as a trial run.

### Indicators in a box

A major aim of [the Indicators Project](http://indicatorsproject.wordpress.com/) is to enable and engage in cross-platform, cross-institutional, longitudinal comparisons of LMS usage. The "indicators in a box" idea is one we've been talking about since at least November 2009. Here's an attempt to give one description of what it might be.

The indicators in a box is a zip file containing an application (probably a set of applications) that help an individual or institution examine LMS usage regardless of their LMS or institution. In a perfect world, you would:

- Download the zip file and unpack it on your system.  
    It would probably be a PHP web application so that it is broadly platform independent, simple enough for just about anyone to run and have a easy-to-use and useful interface.
- Configure the indicators in a box for your context.  
    i.e. tell it which LMS you are using and where the usage data from the LMS is setting (typically, which type of database, and details of how to get a connection to it).
- Configure additional information sources.  
    At the very least it would probably be useful to have some information about the students, courses, terms/semesters used at your institution. Some of this data might be put in configuration files, some in a database.
- Choose which analysis you wish to do.  
    Eventually there would be a broad collection of different analyses and comparisons to perform. You select the ones you want to implement.
- Wait for the conversion and preparation.  
    It's likely, though not certain, that the indicators in a box would rely on a set of scripts that are abstracted away from the specific details of an LMS. i.e. the data in your LMS usage database would need to be converted into another database so that comparisons could be made. There are some drawbacks of this approach and some possible alternatives. The types of analysis you want to do would rive what conversions are done.
- Use the indicators in a box user interface to view the results of the analysis.  
    At this stage, you should be able to use the web-based interface to view various analysis of the usage data and perhaps compare it with other institutions etc. This is where [graphs like this](http://www.flickr.com/photos/david_jones/4037668923/in/set-72157608613577424/) might get displayed.
- Share the results.  
    The real aim is to allow you to specify what you want to share with others. i.e. an aim is to allow different folk using the indicators to share their results, to enable more research.
- Write your own analysis code and share it.  
    The aim of having a cross-platform foundation is that anyone could write their analysis code that could be shared with the other folk using the platform.
- Incorporate the generated patterns into your LMS.  
    The idea is that academic staff and students need to be able to use the analysis and resultant patterns to inform what they do. They do things within the LMS. So, there needs to be a way to include the patterns/analysis into the LMS in a simple and visible way.

This is still early days. Lot's of options in the above. But the basic aim is to have something that is easy to install and which will start generating useful stats and allowing all the people using it to share the data and the analysis in appropriate ways.

### What do I need to do?

This should be needs driven. I need to focus now on what I need for the PhD and hope it can be abstracted later.

In terms of comparison between the two stages, I am interested in seeing changes in:

- Percentage of staff and students using Webfuse.
- Overall amount of Webfuse usage by staff and students.
- Feature usage within Webfuse course sites.

The first two could be viewed as total counts and counts by types of feature. Which links to the feature usage within course sites.

Currently, chapter 4 of the thesis has the following table for feature usage by course sites in Webfuse 1997-1999. Like the [Indicators ascilite paper](http://indicatorsproject.wordpress.com/2009/10/09/the-indicators-project-identifying-effective-learning-adoption-activity-grades-and-external-factors/) this categorisation depends on the work of Malikowski et al (2007) .

| Category | Malikowski et al % | 1997 | 1998 | 1999 |
| --- | --- | --- | --- | --- |
| Transmitting content | \>50% | 45% | 40.6% | 41.2% |
| Class interactions | 20-50% | 1.8% | 3.6% | 7.9% |
| Evaluating students | 20-50% | 1.8% | 1.5% | 2.6% |
| Evaluating course and instructors | <20% | 9.2% | 1% | 9.5% |

#### Feature usage calculation

This seems to suggest a need to:

1. Identify a way of categorising LMS features - such as Malikowski et al (2007) - and mapping the LMS functionality into that feature set.  
    Malikowski doesn't include [class management](/blog2/publications/class-management-the-forgotten-task/). Also, in a Webfuse context, the idea of a page update usage would be useful. Implies some flexibility in the feature categorisation. e.g. page Update might be a new category, course design and updating - it would be interesting to track the amount of time academics have to spend creating a course site over time. I suspect the more times they teach a course, the less they edit it.
2. Calculating the percentage of a course site features which belong to each feature category.
3. Calculating the number of times each feature is used by a student and staff member.
4. Being able to examine some usage by date/time periods.

#### Overall statistics

- Total number of courses sites for a given period.
- Total number of students and total number per course
- Total number of staff and total per course.

Implies need data from outside the LMS. Also a way of specifying term/semester/period and grouping/recognising course offerings by that term/period/semester. Also starts leading into generic demographic information about the students and perhaps the courses.

### Design of feature usage

In order to track usage of features by staff/students it would be necessary to have a list of when they access features, who they are etc. Something like:

- username - unique id for the user
- feature id - unique id for the feature
- descriptor - might be the URL from the system or some other descriptor. A connection back to the platform dependent data to help in debugging and understanding.
- date time
- course
- period
- year

The feature id would be some unique id that connects to a feature categorisation table (as well as other things?):

- feature id - link back to feature usage
- feature category id

Could also link to a category\_descriptor table:

- feature category id
- category name
- category scheme

The idea of all of this is so that you can choose to perform the feature analysis using one of a number of different categorisation schemes.

### Implementation with Webfuse

I have two main sources of data about Webfuse:

- The Webfuse course sites; and  
    These are the actual files/directories from the web server, What is shown and used by students/staff. This includes information about the types of feature a particular page is.
- server logs.  
    These contain who accessed what and when. Though, in the case of "who" is often anonymous because most of the Webfuse course sites were not restricted.

To take the Webfuse data I have and put it into a set of tables like that described above, I would have to:

- Come up with some way to categorise every URL in the server logs in a category scheme.
- Read all the entries in the server logs and apply the categorise function to each entry and then populate the usage table.

At this stage, other functions (mostly web-based) can be run on the resulting data to do the analysis.

mmmm, something to do.

### References

Malikowski, S., M. Thompson, et al. (2007). "A model for research into course management systems: bridging technology and learning theory." Journal of Educational Computing Research 36(2): 149-173.