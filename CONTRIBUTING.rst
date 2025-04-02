============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of contributions
----------------------

Report bugs
~~~~~~~~~~~

Report bugs at https://github.com/amjith/fuzzyfinder/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with `bug`
is open to whomever wants to implement it.

Implement features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with `feature`
is open to whomever wants to implement it.

Write documentation
~~~~~~~~~~~~~~~~~~~

fuzzyfinder could always use more documentation, whether as part of the
official fuzzyfinder docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/amjith/fuzzyfinder/issues.

Get started!
------------

Ready to contribute? Here's how to set up `fuzzyfinder` for local development.

1. Fork the `fuzzyfinder` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/fuzzyfinder.git

3. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

4. When you're done making changes, check that your changes pass the tests and
   respect the project's code style. This project uses ``tox`` for running the
   tests on multiple versions of Python (with ``pytest`` and ``coverage``),
   and for formatting (with ``ruff``)::

    $ tox -e py38,py39,py310,py311,py312,py313  # add any other supported versions
    $ tox -e style

5. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

6. Submit a pull request through the GitHub website.
