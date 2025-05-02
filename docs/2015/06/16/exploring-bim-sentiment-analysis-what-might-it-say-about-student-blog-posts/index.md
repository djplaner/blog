---
title: Exploring BIM + sentiment analysis - what might it say about student blog posts
date: 2015-06-16 22:35:51+10:00
categories: ['4paths', 'bad', 'bim', 'indicators']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Updating &#8220;more student details&#8221; | The Weblog of (a) David Jones
      author_email: null
      author_ip: 192.0.81.73
      author_url: https://davidtjones.wordpress.com/2015/07/23/updating-more-student-details/
      content: '[&#8230;] while I&#8217;m at it, I&#8217;m hoping I might be able to add
        a bit of sentiment analysis to [&#8230;]'
      date: '2015-07-23 12:39:20'
      date_gmt: '2015-07-23 02:39:20'
      id: '1335'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: Sentiment analysis of student blog posts &#8211; The Weblog of (a) David
        Jones
      author_email: null
      author_ip: 192.0.101.131
      author_url: https://davidtjones.wordpress.com/2016/02/14/sentiment-analysis-of-student-blog-posts/
      content: '[&#8230;] June last year I started an exploration into the value of sentiment
        analysis of student blog posts. This morning I&#8217;ve actually gotten [&#8230;]'
      date: '2016-02-14 11:17:07'
      date_gmt: '2016-02-14 01:17:07'
      id: '1336'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The following documents some initial exploration into why, if, and how sentiment analysis might be added to the [BIM module](/blog2/research/bam-blog-aggregation-management/) for Moodle. BIM is a tool that helps manage and mirror blog posts from individual student blogs. [Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) is an application of algorithms to identify the sentiment/emotions/polarity of a person/author through their writing and other artefacts. The theory is that sentiment analysis can alert a teacher if a student has written something that is deemed sad, worried, or confused; but also happy, confident etc.

Of course, the promise of analytics-based approaches like this may be oversold. [There's a suggestion](http://www.slideshare.net/mcieliebak/deep-learning-for-sentiment-at-sgaico-2014-by-mark-cieliebak) that some approaches are wrong 4 out of 10 times. But I've seen other suggestions that human beings can be wrong at the same task 3 out of 10 times. So the questions are

1. Just how hard is it (and what is required) to add some form of sentiment analysis to BIM?
2. Is there any value in the output?

### Some background on sentiment analysis

Tends to assume a negative/positive orientation. i.e. good/bad, like/dislike. The polarity. There are various methods for performing the analysis/opinion mining. There are challenges in analysing text (my focus) alone.

Lots of research going on in this sphere.

Of course there also folk building and some selling stuff. e.g. Indico is one I've heard of recently. Of course, they all have their limitations and sweet spots, Indico's sentiment analysis is apparently good for

> Text sequences ranging from 1-10 sentences with clear polarity (reddit, Facebook, etc.)

That is perhaps starting to fall outside what might be expected of blog posts. But may fit with this collection of data. Worth a try in the time I've got left.

### Quick test of indico

indico provides a REST based API that includes sentiment analysis. Get an API key and you can throw data at it and it will give you a number between 0 (negative) and 1 (positive).

You can even try it out manually. Some quick manual tests

- "happy great day fantastic" generates the result 0.99998833
- "terrible sad unhappy bad" generates 0.000027934347704855157
- "tomorrow is my birthday. Am I sad or happy" generates 0.7929542492644698
- "tomorrow is my birthday. I am sad" generates 0.2327375924840286
- "tomorrow is my birthday. I am somewhat happy" 0.8837247819167975
- "tomorrow is my birthday. I am very happy" 0.993121363266806

With that very ill-informed testing, there are at least some glimmers of hope.

Does it work on blog posts.......actually not that bad. Certainly good enough to play around with some more and as a proof of concept in my constrained circumstances. Of course, indico is by no means the only tool available (e.g. [meaningcloud](https://www.meaningcloud.com/developer/sentiment-analysis/doc/2.0/what-is-sentiment-analysis)).

But for the purpose of the talk I have to give in a couple of weeks, I should be able to use this to knock up something that works with the [more student details script](/blog2/2014/11/13/adding-more-student-information-to-a-moodle-course/).