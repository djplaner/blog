---
categories:
- learninganalytics-elearning
date: 2013-11-03 23:18:51+10:00
next:
  text: BIM for Moodle 2.5
  url: /blog/2013/11/06/bim-for-moodle-2-5/
previous:
  text: Big data in education - part 1
  url: /blog/2013/11/03/big-data-in-education-part-1/
title: Big data in education - part 2
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: elketeaches
      author_email: elkeclarissa@hotmail.com
      author_ip: 124.189.216.206
      author_url: http://elketeaches.wordpress.com
      content: you lost me at "data insult", lol
      date: '2013-11-05 07:46:33'
      date_gmt: '2013-11-04 21:46:33'
      id: '900'
      parent: '0'
      type: comment
      user_id: '0'
    
pingbacks:
    - approved: '1'
      author: Big data in education - part 1 | E-Learning-Inc...
      author_email: null
      author_ip: 89.30.105.121
      author_url: http://www.scoop.it/t/e-learning-inclusivo/p/4010361457/big-data-in-education-part-1
      content: '[&#8230;] And now onto Week 2 of the Coursera MOOC &quot;Big Data in Education&quot;.
        Focusing on the evaluation of models - is it any good? Detector confidence Sadly,
        the audio for the first week&#039;s problem with buzzi...&nbsp; [&#8230;]'
      date: '2013-11-04 01:05:55'
      date_gmt: '2013-11-03 15:05:55'
      id: '899'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
