---
title: The current state of curriculum mapping in/with Moodle
date: 2010-02-20 14:33:30+10:00
categories: ['curriculummapping-cddu']
type: post
template: blog-post.html
---
As part of looking into a [project](/blog2/research/curriculum-mapping/) around curriculum mapping I need to take a look at the current state of play around curriculum mapping in the Moodle community. This is a summary of what I can find at the moment.

Moodle is used in both schools and universities. My impression is that schools have a longer history and broader use of curriculum mapping, however, mapping in universities is hotting up.

In summary, there are a few examples of Moodle "tools" that claim to do some aspect of curriculum mapping. However, none of them seems to provide the services I'm suggesting. There does appear to be some call for this type of service.

> **UPDATE:** More [recent exploration](/blog2/2010/03/10/moodle-outcomes-metadata-and-curriculum-mapping/) is based around Moodle's existing outcomes support which might offer a foundation on which to build curriculum mapping.

### Discussion threads

The Moodle community generally has discussions within Moodle-hosted discussion forums on the [Moodle.org](http://moodle.org/) site. The threads I could find looking at curriculum mapping include (you will have to create an account on the Moodle.org site to view these):

- [Curriculum mapping with Moodle](http://moodle.org/mod/forum/discuss.php?d=79557)  
    Starts with a general question back in September 2007 that never really went anywhere. Some 2009 posts that include a pointer to a more recent thread, a pointer to the curriculum module for Moodle and a pointer to a US-based school's [curriculum mapping done with drupal](http://currmap.orange.k12.nc.us/).
- [Curriculum mapping](http://moodle.org/mod/forum/discuss.php?d=110759)  
    A more recent and complete thread. Includes a pointer to the module, and a pointer to a [Moodle doc](http://docs.moodle.org/en/curriculum_mapping) on curriculum mapping. There's also some feedback from a user of existing mapping tools and summarises one of the aims of the project being thought about here
    
    > Atlas curriculum mapping is time-consuming and frustrating for many, in part because it is divorced from the courses it maps. Since Moodle houses a school's actual courses, it would be most excellent if the mapping could be a layer on top of what's already there.
    
    . There's also a pointer to the announcement of a Moodle block covered in the next point.
- [Announcement of a Moodle block](http://moodle.org/mod/forum/discuss.php?d=117150) - to facilitate the design of a competency based curricula.
- [Curriculum patch](http://tracker.moodle.org/browse/CONTRIB-1604) for Moodle.  
    This is a "patch" to the core of Moodle. It only works with a small subset of Moodle versions. My take on it, is that this is not really mapping curriculum but providing a way to prescribe a fixed hierarchy for a course (tree, parallel or serial) or groups of courses and ensure students move within it.
    
    Doesn't appear to be what I'm interested in. Also demonstrates some of the potential problems that arise when a "patch" needs to change lots of the Moodle core. This needs to be kept to a minimum.
    
- [Moodle docs on curriculum mapping](http://docs.moodle.org/en/curriculum_mapping)  
    Essentially a page dedicated towards spawning the development of a Moodle component for curriculum mapping.

### Other moodle.org resources

- [New moodle block 'curriculum design tool'](http://tracker.moodle.org/browse/CONTRIB-1332?page=com.atlassian.jira.plugin.system.issuetabpanels%3Acvs-tabpanel)  
    Surpisingly not linked into the above discussions, found via a google search. It does seem to be the moodle block that was announced above though.
    
    There is [project page](https://act-dev.med.virginia.edu/) (or [this page](https://act.med.virginia.edu/blocks/pla/index.php) which seems to be running the block) which I didn't find last year when I looked a bit. The block is meant to provide functions to
    
    - Design curriculum maps relating to competencies (educational goals), professional abilities (learning objectives), learning activities (resources) and assessments.
    - Submission of learning activities by educators with associated searchable metadata
    - Review submitted materials
    - Search and browse published curriculum maps and get related learning object repositories.
    - Rate learning objects
    - Checking out materials from the learning object repositories via a shopping cart model (free shopping)
    - Gap analysis for selected learning object items
    - Packaging of selected curricula items with a dynamically created curriculum description including links to learning activities and assessments.
    - Tracking of downloads and follow up surveying of users.
    
    This seems to be somewhat broader than what I had in mind. As implemented it seems to implement a repository for learning objects that can be peer-evaluated against some criteria. Not curriculum mapping amongst existing courses.
    

### Web resources

- [A discussion thread](http://isenet.ning.com/group/moodleusersandadmins/forum/topics/moodle-as-a-curriculum-map) on a school educators network Ning forum.  
    Describes one person's aim to move a school from another mapping platform into using Moodle. Has various reactions and ideas in response. A number of the responses are talking about problems of limited use of specific purpose curriculum mapping software. There is also a description of how one school "kludged" around the direct absence of mapping in Moodle, which seems to be what the original author was going to do. i.e. no direct support for mapping in Moodle, just use Moodle's existing features to approximate it.
    
    There is a post from a Moodle user/admin arguing why the stand alone mapping software is good because it does provide these features. In particular, the post mentions the inability to identify the overlaps or holes.
    
- [Enterprise Learning Intelligence Suite (ELIS)](http://www.remote-learner.ca/node/180)  
    An "integrated stack of technologies designed to provide end-to-end management of an online learning program". Includes curriculum mapping and a range of other services. Apparently being released under the GPL.
    
    Based [on this presentation](http://www.slideshare.net/moorejon/introduction-to-elis) it appears that "curriculum mapping" is really just grouping courses together as a curriculum - similar to the "patch" mentioned above. Not what I had in mind. [Another presentation](http://www.slideshare.net/mchurchward/moodle-in-the-enterprise-1240013) seeks to reinforce this.