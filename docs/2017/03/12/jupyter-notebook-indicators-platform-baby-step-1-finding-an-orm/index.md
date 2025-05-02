---
title: "Jupyter notebook indicators platform: Baby step #1 - Finding an ORM"
date: 2017-03-12 22:30:50+10:00
categories: ['indicators']
type: post
template: blog-post.html
---
[The last post](http://djon.es/blog/2017/03/12/playing-with-python-and-jupyter-notebooks-for-analytics/) documented early explorations of Jupyter notebooks ending with a simple query of a Moodle database. This post takes the first baby steps toward some sort of indicators platform using Jupyter notebooks, Python and github. The focus here is to find some form of ORM or other form of database independent layer.

**Problem:** the code from the last post was specific to Postgresql. If you're Moodle database is based on another database that code won't work. The aim here is to enable some level of sharing of code/analysis/indicators. This means needed a way to keep the code independent of database specifics. This is where [object relational mappers (ORMS)](https://www.fullstackpython.com/object-relational-mappers-orms.html) enter the picture. See [this](http://danielweitzenfeld.github.io/passtheroc/blog/2014/10/12/datasci-sqlalchemy/) for an argument why this is a good idea.

## Pandas and SQLAlchemy

[This book](https://books.google.com.au/books?id=f1F1CgAAQBAJ&pg=PA124&lpg=PA124&dq=python+pandas+database+independent&source=bl&ots=2Pg2BCCJTd&sig=rRj_Rbd9CWOsH8l-1Jlqf6nwXKU&hl=en&sa=X&redir_esc=y#v=onepage&q=python%20pandas%20database%20independent&f=false) offers some examples using sqlalchemy with pandas. A likely combination. [This sqlalchemy cheatsheet](https://github.com/crazyguitar/pysheeet/blob/master/docs/notes/python-sqlalchemy.rst) offers some useful examples.

Need to install sqlalchemy, it appears. Actually just updated

```
conda install -c anaconda sqlalchemy

```

Oh dear, time wasted. Needed to restart the notebook server after that.

Process is

1. Modify the config stuff to create an [sqlalchemy engine](http://docs.sqlalchemy.org/en/latest/core/engines.html).
2. Read the data

Ends up with the following code

```
import json

# Put the config outside the Indicators directory, keep it out of git
with open('../config.json') as f:
    conf = json.load(f)
    
from sqlalchemy.engine.url import URL 
from sqlalchemy import create_engine

engine = create_engine(URL(**conf))

df = pd.read_sql('select id,username,firstname,lastname ' +
                 'from moodle.mdl_user where id<100 ',engine)
df

```

The _config.json_ file looks something like the following. The current plan is that this sits above this directory, as this directory and its contents will eventually end up in github

```
{
  "drivername": "postgresql",
  "database": "someDbaseName",
  "username": "user", 
  "host": "localhost",
  "port": "5432",
  "password": "myPassword"
}  
```

## What's next?

That works and seems a reasonable. Some ideas for the next step

- Figure out how to remove/handle the _moodle_ schema that's in the SQL above, not to mention the _mdl\__ prefix on the table.
    
    Linked to allowing the code to be run across different institution's easily.
    
- Move the config code into a library for this work?
- Set up the github repository, get this code shared and start working with @beerc on this.
- Experiment with how the assumptions built into the Perl code I was using can be translated appropriately into this environment.
    
    How to develop the class hierarchy (or if) using sqlalchemy.
    
    How the perl idioms translate into python, sqlalchemy and pandas. Pandas has some nice features that might eliminate some practices.