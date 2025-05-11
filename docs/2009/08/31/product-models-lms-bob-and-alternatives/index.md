---
categories:
- chapter-2
- design-theory
- elearning
- phd
- psframework
- thesis
coverImage: 3819172601_39a5a27300_o-scaled-e1590632325204.jpg
date: 2009-08-31 14:32:56+10:00
next:
  text: '"e&#038;i report #2 - 20th August - 1st September"'
  url: /blog2/2009/09/01/ei-report-2-20-25th-august/
previous:
  text: 'Procurement and software: alternate models for e-learning'
  url: /blog2/2009/08/31/procurement-and-software-alternate-models-for-e-learning/
title: Product models - LMS, BoB and alternatives
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Thoughts on &#8220;Insidiuous pedagogy&#8221; &laquo; The Weblog of (a)
        David Jones
      author_email: null
      author_ip: 66.135.48.206
      author_url: https://djon.es/blog/2009/10/06/thoughts-on-insidiuous-pedagogy/
      content: '[...] Adopt a best of breed approach for the CMS. [...]'
      date: '2009-10-06 11:07:39'
      date_gmt: '2009-10-06 01:07:39'
      id: '2738'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The following completes the "alternate models" section of the Product component started in a [previous post](/blog2/2009/08/31/procurement-and-software-alternate-models-for-e-learning/). It's a bit rough and ready, but hopefully good enough.

### Product models

The ERP market was one of the fastest growing and most profitable areas of the software industry during the last three years of the 1990s (Sprott 2000) and has tended to dominate the IT field (Light, Holland et al. 2001). It was at this same time – the late 1990s – that the availability of commercial LMS and their use within universities became increasingly prevalent. Perhaps then, it is not surprising that in terms of the underlying product model an LMS appears to be very close to that of a single-vendor Enterprise Resource Planning (ERP) system. In both cases, all the required functionality is provided in one, integrated package sourced from a single provider. In comparing the literature it is possible to see significant commonality between the advantages and disadvantages of an LMS and that of ERP system. The aim of this section is not to repeat the advantages and disadvantages of LMS – covered somewhat in the "LMS characteristics and limitations" section in Section 2.1.2 – or ERPs – covered in more detail in the relevant literature (Kallinikos 2004; Light 2005). It is instead to establish the existence of other potential product models and compare these with the ERP model. In addition, towards the end of this section the additional complicating and recent factor of user-owned technology is raised.

There are two approaches to the design of an LMS (Weller, Pegler et al. 2005):

1. monolithic or integrated approach; and  
    All common tools are provided by the one software package provided and supported by the one vendor. The predominant approach.
2. best of breed approach.  
    An alternative approach also termed a component or hybrid architecture. Aims to provide the same level of integration but the ability to select components that best suit the local context.

The same two approaches can be identified in the broader provision of enterprise information systems. It is possible to identify a reasonable spread of literature (Dewan, Seidmann et al. 1995; Geishecker 1999; Light, Holland et al. 2001; Hyvonen 2003; MacKinnon, Grant et al. 2008; Burke, Yu et al. 2009) examining various questions arising out of the difference between a monolithic ERP product model and the best of breed (BoB) model. This may not be all that surprising as such discussions have been billed as the "long-running debate" with the pendulum swinging from one view to the other and back again (Geishecker 1999). It is a debate that is encompassed be an even longer standing debate over the centralisation of decentralisation of computing, its focus on efficiency versus effectiveness and the supposed rational attempts at optimising the trade-off (King 1983). A debate that appears unresolvable due to the actual driving issues in the debate being the politics of organisation and resources and especially the apparently central issue of control (King 1983).

ERP adoption involves a centralised organisation of processes and a tendency to reduce autonomy and increase rigidity (Lowe and Locke 2008). Centralisation of control preserves top management prerogatives in most decisions, whereas decentralisation allows lower level managers discretion in choosing among options (King 1983). A BoB approach allows each department to select its own solution (Dewan, Seidmann et al. 1995). Light, Holland and Wills (2001) perform a comparative analysis of the ERP (monolithic or integrated) and best of breed (BoB) approaches to enterprise information systems and is summarised in Table 2.3.

Table 2.3 - Comparison of major differences between ERP and BoB (adapted from Light, Holland et al. 2001)
| Best of breed | Single vendor ERP |
| --- | --- |
| Organisation requirements and accommodations determine functionality | The vendor of the ERP system determines functionality |
| A context sympathetic approach to BPR is taken | A clean slate approach to BPR is taken |
| Good flexibility in process re-design due to a variety in component availability | Limited flexibility in process re-design, as only one business process map is available as a starting point |
| Reliance on numerous vendors distributes risk as provision is made to accommodate change | Reliance on one vendor may increase risk |
| The IT department may require multiple skills sets due to the presence of applications, and possibly platforms, from different sources | A single skills set is required by the IT department as applications and platforms are common |
| Detrimental impact of IT on competitiveness can be dealt with, as individualism is possible through the use of unique combinations of packages and custom components | Single vendor approaches are common and result in common business process maps throughout industries. Distinctive capabilities may be impacted on |
| The need for flexibility and competitiveness is acknowledged at the beginning of the implementation. Best in class applications aim to ensure quality | Flexibility and competitiveness may be constrained due to the absence or tardiness of upgrades and the quality of these when they arrive |
| Integration of applications is time consuming and needs to be managed when changes are made to components | Integration of applications is pre-coded into the system and is maintained via upgrades |

