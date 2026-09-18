#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Vendors
Contains the operations for a vendor resource.
	1. get_vendors(self, **kwargs) -> requests.Response
	2. get_vendor(self, vendor_id: str) -> requests.Response
	3. create_vendor(self, payload: dict) -> requests.Response
	4. update_vendor(self, vendor_id: str, payload: dict) -> requests.Response
	5. delete_vendor(self, vendor_id: str) -> requests.Response
"""

import os
import unittest
from sasci360apiplan import vendors


class TestVendors(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = os.environ.get("CI360_ALGORITHM", "HS256")
		api = os.environ.get("CI360_API", "/marketingPlan")
		encoding = os.environ.get("CI360_ENCODING", "UTF-8")
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.vendors = vendors.Vendors(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_vendors(self):
		"""
		1. get_vendors(self, **kwargs) -> requests.Response
		"""
		result = self.vendors.get_vendors()
		print(result)
		self.assertIsNotNone(result)

	def test_get_vendor(self):
		"""
		2. get_vendor(self, vendor_id: str) -> requests.Response
		"""
		vendor_id = "0"
		result = self.vendors.get_vendor(vendor_id=vendor_id)
		print(result)
		self.assertIsNotNone(result)

	def test_create_vendor(self):
		"""
		3. create_vendor(self, payload: dict) -> requests.Response
		"""
		payload = {
			"id": "string",
			"name": "string",
			"description": "string",
			"currency": "string",
			"number": "string",
			"obsolete": True,
			"links": [
				{
					"method": "GET",
					"rel": "self",
					"href": "https://extapigwservice-<server>/<endpoint>/",
					"uri": "/<endpoint>",
					"type": "application/vnd.sas.collection"
				}
			],
			"version": 0
		}
		result = self.vendors.create_vendor(payload)
		print(result)
		self.assertIsNotNone(result)

	def test_update_vendor(self):
		"""
		4. update_vendor(self, vendor_id: str, payload: dict) -> requests.Response
		"""
		vendor_id = "0"
		payload = {
			"id": "string",
			"name": "string",
			"description": "string",
			"currency": "string",
			"number": "string",
			"associatedObjectCount": 0,
			"obsolete": True,
			"createdBy": "string",
			"modifiedBy": "string",
			"creationTimeStamp": "2019-08-24T14:15:22Z",
			"modifiedTimeStamp": "2019-08-24T14:15:22Z",
			"links": [
				{
					"method": "GET",
					"rel": "self",
					"href": "https://extapigwservice-<server>/<endpoint>/",
					"uri": "/<endpoint>",
					"type": "application/vnd.sas.collection"
				}
			],
			"version": 0
		}
		result = self.vendors.update_vendor(vendor_id=vendor_id, payload=payload)
		print(result)
		self.assertIsNotNone(result)

	def test_delete_vendor(self):
		"""
		5. delete_vendor(self, vendor_id: str) -> requests.Response
		"""
		vendor_id = "0"
		result = self.vendors.delete_vendor(vendor_id=vendor_id)
		print(result)
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
