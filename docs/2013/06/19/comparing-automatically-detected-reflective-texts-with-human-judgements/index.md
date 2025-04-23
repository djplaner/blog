---
title: Comparing Automatically Detected Reflective Texts with Human Judgements
date: 2013-06-19 11:46:03+10:00
categories: ['bim', 'bim2', 'elearning', 'indicators']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

The following is a summary and some thoughts on the following paper

> Ullmann, T. D., Wild, F., & Scott, P. (2012). [Comparing Automatically Detected Reflective Texts with Human Judgements](http://ceur-ws.org/Vol-931/paper8.pdf). 2nd Workshop on Awareness and Reflection in Technology-Enhanced Learning. 7th European Conference on Technology-Enhanced Learning (pp. 101–116). Saarbruecken, Germany.

My interest in this paper is as an addition to BIM to provide scaffolding for students in their reflections and also as part of the preparation for my [Moodlemoot'AU 2013](http://moodlemoot.org.au/mod/book/view.php?id=24&chapterid=56) talk next week.

Of course, it also allows me to engage with one of the current fads

> The automated detection of reflection is part of the broader field of learning analytics, especially social learning content analysis \[13\]. (Ullman et al, 2012, p. 102)

where \[13\] is

> Ferguson, R., Shum, S.B.: Social learning analytics: five approaches. In: Proceedings of the 2nd International Conference on Learning Analytics and Knowledge. p. 23–33. LAK ’12, ACM, New York, NY, USA (2012), http://doi.acm.org/10.1145/2330601.2330616

In working through this I'm pointed to [the proceedings](http://ceur-ws.org/Vol-790/) of a 2011 workshop on "Awareness and Reflection in Learning networks". Which is something I'll need to return to, not to mention the [2nd](http://sunsite.informatik.rwth-aachen.de/Publications/CEUR-WS/Vol-931/) and 3rd workshops.

Would appear, that just yet, this work isn't quite ready for BIM. But who knows what has happened in the last year or so. Possibilities exist.

### A distributed cognition aside

At the moment, I'm thinking that that "Moving Beyond" part of that presentation - which will show off what I'm thinking of working on with BIM - is going to be scaffolded with the following which is from Bell & Winn (2000) and is their description of Salomon's (1995) two broad "classes" of distributed cognition as applied to artefacts in a learning environment

1. An individual's cognitive burden can be off-loaded onto the artefact, which may not necessarily help the individual learn about what the artefact is doing.
2. An artefact is designed to reciprocally scaffold students in specific cognitive practices, it helps them in a process and in doing so can help them be able to perform this task without the artefact.

Ullman's et al (2012) work would seem to fit neatly into the second of those classes. I'm hoping it (or other work) will provide the insight necessary to scaffold students in learning how to reflect.

I'm also thinking that there's another dimension to think about in the design of BIM (and e-learning tools in general), the identity of the individual. I'm thinking there are at least three/four different identities that should be considered, they are:

1. Student - as above, the person who's using the tool to learn something.
2. Teacher - the individual there to help the student. (My thinking is rooted in a formal education environment - it's where I work - hence there is a need for a distinction here and my context also drives the remaining identities).
3. Institutional support and management - the folk who are meant to help and ensure that all learning is of good quality.
4. Artefact developers - the folk that develop the artefacts that are being used by the previous three roles.

I'm thinking that a tool like BIM should be concerned with providing functionality that addresses both "distributed cognition classes" for all roles.

### Abstract - Ullmann et al (2012)

- Paper reports on an experiment to automatically detect reflective and non-reflective texts.
- 5 elements of reflection were defined and a set of indicators developed "which automatically annotate texts regarding reflection based on the parameterisation with authoritative texts".
- A collection of blog posts were then run through the system and an online survey used to gather human judgements for these texts.
- The two data sets allowed a comparison of the quality of the algorithm versus human judgements.

### Introduction

Reflection is important - "at 'the heart of key competencies' for a successful life and a well-functioning society" (Ullman et al, 2012, p. 101).

Methods for assessing reflective writings are recent and not full established. Some quotes about how most focus has been on theorising reflection and its use, with little on how to assess reflection.

Issues with manual assessment of reflection

1. Time-consuming.
2. Feedback comes a long time after of reflection.
3. Reluctance to share reflective writing given the nature of reflection.

### Situating the research

This fits within learning analytics and social learning content analysis

Two prominent approaches for identifying automatically cognitive processes

1. Connection between cue words and acts of cognition
2. Probabilistic models and machine learning algorithms.

References to earlier work with both approaches provided.

### Elements of reflection

Points out that no model of reflection is currently agreed upon. Presents 5 elements based on major stream of theoretical discussion

1. Description of an experience.
    
    Sets the stage for reflection. A description of the important parts of the event. Might be a description of external events or the internal situation of the person. Common themes include: Conflict; self-awareness; and, emotions.
    
2. Personal experience.
    
    Still some debate. But self-awareness, inner dialogue indicators.
    
3. Critical analysis
    
    critical questions of content, process and premises of experience to correct assumptions beliefs etc.
    
4. Taking perspectives into account
    
    Using a frame of reference based on dialogue with others, general principles, theory.
    
5. Outcome of reflective writing
    
    New understanding/transformative and confirmatory learning. Sums up what was learned, concludes, plans for the future, new insight etc.
    

Acknowledges overlap between these elements.

A set of indicators were developed for each element.

### Reflection detection architecture

a set of annotators - "bits of software" - developed and combined to do the analysis. Analysing the text and identify certain elements (roughly) based on keywords or other analysis.

- NLP annotator - highlighting elements of natural language.
- Premise (assuming that, because, deduced from) and conclusion (as a result, therefore) annotator
- Self-reference (I me mine) and pro-noun other (he, they, others) annotators
- Reflective vern (rethink, reason, mull over).
- Learning outcome annotator (define, name, outline ) and Bloom's taxonomy (remember, understand, apply, analyse)
- Future tense (will, won't)

An analysis component aggregates and tries to infer knowledge from the annotations. The creation of IF THEN statements used to chain lower level facts together.

This goes on until a high level rule(s) are used to connect with an element of reflection. Ended up using 16 such rules allocated to the five elements of reflection.

### Method

Indicators were developed iteratively with sample texts.

Big question, what "weight should be given to each indicator to form a reflective text" (p. 108).

Used 10 texts marked as prototypical reflective writings from the reflection literature to parameterise the analytics. All this ended up with the following definition of the conditions for a reflective text

> - The indicators of the ”description of experiences” fire more than four times.
> - At least one self-related question.
> - The indicators of the ”critical analysis” element fire more than 3 times.
> - At least one indicator of the ”taking perspectives into account” fires.
> - The indicators of the ”outcome” element fire more than three times.
> 
> (p. 109)

Goes onto describe the questionnaire used as a comparison. Blog posts shown in random with questions. Human judgements reduced to 202. Data gathered by Mechanical Turk. Led to some problems, handled by filtering some.

### Text corpus

Experiment was done using the "Blog Authorship Corpus" a collection of 681,288 posts, 140 millon words from 19320 bloggers from blogger.com in August 2004. Took the first 150 blog files. Short blog posts (less than 10 sentences) and foreign language posts removed.

5176 blog posts were annotated, 4m+ annotations and 170K+ inferences.

### Results

Some value. Human folk more likely to agree with those identifies as reflective by the system.

One of the limiting factors is the parameterisation - the text used to do this was limited and there is no large body of quality reflective text available. Important because the parameterisation influences quality detection.

Doing more work on this.

Closes with

> One possible application scenario especially useful for an educational setting is to combine the detection with a feedback component. The described reflection detection architecture with its knowledge-based analysis component can be extended to provide an explanation component, which can be used to feedback why the system thinks it is a reflective text, together with text samples as evidences.

### References

Bell, P., & Winn, W. (2000). Distributed Cognitions, by Nature and by Design. In D. Jonassen & S. Land (Eds.), Theoretical Foundations of Learning Environments (pp. 123–145). Mahwah, New Jersey: Lawrence Erlbaum Associates.

Ullmann, T. D., Wild, F., & Scott, P. (2012). [Comparing Automatically Detected Reflective Texts with Human Judgements](http://ceur-ws.org/Vol-931/paper8.pdf). 2nd Workshop on Awareness and Reflection in Technology-Enhanced Learning. 7th European Conference on Technology-Enhanced Learning (pp. 101–116). Saarbruecken, Germany.