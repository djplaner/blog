---
title: BIM to do list
date: 2009-09-08 15:19:57+10:00
type: page
template: blog-post.html
comments:
    - approved: '1'
      author: Mark Pearson
      author_email: markp@earlham.edu
      author_ip: 159.28.7.95
      author_url: http://markpea.wordpress.com/
      content: 'David,
    
    
        This is fantastic! It means that student blogging can really take off since teachers
        now have the ability to grade and comment on the postings in a private way. I
        did have a few questions though about the design.
    
    
        1. It wasn''t clear to me the extent of student interaction with the BIM activity.
        There''s a screencast about registering your blog, but once the student has done
        that I wasn''t clear what else she had to do. It seems to me that there should
        be somewhere where the student assigns a blog entry to the question.
    
    
        2. It''s also not clear how the marks are accumulated in the gradebook. Are they
        all summed into one grade item per BIM activity?
    
    
        3. Could things be streamlined with the use of tags? For example, tag the blog
        posting corresponding to the BIM assignment #1 with ''week1_assignment''? Or something
        similar. I guess that different blogging systems handle tags differently.
    
    
        Whatever the case with the above, I think that this is an excellent Activity and
        will really help blogging to break into the mainstream Moodlers consciousness.
        The achilles heel of using blogs with a class has always been the issue of marking
        and private comments and this really seems to be a workable solution. Well done!
        I shall be testing it soon with Moodle 1.9.7.'
      date: '2010-02-24 04:32:55'
      date_gmt: '2010-02-23 18:32:55'
      id: '2750'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: davidtjones
      author_email: d.jones@cqu.edu.au
      author_ip: 59.154.24.147
      author_url: https://djon.es/blog/
      content: "G'day Mark,\n\nFirst, glad BIM is useful for others.  Let me know if you\
        \ have any questions or problems, I'm keen to work with folk to make BIM as useful\
        \ as possible.\n\nI'm working on some additional resources that will explain BIM\
        \ in more detail.   Not sure if you've seen them.  Just in case, will point to\
        \ them here and then respond to your questions\n\nThere are screencasts to help\
        \ users perform their tasks\n   http://cddu.cqu.edu.au/index.php/BIM_User_Resources\n\
        which give some idea of how it works.\n\nThere's also a presentation (set of slides)\n\
        \   http://www.slideshare.net/davidj/introducing-bim\nI hope to be making an audio/screencast\
        \ around this presentation available later this week.\n\n<h3>Student interaction</h3>\n\
        \nThe students interaction could be said to be 3 fold\n1. They register their\
        \ blog/feed.\n2. They can view what BIM knows about their feed\n3. What they write\
        \ on their blog is processed by BIM\n\nPart of that processing is BIM's attempt\
        \ at \"automatic allocation'.  i.e. BIM looks at the student post, compares it\
        \ with the list of questions set for the activity and if it finds a match it will\
        \ automatically allocate the post to the question.\n\nThere is no need for a BIM\
        \ activity to have questions, but most do.\n\nCurrently, there's also an interface\
        \ that allows teaching staff to manually allocate the posts if the automatic allocation\
        \ fails.\n\nThe presentation above provides a brief description of how the automatic\
        \ allocation actually works.\n\n<h3>Marks</h3>\n\nIn this first version, which\
        \ is also my first serious Moodle development, I've taken the easy route, at least\
        \ initially.\n\nEach BIM activity will have its own column in the gradebook. \
        \ So, if you have multiple different BIM activities in a single course, you'll\
        \ have multiple different entries in the gradebook.\n\nThe gradebook entry for\
        \ each student for a single BIM activity is simply the sum of all the marks given\
        \ to the posts.  The assumption was that if the teaching staff wish to scale or\
        \ manipulate the grade, they can do that in the gradebook.\n\n<h3>Tags and streamlining</h3>\n\
        \nInitially, tagging was though of.  But, as you point out, there's a bit too\
        \ much variability between blogging engines and the aim was to support as many\
        \ as possible.\n\nThat's why the automatic allocation is currently only done on\
        \ the title and the body of the post.  BIM currently only relies minimally on\
        \ the body.\n\nThis is an area that could be improved. One of the tasks over coming\
        \ weeks and months.\n\nHope this helps.\n\nDavid."
      date: '2010-02-24 06:00:47'
      date_gmt: '2010-02-23 20:00:47'
      id: '2751'
      parent: '2750'
      type: comment
      user_id: '1'
    - approved: '1'
      author: Mark Pearson
      author_email: markp@earlham.edu
      author_ip: 159.28.7.95
      author_url: http://markpea.wordpress.com/
      content: '&gt;Hope this helps.
    
    
        Yes it does. Of course, as soon as I posted the comment I found your other posts
        about BIM which threw more light on it. After I''ve got this operational on a
        test moodle site I''ll let you know how it works out.'
      date: '2010-02-24 09:08:36'
      date_gmt: '2010-02-23 23:08:36'
      id: '2752'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: davidtjones
      author_email: d.jones@cqu.edu.au
      author_ip: 59.154.24.147
      author_url: https://djon.es/blog/
      content: 'Will be good to hear feedback.
    
    
        The plan is that I will be making some minor changes/fixes to the BIM code today
        based on feedback from Netspot.
    
    
        Nothing drastic at this stage, but addressing some minor problems.
    
    
        e.g. I believe the zip file with the code in it might be slightly badly "zipped".  i.e.
        it has duplicate code.  Will fix that up.'
      date: '2010-02-24 09:33:50'
      date_gmt: '2010-02-23 23:33:50'
      id: '2753'
      parent: '2752'
      type: comment
      user_id: '1'
    - approved: '1'
      author: Mark Pearson
      author_email: markp@earlham.edu
      author_ip: 159.28.7.95
      author_url: http://markpea.wordpress.com/
      content: "&gt; Each BIM activity will have its own column in the gradebook. So,\
        \ if you have multiple different BIM activities in a single course, you\u2019\
        ll have multiple different entries in the gradebook.\n\nThis makes a lot of sense.\n\
        \n&gt;The gradebook entry for each student for a single BIM activity is simply\
        \ the sum of all the marks given to the posts. The assumption was that if the\
        \ teaching staff wish to scale or manipulate the grade, they can do that in the\
        \ gradebook.\n\nYes, ditto. Again, this is the intuitive way that one would expect\
        \ it to work.\n\nI do like the way that you have multiple questions within a singular\
        \ BIM Activity.  It's a natural way to map blog postings to an longer term assignment,\
        \ eg \"every week post a comment on the class discussion\".  Plus, having tutored\
        \ students on the art of trackbacks, one could also add commenting on other posts\
        \ as a BIM assignment.\n\nMark"
      date: '2010-02-25 01:02:55'
      date_gmt: '2010-02-24 15:02:55'
      id: '2754'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: davidtjones
      author_email: d.jones@cqu.edu.au
      author_ip: 59.154.24.147
      author_url: https://djon.es/blog/
      content: 'Mark, glad it''s making sense so far.  There will eventually be some mismatches
        between your ideas and the model in the system. An inevitable mismatch with most
        systems.  I''m keen to hear what that mismatch is when it happens.
    
    
        One source of that mismatch is likely to be that your more advanced with the use
        of blogs than all of the folk locally that used the previous systems (BAM).  Which
        meant the commenting and community aspects of BAM/BIM never developed as much
        as they could.  I only used BAM once, just after it was developed.
    
    
        For example, it would be interesting how to work in the trackbacks and comments
        on other posts into the BIM model.  I suspect it wouldn''t work straight forwardly
        at the moment.
    
    
        One BAM feature that is missing from BIM, is the generation of OPML files for
        academics.  These could be loaded into a news/feed reader and allow the staff
        to track student participation in an informal way.
    
    
        One suggestion for future addition to BIM is a feed forward mechanism. i.e. allow
        teaching staff to configure some method that would filter student posts and then
        generate a feed of some description.
    
    
        The filter might be as simple as including all student posts or it might include
        all the best students posts (based on mark) or those that have been tagged as
        interesting by the teaching staff or by some other means - perhaps number of trackbacks
        or links from other students.
    
    
        I''m particularly interested in hearing from folk who are keen to push the boundaries
        like this.  Happy to modify BIM to provide the type of functionality they''d like.
    
    
        David.'
      date: '2010-02-25 04:52:13'
      date_gmt: '2010-02-24 18:52:13'
      id: '2755'
      parent: '2754'
      type: comment
      user_id: '1'
    
pingbacks:
    - approved: '1'
      author: BIM &#8211; getting student registration working &laquo; The Weblog of (a)
        David Jones
      author_email: null
      author_ip: 74.200.245.226
      author_url: https://djon.es/blog/2009/12/17/bim-getting-student-registration-working/
      content: '[...] the registration process for students. As part of this process I
        am finally starting to use the to do list for what it was meant to be used [...]'
      date: '2009-12-17 10:02:54'
      date_gmt: '2009-12-17 00:02:54'
      id: '2749'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The to do list for BIM development is now [hosted on github](http://github.com/djplaner/BIM/issues).