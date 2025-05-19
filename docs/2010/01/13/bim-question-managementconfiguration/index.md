---
categories:
- bim
date: 2010-01-13 21:57:08+10:00
next:
  text: BIM - Manage Marking
  url: /blog/2010/01/17/bim-manage-marking/
previous:
  text: Another idea for research project arising from the indicators project
  url: /blog/2010/01/12/another-idea-for-research-project-arising-from-the-indicators-project/
title: BIM - question management/configuration
type: post
template: blog-post.html
---
A central assumption in BIM is that student contributions to their feeds are, at least in some part, intended to respond to questions or activities that have been created to encourage reflection and other good stuff. This requires that the teaching staff using BIM have a mechanism for creating and changing the questions students will respond to. This post describes the initial implementation of this screen.

This will be implemented using Moodle's formslib and borrow on work already done. It should be fairly straight forward.

### Required data

Just about the only data required will be all the data associated with the particular BIM activity within the `bim_questions` table.

Will also want to include some statistics about how many students have answered, marked and released responses to these questions. This is to give staff some warning that they may not wish to delete a question for which people have already provided answers.

### Get the data

Already have `bim_get_question_hash`

Need to generate stats about posts for a list of marking\_details. This isn't exactly what we want. Need generate stats for each question.

Add function `bim_get_question_response_stats` which will :

- take an array of all the questions we're interested in.
- add a field `response_stats` for each question which is an array with keys matching status and values matching number of responses in the bim\_marking table.

### Show the data

This is going to be a single form with a set of elements for each question. For each question want:

- The title as a text element.
- The body of the question in a HTML editor.
- The min and max marks in separate text elements.
- Indication of the statistics of student posts for that question.

Want the coordinator to be able to:

- Add a new question.
- Change the values for an existing question.
- Delete a question?  
    In terms of safety, I don't think we actually want to delete data from the database in response to this. Simply make it not visible to most users.

Any changes to a question, once students have answered the question could be a bad thing, but it is something we want the user to be able to do.

Okay, the form is up and showing the data. Time to process the data when the form is updated. The process for this will be something like:

- If there is anything in the "add a question" then have to add a new entry into bim\_questions.
- If any of the existing questions have changed, then have to update those entries.
    - Loop through each question.
    - Compare the content of the question from the database with the content from the submitted form.
    - If there is a change, add the question (minus stats) to another array.
    - At the end of the loop use update\_record with the other array to update the database. **DONE**

Essentially got add working, but need to clear the form and re-load the questions afterwards to get correct performance this will require some re-factoring of the function to remove duplicated code.

Well, according to [this thread](http://moodle.org/mod/forum/discuss.php?d=123618) it appears that you can't do this. So, I've had to go with the redirect route. Done and working.

Last steps to be done:

- Check that the addition and modification is working.
- Add in rules into the form for basic checking. e.g. (complete this in the cleanup at the end)
    - All elements of a new post must be provided - also with existing.
    - min\_mark must be less than max\_mark
    - There shouldn't be duplicate questions (title and body)
    - Maybe treat duplicate title as a special exclusion.
- Add the capability to delete a question.
    - Add a check box to each question.
    - Detect the check box on submit and delete the question.
    - Ask for confirmation?

### What's been done

Essentially the management of questions is working. It's not tidy and complete in terms of full validation of inputs and a few other niceties, but those can wait.

On to the "Manage Marking" screen I believe - viewing markers, marking progress and releasing results.