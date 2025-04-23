---
title: The product component of the Ps Framework
date: 2009-08-19 21:36:38+10:00
categories: ['chapter-2', 'design-theory', 'elearning', 'phd', 'psframework', 'thesis']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

This post contains the start of the Product component of the Ps Framework that forms a section out of chapter 2 of [my thesis](/blog2/research/phd-thesis/).

### Product

> Technology is a tool and like all tools it should fit your hand when you pick it up, you shouldn’t have to bio-re-engineer your hand to fit the tool. – Dave Snowden

E-learning, as used in this thesis, draws on the definition provided by the OECD (2005) where e-learning is defined as "the use of information and communications technology to enhance and/or support learning in tertiary education". The purpose of the Product component of the Ps Framework and this section is to examine the nature of the information and communications technology – the product – used to implement e-learning within universities. Due to its pre-dominance within university e-learning, the emphasis will be on the class of integrated enterprise system known alternatively as the Course Management System (CMS), Learning Management System (LMS) or the Virtual Learning Environment (VLE).

This section first briefly examines some literature from information systems and more broadly about conceptions of technology and the information technology artifact (Section 2.1.1). It will then more onto to examine more closely the nature and characteristics of the technology currently used to support e-learning within universities (Section 2.1.2), before examining in detail some of the limitations of that technology (Section 2.1.3) and examining some alternatives (Section 2.1.4). Lastly, it seeks to draw some lessons for e-learning from this discussion of the Product component of the Ps Framework (Section 2.1.5).

### Conceptions of technology

Bringing to the surface the common assumptions can be particularly useful in the design and implementation of a system – like e-learning within a university – in order to identify where stakeholder frames may be incongruent and internally inconsistent (Orlikowski and Gash 1994). In the past, and especially within the implementation of e-learning within universities, information technology has been taken for granted or assumed to be unproblematic. Such techno-rational conceptions illustrate a quite narrow perspective of what technology is, how it has effects and how and why it is implicated in social change (Orlikowski and Iacono 2001). Conceptions of technology within the practice of e-learning at universities appears particularly limited when it is observed that the almost universal university approach to e-learning has been the adoption of a particular type of system (Salmon 2005; Feldstein 2006; Jones and Muldoon 2007). This section seeks to briefly examine the variety of conceptions of technology found in the literature.

Gana and Fuentes (2006) identify two different ways of understanding technology and its management within society:

1. technology as neutral; and  
    The development of technology follows a linear process and oriented towards efficiency and economic yield through the application of technical rationality that can only be understood and applied by experts with adequate specialised understanding.
2. technology as a social activity.  
    Decisions about technology cannot be based exclusively on specialised technology knowledge but is instead a shared activity attempting to made sense of a complex array of forces arising from development being intrinsically woven together with society and social actors.

In examining conceptions of causal agency in the literature on information technology and organisational change, Markus and Robey (1988) identify three conceptions:

1. the technological imperative;  
    Technology is seen as an exogenous force which determines or at least strongly constrains the behaviour of individuals and organizations. Information technology is seen as shaping organizations, its processes and jobs. Empirical research has generated contradictor findings and it has been proposed that contingencies affect the relationship between information technology and structural change.
2. the organisational imperative; and  
    Assumes that organizations and the people within them have almost unlimited choice over technological options and almost unlimited control over the consequences. This perspective assumes that human actors rationally design information systems to satisfy organisational requirements. It assumes that system designers and management are able to manage the impacts of systems by paying attention to both technical and social concerns. Empirical support is limited and most studies fail to assess designers' intentions and are consequently not complete tests of this imperative.
3. the emergent perspective.  
    Holds that the uses and consequences of information technology emerge unpredictably from complex social interactions. Central to this perspective are the role of computing infrastructure, the interplay of conflicting objectives and preferences, and the operation of non-rational objectives and choice processes. This perspective refuses to acknowledge a dominant cause of change, instead prediction requires detailed understanding of dynamic organisational processes, the intentions of actors and features of information technology.

Sproull and Kiesler (1991) draw on the history of prior technology to develop four points useful in thinking about the potential consequences of new communication technologies. These points are:

