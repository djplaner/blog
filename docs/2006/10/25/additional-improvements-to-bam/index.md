---
categories:
- bam
date: 2006-10-25 15:04:39+10:00
next:
  text: Starting my "blogs for learning" article about BAM
  url: /blog/2006/10/26/starting-my-blogs-for-learning-article-about-bam/
previous:
  text: 'Who is to blame for plagiarism: technology, lecturers or context?'
  url: /blog/2006/10/25/who-is-to-blame-for-plagiarism-technology-lecturers-or-context/
title: Additional improvements to BAM
type: post
template: blog-post.html
---
It's almost the end of term. We've started marking the blogs using BAM and not surprisingly some rough edges are showing. Things to look at

- Merging feeds Currently BAM simply copies over the local mirror of the feed with the new one. This causes problems because Wordpress, and likely other providers, only provide a feed with the last 10 posts. The solution would be to merge the new feeds with the local mirrored copy. XML::Feed, the Perl module used in BAM, offers the splice method to do this. So should be easy.
- Making copy detection, pro-active I find it hard to believe but we have had students who have copied the blog entries of other students. At least half a dozen. Now that it is written, need to have this run as a more regular event and notify students as soon as it happens.
- Increase visibility to students The students don't really see anything from CQU's end. This causes problems in terms of whether they've completed the questions etc. Implement a view and email notification system that gives the student a visible view of CQU's summary of where they are up to. Notify students when the miss certain events.
- Remove the special characters Students tend to cut and paste their posts from Word. This introduces special characters which, after the blog has finished with them, can cause problems.