#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Business Units
Contains the operations for business unit collections.
	1. get_business_units(self, **kwargs) -> requests.Response
	2. get_business_unit(self, business_unit_id: str) -> requests.Response
	3. create_business_unit(self, payload: dict) -> requests.Response
	4. update_business_unit(self, business_unit_id: str, payload: dict) -> requests.Response
	5. delete_business_unit(self, business_unit_id: str) -> requests.Response
"""

import os
import unittest
from sasci360apiplan import business_units


class TestBusinessUnits(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = os.environ.get("CI360_ALGORITHM", "HS256")
		api = os.environ.get("CI360_API", "/marketingPlan")
		encoding = os.environ.get("CI360_ENCODING", "UTF-8")
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.business_units = business_units.BusinessUnits(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_business_units(self):
		"""
		1. get_business_units(self, **kwargs) -> requests.Response
		"""
		result = self.business_units.get_business_units()
		print(result)
		self.assertIsNotNone(result)

	def test_get_business_unit(self):
		"""
		2. get_business_unit(self, business_unit_id: str) -> requests.Response
		"""
		business_unit_id = "0"
		result = self.business_units.get_business_unit(business_unit_id=business_unit_id)
		print(result)
		self.assertIsNotNone(result)

	def test_create_business_unit(self):
		"""
		3. create_business_unit(self, payload: dict) -> requests.Response
		"""
		payload = {
			"id": "string",
			"name": "string",
			"description": "string",
			"currency": "string",
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
		result = self.business_units.create_business_unit(payload=payload)
		print(result)
		self.assertIsNotNone(result)

	def test_update_business_unit(self):
		"""
		4. update_business_unit(self, business_unit_id: str, payload: dict) -> requests.Response
		"""
		business_unit_id = "0"
		payload = {"operations": [{"op": "add", "path": "string", "value": {}, "from": "string"}]}
		result = self.business_units.update_business_unit(business_unit_id=business_unit_id, payload=payload)
		print(result)
		self.assertIsNotNone(result)

	def test_delete_business_unit(self):
		"""
		5. delete_business_unit(self, business_unit_id: str) -> requests.Response
		"""
		business_unit_id = "0"
		result = self.business_units.delete_business_unit(business_unit_id=business_unit_id)
		print(result)
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
