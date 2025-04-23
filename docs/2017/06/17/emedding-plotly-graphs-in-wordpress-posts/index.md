---
title: Emedding plotly graphs in Wordpress posts
date: 2017-06-17 12:50:26+10:00
categories: ['4paths', 'indicators', 'irac', 'learninganalytics-elearning']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

Last year I started using [with Perl to play with](http://plot.ly) [analytics around Moodle Book usage](http://djon.es/blog/2016/08/07/how-and-why-do-people-use-the-moodle-book-module/). This year, @beerc and I have been starting to play with Jupyter Notebooks and Python to play with analytics for meso-level practitioners (Hannon, 2013). Plotly provides a fairly useful platform for generating graphs of various types and sharing the data. Works well with a range of languages and Jupyter Notebooks.

Question here is how well it works with Wordpress. Wordpress has some (understandable) constraints around embedding external HTML in Wordpress posts/pages. But there is a large set of community contributed plugins to Wordpress that help with this, including a couple that apparently work with Plotly.

- [wp-plotly](https://wordpress.org/plugins/wp-plotly/) designed to embed a Plotly hosted graph by providing the plotly URL. Doesn't appear to work with the latest version of Wordpress. **No go**
- [Plot.wp](https://wordpress.org/plugins/plotwp/) provides a Wordpress shortcode for Plotly (plotly and /plotly with square brackets) into which you place Plotly json data and hey presto graph. Has [a github repo](https://github.com/paleolimbot/plotwp) and actually works with the latest version of Wordpress.

### How to produce JSON from Python

I'm a Python newbie. Don't really grok it the way I did Perl. I assumed it should be possible to auto-generate the json from the Python code, but how.

Looks like this will work in a notebook, though it does appear to need the resulting single quotes converted into double quotes and two sets of double quotes removed to be acceptable JSON.

```
#.. Python code to produce plotly figure ready to be plotted
import json
jsonData['data'] = json.dumps( fig['data'])
jsonData['layout'] = json.dumps( fig['layout'])
jsonData

```

For the graph I'm currently playing with, this ends up with

```
{"layout": {"yaxis": {"range": [0, 100], "title": "% response rate"}, "title": "EDC3100 Semester 2 MyOpinion % Response Rate", "xaxis": {"ticktext": ["2014 (n=106)", "2015 (n=88)nLeaderboard", "2016 (n=100)nLeaderboard"], "title": "Year", "tickvals": ["2014", "2015", "2016"]}}, 
  "data": [{"type": "bar", "name": "EDC3100", "x": ["2014", "2015", "2016"], "y": [34, 48, 49]}, {"type": "scatter", "name": "USQ average", "x": ["2015", "2016"], "y": [26.83, 23.52]}]}

```

And the matching graph produced by plotly follows. Roll over the graph to see some "tooltips".

\[plotly\]

{"layout": {"yaxis": {"range": \[0, 100\], "title": "% response rate"}, "title": "EDC3100 Semester 2 MyOpinion % Response Rate", "xaxis": {"ticktext": \["2014 (n=106)", "2015 (n=88)\\nLeaderboard", "2016 (n=100)\\nLeaderboard"\], "title": "Year", "tickvals": \["2014", "2015", "2016"\]}}, "data": \[{"type": "bar", "name": "EDC3100", "x": \["2014", "2015", "2016"\], "y": \[34, 48, 49\]}, {"type": "scatter", "name": "USQ average", "x": \["2015", "2016"\], "y": \[26.83, 23.52\]}\]} \[/plotly\]

### References

Hannon, J. (2013). Incommensurate practices: sociomaterial entanglements of learning technology implementation. Journal of Computer Assisted Learning, 29(2), 168–178. https://doi.org/10.1111/j.1365-2729.2012.00480.x