1. Full possibilities of new technology are hard to foresee;  
    Inventors and early adopters tend to emphasise the planned uses and under-estimate second-level effects.
2. Unanticipated consequences arise from interactions;  
    Efficiency effects have less to do with developing unanticipated consequences of technology than the changing of interpersonal interactions, social organisation, work procedures and ideas about what is important.
3. Second-level effects often emerge slowly; and  
    Such effects tend to arise only after people begin over time to understand, reflect and renegotiate changed patterns of behaviour and thinking.
4. Second-level effects are not determined by technology.  
    Rather than arising from autonomous technologies operating on a passive organisation or society, second-level effects are construct as technology interacts with, shapes, and is shaped by the social and policy environment.

In examining the information systems research literature – in the form of the 1888 articles published within the journal Information Systems Review from 1990 through 1999 - with the intent of discovering what IS researchers had done with the alternative conceptualisations of technology given in the 1980s – such as that given by Markus and Robey (1988) – Orlikowski and Iacono (2001) identified 14 specific conceptualisations of information technology. They clustered these into five broad meta-categories:

1. tool view of technology;  
    Representing the common and received understanding of technology as the engineered artifact, expected to do what was intended by its designers. A focus largely on technical issues independent of social or organisational arrangements within which it is developed and used.
2. proxy view of technology;  
    Attempts to capture critical aspects of information technology through the use of a surrogate and usually quantitative measure such as individual perceptions, diffusion rates or dollars spent.
3. ensemble view of technology;  
    Technology is seen as only one element of a package or web of components that are necessary in order to apply technology to some socio-economic activity. All variants of this view focus on the dynamic interactions between people and technology at various stages of its construction, implementation and use.
4. computational view of technology;  
    A view that focuses on the capabilities of technology represent, manipulate, store, retrieve and transmit information in support of processing, modelling or simulating aspects of the world. Typically focusing on the development of algorithms or models.
5. nominal view of technology: technology as absent.  
    Where technology is incidental or act as background information. The focus is on topics of interest to the IS field but with not specific connection with technology.

An initial change in technology can set the direction of a deviation-amplifying spiral, however, humans can affect technology design and policy and therefore influence second-level effects (Sproull and Kiesler 1991). Management, those responsible for creating the environment in which an organization operates, tends to concentrate on efficiency effects (Sproull and Kiesler 1991; Lacity and Hirschheim 1993). Such a focus can limit the level of disruption caused by information technology and its second-level effects contributing to the maintenance of the status quo. It is not uncommon for adoption of new technological opportunities which significantly deviate from the established socio-technical profile of a sector to be slow (Dolata 2009). Table 3.1 summarises perspectives about information technology, its purpose and the likelilood of sustaining or disruptive innovation (Christensen 1997).

Table 3.1 – Sustaining and disruptive perspectives of information technology
| Source | Sustaining | Disruption |
| --- | --- | --- |
| Strategic information systems (Clark 1994) | For automation and office support | As a source of strategic advantage |
| Communications technologies, networked organisation (Sproull and Kiesler 1991) | Emphasizing efficiency effects | Enabler of previously impossible practices |
| Web-based teaching and learning (Hannafin and Kim 2003) | Harnessed to improve existing practices | Enabling significant transformation by embracing different world views |
| Technology, innovation and firms (Christensen 1997) | Sustaining – helping institutions improve existing products | Disruptive – change the standard, a different set of benefits at lower costs |

As shown in Table 3.1, in particular the Hannafin and Kim (2003) reference, various conceptions of information technology can be found within the literature associated with e-learning, some additional examples follow. It is most likely that technology will reinforce the old systems rather than the new paths (Lian 2000). Educators are likely to use the technology to do things the way they have always been done, but with new and more expensive equipment (Dutton and Loader 2002). Technology is not, of itself, liberating or empowering but serves the goals of those who guide its design and use (Lian 2000). The tools themselves are never value-neutral but are replete with values and potentialities which may cause unexpected responses (Westera 2004). The forms new media take are not technologically given, instead they are historically emergent and best understood by examining how social relations are inscribed in the technology and how the technology is shaped to provide specific functions (Adam 1998). The impact of new technologies depends crucially on the social context (Clegg, Hudson et al. 2003). While a e-learning system can be purported to support various aspects of learning, the reality is more complex, involving the context within which these systems are used and how they are adapted to specific student needs (Conole 2002).

