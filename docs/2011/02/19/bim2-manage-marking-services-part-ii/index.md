---
title: "bim2: manage marking services - Part II"
date: 2011-02-19 07:00:42+10:00
categories: ['bim', 'bim2']
type: post
template: blog-post.html
---
Time to continue the implementation of support services for manage marking started in [the last post](/blog2/2011/02/17/bim2-manage-marking-support-services/). Services left to be implemented are

- Releasing marked posts.
- Registering a blog.

### Releasing marked posts

Standard order for this stuff

1. Controller.
2. Model.  
    In this case, the model will be making changes to the database and storing the outcome.
3. View.

#### Model

First, parse the parameters. There are two: marker and question. The possible combinations are

- question and marker empty == release all marked posts for this activity.
- question set only == release all marked posts for that question.
- marker set only == release all marked posts for that marker.
- marker and question = release all marked posts for that question and that marker.

So, have the model processing and updating the database. Also getting list of changes to report in the view.

The view will need to be able to translate student uid and question id into question title and user name. So need to include students and questions in the model.

#### View

A simple one, simply suggest success and summarise the changes made. Yep, all done. Need to do a bit more checking

### Misc bugs

On manage marking there are a couple of minor bugs to fix

- Empty table and email button showing up when there are no unregistered students.**FIXED**
- The "release" link is appearing within a question heading when there are no questions to release.  
    This one is probably going to be a bit more difficult to fix. Actually, the header code is correct in what it is doing. Time to check out how the rows are calculating whether there is anything marked. The display of marker details appears to be working, it's the calculating of the stats that seems to be letting itself down.
    
    Ahh, all that and it's not a code problem, but with the configuration of the users and course members. Mostly.
    

This is the type of bug that is going to have to be looked for in testing.

### Registering a blog

This allows the coordinator to register a blog for unregistered students. It is essentially the same as the process for a student to register, just a slightly different interface. Hopefully, there can be some significant code reuse. Let's look at how I did it for the student.

The student interface itself is a bit too complex. Registration is handled by some overly complex code within a method of one of the view. i.e. it's not that stand alone. It is complicated because it also includes processing of the form.

Am going to have to put this into a stand along object that can be easily called elsewhere like this \[code lang="php"\] $form = new process\_register\_form( $this->factory ); $form->process(); \[/code\]

There are going to have to be some differences between using it with a student and with a coordinator, including

- heading - this (including breadcrumbs) will have to change.
- return URL - successful processing generates a "return to ??", ?? will change based on where it's calling from.

In terms of the heading, it's even more complex as the student and coordinator should see radically different headings when this is called. In the end, the code looks like this \[code lang="php"\] $form = new process\_register\_form( $this->controller ); $form->set\_header( $this, "view\_header", "registeration" ); $form->set\_return( "?param=regOK&id=".$this->model->factory->cm->id); $form->display(); \[/code\]

The set\_header method is used to tell $form which function to call to display the header that is required. set\_return provides the URL params which let $form now where to redirect output when successfully registered.

So, time to add this in the appropriate place for manage\_marking. There is some difference here in that it's not being called from a view, but instead a controller. Another wrinkle to consider. Let's create a view just for register and stick the call in there, this allows the view to be handled.

Ahh, no another problem, the URL for the register your blog has to be updated. Ahh, that's the first parameter in the form. Done.

Next problem, when the student is registering their blog, the userid is based on their login, but that can't happen when the coordinator is doing it. Has to be based on the student parameter. So, will need to pass in the userid for the student with the blog to be registered as a parameter. So this means I need to

- Generate the form with an extra hidden parameter for coordinator. **done**
- Same for student - how do I get id of browser user? (this->factory->userid) **done**
- Modify processing of the form to use the hidden parameter. **done**

### What's next?

So, manage marking is essentially done. Time to move onto "Your students", some new code there, also a fair bit of work to do, but should get quicker.