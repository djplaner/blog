---
title: bim2 - Registering a new student feed
date: 2011-01-31 16:57:55+10:00
categories: ['bim', 'bim2']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

Apart from the many todos, the [last post covering bim2 development](/blog2/2010/12/30/progressing-the-student-interface-for-bim2/) left off at the task of registering a new student feed. Summarising/recording the development of bim2 to complete that task is the purpose of this post.

Finally getting back into bim2 development (30 Jan), this post dormant for weeks.

### What has to happen

The process for bim, which I'd like to re-create in bim2, goes something like this

1. Student submits the URL for a blog or a feed;
2. Display error messages and advice if the URL is not a URL, can't be retrieved, or a valid ATOM/RSS feed can't be obtained from the URL.
3. For a valid URL, retrieve the feed and cache it
4. Compare the posts in the feed with the set questions for the activity.
5. Update the bim\_marking table with any posts that match.
6. Update the bim\_student\_feeds table with the details of the feed.

In bim this was done with a bim specific version of [Simplepie](http://simplepie.org/). In Moodle 2, simplepie is included and Moodle 2 also has a wrapper around simplepie that is used by the Moodle external blogging functionality. bim2 should use this wrapper as much as possible.

### How does the Moodle 2 simplepie wrapper work?

It's located in _~/lib/simplepie/_ and implemented as a class called _moodle\_simplepie_. Methods include

- constructor that takes a feedurl
- get\_cache\_directory and reset\_cache  
    By default this is a central cache, wonder if bim should reset this to a course specific/bim specific cache?

There's another class _moodle\_simplepie\_file_, am wondering if this is the one to actually use, it knows about Moodle's version of curl. Its methods include

- constructor;  
    Takes a url, timeout value, redirects, headers, useragen...

I wasn't aware of it, but simplepie does have a class (or two), which the above two extend.

Some sample code from Moodle and its external blog feature follows.

```php 
$rssfile = new moodle\_simplepie\_file($data\['url'\]); 
$filetest = new SimplePie\_Locator($rssfile);

if (!$filetest->is\_feed($rssfile)) { 
  $errors\['url'\] = get\_string('feedisinvalid', 'blog'); 
} else { 
  $rss = new moodle\_simplepie($data\['url'\]); 
  if (!$rss->init()) { 
    $errors\['url'\] = get\_string('emptyrssfeed', 'blog'); 
  } 
}
```

SimplePie\_Locator is being used to test if there is a valid feed. It appears that moodle\_simplepie\_file might do some auto-detection. Should check that.

No, it doesn't. Assumes that the url is for the rss feed rather than using simplepie's autodetect.

Now, if I use moodle\_simplepie, instead of moodle\_simplepie\_file, there is the possibility of getting a feed. However, it seems to be getting the wrong one. In my testing I am using this blog as the test, and instead of the posts feed, moodle\_simplpie is returning the comments feed.

Does this happen if I use simplepie directly? No, if I use the version of simplepie included with Moodle 2 correctly, I can auto-detect.

```php

$url = 'http://davidtjones.wordpress.com';

//$rssfile = new moodle\_simplepie($url); 
$rssfile = new SimplePie(); 
$rssfile->set\_feed\_url( $url ); 
$rssfile->init(); 
print "<h1> feed is " . $rssfile->subscribe\_url() . "</h1>";
```

Gives the appropriate output _feed is https://djon.es/blog/feed/_ (though it also gives a couple of warnings about the cache. Change it to 
```php

$url = 'http://davidtjones.wordpress.com';

$rssfile = new moodle\_simplepie($url); 
print "<h1> feed is " . $rssfile->subscribe\_url() . "</h1>";
```

And I'm getting _feed is https://djon.es/blog/feed/_. This isn't right.

Okay, getting an error at the moment with the operation timing out, the joys of a slow network connection. And that's the problem...... Still a problem with moodle\_simplepie\_file, nothing really explains the difference

### Re-starting

Okay, a few weeks have gone by while I finish the thesis etc. Time to get back into it again. During the break, I did hear via a tweet that the RSS client block does do auto-discovery. So that gives another place to look for example code.

This looks like is 
```php
$rss = new moodle\_simplepie(); 
// set timeout for longer than normal to try and grab the feed 
$rss->set\_timeout(10); 
$rss->set\_feed\_url($data\['url'\]); 
$rss->set\_autodiscovery\_cache\_duration(0); 
$rss->set\_autodiscovery\_level(SIMPLEPIE\_LOCATOR\_NONE); 
$rss->init(); 
```

Actually, that's the wrong stuff. Instead of _\_NONE_ it should be _\_ALL_ and that works.

Gotta love it when a plan comes together. Now to remove the debug stuff I stuck in the Moodle simplepie code.

### Using this in bim2

Now to figure out how this should work within bim2. It's been a while since I've been looking at this code, this should prove an interesting test. Ahh, surprisingly painless. Started work on a new\_student\_feed class.

Okay, that's working. The feed is being found and bim2 is able to manipulate the feed using essentially the same simplepie functions as bim was able to.

This means I can start a new post aimed solely at the bim2 aspect.