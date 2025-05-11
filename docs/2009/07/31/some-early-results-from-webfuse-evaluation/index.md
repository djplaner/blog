---
categories:
- chapter-4
- design-theory
- elearning
- phd
- thesis
- webfuse
date: 2009-07-31 23:43:21+10:00
next:
  text: '"How the LMS - as enterprise system - warps the practice of L&#038;T"'
  url: /blog2/2009/08/02/how-the-lms-as-enterprise-system-warps-the-practice-of-lt/
previous:
  text: Thinking about evaluating Webfuse (1996 through 1999) - evaluation of an LMS?
  url: /blog2/2009/07/31/thinking-about-evaluating-webfuse-1996-through-1999-evaluation-of-an-lms/
title: Some early results from Webfuse evaluation
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: 'Evaluation of Webfuse course site feature usage: 2006 through 2009 &laquo;
        The Weblog of (a) David Jones'
      author_email: null
      author_ip: 66.135.48.208
      author_url: https://djon.es/blog/2009/08/02/evaluation-of-webfuse-course-site-feature-usage-2006-through-2009/
      content: '[...] of Webfuse course site feature usage: 2006 through&nbsp;2009  In
        a recent post I messily wrote about the start of the process of evaluating the
        use of Webfuse for my thesis. This [...]'
      date: '2009-08-02 13:09:11'
      date_gmt: '2009-08-02 03:09:11'
      id: '2679'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: 'PhD Update #19 &#8211; Falling just a little short &laquo; The Weblog of
        (a) David Jones'
      author_email: null
      author_ip: 66.135.48.204
      author_url: https://djon.es/blog/2009/08/02/phd-update-19-falling-just-a-little-short/
      content: '[...] of the use of Webfuse from 1996 through 1999. Explained somewhat
        in three posts: early thinking, some more thinking and some early results and
        results of evaluation for [...]'
      date: '2009-08-02 13:45:08'
      date_gmt: '2009-08-02 03:45:08'
      id: '2680'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The following contains some early results from the evaluation of Webfuse course sites as mentioned in the [last post](/blog2/2009/07/31/thinking-about-evaluating-webfuse-1996-through-1999-evaluation-of-an-lms/). The aim is to get a rough initial feel for how the course sites created for Webfuse in the late 90s and early 00s stack up using the framework produced by Malikowski et al (2007). As opposed to other PhD work, this is a case of "showing the working".

### How many page types?

First, let's see how many page types were used each year. The following table summarises the total number of pages and number of different page types (in some years there were page types with different names that had only very slightly different functionality - the following stats are rough and don't take that into account) used in each year.

| Year | \# pages | \# page Types |
| --- | --- | --- |
| 1999 | 4376 | 27 |
| 2000 | 3058 | 39 |
| 2001 | 1155 | 23 |
| 2002 | 9099 | 42 |
| 2003 | 9302 | 40 |

Can see from the above that the number of overall pages managed in Webfuse drops significant drop from 2000 to 2001. 2001 is when the new default course site structure was put in place and when (I think) the courses 85321 and 85349 (which I taught) stopped included the archives of previous offerings. **Check this. May need to look at excluding from consideration some of these?**

During this time there were some page types which had different names, so would be counted more than once in the above, but were essentially the same. **Count the same page types once**.

I have to save the commands to do this somewhere, may as well do it here

```
find . -name CONTENT -exec grep PageType {} ; > all.pageTypes
sed -e '1,$s//1/' all.pageTypes | sort | uniq -c > all.pageTypes.count

```

### Calculate the percentage of page type usage per framework

The next step is a simple calculation. Allocate each page type to one of one of the categories of the Malikowski et al (2007) framework and show the percentage of the pages managed by Webfuse that fall into each category. This isn't exactly what Malikowski et al (2007) count, the count the percentage of courses that use features in each category.

The Malikowski et al (2007) framework includes the following categories:

- transmitting content;
- creating class interactions;
- evaluating students;
- evaluating course and instructors;
- computer based instruction.  
    **Not included** - there are no Webfuse page types that provide functionality that fits with this category.

The following table shows the percentage of pages managed by Webfuse that fall into each category per year. It's fairly obvious from the first year done - 1999, and confirmed with the second, that this approach doesn't really say a lot. Time to move on.

| Category | 1999 | 2000 | 2001 | 2002 | 2003 |
| --- | --- | --- | --- | --- | --- |
| Transmitting content | 97.5% | 84.5% |  |  |  |
| Class interactions | 1.9% | 13.5% |  |  |  |
| Evaluating students | 0.1% | 1.5% |  |  |  |
| Evaluating course | 0.5% | 0.6% |  |  |  |

### Calculate the % of courses using each category

In this stage I need to:

- Count the number of courses in each year.
- Count the % of courses that have features of each category.

Technically, all of these courses will have features for transmitting content, so all those will be 100%, so I've not included it. **Need to recheck the Malikowski definition.**

Also, 2001 seems to be missing a couple of the main terms, so it's had to be excluded - for now. **See if the missing terms can be retrieved.**

| Category | 1999 | 2000 | 2002 | 2003 |
| --- | --- | --- | --- | --- |
| Number of course sites | 190 | 175 | 315 | 309 |
| Class interactions | 7.9% | 43.5% | 11% | 66.6% |
| Evaluating students | 2.6% | 6.3% | 12% | 21.7% |
| Evaluating course | 9.5% | 7.5% | 14% | 91.6% |

Commands I used to generate the above

```
find aut2000 spr2000 win2000 -name CONTENT -exec grep -H PageType {} ; > course.pageTypes
...vi to get period/course:pageTypeName
sort course.pageTypes | uniq  | sort -t: -k2 > course.pageTypes.uniq
... edit to move the page types around

```

Now, there are some interesting results in the above. **Have to check the 2000 and 2002 result for class interactions, unusual dip.**.

The almost 92% of courses with a course evaluation feature in 2003 is due to the raise of the course barometer explained in [Jones (2002)](https://djon.es/Publications/barometer_2.pdf)

Too late to reflect anymore on this. Off to bed.

### References

David Jones, Student feedback, anonymity, observable change and course barometers, World Conference on Educational Multimedia, Hypermedia and Telecommunications, Denver, Colorado, June 2002, pp. 884-889.

Malikowski, S., Thompson, M., & Theis, J. (2007). A model for research into course management systems: bridging technology and learning theory. Journal of Educational Computing Research, 36(2), 149-173.