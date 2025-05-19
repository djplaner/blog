---
categories:
- bad
- concretelounge
- edc3100
date: 2015-07-01 13:33:26+10:00
next:
  text: Can the Moodle book module be made open and other enhancements
  url: /blog/2015/07/03/can-the-moodle-book-module-be-made-open-and-other-enhancements/
previous:
  text: And the little one said, &quot;roll over, roll over&quot;
  url: /blog/2015/06/26/and-the-little-one-said-roll-over-roll-over/
title: Re-building results processing
type: post
template: blog-post.html
---
It's once again time to process final results for a course and return the final assignment. A process that involves

1. Checking overall student results for a course, before returning the final assignment.
2. Identifying all of the students who won't have final results available by the required date.
3. Analysing this offering's performance across the course and comparing it with prior offerings.
4. Returning the final assignment.
5. Ensuring the overall results are entered appropriately into the student records system.
6. Preparing a report for the examiners meeting.

There are three problems driving this

1. What institutional processes/tools are provided to help with these tasks are far from user friendly.
    
    e.g. the greasemonkey script I wrote last year to help with task #5 above.
    
2. There are no institutional processes/tools for some of these tasks.
    
    e.g. the only way to get all of the assignment marks into one place is to put them into the Moodle gradebook. But I believe if I do that then the students can see the marks. Given that I'm still moderating the last assignment marks them seeing the marks is not so good.
    
3. The management of online assignment submission has changed this year, so some of prior workarounds are no longer viable.

### What I used to do

Part of this activity is identifying what I've already got. It's around 7/8 months since I last had to do this, so I don't remember. I'm not sure the impact of this temporal distance is something that the designers of institutional systems and processes are fully cognisant of.

The old process appears to have been

1. Extract individual CSV files for each assignment from EASE. The old online assignment system generated 2 separate CSV files. I needed both.
2. Get another CSV file with Professional Experience results. Whether a students has passed their Professional Experience is determined by another part of the institution using a different system.
3. Run a perl script which would
    1. Extract all the data from the CSV files.
    2. calculate the final results (for each student).
    3. Assign a grade to the student based on circumstances
        - FNP if at all assignments not submitted.
        - F regardless of mark if PE failed.
        - IM if PE mark has not yet been received
        - RN if assignment submitted but still being marked.
    4. Generate grade breakdowns for each campus and overall
    5. Output all that as a CSV file, including comments that I'd added
Import that into Excel and do some further checking.

### What I need to do

The process will be largely the same. The main difference is the source and format of the CSV files. The changes now are

1. Assignment 1, Assignment 2 and PE marks are now in Moodle gradebook. The will all export nicely. Though it does use the long version of the USQ student number. May need to do a workaround for that.
    
    what sort of institution is silly enough to have at least 3 versions of the same student number?. Long with leading 0s. Long without leading 0s. Short!
2. Assignment 3 mark will be in Moodle assignment activity. That will work. The grade is there.
    
    But yet, it uses a different version of the student number (long without leading 0s). But both do have email address, that might be the candidate for unique id. Or the script will just pre-pend leading 0s.

The other major difference is that neither of these CSV files include any mention of the campus or mode the students are using. Which prevents breaking results down. But thankfully I do have database table populated with this information.

Ahh, that's right. I also have to change the PE mark for some students to -1 to indicate they were exempt. This is to discern students for whom there is no PE result yet, from those students who aren't going on PE and should still pass.

My other problem is that the CSV file for A3 has a "status" field that includes new line characters. My poor little Perl CSV parsing module doesn't handle that well.

It's working well enough to help moderate A3 results. Time to do that.

Still to be done

- Modify gradebook.csv to have -1 for PE for those students who will never go \*\*\*\* what about when it's updated?
- Add the campus calculations back in
- Figure out how to handle the status field in Moodle assignment csv.
- Have the script produce an Excel file, not a CSV file