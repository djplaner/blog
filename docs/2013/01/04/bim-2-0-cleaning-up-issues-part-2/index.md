---
title: BIM 2.0 - Cleaning up issues - Part 2
date: 2013-01-04 20:09:44+10:00
categories: ['bim', 'bim2']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: BIM 2.0 &ndash; Cleaning up issues &ndash; Part 2 | A New Society, a new
        education! | Scoop.it
      author_email: null
      author_ip: 89.30.105.121
      author_url: http://www.scoop.it/t/a-new-society-a-new-education/p/3964977647/bim-2-0-cleaning-up-issues-part-2
      content: '[...] Building on that last bit of issue cleanup this aims to reduce the
        list of open BIM issues a bit more. The focus in this part will be #53 issue with
        question management message. #35 add support for...&nbsp; [...]'
      date: '2013-01-04 20:20:23'
      date_gmt: '2013-01-04 10:20:23'
      id: '556'
      parent: '0'
      type: pingback
      user_id: '0'
    
---

See also: [[blog-home | Home]]

Building on [that last bit of issue cleanup](/blog2/2013/01/01/bim-2-0-cleaning-up-issues-part-1/) this aims to reduce the [list of open BIM issues](https://github.com/djplaner/BIM/issues) a bit more. The focus in this part will be

- [#53](https://github.com/djplaner/BIM/issues/53) issue with question management message.
- [#35](https://github.com/djplaner/BIM/issues/35) add support for grademax in configure.
- [#40](https://github.com/djplaner/BIM/issues/40) complete a check on gradebook integration.
- [#37](https://github.com/djplaner/BIM/issues/37) figure out the missing status on manage marking.
- [#38](https://github.com/djplaner/BIM/issues/38) relook at how the help icons are produced (bring it into the modern Moodle age)
- [#57](https://github.com/djplaner/BIM/issues/57) hanging on use of print\_table.

Progressed a little further afield than I had expected with this one. But some progress made.

## Manage question message

Manage question displays a brief "summary" of what it does. Trouble is when a change is made this message starts the new page and is followed a "this is the change that happened" message. After a short time this page disappears replaced by the traditional page. The message shouldn't be displayed on the change. Remove it.

Done. Just moving a bit of code to the right place.

## Add support for grade max

BIM's current integration (inherited from BIM 1.0) is primitive. It simply adds up the marks recorded for each question and sticks it in the gradebook. Moodle activities can offer significantly more flexible support for grading. e.g. the forum plugin supports

- the mean of all ratings.
- the count of ratings.
- The highest rating.
- The minimum rating.
- The sum of all ratings.

For some of these methods the "maximum grade" plays a role. e.g. for the sum of all ratings, the total cannot exceed the maximum grade.

Currently BIM doesn't recognise or support the maximum grade. This didn't cause a problem in Moodle 1.9, but in 2.x it appears to be required. As a first step I need to add support for grade max. More advanced gradebook integration needs to be implemented in the future as part of issues #47 and #3.

As a first step, I looked at some of the other activities to find out how they handle it.

- forum  
    Uses a drop down list to chose a scale that has every number from 1 to 100 as well as "No Grade" and what I believe is an element for each available scale. Grade type can be NONE, VALUE or SCALE. grademax comes into it when it is VALUE.
- Assignment  
    The interface uses a similar drop down box for Grade. An addition is "**grading method**" which allows direct grading but also more advanced features such as rubrics and marking guide. There's also a **grade category** which was present with the forum, category seems to refer to a category in the gradebook.

This seems to be the trend

1. Add a grade "groupitem" to the configure page for the activity.
2. Allow a choice of how/if gradebook integration occurs.
3. Allow a choice of grademax/scale.
4. Possibly allow support for aggregation type.
5. And other options - e.g. advanced grading.
6. Ensure the choices is placed into the database appropriately.

One question I have is what happens when the maximum grade is exceeded? Who does what? Does the activity module code need to decide?

So how do we add these features to the configure page? Forum uses a Moodle provided function - standard\_grading\_course\_module\_elements which adds these elements to the form. [This bit of documentation](http://docs.moodle.org/dev/Grade_settings_modules#moodleform_mod::standard_grading_coursemodule_elements.28.29) suggests that the grade features shown relies on the configuration in MOD\_supports.

Tasks to do

- Can the presence of SCALE be removed from the drop down box?  
    Let's check to see where this SCALE entry is coming from and whether I can add some more. Try the gradebook, ahh view scales. Oops, error from bim 285 of lib.php another record\_exists without an array. Fixed.
    
    So there is the scale that I've been seeing in the drop down list. It's optioned as a standard scale and hence is available site wide. So if I turn that off, it should disappear from BIM? No, because it's still associated with the course. Even if I delete it from the gradebook for a course, it still shows up. Is this the expected behaviour? Even if I remove at the top level it seems to stick around.
    
    This is starting to suggest a need to either support the use of scales (which I really can't see working without some major work, that I do need to do later) or remove them in some way?
    
    Removing doesn't seem to be an option. Leave for now.
    
- How to update the Grade form elements with the existing values (e.g. if grade chosen to be 90, have 90 show up when configuring the activity)  
    It has to be saved in the bim database table. Which means modifying the table, using XMLDB and playing with upgrade.php. At least that's what I did. It's working now.
- Need to remove/modify the old BIM method's for turning on grading. - DONE
- Need to update the display of BIM (e.g. the coordinators view) to report the current status of grading.  
    Done as part of updating the main coordinator page.

## Updating the help

The current approach to generating help icons is old school. The following type of thing \[sourcecode lang="php"\] $help = helpbutton( 'config\_student\_reg', 'bim\_name', 'bim', true, false, '', true );\[/sourcecode\]

needs to be replaced with \[sourcecode lang="php"\] $title\_cell = $OUTPUT->help\_icon( 'config\_student\_reg', 'bim' );\[/sourcecode\]

Need to check all the screens for all the other users

- Coordinator
    - Configure - DONE.
    - Manage questions. - DONE
    - Allocate markers. - nothing to do
    - Manage marking - apparently DONE
    - Find student - DONE
    - Your students - DONE
- Marker
- Student  
    This is quite strange. The student page is mostly generated by the same code that is used in parts for the staff. However, while the help popups work for a staff member, they don't work for a student. Changing to a different them doesn't effect it. Will leave that as is for now.

## Figure out the missing status on manage marking

BIM places a feed item (e.g. a blog post) from a student into a number of different states including: submitted, marked, suspended, released. The manage marking page gives the course coordinator an overview of the number of feed items in each state for each marker. One of the states it displays is Missing. When I was doing some development, I thought I'd identified a bug with the missing status. Need to check this out and be sure its working.

All done. It is working. No problem.

## DO a complete check of gradebook integration

- View BIM as a student
- Release a post
- View BIM as a student  
    Have noticed that this page shows a total. i.e. how much the activity will be marked out of. This is currently calculated by adding up the maximum values for each of the questions. i.e. **not** using grademax. This disconnect needs to be fixed up. Will create an issue.
- View the gradebook as a student.  
    It shows the range, but no value or comments (another thing that will need to be fixed. Do I have to release something in gradebook as the teacher? The mark is showing up - well a mark is (9.9) which is interesting. The student got a mark of 5. More things to be explored here.
    
    This will have to do with the aggregation method. For the course this is set to "Simple weighted mean of grades"
    

In reading [about the gradebook](http://www.vle.monash.edu/supporttraining/learnbytech/moodle/assessing-your-students.html) some misc thoughts

- A BIM activity could be a grade category, with each post being a grade item within that category.  
    This appears to allow the use of the gradebook to aggregate the results. It would lead to the removal of showing a progress result from the student view. May have implications for the marking of posts.