Title: Install
Author: Simon Larsén
Sortorder: 2

# Install

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

# Uninstall

Simply remove the `~/.repobee` directory. Depending on if you chose to modify
your `.bashrc`/`.zshrc`/... during install, or have done so manually, you may
also need to remove a few lines from these files to remove all traces of
RepoBee.
