---
categories:
- bim
date: 2009-12-24 12:00:46+10:00
next:
  text: BIM - the show student posts screen
  url: /blog2/2009/12/26/bim-the-show-student-posts-screen/
previous:
  text: BIM - minor fixes to show student details
  url: /blog2/2009/12/24/bim-minor-fixes-to-show-student-details/
title: BIM - Staff show details screen
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: BIM &#8211; the show student posts screen &laquo; The Weblog of (a) David
        Jones
      author_email: null
      author_ip: 72.233.96.150
      author_url: https://djon.es/blog/2009/12/26/bim-the-show-student-posts-screen/
      content: '[...] The Weblog of (a) David Jones Another voice in the blogosphere    &laquo;
        BIM &#8211; Staff show details&nbsp;screen [...]'
      date: '2009-12-26 13:08:10'
      date_gmt: '2009-12-26 03:08:10'
      id: '2907'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
This post documents the creation/completion of the BIM show details screen. This is used by staff to get a summary of their student details, whether they have registered their feed, made posts etc.

The BIM design will be based on the [equivalent BAM screen](http://www.flickr.com/photos/david_jones/3268716654/in/set-72157608613577424/) with some slight modifications. For example, I don't believe Moodle will have the equivalent of the Webfuse "Photo Gallery" or "email merge" facilities.

The post is starting to evolve into a semi-standard structure that I think I'll use with the other screens. Will see how that goes. The structure at the moment is:

- Identify all the data required for the screen.
- Specify any questions about the implementation I have.
- Document what I did to get the data.
- Document what I did to get it showing in the browser.

### Data that is required

To implement this screen, the code will need to retrieve the following data

- The list of students who the staff member is responsible for marking.
- User details about the staff member (name etc).
- User details about the students.
- Information for the students from `bim_student_feeds`
- Identify which of the marker's students haven't registered their feeds.

### Questions

- Staff (not course coordinator) have two main screens for BIM: show details and show posts. Should I implement these as tabs? **Probably yes**  
    The coordinator will have an additional screen to configure the BIM activity, this could be represented using an additional tab.
- Does the coordinator/teacher/student switch in view.php work with the test data?  
    It seemed to work before. If I'm going to write this screen, I need to login to Moodle as a teacher, but not coordinator. It works as expected. Little wins are good wins - well they are better than loses.

### Get the data

Basically this should document the points identified in the data section above.

#### Staff members students

Need to know which students the staff member is responsible for marking.

For the purposes of testing this is being held in the table `bim_markers_students` because I'm uncertain how the local Moodle instance will populate this information. Eventually, I'm assuming it will be part of the groups features. I can update the code then.

Rather than separate out getting the list of student usernames and then their details. Let's combine all this into the one function `bim_get_markers_students( $bim, $userid)`

Ahh, but of course, I've created the table markers\_students using the course, not the BIM. As this was how BAM worked (sort of). This means `$bim` will need to, in the short term, be replaced with the course id.

DONE: currently returns an array of user details for all the markers' students with the key being Moodle user id.

#### User details for markers

This is a quite straight forward use of Moodle database API.

#### Student information from bim\_student\_feeds

Need to take the student ids from the array above and get the information for the students from bim\_student\_feeds.

```
$student_ids = array_keys( $student_details );
$feed_details = bim_get_feed_details( $bim, $student_ids );
```

#### Identify which students haven't registered

This is essentially find all those students in `$student_details` that don't have an entry in `$feed_details`. The question is, does PHP have some in-built functions that might help with this? A simple for loop and an 'exist' function could do this. Do I worry about going further?

This [page](http://www.w3schools.com/PHP/php_ref_array.asp) suggests that the function `[array_diff_key()](http://www.w3schools.com/PHP/func_array_diff_key.asp)` might be what I'm looking for.

However, the trouble is that `bim_get_feed_details` is returning an array with keys being the feed id, not the student id. Need to update that.

That's working.

### Get it producing in the browser

Time to get it working in the browser.

Will leave the question of the tabbed interface until the next bit of work. Will focus on getting this screen working. There are going to be two main sections to this screen:

1. Registered feeds.
2. Unregistered.

The course description section that is in the BAM version of this screen can be forgotten, I believe, as BIM is working within the course Moodle site.

This is essentially showing a bunch of data in a table. Can do this in for loops, but surely there's a quicker way in Moodle. Seems I need to dig into weblib.php again. Of course, `print_table`. Will need to manipulate the data to use it.

That's working, at a basic level. More work to be done includes:

- Look at alternating row colours to improve layout/appearance.
- Figure out how to display the date/time properly, in this case number of days ago.
- Add in the red/green/yellow for the cases where the last post was a while ago.
- Modify URL for live blog to some HTML.
- Left align the headers.
- Left align the other numeric columns.
- Add the ability to sort by columns.

I now learn about `tablelib.php` that specifies a `flexible_table` class.

### Current status

Have got flexible\_table working somewhat. The sorting isn't working appropriately, the display of columns etc needs some work, but the data is being displayed.

Doing a similar thing with the show posts screen should be fairly simple and somewhat similar. Probably pay for the next step to be to finish these screen and get the tabs working, before duplication for show posts.

Time to go home on Xmas eve.