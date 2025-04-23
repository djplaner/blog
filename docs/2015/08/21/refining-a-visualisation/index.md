---
title: Refining a visualisation
date: 2015-08-21 13:36:42+10:00
categories: ['4paths']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

Time to [refine the visualisation](/blog2/2015/08/18/visualising-locations-of-students-etc/) of students by postcodes started earlier this week. Have another set of data to work with.

1. Remove the identifying data.
2. Clean the data. I had to remind myself the options for the sort comment - losing it. The following provide some idea of the mess. \[code lang="sh"\]\[/code\] :1,$s/"\* Sport,Health&PE+Secondry.\*"/HPE\_Secondary/ :1,$s/"\* Sport, Health & PE+Secondry.\*"/HPE\_Secondary/ :1,$s/Health & PE Secondary/HPE\_Secondary/ :1,$s/\* Secondary.\*/Secondary/ :1,$s/\* Secondry.\*/Secondary/ :1,$s/\* Secondy.\*/Secondary/ :1,$s/Secondary.\*/Secondary/ :1,$s/\* Secdary.\*/Secondary/ :1,$s/\* TechVocEdu.\*/TechVocEdu/
3. Check columns Relying on a visual check in Excel - also to get a better feel for the data.
4. Check other countries Unlike the previous visualisation, the plan here is to recognise that we actually have students in other countries. The problem is that the data I've been given doesn't include country information. Hence I have to manually enter that data. Giving for one of the programs, the following.
    
    | 4506 | Australia |
    | --- | --- |
    | 8 | United Kingdom |
    | 3 | Vietnam |
    | 3 | South Africa |
    | 3 | China |
    | 2 | Singapore |
    | 2 | Qatar |
    | 2 | Japan |
    | 2 | Hong Kong |
    | 2 | Fiji |
    | 2 | Canada |
    | 1 | United States of America |
    | 1 | Taiwan |
    | 1 | Sweeden |
    | 1 | Sri Lanka |
    | 1 | Philippines |
    | 1 | Papua New Guinea |
    | 1 | New Zealand |
    | 1 | Kenya |
    | 1 | Ireland |
    

And all good.