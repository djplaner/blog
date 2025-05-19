---
categories:
- bim
date: 2009-12-24 08:18:36+10:00
next:
  text: BIM - Staff show details screen
  url: /blog/2009/12/24/bim-staff-show-details-screen/
previous:
  text: 'Herding cats and losing weight: the vimeo video'
  url: /blog/2009/12/23/herding-cats-and-losing-weight-the-vimeo-video/
title: BIM - minor fixes to show student details
type: post
template: blog-post.html
---
This post follows on from [the last post](/blog/2009/12/22/bim-cron-and-view-student-details-screen/) in doing some minor improvements to the show student details screen in BIM. This includes:

- Link between the question ID and the question name
- Double check the display of the “All posts”.
- Add in the link to posts for Marked Answers.
- Re-do the interface to be Moodle like.

### Question ID and question name

In a couple of places on the screen there is a need to take the question id and return the question title. Basic solution is:

- Create a hash with question id as key and title as value (possibly with other things).  
    `bim_get_question_hash( $bim )` seems like the go.
- Use the hash in the appropriate places.

Done and working nicely. The link for posts is also done. The all posts is working as currently designed. This means, apart from look and feel, this screen is essentially working.

### Make it Moodle

Moodle has a particular style/approach to HTML/look and feel. At this point in time, I haven't used it for this screen. Time to start doing it.

### Where I'm up to

Did a bunch of work on the view student details screen, tidied up a bunch of stuff. Still not happy with the look, but will leave that till later. Time to move onto some of the staff screens.

A screen dump of the screen is [available on Flickr](http://www.flickr.com/photos/david_jones/4209851502/). It's based on real data so identifying information has been blurred out. But you get the idea, boring, ugly. Needs to be better.