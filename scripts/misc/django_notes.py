##########################################################################
"""                        Django MTV Structure                        """
##########################################################################
"""
Models: Used to organize data, models provide the interface for views to communicate with the database. Models can display complex behaviors including multiple inheritance. Forms can be built on models (or independently) to facilitate even more complicated communiation with views. The module can also be omitted/replaced with custom modules.

Templates: User to generate HTML to send via HTTP Responses. The template language can be used to automate complicated template structures. The templates can also load CSS, JavaScript, HTMX, and similar resources to create "reactive" pages with complex behavior displayed by the client web browser. The module can also be omitted/replaced with custom modules.

Views: Each URL is routed to a view that controls how models and templates are utilized for that URL resource. Many different parameters can be used to determine these behaviors including information from the database, user profiles, the httprequest, etc. """


##########################################################################
"""                          Django Modules                            """
##########################################################################
""" The remainder of this document imports all modules that I commonly use and provides additional information on their use. These are personal notes intended for my own use. """
##########################################################################


""" APPS """
from django.apps import AppConfig
    # In settings, add each app to INSTALLED_APPS = []



""" CONTRIB """

import django.contrib.admin

import django.contrib.auth

import django.contrib.contenttypes

import django.contrib.flatpages

import django.contrib.gis

import django.contrib.humanize

import django.contrib.messages

import django.contrib.postgres

import django.contrib.redirects

import django.contrib.sessions

import django.contrib.sitemaps

import django.contrib.sites

import django.contrib.staticfiles

import django.contrib.syndication


""" CORE """
import django.core.checks

import django.core.exceptions

import django.core.files

import django.core.mail

import django.core.management

import django.core.paginator

import django.core.signals

import django.core.signing

import django.core.validators


##########################################################################
"""                               DATABASE                             """
##########################################################################


import django.db.backends

import django.db.migrations

import django.db.models

import django.db.transaction

from django.db import dispatch


##########################################################################
"""                               FORMS                                """
##########################################################################


""" FORMS """
import django.forms.fields

import django.forms.formsets

import django.forms.models

import django.forms.renderers

import django.forms.widgets


""" HTTP """
from django.http import HttpResponse

""" MIDDLEWARE """
import django.middleware

""" SHORTCUTS """
from django.shortcuts import get_object_or_404, get_list_or_404, render # for simple HttpResponses

""" TEMPLATE """
import django.template

""" TEST """
import django.test

""" URLS """
from django.urls import path, re_path, include, register_converter, reverse, i18n
import django.conf.urls.static
from django.conf.urls import handler400, handler403, handler404, handler500

""" UTILS """
import django.utils


##########################################################################
"""                               VIEWS                                """
##########################################################################


import django.views.decorators

from django.views.defaults import bad_request, page_not_found, permission_denied, server_error

from django.views.generic import ListView, DetailView, ArchiveIndexView
import django.views.generic.dates
import django.views.i18n # - See Internationalization/Translation
from django.views.static import serve


##########################################################################
"""                               END                                  """
##########################################################################
