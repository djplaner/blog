---
categories:
- moodleopenbook
date: 2015-08-03 13:09:12+10:00
next:
  text: Does learning about teaching in formal education match this?
  url: /blog/2015/08/06/does-learning-about-teaching-in-formal-education-match-this/
previous:
  text: What do &quot;scale&quot; and &quot;mainstreaming&quot; mean in higher education?
  url: /blog/2015/07/29/what-do-scale-and-mainstreaming-mean-in-higher-education/
title: An experiment with the oerpub editor
type: post
template: blog-post.html
---
The following is a summary of an initial experiment using [the OERPub editor](http://editor.oerpub.org/) with some actual content from a course I'm currently looking after. The aim is to explore what it's like to use this purpose built open textbook editor that relies on github.

My current suspicion is that it will demonstrate characteristics similar to all these types of projects, i.e.

1. Be based on a very good theoretical/design set of assumptions.
    
    In this case, the semantic web and various computer science perspectives are the influence. It appears to be mostly designed by semantic web type folk, so not surprising.
    
2. Have some really nice features, but have some difficulty interacting with other parts of the authoring/learning/teaching ecosystem.
3. In part, because it will be only partially complete or has a few bugs that have arisen.
    
    Perhaps in part because it was funded from a grant, the grant has finished, and technology et al has moved on. The tool may not have been entirely completed, and is starting to suffer as bits that did work, stop working.
    

### Login with github, create a repository

It took me a while to get this working correctly. Logging in with my github details was simple.

**Question:** How many authors will have github accounts? It's not a difficult task to do, but understanding it all.....

There's also reports that it only works fully with Chrome. The browser specific nature is a small problem, but still a problem.

It uses the idea of a "bookshelf" to contain multiple books. A book shelf also equates to a github repository. The bookshelf/repository that contains the 'book' I'm working on [can be viewed here](https://github.com/djplaner/edu8111-themes). The editor uses a fixed structure to the repository and a particular XML document type (there is an official label for this which I no longer know).

### Authoring

In this case, I'm working with something written by another person. Ideally I would like to import this into the system and there was an import facility implemented. But I've not been able to get it to work. Instead, I'll be doing a copy and paste job and updating as I go.

**Observation:** The missing import feature is a loss

The copy and paste from PDF wasn't working last week. I've exported the PDF to a Word doc and the copy and paste process appears to work.

The editor provides a number of known "elements" of a document. e.g. an "Activity". You drag and drop the elements into your document and then fill in the expected components of that element.

**Problem:** There doesn't appear to be an element for a "Reading".

Given that the "textbooks" I'm likely to work with are more study guides, than text books (a study guide often points people off to other readings after providing some context). This is a problem.

That's a bugger. At this stage it appears that inserting a link in the book isn't working. There's an interface element to do it, but using it isn't changing the display at all and a close look at [the HTML in github](https://github.com/djplaner/edu8111-themes/blob/gh-pages/content/module1.html) reveals that the links aren't being saved in the HTML.

**Problem:** Looks like you can't insert links?

There is a preview option, let's try that. Ohh, the preview functionality includes a lot of words like "Alpha" and "prototype". The PDF preview gives a 404. The [basic view](http://djplaner.github.io/edu8111-themes/basic-view.html) appears to work but doesn't show the links and also reveals that the content suffers from the cut and paste from word issue.

**Problem:** Output options appear to be alpha or broken.

Is the copy and paste from Word a problem? No, doesn't work on entered text either.

Mmmmm, I thought there might be some bugs and limitations, but not quite so much as all that. Seems I'll have to leave this one alone.