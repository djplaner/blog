---
title: Wicked problems, requirements gathering and the LMS approach to e-learning
date: 2009-07-24 15:06:39+10:00
categories: ['chapter-2', 'design-theory', 'elearning', 'phd', 'psframework', 'quotes', 'thesis']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: The dissonance between the constructivist paradigm and institutional e-learning
        &laquo; The Weblog of (a) David Jones
      author_email: null
      author_ip: 72.233.96.144
      author_url: https://djon.es/blog/2011/03/02/the-dissonance-between-the-constructivist-paradigm-and-institutional-e-learning/
      content: '[...] a completely different set of processes that is overly teleological
        and can really only ever engage in interaction and negotiations at the strategic
        level. There&#8217;s much more to say here, but for another [...]'
      date: '2011-03-02 21:57:47'
      date_gmt: '2011-03-02 11:57:47'
      id: '2654'
      parent: '0'
      type: pingback
      user_id: '0'
    
---

See also: [[blog-home | Home]]

Increasingly, the IT requirements of organisations are being met through the application of "enterprise systems". Large systems created by commercial vendors (though increasingly there are also open source variants, which while offering small improvements still suffer some of the same problems) that are meant to provide an integrated solution to a large scale system with an appraoch that combines "best practice" processes and techniques with information technology that will "scale" to meet the requirements of the organisation. Examples including ERP systems like Peoplesoft for finance, human resources and, at universities, student enrolment. In terms of e-learning at Universities the current dominant approach is also to employ "enterprise systems". With e-learning the "enterprise system" is known as the learning management system (lms), course management system (cms), virtual learning environment (vle) or some other 3 letter acronym. Examples include: Blackboard, Moodle and Sakai.

In this context, based on the experience and observations of myself and colleagues from around the world, I'm suggesting the following as a nascent (and fairly cynical) process model for how IT departments approach development of feature requests from users. Have you got any additional steps you'd like added?

The process model is

- Ignore the request.
- Explain that the request can't be done.
- Explain to the requester how the same outcome can be achieved using another process within the existing system. The suggested approach will be so time and resource consuming for the requester that they are unlikely to use it.
- Explain how the cost and resource implications of the request mean it can't be implement at this point in time.
- Explain how, given the need to upgrade to the next version of the enterprise system, IT needs to spend all of its technical resources on upgrading to the next version and consequently can't implement the request feature.
- Funnel the request through a reference group, project board or governance committee who are meant to identify whether or not the request is sensible and worth expending scarce resources. Such groups are usually made up of users - usually management or innovative end-users - and IT people. The user representatives usually have no IT knowledge and have to rely on the objective expert knowledge of the IT people.
- Explain how the given feature doesn't neatly fit within the model on which the enterprise system is built and how that would require IT to extend the enterprise system beyond "vanilla" and that it can't do that. Since, if it goes beyond vanilla the next time it has to upgrade to the next version of the enterprise system it will have to re-implement the feature request, and that's expensive.
- If we get to this stage, the feature request might be implemented. The first stage of this implementation will be to funnel the request to a business analyst who will be tasked to determine the complete requirements for the request. The business analyst will, at the start of this project, usually have no knowledge of the business (e.g. the nature of learning and teaching) or of the technology that will be used to implement the feature. They are meant to develop an objective and complete set of requirements that doesn't need to be sullied by additional knowledge.
    
    It is highly likely that the implementation will not be completed due to a range of factors.
    

So, in an enterprise system environment, I would suggest that it is highly unlikely that any feature request from a coal-face user will be implemented. If the request originates from someone important within the organisation, chances are that it won't be implemented either, but it will go a slightly different route (e.g. it probably won't have to go to the reference group).

But even if the request makes it all the way to the final step, there's a problem.

### Fundamental difficulty in establishing system requirements

The following is a quote from Sommerville (2001, p32). This is the 6th edition of one of the standard textbooks on software engineering. This is what it has to say about establishing system requirements.

> A fundamental difficulty in establishing system requirements is that the problems which complex systems are usually built to help tackle are usually 'wicked problems' (Rittel and Webber 1973). A 'wicked problem' is a problem which is so complex and where there are so many related entities that there is no definitive problem specification. The true nature of the problem only emerges as a solution is developed.

This is the source of the well known problem in software engineering - "The user won't know what they want until they see it, and then they will want something different to what they told you during the requirements gathering stage". This is the reason why the business analyst approach and the related teleological approach to systems development is deeply flawed in just about any context, but especially those that are diverse and less than stable.

I'm hard pressed to think of any context that is more diverse and less stable than that involved with the implementation of e-learning within a university.

### Disclaimers

I know of any number of really talented, nice people that work within IT departments and are driven to provide the best service they can to their clients. I've also seen a few that are not so nice, talented or appropriately motivated.

Personally, I don't believe in universal models. I don't think that all systems/institutions use the model above. I do think, in some situations, that the above model might be appropriate - not just e-learning. However, most IT departments profess a belief in universal models (i.e. single templated processes to implement any system regardless of its type). Most profess that you must generate requirements and only then start implementation, get sign off and then don't touch the system for years. They don't see the need for alternatives, in some situations.

Yes, I have developed alternate solutions or approaches. I'm not just being critical.

### References

Rittel, H. W. J. and M. M. Webber (1973). "Dilemmas in a general theory of planning." Policy Sciences 4(2): 155-169.

Sommerville, I. (2001). Software Engineering, Addison-Wesley.