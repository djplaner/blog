---
categories:
- bim
date: 2010-11-18 17:12:25+10:00
next:
  text: Interesting times ahead
  url: /blog/2010/11/20/interesting-times-ahead/
previous:
  text: Understanding EduFeedr and contrast with BIM
  url: /blog/2010/11/17/understanding-edufeedr-and-contrast-with-bim/
title: Installing and starting with Moodle 2.0
type: post
template: blog-post.html
---
As a first step to [BIM v2.0](/blog/2010/11/09/initial-plans-for-bim-2-0/) I'm installing and starting to play with Moodle 2.0 (RC2). The following is a summary/reflection of the experience. One of the aims of this is to investigate how Moodle 2.0 handles its integration with external blogs and see what lessons/insights I can learn for BIM v2.0.

_Warning:_ This is a little incomplete, I'm posting early for testing purposes.

### Registering external feeds

Okay, this is a surprise. To register an external blog (see image below, click on it for larger version), you need to provide the actual feed url. This is somewhat surprising for two reasons:

- most students/staff don't really know about feeds; and,  
    This raises the question of whether ease of use is more important, or educating them about the new medium is more important.
- it's not needed.  
    Simplepie, which I believe is the PHP library used to retrieve the blog feeds, can do auto-detect.

[![register external blog - Moodle 2](images/5186250586_c9d1f1ceb0_m.jpg)](http://www.flickr.com/photos/david_jones/5186250586/ "register external blog - Moodle 2 by David T Jones, on Flickr")

For BIM, the presence of auto-detect in [Simplepie](http://simplepie.org/) meant it was possible to make it easier for the students/staff. The initial use of BIM was focused on getting the students to reflect etc, it was felt requiring them to grasp what a feed was and figuring out how to find their feed was not central to the outcome.

Having a look at the Moodle 2.0 code, it does use simplepie, or at least a "moodleised" version `require\_once($CFG->libdir . '/simplepie/moodle\_simplepie.php');`

I wonder what the reasons were for not adopting auto-detect?

### What's been done to moodle\_simplepie.php

At the very least, it is a OO wrapper around simplepie. Apparently simplepie is untouched. Going by initial comments, the OO class aims mainly to connect Simplepie with various Moodle configuration variables and settings.

Mmm, I haven't looked at this sufficiently. But it appears that the method used to retrieve the blog avoids using Simplepie's support for auto-detect. It even calls curl directly before passing over to Simplepie. With BIM I assume Simplepie will handle all that. I'm assuming this is due to a performance issue or similar that I'm not aware of.

Actually, it appears that I modified the internals of simplepie to use the Moodle curl configuration variables (mostly proxy from memory). Putting the mods in the wrapper is the more correct approach, however, it does appear to remove the ability to use Simplepie's auto-detect. **Disclaimer:** I haven't checked this thoroughly and thus could be entirely wrong. Which I suspect I am, given that the auto-discovery stuff in Simplepie [is known](http://tracker.moodle.org/browse/MDL-19990?page=com.atlassian.jira.plugin.system.issuetabpanels:all-tabpanel).

Mmm, I probably need to spend more time on this as it would be good if BIM v2.0 would simply use the Moodle wrapper for Simplepie.

### More problems

Bugger. When I do try to register this blog with the direct feed URL, it doesn't work.

> The URL you entered does not point to a valid RSS feed

Works fine on the same machine from BIM, so something in the Moodle 2.0 configuration must be off?

Ok, with a bit of debugging it appears that it's getting a timeout. There's a setting for a 2000 millisecond timeout somewhere. It's a curl problem, or at least that's where it is being reported.

Okay, the default timeout being set in moodle\_simplepie is 2 
```php  
// default to a short timeout as most operations will be interactive 
$this->set\_timeout(2); 
```

Seems that this was too short for my net connection, adding a 0 on the end and it works.

### What does Moodle store about external blogs

First, have to view the entries from my registered blog. There they are, but only the first couple of lines. Can't see any option on this view to allow me to see the complete posts. Is the complete post actually stored?

Looks like posts (from lots of sources) is stored in the post table. 
```sql
id bigint(10) unsigned module varchar(20) userid bigint(10) unsigned courseid bigint(10) unsigned groupid bigint(10) unsigned moduleid bigint(10) unsigned coursemoduleid bigint(10) unsigned subject varchar(128) summary longtext content longtext uniquehash varchar(128) rating bigint(10) unsigned format bigint(10) unsigned summaryformat tinyint(2) unsigned attachment varchar(100) publishstate varchar(20) lastmodified bigint(10) unsigned created bigint(10) unsigned usermodified bigint(10) unsigned 
```

Looks like the display code for the blogs is using the summary field, hence the summary. Looks like the content field for an external blog contains the ID for the blog in the table blog\_external. Suggesting that the entire content for an external blog is not stored internally by Moodle.

Okay, the "mirror" process for external blogs is done by the blog\_sync\_external\_entries function. It appears that it deletes all entries for an external blog each time. Then it retrieves them. It uses the description element in the XML for each item as the content, rather than the content element. Description, I believe, is the summary while content contains the full content.

I'm a bit worried about this deleting of all entries before adding all the posts again. Mainly because not all posts remain in the RSS feed. As people post you are going to lose posts to the external blog. At least if I'm right about the deleting.

If this is the correct interpretation, then when I publish this post the current last entry in my external blog should disappear from my test Moodle. Time to try that out. Of course, there is going to be a delay until the synchronise process is run at some stage. Going by the config option, this is every 24 hours (by default). Time to reduce that, post this and check again in a little while. Interesting, only allows me to reduce it to 12 hours.

**Confirmed.** Based on my testing it appears confirmed that the external blog integration with Moodle only includes the current contents of the external blog's feed in Moodle. Most blogs only keep a limited number of recent posts in their feed. This means that external blog posts are not a permanent member of the Moodle blog. They will disappear as the owner makes more posts.

### Funny characters

The biggest problem I've faced with BIM has been dealing with the "funny" characters inserted into blog feeds when people copy and paste content from Word. Wanted to try this out with the external blog functionality in Moodle 2.0 and see if it remains a problem (i.e. did I miss something simple).

So, I have a known problem feed. Time to register it as an external blog and see what happens. Ok, it registered fine. Do the special characters appear? Will only work if the special characters are at the start of the post, due to Moodle only storying the description, not the whole content. Yep, the problem feed does have the special characters in the description. And yes, they do appear in Moodle. See the image below, see the black diamonds containing question marks? Those are the special characters.

[![Special character problem](images/5188457653_4e56f75a96_m.jpg)](http://www.flickr.com/photos/david_jones/5188457653/ "Special character problem by David T Jones, on Flickr")

I haven't had a problem with special characters in this situation on MySQL. The problem has arisen when using Postgres, at least at one institution.

### Other core/plugins using Simplepie

Seems that the rss block is the only other part of the core using it. Seems to be basic stuff. Uses moodle\_simplepie to construct object and uses mostly straight Simplepie member functions to perform tasks.

It does, however, appear to be using auto-detect. This is looking good for use in BIM 2.0. Though I do wonder why the external blog stuff doesn't use it. Performance?

```php
$rss = new moodle\_simplepie(); $rss->set\_feed\_url($url);
$rss->set\_autodiscovery\_level(SIMPLEPIE\_LOCATOR\_ALL); 
// When autodiscovering an RSS feed, simplepie will try lots of 
// rss links on a page, so set the timeout high 
$rss->set\_timeout(20); 
$rss->init();

if($rss->error()){ return $url; }

return $rss->subscribe\_url();
```

It is interesting that the display feed functionality is done by hard coded table tags, rather than the Moodle table API/classes.

### Testing

One of the other tasks for BIM 2.0 is to start a testing regime. The external blog support apparently comes with some tests, hoping to borrow the approach.

Seems to be some Moodle standard for unit tests with a class UnitTestCaseUsingDatabase, which sounds like one of potentially many. Now I see that there was something available as way [back as 1.7](http://docs.moodle.org/en/Development:Unit_tests) based on [SimpleTest](http://www.simpletest.org/). And here's [the stuff for 2.0](http://docs.moodle.org/en/Development:Unit_tests#Unit_testing_in_2.0).

### Outstanding tasks

- Special characters are there. Implement a test with special characters in blogs...will have to be in the summary.
- Will need to test further whether or not the moodle\_simplepie class can use the SimplePie auto-detect.
- Yes it does. Check to see if the Moodle external blog implementation will actually start losing posts.
- Check out other Moodle plugins using the moodle\_simplepie class.
- Talk with folk involved with Moodle/Simplepie about the "issues" identified above.  
    Seems they already know of this stuff.