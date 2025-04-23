---
title: "Dashboards suck: learning analytics&#039; broken metaphor"
date: 2015-06-24 17:49:54+10:00
categories: ['indicators', 'irac', 'pirac']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: What might a project combining LX Design and Analaytics look like? | The
        Weblog of (a) David Jones
      author_email: null
      author_ip: 192.0.99.190
      author_url: https://davidtjones.wordpress.com/2015/09/14/what-might-a-project-combining-lx-design-and-analaytics-look-like/
      content: '[&#8230;] It hardly ever does anything about affordances or change. This
        is why dashboards suck and are a broken metaphor. A dashboard without the ability
        to do anything to control the car are no value [&#8230;]'
      date: '2015-09-14 11:40:48'
      date_gmt: '2015-09-14 01:40:48'
      id: '1338'
      parent: '0'
      type: pingback
      user_id: '0'
    - approved: '1'
      author: Situation awareness, complex adaptive systems and learning analytics | Col&#039;s
        Weblog
      author_email: null
      author_ip: 192.0.86.68
      author_url: https://beerc.wordpress.com/2015/09/29/situation-awareness-complex-adaptive-systems-and-learning-analytics/
      content: "[&#8230;] I see a role for learning analytics data and I think it links\
        \ to David\u2019s sentiments about why dashboards suck. The retrospective nature\
        \ of business intelligence style dashboards limits their usefulness in the [&#8230;]"
      date: '2015-09-29 14:50:57'
      date_gmt: '2015-09-29 04:50:57'
      id: '1339'
      parent: '0'
      type: pingback
      user_id: '0'
    
---

See also: [[blog-home | Home]]

I started playing around with what became learning analytics in 2007 or so. Since then every/any time "learning analytics" is mentioned in a university there's almost an automatic mention of dashboards. So much so I was lead to tweet.

https://twitter.com/djplaner/status/610769509394182144

I've always thought dashboards suck. This morning when preparing the slides for [this talk](http://bit.ly/4pathsTalk) on learning analytics I came across an explanation which I think captures my discomfort around dashboards (I do wonder whether I'd heard it somewhere else previously).

### What is a dashboard

In the context of an Australian university discussion about learning analytics the phrase "dashboard" is typically mentioned by the folk from the business intelligence unit. The folk responsible for the organisational data warehouse. It might also get a mention from the web guru who's keen on Google Analytics. In this context a dashboard is typically a collection of colourful charts, often even doing a good job of representing important information.

So what's not to like?

### The broken metaphor

Obviously "analytics" dashboards are a metaphor referencing the type of dashboard we're familiar with in cars. The problem is that many (most?) of the learning analytics dashboards are conceptualised and designed like the following dashboard.

[![Van dashboard by Paul  Jerry, on Flickr](https://farm3.static.flickr.com/2748/4210992025_1699fbfc7e_m.jpg "Van dashboard by Paul  Jerry, on Flickr")](https://www.flickr.com/photos/paj/4210992025/)  
[![Creative Commons Creative Commons Attribution 2.0 Generic License](http://i.creativecommons.org/l/by/2.0/80x15.png "Creative Commons Creative Commons Attribution 2.0 Generic License")](http://creativecommons.org/licenses/by/2.0/)   by  [](https://www.flickr.com/people/paj/)[Paul Jerry](https://www.flickr.com/people/paj/) [](http://www.imagecodr.org/)

The problem is that this conceptualisation of dashboards misses the bigger picture. Rather than being thought of like the above dashboard, learning analytics dashboards need to be thought of as like the following dashboard.

[![1977 meets 2009 by Simon Collison, on Flickr](https://farm4.static.flickr.com/3264/3145232705_56f03acc7c_m.jpg "1977 meets 2009 by Simon Collison, on Flickr")](https://www.flickr.com/photos/collylogic/3145232705/)  
[![Creative Commons Creative Commons Attribution-Noncommercial-No Derivative Works 2.0 Generic License](http://i.creativecommons.org/l/by-nc-nd/2.0/80x15.png "Creative Commons Creative Commons Attribution-Noncommercial-No Derivative Works 2.0 Generic License")](http://creativecommons.org/licenses/by-nc-nd/2.0/)   by  [](https://www.flickr.com/people/collylogic/)[Simon Collison](https://www.flickr.com/people/collylogic/) [](http://www.imagecodr.org/)

Do you see the difference? (and it's not the ugly, primitive nature of the graphical representation in the second dashboard).

### Representation without Affordances and removed from the action

The second dashboard image includes: the accelerator, brake, and clutch pedals; the steering wheel; the indicators; the radio; air conditioning; and all of the other interface elements a driver requires to do something with the information presented in the dashboard. All of the [affordances](https://en.wikipedia.org/wiki/Affordance) a driver requires to drive a car.

The first dashboard image - like many learning analytics dashboards - provides no affordances for action. The first vision of a dashboard doesn't actually help you do anything.

What's worse, the dashboards provided by most data warehouses aren't even located within the learning environment. You have to enter into another system entirely, find the dashboard, interpret the information presented, translate that into some potential actions, exit the data warehouse, return to the learning environment, translate those potential actions into the affordances of the learning environment.

Picking up on the argument of Don Norman (see quote in image below), the difficulty of this process would seem likely to reduce the chances of any of those potential actions being taken. Especially if we're talking about (casual) teaching staff working within a large course with limited training, support and tools.

[![Norman on affordances](images/18656913650_b2a17f2513_n.jpg)](https://www.flickr.com/photos/david_jones/18656913650 "Norman on affordances by David Jones, on Flickr")

### Affordances improve learning analytics

Hence, my argument is that the dashboard (Representation) isn't sufficient. In designing your learning analytics application you need to include the pedals, steering wheel etc (Affordances) if you want to increase the likelihood of that application actually helping improve the quality of learning and teaching. Which tends to suggest that your learning analytics application should be integrated into the learning environment.