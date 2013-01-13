c3s.app
========

c3s.app is an early version of a registration and asset management tool 
for a creative commons collecting society. earliest alpha :-)

It is also a demo app for the cone stack, building on pyramid.

Two content types are in this: bands and tracks. A band object can contain 
tracks...


requirements
-------------

in order to set it up successfully, you need several packages available on your system:

 - libxml2
 - libxslt1.1
 - python-lxml
 - libxml2-dev
 - libxslt1-dev
 - libldap2-dev
 - libsasl2-dev


setup / installation
---------------------


 0. virtualenv . && . bin/activate
 1. python bootstrap.py
 2. bin/buildout
 3. bin/testldap start groupOfNames_10_10
 4. bin/paster serve c3s.app.ini
 5. open http://127.0.0.1:8082 in a browser,
    login as admin w/ pw admin