And now onto Week 2 of the Coursera MOOC ["Big Data in Education"](https://class.coursera.org/bigdata-edu-001/). Focusing on the evaluation of models - is it any good?

### Detector confidence

Sadly, the audio for the first week's problem with buzzing.

Classification - predicting a categorical label.

Value of knowing the certainty of a model's prediction - confidence matters.

Uses of detector confidence

- Gradated intervention - cost/benefit can be used to judge (assuming you know things like - how much learning in a minute)
- Discovery with models analyses

Not all classifiers provide confidence. Some provide pseudo-confidence. Some straight forward.

The confidence provided is based on the initial data.

### Diagnostic Metrics

Metrics for classifiers.

- Accuracy (aka agreement in inter rate reliability)
    
    Not a good measure. e.g. not unusual to say 92% of students pass Kindergarten - if the detector says PASS always will get accuracy of 92%.
    
- Kappa
    
    Percentage of progress from expected agreement to perfect.
    
    Interpreting Kappa is not easy. A negative value of Kappa suggests your model is worse than chance. Seen commonly with cross-validation. Your model is junk.
    
    Between 0 and 1 harder to judge. **Typically 0.3-0.5 is considered good enough to call the model better than chance and publishable**
    
    Some ed journals want 0.9
    
    Why no standard? 0.8 is sometimes used as a magic number. Kappa is scaled by the proportion of each category - the data set influences outcomes.
    
    Comparing Kappa values between data sets is not great. If the proportions of data sets can make it okay, informally.
    

And now a quiz to calculate kappa didn't really pay close attention to the formula - it made sense. So, let's jump to the lecture PDF - to painful to do it in the video. So Kappa is

**Update:** After struggling through the following I'm not confident that the slides give a good grounding to do this calculation. I got the Kappa calculation correct on the final week quiz by working through the example on [the Wikipedia page for Cohen's Kappa](http://en.wikipedia.org/wiki/Cohen's_kappa).

(Agreement - Expected Agreement ) (1 - Expected Agreement )

|  | Detector - Insult during collaboration | Detector - No insult |
| --- | --- | --- |
| Data insult | 16 | 7 |
| Data - No insult | 8 | 19 |

Agreement = 16 + 19 = 35%

Data

- Expected frequency for insult = 23
- Expected frequency for no insult = 27

Detector

- Expected frequency for insult = 24
- Expected frequency for no insult = 26

Expected no insult agreement = 0.27 \* 0.26 = 0.0702 Expected insult agreement = 0.23 \* 0.24 = 0.0552

Expected agreement = 0.0702 + 0.0552 = 0.1254

(Agreement - Expected Agreement ) (1 - Expected Agreement )

(0.35 - 0.1254 ) (1 - 0.1254 )

0.2246 0.8746

0.2568..... which is not the answer but I guessed the answer closest (0.398) and got it right. Have checked but can't see what's wrong. The assumption is the percentage calculation. This is something that isn't clear or apparent in the lecture.

Oh joy, another one. Let's try the percentage

|  | Detector - suspension | Detector - no suspension |
| --- | --- | --- |
| Data - suspension | 1 | 2 |
| Data - no suspension | 4 | 141 |

n = 1 + 2 + 4 + 141 = 148 Agreement = 1 + 141 / ( 100/148) = 95.95%

Data

- Expected frequency for suspension = 3 = 2.02%
- Expected frequency for no suspension = 145 = 97.97%

Detector

- Expected frequency for suspension = 5 = 3.37%
- Expected frequency for no suspension = 143 = 96.62%

Expected no suspension agreement = 0.9797 \* 0.9662 = 0.947 Expected suspension agreement = 0.0202 \* 0.0337 = 0.00068074

Expected agreement = 0.947 + 0.00068074 = 0.94768074

(Agreement - Expected Agreement ) (1 - Expected Agreement )

(0.9595 - 0.94768074 ) (1 - 0.94768074 )

0.01181926 0.05231926

0.226 ... again, not exactly one of the options, but the closest one gets a correct answer. Could be a rounding error, small enough difference.

So well done, I have no confidence at all that I know how to calculate Kappa. Good thing RapidMiner (and I assume other tools) will do it for me!!!

### More metrics for classifiers

- Receiver-Operating Characteristics (ROC) Curve Predicting something which has two values (Yes/No etc). Prediction model outputs a probability --- how good is the prediction. Have a threshold - any prediction above take on 1. Anything under 0. This is then compared against truth. Changes to threshold changes the possibility for a case. Four possibilities (true positive, false positive, true negative, false negative). X axis = percent false positives versus true negatives - false positive to the right Y axis = precent true positives versus false negatives - true positives up Want the curve to be above chance - the diagonal.
- Ai - A prime - close to ROC Probability that if a model is given an example from each category, it will accurately identify which is which. Mathematically equivalent to the Wilcoxon statistic. Enabling computation of statistical tests. There are Z tests for comparisons to other sets and chance. Not a good way to compute A prime for 3 or more categories. A prime assumes independence. So can't use if for multiple students. Need to compute A prime for each and integrate across students. Which leads to A prime approximate the area under the ROC curve Implementations of AUC are buggy in all major statistical packages. A prime versus Kappa - A prime more difficult to compute, only works for two categories, invariant across data sets and easy to computer statistical.
- precision - when the model says something is true, how often is it right TP / (TP + FP)
- recall - of cases that are 1, what percentage of these are capture. TP / ( TP + FN )

### Metrics for regressors

- Linear (Pearson's) correlation 1 to 0 to -1 What's good - physics 0.8 is weak. Education - 0.3 is good. Correlation is vulnerable to outliers.
- RMSE/MAD Mean Absolute Deviation - Average of absolute value (actual minus predicted) Root mean squared error - Squared difference (close cousin) MAD - average amount to which predictions deviate from actual values. RMSE can be interpreted the same way (mostly) but large deviations penalised more

Low RMSE/MAD is good - high correlation is good

Information criteria - Bayesian Information Criterion BiC' - trade-off between goodness of fit and flexibility of fit.

BIC prime

- values over 0 - worse than expected given number of variables
- values under 0 - better than expected given number of variables
- Can be used to understand significance of difference between models

AIC - Alternative to BiC - slightly different trade-off between goodnes of fit and flexibility of fit.

No single best method. Understand the data, use multiple metrics.

### Cross validation and over-fitting

Over-fitting - fit to the noise as well as the signal. Can't get rid of it.

Reducing over-fitting

- Use simple models - fewer variables (BiC, AIC, Occam's Razor); less complex functions (minimum description length)

Questions are: how bad and what do we fit.

Assess generalizability

Getting into training set and test set. But uses data unevenly.

Cross validation

- split data point into N equal-size groups
- train on all groups but one, test on last group
- For each possible combination

How many groups

- K-fold Split into K groups; quicker, some theoreticians prefer
- leave-out-one Every data point is a fold; more stable; avoids issue of how to select folds (stratification issues).

Cross-validation variants

- Flat cross-validation - each point has equal chance of being in each fold
- stratified cross-validation - biases fold selection so that some variable is equally represented - e.g. the variable you're trying to predict.
- **Student-level cross validation** - ensure no studetn's data is represented in two folds; allows testing of model generalizability to new students. As opposed to testing generalizability to new data from the same students.
    
    **Minimum cross-validation needed in the EDM conference** Papers that don't, usually get rejected. Okay to explicitly choose something else and discuss the choice. Weka doesn't support this. Batch X-Validation in RapidMiner supports this. Can apply this to other levels - lesson, school, demographic (new)
    

Where do you want to be able to use your model? Cross-validate at that level.

### Types of validity

Generalizability - does your model remain predictive with a new data set

Knowing the context the model will be used in drives what kind of generalisation you should study.

Ecological validity - does findings apply to real-life situations outside research (lab) settings. Could also be schools that easy to do research in (e.g. middle class suburban schools) but fails in other types of schools.

Construct validity - does your model actually measure what it was intended to measure - e.g. does your model fit the training data. But is the training data correct? e.g. which students will end up at other school based on disciplinary records - but other school also includes students moved to a special school for other reasons.

Predictive validity

Substantive validity - do your results matter? are you modelling a construct that matters? If you model X, what impacts will drive?

e.g. boredom correlates with many important factors (good), but visual/verbal preferences for learning materials doesn't predict learning better.

Content validity - does the test cover the full domain. A model of gaming that only captures one approach (systematic guessing) but not another (hint abuse) has lower content validity

Conclusion validity - are your conclusions justified

Many dimensions, all must be addressed.

That's the lectures for week 2 - is there a quiz? (Not really looking forward to that).

### The quiz

Applying a set of metrics. Our choice of tool. Mmm. One question appears to require compiled code for A prime - but told we can ignore that question.

Pearson correlation straight off the bat. Wonder if RapidMiner helps with this. Would appear so - operator called Correlation Matrix. Check the result with Excel. In business.

RMSE - back to the PDF to get the formula and into Excel (with a side visit to Google and [the web](http://dominoc925.blogspot.com.au/2010/05/using-excel-to-calculate-rmse-for-lidar.html))

MAD - done

Now onto accuracy of a model - apparently easy to do in Excel. But I've probably exhausted my knowledge of Excel. And it appears from the forums that I am not alone. The forums also suggest there are some folk having difficulties with the formula - but I don't think that's my problem.

This does appear to be a problem with this MOOC. An assumption of a fair bit of outside knowledge note covered in the lecture to answer the quiz.

I'm switching to Perl. Done, I think. Some of these questions appear to be a stretch from what I remember from the lecture.

And so Cohen's Kappa - is this the same as the Kappa that is mention in the lectures - doesn't appear "Cohen" gets a mention in the lecture. Just little things like this which can cause uncertainty.

Need to construct a detector/data 2 by in Perl. That's easy. Getting the calculation of Kappa to align with what they expect in the quiz system (no MCQ this time). Mm, try that.

And now precision. Easy enough to calculate (I think) - but am unsure that I'm getting to know the value of using the measures in a real bit of research.

Leaving out question 11 - I got 6 out of 10 for this one. Not great by any stretch of the imagination. Where did I go wrong? Looks like everything I did in Perl is wrong. The questions were

- Cohen's Kappa - given problems earlier with Kappa, I wasn't expecting this to be right. But I included 3 decimal points, it wanted 2!!!
- Precision - wrong - looks like this was the recall Looks like the problem here is a silly mistake around definition of true positive etc.
- Recall - this was wrong
- Question about applicability of detector based on precision and recall. This I just guessed. Too late and the leap too large.

Try again. 8 out of 10/11. Precision is still wrong. Cohen's Kappa is correct after fixing the rounding and the judgement about application is wrong as well - but given that precision is wrong, that's not surprising.

Don't have the energy to solve this tonight.