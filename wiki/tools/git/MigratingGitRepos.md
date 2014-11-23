<!-- title: How to migrate a git repository from GitHub to Gitorious -->

The other day I had to move a git repository from GitHub to Gitorious and after
cracking my head against the wall about this problem for a little while, I think
I came up with a pretty elegant solution.

Here are some of the assumptions we are making in this turtorial:

1. You already have a GitHub and a Gitorious account
2. You have an existing GitHub repo that you want to move
3. We will use [this repo][githubrepo] as the example

Now follow these steps:

1. Login to Gitorious and create a new Project with a Repo
2. Find a location on your local system and create a new folder called
   XmlTidy. I usually do this at `~/Projects`
3. Drop into your new folder and initialize a new git repo in it
4. Add a remote reference to your GitHub repository called `origin`
5. Pull all code from the `master` branch in `origin`
6. Add a remote reference to your Gitorious repository called `destination`
7. Push your local `master` branch to the `destination` remote repo

Here's the complete code listing for the above narrative:

    mkdir ~/Projects/XmlTidy
    cd ~/Projects/XmlTidy
    git init .
    git remote add origin git@github.com:gorauskas/XmlTidy.git
    git pull origin master
    git remote add destination git@gitorious.org:xmltidy/xmltidy.git
    git push destination master

That's it... You're done!

[githubrepo]: https://github.com/gorauskas/XmlTidy "Xml Tidy"
