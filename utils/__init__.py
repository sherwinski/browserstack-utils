# -*- coding: utf-8 -*-
"""
browserstack-utils
~~~~~

A Python client library for generating URLs with imgix. Basic usage:

    >>> import imgix
    >>> builder = imgix.UrlBuilder("demos.imgix.net")
    >>> builder.create_url("/bridge.png", {'w': 100, 'h': 100})
    https://demos.imgix.net/bridge.png?h=100&w=100

... or generating signed URLs:

    >>> builder = imgix.UrlBuilder("demos.imgix.net", sign_key="test1234")
    >>> builder.create_url("/bridge.png", {'w': 100, 'h': 100})
    http://demos.imgix.net/bridge.png?h=100&w=100&s=7370d6e36bb2262e73b19578739af1af

Refer to `imgix.UrlBuilder` class documentation for all the supported options.
"""

from .getworkers import fetch_workers
from .deleteworkers import delete_workers
from .cleanup import cleanup
