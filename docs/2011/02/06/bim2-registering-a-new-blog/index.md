---
title: "bim2: registering a new blog"
date: 2011-02-06 21:14:47+10:00
categories: ['bim', 'bim2']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

The following continues the coding of the bim2 process for registering and processing a new student feed. It's taken a couple of weeks, but it is working with only a few minor tweaks and nudges remaining.

Steps involved will be

- saving feed details to the database;  
    Not something I've in Moodle 2. yet.
- figure out how to process the feed;
- generate appropriate successful output;
- generate useful errors.

Most of these are going to reuse basic algorithms from bim, but will have to be re-written to fit with the changes in Moodle 2 and also the OO design for bim2.

### Save feed details

Main requirement is to update bimtwo\_student\_feeds with information about: number of entries, date of last post, blogurl and feedurl.

That was surprisingly easy.

### Handling errors

The possible situations with entry of new feeds include

- **DONE** It is a URL and a valid feed can be found;
- **DONE** It isn't a URL;  
    This is handled by the form and Moodle.
- **DONE**The URL points directly to a feed;  
    Handled using simplepie's features (e.g. get\_permalink)
- **DONE**It is a URL, but there is not feed associated with it;
- **DONE**There is a feed, but there are problems retrieving it.
- **DONE**There is a (purported) feed, but there are problems with the format of the feed.
- **DONE**The possibility that the user has entered some known "bad urls".  
    e.g. http://wordpress.com/ is a common entry, while it has an associated feed it is unlikely that a student will be using that.

All of the remaining uncompleted tasks (except the last) are handled by simplepie. The last one is a bim addition, which I think for now we'll postpone. So, have to update bim2 to display the simplepie errors "nicely".

Next, is to get bim2 to check for some standard wordpress.com mistakes. This is primarily historical and should probably be expanded if folk become aware of other common mistakes.

### Processing the feed

The factor that makes this task a little more difficult is that "processing the feed" will eventually be something bim will also have to do with all feeds. Since this can be quite a large list, it would be good for it to be efficient to work on all feeds, but also not duplicate between the register single and process all requirements.

Processing a feed basically means looking at what is already stored in the _bimtwo\_marking_ table and comparing that with what is in the most up to date version of the feed. If there are any new posts, then those posts need to be inserted into bimtwo\_marking and the bimtwo\_student\_feeds entry needs to be updated (lastpost and num entries).

In bim, this was done with a function bim\_process\_feed which takes the bim activity id, feed details and a list of the questions for the bim. The function then

- Uses simplepie to get the most recent version of the feed;
- Get the contents of the _marking_ table for the user (what posts for this user are already in the database)
- Creates a hash based on the link to each post within the database already that gives access directly to the contents of the marking database
- Uses that hash to identify the questions that haven't been answered yet.
- For each of the items in the feed
    - Checks to see if it is already in the database via the hash.
    - If not
        - Converts the content of the message to UTF-8
        - Loops through all the questions to see if it is an answer to a question.
        - Inserts it into the database.
        - Updates the lastpost and numentries variables (for later update)

There might be some speed increase if the database insertion was held off until the end and done all in one, but am not going to play that game. Need to think about how this can be implemented.

How's this 
```php
$process = new bimtwo\_process\_feed( $this->bimtwo, $this->feed, $questions, $this->simplepie ); 
$process->process\_feed(); 
$this->update\_feed\_details( $process ); 
```

A new class solely for processing the feed. This same code can be re-used when processing all feeds as when processing a single feed. The first three parameters are necessary: the id of the bim activity (bimtwo), the URL for the feed, the array of questions set for this activity, and an optional simplepie object.

The idea is that without the simplepie object, this class would construct its own simplepie object and use it to process the feed. When registering a single student feed, we already have a simplepie object, so wish to avoid the overhead of re-creating it. We won't have this when working on a list of feeds.

Okay, that's all working. In the end, the "update\_feed\_details" function is removed.

### Forms and redirection

The question I'm looking at now is how to handle the "success" case. i.e. the form with the new blog url is submitted and all the processing complete successfully. Want to display some sort of success message and then show the details of the results of the processing. i.e. the normal default page for the student, but with a success message.

It looks like I should use a redirect, but perhaps with an extra parameter to indicate successful registration which is then used by the existing code. I think that's the way to go. How to do the redirect/formulate the URL.