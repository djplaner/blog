---
title: BIM2 and disable_form_change_checker
date: 2013-03-03 18:09:10+10:00
categories: ['bim2']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: Adding bim 2.0 to &#8220;CONTRIB&#8221; | The Weblog of (a) David Jones
      author_email: null
      author_ip: 72.232.113.87
      author_url: https://djon.es/blog/2013/04/05/adding-bim-2-0-to-contrib/
      content: '[...] to a bug report from a Russian user of BIM solved a problem with
        2.3.2 version of [...]'
      date: '2013-04-05 16:46:14'
      date_gmt: '2013-04-05 06:46:14'
      id: '641'
      parent: '0'
      type: pingback
      user_id: '0'
    
---

See also: [[blog-home | Home]]

As a developer, you have to love it when someone using your code diagnoses and identifies their own problem with your code. Especially if they give you a clear and concise explanation you can use. That's what happened with [the BIM2 problem](/blog2/2013/02/27/diagnosing-a-bim-problem/) I blogged about recently. It appears I was using Moodle 2.3.4 the problem was found on Moodle 2.3.2+ and there was a change in the Moodle code in-between. The following describes the bug and hopefully the fix/change I've made to the BIM code.

### The problem

The problem arises in bim/marker/allocation\_form.php with this \[source code="php"\] // turn off the checking $mform->disable\_form\_change\_checker(); \[/source\]

disable\_form\_change\_checker is [described here](http://docs.moodle.org/dev/lib/formslib.php_Form_Definition#disable_form_change_checker) and it was added in [Moodle 2.3.3](http://docs.moodle.org/dev/Moodle_2.3.3_release_notes).

So the question is how to handle this neatly so that BIM gracefully degrades with older versions of Moodle?

### The solution?

One approach is to simply require the more recent version of Moodle, but given this is one function call in one section of the code. There has to be a more fine grain solution, doesn't there?

Perhaps just removing the call? But I remember it getting quite annoying without it. So, for now, it stays.

Of course, method\_exists. I need to code more.

\[source code="php"\] if ( method\_exists( $mform, "disable\_form\_change\_checker" ) ) { $mform->disable\_form\_change\_checker(); } \[/source\]

No problem with 2.4. What about older versions?

Yes, Moodle 2.2 crashes with this problem in BIM. And method\_exists fixes it. Time to commit the code and we're done.