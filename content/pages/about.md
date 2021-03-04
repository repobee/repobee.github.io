Title: About RepoBee
URL:
Save_as: index.html
Author: Simon Larsén
Sortorder: 1

## About
RepoBee is a command line tool that allows teachers and teaching assistants to
work with large amounts of student Git repositories on the GitHub, GitLab and
Gitea platforms (cloud and self-hosted). The archetypical use case is to
automate creation of student repositories based on template repositories, that
can contain for example instructions and skeleton code. Given any number of
template repositories, creating a copy for each student or group is
[just one command away](https://docs.repobee.org/en/stable/repos.html#set-up-student-repositories-the-setup-action).
RepoBee also has functionality for
[updating student repos](https://docs.repobee.org/en/stable/repos.html#updating-student-repositories-the-update-action),
[batch cloning of student repos](https://docs.repobee.org/en/stable/repos.html#cloning-repos-in-bulk-the-clone-action),
[opening, closing and listing issues](https://docs.repobee.org/en/stable/issues.html),
[no-blind](https://docs.repobee.org/en/stable/peer.html) and
[double-blind](https://docs.repobee.org/en/stable/peer.html#double-blind-peer-review)
peer review, and much more!

In addition, RepoBee features a powerful
[plugin system](https://docs.repobee.org/en/stable/plugins.html) that allows
users to either use existing plugins, or
[write their own](https://docs.repobee.org/en/stable/repobee_plug/index.html).
Plugins can do a wide range of things, including making RepoBee compatible with
multiple hosting platforms (GitHub, GitLab, Gitea), providing compatibility
with repositories managed by GitHub Classroom, or running JUnit4 test classes
on cloned student repositories.

## Install
RepoBee supports most UNIX-like environments. That includes **macOS**,
**Windows** through
[WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10) and all
**Linux** distributions. Other UNIX-like environments may work, but they are
not officially supported.

> **Don't want to install?** [We also offer a fully featured Docker image!](https://docs.repobee.org/en/stable/docker.html)

Installing RepoBee is simple, just execute the install script!

```bash
# for bash
bash <(curl -s https://repobee.org/install.sh)

# for zsh
zsh <(curl -s https://repobee.org/install.sh)
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
