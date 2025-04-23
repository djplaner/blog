---
title: Improving jQuery theme/Content Interface integration
date: 2020-05-29 15:55:24+10:00
categories: ['casa']
coverImage: 3102194738_a67d8b1639_o-scaled-e1590732238340.jpg
type: post
template: blog-post.html
---

See also: [[blog-home | Home]]

### The Problem

One of the benefits of using jQuery as the initial framework for [the Content Interface](/blog2/2019/08/08/exploring-knowledge-reuse-in-design-for-digital-learning-tweaks-h5p-constructive-templates-and-casa/#contentInterface) is that you can leverage the existing ecosystem. e.g. jQuery’s themes enable a default Content Interface (on the left) to be “themed” (on the right) by changing a single line of CSS.

| ![](images/j90m7Kbs5MWAgAAAABJRU5ErkJggg==) | ![](images/9Hy3ClDoUNZcXSuV26LyOkB0L1rFea9l+9r3y+ImIYRAj03AIEwSimkCU6UHF3f8PiLqb+WQ147IAAAAASUVORK5CYII=) |
| --- | --- |

The problem is visually obvious in the above. The _Reviewed_ and _Not Reviewed_ additions to the accordion bars have not changed colours to fit the themes. Not to mention being pretty horribly designed regardless of the colour.

Can this be fixed?

### Do jQuery’s themes provide support for this type of colour?

Exploring the [jQuery theme roller](https://jqueryui.com/themeroller/) and the [CSS framework](https://api.jqueryui.com/theming/css-framework/) for jQuery reveals some classes that could be useful: .ui-state-highlight .ui-state-error .ui-priority-primary .ui-priority-secondary .ui-state-disabled

After a bit of experimentation .ui-state-active (Not Reviewed) and .ui-state-disabled (Reviewed) appear to be the best options. Giving the following results.

![](images/v8Bc2mtWun8VBUAAAAASUVORK5CYII=)

![](images/EAABEAABEACBh48AFNjDN2bwGARAAARAAARA4GEn8P8DOfjL7Cg8N50AAAAASUVORK5CYII=)

### Can the Content Interface be modified to support this?

Should be a quick matter of modifying the HTML code that the Javascript is producing.

Yep, that worked. Time to commit and deploy.