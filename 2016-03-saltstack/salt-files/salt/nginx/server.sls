# Copyright 2012-2013 Hewlett-Packard Development Company, L.P.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
{% macro server(site, host, port, path, index=False) %}

extend:
  nginx:
    service:
      - watch:
        - file: /etc/nginx/sites-enabled/{{ site }}

/etc/nginx/sites-enabled/{{ site }}:
  file.managed:
    - source: salt://nginx/server.conf
    - template: jinja
    - context: {
      site: {{ site }},
      host: {{ host }},
      port: {{ port }},
      path: {{ path }},
      index: {{ index }} }

{% endmacro %}
