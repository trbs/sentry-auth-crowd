# -*- coding: utf-8 -*-
from __future__ import absolute_import

import logging

from django.contrib.auth.backends import ModelBackend
from django.db import transaction

from sentry.models import User, UserEmail, Organization, OrganizationMember
from sentry.models import OrganizationMemberTeam, Team
from sentry.models import AuditLogEntry, AuditLogEntryEvent

import crowd

from .constants import CROWD_URL, CROWD_APP_NAME, CROWD_APP_PASSWORD
from .constants import CROWD_DEFAULT_TEAM_SLUGS


def new_user(username, success):
    # see https://github.com/getsentry/sentry/blob/master/src/sentry/auth/helper.py
    name = success['name']
    email = success['email']
    with transaction.atomic():
        user = User.objects.create(
            username=username,
            email=email,
            name=name,
            is_managed=True,
        )
        if not UserEmail.objects.filter(user=user).exists():
            user_email = UserEmail.objects.create(user=user)
            user_email.email = email
            user_email.save()

        if not OrganizationMember.objects.filter(user=user).exists():
            organization = Organization.get_default()

            om = OrganizationMember.objects.create(
                organization=organization,
                role=organization.default_role,
                user=user,
                flags=getattr(OrganizationMember.flags, 'sso:linked'),
            )

            if CROWD_DEFAULT_TEAM_SLUGS:
                for team_slug in set(CROWD_DEFAULT_TEAM_SLUGS):
                    try:
                        team = Team.objects.get(slug=team_slug)
                    except Team.DoesNotExist:
                        logging.exception("Unable to fetch Team with slug '%s'",
                                          team_slug)
                    else:
                        OrganizationMemberTeam.objects.create(
                            team=team,
                            organizationmember=om,
                        )

            AuditLogEntry.objects.create(
                organization=organization,
                actor=user,
                target_object=om.id,
                target_user=om.user,
                event=AuditLogEntryEvent.MEMBER_ADD,
                data=om.get_audit_log_data(),
            )
        return user


class SentryCrowdBackend(ModelBackend):
    """
    Authenticate against Crowd server.

    Auto create account if not exists already
    """

    def __init__(self, *args, **kwargs):
        self._crowd = crowd.CrowdServer(CROWD_URL, CROWD_APP_NAME, CROWD_APP_PASSWORD)
        super(SentryCrowdBackend, self).__init__(*args, **kwargs)

    def authenticate(self, username=None, password=None):
        if username is None or password is None:
            return None

        success = self._crowd.auth_user(username, password)
        if success:
            try:
                user = User.objects.filter(is_active=True).exclude(password='!').get(username=username)
            except User.DoesNotExist:
                user = new_user(username, success)

            return user

        # Example of how token based (SSO) authentication looks like
        #
        # # Create a session. The important bit is the token.
        # session = cs.get_session(username, password)
        #
        # # Check that the token is valid (and of course it should be).
        # success = cs.validate_session(session['token'])

        return None
