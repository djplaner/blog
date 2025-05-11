---
categories:
- bim
- bim2
date: 2010-12-19 13:50:44+10:00
next:
  text: A Theory-Driven Design Framework for Social Recommender Systems
  url: /blog2/2010/12/20/3495/
previous:
  text: First coding steps for bim2
  url: /blog2/2010/12/19/first-coding-steps-for-bim2/
title: Problems with naming of bim2
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: VRBones
      author_email: vrbones@hotmail.com
      author_ip: 118.208.180.4
      author_url: http://www.vrbones.com
      content: FWIW, I'd just call it BIM. Most people who would be installling the modules
        would be comfortable with version management.
      date: '2010-12-23 07:26:38'
      date_gmt: '2010-12-22 21:26:38'
      id: '3211'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: davidtjones
      author_email: davidthomjones@gmail.com
      author_ip: 121.222.174.141
      author_url: https://djon.es/blog/
      content: From what I see, the new name is needed/useful in terms of creating a new
        repo on github. I also am hoping that bim2 will have some significant new features.
        The new name helps distinguish.  Of course, it's almost certainly going to have
        unintended consequences with folk. Ah well, decision made now.
      date: '2010-12-23 08:16:46'
      date_gmt: '2010-12-22 22:16:46'
      id: '3212'
      parent: '3211'
      type: comment
      user_id: '1'
    - approved: '1'
      author: VRBones
      author_email: vrbones@hotmail.com
      author_ip: 118.208.180.4
      author_url: http://www.vrbones.com
      content: Yeah, I didn't read the previous post where you outlined the reasons until
        after I posted. After making a separate repository you're more or less locked
        in to the name change. Still, it's going to get messy later on with bimtwopointfive,
        or bimfifteen.
      date: '2010-12-24 05:22:01'
      date_gmt: '2010-12-23 19:22:01'
      id: '3213'
      parent: '3211'
      type: comment
      user_id: '0'
    - approved: '1'
      author: davidtjones
      author_email: davidthomjones@gmail.com
      author_ip: 121.222.97.150
      author_url: https://djon.es/blog/
      content: ':) There won''t be any bimtwopointfive.
    
    
        The main reason for a different git repository, rather than a new version in the
        old repository.  Is that I wanted to take the time to re-design the structure
        of BIM entirely and then use that as the new foundation moving forward.  The complete
        difference in the code suggested a new repository.
    
    
        IN future, there will just be new versions of bimtwo.  I hope. :)'
      date: '2010-12-24 08:23:39'
      date_gmt: '2010-12-23 22:23:39'
      id: '3214'
      parent: '3211'
      type: comment
      user_id: '1'
    
pingbacks:
    []
    
---
The [last post](/blog2/2010/12/19/first-coding-steps-for-bim2/) covered the initial steps in starting bim2. Including the choice of the name _bim2_. But there is a problem.

### The problem

It's starting to look like the choice of _bim2_ as a name might not have been great. It appears Moodle may not like a digit in the name of a module. Confirmed: when creating a new module, the new name of the module must not contain numbers or other special characters!

> When creating a new module, the new name of the module must not contain numbers or other special characters!

The end result is that the "Add an activity" menu in Moodle only ever shows _bim_ and not _bim2_ which means adding the activity won't work.

The name will have to change. At least within Moodle.

This is just a bit of a bugger. Will mean I have to change the name of the git repository and a whole lot of other mucking around. I can't really go back to use _bim_ as the repo name, as that name is already taken by the Moodle 1.9 version of bim. I really don't like this, both the need to change and the limited knowledge of mine resulting in the need for the change.

### Name change?

So, should the name be _bimTwo_? It's probably the best compromise. But still ugly. Especially since the #bim2 tag is [already being used](http://twitter.com/#!/moodleman/status/16317089866321921) and makes the most sense.

Solution? For now, I think the plan will be to use _bimTwo_ internal to Moodle, but encourage and use bim2 elsewhere. Maybe _bim\_two_ instead?

What do you think? Is there a better solution?

Actually, it will have to be _bimtwo_ due

- underscore being a special character and not working within a Moodle module name;
- uppercase characters don't work/aren't supported in table names in the Moodle database.