---
categories:
- curriculummapping-cddu
date: 2010-04-02 10:04:43+10:00
next:
  text: '"PhD Update #25: A return to discipline?"'
  url: /blog/2010/04/02/phd-update-25-a-return-to-discipline/
previous:
  text: Elevator pitch for &quot;Moodle curriculum mapping&quot;
  url: /blog/2010/04/01/elevator-pitch-for-curriculum-mapping/
title: Moodle curriculum mapping - Step 3
type: post
template: blog-post.html
---
This will be a brief extension of [previous work](/blog/2010/03/30/moodle-curriculum-mapping-step-2/) around [this project](/blog/2010/04/01/elevator-pitch-for-curriculum-mapping/). The main aim is to start identifying some of the methods used by Moodle with its current outcomes approach and how those might be harnessed and modified to support curriculum mapping. In particular, some specific questions include: What's necessary to

- allow the outcomes to be grouped and displayed as such when showing an activity/resource? **IDENTIFIED**
- include a "help" link for each outcome or other means to explain? **IDENTIFIED**
- allow the outcome scale to be used on the activity/resource to indicate how well the activity/resource meets the outcome etc? **IDENTIFIED**
- display the curriculum map for a course?**IDENTIFIED**
- add "outcome mapping" to those elements that currently don't have it? **IDENTIFIED**
- prevent curriculum mapping outcomes showing up in the gradebook?**IDENTIFIED**

This is a work in progress and will be updated over the next couple of days.

### The association - where in code and the database

Moodle tracks which outcomes apply to activities and resources, the question is where in the code does this happen and where in the database is this information stored?

#### The code

The association appears as part of the edit screen for an activity or resource. This is implemented by moodle/course/modedit.php. This script:

- Is given various params, including section and course, including the module being used to "edit" the activity/resource.
- Is fairly typical PHP spaghetti code with little or no comments.
- Acts has a harness/factory getting the module code to generate part of the form.
- Has a section of code that retrieves and display the outcomes, all embedded in this enormous file - ugly.

The outcomes code seems to consist of (this is actually the handling of submission of the form, not display of the form - more on this below)

- Get all the outcomes for the course (whether or not to display them, is left till then)  
    if ($outcomes = grade\_outcome::fetch\_all\_available($COURSE->id))
    
    fetch\_all\_available is implemented in moodle/lib/grade/grade\_outcome.php. And basically defines a class that represents a grade outcome. fetch\_all\_available gets all course related outcomes listed in grade\_outcomes (the detail of the outcomes) and grade\_outcomes\_courses (which outcomes are being used in the course).
    
- Build array of grade\_items  
    It then loops through each outcome from above and uses moodle/lib/grade/grade\_item.php to create a grade\_item object for each outcome. This uses the grade\_items table to store information. Am not 100% sure where this fits in.
- The actual display is done using a "form" display...more on this below.

