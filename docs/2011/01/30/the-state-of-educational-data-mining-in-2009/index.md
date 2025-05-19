---
categories:
- indicators
- lak11
date: 2011-01-30 21:22:40+10:00
next:
  text: Problems of service provision and why can't I have a personalised class timetable?
  url: /blog/2011/01/30/institutional-information-systems-and-the-problems-of-service-provision/
previous:
  text: The demise of ALTC and why I&#039;m not sad
  url: /blog/2011/01/28/the-demise-of-altc/
title: The state of educational data mining in 2009
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: "Tweets that mention The state of educational data mining in 2009 \xAB The\
        \ Weblog of (a) David Jones -- Topsy.com"
      author_email: null
      author_ip: 208.74.66.43
      author_url: http://topsy.com/davidtjones.wordpress.com/2011/01/30/the-state-of-educational-data-mining-in-2009/?utm_source=pingback&utm_campaign=L2
      content: "[...] This post was mentioned on Twitter by Paulo Sim\xF5es, Sreya Dutta.\
        \ Sreya Dutta said: RT @pgsimoes: The state of educational data mining in 2009\
        \ http://dlvr.it/FPZmZ #elearning [...]"
      date: '2011-01-30 22:31:54'
      date_gmt: '2011-01-30 12:31:54'
      id: '3226'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The following is a summary and some initial reflections on the paper

> Baker, S.J.D., Yacef, K. (2009) The State of Educational Data Mining in 2009: A Review and Future Visions: http://www.educationaldatamining.org/JEDM/images/articles/vol1/issue1/JEDMVol1Issue1\_BakerYacef.pdf

It's another reading for the first week of the [LAK11 MOOC](http://learninganalytics.net/).

The format I use for these posts is that the overview section is essentially my summary/reflections on the paper. The rest of the sections are my potted summary of each of the sections of the paper.

EDM == Educational Data Mining

_Disclaimer_ I let this post stew unfinished for a couple of weeks while I progressed the thesis. I'm posting it now unfinished. Time to move on with more recent things.

### Overview

Gives a good overview/feel for the field. But as a high level description it can't provide much detail about specific areas, but does provide the references to go digging.

### Abstract

- Methodological profile of early EDM research compared with 2008/2009 research.
- Trends and shifts include
    - increased emphasis on prediction;
    - emergence of attempts to use existing models to make scientific discoveries
    - reduction in frequency of relationship mining.
- Examine 2 ways of categorising the diversity in EDM research.
- Review research problems addressed by the methods
- Lists and discusses the most cited EDM papers.

### Introduction

EDM field is growing, conferences, new journal. Time to review.

### What is EDM?

Definition from [http://www.educationaldatamining.org/](http://www.educationaldatamining.org/)

> Educational Data Mining is an emerging discipline, concerned with developing methods for exploring the unique types of data that come from educational settings, and using those methods to better understand students, and the settings which they learn in.

Suggests EDM is different from data mining (references an in press publication of one of the authors)

> due to the need to explicitly account for (and the opportunities to exploit) the multi-level hierarchy and non-independence in educational data.

Which means models drawn from psychometrics is often used in educational data mining.

Now, I don't know enough to be comfortable that I understand that, which means I should try and following up on that publication.

> BAKER, R.S.J.D. in press. [Data Mining For Education](http://users.wpi.edu/~rsbaker/Encyclopedia%20Chapter%20Draft%20v10%20-fw.pdf) (a pre-print version). In International Encyclopedia of Education (3rd edition), B. MCGAW, PETERSON, P., BAKER Ed. Elsevier, Oxford, UK.

### EDM Methods

Drawn from a variety of fields. Two attempts to categorise the methods are introduced, but Baker (in press) is the one it goes with.

Percentages in brackets represent percentage of EDM papers (1995-2005) using the method

1. Prediction (28%)
    - Classification
    - Regression
    - Density estimation
2. Clustering (~15%)
3. Relationship mining (43%)
    - Association rule mining
    - Correlation mining
    - Sequential pattern mining
    - Causal data mining
4. Distillation of data for human judgement (~18%)
5. Discovery with methods  
    A model is developed through any process that can be validated. It's then used in analysis or mining.

First 3 are common in data mining.

Distillation of data not widely accepted in data mining, but matches a category in the other categorisation scheme for EDM which suggests it is common in EDM.

"Discovery with methods" most unusual from a data mining perspective.

Relationship mining most prominent in EDM.

### Key applications of EDM methods

EDM research come from various fields: individual learning from software, CSCL, computer adaptive testing, student failure/retention.

Key areas

- Student models;  
    Improvement of student models a key application. Models represent student characteristics. Knowing differences enables different responses which suggests improving student learning. Some enable use in real-time. Applications include (all with references): are students gaming the system; experiencing poor self-efficacy; off-task; bored.  
    In terms of student failure gives three references.
- Domain knowledge models;  
    Psychometric modeling frameworks + space-searching algorithms used to develop automated approaches from data.
- Studying pedagogical support;  
    i.e. which are most effective in which situations for which students.
- Looking for empirical evidence to refine/extend educational theories/phenomena;  
    e.g. Perera et al (2009) use Big 5 theory for teamwork to search for successful patterns of interaction in student teams.

### Important trends in EDM research

#### Prominent papers from early years

Based on Google scholar citations, look at most prominent papers

- (1st) Zaiane (2001) was one to propose and evangelise around EDM.
- (2nd) Zaiane (2002) - a proposal - and (4th) Tang and McCalla (2005) - an instantiation - examine how EDM methods can help develop sensitive/effective e-learning systems.
- (3rd) Baker, Corbett and Koedinger (2004) case study of EDM methods to open new research areas. e.g. scientific study of gaming the system.
- (5th) Merceron and Yacef (2003) and (6th) Romereo et al (2003) present tools to support EDM.
- (7th) Beck and Woolf (2000) use EDM prediction methods to develop student models.

#### Shift in paper topics over the years