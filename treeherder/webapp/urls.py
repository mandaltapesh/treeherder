# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, you can obtain one at http://mozilla.org/MPL/2.0/.

from django.conf.urls import patterns, include, url
from django.contrib import admin

from .api import urls as api_urls
from treeherder.embed import urls as embed_urls

from django_browserid.admin import site as browserid_admin
browserid_admin.copy_registry(admin.site)

urlpatterns = patterns('',
                       url(r'^api/', include(api_urls)),
                       url(r'^embed/', include(embed_urls)),
                       url(r'^admin/', include(browserid_admin.urls)),
                       url(r'^docs/', include('rest_framework_swagger.urls')),
                       url(r'', include('django_browserid.urls')),
                       )
