---
title: Planning an analysis of the learning analytics literature
date: 2013-10-03 13:50:09+10:00
categories: ['indicators', 'irac', 'learninganalytics-elearning']
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: damoclarky
      author_email: d.clark@cqu.edu.au
      author_ip: 138.77.33.149
      author_url: null
      content: 'Hi David,
    
    
        The Diigo API (https://www.diigo.com/api_dev/docs#section-methods) allows retrieving
        bookmarks.  The example response shows (while empty) annotations and comments
        fields along with tags.
    
    
        This could be programmatically extracted after analysis in the browser.
    
    
        Just a thought.
    
    
        Damien.'
      date: '2013-10-03 14:16:19'
      date_gmt: '2013-10-03 04:16:19'
      id: '875'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: David Jones
      author_email: davidthomjones@gmail.com
      author_ip: 139.86.2.14
      author_url: https://djon.es/blog/
      content: Okay, that looks good.  Get's the data into a database.  Trouble is I'm
        thinking something like NVIVO is probably going to have better analysis and visualisation
        functionality of the information.  Sure we could dodgy something up, but may be
        time to bite the bullet.  Of course, I note that NVIVO for the Mac is coming "late
        2013".  My institution has a site licence for NVIVO, yours?
      date: '2013-10-03 15:02:12'
      date_gmt: '2013-10-03 05:02:12'
      id: '876'
      parent: '875'
      type: comment
      user_id: '1'
    
pingbacks:
    - approved: '1'
      author: Approaches for literature analysis | The Weblog of (a) David Jones
      author_email: null
      author_ip: 76.74.254.35
      author_url: https://djon.es/blog/2013/11/15/approaches-for-literature-analysis/
      content: '[&#8230;] of the on-going research projects we have underway (really just
        starting up) is an analysis of the learning analytics literature. The following
        is an ad hoc record of a search into the literature around different approaches
        to [&#8230;]'
      date: '2013-11-15 15:33:49'
      date_gmt: '2013-11-15 05:33:49'
      id: '877'
      parent: '0'
      type: pingback
      user_id: '0'
    
---

See also: [[blog-home | Home]]

With the vague idea of the [IRAC framework done](/blog2/2013/10/03/the-irac-framework-locating-the-performance-zone-for-learning-analytics/), it's time to take the next step, i.e. "to use the framework to analyse the extant learning analytics literature". The following is some initial thinking behind why, what and how we're thinking of doing.

The main question we have here is "how?". Trying to figure out the best tools and process to help do this analysis. I've come up with two possibilities below, any better ones?

Wondering if Evernote and similar applications might offer a possibility? Chance are that [NVIVO](http://anujacabraal.wordpress.com/2012/08/01/why-use-nvivo-for-your-literature-review/) might be an option, or some other for of [qualitiative analysis software](http://provalisresearch.com/products/qualitative-data-analysis-software/freeware/) might be the go.

## Why?

We have a feeling that the learning analytics literature is over focusing on certain areas and ignoring some others. We want to find out if this is the case. This is important because we argue that this possible problem is going to make it harder for learning analytics to be integrated into the learning and teaching process and actually improve learning and teaching.

## What?

The plan is to analyse the learning analytics literature - initially we'll probably focus on the proceedings from the 2013 LAK conference - for two main aims

1. Identify the relative frequency with which the literature talks about the four components of the IRAC framework, i.e. Information, Representation, Affordance and Change.
2. Identify what aspects of each of the four components are covered in the literature.

We think this is sensible because of the theory/principles we've [built the IRAC framework on](/blog2/2013/10/03/the-irac-framework-locating-the-performance-zone-for-learning-analytics/) and some suggestion from the learning analytics literature that the IRAC components apply to learning analytics.

The foundation of the following image is Siemens (2013) analytics model. Over the top of that model we've applied the IRAC framework components. Not only does this suggest that the IRAC components aren't entirely divorced from learning analytics, it also suggests the potential over emphasis that we're worried about. The image shows how the Information component - gathering the information and analysing it - takes up more than three-quarters of the model. While this is an essential component of learning analytics, our argument is that the Affordances and Change components need significantly greater consideration if learning analytics is to be integrated into learning and teaching processes.

[![Slide77](images/9861600413_82f7e37eea_z.jpg)](http://www.flickr.com/photos/david_jones/9861600413/ "Slide77 by David T Jones, on Flickr")

## How?

The basic process is likely to be that each of the co-authors will read each article in the list of papers we select and highlight and annotate sections of the papers that discuss one or more of the four components of the IRAC framework.

For each paper, maintain some sort of database that tracks for each paper and each co-author

- The number of times each framework components is mentioned.
- The text associated with each component.
- Some potential labels for the attribute of each component that the text might represent.

Some possible solutions follow.

### Mendeley

1. Each of us import the list of papers into Mendeley.
2. Read the papers in Mendeley's reader.
3. Use the highlight and annotate tools to indicate appropriate quotes.
    
    The annotation could include the name of the IRAC component.
    
4. When finished a paper, export the annotations as a PDF.
5. Use the PDFs as input to the database.

PDFs are not great for this type of manipulation. Can see some manual work arising there.

### Diigo

1. Convert the list of papers to separate HTML files.
    
    Diigo won't let you annotate PDF files.
    
2. Upload them to a secure web server.
    
    So that only the authors can see them, protecting copyright etc.
    
3. Create a Diigo group for the authors.
4. Use Diigo to tag and annotate the HTML versions of the papers.
5. Extract the information via the Diigo RSS feeds.

Almost a nice solution, however, Diigo doesn't include the annotations in the RSS feed.

### References

Siemens, G. (2013). Learning Analytics: The Emergence of a Discipline. American Behavioral Scientist, 57(10), 1371–1379. doi:10.1177/0002764213498851