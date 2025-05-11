---
categories:
- eei
date: 2019-02-10 16:38:10+10:00
next:
  text: Exploring knowledge reuse in design for digital learning
  url: /blog2/2019/02/24/exploring-knowledge-reuse-in-design-for-digital-learning/
previous:
  text: Improving reuse of design knowledge in a LMS
  url: /blog2/2019/01/30/improving-reuse-of-design-knowledge-in-a-lms/
title: "Digital learning templates \u2013 adding context and configuration"
type: post
template: blog-post.html
---
[My last post](/blog2/2019/01/30/improving-reuse-of-design-knowledge-in-a-lms/) introduced some early steps in exploring how to increase the reuse of design knowledge in design for digital learning (i.e. designing course websites). That post outlined the specific problem, the solution and linked it to work on constructive templates and patterns from the Hypermedia Design literature (Nanard, Nanard and Kahn, 1998). It closed with observing how the current solution was limited. It only provided scaffolding for the act of creating/implementing the specific design. It didn’t offer any affordances for the local context or design for configuration. This post details some early work to address this.

### Reminder of the card interface “template”

Figure 1 shows the particular “template” that I’ve been working on. At the top of Figure 1 is the the card interface which the template generates. Below the card is the “normal” Blackboard content. This content is what the course designer provides. The “template” transforms that content into the card interface. If you were viewing (rather than editing) this page in Blackboard, then you would only see the card interface.

All well and good, it’s pretty and contemporary enough, but there’s a problem.

![](images/MAAAAAElFTkSuQmCC) Figure 1: An initial card interface, including user entered data

### The challenge of rolling over

At the moment we are designing courses and their learning enviromment for the initial offering of the courses in trimester 1, 2019. As a result, the dates we’re putting into the cards are for trimester 1, 2019. That’s fine for the course participants in trimester 1, 2019. But since we hope that these course designs will be reused (perhaps tweaked a bit) in subsequent trimesters (e.g. trimester 1, 2020) our focus on dates for trimester 1, 2019 causes a problem for those subsequent trimesters.

When the course content is rolled over for the next offering, the course convenor will need to manually edit each of the dates to align them with the dates for that trimester. This is not a huge task but it is one more task a busy course convenor has to remember. Another task that consumes cognitive load and reduces the time and head space available for focusing on student learning.

Goodyear and Dimitriadis (2013) argue that design for learning should “look forward – further forward than convention supposes” (np). They argue that design for learning needs to include careful consideration of the design features that will be required to support four different types of design. One of the types of design they identify is _design for configuration_. Configuration is described as what participants in learning (students, teachers and other agents) do to modify what has been designed to suit specific needs. For example, what features can we add into the card interface to support those actions a teacher might need to do to prepare the learning environment for the next offering of the course?

### Use trimester week numbers to specify the date

The institution has [an academic calendar](https://www.griffith.edu.au/__data/assets/pdf_file/0031/326488/2019-Academic-Calendar.pdf) that explicitly numbers each week of the trimester. These trimester numbers are used actively in other learning and teaching practices and artefacts. For example, the institutional course time table lists teaching sessions by the weeks they occur in (e.g. Weeks 1-7, 8). Beyond this the use of trimester weeks has become internalised for some staff and students. For example, Figure 2 represents the way one course convenor modified the use of the card interface in their course. In interacting with the card interface the convenor found it difficult to match the dates on the cards against the semester. The convenor was used to thinking in week numbers. Not dates. Hence the addition of “Week 3” into the title of the card (in the actual course site, the week had been added to most cards).

![](images/JM5eFhz+nwkAAAAASUVORK5CYII=) Figure 2: Course convenor added week number to card title

Rather than the course convenor manually add the trimester week numbers. Why not modify the card interface so they can use the week numbers to specifiy the date? Why not include the week number in the date badge on the card?

Not only would this fit with the common institutional practice of using trimester weeks to identify when modules/learning activities occur. It would also provide support for rolling over (design for configuration). When a card interface is rolled over into a different trimester the card interface will know the new set of dates for that trimester and can automatically use the appropriate dates. It supports the reuse of design knowledge and thus reduces the cognitive load and set of tasks required of the course convenor.

### Implementation

Figure 3 shows the current card interface’s support for using the trimester week numbers. The card at the top shows that both the Week number and the actual date are included in the date label in the top right hand corner of the card. (Some have commented that the date label is getting quite large. If this becomes a major issue it could be addressed by offering different versions of the label. I’ll pick this up more in a subsequent post). Below the card you will see the content provided by the course designer. Note that the date is now specified by providing a week number.

![](images/B5h3wHRAddHBAAAAAElFTkSuQmCC) Figure 3: Card with date specified by using institutional trimester week number

Currently the card interface supports either the original date format (see first card image in this post) or the week format. Figure 3 shows that the course designer has entered _Card Date: Week 3_ into the Blackboard content item. The card interface tweak transforms this into the card interface. If the card interfaces detects a week format for the date, the card interface checks an internal data structure for the course trimester to find the start and end dates for the matching week number. These dates are then displayed.

Of course, there is another problem with this approach.

## Manual entry, interoperability, legos, mashups and the NGDLE

The only official source of dates for trimester weeks I’ve been able to find so far is a PDF document. Actually, [it’s a collection](https://www.griffith.edu.au/academic-calendar-key-dates) of seven PDF documents per year. Since it’s a PDF I have to manually enter the dates from the PDF into the code. A manual process is bad. It’s especially bad when the institution has seven different academic calendars and it appears many different possible semester/trimester/term combinations. It would be great if there was an API I could call to get the data. After all, the Blackboard course identifiers specify which of the many different types of “trimester” the course is running in.

A key functional area – it’s even identified as the “linchpin” (Brown et al, 2015, p.4) - in EDUCAUSE’s conception of the Next Generation Digital Learning Environment (NGDLE) is interoperability. The implementation of the NGDLE is premised on a “Lego” approach where specifications allow different components to be connected into unique assemblages. Brown et al (2015) suggest that the mashup - “a web page or application that ‘uses content from more than one source to create a single new service displayed in a single graphical interface’” (p. 3) – maybe the model for the NGDLE architecture.

The card interface is increasingly becoming a mashup of data from different sources. Hopefully a mashup that makes it easy to reuse a range of knowledge in the design of quality digital learning envrionments. The absence of institutional specifications (APIs) that allow the reuse of institutional information and knowledge is a drag on what can be done. Arguably an indicator that the NGDLE concept has yet to have impact.

We’ll need to follow up on this.

### References

Brown, M., Dehoney, J., & Millichap, N. (2015). [_The Next Generation Digital Learning Environment: A Report on Research_](https://www.digitallernen.ch/wp-content/uploads/2016/02/eli3035.pdf). ELI Paper, Educause. Louisville, CO

Goodyear, P., & Dimitriadis, Y. (2013). In medias res: reframing design for learning. _Research in Learning Technology_, _21_, 1–13. [https://doi.org/10.3402/rlt.v21i0.19909](https://doi.org/10.3402/rlt.v21i0.19909)

Nanard, M., Nanard, J., & Kahn, P. (1998). Pushing Reuse in Hypermedia Design: Golden Rules, Design Patterns and Constructive Templates (pp. 11–20). ACM.