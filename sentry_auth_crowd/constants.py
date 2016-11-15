# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from django.conf import settings


CROWD_URL = getattr(settings, 'CROWD_URL', None)
CROWD_APP_NAME = getattr(settings, 'CROWD_APP_NAME', None)
CROWD_APP_PASSWORD = getattr(settings, 'CROWD_APP_PASSWORD', None)
CROWD_DEFAULT_TEAM_SLUGS = getattr(settings, 'CROWD_DEFAULT_TEAM_SLUGS', None)
