---
categories:
- elearning
- shadowsystems
date: 2009-06-15 10:40:43+10:00
next:
  text: Institutional e-learning strategies
  url: /blog/2009/06/17/institutional-e-learning-strategies/
previous:
  text: 'PhD Update #14 - Moving to a new day'
  url: /blog/2009/06/14/phd-update-14-moving-to-a-new-day/
title: How silly can enterprise IT get? Tools should fit the people, not the other
  way around
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: VRBones
      author_email: vrbones@hotmail.com
      author_ip: 150.101.181.34
      author_url: http://www.vrbones.com
      content: "<blockquote>There are lots of \u201Clittle things\u201D like this that\
        \ reinforce to users of these systems that the they are having to change to fit\
        \ the tool, not the other way around.</blockquote>\nThe problem is that there\
        \ is no computer program or simulation on earth that can replicate a face-to-face\
        \ conversation with another human being. It is ALWAYS going to be a compromise\
        \ because the optimal solution from a users perspective is simply not possible\
        \ yet. Not only that, but a solution that invests heavily in HCI will be far more\
        \ expensive than one that relies on humans adapting to the way the machine needs\
        \ the data presented. Do you want your slash at twice the price? What about 10\
        \ times the price? At some point everyone needs to pick their comfortable point\
        \ on the price / usability scale. What seems to be the point of contention is\
        \ that enterprise systems make a wholesale choice for you.\n\nThat said, HCI has\
        \ huge <a href=\"http://books.google.com.au/books?id=kDVgsGgkF4cC\" rel=\"nofollow\"\
        >cost benefits</a>, so you can't simply ignore it totally. This is especially\
        \ true in a mature space where UI is increasingly the <a>differentiating factor</a>.\
        \ You can also view the whole web2.0 movement as a user interface enhancement\
        \ over traditional web pages.  Best thing about developing HCI is that you know\
        \ users are never going to go back if you can deliver a superior interface.\n\n\
        Personally I'm fairly intolerant of poor UI too, especially in cases where there\
        \ has been an established intuitive solution like the example above. Maybe I'm\
        \ just riled up about demanding that tools \"should\" fit whereas I'd rather seek\
        \ the tool that is the best fit and use that (even if it involves guerilla tactics\
        \ if inside a corporate structure)."
      date: '2009-06-17 15:31:22'
      date_gmt: '2009-06-17 05:31:22'
      id: '2603'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: davidtjones
      author_email: d.jones@cqu.edu.au
      author_ip: 138.77.2.130
      author_url: https://djon.es/blog/
      content: 'G''day Tony,
    
    
        For me it''s more than just HCI.  However, I think you get close to my problem
        with current practice with the first part of your comments.
    
    
        <blockquote>The problem is that there is no computer program or simulation on
        earth that can replicate a face-to-face conversation with another human being.
        It is ALWAYS going to be a compromise because the optimal solution from a users
        perspective is simply not possible yet.</blockquote>
    
    
        The problem I have with most information technology is the assumption that you
        can develop a solution before folk have used it, implement it and then leave it.
    
    
        For me, enterprise IT has to, as much as possible, attempt to be as much like
        a conversation as possible.  i.e. Enterprise IT has to be listening to what people
        are saying and to be clearly and transparently seen to be changing and improving
        what it does in response to that conversation.
    
    
        Sure, you will never get a perfect solution. You can''t do everything all the
        time.
    
    
        However, the model at the moment is to actively ignore people and be seen to not
        respond.  Which is just broken. IMHO
    
    
        David.'
      date: '2009-06-18 14:00:49'
      date_gmt: '2009-06-18 04:00:49'
      id: '2604'
      parent: '2603'
      type: comment
      user_id: '1'
    
pingbacks:
    - approved: '1'
      author: Gaps, shadow systems and the VLE/LMS &laquo; The Weblog of (a) David Jones
      author_email: null
      author_ip: 66.135.48.204
      author_url: https://djon.es/blog/2009/07/31/gaps-shadow-systems-and-the-vlelms/
      content: '[...] with is the lack of fit between enterprise systems and what people
        want to do with them. I&#8217;ve blogged about this with enterprise systems, learned
        to live and thrive in spite of that gap and drawn some lessons from it for enterprise
        [...]'
      date: '2009-07-31 11:51:32'
      date_gmt: '2009-07-31 01:51:32'
      id: '2605'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
I have a thing against large scale enterprise information systems (such as ERP systems like Peoplesoft or learning management systems - commercial or open source) and how they are generally implemented within organisations. This morning provides a wonderful example of why.

