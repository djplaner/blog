---
title: BIM, Moodle, Simplepie, curl and HTTP proxy issue
date: 2013-07-26 10:44:02+10:00
categories: ['bim2']
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: kj
      author_email: k.besley@gmail.com
      author_ip: 194.81.161.134
      author_url: http://scesol.wordpress.com
      content: 'Hi David,
    
    
        Where is the call which doesn''t use the proxy? I have a different issue to you,
        but I''m keen to try your fix. It''s getting irritating!
    
    
        Thanks,
    
    
        Ken'
      date: '2013-07-30 01:31:10'
      date_gmt: '2013-07-29 15:31:10'
      id: '812'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: David Jones
      author_email: davidthomjones@gmail.com
      author_ip: 121.222.147.186
      author_url: https://djon.es/blog/
      content: "G'day Ken,\n\nIf you're having other problems, let me know.  Happy to\
        \ help.\n\nlib/bim_rss.php in the function \"bim_get_feed_url\" - around line\
        \ 247 - see this in GitHub here https://github.com/djplaner/moodle-mod_bim/blob/MOODLE_24_STABLE/lib/bim_rss.php\n\
        \nThe initialisation of the $feed variable needs to be this\n    $feed = new moodle_simplepie();\n\
        \nThe fix is in GitHub - so you could retrieve the code from there.  I also need\
        \ to update the code on Moodle CONTRIB. But was waiting until I investigated a\
        \ couple of other minor problems. I should probably revisit that.\n\nDavid."
      date: '2013-07-30 07:39:34'
      date_gmt: '2013-07-29 21:39:34'
      id: '813'
      parent: '812'
      type: comment
      user_id: '1'
    - approved: '1'
      author: David Jones
      author_email: davidthomjones@gmail.com
      author_ip: 139.86.2.14
      author_url: https://djon.es/blog/
      content: G'day Ken,  FYI, I've updated BIM for Moodle 2.4 on both Github and <a
        href="https://moodle.org/plugins/pluginversions.php?plugin=mod_bim" rel="nofollow">CONTRIB</a>
        to have this fix and also a fix that will prevent non-teaching staff showing up
        on the allocate markers screen.  David.
      date: '2013-08-01 11:05:35'
      date_gmt: '2013-08-01 01:05:35'
      id: '814'
      parent: '812'
      type: comment
      user_id: '1'
    
pingbacks:
    []
    
---
Good news this week. [BIM](/blog2/research/bam-blog-aggregation-management/) got into the institution's testing site for Moodle. One step close to going live. The bad news is that there were a couple of issues to resolve. This post is a record of the attempt to address the big one (successfully as well).

## The problem

When you attempt to register the blog for a student, BIM/Moodle generates this error

> Unable to access the URL you provided
> 
> http://davidtjones.wordpress.com The error created was cURL error 28: connect() timed out!

It appears that it doesn't play nicely with the institutional HTTP proxy. I had noticed this same problem with the development install of Moodle on my laptop, but had thought that was simply my bad practice.

Seems the problem may be a little more than that.

## The plan

The rough plan is

1. Find out if this a known problem?
2. Does this problem effect other Moodle tools that rely on SimplePie?
3. Is there an identifiable difference between what BIM and those other tools?

### A known problem

A search for "moodle simplepie proxy" and similar doesn't reveal a lot. (Simplepie is the 3rd party library that used to search for, parse and generally work with feeds.

You get [this from GitHub](https://github.com/moodle/moodle/blob/master/lib/simplepie/moodle_simplepie.php) which shows the Moodle modified version of GitHub. It includes evidence of modifications to SimplePie to

> make sensible configuration choices, such as using the Moodle cache directory and curl functions/proxy config for making http requests in line with moodle configuration

There is also [this closed issue](https://tracker.moodle.org/browse/MDL-30648) on the Moodle tracker where there was a problem with a proxy that requires authentication. It's been fixed and the fix should be in the versions of Moodle we're using here. Also, I don't believe the institutional proxy fits this problem. In fact, the error is very different.

### Does it effect other Moodle tools?

There's a "register an external blog" facility in Moodle. It connects the external blog to the users Moodle blog (I believe).

I do find it interesting that this asks the user to enter the Feed URL and not the blog URL. SimplePie does a good job of finding feeds from a blog URL (in my experience). Have just checked the code and it does use SimplePie.

Using this to register a URL without having configured the HTTP proxy results in a long period of waiting and then the error "This feed is invalid". Seems to suggest some limitations of the code. Wish I had the time to look at this more.

Configure my box with the proxy details and try again. Oops, that didn't work. Ahh, "Some settings were not changed due to an error" an error message when saving the HTTP proxy that didn't exactly leap out at me. Not immediately obvious what the error was.

Checking the database (mdl\_config) reveals that the proxyhost wasn't set, apparently you don't need the "http://" and the error doesn't identify that. Fixed.

Okay, that works. External blog registered. And posts from the blog showing up in my Moodle "blog".

Let's try BIM now. Nope. The timeout problem again. Implying there's something different going on here.

### Is there a difference?

Yes, eventually tracked down one of the calls to SimplePie is using the normal SimplePie class and not the moodle simple pie class. Hence not using the proxy setup.

Tested it with the student registering process and that works as well.