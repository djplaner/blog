---
title: BIM 2.0 - cleaning up part 4
date: 2013-02-01 11:01:00+10:00
categories: ['bim', 'bim2']
type: post
template: blog-post.html
---
Another step in getting [BIM 2.0](/blog2/research/bam-blog-aggregation-management/) ready for release. Addressing the current two outstanding issues prior to exploration of submitting BIM to [Moodle CONTRIB](http://docs.moodle.org/dev/Guidelines_for_contributed_code#The_CONTRIB_Frequently_Asked_Question_.28FAQ.29) (??appropriate terminology)

The two tasks are

- [Re-examine the cron requirements for bim](https://github.com/djplaner/moodle-mod_bim/issues/62)
- [Complete the initial gradebook integration](https://github.com/djplaner/moodle-mod_bim/issues/40)

And two new ones identified while working on the following

- [misc fix for student view](https://github.com/djplaner/moodle-mod_bim/issues/65)
- [Help popups not showing for students (but working for staff?)](https://github.com/djplaner/moodle-mod_bim/issues/64)

The next step is to explore getting bim into CONTRIB and a final all out test as part of that process.

## Cron requirements

Currently the "cron" code is commented out.

- Do I need to fix it?  
    The cron code in bim 1 will
    - For all bims with mirroring turned on.
    - Make sure the caching directory is set up.
    - get all the student feeds and process them.This is needed so that the mirrored feeds are up to date for the staff when they are marking. When a student visits BIM on Moodle it will automatically update their feed (assuming they've just posted and are checking).
- What additional changes are required?  
    Most of the work being done is built in bim code, that shouldn't need to change much from what it is. The question is whether the "caching directory" code is needed and/or what form it takes in Moodle 2.0. The "caching" is for the RSS file. This is now done by SimplePie which is now in Moodle core. This suggests nothing will need to change.

So lets try uncommenting the code and running it remotely...seems to hangup on the bim\_cron stuff. Some debugging required.

- Not including the bim library file...fixed.
- Incorrect use of get\_records\_select....twice...fixed.

All working.

## Gradebook integration

I need to get my head around how/if the current BIM/gradebook integration is working. This is repeating a bit of what's gone before, but need to get my head back into it. Probably best to start with a brand new BIM.

1. Add a new BIM activity.
2. Set the grademax.
3. View the gradebook to see what this does (all the way through the above and the following).
4. Register a student's blog.
5. View as student now and through the following.
6. Allocate and mark some posts.
7. Release (i.e. put into gradebook) the marked posts.
8. Repeat.
9. Add a grade category in the gradebook.

Let's do a couple of different BIM activities.

- Grade set to 50, 2 questions both with a max mark of 25 (doesn't really effect final mark just as a warning to the marker)
    - On creation, it appears in the gradebook for both teacher and student. The student has the range showing of 0-50.
    - Good to see the auto-allocation of posts to questions working. In fact all is working so far.
    - Let's mark one of the posts: BIM shows the student the update in status appropriately. And gradebook is showing nothing, as expected.
    - Release this result (25 out of 25 for the question). Will that be half of the 50 for grademax?
        - The student BIM screen shows the release appropriately.
        - The student gradeview is showing nothing. \*FAIL\*
        - Neither is the staff view. \*DOUBLE FAIL\*

Time to check what is going on

- coordinator/manage\_marking/bim\_manage\_release is the function that does the release and the update of gradebook. Here's the relevant code \[code lang="php"\] // update the gradebook entry if it makes sense if ( $bim->grade\_feed == 1 ) { $raw\_sql = "SELECT userid,sum(mark) as rawgrade from {bim\_marking} where bim= ? and status='Released' group by userid"; $grades = $DB->get\_records\_sql( $raw\_sql, array( $bim->id ) );
    
    bim\_grade\_item\_update( $bim, $grades ); } \[/code\]
- Changes to make to this code
    
    - The simple _sum(mark)_ is going to have to be replaced with a function.  
        i.e. the SQL should get a list of all the users and all the marks that are currently available for the user. It should then transform that into a grade for the gradebook.
        
        Initially this is probably going to be a simple percentage of grademax (i.e. add up total possible marks from BIM (sum of all question marks), generate percentage of that and then apply it to grademax.
        
        In the future, this is where various marking schemes can be put in place.
        
        **Important:** This implies a need to have a re-calculate and reset grades when/if grademax or the number of questions changes.
        
        Having fixed up the problem in the next step, time to come back and implement the function. Will do that below.
        
    - Check to see why the grade\_item\_update isn't working.  
        It would appear that the code in bim\_grade\_item\_update is simply not correct. Let's check that.
        - A look at the grade\_item\_update function for the forum mod reveals a very different approach. Looking for some Moodle developer documentation might be called for. That can be hard, so analysing the forum code is probably a better starting place.
        - Actually, this may simply be because the forum grading is more complex then what is currently in BIM. BIM is taking a straight value approach. Whatever BIM calculates is meant to go straight into the gradebook. So what is BIM giving it, try another test with some debugging code.
        
        - Ahh, that will be a problem. I've changed the database for the gradebook stuff, but not this code. "grade\_feed" is no more and it isn't using 1 for true.
        - Fix that up and re-mark and then re-release a result and hey presto **it is working**. With two posts marked for a total of 35, a mark of 35 is appearing in the student's gradebook and the percentage overall is working correctly.
    
    ### Calculating bim activity grade
    
    The aim here is to develop a grade calculation function for a BIM activity. This will be the initial version with a single, simple approach. Later on the function will be expanded to offer alternative approaches (at least that's the plan).
    
    The simple approach here will be based on
    
    - Teacher specifying the maximum grade/value that the activity can have in the gradebook.
    - Teacher specifying the number of questions and the maximum mark (as a warning) for each question.
    - Each students' gradebook mark is calculated by
        - Adding up the maximum possible mark for all the questions. (e.g. 50 marks)
        - Adding up the marks the student has for their questions. (e.g. 25 marks)
        - Figuring out the percentage the student has achieved (e.g. if 50 is 100%, then 25 marks is 50%).
        - Applying that percentage to grademax (e.g. grademax = 100, 50% of 100 = 50)
    
    The current code (shown above) calculates an array of arrays with _userid_ and the _rawgrade_. The list of userids is those of students who have posts that have been released. Pseudo-code should be something like \[code lang="php"\] # Will reset the grades for all students with released results function bim\_update\_gradebook( $bim ) { # get the maximum grade for a gradebook entry for this activity # get the total if students gets max marks for each question
    
    \# get an array of all userid/marks for the released posts from bim tables
    
    \# for each student # - add up total of all marks they received # - calculate percentage of total # - calculate what equivalent percentage of maximum grade is # - create an array (userid => , rawgrade => %maximum grade )
    
    \# update the gradebook } \[/code\]
    
    That's done.
    
    But what happens if the grade/mark bim tries to put into the gradebook is greater than grademax? Does the gradebook
    
    - Generate an error?
    - Accept the mark as is?
    - Limit it to the grademax? **This option**
    
    Mmm, setting a question total to 100 has generated an SQL error "Out of range value" for mark. This seems to suggest my mistake. Yes. The mark field in bim\_marking is limited to 4 digits. Is that a problem? The forum module uses a bigger number. I should make that change.... Well that's done.
    
    But there's still the chance of the user entering a bigger number again, perhaps the code should also place a limit. Time to make that change.
    
    The question now is when should this be called. i.e. when should the gradebook be updated with new grades for students. Currently it's called whenever the teacher in charge releases posts (i.e. makes them visible to students). Other situations I can think of where the gradebook might need updating include
    
    - When the marker changes a mark on a student's released post. ( i.e. after a query of some such.) - DONE  
        This is already handled. Whenever a marker changes a grade on a student post its status returns to marked. This means that the lead teacher needs to release it again. Releasing it again updates the gradebook.
    - When a the total possible marks for questions changes.  
        This might happen when the lead teacher changes the maximum possible mark for an existing question or deletes or adds a question. -- DONE
    
    ## Showing out of what for student
    
    The summary of released posts isn't showing the maximum mark possible for that post, just what the student got.
    
    Done.
    
    ## Student help popups, not working
    
    Moodle help is typically provided by popups. You see a little question mark in the interface, click on it and it pops up a box with some assistance. This is working well for the staff users. However, not so well for students. Even though the problem HTML is generated by the same PHP code for both classes of accounts.
    
    Confirmed that the HTML code generated by the PHP code is exactly the same. Implies that the difference must be in the CSS/Javascript included in the different pages. How to identify what and then fix it?
    
    Is there a config setting, site wide or course based? Can't see anything.
    
    Is this just a bim problem for students, or is it there for other modules? It appears to be a bim problem. Forum is working with popup help fine and is using the same HTML code.
    
    Is there something missing from the "header"/"footer" display for student? Yes. No footer being added. Fixed.