---
categories:
- dojo
date: 2006-08-01 13:43:53+10:00
next:
  text: Jenny Anastasi' presentation
  url: /blog2/2006/08/28/jenny-anastasi-presentation/
previous:
  text: Information literacy skills causing problems with BAM
  url: /blog2/2006/07/31/information-literacy-skills-causing-problems-with-bam/
title: Including Dojo in pages
type: post
template: blog-post.html
---
Based on various sources including [the Dojo "manual"](http://manual.dojotoolkit.org/WikiHome/DojoDotBook/BookScript)

Three starting sections in HEAD

1. setting flags - this one is optional
    
    djConfig = { isDebug: false };
    
2. dojo bootstrap - I think I found that this didn't work as a single tag - had to be the open/close tag set
    
3. define the packages to be used
    
    dojo.require("dojo.event.\*"); dojo.require("dojo.io.\*"); dojo.require("dojo.widget.\*");
    

### Path to dojo

With Webfuse - dojo is installed at `/webfuse/tools/dojo/`