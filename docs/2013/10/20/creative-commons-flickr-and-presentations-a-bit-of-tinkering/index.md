---
categories:
- thesis
date: 2013-10-20 18:25:43+10:00
next:
  text: Processing and Visualizing Data in Complex Learning Environments
  url: /blog/2013/10/20/processing-and-visualizing-data-in-complex-learning-environments/
previous:
  text: Supporting Action Research with Learning Analytics
  url: /blog/2013/10/13/supporting-action-research-with-learning-analytics/
tags:
- creative-commons
- creative-commons-licence
title: '"Creative Commons, Flickr and presentations: A bit of tinkering"'
type: post
template: blog-post.html
comments:
    - approved: '1'
      author: elketeaches
      author_email: elkeclarissa@hotmail.com
      author_ip: 124.189.216.206
      author_url: http://elketeaches.wordpress.com
      content: that's a nice bit of code there!  Just wanted to mention that I really
        liked your presentation example; you can't teach well without the odd cat photo.  :-)
      date: '2013-10-21 06:03:46'
      date_gmt: '2013-10-20 20:03:46'
      id: '884'
      parent: '0'
      type: comment
      user_id: '0'
    - approved: '1'
      author: David Jones
      author_email: davidthomjones@gmail.com
      author_ip: 139.86.2.15
      author_url: https://djon.es/blog/
      content: One of my many flaws is I don't use enough cats in my presentations :)
      date: '2013-10-21 08:51:50'
      date_gmt: '2013-10-20 22:51:50'
      id: '885'
      parent: '884'
      type: comment
      user_id: '1'
    
