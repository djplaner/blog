---
categories:
- learninganalytics-elearning
date: 2013-11-03 11:14:50+10:00
next:
  text: Big data in education - part 2
  url: /blog/2013/11/03/big-data-in-education-part-1-2/
previous:
  text: BIM and broken moodle capabilities
  url: /blog/2013/11/01/bim-and-broken-moodle-capabilities/
title: Big data in education - part 1
type: post
template: blog-post.html
---
Yet another MOOC to start. This time ["Big data in education"](https://class.coursera.org/bigdata-edu-001/class/index) by Ryan Baker - one of the names that spring up often in the Educational Datamining field. A coursera MOOC.

### Week 1

Oh dear the audio from the video is not great, wonder how much of that my local set up.

Setting up the importance of EDM/LA with a quote from the editor of the editor of the Journal of Educational Psychology [from here](http://www.edweek.org/ew/articles/2010/12/13/15data.h30.html) that EDM/LA is

> escalating the speed of research on many problems in education

Source of methods is data mining, machine learning, psychometrics and trad statistics.

"Educational data is big, but it's not google-big"

Neural nets not used that much in this field because of context and "smallness" of data.

How big is big? Big data in education larger than classical education research. Big enough for differences in r2 of 0.0019 to come up routinely as statistically significant.

Oh, the prev/next buttons on the video aren't to go between slides in the slideshare, but to videos.

Key types of methods

- Prediction Develop a model that infers a single aspect (predicted variable) from a combination of other aspects of the data (predictor variables).
- Structure discovery Find structure and patterns "naturally" in the data.
- Relationship mining Discover relationships between variables.
- Discovery with models Take a model, combine with other as a component of analysis.

Some coverage of why EDM has been evolving recently.

RapidMiner 5.3 is the tool for this course.

### Regressors

Regressor - a model that predicts a number.

Training label - data set where you know the answer.

Each label has a set of features/other variables which are used to predict the label

Linear regression - variables of different scales requiring transformation. Different types of transformation (e.g. Unitization)

Regression trees

### Classifiers

The label is categorical - not a number.

Specific algorithms work better for specific domains. Useful algorithms in EDM:

- Step regression; Used for binary classification. Fit a linear regression function with arbitrary cut-off.
- Logistic regression; Binary classification. Logistic function generates frequency/odds of variably.
- J48/C4.5 decision trees, Explicitly deal with interaction effects.
- JRip decision rules,
- K\* instance-based classifiers

As advised, RapidMiner 5.3 installed. _Aside:_ like the start "page" for RapidMinor. Links to videos etc with an interface intended to help folk get started. Exactly the sort of thing BIM needs.

Interesting to note that they are using screenshots of what to expect, rather than actually using the software. The data mining with Weka approach - using the software - was better. Especially given the speed at which it's been skimmed through and especially given when the data set provided, doesn't appear to match the one being used. Ahh, that's because I've got the wrong data set, but where is the data set?

Oh, so we do need to install the Weka extension to do this. Would have been nice to have been told this up front. In fact, much of that wasn't that useful. At least not for indepth understanding. Built vague understanding of driving RapidMiner, but that's about all.

More "theory" - more classifiers

Decision rules - sets of if-then

Now onto a case study. This has some good value. Gives broader context.

Given the "we know you've had troubles" messages from the course staff it appears that the brevity of the RapidMiner introduction has hit quite a few people.

### The quiz

So now there's an assignment. Be interesting to see what they ask and how it connects with the lectures.

The quiz comes with the very American notion of the honor code.

So using rapidminer to analyse data sets. Interesting because the lectures treated this process as an after thought. They focused on the concepts with data mining and only quickly mentioned in passing the rapidminer techniques. Not a big leap, but not one that was telegraphed in the lectures as something you should be taking note of (see the above for the absence). So a bit of revision is called for (it's two days since I listened to the above lectures)

Thankfully they have PDFs of the slides. Still a bit of trouble in figuring out the interface, the meaning and purpose of all the operators. Also assumed the need to connect the "Read CSV" operator up to the input port - but not necessary. Let's see if the answer is correct?

Ahh, of course it doesn't appear that I get feedback on the first question until I've complete the whole quiz. Given the uncertainty around the use of RapidMiner this is problematic.

So the operators I'm using

- Read CSV - nice CSV import of the data.
- Set Role - to identify which column in the CSV is the label. What we're trying to develop a model that will help us predict.
- W-J48 - the Weka extension for the J48 algorithm to generate the decision tree (the particular type of model we're using).
- Apply Model - takes an already developed model and applies it to a data set.
    
    W-J48 just develops the decision tree (the model) using the CSV file we inputted as the training set. Apply Model applies that model to a data set to do some prediction, or in this case to test the performance.
    
    Note: I've gotten this mostly from reading the RapidMiner provided synopsis, not from the lecture (or at least what I remember of it).
    
    In this case, we're currently running Apply Model on the same data (I think). This is not good practice.
    
- Binomial Performance - generates a range of statistics about the quality of the model. It's performance.

Now they want us to exclude one of the columns (an attribute?). Import CSV seems a good place to do that - yes you can deselect a row.

That ran a lot slower. Wonder why? In all of this we're reporting the KAPPA value, through we're yet (based on my memory) yet to have a good explanation of what this is telling us.

Now exclude some more columns. Most of these appear not to be specific to the model - e.g. the studentid is not going to be something impacting learning.

Since all of these questions are building on earlier questions, the lack of immediate feedback on the earlier questions is becoming troubling. If I got the first one wrong, then all of these could be wrong as well.

Okay, let's use a different classifier. And another. And another. And another. Interesting past 40 seconds for one of these classifiers. 1m20s in total

And now onto cross-validation with the same example.

And then a question about the changes in the value of kappa due to the use (or not) of cross-validation. An important point, but not one that I thought was made all that explicit in the lecture.

All good - 11 out of 11. A little hit of dopamine from the success and the slightly unexpected nature of it. And so onto week 2.

The "interactive" part of these lectures are so focusing on simple sums. Not really addressing the big picture.