---
title: Sharing "indicators platform" via github
date: 2017-03-13 15:16:32+10:00
categories: ['indicators']
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

Following on from [the last post](http://djon.es/blog/2017/03/12/jupyter-notebook-indicators-platform-baby-step-1-finding-an-orm/) the following documents how to share the "indicators platform" for analytics via github. It's largely intended to help @beerc. I doubt there's nothing (at the moment) that makes this inherently interesting for anyone else.

## End result

The (almost completely useless) end result of this work is [this github repository](https://github.com/djplaner/Indicators).

Hopefully, this will form a foundation that will help it get much more interesting, quickly.

## Jupyter notebooks and github

It's not straight forward to share Jupyter notebooks via github. At least if you wish to maintain privacy of the data.

For example, take a look at [the first version](https://github.com/djplaner/Indicators/blob/cfac4f395f061092eb84031af10279a2d5b80589/Home.ipynb) of the first notebook placed in the repository. Can you see all the programing error messages at the bottom of the page?

Had the SQL command just before this worked, it would contain actual data of real people. This would be bad.

This is because the raw json file that is the notebook will include the data. This is a good thing when you're viewing it on your computer. It's a bad thing when you're sharing it in a public space.

That's fixed in [a more recent version](https://github.com/djplaner/Indicators/blob/ccf46631208fd6b4b1b72a10316aa693526274ef/Home.ipynb).

To achieve this, it was necessary to [follow the instructions on this page](https://gist.github.com/pbugnion/ea2797393033b54674af), which involve

1. Installing a python script on your computer so it can be run.
2. Configuring git to use this script as a filter when sending stuff to github.
3. Configuring the meta-data for the notebook to ensure that the content of data blocks would be removed before going to github.
    
    Suggesting that this step would need to be repeated for each notebook likely to have personal information show up in the data.
    

### Testing that this works

My suggestion is

1. Follow the instructions below.
2. Modify the SQL in the notebook to make sure it generates an error (i.e. not real private data)
3. Commit and push the error version back to github

If no error data shows up on github, then it's working.

## How to use this repository

Basic process should be

1. Get your box set up to run Jupyter notebooks.
    
    It is generally, a [fairly simple process](http://jupyter.org/install.html)
    
2. Clone a copy of the github repository into the directory your notebooks are being stored - creating a directory called _Indicators_
    
    You might want to fork my repository first. This will give you your own github repository. We can then share good changes via pull requests.
    
3. Create a file called _config.json_ in the parent directory for _Indicators_ with the following content (changed to suit your Moodle database)
    
    ```
    {
      "drivername": "postgresql",
      "database": "",
      "username": "",
      "host": "localhost",
      "port": "5432",
      "password": ""
    }
    
    ```
    
4. Open up the notebook and run the cells.