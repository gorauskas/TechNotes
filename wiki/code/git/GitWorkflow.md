<!-- title: Git Workflows that I Use -->


A few conventions I use:

1. The `remote` repository is always called `origin`
2. The main working branch is always called `master`

If you need to review the recent work that has been done, commit it and then
push it to `remote`, do the following:

    $ git status
    $ git diff
    $ git commit -am 'My message here'
    $ git push

If you need to compare the `local` repository to the `remote`, do the following:

    $ git fetch origin
    $ git diff master..origin/master
    $ git pull

If you want to get the latest version from a `git` repository and you don't care
about any local changes, do the following:

    $ git reset --hard HEAD
    $ git clean -f
    $ git pull

The above will copy the latest code from the `remote` and overwrite the local
copy.

If you need to tag a branch, do the following:

    $ git tag -a v0.1 -m 'version 0.1'
    $ git tag
    $ git log --pretty=oneline
    $ git show v0.1

If you need to create a new branch from an existing one in order to implement a
new feature, do the following:

    $ git checkout -b newbranch master
    $ git checkout master
    $ git push origin master
    $ git push origin newbranch
