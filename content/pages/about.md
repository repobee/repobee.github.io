Title: About RepoBee
URL:
Save_as: index.html
Author: Simon Larsén
Sortorder: 1

RepoBee is an open source CLI tool that enables teachers to administrate large
amounts of Git repositories on the GitHub and GitLab platforms. It automates
tasks such as creating repositories for students (or groups) and filling them
with content, batch cloning of student repositories as well as issue management
and light peer review functionality. RepoBee can also be customized through
plugins written in Python.

To learn more about RepoBee, head over to the [GitHub
page](https://github.com/repobee/repobee), or maybe strike directly for the
[documentation over on ReadTheDocs](https://repobee.readthedocs.io).

## Install
Installing RepoBee is simple, just execute the install script!

```bash
# for bash
$ bash <(curl -s https://repobee.org/install.sh)

# for zsh
$ zsh <(curl -s https://repobee.org/install.sh)
```

Follow the instructions from the install script and you should be good to go.
It will install RepoBee into the `~/.repobee` directory for you. Visit [the
install documentation](https://repobee.readthedocs.io/en/stable/install.html)
for more elaborate instructions.

> **Note:** Even if your primary shell is not `bash` or `zsh`, you need to
> install RepoBee with one of them. Then you can execute RepoBee with most
> shells.

## Uninstall
Simply remove the `~/.repobee` directory. Depending on if you chose to modify
your `.bashrc` or `.zshrc` or similar during install, or have done so manually,
you may also need to remove a few lines from these files to remove all traces
of RepoBee.
