---
categories:
- moodleopenbook
- thesis
date: 2015-12-11 14:53:38+10:00
next:
  text: '"Book github tool: producing some HTML5"'
  url: /blog/2015/12/14/book-github-tool-producing-some-html5/
previous:
  text: 'Moodle book and GitHub: working together'
  url: /blog/2015/12/03/moodle-book-and-github-working-together/
tags:
- html5
- semantic
title: '"Moodle book to a single file: which format?"'
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: Rolley
      author_email: r.tickner@cqu.edu.au
      author_ip: 138.77.36.60
      author_url: http://rolleys.wordpress.com
      content: 'I really like HTML semantics, here''s some quick tips based on what I
        reckon:
    
        1) add a doctype to the HTML,  (for HTML5)
    
        2) double check that you closed the  tag for chapter 1, as it looks like chapter
        1 and 2 are mistakenly placed in the same section. Oh wait, I see, its no mistake
        its just a subchapter, in that case it looks good.
    
        3) I''d consider putting the text in the  as normal marked up HTML, like  tags
        and so on if there are going to be paragraphs there, or maybe even a  if that
        is supposed to be a subheading under the . The  is fine but just wondering what
        will the actual content be, and thinking what tags will best represent that content.
    
        4) I''d consider using the title attribute rather than my own custom data-title
        attribute, because there''s already a fair amount of support and functionality
        associated with the title attribute, so you might get more bang for buck with
        that as an attribute.
    
        5) where you''ve got  at the very top of your document, a slight error is that
        it should be  .. so (also any  tags you might want)
    
    
        So the above answers a few of your questions, but I''ll give my thoughts on the
        rest:
    
        Q3) parsing code to produce page num sounds okay to me? Not sure?
    
        Q4) you shouldn''t need to parse anything to identify chapters and sub chapters,
        you can do this already with your structure just by using CSS or JS depending
        on what you want to identify it for?  For visual styling, identifying it already
        without even adding class or id attributes is easy, because of the structure you
        have you can say in the css: section {styles for chapter}; section section {styles
        for subchapters}; and stuff like that. For the headings you can do similar: article
        header h1 {}; article section header h1 {} ... all that for css is little verbose
        but it really just depends how you wanna do it and how specific you want styles.  For
        JS, you can do similar stuff.
    
        Q5) not sure, but, most likely some googling will find a jQuery plugin.  I''d
        rather write my own though ha ha
    
        Q6) there''s a lot of stuff out there (google jQuery UI) and there''s stuff like
        bootstrap and all that too, but I think the challenge you''ll have is those lovely
        skinning tools won''t style for the exact semantics you''re using, they''ll be
        using class attributes to apply styles.  I think for what you''re doing you wanna
        style more off the element semantics though and keep your HTML clean of abstract
        formatting as much as possible right?
    
        Q7) i think so, I''m not sure how you''re parsing stuff around.. are you reloading
        whole pages, or grabbing bits of data to and fro on the fly, or?  I like to use
        PHP to parse JSON, then I like to write JS that deals with that to inject and
        manipulate the DOM.  All depends what you''re doing :)
    
    
        Looking good though :)'
      date: '2015-12-14 09:35:06'
      date_gmt: '2015-12-13 23:35:06'
      id: '1460'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: Rolley
      author_email: r.tickner@cqu.edu.au
      author_ip: 138.77.36.60
      author_url: http://rolleys.wordpress.com
      content: hmm. it removed my html.  google HTML5 doc type for that code snippet.
        and also use head instead of header in the very top part of your html.. I'll email
        you a copy of my post with HTML in it for your reference.
      date: '2015-12-14 09:39:46'
      date_gmt: '2015-12-13 23:39:46'
      id: '1461'
      parent: '0'
      type: comment
      user_id: '0'
    
