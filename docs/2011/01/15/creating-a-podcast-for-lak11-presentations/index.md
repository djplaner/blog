---
title: Creating a podcast for LAK11 presentations
date: 2011-01-15 14:42:11+10:00
categories: ['indicators', 'lak11']
tags: ['lak11']
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: Sylvia Currie
      author_email: sylvia@webbedfeat.com
      author_ip: 66.183.117.209
      author_url: http://blog.webbedfeat.com
      content: Excellent! And absolutely fine to move those files. BTW, I don't know why
        SCoPE is behaving like that -- redirecting you to the home page when you access
        files. I'll look into it!
      date: '2011-01-15 15:07:31'
      date_gmt: '2011-01-15 05:07:31'
      id: '3224'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: davidtjones
      author_email: davidthomjones@gmail.com
      author_ip: 124.185.51.1
      author_url: https://djon.es/blog/
      content: 'Thanks Sylvia.
    
    
        I think the behaviour is built into the Moodle "file.php" file.  The URL for one
        of the files on the SCOPE Moodle is http://scope.bccampus.ca/file.php/365/audio_recordings/LAK11_JAN07-2011.mp3
    
    
        I''m assuming that either built into file.php, or perhaps as a result of the configuration
        of the LAK11 Moodle course, it needs your web browser to have a cookie set to
        access the file.  If I visit that URL after visiting the LAK11 Moodle site, it
        works fine.  If I visit the URL in a fresh browser instance that hasn''t logged
        into the LAK11 Moodle site, then it redirects me here http://scope.bccampus.ca/login/index.php?loginguest=true'
      date: '2011-01-15 15:20:40'
      date_gmt: '2011-01-15 05:20:40'
      id: '3225'
      parent: '3224'
      type: comment
      user_id: '1'
    
pingbacks:
    []
    
---
I'm currently participating in the [Learning and Knowledge Analytics MOOC](http://learninganalytics.net/) being run by George Siemens and others. This post outlines the process I used to create a [podcast of the presentations](http://feeds.feedburner.com/lak11podcast) (click on that link if you want to subscribe to the podcast) being given as part of the course.

### Why?

The presentations are taking place within Elluminate and Elluminate recordings are made available. So why a podcast? Simply put the asynchronous and audio only nature better matches my preferences and context. So, I've repeated a process I use for the [PLE/PLN symposium](/blog2/2009/10/16/podcast-for-presentations-at-the-ples-plns-symposium/). More details below.

### How?

The basic process is

- Bookmark the mp3 files using [del.icio.us](http://www.delicious.com/) using the tag _lak11podcast_.
- Pass the RSS for that those tags produced by del.icio.us through [feedburner](http://www.feedburner.com/) to generate a [podcast](http://feeds.feedburner.com/lak11podcast).
- Subscribe to [the podcast](http://feeds.feedburner.com/lak11podcast) using iTunes or other software.

The one difference between this podcast for LAK11 and the [PLE/PLN podcast](/blog2/2009/10/16/podcast-for-presentations-at-the-ples-plns-symposium/), is that I couldn't bookmark the original mp3 files. These files are made available via the [LAK11 Moodle course](http://scope.bccampus.ca/course/view.php?id=365). Attempting to access the files directly results in a redirect to the home page for the SCOPE Moodle instance where you can login as a guest and view the files.

Works fine if you are a person on the web, but podcast software like iTunes isn't that smart.

The solution I adopted here was to copy the MP3 files out of the Moodle course into a location without a re-direct. In this case drop box. I was a bit reluctant to do this as these aren't my files, however, I'm assuming that given the nature of the MOOC that this should be okay. If not, the files will be removed.

### Limitations

At the moment, production of the podcast relies on new mp3 files being tagged by me with the tag _lak11podcast_. Would probably be more responsive if feedburner was set up to use anything anyone tagged with lak11podcast. For now, I'm leaving the restriction simply to save time and let me get on with some more reading. Happy to change it if people ask.