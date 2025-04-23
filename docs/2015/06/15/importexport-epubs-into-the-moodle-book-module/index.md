---
title: Import/export ePubs into the Moodle book module
date: 2015-06-15 09:48:05+10:00
categories: ['moodleopenbook']
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: Rolley
      author_email: r.tickner@cqu.edu.au
      author_ip: 138.77.36.75
      author_url: http://rolleys.wordpress.com
      content: 'I only got time for a quick quick comment... so...
    
        Usability - the good thing, which should work to your advantage, is that the software
        that reads ePubs ''should'' be available on all the student''s devices already,
        even if they''ve never used it, because the OS''s are usually bundled with something
        - there''s ebook readers on Android I''m sure, and I know for certain iBooks is
        bundled with iOS.
    
        Missing TOC - yep the TOC will be essential.  Best bet is to pull apart an ePub
        file which you know has all the goods, and examine how the TOC is created.  I
        can''t recall.  I do know that all you do is rename the .ePub to a zip, and unzip
        it (via terminal), and then just look at the construction.
    
        HTML - yes, I think we discussed before the possibility of having a sanitiser
        for the HTML.. ePubs will be strict as.  It''s a problem alright if your authors
        don''t know anything about HTML.. eek.
    
        YouTube - good luck HA HA.. This will be a major challenge for you.  It might
        be best to just include a youtube link in the place of the embed, and the youtube
        will open in the OS''s native application - which may also provide additional
        benefits for users (such as being able to use their account management to favourite
        or comment in the video).  Basically the ePub will have to be a stand alone offline
        document, even though that sucks in a way.  I have got them to embed videos which
        are included in the ePub structure, but this makes huge files and is extremely
        buggy, and a plain nuisance trying to get the videos encoded with very specific
        formats - and usually multiple formats (3gp, some other one.. can''t remember).
        Pain in the #### though.. that''s for sure.
    
        Good luck!'
      date: '2015-06-15 10:12:52'
      date_gmt: '2015-06-15 00:12:52'
      id: '1320'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: David Jones
      author_email: davidthomjones@gmail.com
      author_ip: 139.86.69.32
      author_url: https://djon.es/blog/
      content: Thanks Rolley.  WIth the video I assumed getting the video to play would
        be wishful thinking.  Was thinking more of some form of placeholder that makes
        it clear that there was an embedded video there and a link to it.
      date: '2015-06-15 10:20:48'
      date_gmt: '2015-06-15 00:20:48'
      id: '1321'
      parent: '1320'
      type: comment
      user_id: '1'
    - approved: '1'
      author: Christopher Kenniburg
      author_email: Kennibc@dearbornschools.org
      author_ip: 204.39.94.188
      author_url: https://plus.google.com/+ChristopherKenniburgWebmaster
      content: You might want to check out this plugin for Moodle which imports and exports
        ePub files called Lucimoo.  http://lucidor.org/lucimoo/
      date: '2015-08-22 00:39:31'
      date_gmt: '2015-08-21 14:39:31'
      id: '1324'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: David Jones
      author_email: davidthomjones@gmail.com
      author_ip: 101.179.64.28
      author_url: https://djon.es/blog/
      content: Thanks, but that's the plugin being tested in the post.
      date: '2015-08-22 07:09:48'
      date_gmt: '2015-08-21 21:09:48'
      id: '1325'
      parent: '1324'
      type: comment
      user_id: '1'
    