So the display is done using the form class defined by the module, which is an extension of moodleform\_mod. As the specific modules won't know about outcomes, the outcomes display would theoretically be done in course/moodleform\_mod.php. Yep.  
\[sourcecode lang="php"\] if ($this->\_features->gradecat) { $gradecat = false; if (!empty($CFG->enableoutcomes) and $this->\_features->outcomes) { \[/sourcecode\]

The process seems to be:

- Get grade outcomes for the course, again  
    Seems there is some duplication here, as it gets the grade outcomes for the course, all over again.
- Get's all grade items for the course, it any of them have an outcome set, then set this in the form?
- A couple of other steps here, not immediately clear.

The above only seems to be preparatory. There's a later section of code that adds the form elements for the outcomes. Again, there's a fetch all available outcomes. This seems more directly related as it simply adds the elements.

#### Where does it store "mapping"

The next question is where does it store the fact that a particular activity/resource is using/assigned a particular set of outcomes?

This should be set in the code that processes the submission of the form. Which should be moodle/course/modedit.php. Ahh, this is done with grade\_item as described above.

i.e. when you map an activity/resource in a course to an outcome or three, that mapping gets stored in the grade\_items table. The fields in that table are (the descriptions are tentative):

- id - the unique id for the mapping of activity/resource to a single outcome.
- courseid - the id for the course that "owns" this mapping.
- itemname - this is the actual name of the outcome assigned
- itemtype - I believe this describes the type of object you've mapped the outcome to. Possible known values are currently mod, course.
- itemmodule - the name of the specific module that implements the object. Possible values include: forum, bim (i.e. name of any module), assignment, resource.
- iteminstance - I believe this is the id for this particular instance of the module. i.e. the id for the table course\_modules. The pathway to more information about this instance.
- itemnumber - for outcomes, this seems to start at 1000. It is used to give the sequence with which outcomes are assigned to the item. i.e. the first outcome assigned is 1000, the second 1001, the 3rd 1002 .... It appears that a value of 0, might indicate something important
- iteminfo - currently set to NULL for all the entries I've seen so far. So, not currently sure what it is used for.
- idnumber and calculation - also set to NULL or empty for the contents of my database - which doesn't include a lot of real courses.
- gradetype - integer, currently with value of 1 or 2. With outcomes I've set being 2.
- grademax and grademin - fairly obvious. Seems to be set by scale and/or other stuff.
- scaleid - the scale being used.
- outcomeid - the id of the outcome
- gradepass multfactor plusfactor aggregationcoef - various factors used for grade calculation, I believe.
- sortorder - different integer values - purpose not immediately obvious.
- display - big int, currently all set to 0. Not sure of purpose.
- decimals hidden locked locktime needsupdate - various flags ?
- timecreated timemodified - time stamps. Could be useful for identifying outcomes that need to be re-checked.

It appears that grade items and outcome items are treated the same, hence their use of the same table. The full view of categories and items give a good overview of this table.

There is the concept of categories of grades/items, this might be one avenue. i.e. a category for curriculum mapping.

#### What is the implication of this?

The next question is what are the implications to the rest of Moodle. If I map all the activites/resources within a course against a complex set of outcomes, does it have an effect on the gradebook? Any where else?

So, I've set outcomes for a number of activities/resources in a course. Does this show up anywhere else? Two ways of looking:

- Check the gradebook from web interface.
- Look for use of grade\_item class/object.

Mmmm, not good. It appears that every time you add an outcome, it get's added to the gradebook. In terms of curriculum mapping, not what is desired. This is perhaps the first obvious example that curriculum mapping and tracking student performance, while to some extent similar, serve different purposes.

The column in the gradebook for each outcome that is added, has a header that is a link. The link is to a script that shows some detail of the resource or activity that it the outcome is associated with.

Need to turn this off.

Now, you can hide an element in the gradebook. But that just greys it out, doesn't remove it entirely from consideration, which is what is wanted here.

### Adding a description/help

#### Problem

At least initially the outcomes etc shown are not going to make much sense to a teacher. Moodle currently only displays the name of the outcome. The teacher would have to somewhere else to read up on the outcome before they can determine if it applies. It would be helpful if additional assistance was provided there and then.

Some options in terms of what could be displayed, include:

- The description of the outcome.  
    As it stands Moodle allows each outcome to have a textual description. Displaying this as a roll-over or in a new window could provide a minimal level of assistance.
- Link to institutional area for discussion and description of outcomes.  
    The assumption being that most institutions would have a website in which institutional outcomes etc are discussed or described. Providing a link to this area, especially to the context specific to the a particular outcome might be useful.
- Link to other examples.  
    Many of the forms of outcomes etc. are likely to be used in other courses. e.g. institutional graduate attributes. It might be useful to give the option to see other examples of how these attributes are used in other courses. Even to the extent of link directly to those courses and/or reflections/discussion from other teachers using this outome.

These ideas range from the simple and static through to something you'd want to have some curating.

### Possible solutions

The outcomes are displayed around line 220 in moodle/course/moodleform\_mod.php. This is where the change would have to happen. Some possibilities include:

- Using a Moodle helpbutton.  
    Moodle forms have a function - setHelpButton - which associates a help button with an element. Very easy to make this modification. However, the problem is that the helpbutton is typically a call to open a new, small browser window to display HTML file.
    
    This is problematic as the outcomes are added via the Moodle interface and doesn't provide support for adding a help file. So, outcome specific would be difficult. However, an institutional area/approach could be possible. It would require the institution to create HTML files for each outcome.
    
    Let's do a simple test, put the Moodle code under git so I can manage this. And add a help button for each outcome. As expected, works easily. There is the question of how to create the filename for the HTML file. Most outcomes will have spaces and other characters that don't necessarily play nicely with a filename. The language translation side of Moodle could help there, convert the complete outcome name into something more file system friendly.
    
- More complicated HTML  
    Another approach would be to add roll overs, additional links etc to the outcomes. This would require a more radical modification of the Moodle core but not much more than the above. Not to mention the desire to separate attributes up into groups.

### Groupings of outcomes

#### Problem

It is likely that a course may have multiple different types of outcomes etc to map against. e.g institutional graduate attributes, discipline graduate attributes, course learning outcomes, program learning outcomes etc. There are two possible solutions (possibly complementary):

1. Show outcomes grouped by category.  
    To allow the mapping of an activity/resource against all these different groupings, it would be useful to separate out the different outcomes by category. So you could have a visible separation.
2. Have a separate cross mapping.  
    Mapping against all of these different outcomes might be somewhat tiresome, especially given a large amount of overlap between them. An approach that has been used is to produce a mapping between the different outcomes and a single point, and then only map activities/resources against that single point. Which of the different outcomes applies, can then be derived from the single point.

#### Possible solutions

Showing outcomes by category is going to need:

- Some way of specifying categories/groups of outcomes.  
    Which probably implies an additional database table and an additional interface or modification to an existing interface (e.g. the import outcome process) to specify which category an outcome belongs to.
    
    A separate interface minimises changes to core Moodle code, modifying existing interfaces is probably a more user friendly approach, depending on how widespread this need is.
    
- Modification to the form display to recognise the categories.  
    This should/would be a fairly simple thing to do, given the information above and Moodle's form library.
    
    Let's try a simple test. Create two boxes of outcomes that contain a copy of the same outcomes. Mainly to test if nested header/boxes work. No, they don't. You'd have to use a separate header label and then have separate boxes for each, perhaps a table? Though Moodle dislikes table for layout.....
    

### Display a curriculum map for a course

#### Problem

One of the basic functions for curriculum mapping is to get a report that shows how widely (or not) the outcomes are represented within the course in terms of resources, activities and assessments. i.e. you want a visual representation of the outcome mappings.

### Possible solutions

Well, it's basically a report, but you might want it more interactive than that.

Well, the existing outcomes report can do this to some extent. So an extension of this, or the additional of a mapping report might fill the bill.

To a large extent this is a fairly standard web application. Get the data from the database and display it in an appropriate form.

You'll be needing data from the following tables:

- grade\_items - given a course id, this will give you all the outcomes for the course that have been mapped to activities/resources and the ids of those activities and resources.
- grade\_outcomes - will give you details about the outcomes - name, description, and scale id.
- scale - details about the scales
- course\_modules - more information about the module/activity, most importantly perhaps the section of the course in which it appears.
- resource - for the same reason as modules

### Show outcome scale on activity/resource

#### Problem

Rather than simply "mapping" an outcome to a particular activity/resource, it may be useful to indicate how well/to what level does the activity/resource map to the outcome. i.e. use a scale, rather than a simple check box.

This is a fairly major distinction between outcomes for curriculum mapping and outcomes for student progress.

#### Possible solutions

It's looking like a separate set of "Mapping outcomes" might be the way to go. This would also get around the problem with the gradebook from above. This might mean duplicating the items table, or at least adding a flag to differentiate between mapping and progress outcomes.

Similarly, could probably still use the standard outcomes "creation/import" process for both purposes.

Adding separate support would also help make it a bit easier to add curriculum mapping to an instance of Moodle by minimising disruption to the Moodle core.

### Elements that don't have outcomes

#### Problem

As [outlined earlier](/blog/2010/03/23/first-step-in-moodle-curriculum-mapping/) there are some elements of a Moodle course site to which you can't map outcomes. The outcomes don't appear on the "edit" page. Those identified so far are labels and sections.

Sections might be useful, if you wanted to map a course by weeks, rather than by item. But perhaps not, you can generate such a map by aggregating the mapping of the contents.

Labels are way of inserting HTML into sections. Currently they don't have support for outcomes. I've already seen in one course how such labels can be used to specify tasks, such as reading.

#### Possible solutions

Well, labels are the only real problem. The form for labels is generated using moodle/course/modedit.php. The same for anything else. It is the place where outcomes are shown. So, perhaps it's just a switch that needs setting. Perhaps, outcomes aren't here as it isn't expected that these will be used in grades - i.e. student progress tracking.

Nope. The mod\_form.php file for label actively turns off outcomes in a setting. Yep, set that to true and outcomes are there.

In light of the above, you'd probably have a separate set of outcomes for mapping, have this defined as a feature that modules can turn on/off and go down that route.