The above brief examination of different conceptions of technology suggests that views of technology as neutral or deterministic are somewhat limited in the explanatory power. Instead, of quality e-learning arising simply out of the technology is unlikely. Instead the outcomes of e-learning are likely to arise in unpredictable and emergent ways out of the complex interplay between the technology, the organisation and the individuals. It also indicates that it is through this emergence that many unexpected effects arise and open up new possibilities.

### References

Adam, A. (1998). Artificial knowing: gender and the thinking machine. London, Routledge.

Christensen, C. (1997). The innovator's dilemma: when new technologies cause great firms to fail. Boston, Harvard Business Press.

Christensen, C. M. (1997). The Innovator's Dilemma: When New Technologies Cause Great Firms to Fail. Boston, Harvard Business School Press.

Clark, R. (1994, 14 July 1994). "The Path of Development of Strategic Information Systems Theory." 2003, from [http://www.anu.edu.au/people/Roger.Clarke/SOS/StratISTh.html](http://www.anu.edu.au/people/Roger.Clarke/SOS/StratISTh.html).

Clegg, S., A. Hudson, et al. (2003). "The Emperor's new clothes: globalisation and e-learning in higher education." British Journal of Sociology of Education **24**(1): 39-53.

Conole, G. (2002). "The evolving landscape of learning technology." ALT-J **10**(3): 4-18.

Dolata, U. (2009). "Technological innovations and sectoral change. Transformative capacity, adaptability, patterns of change: An analytical framework." Research Policy **38**(6): 1066-1076.

Dutton, W. and B. Loader (2002). Introduction. Digital Academe: The New Media and Institutions of Higher Education and Learning. W. Dutton and B. Loader. London, Routledge**:** 1-32.

Feldstein, M. (2006). Unbolting the chairs: Making learning management systems more flexible. eLearn Magazine. **2006**.

Gana, M. T. S. G. and L. A. T. Fuentes (2006). "Technology as 'a human practice with social meaning' - a new scenery for engineering education." European Journal of Engineering Education **31**(4): 437-447.

Hannafin, M. and M. Kim (2003). "In search of a future: A critical analysis of research on web-based teaching and learning." Instructional Science **31**: 347-351.

Jones, D. and N. Muldoon (2007). The teleological reason why ICTs limit choice for university learners and learning. ICT: Providing choices for learners and learning. Proceedings ASCILITE Singapore 2007, Singapore.

Lacity, M. and R. Hirschheim (1993). Information systems outsourcing: myths, metaphors and realities. Chichester,, John Wiley & Sons.

Lian, A. (2000). "Knowledge Transfer and Technology in Education: Toward a complete learning environment." Educational Technology & Society **3**(3).

Lian, A. (2000). "Knowledge transfer and technology in education: Toward a complete learning environment." Educational Technology & Society **3**(3): 13-26.

Markus, M. L. and D. Robey (1988). "Information technology and organizational change: causal structure in theory and research." Management Science **34**(5): 583-598.

OECD. (2005, 17 January 2006). "Policy Brief: E-learning in Tertiary Education."   Retrieved 5 December, 2006, from [http://www.oecd.org/dataoecd/55/25/35961132.pdf](http://www.oecd.org/dataoecd/55/25/35961132.pdf).

Orlikowski, W. and D. Gash (1994). "Technological frames: Making sense of information technology in organizations." ACM Transactions on Information Systems **12**(2): 174-207.

Orlikowski, W. and C. S. Iacono (2001). "Research commentary: desperately seeking the IT in IT research a call to theorizing the IT artifact." Information Systems Research **12**(2): 121-134.

Salmon, G. (2005). "Flying not flapping: a strategic framework for e-learning and pedagogical innovation in higher education institutions." ALT-J, Research in Learning Technology **13**(3): 201-218.

Sproull, L. and S. Kiesler (1991). Connections: new ways of working in the networked organization. Cambridge, MIT Press.

Westera, W. (2004). "On strategies of educational innovation: between substitution and transformation." Higher Education **47**(4): 501-517.