---
categories:
- bam
date: 2009-08-17 09:07:45+10:00
next:
  text: Moodle, curriculum mapping, task fit and task corruption
  url: /blog2/2009/08/17/moodle-curriculum-mapping-task-fit-and-task-corruption/
previous:
  text: People, cognition, rationality and e-learning
  url: /blog2/2009/08/16/people-cognition-rationality-and-e-learning/
title: '"BIM #4: Re-jigging how BIM works"'
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: 'BIM#5: Getting a prototype BIM going &laquo; The Weblog of (a) David Jones'
      author_email: null
      author_ip: 72.233.96.141
      author_url: https://djon.es/blog/2009/08/20/bim5-getting-a-prototype-bim-going/
      content: '[...] Getting a prototype BIM&nbsp;going  In the last bit of work I did
        on BIM, I got to the stage of having some initial working code for BIM module
        that allow [...]'
      date: '2009-08-20 11:43:18'
      date_gmt: '2009-08-20 01:43:18'
      id: '2712'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: Moodle, curriculum mapping, task fit and task corruption &laquo; The Weblog
        of (a) David Jones
      author_email: null
      author_ip: 74.200.247.113
      author_url: https://djon.es/blog/2009/08/17/moodle-curriculum-mapping-task-fit-and-task-corruption/
      content: '[...] Weblog of (a) David Jones Another voice in the blogosphere    &laquo;
        BIM #4: Re-jigging how BIM&nbsp;works  Lessons for e-learning from&nbsp;people
        [...]'
      date: '2010-01-19 12:55:45'
      date_gmt: '2010-01-19 02:55:45'
      id: '2713'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The [last post in this series](/blog2/2009/08/13/bim-3-getting-the-module-work-making-some-progress/) saw me struggling - the long way around - to the realisation that the implementation model I had in my head wasn't going to work. At least not with the constraints of the model adopted by Moodle.

This post is about me struggling to come up with a implementation model that will actually fit the Moodle model and hoepfully also the students and teaching staff that will use BIM.

### Getting in the Moodle model more

Perhaps part of the problem, is that I'm not familiar enough with the Moodle model to feel how it works. So, let's play with some of the standard modules and add activities.

- Quiz
    - First page is the main configuration page, lots of options. But nowhere to specify the questions or question bank.
    - View the page (as the admin user) and you get to see the question bank editing/adding interface. Also see a range of other buttons.
    - A student view doesn't include the whole question bank interface, just a message "no questions yet"
    - The update interface returns back to the original configuration page.
    - Once a question is answers, the student sees an "Attempt quiz now" button
    - Each of the different operations draw on different php script in the mod/quiz directory.

### Quiz inspired BIM model

Based on the above, the BIM model might become:

- A BIM activity is added to the course.
- This brings up the BIM configure page.  
    This covers everything need to set it up initially. Including the HTML/text to explain to the student the purpose of the assignment and how it works. i.e. not a URL
    
    This might also include an option to change the use of "blog". i.e. if they want BIM to aggregate something other than a blog, just some RSS etc.
    
- The configure page becomes what is shown for the "update"  
    So this means that there is no need for a configure activity.
- A student would then have the following options if they were to view the BIM activity
    - View background information i.e. what it's all about.
    - Register their blog and/or see information about their blog.
    - View progress.  
        This would include a list of the questions they are meant to answer and indications of which they have answered.
- A staff member would see
    - Details - list of all students, who are registered, who is not etc.
    - Post summary - list of all matched answers for each student.
    - Questions - a list of all the questions  
        The coordinator would be able to configure these. Normal teacher would just see the details. The code would be much the same as that for the view progress for the students.

That seems more doable, probably need the block at a later stage.

### Get going

So, let's not rest and do some design. Let's get coding. Start with the configure/update/add option. This is essentially a modification and play with the dummy function provided by the NEWMODULE template. First step should be to identify what configuration data will be needed - at least at a minimum. Here's the first list:

- Name for the bim activity.  
    This becomes the name displayed on the course page.
- Instructions for students.  
    This is the background/instructions for the students about the BIM activity.
- Mirror  
    Should the feed for students in this course be mirrored?
- Register  
    Can students register their feeds.
- Change  
    Can students change their feed.

That's probably enough for now. Some of the obvious ideas for later would include:

