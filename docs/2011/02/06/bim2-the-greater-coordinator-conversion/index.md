---
title: "bim2: the greater coordinator conversion"
date: 2011-02-06 23:10:05+10:00
categories: ['bim', 'bim2']
type: post
template: blog-post.html
---
This tells the story of the conversion of the bim coordinator code into the new OO design being used for bim2.

### Design

The theory is that the code design should share a lot of similarity with the student interface and also some code.

First, a recap of how it works (solely for my benefit).

The main _view.php_ entry point for bim2 contains 3 lines of code 
```php
$factory = new bimtwo\_controller\_factory(); 
$controller = $factory->produce(); 
$controller->process(); 
```

The factory determines which of three types of user has requested the activity

1. coordinator;
2. marker; or
3. student.

Each user type has a controller object, the factory creates the appropriate object and _view.php_ calls that object's _process_ method.

The controller defines a hash called methods which associates a parameter called _tab_ (passed in from the URL) with a method in the controller. For students, it looks like this 
```php
$this->methods = array( 
    "default" => array( 
        "default" => "activity\_details" ), 
        "activity" => array( "default" => "activity\_details" ), "questions" => array( "default" => "questions" ), "posts" => array( "default" => "posts" ) ); 
```

Typically, there is a connection between the values of _tab_ and a tabbed interface for the user.

Typically, that method will create a model object that will generate some data and then create a view object. It will pass the model to the view and the view will display some output.

For example, here's the method for showing the questions for the activity to the students 
```php
function questions() { 
    require\_once "$this->view\_path/student/question\_details.php";
    $this->model = new question\_details( $this ); 
    $this->model->gather\_data(); 
    require\_once "$this->view\_path/student/question\_details\_view.php";
    $this->view = new question\_details\_view( $this ); 
    $this->view->display( $this ); 
} 
```

In theory, the _question\_details_ model object should be able to be re-used by the coordinator interface. Maybe even the view.

### Creating the dummy coordinator design - views

So the plan is to initially create a coordinator controller that displays the tabs etc, but simply displays "hello world" type messages for each tab. Once that's working, it's a matter of implementing the model and view objects for each tab - and also implementing the forms interface where required.

So, the simple first step is to copy the student controller and edit it. Done. So, now login as a coordinator and see if it works?

Yep, after a couple of syntax errors it is working. The coordinator controller methods are the bare minimum e.g.  
```php 
function configure() { 
    print "<h1> Configure </h1>"; 
}

function manage\_questions() { 
    print "<h1> Manage questions </h1>"; 
}
```

So, there are no proper Moodle header/footer and no proper tabbed interface. The construction of these is controlled by the views. So the next step is to create view classes for each of the methods that handle the header/footer/tabs but still only display the "hello world" type message. There is one view per controller method. Time to get that working.

The configure tab is a little different, in that it is meant to re-use a standard form/process for Moodle. Will leave that for later and get the other views working first. Manage questions first. Copy the student/posts\_view.php class over and edit that.

Yep, that all works. It does, however, reveal a couple of points to check, including:

- Currently, the view object has a _view\_header_ function that is repeated in each view object. I believe this can be inherited.  
    Actually, it can quite easily. Add a few lines to the parent view class and hey presto.
- The order in which the tabs being displayed is not in the order I'd prefer. Need to find out how to order tabs.  
    Leave this for now.

So, with the views relying on the parent for view\_header this is working for Manage questions. Now just to add it for all the others. Yep, that's all working, except for configure (and the order of the tabs which is annoyingly incorrect).

Apart from that, this has gone quite smoothly and quickly.

### Calling configure

Ahh, had a vague recollection that there was a specific edit form for configuration, and there is. But the solution adopted in bim (and to be repeated for bim2) is that the configure tab for the coordinator will show the details of the current configuration for this activity and include a link to the Moodle defined edit form to change the configuration.

The point to remember is that when a bim2 activity is first created, Moodle directs appropriately permitted users to the edit form. once configure it shows what I'm working on here.

Short story is that the configure tab is now different from the others in terms of view.

### Order of tabs

Ahh, a little bit of digging reveals that this is not a Moodle core problem. It's doing what should be done and retaining the order. It's the Moodle theme I was using that wasn't putting the tabs in the right order. Will have to let @rolley know.

Of course, the next step is to find a theme that does it properly. first attempt did it, but had too narrow a column and didn't handle the wrapping well. Somewhat influenced by my practice of keeping fairly narrow browser windows.

### Models and views

At this stage, the basic structure for the coordinator interface is there and working (if not doing anything useful).

The next step is to go through each controller method and

- Implement the model that gets the required data.
- Modify the view to display that data appropriately.
- Add the "form handling" extras where required.  
    For the coordinator, most of the methods will require some form handling, this makes things a little more complex.

I'll leave these for tomorrow. Each of these will take a bit of time, so will probably do them as separate posts.

### Update the student views

Before I finish, however, I need to update the student views to remove their specific _view\_header_ method and instead rely on the parent class based on what I added above.

Done, however, the activity\_details\_view is a little more complicated.