---
title: Exploring options for teacher DIY learning analytics
date: 2017-10-07 08:24:07+10:00
categories: ['4paths', 'indicators']
tags: ['teacherdiy']
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: Tony Hirst
      author_email: tony.hirst@open.ac.uk
      author_ip: 109.157.179.139
      author_url: http://blog.ouseful.info
      content: 'Quick comments about my perspective/take on this stuff... Main question
        for me is: are there simple setups that let us distribute a small text file or
        small zip file that can be used to fire up pre-configured software environments
        on arbitrary machines by novice users.
    
    
        Patterns I''ve explored:
    
    
        - virtualbox+vagrant: ideally, you then just give a user a Vagrantfile and a shortcut
        that runs "vagrant up" and it launches a VM containing one or more linked applications.
        The VM can be headless (as per our TM351 VM, which exposes Jupyter notebook and
        OpenRefine to user via a browser on their desktop, and also sets up postgres and
        mongo inside the VM that can be accessed by Python executed via notebook) or provide
        a graphical desktop (as per the V-REP demo).
    
        - kitematic: prebuild a docker image pushed to dockerhub then let someone run
        it using kitematic; requires docker + kitematic to be installed; best for headless
        services; if you want app UI, requires x11 client and config nastiness on host.
    
        - docker-compose: this requires command line - share a docker-compose yaml file,
        which the auto pulls prebuilt containers pushed to dockerhub and links them together.
    
        - O''Reilly Launchbot - put dockerfile + seed files/notebooks in a github repo;
        user pulls down this repo and launches a docker container defined by the repo.'
      date: '2017-10-17 01:43:06'
      date_gmt: '2017-10-16 15:43:06'
      id: '10030'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: admin
      author_email: davidthomjones@gmail.com
      author_ip: 139.86.69.39
      author_url: null
      content: Tony thanks for sharing the patterns in the comment (and sharing more broadly
        on your blog, much appreciated).  The patterns will be very useful.  Finding a
        good fit will be one of the road to cross soon.  We're also going to have to factor
        in working around the absence of administrator rights on an institutional Windows
        MOE.
      date: '2017-10-17 09:01:19'
      date_gmt: '2017-10-16 23:01:19'
      id: '10049'
      parent: '10030'
      type: comment
      user_id: '1'
    
pingbacks:
    []
    
---

See also: [[blog-home | Home]]

