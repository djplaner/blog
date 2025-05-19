---
categories:
- website
date: 2009-01-06 09:34:46+10:00
next:
  text: Reflections and Implications from Webfuse - Domain languages
  url: /blog/2009/01/07/reflections-and-implications-from-webfuse-domain-languages/
previous:
  text: Webfuse usage statistics - Online assignment submission
  url: /blog/2009/01/05/webfuse-usage-statistics-online-assignment-submission/
title: Implementing the rotating banner image
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: EasyCrop - preparing photos for the rotating banner &laquo; The Weblog of
        (a) David Jones
      author_email: null
      author_ip: 74.200.245.227
      author_url: https://djon.es/blog/2009/02/01/easycrop-preparing-photos-for-the-rotating-banner/
      content: '[...] - preparing photos for the rotating&nbsp;banner  As part implementation
        requirements for the rotating banner image on this blog I needed some software
        to crop photos to the required dimensions. Increasingly, [...]'
      date: '2009-02-01 08:59:02'
      date_gmt: '2009-01-31 22:59:02'
      id: '2068'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
I've [mentioned some plans](/blog/2008/12/28/plans-for-implementing-rotating-banner-image/) to implement a rotating banner image on this blog. As you may have picked up from this post, if you're looking at the site, that such a rotating banner image has been implemented. Here's the story.

It's one of pragmatism. The plan of not using an external server, after a minimum of searching, was proving to be a little more difficult than I thought. So rather than waste time I've simply re-used the approach I used on my old site. i.e. this [script](http://cq-pan.cqu.edu.au/WF/object/ImageRotator/?header=image/jpg). At the moment the script simply does a loop through a list of images stored in the file system of the host web server.

After purchasing the "CSS Edit" ability from Wordpress.com (about $AUD20 for a year) I've added a bit of CSS to call the above script and hey presto, rotating banner image.

In the spirit of release early, release often, I hope to continue modifying this to move it further away from the original design and towards some of the newer plans. In particular, the use of Flickr to host the images.