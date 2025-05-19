---
categories:
- website
date: 2008-12-28 11:53:51+10:00
next:
  text: Plans for implementing rotating banner image
  url: /blog/2008/12/28/plans-for-implementing-rotating-banner-image/
previous:
  text: Update on the website move - google rankings
  url: /blog/2008/12/28/update-on-the-website-move-google-rankings/
title: Rotating banner images in Wordpress - the last missing puzzle piece
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: simillibus
      author_email: wtaylor@simillibus.org
      author_ip: 24.21.138.151
      author_url: null
      content: 'David,
    
        The lovely Mandigo WordPress theme has rotating header banners as a built-in feature
        (check out my site, at http://wt.similibus.org)
    
    
        Mandigo can be downloaded from
    
        http://www.onehertz.com/portfolio/wordpress/mandigo/'
      date: '2008-12-28 13:46:46'
      date_gmt: '2008-12-28 03:46:46'
      id: '1928'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: davidtjones
      author_email: d.jones@cqu.edu.au
      author_ip: 59.154.24.147
      author_url: http://cq-pan.cqu.edu.au/david-jones/
      content: 'G''day Will,
    
    
        Thanks for the pointer, however, I think there is a slight disconnect between
        my requirements and what Mandigo will provide.  Please, correct me if I''m wrong.
    
    
        My blog is hosted on Wordpress.com, not my own server.  It''s my understanding
        that because of this I''m limited to the themes which Wordpress.com provide.  i.e.
        I can''t install my own themes written by others.
    
    
        Yep, it seems the Wordpress.com support forums confirm my assumption.
    
    
        It''s a pity, the theme looks quite good.
    
    
        Of course, there is also the other disconnect, I''m an old geek who hasn''t done
        much coding in recent times and I guess I''m seeking excuses to waste some time
        over the Xmas break.
    
    
        David.'
      date: '2008-12-28 15:28:53'
      date_gmt: '2008-12-28 05:28:53'
      id: '1929'
      parent: '0'
      type: comment
      user_id: '1'
    
pingbacks:
    - approved: '1'
      author: Plans for implementing rotating banner image &laquo; The Weblog of (a) David
        Jones
      author_email: null
      author_ip: 74.200.245.227
      author_url: https://djon.es/blog/2008/12/28/plans-for-implementing-rotating-banner-image/
      content: '[...] The Weblog of (a) David Jones Another voice in the blogosphere    &laquo;
        Rotating banner images in WordPress - the last missing puzzle&nbsp;piece [...]'
      date: '2008-12-28 15:50:30'
      date_gmt: '2008-12-28 05:50:30'
      id: '1930'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
**Update:** The old server that I used to use for my website and also to implement the rotating banner on this blog, is down. It will likely to be down for quite some time.

When I [moved by website](/blog/2008/10/16/the-great-website-move-of-2008/) from my long-term personal server to [Wordpress.com](http://wordpress.com/) the one bit of functionality that I lost was the rotating banner image.

[![Kaikoura Ocean Range Sunrise](images/175187603_d3b17a5487_m.jpg)](http://www.flickr.com/photos/david_jones/175187603/ "Kaikoura Ocean Range Sunrise by David T Jones, on Flickr")

The image of the sunrise just north of Kaikoura in the banner above is static. It's always the same. Back on the original website I had a collection of 40+ images that, thanks to a small perl script, would cycle through each one. As of late 2008 you can still see this in action on [this page](http://cq-pan.cqu.edu.au/david-jones/Reading/) - just hit the refresh button to see the banner image change.

I'd like recreate this effect on this site. But I have to do it without server side scripting and I should also probably do it to maximise the benefits of Web 2.0. I've got some ideas about how to do this using [Flickr](http://flickr.com/), [Pipes](http://pipes.yahoo.com/) and JSON or similar. These ideas will have to be reality tested. However, the first thing I should do is check to see what others have already done.

Ahh, it appears that there is the need to pay for a CSS customisation to enable this. 4 cents a day paid via PayPal. The [approach outlined here](http://en.forums.wordpress.com/topic/random-image-header-tutorial?replies=22#post-36298) and requires a server somewhere that will allow you to upload a PHP script. Essentially the approach I was using on my original server.

Not very Web 2.0. Will experiment with Flickr and Pipes, do a bit more searching. Can do some testing without requiring the CSS customisation upgrade.