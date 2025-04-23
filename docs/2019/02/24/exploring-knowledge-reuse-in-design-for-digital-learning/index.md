---
title: Exploring knowledge reuse in design for digital learning
date: 2019-02-24 15:46:18+10:00
categories: ['bad', 'casa', 'elearning']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

This post continues an on-going exploration of knowledge reuse in design for digital learning. Previous posts ([one](/blog2/2019/01/30/improving-reuse-of-design-knowledge-in-a-lms/) and [two](/blog2/2019/02/10/digital-learning-templates-adding-context-and-configuration/)) started the exploration in the context of developing an assemblage to help designers of web-based learning environments create [a card interface](https://medium.com/designed-thought/the-design-and-morality-of-the-card-interface-1f8349e9a9c0) (see Figure 1). Implementing such a design from scratch requires a diverse collection of knowledge that is beyond most individuals. It is hoped that packaging that knowledge into an assemblage of technologies will allow for that knowledge to be used and reused (within Blackboard 9.1) by more people and subsequently have a positive impact on the learning environment and experience.

The card inteface is a simple example of this work. The requirements of the card interface are fairly contained and pre-defined. The next challenge is to explore if and how this can be expanded to something more difficult and open-ended.

![](images/wAGZr6VW5+HagAAAABJRU5ErkJggg==)  
Figure 1: Card interface example

## Problem: developing and maintaining online learning content

Back in 2015 [@abelardopardo](https://twitter.com/abelardopardo?lang=en) wrote a blog post titled [Re-visiting authoring: Reauthoring](http://abelardopardo.blogspot.com/2015/02/re-visiting-authoring-reauthoring.html) which starts

> Creating learning resources is getting incredibly difficult. Gone are the days in which a bunch of PDFs or PPTs were the only resources available to students. In a matter of years, learning resources have to be engaging, interactive, render in all sorts of device..

[This thread](https://community.blackboard.com/thread/6523-content-editor-html-vs-pdf) from the Blackboard community site provides evidence of the problem elsewhere and directly echoes my own experiences with the Blackboard LMS.

> I'm finding that relying primarily on the Blackboard Content Editor to post materials in the course shell as HTML is a time relatively consuming process. I am concerned that, despite training, some faculty may find maintaining these courses too technically challenging. Many faculty have been posting their entire courses as MS word docs. (Behnke, 2018)

Andecdotal observations of my local context suggests that learning modules (online content) with Blackboard generally come in the following categories:

- Nothing.
- Word documents or Powerpoint files.
- Collections of Blackboard content items (e.g. the image on the Blackboard link) – with variable design quality.
- High-end versions designed and implemented by teams of specialists.

The distribution between categories seems to lean heavily toward the first three categories. Contributing factors appear to include: the institutional assumption that individual teachers are largely responsible for producing learning resources; the availability of specialists to help is limited to strategic projects; and, the difficulty of using the Blackboard 9.1 tools to generate learning modules.

As a specialist assigned to a strategic project, my task has been to help a brand new program set up their course sites, including learning modules. Echoing Behnke’s (2018) quote I’ve found using the Blackboard tools too time consuming for outcomes of limited quality.

Hence I needed a solution to the authoring problem that would enable the quick creation and on-going maintenance of good quality online learning modules. A solution with a low floor (i.e. easy enough that an “average” teacher could use it) and a high ceiling (i.e. capable of creating advanced features and high quality). A solution that worked with the tools to hand in my current context.

# Solution: the Content Interface

The last couple of weeks have seen the development of an assemblage of technologies currently labelled (unimaginitevely) [the Content Interface](https://github.com/djplaner/Content-Interface-Tweak). Figure 2 is a screen shot of an example learning module produced using the Content Interface. This blog post was also produced using the first two steps of the Content Interface process. The following sections outline the three step Content Interface process used to produce learning modules.

### 1\. Create and edit content as a Word document

Microsoft Word, of if you’d prefer LibreOffice, is used to create and edit content that is saved as a Word document (.docx). The Word document must be structured using [styles](http://www.consultdmw.com/how-to-use-word-styles.html), including some styles specific to the Content Interface (e.g. Note, Reading, Activity, Embed). For example, [t](https://drive.google.com/file/d/1KvHYiAklqn5RVWcO62cyp7ifBeRA2MA0/view?usp=sharing)[his Word document](https://drive.google.com/file/d/1KvHYiAklqn5RVWcO62cyp7ifBeRA2MA0/view?usp=sharing) was used to produce the learning module shown in Figure 2. That Word document and the learning module is actually an introduction to the Content Interface and illustrates the use of styles. Feel free to download [the Word document](https://drive.google.com/file/d/1KvHYiAklqn5RVWcO62cyp7ifBeRA2MA0/view?usp=sharing) for the learning module in Figure 2 and compare its contents with Figure 2. You can also download [the Word document](https://drive.google.com/file/d/1WwDyIJCZolRjhu_YqByB1JHalLJH7j0A/view?usp=sharing) used to produce this blog post.

![](images/n8jISO3Aesj5DwLnCBl9hcHOAAAAAElFTkSuQmCC)  
Figure 2: Content interface example - Blackboard

### 2\. Convert to HTML using Mammoth

Once editing is complete, the Word document is uploaded to a Web form that converts it into clean HTML. This is done using a locally configured version of [Mammoth.js](https://github.com/mwilliamson/mammoth.js) (a Javascript version of [Mammoth](https://mike.zwobble.org/projects/mammoth/)). Using a _Click to_ copy button on the form, the HTML produced by Mammoth is copied into the clipboard and then pasted into a Blackboard content area. Or, as with this blog post any other web publishing service such as Wordpress. It’s just HTML.

### 3\. Transform the HTML

Since Mammoth produces very nice semantic HTML it’s fairly easy to transform using Javascript. Figure 2 is an example of the current transformation that is done by a combination of Javascript and CSS. Each learning module page in Blackboard has a Javascript file included to perform transformations, including:

- Dividing the document into sections based on _Heading 1_ and displaying the sections via an [Accordion interface](https://en.wikipedia.org/wiki/Accordion_\(GUI\)).
- Allowing any embedded HTML code (e.g. YouTube video) to be displayed.
- Transforming a growing number of higher level semantic elements.  
    For example, the Reading shown in Figure 2. If you examine [the Word document](https://drive.google.com/file/d/1KvHYiAklqn5RVWcO62cyp7ifBeRA2MA0/view?usp=sharing) from which the learning module in Figure 2 was produced,you will see that the text for the activity is displayed as normal text. No icon of someone reading a book. If examine the style, you’ll find that the text does have the Word style _Reading_ applied to it. When it detects text with this style, the Javascript/CSS performs the transformation showin in Figure 2.
- Ensure any non-Blackboard links open in a new Window.  
    By default, Blackboard generates an error if any attempt is made to open a non-Blackboard link in the current browser window.

# Is it any good?

### Eating my own dog food

For a start, it works for me. I’m [eating my own dog food](https://en.wikipedia.org/wiki/Eating_your_own_dog_food). I find I’m able to prepare learning modules (i.e. HTML) quickly and easily. It’s also much easier to work on learning modules provided by someone else. I’m also finding it very useful for me at the moment as I often find having time available to write blog posts coincides with an absence of network connectivity. Not a problem when using a Word processor. In addition, using Word/LibreOffice also means that I can use Zotero for citation management, as well as all the other features (and the foibles) of contemporary Word processors.

At the very least I can see myself using this process, what about others?

### Learning modules for four LMS sites

I’ve been working with three different academics helping them create learning modules for four different course sites. Most of these learning modules are being produced in the last couple of weeks leading up to the start of semester when the academics are busy. So far, discussions with those staff have generated positive comments about the improvement in the quality of the end product and about the value of working in Word, rather than the Blackboard interface.

This week we’ve discovered that sharing Word documents via OneDrive (part of the institution’s technology infrastrucutre) provides some promising benefits. Such documents are shared with the course teaching and development team via a link from the Blackboard learning module page. This provides a single point to go to for the learning module. OneDrive provides the ability to edit online and also provides version control. More exploration needed here.

Other specialists I work with are also talking about the promise the content inteface offers for use in other courses.

Week 1 of trimester starts this week. Still too early to have feedback from students.

### Abelardo’s conditions

In [his blog post](http://abelardopardo.blogspot.com/2015/02/re-visiting-authoring-reauthoring.html), Abelardo identifies seven conditions he was using when looking for a solution. Table 1 is a summary of his conditions and a note on how well (or not) the Content Interface approach meets each condition.

|   **Condition**   |   **Description**   |   **Content Interface**   |
| --- | --- | --- |
|   Content focus   |   No need to worry about visual appearance, table of contents, responsiveness etc.   |   Yes, but more work possible/required.  Mammoth only translate semantic information. Formatting and further transformation done via Javascript/CSS.  More work is required on the Javascript/CSS to provide ToC.   |
|   Support complex textual structures   |   e.g. cross-referencing, sections, subsections, figures, links etc.   |   Yes.  Word/LibreOffice provides much of this.  Javascript/CSS provides additional structures (e.g. Notes, Readings, Activities and more to come)   |
|   Support for interactive elements   |   Embedding videos, MCQs etc.   |   Yes.  Insert any HTML embed code in a document and apply the _Embed_ style   |
|   Use HTML as the underlying format   |   HTML5 in particular   |   Yes.  At least in terms of publishing as HTML anywhere HTML is taken.   |
|   Support collaborative production   |   Version control etc.   |   Early indications, yes.  Experiments with OneDrive to share the Word documents appears to provide this.   |
|   Run on your own machine   |   No complex interface in an online tool, push a button to publish remotely   |   Yes, more work to do.  You author using Word. Work to be done on the one button publishing.   |

# Problems and challenges

Perhaps the biggest limitations and source of challenge with this process is the use of Microsoft Word as the main authoring format. Even though most of the academics I work with use Word as their primary word processor there are issues. Word’s foibles as an authoring platform (e.g. see Figure 3 and [the associated explanation](https://www.explainxkcd.com/wiki/index.php/2109:_Invisible_Formatting)), the stretching of Word’s styles functionality through this process; and, a tendency for many people not to really understand how to use Word as intended (e.g. Ben-Ari & Yeshno, 2006). Hence there’s a question about the mechanics of the process. However, early experience shows there may be some hope.

![](images/5QlgoB+NtEwAAAAASUVORK5CYII=)  
Figure 3: [xkcd's explanation](https://m.xkcd.com/2109/) of one of the challenges of using Word processors

There’s also the question of whether or not the “write in Word and publish in the LMS” process will be an abstraction too far. In particular, the increasing use of semantic elements in Word. A practice that challenges the typical formatting driven use of Word. Intermingled with this is that while the content interface may help reduce the cognitive load associated with the technical aspects of authoring, will this translate to an increased focus on design for learning?

# On-going development

The content interface has been a working concern for less than two weeks. It is hoped that a lot more development will be done to refine this process and its output. Some current plans include:

- One button publishing;  
    Rather than manually upload the Word document and then copy and paste the HTML code, the hope is we can implement a _Publish_ button in Blackboard that automates this process, perhaps connected with OneDrive.
- Program/project specific designs;  
    Currently all learning modules get the same, fairly limited design (i.e. Figure 2). It would be fairly easy to modify the Content Interface to use different visual designs for different programs or other purposes.
- Alternate interface designs;  
    The accordion interface shown in Figure 2 could be changed. For example, a [simple page interface](https://codepen.io/canis1980/full/WaEXZz) and hopefully more contemporary and effective designs.
- Integration of Blackboard content items and tools; and,  
    Blackboard provides a range of items/tools that can be included in a learning module (e.g. quizzes, assignments, discussion forums etc). The aim is to modify the Content Interface to allow such Blackboard tools to be integrated into content at appropriate places.
- Higher level semantic elements.  
    Current semantic elements (e.g. Reading, Activity and Note) are fairly low level. All that happens is that some additional HTML/CSS is added. A good long term goal would be to allow the use of higher level semantic elements that equate to learning designs/activities. For example, allow the use of a Debate style in a Word document which would set up an online environment that helps implement and orchestrate a debate.

# References

Behnke, J. (2018). Content editor HTML vs. PDF? Retrieved February 24, 2019, from https://community.blackboard.com/thread/6523-content-editor-html-vs-pdf

Ben-Ari, M., & Yeshno, T. (2006). Conceptual Models of Software Artifacts. _Interacting with Computers_, _18_(6), 1336–1350. https://doi.org/10.1016/j.intcom.2006.03.005