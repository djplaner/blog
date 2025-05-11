---
categories:
- edc3100
- edu8117
date: 2016-08-05 10:46:29+10:00
next:
  text: How and why do people use the Moodle Book module?
  url: /blog2/2016/08/07/how-and-why-do-people-use-the-moodle-book-module/
previous:
  text: Planning changes to EDC3100 assignment 1
  url: /blog2/2016/07/13/planning-changes-to-edc3100-assignment-1/
title: Valuing the "residue of experience" a bit more
type: post
template: blog-post.html
---
For a while now I have been drawing on the following quote from Riel and Polin (2004)

Over time, the residue of these experiences remains available to newcomers in the tools, tales, talk, and traditions of the group. In this way, the newcomers find a rich environment for learning. (p. 18)

to explain why I encourage/require the use of various types of social media (blogs, social bookmarking, feed readers) in my courses. [This 2014 post](/blog2/2014/08/15/joining-the-swarm-what-a-course-might-be/) identifies the problem (what happens in a course site, stays and dies in a course site) and how the social used in these courses helps address that problem.  If you do a Google search for _edc3100 blog_, you will get another illustration of how at least some of the residue of experience remains available to newcomers in at least one of the courses.

The problem is that this year has revealed that the design of the course doesn't yet value that residue of experience, at least not in terms of the main value measure for many students - assessment. Students gain marks for writing blog posts that link to posts from other students, but the code that does this marking only recognises currently enrolled students. Linking to the broader residue of experience doesn't count.

Interestingly, this has only become an issues this year. Only this year have students been asking why they missed out on marks for links to other ("old") student posts. Leaving aside why it's only started this year, this post documents the move to valuing the residue of experience.

After implementing the code below, it appears that at least 28 (about 25%) students this semester have linked to blog posts from students in previous offerings of the course. Would be interesting to explore this further. See how prevalent the practice has been in previous courses. Update [these visualiations](/blog2/2013/03/18/visualising-the-blog-network-of-edc3100-students/) to show the connections between offerings.

### What I need to do

The process will be

- Refamiliarising myself with how the "valuing" is currently done.
- Planning and implementing how to value the residue of experience.
- Figuring out if/how to check how often the residue of experience has been used.

### How it is currently valued

Some perl code does the work.  Details follow.

_BlogStatistics_ class gathers all information about the blogs for students in the current course offering.  A method _generateAllStatistics_ does some of the grunt work.

But this class also creates a data member _MARKING_ for each student. Based on the _Marking_ class and its _GenerateStats_ method. This class gets the content from the _bim\_marking_ table (i.e. all the posts by the student).

_GenerateStats_ accepts a reference to a hash that contains links to all the other blogs in the course (for the specific offering).  It calls _DoTheLinks_ (gotta love the naming) passes it the hash ref to do the count.

One question is how much old data do I currently have?  Seems like there's only the 2015 and 2016 data easily accessible.

### Planning and implementation

One approach would be

- _BlogStatistics_ generates a list of old student blog URLs
    - add _BlogStatistics::getOldStudentBlogs_ that creates $%_BlogStatistics::OLD\_BLOGS_ **DONE**
- _BlogStatistics_ passes this into each call to _Marking::GenerateStats_  **DONE**
- _Marking::GenerateStats_ would pass this onto _Marking::DoTheLinks_ **DONE**
    - also increment POSTS\_WITH\_STUDENT\_LINKS if a link is to an old student blog **DONE**
    - increment POSTS\_WITH\_OLD\_STUDNET\_LINKS if a link is to an old student blog **DONE**
- Modify the report generator to show OLD links **DONE**