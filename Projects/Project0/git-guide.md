## Command line git

- status
  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub)
    - list of files in local folder than are NOT being tracked by git
    - list of files in local folder that have changes that need to be committed
  - `git status`
- clone
  - Retrieve an entire repository as a Git repository
  - `git clone`
- add
  - Add a file as it looks now to your next commit
  - `git add`
- rm
  - Delete the file from a project and stage the removal for commit
  - `git rm [file]`
- commit
  - Record changes to the repository
  - `git commit -m "commit message here"`
- push
  - Transmit local branch commits to the remote repository branch
  - `git push [alias] [branch]`
- fetch
  - Fetch down all the branches from the Git remote
  - `git fetch [alias]`
- merge
  - Merge the specified branch's history into the current one
  - `git merge [alias]/[branch]`
- pull
  - Fetch and merge any commits from the tracking remote branch
  - `git pull`
- branch
  - Create a new branch at the current commit
  - `git branch [branch-name]`
- checkout
  - Switch to another branch and check it our into your working directory
  - `git checkout`
- ~~init~~
- ~~remote~~

## git files & folders

- .git folder
  - Contains all information that is necessary for the project and all information relating to commits, remote repository address, etc.
  - `ls -a`
- .gitignore file
  - Let git know that it should ignore certain files and not track them
  - Files that should be ignored:
    - Log files
    - Files with API keys/secrets, credentials, or sensitive information
    - .DS_Store on macOS
    - dist folders
    - Dependancies which can be downloaded from a package manager
    - .md files that are irrelevant (todo.md)
  - `.gitignore [filename]`
- ~~.git/hooks~~

## GitHub

- Pull requests
  - Let you tell others about changes you've pushed to a branch in a repository on GitHub. 
  - `git pull`
- SSH authentication to repositories
  - Network protocol that gives users, particularly system administrators, a secure way to access a computer over an unsecured network
  - `ssh UserName@SSHserver.exampl.com`
- ~~Actions~~

## Resources

- [Pro Git Book](https://git-scm.com/book/en/v2)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [What is .git folder and why is it hidden?](https://www.tutorialspoint.com/what-is-git-folder-and-why-is-it-hidden)
- [How to Use a .gitignore File](https://www.pluralsight.com/guides/how-to-use-gitignore-file)
- [About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
- [Secure Shell](https://www.techtarget.com/searchsecurity/definition/Secure-Shell)
- []()
                                                                                                                                                                                         75,6          Bot


