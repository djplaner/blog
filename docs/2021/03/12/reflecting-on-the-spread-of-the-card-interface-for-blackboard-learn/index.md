---
categories:
- casa
coverImage: 36379213_b65e65ed62_o.jpg
date: 2021-03-12 12:02:59+10:00
next:
  text: What are the symbols in digital education/design for learning?
  url: /blog/2021/03/24/what-are-the-symbols-in-digital-education-design-for-learning/
previous:
  text: Do the little things matter in design for learning?
  url: /blog/2021/03/06/do-the-little-things-matter-in-design-for-learning/
title: Reflecting on the spread of the Card Interface for Blackboard Learn
type: post
template: blog-post.html
---
In late 2018 I started work at an institution using [Blackboard Learn](https://en.wikipedia.org/wiki/Blackboard_Learn). My first project helping "put online" a group of 7 courses highlighted just how ugly Blackboard sites could be and how hard it was to do anything about it. By January 2019 [I shared the solution](/blog/2019/01/30/improving-reuse-of-design-knowledge-in-a-lms/) I'd developed - [the Card Interface](https://github.com/djplaner/Card-Interface-Tweak). Below is a before/after image illustrating how the Card Interface 'tweaks' a standard Blackboard Learn content area into something more visual and contemporary. To do this you add some provided Javascript to the page and then add some card meta data to the other items.

![](images/2021-03-12-05-20-10.png)

Since 2019, the work has since grown in three ways:

1. The addition of [the Content Interface](https://github.com/djplaner/Content-Interface-Tweak) as a way to [design and maintain online content](/blog/2019/02/24/exploring-knowledge-reuse-in-design-for-digital-learning/#problem-developing-and-maintaining-online-learning-content) and refinement of both the Card and Content Interfaces.
2. Conceptually through the [development of some design principles](/blog/2019/08/08/exploring-knowledge-reuse-in-design-for-digital-learning-tweaks-h5p-constructive-templates-and-casa/#initial-design-principles-adr-stage-4) for this type of artefact (dubbed Contextually Appropriate Scaffolding Assemblages - CASA).
3. Uptake of the Card Interface (and to a lesser extent the Content Interface) within my institution and beyond.

## The spread - Card Interface Usage - Jan-March 2021

The following graph illustrates the number of unique Blackboard sites that have requested the Card Interface javascript file in the first few months of 2021. In the same time frame, the Content Interface has been used by a bit over 70 Griffith University sites.

![](images/2021-03-12-05-31-00.png)

The heaviest use is within the institution where this all started. Usage this year is up from the original 7 courses at the same time in 2019. What's surprising about this spread is that this work is not an officially approved technology. It's just a kludgge developed by some guy that works for one of the L&T areas in the institution. Uptake appears to have largely happened through word of mouth.

Adoption beyond the original institution - especially in Ireland - was sparked by [this chance encounter on Twitter](https://twitter.com/djplaner/status/1281688249753165824?ref_src=twsrc%5Etfw") (for the life of me I can't figure out to embed a good visual of this tweet, it used to be easy). Right person, right time. More on that below.

![](images/2021-03-12-11-42-53.png)

## Reflections

So why has it played out this way?

What follows are my current reflections bundled up with the [CASA design princples](/blog/2019/08/08/exploring-knowledge-reuse-in-design-for-digital-learning-tweaks-h5p-constructive-templates-and-casa/#initial-design-principles-adr-stage-4).

Would be interesting (to me at least) to actually ask and find out.

### 1\. A CASA should address a specific _contextual_ need within a specific _activity_

The Card Interface address an unfulfilled need. The default Blackboard Learn interface is ugly and people want it to look better. And there isn't much help coming from elsewhere. The Irish adoption of the Card Interface that this isn't a problem restricted to my institution.

The Content Interface isn't as widely used. I wonder if part of that is because the _activity_ it helps with (design and maintain online content) is diversely interpreted. e.g. People differ on what they think is acceptable/good online content, if/how it should be developed, and thinking about it beyond just getting some "stuff" online for Monday. Meaning a lot more effort is required to see the Content Interface as a solution to a need they have.

### 2\. CASA should be built using and result in _generative technologies_

First, to give Blackboard Learn its due. It is a generative platform. It allows just about anyone to include Javascript. This generative capacity is the enabler for the Card and Content Interfaces and numerous other examples. Sadly, Blackboard have decided generativity is not important for Blackboard Ultra.

Early versions of the Card Interface didn't do much. But over the years its evolved and added features. They've been responding to evolving local needs. Perhaps making it more useful?

I think a key point is that the Card Interface is generative for the designer. It provides some scope for the designer to change how it works. The most obvious example being the easy inclusion of images.

It would be interesting to explore more if and how people have used the Card Interface in different and unexpected ways. Or, have they stuck to the minimum.

The Content Interface can be generative, but requires expert knowledge and isn't quite as easy. What choice is available is not that attractice. I suspect if it were more mearningfully and effective generative that would positively impact adoption.

### 3\. CASA development should be _strategically aligned_ and supported

Neither of these tools are institutionally aligned. They have become fairly widely adopted with the team of educational designers I work with and more of a part of our strategic processes. But not core or genral. There's been some spread beyond into other groups but not at the institutional level. There is talk that the Card Interface has had some level of approval by one of the more central groups. It would be interesting to analyse further.

But these tools remain accepted but not formally recognised.

### 4\. CASA should package appropriate design knowledge to enable (re-)use by teachers and students.

To [paraphrase Stephen Downes](https://www.downes.ca/post/72056) this is where a CASA does things right thereby "allowing designers to focus on the big things". Just the ability to implement a card interface is a good first start, but I also wonder how much some of the more contextual design knowledge built into the Card and Content Interface influence use? e.g. the [university date feature](/blog/2021/03/06/do-the-little-things-matter-in-design-for-learning/) of both.

It would be good to test this hypotheses. Also to find out what impact this has on the designer/teacher and the students.

### 5\. CASA should actively support a _forward-oriented_ approach to design for learning

It appears that [the University date](https://djplaner.github.io/Card-Interface-Tweak/customiseACard/#adding-a-date-or-date-range) feature of the cards is used a fair bit. It's the main "forward-oriented" design features. But there's perhaps not much more of this focus in the Card Interface.

The Content Interface is conceived of as a broader assemblage of technologies to design and mantain online content. It can make use of O365 to enable more collaborative discussion amongst the teaching team and enable version control. But I'm not sure many teachers currently think about a lot more than what they are putting up this study period, or this week.

### 6\. CASA are conceptualised and treated as contextual _assemblages_

i.e. it's not just the LMS or any other technology. It's more about how easily and effectively each teacher is able to integrate these tools into their practices, tools and context.

The Card Interface is a simpler and more generic tool. It's easier to integrate and achieve a positive outcome. Hence great adoption within the institution and beyond.

The Content Interface is itself a more complex collection of technology and also attempting to integrate into a more complex set of practices, tools and context.

It would be very interesting to see if, how, and what assemblages people have constructed around each of these tools.