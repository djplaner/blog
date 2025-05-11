---
categories:
- bim
date: 2009-12-15 15:53:40+10:00
next:
  text: BIM - getting student registration working
  url: /blog2/2009/12/17/bim-getting-student-registration-working/
previous:
  text: Here come the indicators, wait for the task corruption
  url: /blog2/2009/12/15/here-come-the-indicators-wait-for-the-task-corruption/
tags:
- moodle
title: BIM and Moodle development - a more coherent overview found?
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: BIM &#8211; getting student registration working &laquo; The Weblog of (a)
        David Jones
      author_email: null
      author_ip: 74.200.245.226
      author_url: https://djon.es/blog/2009/12/17/bim-getting-student-registration-working/
      content: '[...] The Weblog of (a) David Jones Another voice in the blogosphere    &laquo;
        BIM and Moodle development &#8211; a more coherent overview&nbsp;found? [...]'
      date: '2009-12-17 10:03:03'
      date_gmt: '2009-12-17 00:03:03'
      id: '2894'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
Today has been a fairly frustrating today with a mixture of organisational "stuff" and an increasing level of annoyance at the state of the public documentation around Moodle development slowing down [BIM](/blog2/2009/12/14/getting-back-into-bim-summary-and-way-forward/) development. That state is essentially with stuff all over the place, no coherent path through it and regularly discrepancies between advice from different sources, or sometimes the same. But that's the nature of documentation and open source projects.

The one bright spot today has been stumbling over [this book](http://www.packtpub.com/moodle-1-9-extension-development/book) which appears to fill the hole. Even if it is commercial. Having said that, the realease as writing nature of the book and some other aspects (donations to moodle) seems to indicate an enlightened company. On first skim the book looks good. Time will tell. Though, I am guessing that due to the nature of the type of book, complexity of the task and that it's still being written there will be some rough edges (already submitted my first errata), or areas not covered.

Bugger, small problem. The one aspect I'm currently struggling with (use of moodleform\_mod within a Module to create a new form - i.e. not in mod\_form.php) is covered in their example. However, the authors have used moodleform and not moodleform\_mod as the base/abstract class. I thought that was a no no?

Well, if I take their approach and use moodleform. It appears to get past the syntax errors being caused by my lack of understanding. Perhaps I just need to progress with that until future enlightenment.

So some progress today.