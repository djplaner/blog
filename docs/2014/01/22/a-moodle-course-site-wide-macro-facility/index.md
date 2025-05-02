---
title: "A #moodle course site wide \"macro\" facility?"
date: 2014-01-22 10:49:36+10:00
categories: ['moodle']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: What might the 3 levels of organisational culture reveal about university
        e-learning | The Weblog of (a) David Jones
      author_email: null
      author_ip: 66.155.38.18
      author_url: https://davidtjones.wordpress.com/2015/01/20/what-might-the-3-levels-of-organisational-culture-reveal-about-university-e-learning/
      content: '[&#8230;] want to use these. However, it would be really useful if there
        were a combination API and course site wide macro facility that would allow me
        to enter something like the following in the HTML for my [&#8230;]'
      date: '2015-01-20 10:54:40'
      date_gmt: '2015-01-20 00:54:40'
      id: '937'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: 'Concrete lounge #1 &#8211; Helping learners find correct, up-to-date course
        information | The Weblog of (a) David Jones'
      author_email: null
      author_ip: 192.0.99.86
      author_url: https://davidtjones.wordpress.com/2015/02/03/concrete-lounge-1-helping-learners-find-correct-up-to-date-course-information/
      content: '[&#8230;] now implemented a simple &#8220;macro&#8221; facility. This
        has been done [&#8230;]'
      date: '2015-02-03 12:27:19'
      date_gmt: '2015-02-03 02:27:19'
      id: '938'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
**UPDATE (Feb 2015):** Have implemented a version of this using a simple Javascript approach. Not quite course site wide, but functional

In the process - like an increasing number of Oz academics - updating a course site for a new semester. I'm fairly happy with the site as it stands and the Moodle copy process does a good job of updating links (i.e. the link to assignment 1 now links to assignment in the new course site, not the old). The trouble is that the current process doesn't currently do a good job with dates and other values that may change from semester to semester.

So I'm wondering

1. How one might implement a course site wide macro facility?
2. Alternatively, what existing feature of Moodle am I unaware of?

### The problem

Throughout the course site there are a range of labels that will exist each semester, but which may have slightly different values. Some examples include:

- Due dates for assessment.
    
    Assignment 1 tends to be due at the start of week 5, but week 5 has a different date each semester.
    
- Weekly titles.
    
    The course is structured by week. Each week has a particular question as its title. I like to tweak these titles based on what works (or doesn't).
    

Since these "labels" are used in multiple places in the course site, if the values of these labels have to change, I have to find all uses of these labels and change them manually.

### One solution type - a macro facility?

I'd find it useful if there was a central macro facility where I could define a range of variables and their values. For example

- ASSIGNMENT\_1\_DUE\_DATE = 31st March - start of week 5
- WEEK\_10\_TITLE = "Digital citizenship"

On the course site, I would then use the variable (WEEK\_10\_TITLE), rather than the value. Some technology would replace the variable with the value prior to display to the user.

### Implementation?

Really thinking aloud here.

Given the cost of changing the Moodle core - I assume putting something like this in Moodle would require a change to core - that's probably not an option in the short-term. But this is also where existing discussion of an idea like this may have occurred or been addressed.

The only potential method by which I could implement something like this that springs to mind is Javascript. i.e. include some javascript in all the Moodle course pages that implement some form of macro substitution on the client's end.

### Post script

This is an example of attempting to live within the constraints of the system. A longer term solution would be to break out of it entirely. Give up the question of fixed weeks, fixed due dates for assignments, the idea of a course remaining so consistent that only a few values need to change each semester etc. On the last point, there will be more detailed changes made. A feature like this simply gives more time to make those "better" changes by saving time on the more menial requirements.

I also think it's an interesting example of how institutions that are increasingly moving to standardised, industrialised, approaches to supporting learning & teaching are doing it in ways that they are either unaware of gaps in their systems/processes or are unable to conceptualise how this might work.