An organisation I'm aware of has, like many others, a human resources system that maintains information about staff. In the last couple of years it's gotten really modern and added a web interface to it so that staff can change and view their details.

The example of the constraints of such systems and the limitations of how they are implemented in organisations is highlighted by an email today from the HR folk. It reminds staff how to keep their details up to date and includes some instructions on how to enter the data correctly.

Apparently, the system doesn't like the use of characters such as "/" or "-" in address fields. As in

> 5/105 Fred Street

So the advice is to use a space instead of either offending character. i.e. the usage that would break the system

> 5/105 Fred Street

should become

> 5 105 Fred Street

i.e. a space instead of the "/".

### Tools should fit the people, not the other way around

Dave Snowden gave a keynote, [which he described here](http://www.cognitive-edge.com/blogs/dave/2009/04/kmrc_conference_blog_snowden.php) and uses the following quote which I've [used before](/blog/2009/04/06/quotes-from-snowden-and-the-mismatch-between-what-univeristy-e-learning-does-and-what-it-needs/)

> Technology is a tool and like all tools it should fit your hand when you pick it up, you shouldn’t have to bio-re-engineer your hand to fit the tool.

This is a prime example of how enterprise systems in organisations and how they are implemented generally don't deliver this. How they expect people to "bio-re-engineer" what they do to fit the technology, rather than the other way around. The above advice requires people to change how they write an address to fit the limitations or a poorly designed system.

Not to mention that they expect you to remember to do this from some out of context advice. I'm sure folk will remember this advice in 3 months when they move. At the very least the web page that takes the address should/could have some validation that complains about the use of "-" or "/" and provides some in-context advice on how to fix it.

Better yet, the validation should automatically change it before submitting the data and/or the server-side code that updates the database should sanity check and correct this limitation.

The tool should fit the practice of the human beings. Not the other way around.

### So what?

I can here some folk responsible for enterprise systems asking "So what? It's only a small thing people have to remember on the odd occasion they change address. No big thing. Much harder to change the system. Cost/benefit isn't there.". What these folk forget is that this problem is symptomatic of all enterprise information systems. There are lots of "little things" like this that reinforce to users of these systems that the they are having to change to fit the tool, not the other way around.

It's the IT folk, or at least their reputation, suffering death by a thousand cuts as all of these "small things" build up and create a general impression that IT don't care about users and are more interested in their systems and keeping costs down. That the users have to carry the burden. The type of build up that can't be solved by employing public relations folk and forums to "communicate" with the users. You have to walk the walk, not just talk the talk.

Let's not forget the detail of this example. Entry of an address!!! It's not rocket science. It's not something that's just been developed in the last six months. Computer systems have been doing address entry for decades. How can a system not handle this!!!

What sort of message do you think this sends to the users?

All this reminded me of the song [From Little Things Big Things Grow](http://en.wikipedia.org/wiki/From_Little_Things_Big_Things_Grow)

\[youtube=http://www.youtube.com/watch?v=\_tHEGo-g3mw\]

### Organisational fit and success

Yesterday, as part of my thesis travels, I came across [this paper](http://www.editlib.org/p/22846) (Hogarth and Dawson, 2008) that reminded me of the work around organisational fit and the use of configuration theory to explain/understand the success or failure of change through the application of information technology. This discussion seems tightly linked with this example.

Here's some background from Hogarth and Dawson (2008)

> The notion of configurational fit is based on a theory described in the OS literature (Miles & Snow, 1984), and encapsulates the extent to which the multivariate components of organisational life, such as strategy, structure, management processes, and technology, function in-tune with each other (Sauer, Southon, & Dampney, 1997). In the case of IT innovations, organisational fit is attained when the innovation functions in a way that is consistent with the way the organisation functions, and is managed in the way the organisation is managed.

So what happens if the IT innovation has a weak organisational fit? Hogarth and Dawson (2008) again

> In configuration theory, weak fit is the underlying condition that promotes the existence of risk-related behaviours in organisations......Sauer et al. (p. 350) referred to the outcomes of these risk factors as failure modes, which can commonly include process failures (cost and schedule overruns) and interaction failure (non-use of the innovation).

i.e. if there is perceived to be poor fit, the users start to work around the system in ways that will increase the likelihood of system failure. Where system failure has a variety of outcomes.

### References

Hogarth, K. and D. Dawson (2008). "Implementing e-learning in organisations: What e-learning research can learn from instructional technology (IT) and organisational studies (OS) innovation studies." International Journal on E-Learning 7(1): 87-105.