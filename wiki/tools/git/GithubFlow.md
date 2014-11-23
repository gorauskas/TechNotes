<!-- title: Github Flow -->


Here is the Github Flow in a nutshell:

## So, what is GitHub Flow?

1. Anything in the master branch is deployable
2. To work on something new, create a descriptively named branch off of master
   (ie: new-oauth2-scopes)
3. Commit to that branch locally and regularly push your work to the same named
   branch on the server
4. When you need feedback or help, or you think the branch is ready for merging,
   open a pull request
5. After someone else has reviewed and signed off on the feature, you can merge
   it into master
6. Once it is merged and pushed to ‘master’, you can and should deploy
   immediately

That is the entire flow. It is very simple, very effective and works for fairly
large teams – GitHub is 35 employees now, maybe 15-20 of whom work on the same
project (github.com) at the same time.

## Anything in the master branch is deployable

This is basically the only hard rule of the system. There is only one branch
that has any specific and consistent meaning and we named it master. To us, this
means that it has been deployed or at the worst will be deployed within
hours. The master branch is stable and it is always, always safe to deploy from
it or create new branches off of it. If you push something to master that is not
tested or breaks the build, you break the social contract of the development
team and you normally feel pretty bad about it.

## Create descriptive branches off of master

When you want to start work on anything, you create a descriptively named branch
off of the stable master branch. Some examples in the GitHub codebase right now
would be user-content-cache-key, submodules-init-task or redis2-transition. This
has several advantages – one is that when you fetch, you can see the topics that
everyone else has been working on. Another is that if you abandon a branch for a
while and go back to it later, it’s fairly easy to remember what it was.

## Push to named branches constantly

Another big difference from git-flow is that we push to named branches on the
server constantly. Since the only thing we really have to worry about is master
from a deployment standpoint, pushing to the server doesn’t mess anyone up or
confuse things – everything that is not master is simply something being worked
on.

It also make sure that our work is always backed up in case of laptop loss or
hard drive failure. More importantly, it puts everyone in constant
communication. A simple ‘git fetch’ will basically give you a TODO list of what
every is currently working on.

## Open a pull request at any time

GitHub has an amazing code review system called Pull Requests that I fear not
enough people know about. Many people use it for open source work – fork a
project, update the project, send a pull request to the maintainer. However, it
can also easily be used as an internal code review system.

## Merge only after pull request review

We don’t simply do work directly on master or work on a topic branch and merge
it in when we think it’s done – we try to get signoff from someone else in the
company. This is generally a +1 or emoji or “:shipit:” comment, but we try to
get someone else to look at it.

## Deploy immediately after review

Finally, your work is done and merged into the master branch. This means that
even if you don’t deploy it now, people will base new work off of it and the
next deploy, which will likely happen in a few hours, will push it out. So since
you really don’t want someone else to push something that you wrote that breaks
things, people tend to make sure that it really is stable when it’s merged and
people also tend to push their own changes.

## Conclusion

Git itself is fairly complex to understand, making the workflow that you use
with it more complex than necessary is simply adding more mental overhead to
everybody’s day. I would always advocate using the simplest possible system that
will work for your team and doing so until it doesn’t work anymore and then
adding complexity only as absolutely needed.

For teams that have set up a culture of shipping, who push to production every
day, who are constantly testing and deploying, I would advocate picking
something simpler like GitHub Flow.

The above condensed from the original at [Github Flow][githubflow].

## The workflow

    # everything is happy and up-to-date in master
    git checkout master
    git pull origin master

    # let's branch to make changes
    git checkout -b my-new-feature

    # go ahead, make changes now.
    $EDITOR file

    # commit your (incremental, atomic) changes
    git add -p
    git commit -m "my changes"

    # keep abreast of other changes, to your feature branch or master.
    # rebasing keeps our code working, merging easy, and history clean.
    git fetch origin
    git rebase origin/my-new-feature
    git rebase origin/master

    # optional: push your branch for discussion (pull-request)
    #           you might do this many times as you develop.
    git push origin my-new-feature

    # optional: feel free to rebase within your feature branch at will.
    #           ok to rebase after pushing if your team can handle it!
    git rebase -i origin/master

    # merge when done developing.
    # --no-ff preserves feature history and easy full-feature reverts
    # merge commits should not include changes; rebasing reconciles issues
    # github takes care of this in a Pull-Request merge
    git checkout master
    git pull origin master
    git merge --no-ff my-new-feature

    # optional: tag important things, such as releases
    git tag 1.0.0-RC1

## DOs and DON'Ts

No DO or DON'T is sacred. You'll obviously run into exceptions, and develop your
own way of doing things. However, these are guidelines I've found useful.

### DOs

- DO keep master in working order.
- DO rebase your feature branches.
- DO pull in (rebase on top of) changes
- DO tag releases
- DO push feature branches for discussion
- DO learn to rebase

### DON'Ts

- DON'T merge in broken code.
- DON'T commit onto master directly.
- DON'T hotfix onto master! use a feature branch.
- DON'T rebase master.
- DON'T merge with conflicts. handle conflicts upon rebasing.


[githubflow]: http://scottchacon.com/2011/08/31/github-flow.html " "
