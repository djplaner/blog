---
categories:
- addie
- elearning
date: 2009-02-02 15:22:10+10:00
next:
  text: More detail on the money burner
  url: /blog/2009/02/03/more-detail-on-the-money-burner/
previous:
  text: What is a PLE? More than a suite of tools? More than social media?
  url: /blog/2009/02/02/what-is-a-ple-more-than-a-suite-of-tools-more-than-social-media/
title: Data mining of online courses - dominant assumptions and innovation potential
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: 'Getting half-baked ideas out there: improving research and the academy
        &laquo; The Weblog of (a) David Jones'
      author_email: null
      author_ip: 72.233.96.150
      author_url: https://djon.es/blog/2009/02/15/getting-half-baked-ideas-out-there-improving-research-and-the-academy/
      content: '[...] is not a new set of questions. The data mining of such logs is quite
        a common practice and has a collection of approaches and publications. So, the
        questions [...]'
      date: '2009-02-16 09:46:02'
      date_gmt: '2009-02-15 23:46:02'
      id: '2090'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
For almost as long as [learning management systems](http://en.wikipedia.org/wiki/Learning_management_system) have been around their have been researchers and technologists investigating how the usage logs of these systems can be harnessed to inform and improve learning and teaching. For a little while I was sort of involved in a [project](http://cddu.cqu.edu.au/index.php/Category:Blackboard_Indicators) that would look at some of this - interest has waned in line with organisational realignments.

A [colleague](http://beerc.wordpress.com/), however, is continuing on with a project in this area. The following is an attempt to reflect about what little I know about the area and see if there is anything of interest to Col. In the following I am trying to identify the dominant assumptions underpinning this sort of work in order to see if there are any holes which might be ripe for exploitation.

**Disclaimer:** Until recently I haven't paid much attention to the literature in this area and my recent reading was sparse, interrupted and incomplete. Hence the following could do with the insights of those with more knowledge of the literature to correct oversights, misunderstandings and naive assumptions.

### What are we talking about

The common approach to this process uses automated evaluation of system logs and databases (e.g. [Zorrila and Alvarez, 2008](http://portal.acm.org/citation.cfm?id=1381300.1381531&coll=&dl=), [Hung & Zhang, 2006](http://www.editlib.org/index.cfm?fuseaction=Reader.ViewAbstract&paper_id=24009); and [Heathcote and Dawson, 2005](http://eprints.qut.edu.au/archive/00002368/01/2368.pdf)) using some form of data mining or similar technology in order to provide additional information for teaching staff or Universities about the quality of the student experience. The typical form is take the usage logs and databases from a learning management system, put them into some sort of data warehouse system and generate reports for academics and management.

This type of work typically seems to differ on a few characteristics:

- The technology/algorithms used to analyse the system logs and present the results.
- The type of theory of learning or quality online presence that is used to "measure" the quality of the online course or the student experience.

I guess also there will be different communities within e-learning that take a different slant on this work. For example, I believe the intelligent tutorial system folk probably have a large amount of research and literature focused at analysing the student experience using data mining in order to make informed decisions about what to advise the student to do next.

### Dominant assumptions and opportunity for innovation

Col is doing some of this work as part of a research project within his Masters study. So, I'm assuming he is keen to get into some innovation, to do something that hasn't been done yet. So, in the following I'm trying to identify the dominant assumptions that, at least in my experience, seem to characterise this work. The idea is that over turning these assumptions might reveal an interesting line of work.

The assumptions that I'm thinking about (are there more?) include:

- Limit and focus to the LMS logs.  
    Analysis of LMS logs tells only a very small part of the story about students, staff and their interactions within learning and teaching. Even if the focus remains on the logs of computer systems, most students and staff will be leaving a fairly large trail of usage information through a range of other computer systems that could be combined with those in the LMS.
    
    This is especially important as the type of information gathered by mining LMS logs is limited by the nature and design of the LMS. For example, the Webfuse system (Jones and Gregor, 2006) has a design that by default allows open access to all resources. That is no requirement for users to login. Each system has its own design limits.
    
- Kaplan's law of instrument continued.  
    Most of this work is done with similar tools. System logs and databases passed through statistics analysis and/or data mining technology to generate information. While useful, the tendency to focus just on these technologies has the potential to lead to flaws due to [Kaplan's law of instrument](/blog/2008/11/19/tool-users-research-hammers-and-the-law-of-instrument/). Everything looks like a nail, if all you have is a hammer. Are there alternative tools or approaches that can be used, which may be base on different approaches and hence reveal different insight.

- Emphasis on quantitative analysis alone.  
    Simple log usage figures only tell a very small part of story of the student experience. Much of it is hidden within the words and emotions used and experienced by participants. It's increasingly widely recognised that a multi-method approach for research is effective through each method covering limitations of other methods. Marrying quantitative analysis with textual analysis (e.g. [Leximancer](http://www.leximancer.com/)), or qualitative or specific feedback from students (e.g. [course barometers](https://djon.es/Publications/barometer_2.pdf); Jones, 2002) might be interesting.
- Presenting information for staff and the institution, not the students.  
    The aim for most seems to be to make the information available to the teaching staff so they can reflect and make improvements. Have seen little work where this information is made pro-actively available to the students so they can use it to guide their learning or student experience. For example, if a student were to see a huge spike in visitations to a particular page that they hadn't visited, they may consider taking a look.
- How is the insight generated used?  
    Almost all of the research literature I've seen so far shows this information solely being used by researchers after the fact. i.e. after the term has finished they've analysed the data to see what lessons they can learn. The information may not even be shared with the teaching staff and they rarely seem to talk to academic staff. It would be interesting to see what would happen if you worked with academic staff during a term harnessing a range of different analysis/mining tools to provide information that they could respond to. This would allow tracking of what happens and the generation of insight and requirements within a real context of use, which is likely to be more useful and insightful than requirements gather out of context.

### References

Heathcote, Elizabeth and Dawson, Shane (2005) Data Mining for Evaluation, Benchmarking and Reflective Practice in a LMS. In Proceedings E-Learn 2005: World conference on E-learning in corporate, government, healthcare & higher education, Vancouver, Canada.

David Jones, Student feedback, anonymity, observable change and course barometers, World Conference on Educational Multimedia, Hypermedia and Telecommunications, Denver, Colorado, June 2002, pp. 884-889.