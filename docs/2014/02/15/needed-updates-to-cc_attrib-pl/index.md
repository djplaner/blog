---
categories:
- bricolage
date: 2014-02-15 08:23:02+10:00
next:
  text: It's making us stupid
  url: /blog2/2014/02/17/making-us-stupid/
previous:
  text: BIM testing and fixes
  url: /blog2/2014/02/07/bim-testing-and-fixes/
title: Needed updates to cc_attrib.pl
type: post
template: blog-post.html
---
The following is a list of updates I need to make to a perl script [I wrote last year](/blog2/2013/10/20/creative-commons-flickr-and-presentations-a-bit-of-tinkering/) that helps me properly attribute the Creative Commons licenced Flickr photos I use in presentations. This list arises from prepare the [welcome video](http://www.slideshare.net/davidj/welcome-to-edc3100-ict-and-pedagogy) for this year's course. Most, if not all, of the updates are to make it easier to use, prevent the chance of "spam" like behaviour and deal with apparent reliability issues with the Flickr API.

### Parse the slides file - ignore comments

As I discover images I want to use in a presentation, I maintain a text file with the details as follows \[code lang="perl"\] 1,http://www.flickr.com/photos/rameshng/5930493923/ # Welcome picture Welcome.jpg 2,http://www.flickr.com/photos/rameshng/5930493923/ # Welcome picture Welcome.jpg \[/code\]

The script doesn't parse this file yet. Also, the "comments" approach is a new thing and appears useful for tracking. The script should ignore those.

### Track successful comments

One of the main tasks of the script is to post an acknowledgement comment to the [Flickr page](http://www.flickr.com/photos/rameshng/5930493923/) for an image. This morning the Flickr API would successfully post these comments to some pages, and not others. Meaning a manual check to see which worked and which didn't, remove those that did work from the script and try again. Had to do this 3 times.

Would be useful if the script tracked which comments were successfully made and didn't try to make another comment on those. Don't want to start spamming.

### Track all images used

Following on from that, I'm wondering whether the script should track all images ever run through the script. There's a good chance I might use an image in more than one presentation associated with a course, not sure I'd want to make the same comment again. Perhaps I should. If I used the image in a research presentation - very different from the course - perhaps I should make a new comment.