===============================
designate-infoblox
===============================

Provides an integration between Designate and Infoblox grids.

* Free software: Apache license
* Documentation: http://docs.openstack.org/developer/designate-infoblox
* Source: http://git.openstack.org/cgit/stackforge/designate-infoblox
* Bugs: http://bugs.launchpad.net/designate-infoblox

Features
--------

The Infoblox Designate integration allows an Infoblox grid to be used for serving zones controlled by OpenStack Designate.

Devstack
--------

* Setup link to backend-infoblox

Setup
-----

*Setting Up Infoblox for Designate*

* Set up one or more name server groups to be used to serve designate zones.
     * Set the Designate mDNS servers as external primaries
               * Q - can we do multi-master?
     * Add a grid member as a grid secondary; select the "Lead Secondary" option for this member
     * Add additional grid secondaries as desired
* Create a user for use by Designate

*Setting Up Designate for Infoblox*

* Install the Infoblox Designate backend driver
* Designate may be configured to talk to any number of grid API services points (GM or Cloud appliance)
     * A pool target is defined for each API service point that Designate should talk to
     * A single Designate pool should point to only one API service point in any single grid
     * It is OK to point a pool at multiple grids, just not to multiple service points on the same grid
* The [infoblox:backend] stanza in the designate configuration file can be used to set default values for the grid connectivity and other information; these values can be overridden on a per-target basis with the "options" element of the target configuration.
* Designate always puts any servers 


*Example Designate Configuration*

::

 [pool:794ccc2c-d751-44fe-b57f-8894c9f5c842]
 #Specify the API service points for each grid
 targets = f26e0b32-736f-4f0a-831b-039a415c481e
 # Specify the lead secondary servers configured in the NS groups
 # for each target.
 nameservers = ffedb95e-edc1-11e4-9ae6-000c29db281b

 [pool_target:f26e0b32-736f-4f0a-831b-039a415c481e]
 type = infoblox
 # wapi_url, username, password can all be overridden from the defaults
 # allowing targets to point to different grids
 options = net_view: default, dns_view: default, ns_group: Designate

 [pool_nameserver:ffedb95e-edc1-11e4-9ae6-000c29db281b]
 host=172.16.98.200
 port=53


 [backend:infoblox]
 # The values below will be used for all targets unless overridden
 # in the target configuration. http_* options may only be set here,
 # not at the target level.
 http_pool_maxsize = 100
 http_pool_connections = 100
 wapi_url = https://172.16.98.200/wapi/v2.1/
 sslverify = False
 password = infoblox
 username = admin
 multi_tenant = False

* TODO
