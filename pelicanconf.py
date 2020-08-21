#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Simon Larsén"
SITENAME = "RepoBee"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/Stockholm"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SITE_BANNER = "/images/RepoBee_large-black.png"
THEME = "theme"

GITHUB_LINK = "https://github.com/repobee/repobee"
RTD_LINK = "https://repobee.readthedocs.io"

STATIC_PATHS = [
    "extra/CNAME",
    "images/RepoBee_large-black.png",
    "favicon.ico",
    "extra/plugins.json",
    "extra/install.sh",
]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/plugins.json": {"path": "plugins.json"},
    "extra/install.sh": {"path": "install.sh"},
}

# Social widget
SOCIAL = (("You can add links in your config file", "#"), ("Another social link", "#"))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
