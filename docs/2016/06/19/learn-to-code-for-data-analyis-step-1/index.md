---
title: Learn to code for data analyis - step 1
date: 2016-06-19 11:03:43+10:00
categories: ['bad', 'pirac']
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: Tony Hirst
      author_email: tony.hirst@gmail.com
      author_ip: 86.171.50.1
      author_url: http://blog.ouseful.info
      content: 'Hi David
    
        I was interested to read your comments:-) There are actually various other ways
        of delivering Jupyter notebooks (I started to collected examples here https://blog.ouseful.info/2014/12/12/seven-ways-of-running-ipython-notebooks/
        ) but for the FutureLearn we course we were hampered by having to take a DIY approach
        w/ no funding that would also allow learners to persist their notebooks on a course
        with a large number of students under further constrains of bandwidth, arbitrary
        operating system, wide in computer capability, scant scientific computing / programming
        computer admin skills etc!
    
        I think the notebooks offer a really promising environment for a wide range of
        computational science / social science / digital humanities activities. For example,  you
        can easily use them to create interactive widgets too (though we don''t cover
        that in the F/L course), eg https://blog.dominodatalab.com/interactive-dashboards-in-jupyter/
    
        I think it could be useful if s/one like FutureLearn tied up with one of the companies
        that uses notebooks as part of their online data analytics service and got them
        to sponsor something like a tmpnb setup, but from I can tell, I''m in a minority
        of one!
    
        --tony'
      date: '2016-06-20 03:25:56'
      date_gmt: '2016-06-19 17:25:56'
      id: '3363'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: David Jones
      author_email: davidthomjones@gmail.com
      author_ip: 139.86.69.33
      author_url: https://djon.es/blog/
      content: ':) All I know about Jupyter notebooks comes from reading your blog (love
        your work), and now the experience of the course. Hadn''t realised the course
        was a DIY effort.  All the more impressive for that. My hat is off to you and
        your colleagues.
    
    
        I''m with you. There is a lot of promise here and I''m hoping to play some more.
        Particularly interested in terms of its application to learning analytics within
        an institutional setting. Might be sufficient for me to find the time to move
        from Perl to Python (though I just discovered that there is an IPerl...)'
      date: '2016-06-20 08:30:18'
      date_gmt: '2016-06-19 22:30:18'
      id: '3364'
      parent: '3363'
      type: comment
      user_id: '1'
    - approved: '1'
      author: Tony Hirst
      author_email: tony.hirst@gmail.com
      author_ip: 86.171.50.1
      author_url: http://blog.ouseful.info
      content: 'Hi David
    
    
        The course was a DIY effort in the sense that the programming environment choice
        was outs and it was up to us as to how to enable the learners to make use of it.
        The course itself had an editor, media production folk for the interview/video
        segments with Ruth, production manager, and probably others! Much of the work
        was done by lead educator Michel Wermelinger.
    
    
        Re: learning analytics, I did the reflexive thing and tried to use what was covered
        in the course to analyse the data the platform gives back to us - though in the
        end I also went passed what the course covered. An example notebook (without any
        data in it) is linked to from here: https://blog.ouseful.info/2016/04/27/futurelearn-data-doodles-notebook-and-a-reflection-on-unlearning-analytics/
    
    
        Re: IPerl - yes, another of the really attractive things about Jupyter is the
        way that the programming language kernel is split from the notebook - so the notebook
        just represents a particular sort of user interface that can then be used with
        a variety of languages.
    
    
        The notebooks are also starting to act like some sort of source medium for other
        expressions of the code, such as dashboards ( https://github.com/jupyter-incubator/dashboards
        ) and APIs ( http://blog.ibmjstart.net/2016/01/28/jupyter-notebooks-as-restful-microservices/
        ).'
      date: '2016-06-20 18:55:02'
      date_gmt: '2016-06-20 08:55:02'
      id: '3365'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: David Jones
      author_email: davidthomjones@gmail.com
      author_ip: 124.176.217.5
      author_url: https://djon.es/blog/
      content: Thanks Tony.  As it happens I'm working with some colleagues around analytics
        at the moment and have started wondering about the notebooks as a method to help
        them understand and engage with it all.  Though I have to admit I'm <a href="https://davidtjones.wordpress.com/2015/06/24/dashboards-suck-learning-analytics-broken-metaphor/"
        rel="nofollow">biased against the concept of the dashboard</a>.  More reading,
        thinking, and playing due.
      date: '2016-06-22 17:04:22'
      date_gmt: '2016-06-22 07:04:22'
      id: '3366'
      parent: '3365'
      type: comment
      user_id: '1'
    - approved: '1'
      author: David Jones
      author_email: davidthomjones@gmail.com
      author_ip: 124.176.217.5
      author_url: https://djon.es/blog/
      content: Mmmm, notebooks as APIs, very interesting given my espoused bias.
      date: '2016-06-22 17:05:55'
      date_gmt: '2016-06-22 07:05:55'
      id: '3367'
      parent: '3365'
      type: comment
      user_id: '1'
    
