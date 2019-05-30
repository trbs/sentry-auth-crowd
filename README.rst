Crowd Auth Backend for Sentry
=============================

A Crowd authentication backend for Sentry.


Install
-------

.. code-block:: console

    $ pip install sentry-auth-crowd

If you are using `getsentry/onpremise`_ to install sentry, just add `sentry-auth-crowd` in getsentry/onpremise/requirements.txt .

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
    # Put this after AUTHENTICATION_BACKENDS declaration, if it not exists, just set
    AUTHENTICATION_BACKENDS = AUTHENTICATION_BACKENDS + (
        'sentry_auth_crowd.backend.SentryCrowdBackend',
    )
    
If you are using `getsentry/onpremise`_ to install sentry, after done above, remember to rerun *docker-compose build* then *docker-compose up -d*, now enjoy it!

.. _getsentry/onpremise: https://github.com/getsentry/onpremise 

SSO Support
-----------

sentry-auth-crowd current does not support the SSO authproviders from Sentry.
We are happy to accept PR's to add support for this.
