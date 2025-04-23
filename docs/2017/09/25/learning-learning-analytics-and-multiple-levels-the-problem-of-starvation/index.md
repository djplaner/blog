---
title: "Learning, learning analytics and multiple levels: The problem of starvation"
date: 2017-09-25 15:22:13+10:00
categories: ['indicators']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

In which I play with some analytics and use some literature in an attempt to understand why the institutional implementation of learning analytics as a starvation problem (like most institutional attempts to leverage digital technologies). In this context, I'm using the [definition of starvation](https://en.wikipedia.org/wiki/Starvation_\(computer_science\)) from computer science.

### Multiple time scales of human behaviour and appropriate methods

In a section titled "Data from learning on multiple levels: learning is complex", Reiman (2016) writes

> Nathan & Alibali (2010) distinguish between learning in milliseconds and below (biological), seconds (cognitive), minutes to hours (rational), days to months (socio-cultural), and years and beyond (organizational) (p. 134)

Digging into Nathan & Alibali (2010) reveals the following table titled "Time scales of human behaviour and the corresponding areas of study and research methods" (which is in turn adapted from elsewhere).

[![Time Scales of Human Behavior and the Corresponding Areas of Study and Research Methods](images/37271669022_622941e6e0_z.jpg)](https://www.flickr.com/photos/david_jones/37271669022/in/dateposted-public/ "Time Scales of Human Behavior and the Corresponding Areas of Study and Research Methods")

What I find interesting about this is that it places the types of activities a teacher would do at a very different time scale than what an organisation would do. It also suggests that there are very different methods to be used at these very different levels. Suggesting that using a method in the wrong scale will be less than appropriate.

To perhaps draw a long bow, might this suggest that the methods currently being used to support institutional implementation of learning analytics might work fine at the organisational level, but perhaps a little less so at the level of teaching practice? Or perhaps, the limitation arises from the inability to move up and down levels quickly enough.

(Aside: Especially when you consider that the table above doesn't (for me) capture the full complexity of reality. Capturing the time scales is important, but I think it fails to capture the fact that as you move down the _level of study_ you are increasing the quantity and diversity of units of study. i.e. At a system level you might be talking about the Australian higher education sector and its use of learning analytics. There are ~38 universities in Australia that could be studied at the organisational level. Within those organisations there are likely to be 1000s of courses, at least 100s of teaching staff, and 10000s of students. Each very diverse.)

### A case in point

A team I'm a part of has created a online resource that has been used by staff. From the institutionally provided system I can grab the raw logs and perhaps generate the odd image. But I can't do easily do the sort of analysis I'd like to do. What works at the institutional level, doesn't work at the individual course/case level.

But I can engage in some DIY. Jupyter notebooks, Python, plotly, a bit of faffing around with CSV files and....

- Get a list of the people who accessed the resources and how many times they did and turn it into a graph.
- Do the same with the different parts of the resource.
    
    Though it's a bit more difficult given the limited data in the CSV file
    
- And plot the usage against days.

None of this is technically difficult. It's also something that could be useful to others. But they don't have the knowledge and the institution doesn't appear to provide the service.

This particular need is unlikely to receive direct attention. It may well get solved when some enterprise bit of kit gets new functionality. But, if that happens, chances are it will go under-used as users aren't aware of the capability and the technical folk aren't aware of the need.

### A solution?

What if there were methods by which the institution could move up and down the layers? Dip down into the level of hours and days, build some stuff, see it used and then scale up the useful stuff so its "enterprise"?

### References

Reimann, P. (2016). Connecting learning analytics with learning research: the role of design-based research. Learning: Research and Practice, 2(2), 130–142. https://doi.org/10.1080/23735082.2016.1210198

Nathan, M. J., & Wagner Alibali, M. (2010). Learning sciences. Wiley Interdisciplinary Reviews: Cognitive Science, 1(3), 329–345. https://doi.org/10.1002/wcs.54