pingbacks:
    - approved: '1'
      author: Import/export ePubs into the Moodle book module...
      author_email: null
      author_ip: 185.82.148.10
      author_url: http://www.scoop.it/t/moodled/p/4045734905/2015/06/15/import-export-epubs-into-the-moodle-book-module
      content: '[&#8230;] One of the likely aims of the Moodle &quot;open&quot; book project
        that interested me was the ability to export Book modules to ePub format. A capability
        I think would be seen as valuable for students in my ...&nbsp; [&#8230;]'
      date: '2015-06-15 11:53:41'
      date_gmt: '2015-06-15 01:53:41'
      id: '1322'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: Testing the Lucimoo epub export book tool | The Weblog of (a) David Jones
      author_email: null
      author_ip: 192.0.99.24
      author_url: https://davidtjones.wordpress.com/2015/08/18/testing-the-lucimoo-epub-export-book-tool/
      content: '[&#8230;] reported earlier the ePub contains a few errors because apparently
        the original HTML content in my Book resource [&#8230;]'
      date: '2015-08-18 10:22:44'
      date_gmt: '2015-08-18 00:22:44'
      id: '1323'
      parent: '0'
      type: pingback
      user_id: '0'
    
---

See also: [[blog-home | Home]]

One of the likely aims of the [Moodle "open" book project](/blog2/the-moodle-open-book-module-project/) that interested me was the ability to export Book modules to ePub format. A capability I think would be seen as valuable for students in my course, given the heavy use of the book module. In developing the Moodlemoot'AU 2015 [session on the project](https://mootau15.moodlemoot.org/mod/data/view.php?d=1&rid=126) this was certainly I've been trawling the Moodle community forums for discussions about the Book module. This type of function has been mentioned as desirable by others.

Then last night I stumble across [this post](https://moodle.org/mod/forum/discuss.php?d=315119) from Saturday in which someone has done it. Written some add-ons that will not only export in the ePub format, but also allow the import of ePub formats. Some [discussions in tracker](https://tracker.moodle.org/browse/MDL-37199) about this that I may wish to look at again later. What follows is some initial experiments with that code.

In summary, looks like it works very well and is very promising. The biggest problem is that it is very finicky about the HTML. Generating big red error boxes when the HTML (which works in the browser) doesn't meet it's standards. Could be very useful.

Wonder how difficult it would be in getting it installed on the institutional Moodle?

### Export

I'm going to start with the [export tool](https://moodle.org/plugins/view/booktool_exportepub) as that's my main interest. Instructions [here](http://lucidor.org/lucimoo/manual.php)

1. Download the zip file.
2. Install view Site Admin / Plugins...
    
    Being added as a "Tool" within the book. **note:** perhaps a model for other functions?
    
    No problems.
    
3. Test it with some of the EDC3100 books.
    
    Head into one of the EDC3100 books. And there is a new link under the "Book administration" menu - Download as ebook.
    
    Click on that link and an ePub file gets downloaded and opened in iBooks.
    
    Errors coming in terms of rendering. I'm assuming at the moment due to some of the HTML I've included.
    
    [![Error](images/18818293851_4313105ede_n.jpg)](https://www.flickr.com/photos/david_jones/18818293851 "Error by David Jones, on Flickr")
    
    Yep, the problem is a bit of poor HTML. Appears that the ePub export tool is quite a bit stricter about HTML than a browser. **Suggestion:** meaning that some sort of warning about HTML issues with book chapters might be useful.
    

A copy of the epub file produced during testing can be [seen here](https://dl.dropboxusercontent.com/u/14025788/MoodleOpenBook/PKM%20and%20Reflection%20-%20fixed.epub), including a range of errors generated by less than stellar HTML.

Some points to ponder:

- The reliance on strict HTML is going to be a barrier to many, more support from the tools is required to reduce this barrier.
    
    Some ideas of the type of support might include:
    
    - Some way for the book module to analyse and highlight (or fix) problem HTML prior to export to ePub.
    - An option for the ePub export tool not to show the quite obvious errors.
        
        Some of the errors don't appear to impact display. It's the big red error box that impacts display. Being able to turn this off might be useful.
        
- Some thought will need to be given to video and other non-book content.
    
    Page 28 (in the ePub) I produced above has a YouTube video to play when viewed in Moodle. In the ePub there is nothing, no link, no image etc suggesting that the video should go there.
    
    The ePub does show links and other HTML, but not YouTube embeds. Automatically including something suggesting and linking to the video would be useful.
    
- Missing ToC
    
    A feature of the Moodle book in both it's online and print forms is that it produces a table of contents that helps navigation. The ePub export isn't producing a ToC. Could be useful.
    
- Bundling up multiple books into an ePub.
    
    As mentioned in [the presentation abstract](https://mootau15.moodlemoot.org/mod/data/view.php?d=1&rid=126) my course has 70+ books with 670+ chapters. One of the aims of the ePub export tool is to allow students to have offline copies of the books. At the moment the ePub export tool only works one book at a time. Meaning students would have to export each of the 70+ books individually.
    
    A tool that allows exporting collections of books to ePub - perhaps as a single ePub or as separate ePubs would be useful. e.g. the ability to export all the books in a topic (or a course) into a single ePub.
    
    This is the same sort of tool that would be useful if a book search tool was implemented. The ability to search within a single book, all books in a topic, or all books in a course.
    
- Confusion over "page" numbers.
    
    I can see the student questions now.
    
    > I'm having problems understanding the last sentence on page 52 of the PKM and reflection book. Help!!!
    
    While the student has been reading the ePub (hence page 52), I'm more than likely to be only using the Moodle based versions of the book. Creating some confusion as we have to translate back and forth between page numbers.
    
- Usability of the ePub format.
    
    I don't have any real experience using the ePub format. So I wonder how useful it will be for students. i.e. how many have software that can read iBooks on the various devices they want to use?