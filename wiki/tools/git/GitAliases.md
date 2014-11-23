<!-- title: Useful Git Aliases -->


Here are some useful aliases for Git:

## git ls

`git log` is pretty useless. It doesn't list the branch the commit was made on,
it doesn't show colors and it doesn't show branching visuals. But with this
alias you get all that. List commits in short form, with colors and branch/tag
annotations and visuals.

    git config --global alias.ls "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --decorate"

## git ll

List commits as above but also showing changed files.

    git config --global alias.ll "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --decorate --numstat"

## git lds

List one line commits that display dates.

    git config --global alias.lds "log --color --graph --pretty=format:'%Cred%h% %ad%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --decorate --date=short"

## git grep

Find a file path in codebase which contains a string or pattern.

    git config --global alias.grep '!git ls-files | grep -i'

## git ltg

Show the last tag.

    git config --global alias.ltg 'describe --tags --abbrev=0'

## git unpushed

Sometimes I wonder what is left to push to origin. Git doesn't have an easy
way to see this, but with this alias you get the commits that haven't been
pushed to upstream. Also you get colors and branching visuals like
above.

    git config --global alias.unpushed "log --branches --not --remotes --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

## git undo

Git doesn't have an undo option to undo the last commit. But with this alias you
can easily undo the last commit.

    git config --global alias.undo 'reset --hard HEAD~1'

However if you've added many files in the last commit (like a package or
something), git doesn't delete them. But you can do that with this alias: `git
clean -f -d`

## git visual

Run a git graphical user interface on top of your git directory.

    git config --global alias.visual '!gitk'

## git la

Going meta! List out all your aliases.

    git config --global alias.la '!git config -l | grep alias | cut -c 7-'

## Basic stuff

Of course I use a ton of basic shortcuts, here’s a few ingrained in my fingertips:

    cp = cherry-pick
    st = status -s
    cl = clone
    ci = commit
    co = checkout
    br = branch
    diff = diff --word-diff
    dc = diff --cached
