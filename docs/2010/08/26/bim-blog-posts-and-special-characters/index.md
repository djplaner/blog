---
title: BIM, blog posts and special characters
date: 2010-08-26 10:32:49+10:00
categories: ['bim', 'bimerrors']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

The following is a summary/explanation of a common problem with BIM and its mirroring of blog posts and a common solution. The problem is generally caused by folk creating their blog posts in Word and then copying and pasting them into the blog post. For various reasons this process brings along some "special" characters which, while they work fine in Word, screw up royally within more constrained textual representations, like those of Web browsers and XML/RSS parsing libraries.

### Reported problem

A student has made a post to their blog, the teacher can see it on the student's blog, but it's simply not present within BIM. BIM isn't picking it up.

### Diagnosis of the problem

Steps to diagnosing the source of the problem were:

- Login to the Moodle course site and confirm the problem.  
    Yes, student has posted it to his blog, but BIM not picking it up.
- Register the student blog with a local copy of BIM.  
    Ahh, the blog post shows up on my local copy, but only the first dozen or so characters.
- Look at the feed for the student blog.  
    Find the tell-tale signs of special characters exactly where my local copy of BIM cuts off the post.

Okay, BIM currently attempts to handle special characters, obviously it is missing something.

### Common solution

This appears likely to be an on-going problem, so am going to leave a bit of commented code in place that I use to implement this "solution". The "solution" is basically get BIM to print out each individual character in a blog post along with its ASCII value. Use this ASCII value to modify the bim\_clean\_content function to remove the offending special character.

The code that implements this character by character display looks like this

\[sourcecode lang="php"\] # KLUDGE: simple test to find out which special characters are # causing problems $contenta = str\_split( $content); print "<h1> $title </h1>"; foreach ( $contenta as $char ) { echo "$char .. " . ord( $char ) . "<br />"; } \[/sourcecode\]

For this particular problem the offending character is 189. So add the following to the function bim\_clean\_content. It appears that character 189 is some sort of dash.

\[sourcecode lang="php"\] $post = ereg\_replace( chr(189), "-", $post ); \[/sourcecode\]

Re-register a student with the same blog and 189 has been replaced. Remove the kludge and it all appears to be registered correctly.