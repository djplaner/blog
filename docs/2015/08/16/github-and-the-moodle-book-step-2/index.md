---
title: github and the Moodle book - Step 2
date: 2015-08-16 17:27:55+10:00
categories: ['moodleopenbook']
type: post
template: blog-post.html
comments:
    []
    
pingbacks:
    - approved: '1'
      author: github and the Moodle &#8211; Step 3 | The Weblog of (a) David Jones
      author_email: null
      author_ip: 192.0.80.160
      author_url: https://davidtjones.wordpress.com/2015/08/20/github-and-the-moodle-step-3/
      content: '[&#8230;] to follow up step 2 in connecting github and the Moodle book
        [&#8230;]'
      date: '2015-08-22 16:04:30'
      date_gmt: '2015-08-22 06:04:30'
      id: '1376'
      parent: '0'
      type: pingback
      user_id: '0'
    
---

See also: [[blog-home | Home]]

The continuing story of linking github and the Moodle book module. Following on from [step 1](/blog2/2015/08/14/bringing-github-and-the-moodle-book-module-together-step-1/) the main aim here is to grok [the PHP client](https://github.com/tan-tan-kanarek/github-php-client) for the github api I'm currently chosen.

Some additional work to be done includes

1. Consider use of branches etc
2. Ponder whether to work only with releases - or more open as listed below. Releases is more directly supported by the PHP client, but directly with content may be a little more flexible. But releases are perhaps more inline with expectations? Perhaps this is a question to answer by looking at some of the ways other similar projects are working.
    
    At this stage, I sort of see using the book to modify the repo as something that is happening prior to a release.
    
3. Looks like storing the sha of the file in a local Moodle database will be necessary to help with checking statuses etc.

## How to (if)?

I've got it installed and working from command line php scripts. Need to figure out how to use it

1. Does the file exist in the repo? Getting the content should return a 200 status code and "type: file" if it is a file, but it will also return the content of the file.
2. Create a new file API](https://developer.github.com/v3/repos/contents/#create-a-file): PUT /repos/:owner/:repo/contents/:path [Initial implementation in PHP working.
3. (fetch) Get the content for the file. API](https://developer.github.com/v3/repos/contents/#get-contents) - GET /repos/:owner/:repo/contents/:path [Intial implementation in PHP working.
4. (push) Update the file with new content. API:](https://developer.github.com/v3/repos/contents/#update-a-file) PUT /repos/:owner/:repo/contents/:path [Initial implementation in PHP working
5. What is the status of the file in the repo? What do I actually mean by status? The full history? Still need to find what, if anything in github/git/the API provides this.
6. What is the relationship between the content/status of the file in the repo and the content in the book. Looks like it's available via the same call.

### How does it work

Would help if I understood the model that it uses. Some of the example code includes something like\[code lang="php"\]$commits = $client->repos->commits->listCommitsOnRepository($owner, $repo);\[/code\]

The question is whether or not there is any pattern in common between this and the github API. I assume there is and grokking that pattern should lead to understanding how to use the API.

The assumption is that the client provides a method to access the API and hence the pattern of methods etc should match.

In [the GitHub api](https://developer.github.com/v3/) is there an equivalent to _listCommitsOnRepository_? And is it found in something within a hierarchy of repos/commits?

[There does](https://developer.github.com/v3/repos/commits/#list-commits-on-a-repository) appear to be a match. The heading _List commits on a repository_ seems to match and its found within repos/commits.

Can I apply this to get the contents of a file?

The [GitHub API defines it here](https://developer.github.com/v3/repos/contents/#get-contents)

1. Title - _Get contents_ meaning method _getContents_??
2. Structure is Repositories/Contents
3. parameters - owner, repo, path

Leading to something like \[code lang="php"\]$commits = $client->repos->contents->getContents($owner, $repo, $path);\[/code\]

Let's see if I can write code to retrieve the contents [of this file](https://github.com/djplaner/edc3100/blob/master/Who_are_you.html) from GitHub.

Mmm, getting undefined method for getContent(s).

Let's dig into the code. [GitHubClient](https://github.com/tan-tan-kanarek/github-php-client/blob/master/client/GitHubClient.php) class creates the various objects.

What does [GitHubRepos](https://github.com/tan-tan-kanarek/github-php-client/blob/master/client/services/GitHubRepos.php) contain? There is a link "contents" ([GitHubReposContents](https://github.com/tan-tan-kanarek/github-php-client/blob/master/client/services/GitHubReposContents.php)) as expected. But it only apparently gets the readme!!!

Which does work. But begging the question, where's the rest?

One fall back would be to call directly - the getReadMe is implemented via \[lang code="php"\]return $this->client->request("/repos/$owner/$repo/readme", 'GET', $data, 200, 'GitHubReadmeContent');\[/lang\]

That appears to work. Now the question is whether I can get the content. Yep, there is a method that will do that. But it's still encoded in base64. [This](http://php.net/manual/en/function.base64-decode.php) will fix that. The rough code that's working follows.

### Code for get a file

The following only works if the repository is open. The major kludge here is the use of _GitHubReadmeContent_ as the last parameter in the request. This appears to define the type of object that is returned by request. This appears to work (for now) because the Readme is just another file. Hence it appears that the various members etc are directly applicable.

A final version should check use _getType_ to check that the type of content returned is a file and not a symlink or directory

\[code lang="php"\] $owner = 'djplaner'; $repo = 'edc3100'; $path = 'Who\_are\_you.html';

$client = new GitHubClient();

$data = array(); $response = $client->request( "/repos/$owner/$repo/contents/$path", 'GET', $data, 200, 'GitHubReadmeContent' );

print "content is " . base64\_decode( $response->getContent() );\[/code\]

### Creating a new file?

At this stage, I'm thinking I'll stick with the approach of using request directly. Mainly because [GitHub API for this](https://developer.github.com/v3/repos/contents/#create-a-file) indicates it's part of Contents. And it already appears that contents doesn't include support for method. Yep, not there.

_PUT /repos/:owner/:repo/contents/:path_ will do it. But it also lists other parameters message (commit message) and content as required. Plus committer and branch as optional. Plus this is also likely going to require credentials.

Yep, 404 error. Credentials required. Put in what I think is the required code and get a 422. Which is invalid field. API documentation suggests content is required. Best provide some.

And that appears to work. At least the file was [created on GitHub](https://github.com/djplaner/edc3100/blob/master/A_new_file.html). But it got a 201, rather than a 200 back. Which is actually what the documentation says should happen. Another quick test.

That's better and the [2nd file is created](https://github.com/djplaner/edc3100/blob/master/A_2nd_new_file.html). This code is listed below.

An example of the PHP client appears to be using releases as a way to upload (or create) a new file.

### Code to create a file

Much the same limitation as above - i.e. is GitHubReadmeContent really the best value for the last parameter.

Will also need to look at handling exceptions (e.g. when the response code is different).

\[lang code="php"\] $owner = 'djplaner'; $repo = 'edc3100'; $path = 'A\_2nd\_new\_file.html'; $username = 'djplaner'; $password = 'some password';

$client = new GitHubClient(); $client->setDebug( true ); # this is a nice little view $client->setCredentials( $username, $password );

$content = "This will be the content in the second file. The 1st time";

$data = array(); $data\['message'\] = 'First time creating a file'; $data\['content'\] = base64\_encode( $content );

$response = $client->request( "/repos/$owner/$repo/contents/$path", 'PUT', $data, 201, 'GitHubReadmeContent' ); \[/code\]

### Update a file

Going to stick with the same method. In essence, this should be an almost direct copy of the code above. Ahh, one difference. There is an additional required parameter - sha - "The blob SHA of the file being replaced". This will be something that needs to be gotten from git - it's returned by getting content. Wonder if there's a get status?

That appears to be working

### code to update file

\[code lang="php"\] $owner = 'djplaner'; $repo = 'edc3100'; $path = 'A\_2nd\_new\_file.html'; # an existing file $username = 'djplaner'; $password = 'some password';

$content = "This will be the content in the second file. The 4th time";

$client = new GitHubClient(); #$client->setDebug( true ); $client->setCredentials( $username, $password );

$sha = getSha( $client, $owner, $repo, $path ); # get the content to get sha

$data = array(); $data\['message'\] = 'First time creating a file - Update 4'; $data\['content'\] = base64\_encode( $content ); $data\['sha'\] = $sha; $data\['committer'\] = array( 'name' => 'David Jones', 'email' => 'some email' );

$response = $client->request( "/repos/$owner/$repo/contents/$path", 'PUT', $data, 200, 'GitHubReadmeContent' );

print\_r( $response ); \[/code\]

### Statuses

[Separate part of the API](https://developer.github.com/v3/repos/statuses/) seems to deal with these. Works on the sha.

Seems the PHP client has a method based on repos to access this listStatusesForSpecificRef

Mmmm, this doesn't look like it will do what I want at all. More searching required.