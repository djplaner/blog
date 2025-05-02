---
title: How might github and the Moodle book module work together
date: 2015-08-13 16:22:42+10:00
categories: ['moodle', 'moodleopenbook']
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: Tim Klapdor
      author_email: tim.klapdor@gmail.com
      author_ip: 137.166.105.218
      author_url: http://timklapdor.wordpress.com
      content: 'This is a really interesting project you''re working on - lots to absorb
        in terms of the workflow and technology and how the two interact. Over the last
        couple of weeks I''ve been playing around with Static Site generation via GitHub
        and Jekyll and I think there''s some techniques that could be co-opted into your
        work. The Jekyll workflow is quite interesting as it separates site design from
        the content and writing process itself. Templating is done via HTML and Liquid
        templates and content is handled by something simple like markdown. Each chapter
        (or post depending on your output) is a separate text file and media can also
        be stored and linked to. Once you have your content and template set up you "build"
        with Jekyll which merges the two together. When paired with GitHub this build
        is automated, so that when there''s a new commit it triggers a build. In this
        way you can create a "dynamic" site but without the need of a database. My site
        www.inhal.es works this way and runs off GitHub pages with a domain pointing to
        it. Would be interesting to see if this kind of workflow/content could be incorporated
        into an LMS as it would be a fantastic workaround for a lot of issues.
    
    
        One thing you might want to check out is prose.io - which is a fronted editing/posting
        tool for GitHub. I haven''t had a chance to set it all properly but it''s a single
        page web app that just uses HTML5, javascript and the GitHub API to allow you
        to directly edit, add and upload new content. Editing in Moodle could perhaps
        point to something like prose.io or use similar API calls to make commits to the
        source.
    
    
        Really interested to see where this goes!'
      date: '2015-08-14 10:02:39'
      date_gmt: '2015-08-14 00:02:39'
      id: '1370'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: David Jones
      author_email: davidthomjones@gmail.com
      author_ip: 101.179.64.28
      author_url: https://djon.es/blog/
      content: 'Thanks for the various pointers. Will follow up.  I''m spending much of
        today making some initial forays in implementation.  You''re right about it being
        complex, especially when you consider the broader workflow implications.  I''m
        a simple guy, so I''m going to start with bricolage. i.e. scratch my own itch
        using the bare minimum possible.  But hopefully in such a way that more complex
        things can emerge as required.
    
    
        Hence my current thinking is based on my current workflow<ol> <li> Create new/major
        edits of existing "books" by editing HTML files (I use vim).<p>Based on my current
        needs, I''m not a fan of Markdown. Currently don''t have a driving need to learn
        another markup language. (A very simple form of) HTML is second nature to me.
        Would take a long time for another markup language to achieve that, time I don''t
        have </p> </li> <li> Import them into the Book module.</li> <li> Maintain them
        there during term.<p>Changes in response to student feedback and experience.</p>
        </li> <li> At the end of semester, the content is rolled over to the next site.<p>Moodle
        does a very nice job of maintaining connections between content and activities.
        My content has links to numerous Moodle activities. Much of the content is a)
        set the context, b) explain the activity, c) go do the activity.</p> </li> <li>
        For major changes, export a single HTML file and return to step 1. </li> </ol>
    
    
        Github, I hope, will allow me to avoid some of the manual import/export steps
        and also allow me to maintain another repository for the changes I make via vim.
    
    
        At the same time, I''m hoping it will allow others to make use of the content.  Will
        see how that all goes, part of the fun of emergence.'
      date: '2015-08-14 11:03:00'
      date_gmt: '2015-08-14 01:03:00'
      id: '1371'
      parent: '1370'
      type: comment
      user_id: '1'
    
