---
title: UnAPI as a basis for Web 2.0 course sites
date: 2006-09-20 20:15:32+10:00
categories: ['web-20-course-sites']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

**Background Problem**

Everytime someone is introduced to Webfuse they wonder why we haven't sold it, made it available to other organisations.

Apart from being lazy, the real reason doesn't seem to be accepted all that easily. i.e. that the whole idea behind Webfuse is that it is the "glue" between the various bits of software and the CQU context and consequently very specific to CQU isn't widely accepted.

**Making it more general**

So with the web 2.0 course site idea (must get a better name - Webfuse 2.0?) need to think about a way of making it more portable to other institutions.

One approach would be to support the heavy weight education standards - IMS, SCORM and the like. I have a problem with that approach. Similarly, web services.

Some of the lightweight service stuff might work.

**A solution?**

[UNAPI](http://unapi.info/) looks like it might be a solution. From the UNAPI description

> unAPI is a tiny HTTP API any web application may use to co-publish discretely identified objects in both HTML pages and disparate bare object formats. It consists of three parts: an identifier microformat, an HTML autodiscovery link, and three HTTP interface functions, two of which have a standardized response format.

The idea would be that obtaining all the institutional information (course codes, names, students? etc) would be done via an UNAPI service. So porting it to another institution would be implementing that API for that institution.