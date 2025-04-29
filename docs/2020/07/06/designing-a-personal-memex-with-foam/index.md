---
title: Designing a personal \"memex\" with Foam
date: 2020-07-06 11:11:58+10:00
categories: ['pkm']
tags: ['memex']
coverImage: 49997112801_e233541a82_k-e1593997890516.jpg
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

**Designing potential use of Foam for PKM**

For years I’ve been annoyed at the lack of structure in my approach to managing and leveraging information (it never really becomes knowledge). The process through which I [Seek > Sense > Share](http://jarche.com/2014/02/the-seek-sense-share-framework/) information/knowledge has been ad hoc, disorganised and broken.

Last week @downes shared [details about Foam](http://www.downes.ca/cgi-bin/page.cgi?post=71058). The [first release of which was announced](https://twitter.com/jevakallio/status/1276098596111290370) two weeks before I’m writing this.

The following is me figuring out how I might kludge Foam together with the other assemblages I use to help fix what is broken. Of course, it takes much more than a technology.

## What is Foam? Why use it? Why not?

Foam is a tool intended to help individuals store, manage and leverage knowledge. It’s inspired by tools such as [Roam](https://roamresearch.com/) and [Notion](https://www.notion.so/), which are getting [some attention](https://medium.com/@francescod_ales/is-roam-research-the-next-big-tool-2e969a5245c2). It also harks back to [Smallest Federated Wiki](/blog2/2015/01/21/trying-out-a-new-writing-process/) and [Wikity](http://djon.es/blog/2016/04/23/playing-with-wikity/). Ideas that have promised to help with the problem I’ve identified above, but which I’ve never been sufficiently disciplined to effectively use. Hence no solution.

Foam has some [established principles](https://foambubble.github.io/foam/principles) which resonate and which may help address some of the dissonance prior toools created with my personal practice. Like @downes I am attracted by the underpinning technology used by Foam - [Visual Studio Code](https://code.visualstudio.com/) and [GitHub](https://github.com/). First, because I’m increasingly using those technologies in my work so my familiarity with them is increasing. Forming a virtuous circle, using Foam will help improve my familiarity with these tools and help my work. Second, the small pieces loosely joined approach enabled by both technologies resonates strongly with my [prior work](/blog2/2009/02/15/alternatives-for-the-institutional-implementation-of-e-learning-lessons-from-13-years-of-webfuse/) and assumptions about what works, or not. Though the fact that they still position [“Build vs Assemble”](https://foambubble.github.io/foam/build-vs-assemble) as an either/or suggests that they haven’t made explicit the idea that out it is both/and.

[Foam’s principles](https://foambubble.github.io/foam/principles) mention an intent to “allow users to operate in a decentralised” manner, which is also pleasing. I need to figure out how to integrate Foam into the assemblage of tools, practices and knowledge that will form my PKM processes. Inevitably my choices will be different than others. VSCode and GitHub are designed to more easily support this difference than some other choices. For example, some early examples of how the tools underpinning Foam might help inter-connect Foam with my existing assemblages, include:

- Using this [sync GitHub/Wordpress tool](https://github.com/mAAdhaTTah/wordpress-github-sync) to publish content from Foam to my blog.
- Using this [Python Zotero API](https://pypi.org/project/Pyzotero/) to import notes and references into Foam from my Zotero library.
- Using this [Python module](https://pypi.org/project/pydiigo/) to import bookmarks and comments from Diigo (and perhaps a similar
- Using this [Python module](https://pypi.org/project/python-hypothesis/) to do similar with Hypothes.is.

And that list is without exploring further into the VSCode ecosystem (e.g. this [citation picker for Zotero](https://marketplace.visualstudio.com/items?itemName=mblode.zotero) or the VSCode extension that allows typing TODO in a note to create a github issue). The presence of these ecosystems point to the strength of using technologies (VSCode/GitHub) that are widely used by a lot of people (who code). The list above illustrates that other people have already provided solutions to requirement I have. Solutions which are generally protean enough for me to customise to my context.

### Why not use Foam?

It’s still early days. There remains a question whether this tool and its community will evolve productively. It’s also a bit rough around the edges and perhaps not fully feature complete. Not surprising since it is essentially [two weeks since the release of a functional prototype](https://twitter.com/jevakallio/status/1276102925849329664).

Foam is not an integrated system. It’s a best-of-breed system. Each of these [product models have plusses and minuses](/blog2/2009/08/31/product-models-lms-bob-and-alternatives/). A best-of-breed approach is more flexible and customisable. It’s also requires more knowledge to use effectively. Especially when the number of components that make up the best-of-breed system becomes quite large. As it can quickly become with Foam. Also, Foam is a best-of-breed system that you are responsible for fitting together.

The technical knowledge required to get going is relatively high. Rough around the edges means it’s probably best if you are familiar already with GitHub and VSCode. Markdown is the core authoring environment. It’s something else to learn.

The reliance on the filesystem to store data may be a limit on functionality and scalability. This type of note-taking approach (arguably) works best with a hypertext type structure. Not a hierarchical/categorical structure. The Web versus Gopher. A problem touched on by [Berners-Lee talking about Bush](https://www.w3.org/Talks/9510_Bush/Talk.html). GitHub controls file structures. File structures are hierarchical.

### What else might you use?

There’s a GitHub repository to answer that question. The [Digital Gardners repo](https://github.com/MaggieAppleton/digital-gardeners) is described as “A collective of gardners publicly tending their digital notes on the interwebs”. It includes sections on Gardening Tools, How-tos, theory etc.

Interesting that @holden’s [dLRN 2015 presentation](https://hapgood.us/2015/10/17/the-garden-and-the-stream-a-technopastoral/) gets a mention. First connection to my earlier dabbling and still one of the best descriptions of the importance/difference of this type of approach. In which he harks back to memex and explains why the following isn’t an entirely fitting name for what I might do with Foam here. e.g. contains my material and the materials of others. Links are associative. Links made by readers and writers.

## **Introducing Memex**

My first quick test of Foam was labelled secondBrain. I wasn’t happy with that name and the following illustrates that I’ve moved further away from that term. To quote Bush (Bush, 1945)...”it needs a name”...

> Consider a future device for individual use, which is a sort of mechanized private file and library. It needs a name, and to coin one at random, “memex’’ will do. A memex is a device in which an individual stores all his books, records, and communications, and which is mechanized so that it may be consulted with exceeding speed and flexibility. It is an enlarged intimate supplement to his memory.

While this use of Foam is certainly not going to be functionaly equivalent to Bush’s “memex” or later conceptualisations informed by the Web and greater hypertext thinking. The purpose certainly fits. I’m hoping the disciplined use of Foam will provide “an enlarged supplement” to my memory etc.

So welcome to my [personal prototype memex](https://djplaner.github.io/memex/). That will take you to the github pages representation of the memex. If you’re really keen you can access [the github repository](https://github.com/djplaner/memex).

As it stands it is pretty limited. I still haven’t figured out completely how to use it.

## How to use it?

One of [the Foam principles](https://foambubble.github.io/foam/principles) is “Foam is not a philosophy”. i.e. how you use Foam is really up to you. Figuring how to use Foam in an effective and disciplined way is perhaps the hardest task. A task I’ve not been successful with to date with other tools. The following is some exploration and thinking about how I might turn this around.

The [Foam recipes section on Worflow](https://foambubble.github.io/foam/recipes" \l "workflow) is currently empty. But Foam does talk mention [Second Brain](https://www.keepproductive.com/blog/how-to-build-a-second-brain) and Zettelkasten (which is not a new idea). There are others. The [digital gardeners repo](https://github.com/MaggieAppleton/digital-gardeners) mentions some. Following explore Zettelkasten, SecondBrain and Seek > Sense > Share for ideas to inspire how I might use Foam.

### Zettelkasten

This [Medium post on Zettelkasten](https://writingcooperative.com/zettelkasten-its-like-gtd-for-writing-and-here-s-why-you-should-consider-it-7dddf02be394) (a form of notetaking) describes the zettelkasten method as relying on a sequence of activities: Collect, Process, Cross-Reference and Use. It also lists the following requirements

- Notes are atomic. i.e. as [mentioned here](https://leananki.com/zettelkasten-method-smart-notes/), make them agnostic to a parent topic.
- Each note has a home. But also points out the limitation of a topic based organisation as notes can belong to multiple topics. An [emergent home](https://leananki.com/zettelkasten-method-smart-notes/).
- Each note has a name.
- Notes link to other notes.
- Cross reference keywords.

A [more detailed post on zettelkasten](https://leananki.com/zettelkasten-method-smart-notes/) offers the following “tools for the zettelkasten method”

- Inbox. Where rough ideas are captured for further processing.
- Reference manager. How you cite references. Mentions Zotero. Rasing the question of how to cite references in Markdown/VSCode? Hey presto, [there’s a VSCode package](https://marketplace.visualstudio.com/items?itemName=mblode.zotero) for that.
- The Zettelkasten Recommneded that this be plain-text. This is where Foam most explicitly enters the picture.

It also offers the following process

- Capture. Reading and taking literature notes. Literature notes are a collection of all the notes made on an article/book.
- Elaborate. Turning notes into Zettels. Summarise contents into the Zettel title. Write for others. A structure including
    - Title/Zettel id
    - Elaboration
    - Highlights
- Connect Add them into the network of Zettels. Tags. Links out and in. Structure notes become important here. Including indication of type of note in Zettel UID: L=literature note. L2=mid-level structure note. L1=top-level structure notes….perhaps too much.
    
    Tags. Use different types of tags ## for L1 notes.

### Second Brain

[SecondBrain](https://fortelabs.co/blog/basboverview/) appears to be a similar and more commercial process (e.g. there’s a [company LinkedIn page](https://www.linkedin.com/company/secondbrain/)). This [description of SecondBrain](https://www.keepproductive.com/blog/how-to-build-a-second-brain) identifies two core concepts: CODE and PARA.

CODE summarises “four universal steps”

- Collect – a place to collect what’s interesting.
- Organise – the structure it suggests is captured by PARA
- Distill – notes themselves aren’t enough. Progressive summarisation.
- Express – share with the world.

PARA suggests structuring content into

- Projects – tasks liked to a goal/deadline
- Areas – sphere of activity to be maintained
- Resources – topic or theme of on-going interest
- Archives – inactive items from the first three.

This sequence is meant to capture the flow between actionable tasks (Projects down) and non-actionable information.

[Progressive summarisation](https://fortelabs.co/blog/progressive-summarization-a-practical-technique-for-designing-discoverable-notes/) appears to be the description of how to create and manipulate notes through the PARA/CODE concepts. Based on the idea of “note-first” rather than tag or category first. i.e. the primary focus is design of individual notes. Balancing discoverability (relying on compression) and understanding (relying on context) – touching on the reusability paradox.

Progress summarisation has layers of summarisation and the idea of opportunistic compression. You do it over time as needed. Not all resources go through all the layers. The layers are

- Layer 0 – the original, full-length resource.
- Layer 1 – initial notes/summary generated by note-taking program.
- Layer 2 – bold passages. The “best parts” of the Layer 1 notes. The core of the idea.
- Layer 3 – Highlighted passages The “best of the best”.
- Layer 4 – Mini-summary. 2 & 3 converted into an executive summary.
- Layer 5 – Remix. Changes to how and where they are structured. Perhaps more linked with expressing the idea.

SecondBrain doesn’t (as of yet) capture the flow of random insights coming in???

### Seek > Sense > Share

The [Seek > Sense > Share Framework](http://jarche.com/2014/02/the-seek-sense-share-framework/) from [@hjarch](https://twitter.com/hjarche)e offers a conceptualisation that I’ve used personally and in my teaching for quite some time. It’s seen as a method for putting [Personal Knowledge Mastery](http://jarche.com/pkm/pkm-workshop/) into practice. It offers more a way of thinking about what’s required rather than offering explicit guidance into the how – one of its strengths. It’s easy to see connections between Seek/Sense/Share, CODE and the other processes above.

## **What do I want to do with it?**

Frameworks are useful, but how do I want to apply them. What do I need/want to do? Who am I? Who do I want to be?

I increasingly think of myself as a toolsmith in the sense expressed by Brooks (1996) whose delight “is to fasion powertools and amplifiers for minds” (p. 64). I’m a nerd who builds things that people want to use for pesonally productive ends. Mostly in the realm of (formal) educational technology. Consequently, it’s much more complex than just technology. Hence the current title of this blog – some assemblage required. Theory about people, learning, systems, organisations, teaching etc is required. Hence the tasks I need to undertake could include: reading, writing papers, developing software, thinking.

I’m not sure I see SecondBrain’s PARA approach fitting here. I won’t be using Foam for everything. Just tracking of notes. Zettelkasten seems a better fit for the purpose. Plus I’m worrred about too explicit a categorisation scheme and especially Foam’s reliance on the file structure and subsequent scalability issues. All notes in a single directory?

### **The purpose**

The intent is that [my memex](https://djplaner.github.io/memex/) will be where I store more notes which eventually become Zettels. The workflow will mirror Seek > Sense > Share. With memex being the core of Sense but having connection swith Seek and Share. Perhaps suggesting that Seek > Sense > Share become the structure.

### Initial design

The home page could have a brief background, but then links to Seek, Sense and Share. Sections on the home page but also directories in the repo used in the following way

- Seek. Contains pointers (and perhaps scripts) used to triage notes from seeking into memex. Layer 1 in SecondBrain concepts. A todo list of notes that need to be made sense of.
- Sense. Where all the Zettels sit. As “seek notes” are summarised and connected they move into this directory. The sense page contains lists of stucture notes and unallocated notes. Structure notes represent major areas of interest I’m working on and may correspond to directories within the sense directory. Unallocated notes are those that have been “zettelised” but which aren’t yet connected.
- Share. Contain an explanation of various means I’m using for sharing, but also explicit outcomes. e.g. papers, blog posts, github repos? Etc. Some of the outcomes would be works in progress, but others may be concrete artifacts that are used as part of my POSSE model.

## To do

I now need to figure out if and how this plan can be best implemented with Foam’s nascent and evolving functionality and subsequently integrated into my assemblage of technologies and practices.

### Foam questions

The whole directory/file question is probably the main one at the moment. If/how to do that and what are the trade-offs?

How do w[iki links](https://foambubble.github.io/foam/wiki-links) work and from there visualisation and back linking?

If and how can tags be simulated within Foam? Can I add “tags” to markdown files in a way that allows the automated genration of structure notes?

And I’m sure many others

### Assemblage integration

For this to work I need to connect memex to the rest of the tools I use

Seek

- [Fix my Zotero installation](https://www.nrel.colostate.edu/set-up-best-reference-manager/).
- Translate notes from various sources (Kindle, Zotero, Diigo, Hypothes.is, Wikity) into memex.
- Put in place process to keep those notes flowing into this.

Sense

- Work out the process, structure and technology to make sense of in-coming notes.
    - What’s the landing page into memex like?
    - Structure underneath.
- Figure out how Zotero and VSCode can effectively work together
- Figure out how to handle moving notes around the directory structure and connection with links (wiki and markdown)

Share

- Explore POSSE style links from Foam to
    - my blog (wordpress). Posting and pages?
    - Twitter.
    - MS Teams?
- How it figures into more formal writing.

And of course the simple task of trying to get all this to fit together and use in a disciplined and effective way.

## References

Brooks, F. (1996). The Computer Scientist as Toolsmith II. _Communications of the ACM_, _39_(3), 61–68.

Bush, V. (1945). As We May Think. _The Atlantic Monthly_.