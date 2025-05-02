---
title: BIM 2.0 - cleaning up part 3
date: 2013-01-06 22:02:57+10:00
categories: ['bim', 'bim2']
type: post
template: blog-post.html
---
The third in a series of posts documenting necessary cleaning up of [issues](https://github.com/djplaner/BIM/issues?labels=immediate&state=open) with BIM. Getting closer and closer to release of 2.0b

Issues being cleaned up here include

- [#56](https://github.com/djplaner/BIM/issues/56) - "add an activity" help text
- [#39](https://github.com/djplaner/BIM/issues/39) - some more consideration of help text for BIM 2.
- [#58](https://github.com/djplaner/BIM/issues/58) - getting a "do you want to leave" this page message on allocation.
- [#50](https://github.com/djplaner/BIM/issues/50) - checking the BIM code against the Moodle coding style.

## Add an activity help text

In Moodle 2.4 (at least), when you selecting an activity to add the chooser will display a collection of help text for the plugin you've just chosen. Need to put some text in for BIM. Question, where is this specified? Trawling the Moodle docs for this might be difficult. Will start with the code of some existing modules.

Mmm, a quick find and grep didn't reveal what I thought would be there. At least not with assignment, search on forum reveals the _modulename\_help_ help string. Provided one of these for BIM, two problems

1. The help text isn't appearing.  
    Viewing the source of the course page, it appears that the help text is added into this page. It's not created/called after the add an activity link is clicked. Seems it is being done in modchooser. course/renderer::course\_modchooser\_module\_types is the function that seems to extract it.
    
    This method is using a set of objects for each module. Those with a help text have a help field. Where is this being set? It's passed into the original function. It appears to be extracted by course/lib/get\_module\_metadata. Which is in turn using _get\_string\_manager_ to get an object that has a method _string\_exists_ which is used to see if _modulename\_help_ exists. And I can confirm it's not working for bim.
    
    So obviously restarting the apache daemon wasn't sufficient, purge all caches in Moodle and it is working.
    
2. Where is the "more help" link coming from.  
    The searching above suggests it is looking for an entry in the lang file for _modulename\_link_. But this is only for modules with entries in the moodle docs. i.e. not bim. What do other contrib modules do? For now will ignore this. The [guidelines for Moodle docs](http://docs.moodle.org/24/en/MoodleDocs:Guidelines_for_contributors) offers some suggestions for contributed code.

## BIM help text

Will move this to a future improvement. Will need to look at setting up a public website (perhaps in Moodle docs) once I have BIM up and running.

## Do you want to leave

When a post is allocated to a question, selecting the question generates a form submission. This is now resulting in the browser generating a do you want to leave the page message.

1. Is this just chrome?  
    No, Firefox does it as well.
2. How is BIM actually doing "form submission" in this case?  
    The moodle\_form object for allocation posts creates a SELECT element with a _onchange="this.form.submit()_ attribute.
    
    It is done this way to avoid the complexity entailed with allowing a marker to allocate different questions at the one time. e.g. Javascript would have to prevent them from allocating more then one post to the one question (of course, this does raise the question of why BIM doesn't support allocating more than one post to a question, this would be more flexible and potentially useful)
    
3. Is this a known problem/feature of Moodle 2.x?  
    It appears this may be as a result of [this issue](https://tracker.moodle.org/browse/MDL-31315) i.e. it's something they've explicitly added into Moodle 2.3. to prevent users from navigating away from pages with forms that have changed. Of course, the trouble is that in this case the code is actually doing a submit. Changes will be processed.
4. Can this be done without generating the message?  
    The text of the message is defined in the lang/en/moodle.php file with the string _changesmadereallygoaway_. This is used in a number of files including lib/formslib.php that has a check \[sourcecode lang="php"\] if ($form->is\_form\_change\_checker\_enabled()) { $PAGE->requires->yui\_module('moodle-core-formchangechecker', 'M.core\_formchangechecker.init',\[/sourcecode\] in the startForm method.
    
    Knowing some of the right terms to search for leads [to this](http://docs.moodle.org/dev/lib/formslib.php_Form_Definition#disable_form_change_checker) and a method to turn it off. ANd that does it.
    

6. Is there a better way to achieve the "form submission" on allocate?  
    A suggestion from this [tracker item](https://tracker.moodle.org/browse/MDL-35395?page=com.atlassian.jira.plugin.system.issuetabpanels:all-tabpanel) suggests
    
    > pure js alternatives (nested elements... actions at distance...).
    
    Appears this old hacker may need to update some knowledge and modify some code.

## The Moodle coding style

Time to check the BIM code against the accepted Moodle code styles.

### Automated code checkers

[Code-checker](https://moodle.org/plugins/view.php?plugin=local_codechecker) is an install into Moodle that generates a web page with errors and warnings. Running it over the bim code finds quite a few, including:

- use of tab characters;
- lines with over 180 chars;
- apparent requirement to start all files with appropriate licence/comments.
- whitespace at the end of lines;  
    A bit of RE magic "1,$s/^s$//g" and/or "1,$s/s$//"  
    Would appear to be an artifact of copy and paste.
- Ending inline comments with punctuation!!
- Indentation  
    in vim, go to start of file and do _\=G_
- spaces after and before the start/end brackets of a foreach.
- NULL TRUE FALSE should be lower case.

Now error free.

And now onto [moodlecheck](https://github.com/marinaglancy/moodle-local_moodlecheck) which checks the documentation - which should reveal numerous errors/oversights in BIM.

Quite a few. Out-dated usage removed.