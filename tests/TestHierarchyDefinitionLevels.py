#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Hierarchy Definition Levels
Contains the operations for a hierarchy level resource.
	1. get_hierarchy_definition_levels(self, hierarchy_definition_id: str, **kwargs) -> requests.Response
	2. get_hierarchy_definition_level(self, hierarchy_definition_id: str, hierarchy_definition_level_id: str) -> requests.Response
	3. create_hierarchy_definition_level(self, hierarchy_definition_id: str, payload: dict) -> requests.Response
	4. update_hierarchy_definition_level(self, hierarchy_definition_id: str, hierarchy_definition_level_id: str, payload: dict) -> requests.Response
	5. delete_hierarchy_definition_level(self, hierarchy_definition_id: str, hierarchy_definition_level_id: str) -> requests.Response
"""

import os
import unittest
from sasci360apiplan import hierarchy_definition_levels


class TestHierarchyDefinitionLevels(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = os.environ.get("CI360_ALGORITHM", "HS256")
		api = os.environ.get("CI360_API", "/marketingPlan")
		encoding = os.environ.get("CI360_ENCODING", "UTF-8")
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.hierarchy_definition_levels = hierarchy_definition_levels.HierarchyDefinitionLevels(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_hierarchy_definition_levels(self):
		hierarchy_definition_id = "0"
		result = self.hierarchy_definition_levels.get_hierarchy_definition_levels(hierarchy_definition_id=hierarchy_definition_id)
		print(result)
		self.assertIsNotNone(result)

	def test_get_hierarchy_definition_level(self):
		hierarchy_definition_id = "0"
		hierarchy_definition_level_id = "0"
		result = self.hierarchy_definition_levels.get_hierarchy_definition_level(hierarchy_definition_id=hierarchy_definition_id, hierarchy_definition_level_id=hierarchy_definition_level_id)
		print(result)
		self.assertIsNotNone(result)

	def test_create_hierarchy_definition_level(self):
		hierarchy_definition_id = "0"
		payload = {
			"id": "string",
			"name": "string",
			"description": "string",
			"iconName": "string",
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
		result = self.hierarchy_definition_levels.create_hierarchy_definition_level(hierarchy_definition_id=hierarchy_definition_id, payload=payload)
		print(result)
		self.assertIsNotNone(result)

	def test_update_hierarchy_definition_level(self):
		hierarchy_definition_id = "0"
		hierarchy_definition_level_id = "0"
		payload = {
			"id": "string",
			"name": "string",
			"description": "string",
			"iconName": "string",
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
		result = self.hierarchy_definition_levels.update_hierarchy_definition_level(hierarchy_definition_id=hierarchy_definition_id, hierarchy_definition_level_id=hierarchy_definition_level_id, payload=payload)
		print(result)
		self.assertIsNotNone(result)

	def test_delete_hierarchy_definition_level(self):
		hierarchy_definition_id = "0"
		hierarchy_definition_level_id = "0"
		result = self.hierarchy_definition_levels.delete_hierarchy_definition_level(hierarchy_definition_id=hierarchy_definition_id, hierarchy_definition_level_id=hierarchy_definition_level_id)
		print(result)
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
