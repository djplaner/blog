---
categories:
- bim2
date: 2013-02-27 18:11:24+10:00
next:
  text: BIM2 and disable_form_change_checker
  url: /blog/2013/03/03/bim2-and-disable_form_change_checker/
previous:
  text: And it starts again, edc3100 in 2013
  url: /blog/2013/02/26/and-it-starts-again-edc3100-in-2013/
title: Diagnosing a BIM problem
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: BIM2 and disable_form_change_checker | The Weblog of (a) David Jones
      author_email: null
      author_ip: 72.233.69.24
      author_url: https://djon.es/blog/2013/03/03/bim2-and-disable_form_change_checker/
      content: '[...] if they give you a clear and concise explanation you can use. That&#8217;s
        what happened with the BIM2 problem I blogged about recently. It appears I was
        using Moodle 2.3.4 the problem was found on Moodle [...]'
      date: '2013-03-03 18:09:14'
      date_gmt: '2013-03-03 08:09:14'
      id: '640'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The following problem with using BIM has [been reported](/blog/research/bam-blog-aggregation-management/#comment-6088) the following is a record of my attempt to recreate and fix the problem. The problem

> I installed BIM2 on my Moodle 2.3. The installation was successful and I even managed to create a BIM activity. There is only one problem — When I go to Mark posts and click on a post, the only thing that is shown on the screen is the Changing post allocation headline. The rest of the screen is empty.

In the end, I haven't been able to recreate the error. It's all worked as expected. Hopefully the following detail is sufficient to identify what I did differently.

The process I plan to use is

1. Install a fresh version of BIM2 on my local install of Moodle 2.3  
    The problem may arise from the version of the code or how it was installed. Making the process I use explicit may help identify any difference. This probably isn't where the problem is, but have to rule it out.

3. Create a new course, including students, staff and groups.

5. Create a BIM activity.

7. Try to mark posts often and early in between the following steps
    - Have a student subscribe a blog.  
        Being able to click on a post suggests that a student was at least able to subscribe.
    - Create some questions  
        I'm wondering if clicking on a post before specifying questions may be the cause of the problem.
    - Allocate students to a marker.  
        This shouldn't be a problem. BIM should tell you there's nothing to mark.

## Install BIM2

There's already a version of BIM2 installed. Let's see if the uninstall process works for BIM. Yes, all the database tables are gone. Now to remove the bim directory. Done.

Now, install the new version of BIM2. The BIM code is available [from github](https://github.com/djplaner/moodle-mod_bim). You do need to make sure to use [the BIM2 branch](https://github.com/djplaner/moodle-mod_bim/tree/bim2) and not the old BIM1 code (which won't work for Moodle 2.x).

Perhaps the easiest way for a non-coder to install the BIM2 code is to use the "ZIP" button on the [BIM2 tree](https://github.com/djplaner/moodle-mod_bim/tree/bim2). This downloads a file called moodle-mod\_bim-bim2.zip. You simply unpack this in the mod directory of your moodle install. For me this looks like

\[code lang="sh"\] unzip moodle-mod\_bim-bim2.zip mv moodle-mod\_bim-bim2 bim \[code\]

i.e. when you unzip the file it creates a directory called "moodle-mod\_bim-bim2" with all the bim code in it. You need to rename this directory to bim.

Now to install the module. Back to the site administration and the notifications page in Moodle and there's the message that bim needs to be installed. Click on the button and get the nice green Success message.

<h2>Create a new course etc.</h2>

In order to create a BIM activity, you will need to have a course site in Moodle that includes <ul> <li> Some enrolled students. </li> <li> Some enrolled staff. </li> <li> The students organised into groups. </li> </ul>

So, I'm going to <ul> <li> Create a new course. <br />Just a name and a number should be fine. </li> <li> Enrol some users.<br />I typically start by enrolling the admin user account as a teacher. I should probably create some teacher accounts, but not yet. <p>I don't have any students in this test version of Moodle 2.3. So I need to upload some before I can enrol them in the new course. To do this I have an text file I use with the "Upload Users" feature. The text file is looks like this.</p> \[code lang="sh"\] username,password,firstname,lastname,email s001,fred,Fred,Nerf,s001@nowhere.org s002,fred,Nerf,Fred,s002@nowhere.org s003,fred,Dawn,Hay,s003@nowhere.org \[/code\]

Now enrol them in the course.

- Put the students into a group.
    
    To mark posts in BIM, you need to allocate the students to a marker. Currently this is done by allocating Moodle groups to which the students belong. i.e. you can't allocate individual students to markers, only groups. So, create some groups.
    
    I just create an "all" group and add my three students.
    

## Create the BIM activity

Click on the "Add an activity or resource" on the course site and there's BIM in the list of activities. Select it and click add. Configure the BIM activity

- Provide a name (the only compulsory part).
- A description.
- Enable registration and mirroring  
    You don't have to but without these the activity is pretty useless.
- Select whether you're going to integrate this into the gradebook, or not.  
    For this one, I wont'.
- Click on "Save and display"

I can now see the "coordinators" interface for BIM. "coordinator" == "teacher in charge". Since I create the BIM activity, it's what I see.

I'm going to quickly click on each of the tabs in this interface

- Configure BIM  
    The default screen, shows a summary of the configuration and a link to change the configuration. All good.
- Manage questions  
    Where add, edit or delete questions that the students are expected to respond to via their feeds.
    
    As expected, there are "No current questions". All good.
    
- Allocate markers  
    Allocate markers to groups. Nothing allocated yet. It is showing all the teaching staff (just the admin account) and against those all of the groups (just the "All" group).
- Manage marking  
    Allows the coordinator to see marking progress for all markers. Currently showing no markers allocated and no registered students.
- Find student  
    Allows you to search for a specific student. Just the search box currently. Let's search for "dawn". Finds the student and tells me "No registered feed". As expected.
- Your students  
    This is where the marking happens. Where I can see the students allocated to me to mark. Nothing allocated, so it's showing no students allocated.

So far, so good.

## Some testing

### Register a blog for a student

I'm going to to this two ways

1. Coordinator can register a blog for a student via the Manage marking page.  
    Click on the "register blog" link, paste in the URL of my blog - http://davidtjones.wordpress.com, save changes......
    
    Error - curl couldn't connect to host. Ahh, I'm doing this from my office. The university has a web proxy. I haven't configured Moodle with the details.
    
    Go to site administration, search for proxy, enter the details. Try again to register.
    
    A delay, back at home. No proxy and the blog is registered no problems.
    
    Now try to view and mark posts. I don't think this should work as no students are allocated to me as a marker. That is as expected.
    
2. Have the "student" login and register a blog.  
    Start up another browser, log in as the user and register another blog. Go to the course and the BIM activity. See the normal "register your blog" for the student. I'll use a random blogspot blog for this student. Registered all ok from the student's perspective. All appropriate from the teacher's perpsective.

### Allocate the student group

Use the allocate markers screen. Manage marking is no showing this. Click on Your students and it all appears as I would expect. I can click on the "mark posts" link and see the detail.

There's nothing to mark at this stage, but I can click on a link that will show all of the student posts. I wonder how this will work? Don't think I've done it in this order before.

No worries. As expected, shows the list of posts. Allows me to "change allocation" but the only option is unallocated. Which works, though perhaps isn't neat. It should show a "Can't allocate because no questions" type error. Add an issue in github so this can get fixed.

### Create some questions

So create some questions so I can actually try some marking. Create two dummy questions.

Now revisit the "Your students" tab to do the marking. As expected, none of the registered students' posts have matched the questions. I have to go to the Allocate posts page to manually allocate the posts to questions.

Done. The "Mark it" link is there now. (Finally). As expected I get the marking interface.

All working. Try the second student. All working.