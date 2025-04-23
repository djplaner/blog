---
title: Statistics in Education - Week 1
date: 2013-08-10 23:02:43+10:00
categories: ['thesis']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

Have signed up for another MOOC - [Statistics in Education for Mere Mortals](https://www.canvas.net/courses/statistics-in-education-for-mere-mortals) - to fill a hole. What follows is the diary of the first week.

According to the syllabus, I'm already a bit behind.

So the instructor is doing some research around participation - one of the motivations for offering the course. Google map of participants. Seems I'm #2 for Queensland. Concentration seems to be Eastern US.

### Canvas

The MOOC is being run using the Canvas LMS. Second time using the system. Am finding it interesting that there seems to be in-built support for the idea of a learning path. The series of activities/resources is sequential and the system seems to support that. The lack of support for this type of functionality in Moodle is something I've missed. Finding the ability to step through each step sequentially appealingly efficient.

### Research questions

Will be interesting to see the research that comes of this. Have to admit to some of the questions leaving me a little underwhelmed.

## First presentation

And the content begins. A 20 minute video. Lecture with a talking head in the bottom left hand corner, which disappears when the slides start. No annotation of the slides during the lecture, might have helped in places.

:) A "wii play station" as a type of video game console.

Good quote

> Measurement is limiting the data ... so that those data may be interpreted and, ultimately, compared to an acceptable qualitative or quantitative standard
> 
> Data limited by: measurement construct; instrument capability; amount of raw information we are prepared to deal with

Need to think about this applies to analytics. Data mining has approaches to get around this limitation of statistical approaches.

Metaphor

> Isolating meaningful data when conducting most research studies is like .... filling a tea cup with a fire hose

### Four scales of measurement

Different scales suggest different operations are possible.

1. Nominal scale - Frequency distribution
    
    Nominal == name. Numbers are used as a name, not as a quantity. Doing arithmetic on these numbers is nonsensical.
    
2. Ordinal scale - median and percentiles
    
    Ordinal == order/ranking. e.g. ranking preferred candidates.
    
3. Interval scale - add or subtract, mean, standard deviation, standard error of the man
    - Has equal amounts of measurement.
    - Zero point established arbitrarily.
        
        e.g. temperature and 0 degrees.
        
    - Can determine, mean, standard deviation, and product moment correlation.
    - Can apply inferential statistical analysis.
4. Ratio scale - ratio
    - Equal measurement units.
    - Has an absolute zero point.
    - Expresses values in terms of multiples and fractional parts and the ratios are true ratios (e.g. ruler )
    - Can determine geometric mean and percentage variation
    - Can conduct virtually any inferential statistical analysis

Measuring temperature is given as example of interval scale. Where you can't say 40o is twice as hot as 20o. It's just an interval, not a ratio. Where as length is.

### Types of Statistics

Presents two

1. Measures of central tendency - first module
2. Measures of variability - second module

### Measures of central tendency

- Mean - average of a set of numbers
- Median - the number at the midpoint of a set of numbers.
- Mode - the most popular number.

All are the same in a normal distribution. But not in a skewed distribution.

So the statistics in this course assume a normal distribution. Seems limiting.

In passing the central tendency gets defined as the number that best represents a group of numbers. The explanation of median/mean would have been better illustrated visually, rather than by narration of a text-based powerpoint slide.

### Normal distribution

Woo hoo. Narrated lecture + graphics tablet.

As the description of the normal distribution proceeds, I'm wondering how on earth I would ever be doing anything that would have data in a normal distribution? But perhaps just indicates the value of "central tendency".

### The Galton Machine

A bit of fun. Link to [Java applet](http://www.ms.uky.edu/~mai/java/stat/GaltonMachine.html).

### Computing the man of a set of scores

It appears that Excel will be the statistical software of choice. Perhaps including some auto marking of student work. The first is a simple task to test this out. Apparently going to take an hour to do. 11 minutes in, not sure how it could drag on that long.

It will be interesting to see how many questions arise from simple technical issues - like using different versions of Excel. Shall also be interesting to see how the difficulty of the activities grows.

Interesting that the quiz self evaluation asks for results in tenths, but the quiz system wants to add a couple of zeros to the end. I can see that throwing a few people off.

Woo hoo. 100%.

The next page after the quiz is a discussion forum for general help. There are a few folk reporting problems. Especially with the second and third questions. I'm guessing this arises from this combination of factors

1. The video creating the spreadsheet only rounded off results in set of averages, and **not** the averages that would be used for the second and third questions. It didn't need to, because that data meant the averages were rounded to a tenth
2. The new data doesn't result in data rounded to the tenth.
3. The quiz question asks for results rounded to the tenth.

In entering the new data, I added the rounding. But I imagine others didn't.

Appears that other folk didn't modify their existing spreadsheet.

Ahh, other folk from China and Pakistan reporting being unable to access the YouTube videos.

### Descriptive statistics - Standard Deviation

Onward and upward.

Statistic has two meanings: a description or an estimate about population.

Mm, the video didn't do a great job of clearly defining the difference betwen sample and population. Use an example, but didn't clearly define it. Google is my friend.

And here comes the terminology

- Population - "a set of entities concerning which statistical inferences are to be drawn.
- Sample - a subset of the population.

The questions

1. Collecting data on a population?
    
    Describe the population using a parameter.
    
2. Want to know about a population, but can only collect data on a sample?
    
    Sampling gives the sample and then we do a description using a statistic, which is then used to make an inference about the parameter for the population.
    
3. Only collecting data on a sample?

Mmm, seems Broad is cleaning up in Durham.

Here comes the maths and symbols.

Population is mu. Sample is Summation of X i.e. X bar (a bar over the top of X).

So, we did central tendency above. That's one type of descriptive statistic. Now it's the other main type of descriptive statistics. Measures of variability. Kurtosis - shape of the curve, it's peakedness.

Three methods to measure variability

1. Range - Difference between high and low scores.
    
    Only tells the difference between two scores. Ignore the others.
    
2. Deviation scores - Computer the difference between each score and the grand mean.
    
    Now take the average. Well the average of this always 0.
    
    This is described, could have been much better with a visual.
    
3. Standard deviation
    
    Square the difference scores first (gets rid of the negatives). Then take the square root.
    

[![ by kxp130, on Flickr](http://farm3.static.flickr.com/2618/4174928680_7c95b42ed1_m.jpg " by kxp130, on Flickr")](http://www.flickr.com/photos/kxp130/4174928680/)  
[![Creative Commons Attribution-Noncommercial 2.0 Generic License](http://i.creativecommons.org/l/by-nc/2.0/80x15.png "Creative Commons Attribution-Noncommercial 2.0 Generic License")](http://creativecommons.org/licenses/by-nc/2.0/)  by  [](http://www.flickr.com/people/kxp130/)[kxp130](http://www.flickr.com/people/kxp130/) [](http://www.imagecodr.org/)

When estimating the population parameter for a sample has a N-1, rather than N. Why? Apparently a rule thumb developed over time, imagine there must be some research behind it. Instructor admits not a good explanation. It's a problem area.

At this point, interesting that there hasn't been much placement of why we're doing this.

Another example with this table where some visualisation accompanying the verbal explanation would have helped.

And now the difficult stuff. What does a SD of 8.66 mean?

If all sold the same then SD = 0. If all sold about the same, then SD should be small. But what is considered small?

And now another Excel exercise, apparently 26 minutes of video == 90 minutes worth of activity. I don't think so....really dragging now. Small win. Picked up an Excel tip.

2nd quiz done. I think I'll stop there for the night. Time to watch some cricket and read a book.