pingbacks:
    []
    
---

See also: [[blog-home | Home]]

An attempt to start another MOOC.  Learn to code for data analysis from FutureLearn/OUUK.  Interested in this one to perhaps start the migration from Perl to Python as my main vehicle for data munging; and, also to check out the use of Jupyter notebooks as a learning environment.

Reflections

- The approach - not unexpectedly - resonates. Very much like the approach I use in my courses, but done much better.
- The Juypter notebooks work well for learning, could be useful in other contexts.  Good example of the move toward a platform
- The bit of Python I've seen so far looks good. The question is whether or not I have the time to come up to speed.

### Getting started

Intro video from a BBC journalist and now the software.  Following a sequential approach, pared down interface, quite different from the standard, institutional Moodle interface. It does have a very visible and simple "Mark as complete" interface for the information.  Similar to, but perhaps better than the Moodle book approach from EDC3100.

Option to install the software locally (using Anaconda) or use the cloud (SageMathCloud).  Longer term, local installation would suit me better, but interested in the cloud approach.  The [instructions](http://www.open.edu/openlearn/learn-to-code-installation) are not part of the course, seem to be generic instructions used for the OUUK.

**SageMathCloud**

Intro using a video, which on my connection was a bit laggy. [SageMathCloud](http://cloud.sagemath.com) allows connection with existing accounts, up and going.  Lots of warnings about this being a free service with degraded performance, and the start up process for the project is illustrating that nicely.  Offline might be the better option. Looks like the video is set up for the course.

The test notebook loads and runs. That's nice.  Like I expected, will be interesting to see how it works in "anger".

Python 3 is the go for this course, apparently.

**Anaconda**

Worried a little about installing another version of python.  Hoping it won't trash what I have installed, looks like it might not.  Looks like the download is going to take a long time - 30 min+.  Go the NBN!

### Course design

Two notebooks a week: exercise and project.  Encouraged to extend project. Exercises based on data from WHO, World Bank etc.  Quizzes to check knowledge and use of glossaries.  Comments/discussions on each page.  Again embedded in the interface, unlike Moodle.  Discussion threads expand into RHS of page.

# Course content

## Week 1

**Start with a question** - point about data analysis illustrated with a personal story. Has prompts to expand and share related to that story.  Encouraging connections.

Ahh, now the challenge of how to segue into first steps in programming and supporting the wide array of prior knowledge there must be. Variables and assignment. and a bit of Jupyter syntax.  Wonder how the addition of Jupyter impacts cognitive load?

Variable naming and also starting to talk about syntax, errors etc. camelCase is the go apparently.

And now for some coding. Mmm, the video is using Anaconda.  Could see that causing some problems for some learners. And the discussion seems to illustrate aspects of that.  Seems installing Anaconda was more of a problem. Hence the advantages of a cloud service if it is available..

Mmm, notebooks consist of cells. These can be edited and run. Useful possibilities.

Expressions.  Again Juypter adds it's own little behavioural wrinkle that could prove interesting.  IF the last line in a cell is an expression, it's value will be output.  Can see that being a practice people try when writing stand alone python code.

Functions. Using established functions.

Onto a quiz.  Comments on given answers include an avatar of the teaching staff.

Values and units.  With some discussion to connect to real examples.

Pandas. The transition to working with large amounts of data. And another quiz, connected to the notebook.  That's a nice connection.  Works well.

Range of pages an exercises looking at the pandas module.  Some nice stuff here.

Do I bother with the practice project?  Not now.  But nice to see the notebooks can be exported.

## Week 2 - Cleaning up our act

The BBC journalist giving an intro and doing an interview. Nodding head and all.

Ahh weather data.  Becoming part of the lefty conspiracy that is climate change?  :)

Comparison operators, with the addition of data frames.  Which appears to be a very useful abstraction.

Bitwise operators. Always called these logical or boolean operators.  Boolean isn't given a lot of intro yet.

Ahh, the first bit of "don't worry about they syntax, just use it as a template" advice. Looks like it's using the equivalent of a hash that hasn't yet been covered.