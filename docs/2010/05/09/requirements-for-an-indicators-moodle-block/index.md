---
title: Requirements for an &quot;indicators&quot; Moodle block
date: 2010-05-09 14:18:26+10:00
categories: ['elearning', 'herding-cats', 'indicators']
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: Mark Pearson
      author_email: markp@earlham.edu
      author_ip: 159.28.7.95
      author_url: http://markpea.wordpress.com/
      content: '''Indicators'' sounds like a really great idea. In terms of visualization
        tools I''d suggest taking a look at Visifire : http://visifire.com/ which looks
        like it''s a very powerful javascript based charting package which will work with
        php.
    
    
        The question I''d be asking up front is "what do Teachers really need out of Moodle
        that they''re not getting right now?" I''d suggest that one answer might be ''keep
        track of students who are falling behind''. Wouldn''t it be great to have a block
        located on your MyMoodle page that polled all your courses and raised warnings
        and alerts on those students who seem to be falling behind. Then you can decide
        on proactive action to aid student success  rather than remediation to ameliorate
        failure. How this could be implemented and displayed is a matter for the geniuses
        that constructed BIM!
    
        For students the leading question seems to me to be more simple. "What stuff have
        I go coming up and when is it due?". MyMoodle course display tries to address
        this but a timetable format that sucks in details from all courses and delivers
        warnings of important assignments due would be better.
    
        A model of utility + pedagogical power is Michael de Raat''s Progress bar block
        at http://www.sci.usq.edu.au/staff/deraadt/progressBar.html. This is something
        that''s simple to grasp, flexible to configure and powerful beyond it''s humble
        appearance.
    
        It seems to me that MyMoodle is the place to put this and the ''block'' could
        easily be sited in the central section of the MyMoodle display.
    
        Finally, perhaps we should be thinking about how Moodle could be better integrated
        with the ubiquitous technology that 99.9% of students possess and that is cell
        phones (mobiles in euro parlance). Wouldn''t it be great if the student indicator
        block were integrated with SMS so that you could have it send you a text to remind
        you about an essay due tomorrow or a reading for tonight, or an alarm for an exam,
        etc? Moreover, why faff about with expensive ''clickers'' when everyone has cell
        phones, and texting is ubiquitous? The possibilities here for class use of Moodle
        are enormous!'
      date: '2010-05-11 01:17:03'
      date_gmt: '2010-05-10 15:17:03'
      id: '3028'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: davidtjones
      author_email: d.jones@cqu.edu.au
      author_ip: 138.77.2.133
      author_url: https://djon.es/blog/
      content: 'Mark, thanks for the comments and the pointers.  A quick response with
        some additional information.
    
    
        Visifire looks good, though the Microsoft emphasis makes me somewhat leery.  But
        the idea is there, this stuff needs to look great and provide significant functionality.
    
    
        Thanks also for the pointer to the progress bar.  We need to look at this and
        probably follow up with Michael, I think he''s going to Moodlemoot AU 2010, so
        maybe there.
    
    
        You''re question about "what do teachers really need" is an important consideration,
        but I''m also being driven by a bit more than just what they need.   Increasingly,
        my interest is in modifying the system within which the teachers are operating
        in ways that encourage and enable them to improve their practice.
    
    
        I''ve expressed parts of this before (<a href="https://djon.es/blog/2010/02/03/loosing-weight-nudging-and-changing-the-lt-environment-early-foundations-of-my-work/"
        rel="nofollow">losing weight, nudging and change</a>) and recently I''m increasingly
        interested in some insights from distributed cognition and perhaps distributed
        leadership (more on this later).
    
    
        But much of this relates to your example, modify the Moodle environment so that
        it makes academics aware of what is going on and are actively encouraged and enabled
        by the environment to do the right thing about it.'
      date: '2010-05-11 09:32:01'
      date_gmt: '2010-05-10 23:32:01'
      id: '3029'
      parent: '3028'
      type: comment
      user_id: '1'
    - approved: '1'
      author: markdrechsler
      author_email: mark.drechsler@internode.on.net
      author_ip: 203.30.161.239
      author_url: null
      content: 'Hey David,
    
    
        This sounds great, and I look forward to seeing more of it whether it be at the
        Moot or elsewhere.
    
    
        I''ll throw in a comment about your point on "getting a large bunch of data and
        doing some calculations" and the impact that might have on performance.
    
    
        One of the things our Dev team have found with some third party blocks/plugins
        is a lack of forethought of how a piece of code will impact the environment, so
        its great that you''ve got this on your ''to do'' list.
    
    
        Couple of thoughts spring to mind.
    
    
        Firstly, one of the standard architectural components we (as in the NetSpot we)
        include is a separate (virtual) utility server to run Moodle''s CRON job tasks
        without having an impact on the transactional performance for users. If there''s
        data crunching to be done then I''d strongly suggest that this block runs it as
        part of the CRON job on this separate server and then just needs to retrieve the
        specific individual data on the fly rather than calculating the whole thing in
        real time.
    
    
        Secondly, and I almost feel like stabbing myself through the hands with a fork
        as I type this based on the last data warehouse project I was involved in, I wonder
        if setting up a separate data warehouse environment for this Moodle data would
        be a good thing. It would be a non-trivial job to set up something like http://bit.ly/cJVsof
        on a separate server, set up the ETL processes as part of the CRON, define the
        cube structures and then work out a way to pull the pre-calculated data from the
        cubes back into the Moodle block, but you''d also end up with a massive amount
        more potential for ad-hoc queries on Moodle''s data without having any performance
        overhead to Moodle itself - something I''ve been dreaming about for a long time
        but never had the opportunity to look at. Of course it would also restrict the
        block''s shareability with the community, would need careful design to minimise
        the impact of upgrades to Moodle''s data structure, and it would be a hell of
        a lot more work, so perhaps I am just over-engineering a solution - maybe its
        the ancient German blood in me coming out or something.
    
    
        Anyway, just thought I''d chuck the ideas down, feel free to disregard if they
        sound like rubbish :)'
      date: '2010-05-13 10:15:14'
      date_gmt: '2010-05-13 00:15:14'
      id: '3030'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: davidtjones
      author_email: d.jones@cqu.edu.au
      author_ip: 138.77.2.133
      author_url: https://djon.es/blog/
      content: 'G''day Mark,
    
    
        Thanks for taking the time to comment.
    
    
        In terms of thinking about impact, I have to admit that my experience with BIM
        and interacting with some of the guys at Netspot has reminded me how important
        this is.  One of the initial aims of the indicators block work is simply to upgrade
        the skills/knowledge that project members have of Moodle development. A half-baked
        idea in my head was that the "processing" of large amounts of data would be done
        by cron, I believe I understand how to do that, but the question of a separate
        server, that''s new.
    
    
        My initial assumption would be that this is something that can be configured in
        Moodle.  i.e. if we follow the Moodle cron process properly, folk hosting should
        be able to configure it to run on separate servers, correct?  We''ll find that
        out as things go.
    
    
        Ahh, data warehouses. We come to one of the interesting aspects of the project,
        both politically and theoretically. I don''t speak for all of the folk in the
        indicators project, but I have <a href="https://djon.es/blog/2010/01/27/some-reasons-why-business-intelligence-tools-arent-the-right-fit/"
        rel="nofollow">argued</a> that I think data warehouses are not the full story.  I
        certainly think there is some value in data warehouses, however, I''m somewhat
        skeptical of whether the value exceeds the cost (sometimes).  More importantly,
        I don''t think data warehouses are the right fit for what I''m interested in,
        improving the quality of the majority of learning and teaching through the idea
        of <a href="https://djon.es/blog/2010/03/25/from-theory-to-intervention-mapping-theoretically-derived-behavioural-determinants-to-behaviour-change-techniques/"
        rel="nofollow">behaviour change</a>.
    
    
        A small part of this is that I don''t think the majority of teachers are going
        to make use of the types of query you can generate through a data warehouse.  They
        don''t have the knowledge, interest or time to do it.  But, I think/believe that
        if you can package the information into an appropriate form so that it is integrated
        into what teachers are doing, you might be able to improve L&amp;T.
    
    
        It''s not as simple as that. But that''s my interest.
    
    
        Actually, must have a chat about your data warehouse project when we meet in Melbourne.
    
    
        David.'
      date: '2010-05-13 10:41:15'
      date_gmt: '2010-05-13 00:41:15'
      id: '3031'
      parent: '3030'
      type: comment
      user_id: '1'
    - approved: '1'
      author: markdrechsler
      author_email: mark.drechsler@internode.on.net
      author_ip: 203.30.161.239
      author_url: null
      content: 'Hey David,
    
    
        Regarding whether or not the CRON job will shoulder the load (I think) will depend
        on how much crunching needs to be done to calculate the required aggregated fields
        to use in the block later, how they are stored in the database and probably a
        stack of other stuff - I''d suggest getting in Ashley Holman''s ear at the Moot
        about it - he''s good with this sort of thing.
    
    
        As for the DW, yep, I agree with you - most of the time it is very arguable as
        to whether the effort outweighs the benefit, hence my comment about the forks-through-hands.
        My last (and only) experience was in the SA Education Department, topically enough
        relating to the NAPLAN test back in 2003. How time flies. I do still wonder if
        a star schema based data model for Moodle could be set up which would be generic
        enough to be of use to anyone, but that is another discussion entirely!
    
    
        Keep up the great work and genuine thought about this stuff, its appreciated.
    
    
        Mark.'
      date: '2010-05-13 11:27:24'
      date_gmt: '2010-05-13 01:27:24'
      id: '3033'
      parent: '0'
      type: comment
      user_id: '0'
    
pingbacks:
    - approved: '1'
      author: Getting started with Col&#8217;s indicators block &laquo; The Weblog of
        (a) David Jones
      author_email: null
      author_ip: 74.200.247.227
      author_url: https://djon.es/blog/2010/05/13/getting-started-with-cols-indicators-block/
      content: '[...] started with Col&#8217;s indicators&nbsp;block  Col has been playing
        around with some ideas for a Moodle indicators block. This is a record of my first
        attempt to install and play with the block. Might also do a bit of [...]'
      date: '2010-05-13 11:04:38'
      date_gmt: '2010-05-13 01:04:38'
      id: '3032'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: 'Understanding what teachers do: First step in improving L&amp;T &laquo;
        The Weblog of (a) David Jones'
      author_email: null
      author_ip: 72.233.96.138
      author_url: https://djon.es/blog/2010/05/25/understanding-what-teachers-do-first-step-in-improving-lt/
      content: '[...] and learning. Much of what I do (e.g. Moodle curriculum mapping,
        the broader alignment project, and the indicators Moodle block) is aimed at modifying
        the environment/network around teaching staff to enable and encourage them [...]'
      date: '2010-05-25 10:17:09'
      date_gmt: '2010-05-25 00:17:09'
      id: '3034'
      parent: '0'
      type: pingback
      user_id: '0'
    
---

See also: [[blog-home | Home]]

The [Indicators project team](http://indicatorsproject.wordpress.com/) are off to [Moodlemoot AU 2010](http://moodlemoot.org.au/). All three are giving presentations, but only two (i.e. not me) are on the indicators project. In thinking about how we might make the most of this opportunity, we've floated the idea of announcing an "indicators" Moodle block at the conference. This post is an attempt to make concrete our thinking and take some steps towards making it happen, hopefully even generate some interest and external comments.

### What is an "indicators" Moodle block?

At least for me, at the moment, an "indicators" Moodle block is a simple extension to Moodle that just about anyone can install into their Moodle install and start getting some insights into whether or not what they (teaching staff, students or administrators) are doing is good, bad or indifferent.

Such a block would probably fulfill some/all of the following:

- Can be embedded into a normal Moodle view.  
    As a teaching staff member, or a student, the block would be part of my normal Moodle interface. It's not located somewhere special that I have to remember to visit, it's always there.
- Is very visual.  
    It sends a strong, very clear message. I don't have to apply special knowledge or spend a lot of time trying to understand what it is telling me. If I'm doing something wrong, it should be red or something similar.
    
    This does **NOT** mean that is obtrusive. As a part of a normal Moodle view it can take my attention away from other stuff.
    
- Enables comparisons.  
    It doesn't tell me how many times I've posted to the discussion forum, it tells me how much less (or more) I've posted than the best students, or all the students, or the worst students. In a friendly way it helps me understand how my use of the LMS compares to that of others.
- Only uses what data is already in Moodle.  
    The aim is for anyone with a Moodle install to be able to add this block and use if straight away. No need to modify/connect with external data sources (at least not yet).
- Serves as a stepping stone to more functionality.  
    The first block is our foray into providing such a service. Over time we might add more functionality. The block has to be a good open source project, something others can add to.
    
    Also, the block has to allow the use to provide more than just visualise the data. It should help them to plan actions they might take, to talk to others about this, to track history etc.
    

### Other tasks

Apart from thinking about what it actually is, we also need to think about what we need to do to start implementation. Here's my first list.

- Identify some visualisation software.  
    Most of these will be graphs or perhaps networks. We need to find a way to generate these graphs/network diagrams from PHP and in a way we can include in a Moodle block.
- Figure out the Moodle database structure.  
    Whatever we do we'll be pulling data from Moodle. So need to find out the format for the bit we're interested in.
- Data caching?  
    Most of these examples are likely to require getting a large bunch of data and doing some calculations before generate the visualisation. The block can't be a performance hog, so we're going to have to figure out some way to minimise performance impact. Caching?
- Moodle block programming.  
    Have done a little, there's a bit of doco out there. So shouldn't be too hard.
- Managing the code.  
    We haven't done any joint development yet. Doing something like this would require us to figure out how we manage the development process.
- Who does what?