A few of us recently submitted a paper to [ALASI'2017](http://itali.uq.edu.au/alasi2017) that examined a "case study" of a teacher (me) engaging in a bit of DIY learning analytics. The case was used to drawing a few tentative conclusions and questions around the institutional implementation of learning analytics. The main conclusion is that teacher DIY learning analytics is largely ignored at the institutional level and that there appears to be a need and value to support it. The question is how (and then if supported, what happens)?

This post is the start of an exploration of some technologies that combined may offer some of the affordances necessary to supporting teacher DIY learning analytics. The collection of technologies and the approach owes a significant amount of inspiration to [Tony Hirst](https://blog.ouseful.info/about/), especially in [this post](https://blog.ouseful.info/2017/06/27/byoa-bring-your-own-aplication-running-containerised-applications-on-the-desktop/) in which he writes

> What I care about are some of the features that Docker has, and how I can use those features to make my own life easier, ... supporting personal, DIY, BYOA (“bring your own app”) IT that works at an individual level in the form of end-user applications, or personal digital workbenches

The plan/hope here is that Docker combined with some other technologies can provide a platform to enable a useful combination of do-it-with (DIW) and do-it-yourself (DIY) paths for the institutional implementation of learning analytics. The follow is mostly documenting ad hoc exploration of the technologies.

In the end, I've been able to get working a Jupyter notebook working as a JSON API and started explorer docker containers. Laid the ground work for the next step which will be to explore how and if some of this can be combined to integrate some of the work Hazel is doing with [some of the Indicators work from earlier in the year](http://djon.es/blog/2017/03/13/sharing-indicators-platform-via-github/).

## Learning more - Juypter notebook JSON api

Tony provides [a description](https://blog.ouseful.info/2017/09/06/building-a-json-api-using-jupyer-notebooks-in-under-5-minutes/) of using Jupyter Notebooks to provide a JSON API. Potentially this provides a way for DIY teachers to create their own [MAV-like server](https://github.com/damoclark/mav-enterprise).

[Tony's exploration](https://blog.ouseful.info/2017/09/06/building-a-json-api-using-jupyer-notebooks-in-under-5-minutes/) is informed by [this](http://blog.ibmjstart.net/2016/01/28/jupyter-notebooks-as-restful-microservices/) from some aspect of IBM that aims to introduce the [Jupyter kernel gateway (github repo)](https://github.com/jupyter/kernel_gateway)

The README.md from [github repo](https://github.com/jupyter/kernel_gateway) mentions serving HTTP requests from "annotated notebook cells". Suggesting that the method of annotation will be important. The [IBM example code](https://github.com/jupyter/kernel_gateway_demos/blob/master/scotch_demo/notebooks/scotch_api_python.ipynb) that each API call is handled by a particular block starting with an appropriately formatted comment i.e.

> single-line comments containing a HTTP verb ... followed by a parameterised URL path

Have a simple example working.

## Deploying - user experience

The IBM bit then goes about using Docker to to deploy this API. But before I do that. Lets get some experience at the user en with [Tony's example](https://github.com/psychemedia/ou-robotics-vrep/tree/master/robotVM).

1. [Install VirtualBox](https://www.virtualbox.org/wiki/Downloads) _Question:_ Is this something a standard user can do?
2. [Install vagrant](https://www.vagrantup.com/downloads.html)
3. command line to install a vagrant plugin
    
    _Question:_ Too much? But can probably be worked around.
    
4. Download the repo as a zip file.
    
    Had to figure out to go back to the repo "home" to get the download option (long time between drinks doing this).
    
5. Run the vagrant file
    
    Ok, it's downloading the file from the vagrant server (from [the ouseful area](https://app.vagrantup.com/ouseful/) on Vagrant).
    
    It's a 1.66Gb file. That size could potentially be an issue, suggesting the need for a local copy. Especially given the slow download.
    
    An hour or two later and it is up and running. There's a GUI linux box running on my Mac.
    

Don't know a great deal about the application that is the focus, but it appears to work. It's a 3D application, so the screen refresh isn't all that fast. But as a personal server for DIY teacher analytics, it should work fine, at least in terms of speed.

Running it a second time includes a check to see if it's up to date and then up it pops.

The box appears to have Perl, Python and Juypter installed.

## Deploying - developing a docker/container/images

This raises the question of the best option for creating and sharing a docker/container/_insert appropriate term_ - I'll go with images - that has Jupyter notebooks and the kernel\_gateway tool running. At this stage, this purpose seems best served by a headless virtual machine with browser-based communication the method for interacting with Jupyter notebooks.

Tony appears to do exactly this (using OpenRefine) using Kitematic in [this post](https://blog.ouseful.info/2017/06/27/byoa-bring-your-own-aplication-running-containerised-applications-on-the-desktop/). Later in the post the options appear to include

- Sharing images publicly via the Dockerhub registry
- Use a private Dockerhub registry (one with the free plan)
- On a local computer
- Run your own image registry
- And, I assume use an alternative.

Tony sees using the command line a draw back for running your own. Perhaps not the biggest problem in my case. But what is the best approach?

[Dockerhub](https://docs.docker.com/docker-hub/) and its ilk do appear to provide extra help (e.g. official repositories you can build upon).

[One set of alternatives](https://www.slant.co/options/8674/alternatives/~docker-hub-alternatives) appear largely focused on supporting central IT, not the end user. Echoing a concern expressed by Tony.

[Intro from another alternative](https://sloppy.io/gitlab-container-registry-alternative-docker-hub/) suggests that docker is becoming more generic. Time to look and read further afield.

### Intro to containers

[From Medium](https://medium.com/flow-ci/introduction-to-containers-concept-pros-and-cons-orchestration-docker-and-other-alternatives-9a2f1b61132c)

- Containers abstract the OS etc to make it simple to deploy
- Containers usually measured in 10s of megabytes
- Big distinction made between containers and virtual machines, perhaps boils down to "containers virtualise the OS; virtual machines the hardware"
    
    Though interesting, the one tried above required the downloading of a virtual machine first. _Update:_ That appears to be because I'm running Mac OS X. If I were on a Linux box, I probably wouldn't have needed that.
    
- The following seem to resonate most with the needs of teacher DIY learning analytics
    
    > - Using containers can decrease the time needed for development, testing, and deployment of applications and services.
    > - Testing and bug tracking also become less complicated since you there is no difference between running your application locally, on a test server, or in production.
    > - Container-based virtualization are a great option for microservices, DevOps, and continuous deployment.
    
- Docker is based on Linux and open source, is the big player.
- Spends some attention on container orchestration - appears to be focused on enterprise IT.

Following offers a creative intro to Kubernetes

https://youtu.be/4ht22ReBjno

Starts with the case for containers (Docker), but then moves onto orchestration and the need for Kubernetes. Puts containers into a pod, perhaps with more than one if tightly coupled. Goes onto to explain the other features provided by Kubernetes.

And intro to Docker

https://www.youtube.com/watch?v=RyxXe5mbzlU

## Rolling my own

Possible technology options

- [Docker toolbox](https://www.docker.com/products/docker-toolbox)
    
    Though that appears to [be deprecated](https://docs.docker.com/toolbox/overview/)
    
- [Docker for Mac](https://www.docker.com/docker-mac) (and a version for Windows)
    
    Download it; test it...all works
    

Do the following and I have a web server running in Docker that I can access from my Mac OS browser.

```
AA17-00936:docker david$ docker run -d -p 80:80 --name webserver nginx
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
afeb2bfd31c0: Pull complete 
7ff5d10493db: Pull complete 
d2562f1ae1d0: Pull complete 
Digest: sha256:af32e714a9cc3157157374e68c818b05ebe9e0737aac06b55a09da374209a8f9
Status: Downloaded newer image for nginx:latest
f1f6925acc31f80faf726358f8de5712458ff3649d2c0626bf3bb37f11d1b070
AA17-00936:docker david$ 

```

### Dig into tutorials and have a play

Docker share a [git repo](https://github.com/docker/labs/) for tutorials and labs. Which are quite good and useful.

[Getting set up](https://github.com/docker/labs/blob/master/beginner/chapters/setup.md) with some advice above.

[Running your first container](https://github.com/docker/labs/blob/master/beginner/chapters/alpine.md) includes some simple commands. e.g. to show details of installed images. Showing that they can be quite small.

_Question:_ To have folk install Docker, or do the VM route as above?

```
AA17-00936:docker david$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu              latest              2d696327ab2e        11 days ago         122MB
nginx               latest              da5939581ac8        2 weeks ago         108MB
alpine              latest              76da55c8019d        2 weeks ago         3.97MB
hello-world         latest              05a3bd381fc2        2 weeks ago         1.84kB

```

[Web apps with docker](https://github.com/docker/labs/blob/master/beginner/chapters/webapps.md), which also starts looking at the process of rolling your own.

This is where discussion of different types of images commence

- Base (e.g. an OS) and child images which add functionality to a base image
- Official images - sactioned by docker
- user images

Process can be summarised as

- Create the app (example is using a Python web framework - Flask)
- Add in a _Dockerfile_ - text file of commands for the Docker daemon when creating an image
- Build the image
    
    Does require an account on the Docker cloud
    
    And there it goes getting all the pre-reqs etc. Quite quick.
    

And successful running.

[Docker Swarm](https://github.com/docker/labs/blob/master/beginner/chapters/votingapp.md) running multiple copies, including on the cloud. Given the use case I'm interested in is people running their own...not a priority.

It does provide a look at Docker Compose files and a more complex application - multiple containers and two networks. Given my focus on using Jupyter Notebooks and perhaps the kernel gateway, this may be simplified a bit.

Seems we're at the stage of actually trying to do something real.

### Create a Docker image - TDIY

Jupyter Notebook, kernel gateway and a simple collection of notebooks - perhaps with greasemonkey script

## Misc. related stuff

[Bit on microservices](https://medium.com/flow-ci/a-simple-introduction-to-microservices-a69446d2c211) (microservice architectural style) pointing out the focus on

> principles of loose coupling and high cohesion of services

and in turn a number of characteristics

- Applications are made up of small independent services
    
    Is TDIY LA about allowing teachers to create applications by combining these services?
    
- Services are independently modifiable and (re)deployable
    
    But by whom?
    
- Decentalised data management: each service can have its own database
    
    What about each user?
    

Goes on to list a range of advantages, but the disadvantages include

- inefficiency - remote calls, network latency, potential duplication etc.
    
    But going local might help address some of this.
    
- _Developing a user case could need the cooperation of multiple teams_
    
    This is the biggest barrier to implementation within an instituiton. But raises the spectre of shadow systems, kludges etc.
    
- complications in debugging, communication

[Microservices and containers](https://www.infoq.com/articles/container-landscape-2016) covers some of the alternatives.

Seems docker is the place -- it's bought Kitematic and apparently not loved it - a risk for basing the DIY approach on it.

> Another part of the story is that you can build your own images and either share them publicly via the Dockerhub registry, keep them locally on your own computer, post them to a private Dockerhub repository (you get a single private repository as part of the Dockerhub free plan, or can pay for more…), or run your own image registry.

[Dockerhub](https://hub.docker.com/) is probably the option I want to use here because of the focus on being open, of being cross institutional etc.