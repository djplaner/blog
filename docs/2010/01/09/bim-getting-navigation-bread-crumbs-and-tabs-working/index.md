---
title: BIM - getting navigation bread crumbs and tabs working
date: 2010-01-09 11:47:06+10:00
categories: ['bim']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: BIM &#8211; Design of &#8220;Manage Marking&#8221; and other features for
        Coordinators &laquo; The Weblog of (a) David Jones
      author_email: null
      author_ip: 76.74.248.143
      author_url: https://djon.es/blog/2010/01/09/bim-design-of-manage-marking-and-other-features-for-coordinators/
      content: '[...] The Weblog of (a) David Jones Another voice in the blogosphere    &laquo;
        BIM &#8211; getting navigation bread crumbs and tabs&nbsp;working [...]'
      date: '2010-01-09 12:36:08'
      date_gmt: '2010-01-09 02:36:08'
      id: '2910'
      parent: '0'
      type: pingback
      user_id: '0'
    
---

See also: [[blog-home | Home]]

In the [last bit of work](/blog2/2010/01/07/bim-allocate-questions-screen/) on BIM I got the Allocate Posts page working. This created the issue of getting the navigation/bread crumbs trail work in a useful way. I made an initial start on that, this post tries to get it complete. It will also be an attempt to get the "tabbed" screen for the coordinator working.

Work to do includes:

- Get them working for a student.
- Get bread crumbs working for marker.
- Start work on the coordinator screens - tabs and breadcrumbs.
- Maybe do some re-factoring for the bread crumbs code.

### Student bread crumbs

Have made various changes to view.php while getting the markers stuff to work. Need to check that and get the breadcrumbs working.

First, there is now no header being shown for the student. That's due to the new header function. Fixed. Bread crumbs are working.

### Bread crumbs for the marker

Basically an extension of yesterday's work, checking it fits and fixing any errors. Work to do includes:

- Add a link/some description about the show post details screen on the show student details screen. **DONE**

### Coordinator screens

The use of bread crumbs for the coordinator is in large part tied to the use of navigation tabs for the interface. A coordinator will be able to perform the following tasks:

- Configure the bim activity.  
    This is the initial task and is probably going to include:
    - Details about the activity (name etc).
    - Specifying the questions for bim.
- View student details.  
    Essentially the same as a normal teacher.
- Manage the release of marking.  
    Only the coordinator can authorise the release of marks/comments back to students. Eventually this should be able to be devolved and worked into the view student details, in someway.

Might also be good to provide some details about marker progress - which markers done what.

So, initially, let's try for three tabs: Configure, Manage Marking (include details about marker progress and release of results), and View Student Details.

mod/quiz/tabs.php seems to be an accessible way to understand the use of tabs. Let's start with that. The process seems to be:

1. Create an array of tabobjects with at least three values: unique string id, link and textual name (to be displayed?).
2. Call `print_tabs` and pass in: list of all tabs, the current one, any that are inactive, those that are activated.  
    The current one uses the id of the tabobject. The other two parameters are an array of ids.

Okay, it seems that the list of all tabs, is actually a nested list. That was one of the barriers I was facing. It's actually an array of arrays of tabobjects. Not an array of tabobjects.

Bugger, that limited understanding has held me up a bit. Easy to move on now.

### What's to be done

To complete the coordinators stuff there are three main tasks:

1. Implement the form and processing for the configuration of BIM.  
    This will need to
    - Work properly from the start (i.e. no configuration).
    - Ensure that any changes to configuration once use of the BIM activity has started is done safely.
2. Design and implement the manage marking page.  
    Aim here to allow the coordinator to :
    - view a summary of what markers have marked what
    - release marked results/comments
    - view the details of a markers students
3. See how the existing student/post details screens can be harnessed to show up in the coordinators "Show details" tab.

I'm going to leave the first two to other posts. These are new functionality. Will look at reuse for the last point now.

### Matching coordinator with Moodle stuff

Moodle has the following roles in courses (at the moment): administrator, course creator, teacher, non-editing teacher, student, guest. Not 100% clear where CQU is going with the conversion of local roles into Moodle, will have to ask. But theoretically teacher might be equivalent to coordinator, and that's not currently working that way.

This is set up in db/access.php.

This is finally set up and working and the capabilities are better named now as well.

### Coordinator's show details

The coordinator of a course is also likely to be a marker. So they need to be able to see the same details about students and posts as other markers. That code is already implemented. The aim here is to reuse that code for the coordinator and make the output appear as part of the coordinator's tabs.

Basically working simply by adding in the appropriate calls to the functions via the coordinator function. One limitation is that the bread crumbs aren't working for the coordinator. This is in part due to the overuse of the screen parameter. Suggestion

- Rename the screen parameter for the coordinator tabs.  
    It's no been changed to "tab". Should also change the value so it matches in the id for the tab in bim\_build\_coordinator\_tabs. Done.
- Add a screen parameter.  
    Make sure the param for the show student details is used appropriately.
- Update the bim\_print\_header function to work with coordinator.  
    Improved the navigation for both groups.

### What's been done

First major steps in the coordinator screen have been taken. The tabs work. They can see details about their students. When I implement marking for other teachers, it will work for the coordinator.

### What's to be done?

The two remaining screens for coordinator need completion

1. Configure BIM - this needs connection with the "normal" Moodle configure aspect. The use of formslib should ease this. I hope.
2. Manage marking - need to think about how to design this and what to put in. May need to ask the coordinators for suggestions.

Also need to implement the marking screen. Once that is done. There is some tidying up to do and it is just about there.