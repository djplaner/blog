---
title: Plans for implementing rotating banner image
date: 2008-12-28 15:50:08+10:00
categories: ['website']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Implementing the rotating banner image &laquo; The Weblog of (a) David Jones
      author_email: null
      author_ip: 72.233.96.151
      author_url: https://djon.es/blog/2009/01/06/implementing-the-rotating-banner-image/
      content: '[...] the rotating banner&nbsp;image  I&#8217;ve mentioned some plans
        to implement a rotating banner image on this blog. As you may have picked up from
        this post, if [...]'
      date: '2009-01-06 09:34:53'
      date_gmt: '2009-01-05 23:34:53'
      id: '1931'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
**Problem:** Implement a [rotating banner image](/blog2/2008/12/28/rotating-banner-images-in-wordpress-the-last-missing-puzzle-piece/) on this blog which is hosted by [Wordpress.com](http://wordpress.com/). This means I cannot install any Wordpress themes that automatically support bnner rotation (e.g. the [Mandigo](http://www.onehertz.com/portfolio/wordpress/) theme suggested by [Will Taylor](http://wt.similibus.org/).

There is a [known approach](http://en.forums.wordpress.com/topic/random-image-header-tutorial?replies=22#post-36298) that relies upon you having some disk space on a server that will let you run a PHP script. I'd like to avoid using that approach.

Instead, my hope is to cobble something together using Flickr, Pipes and a bit of CSS. The following is an attempt to outline what steps are necessary to test this out.

### Flickr constraints

First stop is to see if the conditions of use on Flickr will allow this. Yep, the [Flickr Community Guidelines](http://www.flickr.com/guidelines.gne) seems to indicate that you can use your content on other sites, just make sure that is a link back.

So, I should be able to show a flickr photo in the banner as long as there is a link back to the page on Flickr it comes from.

### Modify CSS to get image from pipes

Next step is to see if I can modify the CSS of the theme I'm using to include a banner image, and then perhaps to include a banner image from a [Pipes](http://pipes.yahoo.com/).

### Use pipes to extract a single image from a gallery

Next step, would be to figure out how to write a pipe that will extract a single image from a Flickr gallery. Once that's working figure out how to loop through the contents of the gallery so that rotation through the images is achieved.

### Figure out the link back to the flickr photo page

If that's all working I need to figure out how to provide a link back to the original flickr page. A banner image in a blog header usually returns back to the home page for the blog. Thinking perhaps some additional text with the name of the image could be included with a link back to the flickr photo page.