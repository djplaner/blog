---
title: Fixes to BIM
date: 2010-02-25 10:20:48+10:00
categories: ['bim']
type: post
template: blog-post.html
---
Prior to [BIM](/blog2/research/bam-blog-aggregation-management/) being installed and used at my current institution it had to be checked by folk at NetSpot. The following details what I've had to do in response to that.

All of the changes are fairly minor, some won't be changed as I don't see the point and don't have the time. Shall be interesting to see how that goes down.

Especially, given that the evaluation response to the following two questions

- Can the plugin be deployed in its current state without first applying fixes?
- Considering any Security/Maintenance issues identified above would the decision to install and support this plugin contain acceptable risks to NetSpot or the client?

Was YES!

### Left over debug stuff

- references to localhost
- reference to brisbane

### Getting a list of students

The advice is

> Getting a list of students should be extended to a selectable select of roles instead of hard code role

Actually moved this to using get\_users\_by\_capability.

### Paging

Essentially, where lots of database records are going to be displayed the request is to "page" the results to minimise load.

In particular, the suggestion is to introduce paging for

- Find student - There is a hard-coded limit within the code that restricts find student to getting 200 student records.
- Your student - Limited to what staff are allocated to. Could, theoretical be the entire course, which could be large.

Will leave this as is. This is only getting a few records of data per student. Shouldn't be a great load and will take a fair bit to modify the code.

### Logging

Apparently my use of "add\_to\_log" is somewhat off. Not surprisingly as it was a learning process and a bit of cut and paste went on.

Two problems are currently apparent:

- a missing $ sign for cm->id
- possible wrong parameters being sent to the URL related to this.

### Custom HTML

A couple of the forms I use have some custom HTML in them. i.e. rather than use the Moodle forms constructs it outputs some HTML.

I can see the point in having this, but it's not a strong point. It's using HTML tables for layout which does break one of the aims of Moodleform. But I also would like to save the time it takes me to figure out how to achieve the look I need for these forms with just the Moodleform stuff for other tasks that are a little important.

However, I can see some folk being anal about this. May have to come back to it.

### Backup and restore

As per an earlier post this is not 100% complete. Will have to complete it, eventually. At the moment back up of questions does work. This is the main functionality required to roll over courses, the immediate need.

### The zip file

The zip file I uploaded was a bit confused in terms of having two copies of the bim code, one in a sub-directory.