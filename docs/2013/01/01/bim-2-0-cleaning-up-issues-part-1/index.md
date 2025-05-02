---
title: BIM 2.0 - cleaning up issues - Part 1
date: 2013-01-01 17:01:01+10:00
categories: ['bim', 'bim2']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: BIM 2.0 &#8211; Cleaning up issues &#8211; Part 2 &laquo; The Weblog of
        (a) David Jones
      author_email: null
      author_ip: 216.151.210.30
      author_url: https://djon.es/blog/2013/01/04/bim-2-0-cleaning-up-issues-part-2/
      content: '[...] on that last bit of issue cleanup this aims to reduce the list of
        open BIM issues a bit more. The focus in this part will [...]'
      date: '2013-01-04 20:10:53'
      date_gmt: '2013-01-04 10:10:53'
      id: '546'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
While [BIM 2.0](/blog2/research/bam-blog-aggregation-management/) is largely working there remains a [list of 30 open issues](https://github.com/djplaner/BIM/issues) to be addressed. 19 of these are "future" issues. i.e. changes that would be really nice but aren't necessary for the immediate release of BIM 2.0. The following is the first part of working on the 11 that are of immediate interest.

Of initial interest will be

- Ensuring deleting a BIM activity removes all data from the bim tables [issue #55](https://github.com/djplaner/BIM/issues/55)
- Error on releasing a marked post - [issue #54](https://github.com/djplaner/BIM/issues/54)

## Deleting a BIM activity

The mod/bim/lib.php file has a method forum\_delete\_instance that is meant to do this. The error is a little obvious

\[sourcecode language="lang="php"\] if ( ! $DB->delete\_records( 'bim\_group\_allocation', array('id'=>$bim->id))) { $result = false; } \[/sourcecode\]

It should be looking for the field id. The field in the other tables for the BIM id is 'bim'. This is actually a problem that appears to extend back to BIM 1.

Changed. Tested. Fixed.

## Error releasing a post

This is a problem when gradebook integration is turned on (why it hasn't shown up previously). The SQL statement used to extract marks to update the gradebook doesn't work with Moodle 2.x. Update this and it should work.

That seems to have worked. No more problem. The status has been updated. Time to check if the gradebook has been updated appropriately. Yep. Gradebook updated correctly. Can close this one off.