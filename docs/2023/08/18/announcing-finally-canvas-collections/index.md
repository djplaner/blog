---
title: Announcing (finally) Canvas Collections
date: 2023-08-18 12:19:47+10:00
categories: ['casa']
tags: ['canvas', 'casa']
coverImage: Collections-2.png
type: post
template: blog-post.html
---
Finally, a reasonable version of Canvas Collections and associated support materials is ready to announce. Following will eventually form the content of a blog post posted to [the Canvas community space](https://community.canvaslms.com/t5/Canvas/ct-p/canvas).

## Introduction

Canvas Collections is an open source tool that helps to transform the Canvas modules index page by adding [structure](https://djplaner.github.io/canvas-collections/#structure), [visuals](https://djplaner.github.io/canvas-collections/#visuals), and [context](https://djplaner.github.io/canvas-collections/#context). This can help you improve the organisation, aesthetics, usability, and findability of your Canvas course. Improvements known to [enhance student self-efficacy, motivation, and retention](https://djplaner.github.io/canvas-collections/#why).

The following offers a summary of how you use it and what you can do with Canvas Collections. See the [Canvas Collections' site for more](https://djplaner.github.io/canvas-collections/). Questions and suggestions welcome, here on the Collections' site.

## How do you use it?

Collections is most useful when [installed institutionally](https://djplaner.github.io/canvas-collections/getting-started/install/institutional/). But you need to be an administrator to do that. That might not be an option for you.

Collections can also be [installed individually](https://djplaner.github.io/canvas-collections/getting-started/install/individual/). Most useful for teachers/designers of Canvas course sites, or people just wanting to experiment with Collections. Individual installation has two steps: 1. Install the [Tampermonkey browser extension](https://tampermonkey.net/) 2. Install the [Canvas Collections userscript](https://github.com/djplaner/canvas-collections/raw/main/dist/canvas-collections.user.js).

Once installed, you can: 1. [Check it is installed](https://djplaner.github.io/canvas-collections/getting-started/install/is-it-installed/). 2. [Configure Collections](https://djplaner.github.io/canvas-collections/configure/overview/) for your course. 3. [Navigate your course](https://djplaner.github.io/canvas-collections/navigate/navigate-options/) using Collections.

## What can you do with it?

### Start with vanilla Canvas modules

The following image is an example (vanilla) Canvas modules index page. Showing the standard linear structure with a visually limited interface and little contextual information visible.

From what you see here, can you identify the three driving questions behind the design of this course?[![Scrolling through a Canvas modules index page. Showing 13 modules and all their items in one long linear scroll. Each module visualised with a 'windows-95' like folder with a list of items.](images/vanillaModules.gif)](https://github.com/djplaner/canvas-collections/raw/main/docs/assets/vanillaModules.gif)

### Add live (dynamic) Canvas Collections

The following image is the same course. However, the Canvas Collections code is live and is dynamically modifying the Canvas modules index page to add

- Structure - modules have been allocated to four _collections_ with only the modules belonging to the currently selected collection visible at any one time.
- Visuals - each collection is using a different _representation_ (and also including content from a Canvas page) which allows direct navigation to a module.
- Context - additional contextual data (e.g. description, banner image/iframe, date etc.) is visible for each module. (What isn't shown is that this data can include [requirements completion](https://djplaner.github.io/canvas-collections/reference/conceptual-model/representations/griffith-cards/#progress-ring))

Can you identify the three driving questions behind the design of this course from this view?[![Canvas modules page configured with four collections (why, what, how, and questions & suggestions). Changing between different collections, showing only that collection's modules at any one time. Navigating directly to a module by clicking on its specific representation. Showing off the representations which include cards for each module. Cards with images/iframes, descriptions, dates, labels and other contextual data](images/withCanvasCollections.gif)](https://github.com/djplaner/canvas-collections/blob/main/docs/assets/withCanvasCollections.gif)

### Create a Claytons (static) Canvas Collections page

Live Collections requires installing the Canvas Collections code (institutionally or individually). If installed individually, then you probably can't use live Collections with students (each student would have to install Collections individually).

As an alternative, you can use your individual installation of Collections to create a Canvas page that contains a static ([Claytons](https://australianfoodtimeline.com.au/claytons-enters-australian-vernacular/)) version of Canvas Collections. Echoing the common Canvas community practice of creating a visual home page for a Canvas course. The difference being that Collections does the design work for you.

The following demonstrates a Claytons Collections version of the live Collections above. Same (similar) collections, representations, and contextual data. However, all saved onto a Canvas page that is being used as the course home page.

(NOTE: Due to [limitations of the Canvas RCE](https://community.canvaslms.com/t5/Canvas-Resource-Documents/Canvas-HTML-Editor-Allowlist/ta-p/387066) at least one of the current representations shown does require external CSS to work.)[![Animation showing how a Canvas page has been updated to contain a sequence of tabs for each collection. Allowing the visitor to see different representations of Canvas modules (but not the modules themselves). Representations that are basically the same as live Canvas Collections. Clicking on the representation for a module will take you directly to that module.](images/claytonsCollections.gif)](https://github.com/djplaner/canvas-collections/blob/main/docs/assets/claytonsCollections.gif) 

### Modify Canvas Collections

Canvas Collections is explicitly designed to be [generative](https://djplaner.github.io/canvas-collections/#generativity). That is, to improve the capacity of the community ["to produce unprompted change driven by large, varied, and uncoordinated audiences"](https://en.wikipedia.org/wiki/Generative_systems). By making it simpler (though perhaps not simple) for others to make changes. [The rationale](https://djplaner.github.io/canvas-collections/about/rationale/) behind Canvas Collections is that generativity is a key enabler for providing [usable short arc design tools that scale](https://djplaner.github.io/canvas-collections/about/rationale/#usable-short-arc-design-tools-that-scale)

Some of the means used to achieve this, includes:

1. [Source code distributed](https://github.com/djplaner/canvas-collections) under an [open source licence (GPLv3)](https://github.com/djplaner/canvas-collections/blob/main/LICENSE).
2. Written using [Svelte component framework](https://svelte.dev/)
3. Designed with an architecture that (hopefully) supports generativity.