---
title: BIM - talking to the gradebook
date: 2010-02-07 21:35:58+10:00
categories: ['bim']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: 'BIM &#8211; Tidy up #4 &#8211; Getting ready for user testing &laquo; The
        Weblog of (a) David Jones'
      author_email: null
      author_ip: 72.233.104.49
      author_url: https://djon.es/blog/2010/02/04/bim-tidy-up-4-getting-ready-for-user-testing/
      content: '[...] Gradebook stuff. &#8211; moving to another post [...]'
      date: '2010-02-07 21:39:06'
      date_gmt: '2010-02-07 11:39:06'
      id: '2926'
      parent: '0'
      type: pingback
      user_id: '0'
    
---

See also: [[blog-home | Home]]

One of the bigger tasks left to do is to integrate BIM with the gradebook. Some [initial exploration](/blog2/2010/01/26/bim-sending-results-to-the-gradebook/) has been done, this post seeks to document the initial implementation.

This implementation is going to be quite simple, and perhaps simple minded. The less than straight-forward nature of the task of finding information about how to do this and the reducing time available are the main reasons for the simple approach. Potentially, the simple approach might also help the academic staff driving it.

### Initial design

As posts are "released" by the coordinator, the marks will be added to a column in the gradebook that matches the name of the BIM activity. i.e. this will be simple addition. In terms of scaling etc. it will be up to the teaching staff to use the gradebook features to do this.

At best there should be an option to include in the gradebook.

### Implementation

#### Add option to include results in gradebook

- Modify the bim table with new field.
- Modify mod\_form.php to have field.
- Modify lib.php functions to appropriately modify the database appropriately.
    
    **TO DO:** Modify add\_instance to include a call to grade\_update to add the item to the gradebook.
    
    Borrowing a lot from existing modules.
    

Question arises: what happens if the gradebook option is added after some results have been released? Should BIM:

- Not allow changing.
- Allow coordinator to "reset" gradebook for all currently released results?

#### Add the results

- Modify the "release" posts function to update the gradebook.
    
    **TO DO:** If the appropriate option is set, then call grade\_update to change the entry.
    
    Have initial code in place. Doesn't seem to be updating correctly. Need to look at this more. Subsequent additions of marks, not summing up?
    

A simple testing process for this:

- Register feeds for 3 students in the one course.
- Allocate posts to a few questions for each.
- As an iterative process
    - Mark one or two, check gradebook, release one or two, check gradebook, repeat
- Repeat for another course, observe.

Initial testing of releasing 2 students with 2 of the same questions, works fine. All in gradebook as expected.

More questions/students seems to work.

Go to another course, without creating questions and register a couple of student blogs. Now, create the questions and run the bim\_cron function. Yep, that works like a charm. Now back to gradebook.

Adding BIM to gradebook after initial addition is working. Can I release and add marks to it? Oops, yes, but it adds another entry!!!! Bugger. Will it do it again? Nope. and it works.

**TO DO:** fix the problem with an update of BIM adding Gradebook followed by release resulting in 2 columns, not one.

Problem with bugs introduced in the update\_instance method. Fixed and working.