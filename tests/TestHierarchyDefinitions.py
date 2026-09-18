#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Hierarchy Definitions
Contains the operations for hierarchy definition collections.
	1. get_hierarchy_definitions(self, **kwargs) -> requests.Response
	2. get_hierarchy_definition(self, hierarchy_definition_id: str) -> requests.Response
	3. create_hierarchy_definition(self, payload: dict) -> requests.Response
	4. update_hierarchy_definition(self, hierarchy_definition_id: str, payload: dict) -> requests.Response
	5. delete_hierarchy_definition(self, hierarchy_definition_id: str) -> requests.Response
"""

import os
import unittest
from sasci360apiplan import hierarchy_definitions


class TestHierarchyDefinitions(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = os.environ.get("CI360_ALGORITHM", "HS256")
		api = os.environ.get("CI360_API", "/marketingPlan")
		encoding = os.environ.get("CI360_ENCODING", "UTF-8")
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.hierarchy_definitions = hierarchy_definitions.HierarchyDefinitions(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_hierarchy_definitions(self):
		"""
		1. get_hierarchy_definitions(self, **kwargs) -> requests.Response
		"""
		result = self.hierarchy_definitions.get_hierarchy_definitions()
		print(result)
		self.assertIsNotNone(result)

	def test_get_hierarchy_definition(self):
		"""
		2. get_hierarchy_definition(self, hierarchy_definition_id: str) -> requests.Response
		"""
		hierarchy_definition_id = "0"
		result = self.hierarchy_definitions.get_hierarchy_definition(hierarchy_definition_id=hierarchy_definition_id)
		print(result)
		self.assertIsNotNone(result)

	def test_create_hierarchy_definition(self):
		"""
		3. create_hierarchy_definition(self, payload: dict) -> requests.Response
		"""
		payload = {
			"id": "string",
			"name": "string",
			"description": "string",
			"generalLedgerCode": "string",
			"associatedCostCenterCount": 0,
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
		result = self.hierarchy_definitions.create_hierarchy_definition(payload=payload)
		print(result)
		self.assertIsNotNone(result)

	def test_update_hierarchy_definition(self):
		"""
		4. update_hierarchy_definition(self, hierarchy_definition_id: str, payload: dict) -> requests.Response
		"""
		hierarchy_definition_id = "0"
		payload = {
			"id": "string",
			"name": "string",
			"description": "string",
			"generalLedgerCode": "string",
			"associatedCostCenterCount": 0,
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
		result = self.hierarchy_definitions.update_hierarchy_definition(hierarchy_definition_id=hierarchy_definition_id, payload=payload)
		print(result)
		self.assertIsNotNone(result)

	def test_delete_hierarchy_definition(self):
		"""
		5. delete_hierarchy_definition(self, hierarchy_definition_id: str) -> requests.Response
		"""
		hierarchy_definition_id = "0"
		result = self.hierarchy_definitions.delete_hierarchy_definition(hierarchy_definition_id=hierarchy_definition_id)
		print(result)
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
