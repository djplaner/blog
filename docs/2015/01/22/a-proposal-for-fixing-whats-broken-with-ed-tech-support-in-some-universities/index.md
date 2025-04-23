---
title: "A proposal for fixing what&#039;s broken with ed tech support in some universities"
date: 2015-01-22 11:57:49+10:00
categories: ['academicdevelopment', 'bad', 'elearning']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

[This paper](/blog2/2015/01/06/tpack-as-shared-practice-toward-a-research-agenda/) analyses the outcomes of what a small group of academics (myself included) attempted to do to develop the knowledge/capability to develop effective learning for hundreds of pre-service teachers via e-learning. That experience is analysed using a distributive view of knowledge and learning and illustrates just how broken what passes for ed tech support/academic staff development in some universities. Picking up on [yesterday's post](/blog2/2015/01/21/perceived-usefulness-is-the-most-influential-factor-on-intention-and-actual-use/), the paper reports on academics harnessing their digital fluency to address the almost complete lack of usefulness of the institutionally developed attempts at supporting academic staff in developing the knowledge necessary for effective e-learning.

The distributive view of knowledge and learning used [in the paper](/blog2/2015/01/06/tpack-as-shared-practice-toward-a-research-agenda/) drew on three conceptual themes from Putnam and Borko (2000) and one theme we've added. Those themes suggests that knowledge and learning is/should be

1. situated; Context matters. An inappropriate context can limit transfer of learning into different contexts. The entire system/context in which learning takes place is fundamental to what is learned.
2. social; How we think and what we know arises from on-going interactions with groups of people of time.
3. distributed; and, The knowledge required to perform a task does not exist solely within an individual person or even groups of people. It also resides in artifacts. Appropriate tools can enhance, transform and distribute cognition and expand "a system's capacity for innovation and invention" (Putnam & Borko, 2000, p. 10).
4. protean. The computer is “the first metamedium, and as such has degrees of freedom and expression never before encountered” (Kay, 1984, p. 59) it has a "protean nature". i.e. digital technology can be flexible and should be open to be manipulated in response to needs.

This post is an attempt to propose one way in which institutional attempts at ed tech support could be transformed to actually support these four themes. i.e. to actually be made useful and appropriate for the task.

## Analysing existing practice

When I first started on this post the plan was to analyse my existing institution's attempts at ed tech support. So I logged into the Moodle site for the course I'll be teaching next semester and asked the question, "If I had problem with X (whatever that is), how would I find an answer?". The answer to that question was summarised in [this post](/blog2/2014/12/31/an-illustration-of-the-difficulty-of-learning-about-network-learning/). A post that is password protected because of the embarrassing difficulty I had in answering that question.

Using the four themes the following criticisms might be made

1. situated; The support resources were not situated in the context. I could not find any help with the course site from within the course site. I had to go to another website and waste time figuring out which labyrinth of links I would follow to get to the support resources. The first time I tried it I failed.
    
    I just wanted to check some aspect of my earlier analysis. Initially I had difficulties finding my way through the labyrinth.
2. social; Almost the entire support resources were centrally produced and approved. Some with heavy production values. Pure information distribution. There was a small collection of Moodle discussion forums intended I imagine to encourage social interaction. Half of those forums had no posts, the other half had single posts all from the same author.
    
    Apart from the discussion forums, the only way to add to these resources was via the small number of people from central support.
    
    This also means that the "message" shared via these resources can be controlled by the institution. Raising the question about whether differing views can be expressed. For example, there is a section on using the Mahara e-portfolio that extols the educational virtues of Mahara. There's no way I can contribute the reasons I don't use Mahara and use something different. The point isn't that Mahara is a bad tool, but that there are some issues with using it and alternatives. More importantly, there's no way to share this alternate view.
3. distributed; and Any content to be added to the site had to be manually added by a small select group of people. There was no integration between the resources and other systems. For example, the IT Help Desk system was in no way integrated. So if there was a known problem with the "discussion forums" being raised through the IT help desk, there was no way for that information to appear in the support resources on "discussion forums".
4. protean. The support resources were implemented in an ad hoc collection of Moodle-based course sites. The resources were all static and professionally designed. Little or no way to repurpose those resources or to add to them.
    
    Moodle discussion forums can generate RSS feeds and also have the option of subscribing to a forum via email. These are methods that allow a user to modify how they interact with the discussion forum. If I'm interested in a forum I can integrate new activity on the forum into my daily routine either through my feed reader or email.
    
    The ability to grab the RSS feed or subscribe via email to the discussion forums in these support resources are not visible via the interface that has been used.

## Some design principles

Beyond critiquing what exists, the four conceptual themes above might also be useful in terms of developing guidelines for what might be. Here's an initial brainstorm of potential guidelines. Feel free to add and argue.

1. The support resources should be situated within the context of the academics. Some of what this might suggests includes
    - If you want to learn about using the discussion forums better, you should be able to do this from within the discussion forum.
    - If you want to know how to use the discussion forum for a introductory/warm up activity at the start of semester, this should be possible.
    - The support you receive should be tailored(able) to the type of course or discipline you are teaching.
    - The support system should know who you are, what you're teaching, what you've done before, what groups you belong to, what time of semester (e.g. before semester starts, first couple of weeks, assessment due, end of semester etc) it is etc.
    - The support system should use the tools that people use (not the institution). i.e. not this from Dutton
        
        > Organizations aren’t thinking about the ‘networked individual’ – the networking choices and patterns of individual Internet users. They’re still focused on their own organizational information systems and traditional institutional networks.
        
2. The support area should encourage/enable participation in various discourse communities. Which might suggest approaches such as
    
    - The system should make you aware of the communities/individuals that are using the tool you are currently (thinking of) using. e.g. if you're looking at using the [BIM Moodle module](http://bit.ly/bambim) the support system should help you become aware of who else has used the tool and perhaps how (leading into..)
    - The system should help capture and make available for on-going use the ["residue of experience"](/blog2/2014/08/15/joining-the-swarm-what-a-course-might-be/) (Riel & Pollin, 2004) of other members of the community. The discussion, reflections and analysis of prior use of tools and methods should be available. At a simple level, this might be ensuring that any and all questions about the discussion forum (including those from the helpdesk) be visible/searchable from the support site about the discussion forum.
    
3. The support area should integrate with and integrate into it all of the appropriate organisational and external systems and processes. This might include such things as
    - Knowledge from other systems offering support appear automatically. For example, any [known issues](http://www.vle.monash.edu/knownissues.html) information about tools are integrated appropriately into the environment.
    - Organisational information sources such as student records systems, teaching responsibilities databases, results of course evaluation surveys etc should be integrated into the support and used to situate and modify resources appropriately.
    - Knowledge from the support area should be openly available (as appropriate) for integration into other systems. Might be as simple as generating an RSS/OPML feed (or two) or allowing email subscription. Perhaps publish an API.
    - The "how to do" advice in the support area should actually help you do it. i.e. rather than a sequence of steps describing what you do, there's actually a link that will take you back to actual system and help you do it. Linked to the idea of [Context Appropriate Scaffolding Assemblages (CASA)](/blog2/2015/01/13/this-year-its-all-about-the-connections/#case).
4. The support area should support manipulation and change by the users and their actions (protean). This might mean
    - Something as simple as having decent customisation options.
    - Something more radical like [Smallest Federated Wiki](http://wardcunningham.github.io/). i.e. where each individual or group could fork the support resources and make their own changes. Changes that might be potentially integrated back into the original institutional version.
    

## One illustration

So how might that work in action. Here's one possible illustration.

### Login

You start by logging in to one of the institutional systems (e.g. the LMS).

Straight away I have a qualm about whether or not a login is required. In order for the system to know about you (see the situated principle above) some form of identification is required. But requiring a login means that system isn't open. So perhaps there's an avenue that doesn't require a login.

### The Mini-map appears

Not only do you login to the LMS but you also login to the "support system" and the mini-map appears.

The mini-map is a small icon (or three) that appears in the browser. Perhaps in the top right hand corner of the page. From now on, where ever you go the mini-map is there. But as you move around to different systems it will likely change because it knows your situation and responds accordingly.

This is based on the [mini-maps concept](http://en.wikipedia.org/wiki/Mini-map) from games occuring in immersive 3D worlds. The suggestion isn't that this mini-map be represented as an actual map (though perhaps it might be), the point is that the purpose is to help orient you within the e-learning space.

### What the mini-map might do

Nesbitt et al (2009) suggest that a

> mini-map might also display the position of key landmarks along with the position of the player's avatar and any other relevant actors in the game

which gives some idea of what the "mini-map" in this context might do.

Specific functionality might include

1. You are here. Provide a summary of what it knows about your current location within the teaching and learning environment. This might include insight into the time of term, common or required tasks you may need to complete soon (or have completed at similar times in the past), updates and announcements updating you on what's going on in the environment since you were last here.
    
    e.g. new problems that have arisen around where you are. Such as the lecture capture system being down and that it is being worked upon. This would also suggest that the support system is independent (distributed) from the various services. So it can keep working if they are down.
2. Who else is here. Let you know who else is on this particular page, or who else is using this particular service in another course or at another time. e.g. other people who have used this particular service. Provide some functionality to allow you to control and organise who you want to know about.
3. What have they done Access to the residue of experience, what have these people actually done within your current location. What worked. What didn't. This might also be links to literature etc.
4. How to do stuff. Advice on how to perform various tasks. Pedagogical patterns, learning designs etc including potential CASA's that would help or do stuff for you.

### And on a non-institutional system

The mini-map would appear when you visit any online location that has been used for learning and teaching. For example, if you want to Google Drive you would have access to (almost) the same functionality described above.

If the mini-map didn't appear, because you've visited a tool that no-one else has used before, you could choose to add the tool to the mini-map and that addition would then be visible to others.

### Implementation

I see the mini-map being implemented with something like a [Greasemonkey script](http://en.wikipedia.org/wiki/Greasemonkey). This is how it's possible for it to appear independent of whether you're viewing an institutional or non-institutional system.

It might work something like the following

1. You've installed the Greasemonkey script on your browser.
2. You can choose to enable or disable the script at anytime.
3. Then, whenever you visit a web page the mini-map grabs the URL for that page and sends it to a server.
4. The server checks to see if that URL matches anything supported by the mini-map.
5. The version of the mini-map that is displayed depends on whether the URL is currently supported
    - Supported - then show the full mini-map.
    - Not supported - then show the minimal mini-map with just the option to "add this page"
6. If viewing the supported mini-map you then have access to a range of functionality.
7. Some functionality will pop up new information. e.g. click on the "People" icon and the mini-map might show a list of people you "know" that are/have been here.
8. Some functionality will take you into a different system. e.g. click on one of the people in the list and you might get taken to a web page that shows what they were doing, when, and also provides access to details of what others have done.

The different systems used to provide the various support services should tend to be whatever makes sense but with a focus on being tools people use all the time and not limited to institutional tools. You might use [Slack](http://slack.com/) for some functions. SFW might be good for others.

An interesting and challenging extension to this would be to allow the "mini-map" to be extensible by just about anyone at anytime.

Time for lunch.

## References

Dutton, W. (2010). Networking distributed public expertise: strategies for citizen sourcing advice to government. One of a Series of Occasional Papers in Science and Technology Policy. Retrieved from http://papers.ssrn.com/sol3/papers.cfm?abstract\_id=1767870

Nesbitt, K., Sutton, K., Wilson, J., & Hookham, G. (2009). Improving player spatial abilities for 3D challenges. Proceedings of the Sixth …, 1–3. doi:10.1145/1746050.1746056

Putnam, R., & Borko, H. (2000). What do new views of knowledge and thinking have to say about research on teacher learning? Educational Researcher, 29(1), 4–15. Retrieved from http://www.jstor.org/stable/1176586

Riel, M., & Polin, L. (2004). Online learning communities: Common ground and critical differences in designing technical environments. In S. A. Barab, R. Kling, & J. Gray (Eds.), Designing for Virtual Communities in the Service of Learning (pp. 16–50). Cambridge: Cambridge University Press.