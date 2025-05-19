---
categories:
- bam
date: 2009-07-09 15:14:35+10:00
next:
  text: BAM and the Chinese "firewall"
  url: /blog/2009/07/15/bam-and-the-chinese-firewall/
previous:
  text: Academics - the next part of the People section
  url: /blog/2009/07/07/academics-the-next-part-of-the-people-section/
title: Integrating BAM into Moodle - Can it be done?
type: post
template: blog-post.html
---
[Blog Aggregation Management](/blog/research/bam-blog-aggregation-management/) (BAM) is a little project of mine that's been going since 2006. It's an example of, what I think, is a more appropriate product model for e-learning systems - essentially [small pieces loosely joined](http://www.smallpieces.com/)/best of breed/PLE. Currently BAM is based on the infrastructure provided by [Webfuse](/blog/2009/02/15/alternatives-for-the-institutional-implementation-of-e-learning-lessons-from-13-years-of-webfuse/), another project of mine (which embodies and enables the better product model).

Trouble is that come 2010 Webfuse is history as my current institution cans Webfuse in favour of Moodle. There are about 5 or 6 courses at that institution that currently use BAM and many more that could probably use it. So, if there is to be a future for BAM it will have to be ported to [Moodle](http://www.moodle.org/). This is the first step in checking to see if this can be done. It will be subsequently be followed by whether or not it should be done and whether it will be done.

The following isn't a real blog post. It's more a unstructured collection of ad hoc, formative reflections as I confuse myself diving through the Moodle world as a ill-informed newbie.

### How do you find out developing something for Moodle?

Each system embodies a way of looking at the world, a set of terms and concepts. Essentially I need to get some sort of insight into its structure, language and world view. From there I can make some vaguely informed decision as to whether the BAM worldview has any hope of living nicely with the Moodle world-view. I need some resources.

Well, the [Moodle site](http://www.moodle.org/) has [this pointer](http://moodle.org/development/) towards development resources. Of course, there's also the constructivist approach recommended by [Dan Poltawski](http://blog.danpoltawski.co.uk/archives/2009-05-Secrets-of-Learning-Moodle-Development!.html). There's a lot to be said for that approach, but it's a little heavyweight for my current requirements.

What other stuff is there on the Moodle main site?

- FAQS! There's a [FAQ for development](http://docs.moodle.org/en/Development:Developer_FAQ).  
    But most of that seems to be low level code related stuff. I'm looking for a bigger picture.
- There are some pointers to information about creating new modules or plugins. - apparently there are 22 different types of plugins.
    - [Make a new plugin](http://docs.moodle.org/en/Development:Developer_documentation#Make_a_new_plugin)
- [the manuals](http://docs.moodle.org/en/Moodle_manuals)
- [The coding guide](http://docs.moodle.org/en/Coding)

The following list of resources is something I'll probably have to come back to at a later date when/if coding commences.

- [Working with the community](http://docs.moodle.org/en/Development:Working_with_the_Community)
- The [database abstraction layer](http://docs.moodle.org/en/Development:XMLDB_Documentation)
- the [roles system](http://docs.moodle.org/en/Development:Roles)
- the [forms library](http://docs.moodle.org/en/Development:lib/formslib.php)
- the [file API](http://docs.moodle.org/en/Development:Using_the_file_API)

### Absence of definitions or an overview

I'm about 4 or 5 hours into my examination of Moodle and whether BAM might go into it. The biggest problem I have is that I haven't been able to find an overview. Something that defines terms such as blocks, activity modules etc and shows how they all link together.

All of the developer docs like "how to develop a block" just leap straight into answering the question. None seem to offer a description or pointer to a description of what a block is and how it compares to other components.

This [set of powerpoint slides](http://lyceum.open.ac.uk/temp/creating_moodle_modules.ppt) (by Sam Marshall) on creating Moodle modules seems to be the best so far.

Perhaps this [Moodle Programming course](http://dev.moodle.org/course/view.php?id=2) might help fill the hole.

### Nature of modules

Each module has it's own directory. Will include a list of files, directories for specific purposes.

Each module can specify capabilities - who can do what?

### Existing work

As others have pointed out, Moodle already has blogs and there is also a [project](http://docs.moodle.org/en/Student_projects/Blog_improvements) currently looking at improving the Moodle blog component. Actually, that's a 2008 project. The [project blog](http://moodle.org/blog/index.php?userid=27192) just seems to peter out - no final "it's done" post. However, [according to this](http://docs.moodle.org/en/GSOC/2008#Blog_improvements_and_the_addition_of_a_blog_assignment_module) it completed successfully and contributed code which is available as [patches](http://tracker.moodle.org/browse/MDL-15435) and may also be merged into Moodle 2.0

Looking into that project brings me to [a thread on the Moodle site](http://moodle.org/mod/forum/discuss.php?d=44830) (you may have to login to see the thread) about the blog component. It starts off with a post from [Martin Dougiamass](http://moodle.org/user/view.php?id=1&course=5) explaining some of the initial rationale.

That post reinforces the point that there is a strong model underpinning Moodle and how it should work that drives the design decisions. At least on an initial read, the aim of Blogs in Moodle was to provide a blog like facility that fit within the Moodle model. The idea of integrating BAM into Moodle comes from a different perspective and there might be some interesting clashes of perspective/assumptions.

An assumption behind BAM is that you actually want the students to be posting their comments on the open web, to enable some of the serendipity related fun to happen. Moodle appears to be based on an assumption of a much tighter integration.

### What type of plugin?

If implemented, I'm assuming BAM will be some kind of plugin and one of those [listed here](http://docs.moodle.org/en/Development:Developer_documentation#Make_a_new_plugin). In the following, I'm documenting my investigations about which type BAM might be.

From the initial list, without looking forward, I'm guessing that BAM might be or be related to one of the following:

- Activity module
- Assignment type  
    This looks potentially interesting/related. BAM is mostly used at the moment as an assignment. So it's inclusion here probably fits current operation. However, currently BAM is separated from the assignment stuff which allows a bit more flexibility....mmm. There are examples of [non standard assignment types](http://docs.moodle.org/en/Non-standard_assignment_types). Which are some sort of plugin to the existing assignment component.
- Gradebook or Portfolio plugins

### What's next?

Well, I should perhaps follow the [published guidelines](http://docs.moodle.org/en/Development:Overview#Major_Development). Completing the first step - make sure it's a good idea - is first. I'll need to

- Check to see if the blog improvements offer something close to BAM.
- Dig around a bit more in Moodle to see if BAM can be implemented.
- Ask a question on the forums.