Even in 1983, over twenty-five years ago, it was recognized that the terrain in which to decide between centralized and decentralized computing was continually changing (King 1983). This change is driven in no small part by the changing nature of technology from main-frames to personal computers to managed operating environments. Similarly, the smaller discussion between ERP and BoB has also been influenced by changes in technology. In the early to mid-1980s, the mainframe-dominant market automatically defaulted to an integrated ERP approach (Geishecker 1999). Most recently integration technologies like web services and service-oriented architectures (SOA) are seen to be enabling the adoption of BoB approaches (Chen, Chen et al. 2003). Such approaches are having an impact within the LMS field with attempts at implement a BoB LMS being enabled by the development of service-oriented architectures such as that be JISC (Weller, Pegler et al. 2005). Such an approach may allow a more post-industrial approach to the LMS allowing the taking of parts that are needed, when they are needed and granting control where it is needed (Dron 2006). Bailetti et al (2005) report on an early system that uses web services to implement a BoB approach.

In general, however, discussion about and comparison between ERP and BoB approaches to enterpise systems suffer the same limitation as the discussion of procurement strategies in the previous section. They are still based on the assumption that it is the responsibility of the institution, and its information technology department, to select, own and maintain all of the information systems required by users. Web 2.0, e-learning 2.0 (Downes 2005) and the rise of social software requires that organization of e-learning moves beyond centralized and integrated LMS and towards a variety of separate tools which are used and managed by the students in relation to their self-governed work. (Dalsgaard 2006). Stiles (2007) argues that in the future organizational needs will be best met by a BoB approach, however student initiated processes will be done using their choice of tools and services. An approach that provides students with a tool-box of loosely joined small pieces (Ryberg 2008).

### References

Bailetti, T., M. Weiss, et al. (2005). An open platform for customized learning environments. International Conference on Management of Technology (IAMOT).

Burke, D., F. Yu, et al. (2009). "Best of Breed Strategies: Hospital characteristics associated with organizational HIT strategy." Journal of Healthcare Information Management **23**(2): 46-51.

Chen, M., A. Chen, et al. (2003). "The implications and impacts of web services to electronic commerce research and practices." Journal of Electronic Commerce Reseaerch **4**(4): 128-139.

Dalsgaard, C. (2006) "Social software: E-learning beyond learning management systems." European Journal of Distance Education **Volume**,  DOI:

Dewan, R., A. Seidmann, et al. (1995). Strategic choices in IS infrastructure: Corporate standards versus "Best of Breed" Systems. ICIS'1995.

Downes, S. (2005). "E-learning 2.0." eLearn **2005**(10).

Dron, J. (2006). Any color you like, as long as it's Blackboard. World Conference on E-Learning in Corporate, Government, Healthcare and Higher Education, Honolulu, Hawaii, USA, AACE.

Geishecker, L. (1999). "ERP vs. best-of-breed." Strategic Finance **80**(9): 62-67.

Hyvonen, T. (2003). "Management accounting and information systems: ERP versus BoB." European Accounting Review **12**(1): 155-173.

Kallinikos, J. (2004). "Deconstructing information packages: Organizational and behavioural implications of ERP systems." Information Technology & People **17**(1): 8-30.

King, J. L. (1983). "Centalized versus decentralized computing: organizational considerations and management options." ACM Computing Surveys **15**(4): 319-349.

Light, B. (2005). "Potential pitfalls in packaged software adoption." Communications of the ACM **48**(5): 119-121.

Light, B., C. Holland, et al. (2001). "ERP and best of breed: a comparative analysis." Business Process Management Journal **7**(3): 216-224.

Lowe, A. and J. Locke (2008). "Enterprise resource planning and the post bureaucratic organization." Information Technology & People **21**(4): 375-400.

MacKinnon, W., G. Grant, et al. (2008). Enterprise information systems and strategic flexibility. 41st Annual Hawaii International Conference on System Sciences, Waikoloa, Hawaii.

Ryberg, T. (2008). Challenges and potentials for institutional and technological infrastructures in adopting social media. 6th International Confernece on Networked Learning, Halkidiki, Greece.

Sprott, D. (2000). "Componentizing the enterprise application packages." Communications of the ACM **43**(4): 63-69.

Stiles, M. (2007). "Death of the VLE? A challenge to a new orthodoxy." Serials **20**(1): 31-36.

Weller, M., C. Pegler, et al. (2005). "Students' experience of component versus integrated virtual learning environments." Journal of Computer Assisted Learning **21**(4): 253-259.