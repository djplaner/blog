---
categories:
- bim
- bim2
date: 2013-04-05 16:46:07+10:00
next:
  text: An ad hoc exploration ethnographic research
  url: /blog/2013/04/07/an-ad-hoc-exploration-ethnographic-research/
previous:
  text: Meaningless freedom and auto-marking the learning journals
  url: /blog/2013/04/01/meaningless-freedom-and-auto-marking-the-learning-journals/
title: Adding bim 2.0 to "CONTRIB"
type: post
template: blog-post.html
---
Next step in the development of [bim v2.0](/blog/research/bam-blog-aggregation-management/) is to start the process of submitting it to [CONTRIB](http://docs.moodle.org/dev/contrib). i.e. essentially getting out officially into the Moodle community.

The following is my attempt to figure out and record the process for doing this. This was actually started a couple of months ago but then semester started, a bit of breathing space now and I need to catch up on this.

Evidence of progress

- The [BIM module entry](http://docs.moodle.org/24/en/BIM_module) in Moodle docs.
- The [tracker issue for BIM](https://tracker.moodle.org/browse/CONTRIB-4249).
- The [BIM announcement post](https://moodle.org/mod/forum/discuss.php?d=226074) in the ["General add-ons" forum](https://moodle.org/mod/forum/view.php?id=44).
- And an entry has been added into Moodle plugins directory that is awaiting approval.

Overall, the process hasn't been that difficult. A little disjointed in places and between that and my rushing it in places, there may be a few things to fix up. But it's done.

Will be interesting to observe what happens from here. Beyond responding to that, it's time to start thinking about further changes to BIM.

## Finding the right process

Of course, [the background on CONTRIB](http://docs.moodle.org/dev/contrib) I linked to above is obsolete. CONTRIB is using git, not CVS anymore (I believe). Time to find where the right process is documented. It's a bit of an issue when the obsolete documentation on this are what Google is returning as the top hits.

The ["Guidelines for contributed code](http://docs.moodle.org/dev/Guidelines_for_contributed_code) seem more up to date. The process listed - or at least my interpretation - is summarised in the following sections.

### Create a git repository

[Create a git repository](http://docs.moodle.org/dev/Guidelines_for_contributed_code#How_to_submit_code), preferably using the format _moodle-{plugintype}\_{pluginname}_.

This implies I'll need to rename the [existing BIM git repository](http://github.com/djplaner/BIM/). I wonder what support git has for this? I discover and implement one approach below.

[Forking the existing bim repository](https://help.github.com/articles/fork-a-repo) might be an option. But not sure I would want to maintain the connection. Can it be renamed? Well apparently there is a feature to do this. That appears [to have worked](https://github.com/djplaner/moodle-mod_bim), the question will be what ramifications are discovered into the future. At the very least, I imagine my local clones of bim will need to be updated.

Here's what I did \[code lang="bash"\] git clone https://github.com/djplaner/moodle-mod\_bim.git cd moodle-mod\_bim git checkout bim2 mv moodle-mod\_bim bim # make some changes git push \[/code\]

All seems to be working. Of course, all the hypertext links on the blog are now broken because of the new repository name. Will have to update a few of those.

### Test the code

Make sure the code is tested. Here's what I've done to date

- A range of testing while under development.
- Including some testing of BIM under versions 2.4.1, 2.3.4, 2.2.7 and 1.9.19 of Moodle.
- Thanks to a bug report from a Russian user of BIM [solved a problem](/blog/2013/03/03/bim2-and-disable_form_change_checker/) with 2.3.2 version of Moodle.
- Been using BIM for my current teaching. Not in a full on way but it's getting some testing.

Some more work to do

**Backup and restore test**

Do a backup and restore of the EDC3100 blogs between BIM installs on different versions of Moodle. Doing this from 2.4 to 2.4 as well as 2.3 will also provide me with a decent test space for the issues below and in an on-going way. 300+ students with multiple posts is a much more reasonable foundation for testing. That worked surprisingly easily.

**Revisit open issues**

Some recent playing with BIM revealed a potential issue, so need to explore that a bit and also look at any of the other [immediately open issues](https://github.com/djplaner/moodle-mod_bim/issues?labels=bim2%2Cimmediate&sort=updated&state=open) that should be addressed before adding the code to CONTRIB.

- Problem with adding [questions and hanging process\_unallocated](https://github.com/djplaner/moodle-mod_bim/issues/68)  
    With a BIM activity already created with students registered and posts mirrored, it appears that when you add a question, then the function process\_unallocated (attempts to decide if any student posts match the question) hangs.
    
    Recreate the problem. Add a question to a copy of the EDC3100 BIM activity and do the processing thing. And I can't re-create it. All working as expected. Thinking this may have been due to proxy problems giving the appearance of a problem.

### Documentation

[Documenting the plugin](http://docs.moodle.org/dev/Guidelines_for_contributed_code#How_to_provide_documentation) is important and suggested to be done [on the English Moodle docs](http://docs.moodle.org/dev/Plugin_documentation).

Where would the BIM docs reside? It should be in "the most recent version of Moodle for which the plugin works". One of the bits of advice for the process is to go into BIM and find where the link for "Moodle docs for this page" points. Which in the case of BIM is [here](http://docs.moodle.org/24/en/mod/bim/view).

Of course, it's not that simple. It appears this is the proper place to get started [http://docs.moodle.org/24/en/BIM\_module](http://docs.moodle.org/24/en/BIM_module)

What is required of the docs, [The stamp collection module](http://docs.moodle.org/24/en/Stamp_collection_module) is given as an example and the provided list of contents includes:

- Template code.
- Features overview.
- Installation instructions.

Done sufficiently for now, I hope.

### Request to be tested

[Request that the code be tested/reviewed](http://docs.moodle.org/dev/Guidelines_for_contributed_code#How_to_request_that_your_code_be_tested.2Freviewed). Done, at least I think this is [what was required](https://tracker.moodle.org/browse/CONTRIB-4249).

### Add it to the plugins directory

[Share the code](http://docs.moodle.org/dev/Guidelines_for_contributed_code#Share_code_in_the_Moodle_plugins_directory) in the [Moodle plugins directory](https://moodle.org/plugins).

Need to create a zip file containing the module that can be installed and tested. Apparently this will do it. \[code lang="sh"\]git archive -o ~/Desktop/BIM2.zip --prefix=bim/ bim2\[/code\]

Will need to test that this works ok.

- Delete BIM from Moodle install.
- Unzip the zip file created by the above.
- Go to notifications.
- Install it.
- Create a BIM activity.

That seems to work. I do wonder what I've missed.

Well, $module->release in version.php appears to be one of those things.

While I am here, might be a good time to update the BIM icon. Moodle 2.x appears to support much larger icons and the image @rolley provided for BIM 1.x doesn't scale too well. That appears to be a step too far for me.

I'll leave it at that. It's been uploaded. Not sure I've gotten everything, but it will do for the day.