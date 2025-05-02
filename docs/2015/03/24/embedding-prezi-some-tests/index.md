---
title: Embedding prezi - some tests
date: 2015-03-24 11:25:14+10:00
categories: ['thesis']
tags: ['edc3100']
type: post
template: blog-post.html
---
A student of mine is reporting problems embedding a Prezi into a blog post. Here's a quick test.

### Straight from Prezi

Let's go with the straight prezi embed code

It looks something like this \[code lang="html"\] [https://prezi.com/embed/8enn0a8y7qx3/?bgcolor=ffffff&lock\_to\_path=0&autoplay=0&autohide\_ctrls=0#](https://prezi.com/embed/8enn0a8y7qx3/?bgcolor=ffffff&lock_to_path=0&autoplay=0&autohide_ctrls=0#) \[/code\]

And the embeded prezi should appear below

[https://prezi.com/embed/8enn0a8y7qx3/?bgcolor=ffffff&lock\_to\_path=0&autoplay=0&autohide\_ctrls=0#](https://prezi.com/embed/8enn0a8y7qx3/?bgcolor=ffffff&lock_to_path=0&autoplay=0&autohide_ctrls=0#)

After a preview it's obvious this doesn't work.

The assumption being the that Prezi "embed code" isn't liked/supported by Wordpress.

The question being whether you can transform the Prezi "embed code" into something that is liked by Wordpress.

### Transform the Prezi "embed code"

A quick Google search [embed prezi wordpress.com blog](https://www.google.com.au/search?q=embed+prezi+wordpress.com+blog&ie=utf-8&oe=utf-8&gws_rd=cr&ei=mroQVZb1L4enmAW4z4HgDg) reveals [this service](https://wordprezi.appspot.com/) that appears to transform the embed code.

Oh, but it looks like Prezi's done something that might break this transformation on Wordpress.com

\[gigya src="http://prezi.com/bin/preziloader.swf" allowfullscreen="true" allowscriptaccess="always" width="550" height="400" bgcolor="#ffffff" flashvars="prezi\_id=8enn0a8y7qx3&lock\_to\_path=0&color=ffffff&autoplay=no&autohide\_ctrls=0" \]

Yep, that doesn't appear to work.

And the same Google search above reveals [this discussion](https://en.forums.wordpress.com/topic/how-to-embed-prezi?replies=5) which describes why.