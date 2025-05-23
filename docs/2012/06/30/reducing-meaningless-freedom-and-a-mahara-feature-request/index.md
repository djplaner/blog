---
categories:
- design-theory
- elearning
- webfuse
date: 2012-06-30 11:11:05+10:00
next:
  text: '"Why do (social) networks matter in teaching &#038; learning?"'
  url: /blog/2012/07/07/why-do-social-networks-matter-in-teaching-learning/
previous:
  text: People and e-learning - limitations and an alternative
  url: /blog/2012/06/29/people-and-e-learning-limitations-and-an-alternative/
title: Reducing meaningless freedom and a Mahara feature request
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: Peter Albion (@palbion)
      author_email: palbion@twitter.example.com
      author_ip: 121.223.74.169
      author_url: http://twitter.com/palbion
      content: Early experiences (mid-1990s) of students creating webpages with images
        missing because they were linking to a local drive and not the server moved me
        to advise students to test websites before submission on a different computer
        where they are just any user. That should work to avoid non-functioning submissions
        but of course some students don't bother or cannot manage that step either.
      date: '2015-05-07 20:42:30'
      date_gmt: '2015-05-07 10:42:30'
      id: '385'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: David Jones
      author_email: davidthomjones@gmail.com
      author_ip: 139.86.69.32
      author_url: https://djon.es/blog/
      content: 'In this case reducing meaningless freedom could have been done by having
        the submission system run a link checker over the submitted site. If there were
        any broken links, notify the student and reject the submission (until all the
        links worked).
    
    
        My problem from yesterday was that Moodle largely retains the filenames used by
        the students on their computer.  So with an assignment where they submit three
        files for three different parts, I can''t easily identify which file matches which
        part. A small pain when marking manually, a huge pain when trying to do some additional
        processing via scripts.'
      date: '2015-05-08 08:41:36'
      date_gmt: '2015-05-07 22:41:36'
      id: '386'
      parent: '385'
      type: comment
      user_id: '1'
    
pingbacks:
    []
    
---
_Note:_ An update to this post included at the end.

I'm currently finalising results for a course with 250+ students spread across multiple campuses and online. The final large assignment - worth 70% of the final mark - requires that students create a portfolio (are people still using the term "eportfolio"?) in Mahara and submit it via the institutional assignment submission system.

Due to the nature of the portfolio content and concerns about privacy of school student (it's a pre-service teacher course) the portfolio cannot be opened up to everyone. Not to mention the fact that many of the students retain this fear that someone is going to copy their work. So, students have to create this multi-page, multi-resource portfolio in Mahara and make sure that certain people can access the portfolio.

With 250+ students it was always going to be the case that a decent handful would have problems, even with reasonable instructions. And it is this decent handful that is creating extra workload for the teaching staff. Additional workload that could be avoided if a principle we formulated in early work around assignment submission - reduce meaningless freedom - was applied to Mahara.

The following outlines that principle and outlines a feature request for Mahara that might help.

### Reduce meaningless freedom

Online assignment submission was one of the first applications of online learning we explored back in the mid-1990s in our courses with large numbers of distance education students (Jones and Jamieson, 1997). The early systems were not that well designed and increased the workload on the marker (sorry Kieren). However, they did help with a range of improvements over the traditional physical assignment submission process.

From this experience, we developed the principle of "reduce meaningless freedom". Here's how it was described in Jones (1999)

> An important lesson from the on-going development of online assignment submission is to reduce the amount of “meaningless freedom” available to students. Early systems relied on students submitting assignments via email attachments. The freedom to choose file formats, mail programs and types of attachments significantly increased the amount of work required to mark assignments. Moving to a Web-based system where student freedom is reduced to choosing which file to upload was a significant improvement.

The problem was that when marking large numbers of assignments, you want to get into a routine. You can only get into a routine if certain important aspects are the same (e.g. file formats, file names etc, the ability to access a Mahara portfolio). The trouble is that if you have a large number of people completing a process, if there is any flexibility in the process they will complete it in different ways (including not completing it properly).

This is not a problem that can be solved by improving the instructions or applying a checklist. With a large enough number of people, there will be people who can't follow those instructions or ignore the checklist.

Consequently, the information system has to be designed to remove any freedom to vary from the process. It shouldn't remove all freedom, just those that aren't important to the outcome of the process but will increase workload in processing. For example, we want the students to be able to express their creativity with their Mahara portfolios. We just don't want them to have the freedom to submit a URL for a portfolio that we can't access.

The system should remove, or at least limit, this freedom.

### Mahara feature request

The problem here is that for people new to Mahara, it is very difficult to check who can access a complex, multi-page portfolio. I do know that there is a way to give access to a complex, multi-page portfolio: you create a collection, add the pages to that collection, and create a secret URL that the collection. This is the process we described to students. The trouble is that the students have to choose to follow this process and they are free not to.

You could be hard about this and be very explicit. "If you don't do this you will fail!". But that doesn't create a positive learning environment I'd like to have in my courses and fails to recognise that our tools should be helping us achieve our goals.

What would be useful, is if Mahara had a "show/check access" feature. Where a person creating a Mahara portfolio could submit the URL and Mahara would generate a report of who could access which components of that portfolio. It would recurse through all the Mahara links accessible from that URL and report on who could access those links.

Having this as a feature that people have to choose to use still involves some freedom. To remove that freedom a bit more, this process could run in the background and the outcome could be made visible via the Mahara interface. For example, when editing a page that contains links to other parts of Mahara, the interface could add an appropriate label explaining who can access those links.

### An update

Thanks to @icampus21.com it is revealed to me that Mahara already has this feature. That its share facility does show what is accessible. Kudos to the Mahara developers. Now I don't follow @icampus21.com on Twitter and pretty sure they don't follow me. So this is a nice bit of learning thanks to Twitter, hash tags and @icampus21.com

This begs the question as to why I wasn't already aware of this. After all, I'm responsible for this course and somewhat computer literate. A significant part of the answer has to be the limitations of my approach to learning about Mahara. But other contributing factors would include that this feature is neither explicitly obvious from using Mahara nor in the preparation/resources provided by my current institution.

One perspective is that there is too much freedom in the way the institution allows the use of Mahara in courses. It should remove the freedom I have from getting this far into a semester without being aware of this. But perhaps it can also be addressed by making it more explicit/obvious in Mahara?

Then there is the whole robustness versus resilience perspective as argued by [Dave Snowden](http://rajile.com/2011/05/24/robustness-vs-resilience/).

### References

Jones, D., & Jamieson, B. (1997). [Three Generations of Online Assignment Management](/blog/publications/three-generations-of-online-assignment-management/). In R. Kevill, R. Oliver, & R. Phillips (Eds.), (pp. 317-323). Perth, Australia.

Jones, D. (1999). [Solving some problems with university education: Part II.](/blog/publications/solving-some-problems-with-university-education-part-ii/), Proceedings of AUSWEB'99, Balina, Australia.