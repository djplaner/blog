---
categories:
- bim2
date: 2013-05-26 09:55:43+10:00
next:
  text: One-size-fits-all formulas
  url: /blog2/2013/05/29/one-size-fits-all-formulas/
previous:
  text: Which Moodle (or other LMS) tool is best at support and training?
  url: /blog2/2013/05/23/which-moodle-or-other-lms-tool-is-best-at-support-and-training/
title: Preparing BIM for Moodle 2.4 (and beyond?)
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: How to help improve the Moodle book module | The Weblog of (a) David Jones
      author_email: null
      author_ip: 192.0.80.62
      author_url: https://davidtjones.wordpress.com/2015/02/10/how-to-help-improve-the-moodle-book-module/
      content: '[&#8230;] the change using git Prior work contains an example of how to
        get a version of the Moodle source using git and start making [&#8230;]'
      date: '2015-02-10 19:55:51'
      date_gmt: '2015-02-10 09:55:51'
      id: '762'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
Time for a bit of coding. The following has gone on over a few weeks.

[BIM](/blog2/research/bam-blog-aggregation-management/) has been added into the [Moodle plugin database](https://moodle.org/plugins/view.php?plugin=mod_bim). A part of this is providing versions of the plugin that work with each of the versions of Moodle. Currently BIM is available for Moodle versions 2.0 through 2.3. I need to provide a version that works with Moodle 2.4 and perhaps explore what, if anything different, is required for the imminent (since released) Moodle 2.5 release. This is a record of that work.

### Misc updates

First, it's time to update the various BIM related pages

- The [BIM page](/blog2/research/bam-blog-aggregation-management/) on this blog needed updating to show that BIM is now available via the Moodle plugin database.
- The Moodle docs [BIM page](http://docs.moodle.org/24/en/BIM_module) also needs updating due to this progress.

### Misc bugs

One of the less than perfect Moodle development practices I had adopted was not having the debug messages appear on the page. Hence I was unaware of the following two problems

> Notice: Undefined variable: strbims in mod/bim/lib/locallib.php on line 244 Notice: Undefined variable: base\_url in mod/bim/lib/locallib.php on line 249

Thanks to [Anthony](http://docs.moodle.org/24/en/User:Anthony_Borrow) for picking these up. Fix these first. Which will mean committing these to github and creating new zip files.

Having turned the full debugging options on reveals a range of similar messages to address

- undefined variable screen in student/view.php - line 42 - **DONE**
- A little surprising, was on-going use of "print\_heading" which should have changed as part of [migration to 2.0](http://docs.moodle.org/dev/Deprecated_functions_in_2.0#print_heading_.280.29)
- error() is a deprecated function, - **DONE**
- Issues with the use of redirect. - **DONE**
    
    This is slightly larger than the above. A couple of the workflows in BIM involve a message being given in one complete page, a delay and then a redirect to another BIM page. This breaks how a Moodle script [should work](https://moodle.org/mod/forum/discuss.php?d=142191). I was going to leave this alone, but testing some of the above minor changes requires this to be fixed.
    
    Simple solution for now will be to replace the timed redirect with a simple link for the user to click.
    
- Undefined property: stdClass::$cmidnumber - from manage questions - **DONE**  
    happens in bim\_grade\_item\_update, which is called from bim\_update\_gradebook...similar problem [to this](https://tracker.moodle.org/browse/MDL-12961?page=com.atlassian.jira.plugin.system.issuetabpanels:changehistory-tabpanel) which also provides the basics of a solution.

### Using GIT more appropriately

This does raise the question about to another point mentioned by Anthony - the Github file repository on Moodle.org. Apparently this would make zip files easier.

Part of what I'm trying to do with BIM is to explore how tools like BIM can be made more flexible and responsive. This will, in part, need a solid foundation that links properly with the broader Moodle development practices.

After a bit of exploration this seems to mean creating branches in the BIM github repository with names such as MOODLE\_23\_STABLE, MOODLE\_24\_STABLE which then enables easier integration with the type of processes [described here](http://docs.moodle.org/24/en/Git#Books_and_tutorials).

Let's start with [setting up Moodle](http://docs.moodle.org/24/en/Git#Obtaining_the_code_from_Git) via git \[code lang="bash"\] git clone git://git.moodle.org/moodle.git cd moodle git branch -a git branch --track MOODLE\_24\_STABLE origin/MOODLE\_24\_STABLE git checkout MOODLE\_24\_STABLE \[/code\]

What work I've done on BIM so far is suitable for a MOODLE\_23\_STABLE branch. There is also an older MOODLE\_19\_STABLE version of BIM. I need to fix the BIM github repo to have these branches. Then I can start work on the MOODLE\_24\_STABLE version below.

This means I need to refresh (again) my understanding of github and branches. One of the drawbacks of only dipping into development irregularly and quickly is that I don't really ever grok it. May be easier than I thought.

\[code lang="bash"\] git branch MOODLE\_23\_STABLE git push origin MOODLE\_23\_STABLE \[/code\]

And there's such a branch added. Add the one for 24 and start thinking about making the changes. Also done the one for MOODLE\_19

### What's needed - 2.4

Lastly, there's a need to make some changes for 2.4

- create an addinstance capability in db/access.php- **DONE**
- update version.php for [Moodle 2.4 release](http://docs.moodle.org/dev/Releases) - **DONE**/li>

Create the zip file that I'll upload to CONTRIB \[code lang="bash"\] git archive -o ~/Desktop/BIM\_24.zip --prefix=bim/ MOODLE\_24\_STABLE \[/code\]

That sort of worked, but I believe there may be a bit more to do.

### Version 1.9 into CONTRIB

Another task is to get the old version of BIM for Moodle 1.9 into CONTRIB

That seems to be done.