---
categories:
- bim
- bimerrors
date: 2010-09-05 18:04:00+10:00
next:
  text: Back into the thesis
  url: /blog/2010/09/13/back-into-the-thesis/
previous:
  text: Light-weight analytics tools as part of scaffolding, context-sensitive conglomerations
  url: /blog/2010/09/04/light-weight-analytics-tools-as-part-of-scaffolding-context-sensitive-conglomerations/
title: More problems with BIM and special characters
type: post
template: blog-post.html
---
The following is a record of some work to investigate some more apparent problem with BIM mirroring blog posts that contain "special" characters due to a bit of copying and pasting from Word into Wordpress.

### An aside on supporting a tool like BIM

All of my previous software support has been around software that I (or the team I work for) have developed and for which we are also responsible for hosting and supporting the people using it. i.e. we knew exactly what was going on where.

With BIM the development, support and hosting are all separated. I write BIM, but I don't host of support it. Which means I don't know what the folk who are doing the hosting/supporting have done (or haven't done). Which adds all sorts of complexity to the process.

This sort of separation is increasingly common and is often aimed at saving resources/money. But I do wonder whether or not that if viewed from an overall perspective it is adding more cost (in the broadest possible sense i.e. including the hassle and inefficiency caused by the difficulty but which doesn't typically show up in anyone's budget bottom line) into the whole task of supporting systems.

### The problem

There are at least two, almost invariably related, problems:

- Special characters that aren't being translated safely.
- Some situations where Moodle/BIM on Postgres is not able to insert student posts.

### The postgres problem

There appears to a problem with Postgres/Moodle/PHP/BIM falling over when attempting to insert some posts. Maybe because of special characters. The only way I have of testing this at the moment is black box, i.e. re-creating it on a Postgres-based Moodle install. First step is to identify where this is happening and see if something can be done to make it not so catastrophic a failure.

#### Fail all posts, if one post fails

The error I'm seeing is

> bim\_process\_feed: inserting bim\_marking \*\*url here\*\*

Ok, that seems to match this bit of code

\[sourcecode lang="php"\] if ( ! insert\_record( "bim\_marking", $safe ) ) { mtrace( get\_string( 'bim\_process\_feed\_error', 'bim', $entry->link ) ); return false; } \[/sourcecode\]

Ok, the first thing here is that the "return false" should go. This breaks out of the whole insert process. What should happen is simply move onto the next entry and try to insert that.

Ok, that's updated and into github.

#### Why are posts/inserts failing

The above was causing a problem because Postgres would report a failure when blog posts with certain characters were being inserted. The same posts are not causing a problem with MySQL.

Is this a known problem with Postgres? Are there solutions from the Postgres community that might help out here?

Doesn't seem to be too much via Google, at least with what I was searching for. Guess I turn to exploring more the special characters in the posts that are causing problems.

### More special character problems

The process here is to repeat what I did last time, modify my version of BIM to be somewhat explicit about the characters in posts it is inserting, find out which aren't being handled, and then add some code to handle them.

The list of potentially problematic characters are:

- a bullet point  
    Turns out that this is a [middot (search for 183](http://www.tedmontgomery.com/tutorial/htmlchrc.html). So, I've added a translation for this. This works, however, it does highlight a problem with "bad handling" described in the next section.

### Bad handling

At least on MySQL, some of the changes seem to be introducing some rather weird translations. For example, a middot and some white space is translated into similar looking characters but with each surrounded by a single quote. This needs to be fixed.

Ahh, some code I lifted is using ereg\_replace, which according to [this](http://www.rdeeson.com/weblog/61/using-multi-byte-character-sets-in-php-unicode-utf-8-etc.html) is not multi-byte safe. Replace it with mb\_ereg\_replace, and all is good.

This seems to be the major problem.

Will see how it goes when testing with other problem data.