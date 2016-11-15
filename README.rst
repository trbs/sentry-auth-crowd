Crowd Auth Backend for Sentry
=============================

A Crowd authentication backend for Sentry.


Install
-------

.. code-block:: console

    $ pip install sentry-auth-crowd


Setup
-----

In Atlassian Crowd create an application for Sentry we will need the
application name and password for the Sentry configuration.

Make sure the remote addresses are set correct to avoid authentication failures.

The following settings should be set in ``sentry.conf.py``:

.. code-block:: python

    # Url of the Crowd server
    CROWD_URL = ""
    # The application name of Sentry in Crowd
    CROWD_APP_NAME = ""
    # The application password of Sentry in Crowd
    CROWD_APP_PASSWORD = ""
    # The team slugs a new user should automatically be member of.
    CROWD_DEFAULT_TEAM_SLUGS = []


SSO Support
-----------

sentry-auth-crowd current does not support the SSO authproviders from Sentry.
We are happy to accept PR's to add support for this.