- Dates for when students can register.

#### Config form

So let's get going on modifying this thing:

- Uses the [formslib stuff](http://docs.moodle.org/en/Development:lib/formslib.php) from Moodle.  
    Various PHP functions to automate setting up the HTML form and having it play nicely with the Moodle checks etc.
- Draws on the language files lang/\*/bim.php to specify various strings that are used in the interface.
- Seems to be a standard to start with "General" settings, then specific activity settings, then some more specific ones.
- Mirror, Register and Change are all essentially booleans, they need to be checkboxes.  
    Quiz uses these a lot. So might steal the examples. Probably not the best approach. How are the docs? Probably better to start with the more [generic ones](http://www.midnighthax.com/quickform.php)
    
    So the code goes something like
    
    ```
            $mform->addElement('advcheckbox', 'register',
                        get_string('register', 'bim'), '' );
            $mform->addElement('advcheckbox', 'change',
                        get_string('change', 'bim'), '' );
            $mform->addElement('advcheckbox', 'mirror',
                        get_string('mirror', 'bim'), '' );
    
    ```
    
    Will need to do some additional checks as we go along, but that's working in terms of display at the moment.
- Add help links for the BIM settings.  
    This makes use of the setHelpButton method of the form class. Need to create an appropriate HTML file within the lang/\*/bim/help/bim directory that matches the string name used in lang/\*/bim.php. Then various parameters make the link
    
    ```
    $mform->setHelpButton( 'register', array( 'register',
          get_string( 'register', 'bim' ), 'bim' ));
    $mform->setHelpButton( 'mirror', array( 'mirror',
          get_string( 'mirror', 'bim' ), 'bim' ));
    $mform->setHelpButton( 'change', array( 'change',
          get_string( 'change', 'bim' ), 'bim' ));
    ```
    
- Get it stored in the database.  
    Done the simple interface stuff, now to get it stored in the database. I'm assuming this is going to related to update\_instance in lib.php
    
    The intro and other standard stuff in the form is handled by default in the mdl\_bim table. And by some fairly simple code.
    
    And if I do a print\_r( $bim ) in the function I can see that the form data is all passed in as expected. All nicely put into 1s and 0s for the checkboxes so it can be put straight into the mdl\_bim\_configure table I set up earlier. All I have to do now is to figure out how it works.
    

#### Working with the database

Most of the example modules I'm looking at seem to be accessing the global $DB, retrieving data from the form object, doing some checks/manipulationg and then calling various methods of $DB to stick it in the database. So, probably just means getting a grasp on $DB and its methods.

So this is one area where a move to Moodle 2.0 will need a change. The DML for pre-2.0 is different than for 2.0 onwards. Pre-2.0 [docs](http://docs.moodle.org/en/Development:DML_functions_-_pre_2.0)

Tasks to do

- Change the config of mdl\_bim\_configure to use bim id rather than course id.
    - Of course this is when I discover the "change" is a reserved name by XMLDBB. Have to change this and the other code.
    - In the end, rather than figure out how to upgrade, I just deleted the module and reinstalled - blowing away the old dbase
- Modify add\_instance to insert initial default values in mdl\_bim\_configure
    
    - Need to get the id for the entry in the mdl\_bim table, used as field for the mdl\_bim\_configure table  
        The insert\_record function is meant to return the id.
    - Create a default record and then insert it into mdel\_bim\_configure.
    
    Well that works ok. Should I be putting error checking in? Maybe eventually. Still working on the prototype.
    
- Modify the form so that it retrieves the information from bim\_configure and shows it
    - I'm assuming this implies mod\_form.php needs updating?
- **Wrong** - much simpler way is to modify bim table to include what's necessary. Much smarter and more Moodle approach.

Yes, well that works much better.

### Status

Have other things to do. Today's seen some progress, mostly in terms of getting a better understanding of the Moodle model and figuring out how BIM might fit within that. The main measurable outcome of the day is that a BIM module exists and it can be used to add an activity to a Moodle course.

Of course, it won't do anything, but all the other stuff is there.

At this stage, I think next Tuesday's task will be to implement some hard-coded HTML to develop a prototype. However, that's not likely to look too Moodle like. I might look at going a step further and having it be able to use an existing set of tables. Almost hard-coded but with some real data....