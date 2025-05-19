---
categories:
- eei
date: 2017-09-23 14:30:28+10:00
next:
  text: '"Learning, learning analytics and multiple levels: The problem of starvation"'
  url: /blog/2017/09/25/learning-learning-analytics-and-multiple-levels-the-problem-of-starvation/
previous:
  text: What's changed in academic staff development?
  url: /blog/2017/07/16/17252/
tags:
- research
- workflow
title: Further developing research workflow
type: post
template: blog-post.html
---
An attempt to briefly document an exploration into possibilities for enhancing my digital workflow.

Main personal outcome is the modification of my research workflow to incorporate Zotfile to improve file naming and also to allow sharing of PDF files with my mobile. Sharing done via Google drive to the PDF Expert app and back again. Zotfile very nicely auto-extacting annotations and highlights from the PDF into Zotero note file.

Still need some further refinement, but good enough to get me reading and highlighting more.

### Why?

I'm reasonably happy with [the move to Zotero](http://djon.es/blog/2017/05/20/bye-bye-mendeley/) for citation management, but have some weaknesses and challenges in my workflow I'd like to address, including:

- Need to more active in annotating, sensemaking and sharing thinking on papers.
- Add the ability to do this on both mobile and laptop platforms.
- Scaffold/guide the use of the tools.

### Changes to make?

From the below, the following might be useful changes to make

- Modify file naming of PDFs to a fixed style.
    
    Zotfile appears to do this for Zotero.
    
