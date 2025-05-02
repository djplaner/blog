---
title: Getting started with NVivo
date: 2014-01-14 15:39:07+10:00
categories: ['edc3100', 'nvivo']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Analysing some course evaluation comments | The Weblog of (a) David Jones
      author_email: null
      author_ip: 66.155.38.68
      author_url: https://djon.es/blog/2014/01/15/analysing-some-course-evaluation-comments/
      content: '[&#8230;] analysis was used as an initial exploration of using NVivo.
        The method used [&#8230;]'
      date: '2014-01-15 11:34:05'
      date_gmt: '2014-01-15 01:34:05'
      id: '929'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
What follows is some initial explorations into the use of [NVivo](http://www.qsrinternational.com/products_nvivo.aspx) for the qualitative analysis of content. I'm going to use the task of [analysing student comments](/blog2/2014/01/13/evaluating-edc3100-in-2013-step-1/) from the evaluation of a course as a test case.

**Aside:** Just been told that "raw" data (i.e. de-identified course evaluation data with responses grouped by student) "is not given out in any form". So rather than having useful data to import easily, I'll have to kludge up the importation of some hamstrung data.

## Start with the question(s)

As with all good research, I'll start with the questions I want to answer with this analysis.

1. What themes do the student comments cover?
2. What themes are the most prevalent?
3. Is there any difference between offerings or mode of delivery (on-campus, which campus, online)?

(Remember, the aim here is mostly to learn Nvivo so the limitations of my "research" questions are noted)

## Sourcing assistance

I was going to include both help from Nvivo and the broader web, but so far the [NVivo documentation](http://help-nv10.qsrinternational.com/desktop/welcome/welcome.htm) is providing sufficient. Though as you get deeper into it

On first glance, it appears NVivo comes with some significant help. Help that seems to be well designed (at version 10 of the product you'd hope they'd built up some expertise). Nice and very early introduction of sample research projects and how you'd go about doing that research. I'll borrow some of that for the process below.

### Key concepts

All systems have some abstractions they use. Nvivo is no different. The nice "[understand the key concepts](http://help-nv10.qsrinternational.com/desktop/concepts/Understand_the_key_concepts.htm)" section seems to list four (only four?)

1. Sources - the (multimedia) stuff you're analysing
    - Internals - the sources that can be imported into Nvivo.
    - Externals - those you can't import.
    - Memos - the place you store your insights about the analysis
    - Framework matrices - to summarise source materials.
2. Coding and nodes - you code your source material into nodes. Provides access to all the references to that node.
    
    Appears this can be hierarchical
    
    Includes "case" node to store attributes. Often used to identify people/places. Classification sheets used to view the values for these nodes.
    
    Nodes can be organised into folders.
    

4. Node classifications - apparently intended for "demographic attributes".
5. Source classifications - using case nodes to manage bibliographic data

### Sources

Sources/data can be organised using folders (recommended for the start), sets (used later to gather sources/nodes from different folders) and search folders (?). Also source classifications to organise/compare based on attributes. e.g. book, journal article, web page.

## Create a project

Enough reading. Let's get going. Some of the following is initial exploration, confirming assumptions drawn from the help material in the actual tool.

Hit the new project button enter title, description, accept the default filename. Mmm, user actions can go to an event log - transparency/repeatability measure I assume. Leave it off for this play.

Ok, a window where I can recognise the point of most elements. Let's see if I can create a node. Yep, but I want it to be a case node, can't figure out how to change it to that. Ahh, I need to create a classification first. ANd I also need to take care of the type of node. Mm, might wait on doing this until we think things through a bit.

## Import some data

Given the inability to get the data in a manipulable format, I need to kludge something out of the institutional web interface.

To remind myself, the main survey had

- 8 closed questions; and,
    1. Overall, I was satisfied with the quality of this course.
    2. I had a clear idea of what was expected of me in this course.
    3. My learning was assisted by the way the course was structured.
    4. My learning was supported by the course resources.
    5. I found the assessment in this course reasonable.
    6. I received useful feedback in this course.
    7. The teaching team supported my learning.
    8. Overall, I was satisfied with the quality of teaching in this course.
- Four open questions
    1. What did you find were the most helpful/effective aspects of this course?
    2. What did you find were the least helpful/effective aspects of this course?
    3. What improvement would you suggest to the course itself?
    4. Please feel free to make any other comments, particularly in relation to your ratings for this course
- And a couple of optional closed questions, for semester 2 these were (pick which question I selected - from a pre-approved list - and which the institution included).
    1. It was easy to navigate my way around the StudyDesk.
    2. You may have completed previous USQ student surveys in the past. Is this new set of questions an improvement? Please ignore this question if this is the first time you have completed a USQ student survey

For each of the closed questions there was also an option for students to provide some free text responses.

The web interface I have access to will provide the following associations

- For each closed question, it shows a list of any textual responses for that question (with the numeric response) plus the option to expand out all the other free text responses made by that student.
- For each open question, a list of the textual responses plus the option to expand out all other free text responses made by the student.

Theoretically possible to combine these two to get a better picture, but it would be manual and also plagued by the issue of not all students answered all open questions.

So the best option for the purposes of this exercise may be to select one of the open questions (hopefully one most students answered) and copy and paste those responses into a Word document. Then rely on Nvivo's data wizards to import and separate responses by question and student. So the format would be something like

- Chosen question - What did you find were the most helpful/effective aspects of this course?
    - Students response to this question - The quick responses from the teaching team.
        
        And for each of the other open questions the student responded to.
        
        - Question text: What did you find were the most helpful/effective aspects of this course? (yes it duplicates)
            - Student response: The quick response from the teaching team.
        - Question text: My learning was supported by the course resources.
            - Student response: Sometimes was frustrating that assessable course material was added after I had completed the weeks work (5/5)
                
                **Note:** the numeric response from the student for this comment on one of the closed questions.
                

Copy and paste this into word and play with paragraph styles might work? Of course the copy and paste is ugly. The manual conversion with macros is doable for this test. The question is whether Nvivo will auto-import?

Have the data file in the format. Create a node for the offering. Import the external data as a source. Do the auto-coding and hey presto. Imported correctly!!! FTW.

Concept proved. Now I need to develop the appropriate strategy to import the sources.

## Planning the analysis

The following is an attempt to plan out the process I'll use. Just for once, having planned it all out first, prior to starting might be an idea. The following process is loosely adapted from the [Nvivo help docs](http://help-nv10.qsrinternational.com/desktop/concepts/using_nvivo_for_qualitative_research.htm#MiniTOCBookMark4)

1. Set up the project - research design, project journal, and make a model.
    
    Going to leave this until later. This isn't really a research project.
    
2. Import that data organised by folders.
    
    The data I'll import will come in two forms
    
    1. Word documents for open question responses.
        
        For each mode I'll create a Word document by copying and pasting from the web application. The responses will be grouped by student identified by a code and use paragraph formatting so I can use the auto-coding feature.
        
    2. Spreadsheets for closed question responses and "demographics".
        
        Each mode will have it's own spreadsheet that contains information about the students. This will include: the year, semester and mode of them taking the course; and, their responses to the closed questions. Note: it will only include responses for those closed questions where the student provided a comment (the limitation of the data).
        
3. Node structure and coding
    - Does a word frequency query reveal anything?
    - Use an initial list of nodes including: negative, positive. The rest I'll leave open.
4. Set up nodes for people, places etc.
5. Explore the material and code themes.
6. Run a matrix coding query to see about prevalence of themes.

### Prepare the data

Need a test run of the data and its importation. The process is to

- Word document
    - Select the open response question that has the most responses on the assumption we'll get the most data.
        
        Significant problem here as not all students respond to all open questions. So even picking the open question with the most responses, I may be missing the data. God I hate badly designed systems and institutions that don't recognise the importance of rapid response.
        
    - copy and paste without formatting into Word.
    - change the paragraph formatting to the following
        - H1 - student identifier
        - H2 - the text of the open question.
        - Body - the student's response.
    - Replace the student identifier with code - _NUM_\-_YEAR_\-_SEM_\-_MODE_ where
        - _NUM_ = unique number starting at 1 and incrementing.
        - _YEAR_ = the year (duh)
        - _SEM_ = 1 or 2 representing the semester
        - _MODE_ = one of the following representing the mode of delivery: Toowoomba, Fraser Coast, Springfield, Online.
- Spreadsheet
    - Create columns: Student,Semester,Year,Mode, SEC01, SEC02, SEC03, SEC04, SEC05, SEC06, SEC07, SEC08.
        
        Student will the be the id from the Word document. Yes the id will duplicate the next three columns, but I'm assuming this might be needed to allow manipulation by NVivo and ease of understanding by human beings.
        
        SEC01 etc are the ids used by the institutional system for each of the closed questions. These will be used to hold the student's response to these questions if it is available from the Word document.
        
    - For each student add a row from the Word doc.

Okay, let's try this.

- Both files created for the smallest sample of students (n=11)
- Import the word document into NVivo - no worries.
- Import the spreadsheet - counts as a [data source](http://help-nv10.qsrinternational.com/desktop/concepts/about_dataset_sources.htm) (perhaps).
    
    Can choose columns to be classifying or codable fields. In this case, I believe I'm looking at classifying fields.
    
- Set up the "respondent" classification.
- Set up the positive/negative nodes initially, also a node for the specific offering (overkill?).
- Auto create the nodes from the document - done.
- Classify the student nodes as "Respondents".
- Fill in the attribute values for the student nodes?
    
    Actually, that happens automatically when importing the spreadsheet. The label for the first column becomes the name of the classification and the value (as I'd hoped) gets linked with the content node.
    
- Let's do a bit of manual coding for positive/negative.
    
    Figuring out the mechanism for coding is surprisingly more difficult that I expected.
    
    Didn't take long looking at the responses to think about "Suggestion" as another category/node. All done, not a bad process.
    

## Current status

The basics of NVivo learnt. Some possible limitations for certain activities identified. But there will be work arounds. More on what the evaluation revealed (not a lot new) tomorrow.