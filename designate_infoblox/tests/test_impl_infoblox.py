# Copyright 2014 Infoblox
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from mock import MagicMock

from designate import objects
from designate.tests.test_backend import BackendTestCase
from designate_infoblox.impl_infoblox import InfobloxBackend


class InfobloxBackendTestCase(BackendTestCase):

    def get_domain_fixture(self):
        return super(InfobloxBackendTestCase, self).get_domain_fixture(
            values={
                'name': 'test.example.com.'
            }
        )

    def setUp(self):
        super(InfobloxBackendTestCase, self).setUp()
        self.target = objects.PoolTarget.from_dict({
            'id': '4588652b-50e7-46b9-b688-a9bad40a873e',
            'type': 'infoblox',
            'masters': [],
            'options': [],
        })

        self.backend = InfobloxBackend(self.target)
        self.backend.start()
        self.backend.infoblox = MagicMock()

    def test_create_domain(self):
        context = self.get_context()
        domain = self.get_domain_fixture()
        self.backend.infoblox.get_dns_view = MagicMock(return_value='default')
        self.backend.create_domain(context, domain)
        self.backend.infoblox.create_zone_auth.assert_called_once_with(
                              fqdn='test.example.com',
                              dns_view='default')

    def test_update_domain(self):
        context = self.get_context()
        domain = self.get_domain_fixture()
        self.backend.update_domain(context, domain)

    def test_delete_domain(self):
        context = self.get_context()
        domain = self.get_domain_fixture()
        self.backend.create_domain(context, domain)
        self.backend.delete_domain(context, domain)
        self.backend.infoblox.delete_zone_auth.assert_called_once_with(
                              'test.example.com')
