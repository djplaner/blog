---
categories:
- bam
date: 2009-07-30 11:39:02+10:00
next:
  text: '"BAM into Moodle #9 - a working eStudyGuide block?"'
  url: /blog/2009/07/30/bam-into-moodle-9-a-working-estudyguide-block/
previous:
  text: The design and implementation of Webfuse - Part 3
  url: /blog/2009/07/29/the-design-and-implementation-of-webfuse-part-3/
title: '"BAM into Moodle #8 - finishing the eStudyGuide building block"'
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: 'BAM into Moodle #9 &#8211; a working eStudyGuide block? &laquo; The Weblog
        of (a) David Jones'
      author_email: null
      author_ip: 74.200.245.188
      author_url: https://djon.es/blog/2009/07/30/bam-into-moodle-9-a-working-estudyguide-block/
      content: '[...] The Weblog of (a) David Jones Another voice in the blogosphere    &laquo;
        BAM into Moodle #8 &#8211; finishing the eStudyGuide building&nbsp;block [...]'
      date: '2009-07-30 15:54:10'
      date_gmt: '2009-07-30 05:54:10'
      id: '2676'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The [last post](/blog/2009/07/28/bam-into-moodle-7-an-estudyguide-block/) in this series described the start of a little project to learn more about PHP/Moodle programming in order to get BAM into [Moodle](http://www.moodle.org/). Essentially everything is done, there are two main tasks left:

- Identify how to "properly" retrieve a file over http in PHP/Moodle and figure out how to use it.
- Confirm the phpxml is the best way to parse XML in PHP/Moodle and figure out how to use it.

Once those are done, a rudimentary eStudyGuide block will be complete and I'll have filled in two of the main holes in my knowledge necessary to put BAM into Moodle.

### How to retrieve a file over http in PHP/Moodle

What a difference some time makes. I spent a bit of time Tuesday hunting the web and Moodle for information on this. This morning, apparently, it took 5 minutes. [curl](http://au2.php.net/curl) seems to be the go.

Starting with this [curl tutorial](http://blog.unitedheroes.net/curl/) - not to mention [the examples here](http://au2.php.net/manual/en/curl.examples-basic.php)

Here's a list of questions I think I need to answer around the use of curl, and hopefully the answers I've found:

- How do you use curl to get through basic auth?  
    
    ```
     curl_setopt($curl_handle,CULTOPT_HTTPAUTH,CURLAUTH_ANY);
    curl_setopt($curl_handle,CURLOPT_USERPWD,'username:password');
    ```
    
    CURLAUTH\_ANY is a ?constant? that says use any HTTP auth method.
- How do you set a mime-type on what's going back to the client?  
    The simplest examples simply get the remote file and return it to the browser. If you do this with a non-HTML file there appears to be some issues around the client handling it appropriately.
    
    One solution I've found is to use the CURLOPT\_FILE option to save what is returned by curl to the file system. Then use the header and readfile functions to set everything up appropriately i.e.
    
    ```
    header("Content-type: image/jpeg");
    header("Content-Disposition: attachment; filename=imageName.jpg");
    readfile("tmpfile");
    ```
    
    Would imagine you'd have to use some sort of session variable to keep the filename unique and also remember to remove the file.
    
    Wonder if you can use header without the need for readfile? Yep, the works, use the CURLOPT\_RETURNTRANSFER option so that the file is returned as a string and then use the following
    
    ```
    header("Content-type: image/jpeg");
    header("Content-Disposition: attachment; filename=imageName.jpg");
    print $buffer;
    ```
    
    Of course the question now becomes what if you are transferring really large files. Won't that consume "RAM" for the web server and on a heavily used site cause some "issues"? So maybe the file option is better.
    
- What are the necessary checks etc you should do when using curl?  
    Seem to be all fairly standard ones, check return values etc, don't do horrible security stuff. That said, there seems to be some variability within the existing Moodle code that is using curl - some seems to be quite anal about checks.
- What's TRUE in php?  
    CURLOPT\_BINARYTRANSFER needs to be set to TRUE for transferring binary files. What's the numeric value for TRUE in PHP? Okay, 0 is false. Somewhat familiar.

### Parsing XML

Appears, at the moment that the "xmlize" library in Moodle is the simplest method to parse XML. Produces a nested data structure with the content. Pretty similar to what is done at the moment. Is there something better?

Given that parsing XML isn't a main requirement for BAM, I won't bother going any further. I think I'll be using Magpie to parse the RSS that BAM needs to manipulate.

xmlize is simple to use, looks like it is time for lunch. After lunch will be trying to code all this up. I want a working eStudyGuide block by the end of the day.