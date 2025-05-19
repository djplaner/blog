---
categories:
- bim
date: 2010-02-03 15:37:46+10:00
next:
  text: '"BIM - Tidy up #4 - Getting ready for user testing"'
  url: /blog/2010/02/04/bim-tidy-up-4-getting-ready-for-user-testing/
previous:
  text: Loosing weight, nudging and changing the L&#038;T environment - early foundations
    of my work
  url: /blog/2010/02/03/loosing-weight-nudging-and-changing-the-lt-environment-early-foundations-of-my-work/
title: '"BIM - Tidy up #4 - Security checks"'
type: post
template: blog-post.html
---
The last tidy up of BIM resulted in some fairly major code changes as early design assumptions were over-turned in favour of more PHP/Moodle like approaches, not to mention general better design/structure. This tidy up turns to some of the more "housekeeping" types of tasks. This one seeks to ensure that BIM follows all of the security guidelines as [suggested on the Moodle site](http://docs.moodle.org/en/Development:Security)

### Auth and capabilities

- require\_login course is used **check**
- has\_capability called early. **check**

### Forms

- Use moodleforms wherever possible **check**  
    There are 7 forms in BIM
    - allocation\_form.php
    - coordinator/find\_student\_form.php
    - coordinator/marker\_allocation\_form.php
    - coordinator/question\_form.php
    - marking\_form.php
    - mod\_form.php
    - ./student/register\_form.php
- setType method for each field
    - allocation\_form.php **check**
    - coordinator/find\_student\_form.php **check**
    - coordinator/marker\_allocation\_form.php **check**
    - coordinator/question\_form.php **check**
    - marking\_form.php **check**
    - mod\_form.php **check**
    - ./student/register\_form.php **check**
- use optional\_param/required\_param **check**
- Clean data from external sources - RSS Feeds  
    I'm using SimplePie to retrieve all the feeds. I'm assuming this does the job of cleaning. I would hope so. This will need confirmation

### Output

[more information](http://docs.moodle.org/en/Development:Output_functions)

- Use **s** or **p** to output plain text
- use **format\_string** for minimal HTML
- use **format\_text** for all other content
- use stripslashes on data from option\_param or required\_param if being outputed

There's also the question here of some of the internationalisation stuff that I need to include.

Currently, I'm simply using "print". Source files using print include:

- coordinator/allocate\_markers.php **check**
- coordinator/find\_student.php **check**
- coordinator/manage\_marking.php **check**
- coordinator/view.php **check**
- coordinator/question\_form.php **check**
- lib/bim\_rss.php **check**
- lib/locallib.php **check**
- marker/view.php
- marker/allocation\_form.php **check**
- marking\_form.php
- student/view.php

Adding in language support is interesting. Not a lot of examples. Having to use some arcane greps and finds to discover examples and try to deduce from there.

### Log every request

Use **add\_to\_log**

The major requests for BIM are:

- Coordinator **Check**
    - Configure BIM
    - Manage and change questions
    - Allocate markers
    - Manage marking
        - View students in various states
        - Release results
    - Find student
    - Your students
        - student details
        - post details
        - reallocate post
        - Mark post
- Marker **CHECK**
    - student details
    - student post details
    - reallocate post
    - Mark post
- student **CHECK**
    - view details
    - try to register feed