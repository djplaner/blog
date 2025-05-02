---
title: Can I roll my own federated wiki? (not yet)
date: 2014-12-18 09:16:59+10:00
categories: ['thesis']
tags: ['fedwikihappening']
type: post
template: blog-post.html
---
So I now have a federated wiki of [my own](http://david.au.fedwikihappening.net/view/welcome-visitors). Rolled by the good folk of #fedwikihappening.

But it doesn't feel like it's mine. It's on someone else's server. Which sort of defeats the purpose of a federated wiki a little. Though I do recognise it makes it easier for folk to get started, which [may not be a good thing](http://cogdogblog.com/2014/12/16/over-easy/)?

The question this post is attempting to answer is, can I roll my own federated wiki?

## Easy but not quite a good fit

There are some easy methods for installing the tool

https://twitter.com/holden/status/544975687988166657

However, it assumes a certain type of environment. One that I don't have at the moment. I may have to get such an environment, but let's see if I can kludge it into the environment I do have.

## Use the source

Kludging will require playing with [the source](https://github.com/WardCunningham/Smallest-Federated-Wiki). So download that.

A source that would appear not destined for command line installation. Not a lot of suggestions how to do that. At least until you find the [installation guide](https://github.com/WardCunningham/Smallest-Federated-Wiki/wiki/Hosting-and-Installation-Guide).

Will use this to install it locally and explore what is required. Will figure out if and what might be required for hosting in the cloud later.

Ahh, it appears that the installation guide is slightly out of date. The following doesn't work with the current code \[code lang="sh"\]cd Smallest-Federated-Wiki/server/express\[/code\]

But the first step of that installation guide was to install NodeJS, which provides the npm command which is used to do the default installation approach. \[code lang="sh"\]npm install -g wiki\[/code\] But that breaks if you don't have write access to /usr/local/lib/node\_modules. Suggesting I'd need to install NodeJS in my user account on the remote site.

That appears to have worked. With everything in /usr/local/lib/node\_modules

## Installing locally

It appears that NodeJS can be [installed locally](http://increaseyourgeek.wordpress.com/2010/08/18/install-node-js-without-using-sudo/) by using the source. However, I wonder if I can run the wiki as a stand alone server on the host? Only one way to find out (short of asking).

Bugger, get a "virtual memory exhausted" error when compiling NodeJS. Initial searching appears to suggest that the problem is with a [bug in the version of gcc](http://www.imagemagick.org/discourse-server/viewtopic.php?t=23190#p97352) - 4.4.x

## Next steps?

Options include

- Still need to answer the question whether or not I could run the wiki as a server on a different port.
    
    The docs might say.
    
- Ask the good folk at reclaim hosting for some insights.
- Follow @holden's advice and go with another host that's known to support fedwiki.