- Have files (and Zotero information, and annotations) available via a cloud service
    
    Zotfile will allow this with whichever cloud service
    
    [This post](http://thedigitalresearcher.com/how-to-make-zotero-even-better-with-zotfile/) has more specific advice. Includes mention of being able to explicitly send specific files to the tablet, as well as changing the location where files are stored
    
    Upgrade to the 5.0 version of Zotero, download the Zotfile xpi file and install using Zotero. Change preferences.
    
    Nice - the renaming attachment (existing) works nicely.
    
    Send to tablet uses a Zotero category, configured to a Google drive.
    
    Annotation done on the phone. Used Zotfile to bring it back into Zotero and it automatically extracted the annotations into Zotero notes. Very nice.
    
    And the annotations and highlights I made are visible in Adobe on the laptop. Win all around.
    
- Previous or other as form of back up
- Find a iOS PDF viewer/annotater
    
    [PDF Expert 6](https://thesweetsetup.com/apps/best-pdf-manager-editor-ipad/) seems to be thought highly of. Apparently it supports WebDAV. Opening up the question of whether or not this could be used with the Zotero support for WebDAV? [Article](http://www.chronicle.com/blogs/profhacker/make-your-own-zotero-webdav-server-and-access-your-zotero-attachments-anywhere/38526) talking about setting up your own Webdav Zotero server, using [PHP code](https://github.com/krueschan/phpZoteroWebDAV) last modified 6 years ago.
    
    Trying Google drive using the Zotero send to tablet option. Configure the app with Google account works smoothly. Now to try it out with a journal article I wanted to read - the size of the iPhone might be an issue here.
    
    The worked okay, could get use to it. Size of the phone is an issue.
    
- Experiment with extract annotations from PDFs into Zotero
    
    Zotfile again.
    
- Pay more attention to auto imported citation information
    
    Develop/find a cheatsheet of changes to make \*\*\* need to find this \*\*\*
    
- Pay more attention to how to annotate/highlight

## What are others doing?

First task is to look at what others are doing.

### Introducing digital workflows for academic research on Mac

[First](https://blogs.cul.columbia.edu/butler/2014/04/03/introducing-digital-workflows-for-academic-research-on-the-mac-2/) in a series of blog posts by Francis Hittinger. Quite detailed, though Mac focused and from 3 years ago, interesting to see how well the technologies suggested have aged.

- [PDF chaos - Digital workflow basics](https://blogs.cul.columbia.edu/butler/2014/04/12/pdf-chaos-digital-workflow-basics/)
    
    Uses GTD movement to argue the need for a system for capturing unfinished tasks, to lighten the load. Resonates with me. Starts with PDF workflow.
    
    Make some case for naming, folders etc. But I have a feeling that there's too much focus on computer abstractions and not enough on abstractions meaningful to the task/human.
    
    1. Always OCR PDFs
    2. Split dual-paged PDFs
- [Sente for PDF management](https://blogs.cul.columbia.edu/butler/2014/04/17/sente-for-pdf-management-on-the-mac-and-ipad-1-capturing-and-organizing-pdfs/)
    
    This is where the specific technology focus might prove a challenge for me. [Sente](http://www.thirdstreetsoftware.com/site/Sente.html) is a Mac specific tool similar to Zotero. I'm not likely to change ATM. Maybe lessons I can learn here though.
    
    Largely looks at getting the PDF and the citation into citation management software. Suggestions for alternatives to Google for the citation might be useful.
    
- [Sente management #2](https://blogs.cul.columbia.edu/butler/2014/05/12/sente-for-pdf-management-on-the-mac-and-ipad-2-capturing-and-organizing-pdfs-metadata-tagging-statuses/)
    
    More discussion of Sente's capabilities, some general use if practices abstracted, include a status in the research pipeline for papers, use of tags.
    
- [Sente #3](https://blogs.cul.columbia.edu/butler/2014/05/21/sente-for-pdf-management-on-the-mac-and-ipad-3-quick-add-zotero-workflow-and-automated-researching/)
    
    More ways to get references into Sente
    
- [Sente #4](https://blogs.cul.columbia.edu/butler/2014/06/12/sente-for-pdf-management-on-the-mac-and-ipad-4-readingannotation-in-sente-and-power-note-taking-tagging-with-sente-assistant/)
    
    Focuses on the Sente annotation feature, apparently powerful and cross platform. Some good material on the importance of note taking and even mentions [Xanadu](http://www.xanadu.com/) and a [pandoc/markdown workflow](https://github.com/dh-notes/pandoc-workflow/blob/master/main.md). Identifies some limitations of analog note taking and then launches into using Sente for notetaking, including links to suggestions for [note taking workflow](http://jones.kaist.edu/notebook/2012/09/an-academic-notetaking-workflow.html).
    

And it appears that the series was never ended. Never got to the potentially interesting stuff

### Pandoc and Zotero

[Github](https://github.com/dh-notes/pandoc-workflow/blob/master/main.md) tutorial. A more open approach. [This post](http://verifyandrepair.com/04-11-2016/writing-workflow-2016-markdown-environment/) offers a description of a specific researcher's approach. Offers this rationale for markdown

> Microsoft Word uses the paradigm of the word processor: printed words on a sheet of paper. Markdown treats writing as code: iterative and malleable.

Leads up to [a post](http://verifyandrepair.com/05-12-2016/file-management-version-control/) explaining the benefits of using github when writing. The posts includes various applications etc that help.

[Another post](https://davepwsmith.github.io/academic-scrivener-howto/) linking markdown with Scrivener and Zotero via pandoc.

As someone who uses vim to write code and HTML documents, there's much in this that resonates with me. But I still wonder if I have the time to make this radical a change? If someone with my background pauses, it does seem to suggest that this approach is not for everyone. Which, given a recent attempt to focus on collaboration with others, decreases the likelihood of adoption this approach.

### Correct auto citation import

Google is flaky (forgetting place for books). Better to use Worldcat (OCLC) or official academic library catalogue - Stanford and University of Wisconsin

- Right sort of publication
- pages
- DOI
- Sentence case

### Zotero workflows

[Post](http://www.mkbehr.com/posts/a-research-workflow-with-zotero-and-org-mode/) explaining a workflow that uses Zotero and Emacs enabled by [orgmode](http://orgmode.org/) and [Zotxt](https://gitlab.com/egh/zotxt). Some interesting stuff, especially Zotxt which appears to provide a potential API to your local Zotero library.

[Workflow](http://www.johnbcole.com/scienceblog/a-zotero-based-workflow-for-reading-and-annotating-scientific-articles.html) - Zotero - ZotFile - Dropbox - ZotPad - Notability (PDF viewer/annotator)

### Academic note taking

[A academic notetaking workflow](http://jones.kaist.edu/notebook/2012/09/an-academic-notetaking-workflow.html) take.

[Page](https://forums.zotero.org/discussion/66557/workflow-for-taking-notes-while-resaearching) that mentions use of Zotfile for extracting annotations from PDF documents and into Zotero notes. Might be useful with Zotxt.

[More detailed look](https://gettingthingstech.com/zotero-workflow-zotfile/) at Zotero and ZotFile, covers installing, configuring and then using it to rename and organise PDFs and extracting annotations.

Using Zotfile seems key to moving PDFs to a cloud service.

### Content outlines

[Blog post](https://blogs.cul.columbia.edu/butler/2014/06/05/daniel-wessel-using-content-outlines-and-circus-ponies-notebooks-for-writing-articles-and-theses/) defining and explaining content outlines, in particular getting the structure right.

## Available tools

### Zotero

Zotero has a ["for mobile" page](https://www.zotero.org/support/mobile).

Includes mention of [Papership](http://www.papershipapp.com/) as a PDF annotation tool that integrates with Zotero account. Suggesting a need to have more storage on my Zotero account. Wondering how to make use of other cloud services I already have? [This post](http://islamicate-dh.github.io/2016-05-27-set-up-zotero-between-multiple-computers/) mentions using WebDAV to sync with Google drive (what about one drive?)

[Zotfile](http://zotfile.com/) ([open source](https://github.com/jlegewie/zotfile)) may help with that. Can link with a PDF reader app, focus here seems to be on getting a app that will sync with the particular cloud storage service you're using. Zotfile also appears likely to help with naming of PDF files.

[Some information](http://guides.library.cornell.edu/c.php?g=32258&p=203321) from Cornell University library on zotero syncing/storage management