pingbacks:
    - approved: '1'
      author: 'Book github tool: producing some HTML5 | The Weblog of (a) David Jones'
      author_email: null
      author_ip: 192.0.82.89
      author_url: https://davidtjones.wordpress.com/2015/12/14/book-github-tool-producing-some-html5/
      content: '[&#8230;] Moodle book to a single file: which format? [&#8230;]'
      date: '2015-12-14 15:37:46'
      date_gmt: '2015-12-14 05:37:46'
      id: '1462'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The [Moodle Book github tool](/blog/2015/12/03/moodle-book-and-github-working-together/) allows the import/export (pull/push) of Book content from/to GitHub. The content from the Moodle Book is stored as a single file on GitHub. One of the many unanswered questions about the tool is the format of the exported file. The current format is a bit of dodgy HTML with divs, classes, and ids.  Aim here is to figure out if and how the [HTML 5 semantic elements](http://www.w3schools.com/html/html5_semantic_elements.asp) might provide a more useful method.

Given that my last serious web development role and interest was 10+ years ago, some of the following is likely to be a bit silly.  It's not helped by the fact that the online explanation of some of these elements differ and the whole semantic element thing appears to be somewhat less than widely supported and used.

### HTML 5 semantic elements

Are a collection of elements/tags in HTML 5, including <article> <aside> <header> etc that are intended to help define different parts of a web page and thus make it easier to share/reuse data across applications. Sounding exactly like what is needed here.

All are probably relevant, but the more immediately relevant include:

- <article> - Specifies independent, self-contained content. Good match for an individual book. Includes sections.
- <section> - A section in a document. Good match for a book chapter (or sub-chapter)? Can be nested.
- <header>  - for either a document or section Could be used within a section to specify the title of the chapter from the book, but also appear on the page when viewing the single file.
- <footer> - for either document or section Could be used within a section to hold icons for next/previous (getting optional here)
- <nav> - defines a set of navigation links Thinking this could be added to the github file by the tool to add navigation links within the file.  Ability to jump to specific chapters etc.
- <aside>
- <details>
- <main>

### Structure for the single github file

Which brings me to to the following. Note: the Moodle book calls every page a chapter or a sub-chapter. A sub-chapter(s) is nested within a chapter.

\[code lang="html"\] <html> <header> <title>Title of book in Moodle</title> </header> <body>

<article data-title="Title of book in Moodle" data-introformat="1" data-customtitles="0" data-numbering="1" data-navstyle="1"> <header> <h1>Title of book in Moodle</h1> <div>Introduction to the book from Moodle</div> </header>

<section data-pagenum="1" data-contentformat="1" data-title="Title of 1st chapter from book"> <header> <h1>Title of 1st chapter from book</h1> </header> CONTENT OF THE CHAPTER from the book

<section data-pagenum="2" data-contentformat="1" data-title="Title of 2nd chapter (and a sub-chapter) from book"> <header> <h1>Title of 2nd chapter (and a sub-chapter) from book</h1> </header> Content of the sub-chapter from the book </section> </section>

<section data-pagenum="2" data-contentformat="1" data-title="Title of 3rd chapter from book"> <header> <h1>Title of 3rd chapter from book</h1> </header> CONTENT OF THE 3rd CHAPTER from the book

</section> </article> </body> </html> \[/code\]

Entering HTML like that to get pretty coloured in Wordpress is harder than it looks.

Testing the structure is quite easy given [this online outliner](https://gsnedders.html5.org/).

 

### Questions

My first question is whether or not the above is "valid" HTML 5? The outliner seemed to like it.

The second question is whether or not the above will work? Not from a HTML 5 perspective, but my code.

Which picks up the following questions

1. Do the data attributes play nicely with semantic elements?
2. Should the title be both a data attribute and in the header element?
3. Should I rely on the parsing code to auto-generate pagenum?
4. Should I rely on the parsing code to identify chapters and sub-chapters?
5. Are there any nice existing javascript resources that will auto-generate the navigation between chapters? (Or do I have to write something?)
6. Are there any nice CSS resources that will style semantic elements nicely? (Or do I have to write something?)
7. Will the PHP parsing code handle semantic elements (and data attributes)?