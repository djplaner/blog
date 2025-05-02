---
title: "BIM - Tidy up #3"
date: 2010-02-01 14:38:13+10:00
categories: ['bim']
type: post
template: blog-post.html
---
Next step in tidying up is to clean up the checking, calculation and setting of the blog and feed URLs as students register their blogs.

First, fix up some problem with markers without any students.

### Unregistered students

Which highlights a problem with coordinator seeing unregistered students. Add this information to the Manage Marking page.

Process is: get all student details, call the appropriate functions.

Now there is a bim\_get\_all\_students, but it currently relies on bim\_markers\_students. Need to replace that.

Let's use it first and get that bit working. Done.

Now time to replace the kludge with something that will actually get all students in a course. I'm guessing that `get_users_by_capbility` is the one to use here. Done.

### Checking of blog URLs

One of the biggest areas for work is students who make mistakes when registering their blog. BAM does a range of tests including:

- Can the URL actually be retrieved.
- Does the URL include a link to RSS feed - done via auto-discovery.
- Can the feed (any one of them) be retrieved.
- Can the feed be parsed as XML

At the very least these checks need to be made.

Additional checks that need to be made, based one experience:

- The feed is not the wordpress.com feed  
    Students can choose to register something a bit too early in the blog creation process that returns the main feed from wordpress.com.
- They register the edit screen of Wordpress e.g. http://myblog.wordpress.com/wp-admin/edit.php.

The checking is one stage, the other is how to communicate these problems back to the students.

So, checks to implement:

- Is it even a valid URL.
- Can the URL be retrieved
- Can we get some auto discovery feeds
- If not, is the URL itself a feed?
- If there are feeds, loop through each one, and work with the first one that
    - We can retrieve
    - Is a feed
    - And doesn't break any of the exclusions we know of

Interestingly, [SimplePie](http://simplepie.org/) makes this process much simpler in that it does much of the checking itself.

Should also look at client side checking i.e. make the form stop if the student hasn't put in a URL. Do that later.

#### Testing SimplePie

- User enters blog url (not RSS) - e.g. http://davidtjones.wordpress.com - then permalink is blog and subscribe url is feed for both Wordpress and blogger
- User enters feed URL - e.g. https://djon.es/blog/feed/ - permalink is blog and subscribe url is feed. Wordpress and blogger.

So, it seems I can trust SimplePie to do this and simply check permlink/link and the subscribe link. Need to check that both URLs are gettable and that the subscribe url is actually RSS.

Simply getting a page that doesn't have a feed, will generate an error.

So the logic appears to be:

- Create SimplePie object with URL provided by user.
- Any errors, crash out.
- Compare the permalink and subscribe URLs
- If the value passed in is not the subscribe URL, get it??? **No**, it looks like SimplePie automatically gets the RSS, so if it can't it would generate an error. Will need to test that. Yes, that's what happens

### Client side validation of URL

The form for registration uses Moodles formslib which in turn is based on the Pear library which has [some documentation](http://pear.php.net/manual/en/package.html.html-quickform.intro-validation.php) around validation.

Client side validation is generally done (I think) with the `addRule` method. Pear doesn't seem to support a URL type, but Moodle does.

That seems to have too much difficulty for now.

### Processing and allocating the feed elements

The last major task is to process and allocate items in the feed. This needs to be called on an individual blog when it is first registered, but also via cron at the fixed time.

Given a single student feed, the process is:

- Get the elements in the feed.
- For each element in the feed
    - Check to see if there is an existing feed in the database for this item, this is based on the permalink for the item stored in bim\_marking
    - If there isn't an entry, prepare to put one in.
    - Loop through each unallocated question for this student
        - If the post seems to match the question, modify the entry for the post.
    - Insert the new entry

Implementation and a need to re-use this code for the cron job that mirrors/processes registered blogs has resulted in a bit a re-factor. bim\_process\_feed( $bim, $student\_feed, $questions ) is up and going.

In terms of text similarity there appear to be a few in-built [PHP functions](http://www.php.net/manual/en/function.levenshtein.php) that might be helpful later on. This [Pear class](http://www.go4expert.com/forums/showthread.php?t=4189) could also be a great help.

### Get and test the cron updating

Okay, the cron code has been updated with the new methods. Rather than run from cron I want to see what's going on. So going to modify the default "config" page for a coordinator to run the cron function.

It seems to be working, but to be truly sure I need to start looking at some individual student entries and how they change. For that, I need to add the student search facility that is currently missing.

Delete a small number of entries from bim\_marking for students.

Run the cron thing to see if it works. Done.

### Student search facility

Coordinators need to be able to search through all students and view their details. A marker doesn't need to do this as they have a list of all their students shown and they can simply use the browser find facility. A coordinator, theoretically, has their own students as well as a responsibility to look after all students. Hence they need to be able to enter a student number and see their details.

Implementation plan:

- Add a "Find student" tab.
- Implement a simple form that takes details about students (try to do something like MyCQU in terms of making it simple).
- Display specific student details or a list of potentials to search from.
- Use the standard "student details" function to show the details.

Done, which is now bringing us back to the question of the item titles which is problematic because of the changes in what's being stored in the database...

### Limiting use of xml files - all in database

A difference between BIM and BAM is that BIM will be storing all posts made to the student feed in the database. BAM only stored posts allocated to questions. This caused two issues:

- The ability for markers to "unallocate" posts meant that there were some unallocated posts in the database. This starts to create a duplication/difference. Some unallocated posts are in the database, some are.
- Feeds don't always provide a history of all the posts. So some might be lost. Not really a problem with current use as most students didn't make enough posts.

By making the decision to put all posts in the database, there's a need to update some early design decisions that were made on the basis of the BAM design.

#### Add post title to bim\_marking

Because all the posts are going into the database. Need to add the title into the database table bim\_marking.

Done.