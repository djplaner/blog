---
categories:
- research
date: 2017-05-20 09:05:02+10:00
next:
  text: Emedding plotly graphs in Wordpress posts
  url: /blog/2017/06/17/emedding-plotly-graphs-in-wordpress-posts/
previous:
  text: Early steps in developing a design system/model for Professional Learning
    Opportunities
  url: /blog/2017/04/26/early-steps-in-developing-a-design-systemmodel-for-professional-learning-opportunities/
title: Bye, Bye Mendeley?
type: post
template: blog-post.html
---
So, I have a problem. What was a wonderful open source product was bought by a big publisher. I'm an open kind of guy so this has always been a bit disquieting. It recently got a bit worse.

https://twitter.com/djplaner/status/863934554062573568

Time to start actively searching.

@matbury recommended the alternative I was most aware of

https://twitter.com/matbury/status/863963530235703300

Then I stumbled across [this comparison of citatation management software](http://guides.library.utoronto.ca/c.php?g=250610&p=1671260) from the University of Toronto. What struck my particularly about this comparison was the following entry under the Zotero column

> Also works with Google Docs

As it happens, I'm increasingly using Google docs for collaborative creation for both work and research. Working with Google docs is a big plus. The question here is how well does Zotero work with Google docs? How much time/agony will be involved in moving?

The following documents on-going experimentation in doing so. It reveals that it doesn't look like it will be too painful and that as I'm in the early days of a couple of group writing projects, probably a good time to make the move and test it out on some authentic tasks.

Looking increasingly like bye bye Mendeley. Would probably prefer an approach that didn't rely on a single server for syncing/group sharing, but Zotero looks good enough for now.

[![Bye Bye... See Ya! by Lisandro M. Enrique, on Flickr](https://farm1.static.flickr.com/108/274852368_3bd1afcde7.jpg "Bye Bye... See Ya! by Lisandro M. Enrique, on Flickr")](https://www.flickr.com/photos/latente/274852368/)  
"[Bye Bye... See Ya!](https://www.flickr.com/photos/latente/274852368/)" ([CC BY 2.0](https://creativecommons.org/licenses/by/2.0/)) by [Lisandro M. Enrique](https://www.flickr.com/people/latente/)

## Install Zotero

First step is to [install Zotero](https://www.zotero.org/download/). Apparently there is now both a standalone (which works with browser extensions) and a Firefox version. Download the stand alone version for the Mac.

Installing the stand alone version it picked up an old Zotero data directory from the days of early experimentation in the noughties.

Installation also takes you back to the Zotero site to create an account on the service, because

> It's a free way to sync and access your library from anywhere, and it lets you join groups and back up all your attached files.

I'll do that (not without some minor reservations, wonder if anyone is working on a distributed method for sharing citations/references?). Now time to configure browser extension and stand alone Zotero with that account (and restart Word for that integration to work).

That seems to be working. There is a surprising amount of material in the old Zotero directory, back from the thesis days.

How to import my Mendeley library? A Google search reveals [this advice](http://thedigitalresearcher.com/how-to-import-your-mendeley-library-into-zotero/). Let's try that.

Creates a 1.6 Mb file for 3808 documents. The advice is that

> Unfortunately, Zotero won’t retain your Mendeley folders or groups, but it does import the PDFs of any attached journal articles.

Losing the folders is a bit of a bugger. But I suppose I can retain Mendeley for when I need to find something.

It's probably taken somewhere around 10 minutes to import that collection into Zotero.

All seems to be there, but of course there are some things that have been lost, including

- As mentioned the folder/group structure that I'd used in Mendeley to organise references into structures relevant to the work I was doing.
- I've also lost the annotations and notes that I'd started making using Mendeley's internal features. Had been worried about that. Appears Zotero doesn't support annotations on the PDFs, but then there are the Adobe methods for that, which might be a better long term approach.

## Citation management and Google docs

According to [this page](https://www.zotero.org/support/google_docs) working with Google docs is via the same mechanism used for plain-text documents.

- Add a bibliography, by selecting the list of items and drag them into the document.
    
    Suggesting a need to maybe create a folder or similar for every reference you want to use in a Google doc. Suggesting collaborative use would require all the collaborators to agree on processes, perhaps using a common Zotero group owned resource?
    
- Add a citation, hold the shift key before dragging.

Apparently there are requests in to Google to allow a better integration.

Let's see how the existing method (more [detail here](http://libguides.princeton.edu/c.php?g=84519&p=541292)) works. The following image shows the result. The first line shows the results of adding a bibliography, the second adding a citation. The citation format is not what I'd prefer. So the question is whether it can be changed.

[![Google docs / Zotero usage](images/33953714643_66d3f4e932.jpg)](https://www.flickr.com/photos/david_jones/33953714643/in/dateposted-public/ "Google docs / Zotero usage")
<script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

There is some other advice on how to do this a bit more effectively. But it doesn't quite meet the expectations about what citation management really working with Google docs might be. But it is a step up. What about other features?

## What's it like with Word?

I still end up writing most my formal publications in Word, so that experience is important.

New Word document - Add-ins tab has now been modified to include icons for Zotero. Insert new citation, pops up a dialog box to configure document preferences. Assume this is because the first time I've used Zotero with this document.

Much like Mendeley another dialog box pops up, you enter author name or other, choose from some options and hey presto citation is inserted.

Insert bibliography and done.

All very similar. Might have a few wrinkles of difference, but I don't imagine that (given the size of the Zotero community) wouldn't be something that can't be figured out.

## Online library, groups etc.

With the Zotero account comes an online library, as shown in the following image. Seems the current situation is

- 300Mb for free and never (big call) expires
- 2Gb for $USD20 a year.
- 6Gb for $USD60 a year.
- Unlimited for $USD120 a year.

[![Zotero library online](images/34630618481_d995e1e94d.jpg)](https://www.flickr.com/photos/david_jones/34630618481/in/dateposted-public/ "Zotero library online")
<script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

There are options to control the privacy of the online library: public the entire library; public notes; hide from search engines. I've just changed those settings so that the library (not the notes) is public. You can see [it here](https://www.zotero.org/djplanner/items)

The group functionality supports collaboration and explicitly mentions web-based bibliographies for classes. This could be interesting.

[The group page](https://www.zotero.org/support/groups) mentions that there are no limits on groups and outlines a range of features and uses. One of the limits, I assume will be the amount of storage space online.