pingbacks:
    - approved: '1'
      author: Bringing github and the Moodle book module together &#8211; step 1 | The
        Weblog of (a) David Jones
      author_email: null
      author_ip: 192.0.83.14
      author_url: https://davidtjones.wordpress.com/2015/08/14/bringing-github-and-the-moodle-book-module-together-step-1/
      content: '[&#8230;] following is the first step in actually implementing some of
        the ideas outlined in an earlier post about bringing  and the Moodle Book module
        together. The major steps covered here [&#8230;]'
      date: '2015-08-14 17:36:46'
      date_gmt: '2015-08-14 07:36:46'
      id: '1372'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The [Moodle open book project](/blog2/the-moodle-open-book-module-project/) is attempting (not surprisingly) to modify the [Moodle book module](https://docs.moodle.org/29/en/Book_module) to enable it to produce open resources (educational or otherwise). The main focus is on making the content of the books open in a way that enables modification and reuse. The plan is to do this by enabling a Moodle book resource to be linked to github.

The following is an exploration of and an attempt to describe how this might work at a fairly high level.

What do you think? Might this work? Are there better options?

The next step will be to try some realistic technical explorations to see if this can be implemented.

### Why?

The idea is that once in github different people (or courses) can use github to modify and collaborate around the same document. e.g. a book I created for my course, might be useful for another course looking at ICT and Pedagogy. Rather than play around with Moodle backups, I could create a github repository and the content of the book to that repository. The author of the other course can then fork that repo and import the content of the book from their repo into Moodle.

Any changes that either of us make to the book are stored in github. We can then use github's features to share and manage changes.

Beyond this, I could make all of the books in my course available via github. Who knows, some of my students might find them useful or may wish to make changes that might enhance the work.

### Implementation

At this stage, the idea is to implement the github 'connection' as a [book tool](https://moodle.org/plugins/browse.php?list=category&id=56). This means it can be installed by each Moodle site that wants it. When installed there will be a new link in the Book administration block through which you access the github functionality.

The intent is that an individual Book resource will be linked to a single file hosted in a github repository. The file would be a single HTML file (at least initially) with the different chapters and sub-chapters indicated in some yet to be defined way. The final format will aim to allow the HTML file to be edited by as many different editors as possible, but still allow simple importation into the Book module.

As a future feature, it might be possible and useful to all the import/export of that single file from github into the Book to be done using the user's choice of other import/export tool. i.e. if I might want the file in github to be an epub file, I would configure the github tool to use the [Lucimoo EPUB export/import tools](https://moodle.org/plugins/view/booktool_exportepub) to produce the file that is sent to/from github.

### What it might look like

Initially, it might look like the following. The _(off)_ is meant to be an indication that the connection to github is currently off. i.e. not being used.

[![001_off](images/19910790803_a09eb5e037.jpg)](https://www.flickr.com/photos/david_jones/19910790803/in/dateposted-public/ "001_off")

Clicking on the GitHub link would open up a form that would be used to configure the necessary information including:

1. github repository - that contains the file.
2. file - the actual file being linked to.
3. github credentials - of the author (with the option that this might be left empty for repositories configured to allow that).
4. behaviour spec - i.e. how to import the file (replace existing content, append?), how to handle changes made in the book
    
    Initially, this would probably be left to some default combination. It would also be dependent on the settings of the repository and the permissions of the github credentials.
    
    More work required here.
    

Once this is configured, the administration link would change to indicate that a connection had been made. It would now have a link to the file on github and also some indication of the relationship between the book and the github file. In the following image "clean" implies the book and github file are a match.

[![002_on](images/19909046764_02b7de4273.jpg)](https://www.flickr.com/photos/david_jones/19909046764/in/dateposted-public/ "002_on")

If changes are made in the Moodle book this would mean that the book is "ahead" of the github file. The github link would change appropriately. It would also add an additional link "push". Clicking on that link should probably display a page that provides some details of the changes to be pushed and allows the author to make the choice whether to push or not.

[![003_push](images/20344990589_7fd2d01519.jpg)](https://www.flickr.com/photos/david_jones/20344990589/in/dateposted-public/ "003_push")

If the version of the file on the repository had been changed, then changes are also made.

[![004_out_of_date](images/20344990349_bdf9123aca.jpg)](https://www.flickr.com/photos/david_jones/20344990349/in/dateposted-public/ "004_out_of_date")

Leaving the question of what happens when both local and remote changes have been made? Both? Some thought to be given here.

[![005_both](images/20531711885_3cf579c991.jpg)](https://www.flickr.com/photos/david_jones/20531711885/in/dateposted-public/ "005_both")

### Assumptions

This is all based on

1. The Book author has the details and credentials to a GitHub respository that contains a file of the correct format; This might be a challenge for some authors.
2. There is no local git repository. Asking folk supporting a Moodle instance to install git on the server is a bit much. Instead, the content for the book will be stored in the Moodle database. No problems for Moodle, but raises questions about how to determine whether there have been changes. At least two current possibilities
    1. Store the date of last change on the repo in the Moodle database and compare dates for changes to the book.
    2. Generate/store a version of the HTML file locally and do a compare (sounding very heavyweight).

4. That different books in a single course could be linked to entirely different github repositories.
5. That the idea of adding additional links and status information about github into the administration block doesn't break some Moodle style guide.

### Outstanding questions

Lots.

More specifically

- How to handle links between chapters? A book is made up of chapters (a single HTML page). When displayed in Moodle the Book module provides simple next/previous page navigation. It's also fairly common for authors to hard-code links between chapters (and even into chapters in other books). If the github version of a book stores all the chapters in a single file, what about these links?
    
    How do the existing export/import plugins handle this?
- How to handle embedded resources (images, movies etc)? Books also contain embedded images, movies etc. The issue of how these are provided is a common one. I tend to use external services, but others place them into Moodle, how to handle these? How do the existing export/import plugins handle them?
- Is all of the above technically possible with github, the github API, PHP, Moodle etc.
- Does all this need to be github specific? Is there a way (and a need) for this to git specific, but not github specific?
- What might be the process for create a new file in a repository based on an existing Moodle book?