---
categories:
- bim
date: 2010-12-02 11:25:19+10:00
next:
  text: A new theme for Moodle 2
  url: /blog/2010/12/06/a-new-theme-for-moodle-2/
previous:
  text: Schools, systems and change done to me
  url: /blog/2010/11/29/schools-systems-and-change-done-to-me/
title: More testing for Moodle and BIM versions 2.0
type: post
template: blog-post.html
---
Continuing on with [playing with Moodle 2.0](/blog/2010/11/18/installing-and-starting-with-moodle-2-0/) and in particular its external blog syncing and integration of SimplePie. The aim here is to test the problem with special characters in feeds and what it does to PostgreSQL databases.

### The problem

This is the [biggest problem](/blog/2010/09/05/more-problems-with-bim-and-special-characters/) I've had with BIM and only really appears to be a problem with folk using PostgreSQL. Though I'm wondering whether there is some sort of option in PostgreSQL to solve this.

In summary, the problem is:

- Student creates a blog post by writing the content in Word.
- Then copying and pasting from Word into the blog engine's text box.
- This creates posts that contain special characters.  
    e.g. [this one](http://vjones88.wordpress.com/2010/08/16/week-6/), though this was not the student's fault. The teacher created directions that included special characters that were copied over by the student.
- When BIM tries to import these posts and Moodle is using a PostgreSQL database, it won't insert into the database.

**Important:** I don't have this problem on the MySQL database I typically use.

So, can I re-create this problem on Postgres.

### PostgresSQL

Well there's an executable PostgreSQL ready for install, download that. Oh dear, need to change a kernel configuration and re-boot.

Now, let's create another Moodle 1.9 install and get BIM working on it with some "bad" feeds.

- Moodle installed and working.
- Bring in a copy of BIM  
    I'm always forgetting this as I don't use git often enough now, so a bit of documentation  
```sh
sudo git clone git://github.com/djplaner/BIM.git 
```
    Go to http://localhost/mp/admin and the install runs and success.
- Let's backup a course from my MySQL Moodle 1.9 install and import it here.
- Okay, nothing showing, some problem with BIM.  
    Note to self, BIM needs to be installed in a directory with lowercase bim, not uppercase.
- Create some student accounts, allocate them to groups.
- Allocate markers in BIM.  
    Opps, debug error.
    
    ```
    Ahh, no check if there are no markers.  Will have to modify this. Done.
    ```
    
- Set up Moodle 1.9 based on Postgres
- Create the moodle database on postgres
- Set up the BIM module and feed it a bad feed.

### Results

I didn't have a problem. The feeds which have traditionally not worked with BIM on the institutional servers, worked fine with the local version of Postgres. Which is sort of what I suspected.

This provides further evidence to suggest that the problem with BIM and special characters is arising from something specific to the configuration of Postgres at the institution. Have asked for the specific details of the configuration to see if there is any difference. Also asked for any additional problem reports they may have, just to see if other feeds might cause a problem locally.

In short, at the moment, there doesn't appear to be a general problem.