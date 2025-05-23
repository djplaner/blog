---
categories:
- bad
- oep
- site2016
date: 2016-03-26 02:40:52+10:00
next:
  text: LATs, OER, TPACK, and GitHub
  url: /blog/2016/03/26/lats-oer-tpack-and-github/
previous:
  text: 'Mapping the digital practices of teacher educators: Implications for teacher
    education in changing digital landscapes'
  url: /blog/2016/03/24/mapping-the-digital-practices-of-teacher-educators-implications-for-teacher-education-in-changing-digital-landscapes-2/
title: '"SITE''2016: LATs, OER, and SPLOTs?"'
type: post
template: blog-post.html
---
[SITE'2016](https://www.academicexperts.org/conf/site/2016/) is almost finished, so it's past time I started sharing some of the finds and thoughts that have arisen. There's been a (very small) bit of movement around the notion of open. I'll write about LATs and OER and some possibilities in another post. This post is meant to explore the possibility of adapting some of the TPACK learning activities shared by @Keane\_Kelly during [her session](https://www.academicexperts.org/conf/site/2016/papers/48707/) into [SPLOTs](http://cogdog.trubox.ca/2015/02/17/splot-tpc-2015/).

It's really only an exploration of what might be involved, what might be possible, and how well that might fit with the perceived needs I have in my course(s), but at the same time make something that breaks out of those confines. I'm particularly interested in Reil and Polin's idea around residue of experiences and rich learning environments.

Over time, the residue of these experiences remains available to newcomers in the tools, tales, talk, and traditions of the group. In this way, the newcomers find a rich environment for learning. (p. 18)

As most of my teaching and software development work has had to live within an LMS, I'm also a novice at the single web page application technology (and SPLOTs).

## What is a SPLOT?

A [SPLOT is](http://cogdog.trubox.ca/2015/02/17/splot-tpc-2015/)

Simplest Possible Learning Online Tools. SPLOTs are developed with two key principles in mind: 1) to make sharing cool stuff on the web as simple as possible, and 2) to let users do so without having to create accounts or divulge any personal data whatsoever.

The work by @cogdog builds on Wordpress, but I'm wondering if something similar might be achieved using some form of [single web page application](https://en.wikipedia.org/wiki/Single-page_application)?

i.e. a single web page that anyone could download and start using. No need for an account. Someone teaching a course might include this in a class. Someone with a need to learn a bit more about the topic could just use it and gain some value from it.

## TPACK learning activities

[Kelly's presentation](https://www.academicexperts.org/conf/site/2016/papers/48707/) introduced four learning activities she uses to help students in an Educational Technology course develop their understanding about the TPACK framework. They are fairly simple, mostly offline, but appear to be fairly effective. My question is whether they can be translated into an online form, and an online form that is widely shareable - hence the interest in the SPLOT idea.

### Vocabulary target review

[![archery target by Leo Reynolds, on Flickr](images/13000817174_a6bf6b698c_m.jpg "archery target by Leo Reynolds, on Flickr")](https://www.flickr.com/photos/lwr/13000817174/) "[archery target](https://www.flickr.com/photos/lwr/13000817174/)" ([CC BY-NC-SA 2.0](https://creativecommons.org/licenses/by-nc-sa/2.0/)) by  [](https://www.flickr.com/people/lwr/)[Leo Reynolds](https://www.flickr.com/people/lwr/) [](http://www.imagecodr.org/)

In this activity the students are presented with a target (using a Google drawing) and a list of vocabulary related to TPACK (though this could be used for anything). The students then place the vocab words on the target. The more certain they are of the definition, the more "on target" the place the words. This then feeds into discussions.

At some level, through the use of Google drawing it's already moving toward a SPLOT.

What if the students are entirely online, and especially with a tendency to asynchronous study? How might this be adapted to anyone, anytime and provide them with an access to the residue of experience of previously participants?

One approach might be something like a single web-page application that

1. Presents that target and a list of vocab words that the user can place as appropriate. This list of vocab words could be hard-coded into the application. Or, perhaps the specific application (you could produce different versions for different vocab) could be linked to a Google doc or some other source of JSON data. The application gets the list of vocab words from that source.
2. Once submitted the application could allow the user to view the mappings from previous users. This could be filtered by various ways. The assumption is that the application is storing the mappings of users somewhere. The representation might highlight other mappings that are related in someway to the user's map.
3. View provided definitions. Having provided their mapping the user could now gain access to definitions of the terms. There might be multiple definitions. Some put into the system at the start, some contributed by other users (see next step).
4. Identify the most useful definitions. The interface might provide a mechanism by which the user can "like" definitions that help them.
5. Provide a definition. Whether this occurs at this stage or earlier, the user could be asked to provide a definition for one or more terms after/prior to seeing the definitions of others.
6. Remap their understanding. Having finished (more activity could be designed in the above) the user moves the words to represent any change in their understanding of the words. The system could track and display how much change has occurred and compare it with the changes reported by others.

### TPACK game

The second activity is a version of [the TPACK game](http://www.matt-koehler.com/the-tpack-game/) (or [this video](https://www.youtube.com/watch?v=7z3aP_Chj6c)). A game that is already available online, but not as a flexible object that people can manipulate and reuse. Immediate thought is the following might help make a "more SPLOT" version of the TPACK game

1. Provide a single web page application that implements a variety of ways to interact with the TPACK game. For example,
    - The [current version](http://www.matt-koehler.com/the-tpack-game/) has people trying to identify a third element of TPACK given the other two. Which appears to be the version used by @Keane\_Kelly
    - Another version might be to show a full set of three and ask people to reflect on whether or not the combination is a good fit, one they've seen before, not a good fit, and why.
2. Provide the capacity to provide answers to to the application that are stored and perhaps reused. For example, the two different versions of the game above could be combined so that if someone suggests a particular combination in the first one that has already been "evaluated" they could be shown what others have though of it and why.
3. Provide the capacity to share and modify the values for T, P and C. The current online version of the game plus @Keane\_Kelly appear to have their own set of values for T, P, and C. Kelly mentioned the need to keep the Technology updated over time, but there's broader value in keeping a growing list of values for all.  As there is also for customising some.  e.g. some technologies won't always make sense in all environments, but in particular the content might be something to customise, e.g. for a specific curriculum or topic area.
    
    If it were an online application that used some sort of shared data space, it could be grown through use. It should also be possible to modify which data store is used, to support customisation to a particular context.