pingbacks:
    - approved: '1'
      author: Needed updates to cc_attrib.pl | The Weblog of (a) David Jones
      author_email: null
      author_ip: 192.0.80.121
      author_url: https://djon.es/blog/2014/02/15/needed-updates-to-cc_attrib-pl/
      content: '[&#8230;] following is a list of updates I need to make to a perl script
        I wrote last year that helps me properly attribute the Creative Commons licenced
        Flickr photos I use in [&#8230;]'
      date: '2014-02-15 08:23:05'
      date_gmt: '2014-02-14 22:23:05'
      id: '886'
      parent: '0'
      type: pingback
      user_id: '0'
    
---
The following is a summary of some tinkering to develop a script that will help me appropriately attribute use of Creative Commons licensed images in presentations. Beyond addressing a long-standing problem of mine, this bit of tinkering is an attempt to feel a bit productive.

## The problem

When I give presentations I use Powerpoint (not inherently the problem). I use it in a particular way. Lots of slides, little if any text, and each slide with an interesting photo related to the point I'm trying to make. What follows is an example. (Move beyond the first slide for a feel).


!!! warning "Outdated content no longer available"

    Presentation from Slideshare no long available


The images are all licensed with a Creative Commons licence and I source them from Flickr via the [Creative Commons search](http://search.creativecommons.org/). According to [this source](http://creativecommons.org.au/content/How_to_Attribute_CC_Materials_edu.pdf)

> All Creative Commons licences require that users of the work attribute the creator. This is also a requirement under Australian copyright law. This means you always have to acknowledge the creator of the CC work you are using, as well as provide any relevant copyright information.

The document continues with "For many users of CC material, attribution is one of the hardest parts of the process". My current practice is to include the URL of the original image on Flickr on each slide. This has three problems

1. It adds text to each slide, taking away some of the impact of the image.
2. Doesn't fulfil the requirements of the CC licence.
3. With this style of presentation, most 20/30 minutes presentations are getting close to 100 slides often with the same number of images to attribute.

The requirements are

> you should:
> 
> - Credit the creator;
> - Provide the title of the work;
> - Provide the URL where the work is hosted;
> - Indicate the type of licence it is available under and provide a link to the licence (so others can find out the licence terms); and
> - Keep intact any copyright notice associated with the work.

There are a range of online services that help with attribution. [ImageCodr](http://www.imagecodr.org/) generates HTML, which I use often. [flickr storm](http://www.zoo-m.com/flickr-storm/) does a similar task somewhat differently. The [Flickr CC helper](http://cogdogblog.com/flickr-cc-helper/) will generate HTML or text.

To fit with the workflow I use when creating presentations, I'm after something that will

1. Parse a text file of the format
    
    1 http://my.flickr.com/photo 2 http://my.flickr.com/photo2
    
2. Use the Flickr API to extract the information necessary for an appropriate CC attribution.
3. Add that to a text/HTML file that will form a "credits" slide at the end of a presentation.
    
    As per the advice from [this source](http://creativecommons.org.au/content/How_to_Attribute_CC_Materials_edu.pdf)
    
    > Alternatively, you can include a ‘credits’ slide at the end of the show, that lists all the materials used and their attribution details. Again, you should indicate the slide or order so people can find the attribution for a specific work.
    
4. Optionally, add a message to the photo on Flickr summarising how/where the photo has been used.

## Tinkering process

What follows is the planned/actual tinkering process toward implementation of a solution as a Perl script. The script will use the [Flickr API](http://www.flickr.com/services/api/) to extract the licence information and hopefully add a comment.

### Flickr API working - extracting information

Perl has a range of [Flickr related modules](http://search.cpan.org/search?query=flickr&mode=all). [Flickr::API2](https://github.com/TJC/Flickr-API2) seems to be the current standard.

The [flickr.photos.licences.getInfo](http://www.flickr.com/services/api/flickr.photos.licenses.getInfo.html) method gives a list of all the licenses. When you get a photo by id (part of the URL) Flickr returns a licence id with which you can find the URL and name of the licence for the photo.

Some limitations of the information

- Flickr doesn't provide the abbreviation for the CC licences.  
    hard-coded into the script.
- The url\_l method for Flickr::API2 doesn't seem to be working.  
    that's because it's not a method - page\_url works.
- The owner\_name method for Flickr::API2 doesn't seem to always reliably return the owner's name.  
    Use the username as a supplement.

### Generating credits page

Initially, I was going to copy the format used by the [flickr cc attribution helper](http://cogdogblog.com/flickr-cc-helper/) i.e.

cc licensed ( \*ABBR\* ) flickr photo by \*username\*: \*URL\*

But [this](http://creativecommons.org.au/content/How_to_Attribute_CC_Materials_edu.pdf) suggests that the title of the work and a link to the licence is also required (though it does mention flexibility). The format they're using is

\*title\* by \*name\* available at \*url\*  
under a \*licence name\*  
\*licence url\*

Will do this as simple text, single reference to a line. Will also add in the slide number.

After a bit of experimentation the following is what the script is currently generating

Slide 2, 3: "My downhill run!" by Mike Mueller available at http://flickr.com/photos/mike912mueller/6407874723 under Attribution-NonCommercial-ShareAlike License http://creativecommons.org/licenses/by-nc-sa/2.0/

Slide 4: "Question Mark Graffiti" by zeevveez available at http://flickr.com/photos/zeevveez/7095563439 under Attribution License http://creativecommons.org/licenses/by/2.0/

Slide 1: "Greyhound Half Way Station" by Joseph available at http://flickr.com/photos/josepha/4876231714 under Attribution-NonCommercial-ShareAlike License http://creativecommons.org/licenses/by-nc-sa/2.0/

Modified to recognise that I sometimes use an image on multiple pages. I should perhaps add a bit of smarts into the code to order the slides correctly, but time is short.

### Adding comment on Flickr

The [flickr.photos.comments.addComment method](http://www.flickr.com/services/api/flickr.photos.comments.addComment.html) seems to offer what I need. Of course it's not that simple. To make a comment the script needs to be authenticated with flickr. i.e. as me.

The documentation for Flickr::API2 is not 100% clear on this and the evolution of authentication means that flickr is moving on, but the following process seems to work

- Get a "frob" \[sourcecode lang="perl"\] use Flickr::API2; my $api = Flickr::API2->new({ 'key' => <em>mykey</em>, 'secret' => <em>mysecret</em> }); my $result = $api->execute\_method( 'flickr.auth.getFrob' ); my $frob = $result->{frob}->{\_content}; \[/sourcecode\]
- Get a special URL to tell Flickr to authorise the script \[sourcecode lang="perl"\] my $url = $api->raw->request\_auth\_url( 'write', $frob ); print Dumper( $url ); # wait until I visit the URL and hit enter <STDIN>; \[/sourcecode\]
- Get the token \[sourcecode lang="perl"\] my $res = $api->execute\_method( 'flickr.auth.getToken', { 'frob' => $frob} ); print Dumper( $res ); \[/sourcecode\]
- Copy the token that's displayed and hard code that into subsequent scripts, including adding a comment using my flickr account. \[sourcecode lang="perl"\] my $comment =<<"EOF"; G'day, This is a test comment. EOF my $response = $api->execute\_method( "flickr.photos.comments.addComment", { photo\_id => 3673725336, comment\_text => $comment, auth\_token => <em>the token I got</em> } ); \[/sourcecode\]

## Put it all together

I'm going to use a small presentation I use in my teaching as a test case. I'll hardcode the link between image and slide number into the initial script. Longer term the script will rely on there being a text file of the format

> 1,_flickr photo url_ 2,_flickr photo url_

(see below for some ideas of how I'll do this)

It all works. Up above you can see the credit text produced based on a small presentation I use in my teaching. The following is one of the images used in that presentation. If you click on the image you can see the comment that was added by the script.

[![Greyhound Half Way Station by joseph a, on Flickr](http://farm5.static.flickr.com/4115/4876231714_2e5f81b446_m.jpg "Greyhound Half Way Station by joseph a, on Flickr")](http://www.flickr.com/photos/josepha/4876231714/)  
[![Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License](http://i.creativecommons.org/l/by-nc-sa/2.0/80x15.png "Creative Commons Attribution-Noncommercial-Share Alike 2.0 Generic License")](http://creativecommons.org/licenses/by-nc-sa/2.0/)  by  [](http://www.flickr.com/people/josepha/)[joseph a](http://www.flickr.com/people/josepha/) [](http://www.imagecodr.org/)

What follows are various bits of the script, happy to share the file, but I don't imagine that there's a lot of folk with Perl installed and configured that would want to use it. There needs to be some more work tidying up and adding in error checking. But it works well enough for now.

The main logic of the script is

\[sourcecode lang="perl"\] use strict; use Flickr::API2;

\# hard-code abbreviations for CC licences based on Flickr id my %CC = ( 1 => "BY-NC-SA", 2 => "BY-NC", 3 => "BY-NC-ND", 4 => "BY", 5 => "BY-SA", 6 => "BY-ND" );

my $TOKEN = "my token"; my $auth = { 'key' => 'my key', 'secret' => 'my secret' };

\# which flickr URLs appear on which slides # flickr photo URL is the key, value is array of slides on which the image appears my $PHOTO\_SLIDES = { 'http://www.flickr.com/photos/7150652@N02/4876231714/' => \[ 1 \], 'http://www.flickr.com/photos/27933068@N03/6407874723/' => \[ 2, 3 \], 'http://www.flickr.com/photos/zeevveez/7095563439/' => \[ 4 \] };

my $COMMENT =<<"EOF"; --whatever comment I want to add EOF

my $API = Flickr::API2->new( $auth ); my $credits = generate\_credits( $PHOTO\_SLIDES, $API ); add\_comment( $PHOTO\_SLIDES, $COMMENT, $API ); print $credits; \[/sourcecode\]

To add the comments (I'm guessing the extraction of the Flickr ID will break eventually)

\[sourcecode lang="perl"\] sub add\_comment($$$) { my $photo\_slides = shift; my $comment = shift; my $api = shift;

foreach my $photo\_url ( keys %$photo\_slides ) { if ( $photo\_url =~ m#http://www.flickr.com/photos/.\*/(\[0-9\]\*)/# ) { my $id = $1; my $response = $api->execute\_method( "flickr.photos.comments.addComment", { photo\_id => $id, comment\_text => $comment, auth\_token => $TOKEN } ); } } } \[/sourcecode\]

And finally generating the attribution information

\[sourcecode lang="perl"\] sub generate\_credits( $$ ) { my $photo\_slides = shift; my $api = shift;

\## Get the licence options my $response = $api->execute\_method( "flickr.photos.licenses.getInfo" ); my $licences = $response->{licenses}->{license};

my $content = "";

foreach my $photo\_url ( keys %$photo\_slides ) { # extract the id if ( $photo\_url =~ m#http://www.flickr.com/photos/.\*/(\[0-9\]\*)/# ) { my $id = $1; my $photo = $api->photos->by\_id( $id );

\# get the licence my $info = $photo->info(); my $licence = getLicence( $info->{photo}->{license}, $licences); die "No CC licence found for $photo\_urln" if ( ! defined $licence ) ; $content .= displayInfo( $licence, $photo, $info, $photo\_slides->{$phto\_url} ); } } return $content; }

sub displayInfo( $$$ ) { my $licence = shift; my $photo = shift; my $info = shift; my $slides = shift; # array of slide numbers

my $slide = join ", ", @$slides;

my $url = $photo->page\_url; $url =~ s/ //g; my $name = $photo->owner\_name; $name = $info->{photo}->{owner}->{username} if ( $name eq "" );

return <<"EOF"; Slide $slide: "$photo->{title}" by $name available at $url under $licence->{name} $licence->{url}

EOF }

sub getLicence( $$ ) { my $id = shift; my $licenses = shift;

foreach my $licence ( @{$licenses} ) { return $licence if ( $id == $licence->{id} ); }

return undef; } \[/sourcecode\]

## Getting the URLs of images

The final script assumes I have a text file of the format

The question of how to generate this text file remains open. I can see three possible options

1. Construct the file manually.
    
    This would be painful and have to wait until after the presentation file is complete. Manual is to be avoided.
    
2. Extract it from the Slideshare transcript.
    
    As well as producing an [online version of a presentation](http://www.slideshare.net/davidj/moving-beyonda-fashion), Slieshare also produces a transcript of all the text. This includes flickr photo URLs. This currently works because of my practice of including the URLs on each slide, something I'd like to avoid. As a kludge, I could probably include the URL on each slide but place it behind the image. i.e. make it invisible to the eye, but still to slideshare?
    
3. Extract it from the pptx file.
    
    Powerpoint files are now just zip file collections of xml files. I could draw on perl code [like this](http://www.perlmonks.org/?node_id=1022468) to extract the URLs. Perhaps the best way is to insert the Flickr URL of the photos used in the notes section (as they too are XML files).
    

#3 is the long term option. Will use #2 as my first test.