Title: About RepoBee
URL:
Save_as: index.html
Author: Simon Larsén
Sortorder: 1

## About
RepoBee is an open source CLI tool that enables teachers to administrate large
amounts of Git repositories on the GitHub and GitLab platforms. It automates
tasks such as creating repositories for students (or groups) and filling them
with content, batch cloning of student repositories as well as issue management
and light peer review functionality. RepoBee can also be customized through
plugins written in Python.

For new users, the
[User Guide](https://repobee.readthedocs.io/en/stable/userguide.html) is a
great place to start getting to know RepoBee and what it can do. For the more
impatient folks out there, the complete CLI of the core application (i.e.
plugins not included) is listed in the
[CLI Documentation](https://repobee.readthedocs.io/en/stable/cli.html).

## Install
RepoBee supports most UNIX-like environments. That includes **macOS**,
**Windows** through
[WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10) and all
**Linux** distributions. Other UNIX-like environments may work, but they are
not officially supported.

> **Upgrading from RepoBee 2.x?** [Please see the v3.0.1 release notes before
> proceeding](https://github.com/repobee/repobee/releases/tag/v3.0.1)

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
