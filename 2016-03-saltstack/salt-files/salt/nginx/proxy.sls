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
{% macro proxy(site, server, port, http=True, https=False) -%}

extend:
  nginx:
    service:
      - watch:
        - file: /etc/nginx/sites-enabled/{{ site }}

/etc/nginx/sites-enabled/{{ site }}:
  file.managed:
    - source: salt://nginx/proxy.conf
    - template: jinja
    - context: {
      site: {{ site }},
      server: {{ server }},
      port: {{ port }},
      http: {{ http }},
      https: {{ https }} }
    {% if https -%}
    - require:
      - file: /var/lib/nginx/ssl/{{ site }}.proxy.crt
      - file: /var/lib/nginx/ssl/{{ site }}.proxy.key
    {%- endif %}

{% if https -%}
/var/lib/nginx/ssl/{{ site }}.proxy.crt:
  file.managed:
    - contents_pillar: nginx_ssl_crt

/var/lib/nginx/ssl/{{ site }}.proxy.key:
  file.managed:
    - contents_pillar: nginx_ssl_key
{%- endif %}

{%- endmacro %}
