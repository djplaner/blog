---
title: How to help improve the Moodle book module
date: 2015-02-10 19:55:30+10:00
categories: ['bad', 'concretelounge', 'edc3100', 'moodle']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Initial rationale and ideas for &#8220;continuous improvement&#8221; of
        learning and teaching | The Weblog of (a) David Jones
      author_email: null
      author_ip: 192.0.81.34
      author_url: https://davidtjones.wordpress.com/2015/02/18/initial-rationale-and-ideas-for-continuous-improvement-of-learning-and-teaching/
      content: '[&#8230;] &larr; How to help improve the Moodle book&nbsp;module [&#8230;]'
      date: '2015-02-18 12:57:43'
      date_gmt: '2015-02-18 02:57:43'
      id: '1223'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: Starting the &#8220;Moodle open book&#8221; project | The Weblog of (a)
        David Jones
      author_email: null
      author_ip: 192.0.82.20
      author_url: https://davidtjones.wordpress.com/2015/04/13/starting-the-moodle-open-book-project/
      content: '[&#8230;] trip authoring with the Moodle book module has some space for
        improvement. These simple steps have helped, but more could be [&#8230;]'
      date: '2015-04-13 22:10:12'
      date_gmt: '2015-04-13 12:10:12'
      id: '1224'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: 'Import and the Book module: a case of knowledge loss? | The Weblog of (a)
        David Jones'
      author_email: null
      author_ip: 192.0.86.68
      author_url: https://davidtjones.wordpress.com/2015/07/18/import-and-the-book-module-a-case-of-knowledge-loss/
      content: '[&#8230;] outlined in this post I had a problem with the Moodle Book module
        and its import functionality. A problem illustrated by [&#8230;]'
      date: '2015-07-18 15:53:50'
      date_gmt: '2015-07-18 05:53:50'
      id: '1225'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
As mentioned [in the last post](/blog2/2015/02/08/kludging-an-authoring-process-with-moodle-books-etc/) there are limitations in the Moodle book module that are acting as [a concrete lounge](http://fedwiki.djon.es/view/welcome-visitors/view/concrete-lounge). The following documents an attempt to help improve the module.

In the end, I've made some serious steps to contributing a bit of code to a standard plugin (as I write this, I'm imagining how experienced Moodle folk will shudder at the many misuses of Moodle terms in the following).

**Update:** The "bug" in the Book module reported below is not a bug. There's actually functionality in the Book module to support this, it's just not obvious. More [explanation is available](/blog2/2015/07/18/import-and-the-book-module-a-case-of-knowledge-loss/).

## Task and context

As described in [the last post](/blog2/2015/02/08/kludging-an-authoring-process-with-moodle-books-etc/) the context is a course website hosted in the Moodle LMS. A course that uses quite heavily [the Moodle book module](https://docs.moodle.org/28/en/Book_module). The module has import function that is meant to allow you to import a collection of HTML documents into a book.

## Concrete lounge

The problems with the import process include

1. Titles for imported titles are 100% from the HTML filenames. e.g. call your file "Diigo tool disappears\_sub.html" and the chapter title will be "Diigo tool disappears\_sub.html". Rather than "Diigo tool disappears". The \_sub is required by the import function to indicate a sub-chapter. The .html is to indicate a HTML file.
2. The order of imported chapters is based on the order in the file system. e.g. If I have the following files to import \[code lang="sh"\] dj:001 david$ ls \*.html A blog.html Diigo tool disappears\_sub.html Diigo.html The tools we'll be using.html Twitter.html \[/code\] Regardless of the order in which I add these files to the zip file (import is via a zip file), the order that they will appear as chapters in the book is dependent on the order the file system of the Moodle computer creates. Even if I create the zip file in the right order \[code lang="sh"\] dj:001 david$ unzip -t import.zip Archive: import.zip testing: The tools we'll be using.html OK testing: Diigo.html OK testing: Diigo tool disappears\_sub.html OK testing: A blog.html OK testing: Twitter.html OK No errors detected in compressed data of import.zip. \[/code\] The first chapter will be "A blog.html"
3. There is not option to remove all existing chapters before import. There are situations where I'm trying to replace the entire book with the import. Currently I have to create a brand-new book resource, or manually remove all the chapters in the current book.
4. No method for linking to a chapter prior to import. If I create the collection of chapters elsewhere, there will be times when I wish to create links between those chapters. Currently there is apparently no capacity to do this.

## Bricolage

Here's what I've done so far to address this problem with the resources available.

### Process to make changes to Moodle core

[This seems](https://docs.moodle.org/dev/Process#Fixing_a_bug) to be the process I need to follow for the above which translates into

1. Is there a tracker issue? Via various trails I end up at the [book page/section](https://tracker.moodle.org/browse/MDL/component/12138/?selectedTab=com.atlassian.jira.jira-projects-plugin:component-summary-panel) in tracker. Raising the question which versions of the book Module am I dealing with? Time to track through the [book issues](https://tracker.moodle.org/browse/MDL-37199?jql=project%20%3D%20MDL%20AND%20component%20%3D%20Book%20ORDER%20BY%20updated%20DESC%2C%20priority%20DESC%2C%20created%20ASC) in tracker. Those related appear to be
    
    - [support for re-importing chapters](https://tracker.moodle.org/browse/MDL-33219?jql=project%20%3D%20MDL%20AND%20component%20%3D%20Book%20ORDER%20BY%20updated%20DESC%2C%20priority%20DESC%2C%20created%20ASC) Close to what I'm working on. But it's old. Created in 2008.
    - [Book HTML zip incorrect URL](https://tracker.moodle.org/browse/MDL-41473?jql=project%20%3D%20MDL%20AND%20component%20%3D%20Book%20ORDER%20BY%20updated%20DESC%2C%20priority%20DESC%2C%20created%20ASC) Picks up on the issue with links between chapters that have been imported. This appears to have been fixed and should be in from 2.5 onwards. Need to check this (NOTE: I haven't actually tried this process yet).
    
    Nothing apparent.
    
    So as [a user](https://docs.moodle.org/dev/Process#Users) I can report the bug/make a feature request and then contribute by making a fix. So let's create an issue in tracker. What type of issue should it be?
    
    - bug - A problem which impairs or prevents the functions of the product.
    - improvement - An improvement or enhancement to an existing feature or task.
    
    Either could apply. I'll be positive and call it an improvement. [Issue created](https://tracker.moodle.org/browse/MDL-49128?filter=-2).
2. Which branches should the fix be made on? The advice is
    
    > Bugs should normally be fixed on all the supported stable branches that are affected. New features should just go into master, but sometimes minor enhancements are made on the most recent stable branch.
    
    So where does this fit? I assume a bug or minor enhancement. The other factor is that if I make this change on the version that my institution is using, that will increase the chances that I might get to use it this semester (which are very slim). Of course, it's difficult to remember/discover which version of Moodle we're using. I think perhaps 2.7 for now. Which seems to the [other supported release](https://download.moodle.org/releases/supported/).
3. Develop the change using git [Prior work](/blog2/2013/05/26/preparing-bim-for-moodle-2-4-and-beyond/) contains an example of how to get a version of the Moodle source using git and start making changes. Will start with that.
    
    My issue number is MDL-49128
    
    - [Git for developers](https://docs.moodle.org/dev/Git_for_developers) This is the process I'm currently using.
    - [GIT commit cheat sheet](https://docs.moodle.org/dev/Commit_cheat_sheet)
    
    The process I'll use is
    - Fork the branch of Moodle I want to work on MOODLE\_??\_STABLE \[code lang="sh"\] dj: david$ history | grep git git clone git://git.moodle.org/moodle.git git clone git://github.com/djplaner/moodle.git git branch -a # what are the available branches git remote add upstream git://git.moodle.org/moodle.git # connect upstream git checkout MOODLE\_27\_STABLE \[/code\]
    - Create the branch \[code lang="sh"\] git checkout -b MDL-49128-book-import-fixes origin/master \[/code\]
    - Make changes - see below
    
    - Testing process
        - zipfiles.zip Has the following files that should be displayed in this order
            1. The tools we'll be using.html
            2. Diigo.html
            3. Diigo tool disappears\_sub.html (this is a sub chapter)
            4. A blog.html
            5. Twitter.htmlWithout either fix the chapters will start with A blog.html, Diigo.html etc. through to Twitter.html. With the both fixes, the order of chapters should match the numbered list above. Also, the chapter names should not include .html or \_sub
        - zipdirs.zip Has essentially the same chapters, however, they are implemented as folders containing a single HTML.
    - Commit the changes to my repo This wasn't as straight forward as I thought. Ended up with \[code lang="sh"\] git remote set-url origin https://github.com/djplaner/moodle.git git push origin MDL-49128-book-import-fixes \[/code\] Which ends up creating this [nice little summary](https://github.com/djplaner/moodle/compare/MDL-49128-book-import-fixes?expand=1) on github.
    - Ask the Moodle devleopers to review it Updated the issue in the tracker, time to wait and see what I got wrong.

### Making changes

I've been using the zipfiles approach. A zip file with a collection of HTML files, each file equals one chapter. This is fixed based on previous work.

There is also a zipfolders approach. A zip file of folders. Where each folder equals one chapter.

The order fix is working on zip folders. However, with the chapter names, I'm now getting both the chapter name and the file name. So _The tools well be using/The tools well be using_. Should the filename or the folder name be used?

I'm assuming the folder name. The book module import code appears to support this. For example when reading HTML files it is looking for default files in the folders. i.e. Default.htm and index.htm. Suggesting that it isn't assuming that these have the names of the chapters.

That appears to be working.

## Factors

I have to think that anyone who had used the import function in action - like I [tried to do](/blog2/2015/02/08/kludging-an-authoring-process-with-moodle-books-etc/) - would have been aware of the limitations of the import function. It just doesn't seem designed to be useful. Thus it seems logical to suspect that maybe the original designer wasn't a user. They weren't solving their own (or someone close to them) problem. Just implementing a feature. Hence they weren't in a position to know how limited it was.

This distance between implementing the function and using the function seems to be a common feature of concrete lounges. Anyone who has to use a concrete lounge for any length of time is going to be aware of the pain and want to change it.

The fact that this particular bit of pain has stood for so long, has to say something. Perhaps it's just at the book module is just an unloved child? But it is part of Moodle core now, so it has to be perceived to be useful for some.