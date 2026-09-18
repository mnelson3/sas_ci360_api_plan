#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Cost Centers
Contains the operations for cost center collections.
	1. get_cost_centers(self, **kwargs) -> requests.Response
	2. get_cost_center(self, cost_center_id: str) -> requests.Response
	3. create_cost_center(self, payload: dict) -> requests.Response
	4. update_cost_center(self, cost_center_id: str, payload: dict) -> requests.Response
	5. delete_cost_center(self, cost_center_id: str) -> requests.Response
"""

import os
import unittest
from sasci360apiplan import cost_centers


class TestCostCenters(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = os.environ.get("CI360_ALGORITHM", "HS256")
		api = os.environ.get("CI360_API", "/marketingPlan")
		encoding = os.environ.get("CI360_ENCODING", "UTF-8")
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.cost_centers = cost_centers.CostCenters(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_cost_centers(self):
		"""
		1. get_cost_centers(self, **kwargs) -> requests.Response
		"""
		result = self.cost_centers.get_cost_centers()
		print(result)
		self.assertIsNotNone(result)

	def test_get_cost_center(self):
		"""
		2. get_cost_center(self, cost_center_id: str) -> requests.Response
		"""
		cost_center_id = "0"
		result = self.cost_centers.get_cost_center(cost_center_id=cost_center_id)
		print(result)
		self.assertIsNotNone(result)

	def test_create_cost_center(self):
		"""
		3. create_cost_center(self, payload: dict) -> requests.Response
		"""
		payload = {
			"id": "string",
			"name": "string",
			"description": "string",
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
		result = self.cost_centers.create_cost_center(payload=payload)
		print(result)
		self.assertIsNotNone(result)

	def test_update_cost_center(self):
		"""
		4. update_cost_center(self, cost_center_id: str, payload: dict) -> requests.Response
		"""
		cost_center_id = "0"
		payload = {
			"id": "string",
			"name": "string",
			"description": "string",
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
		result = self.cost_centers.update_cost_center(cost_center_id=cost_center_id, payload=payload)
		print(result)
		self.assertIsNotNone(result)

	def test_delete_cost_center(self):
		"""
		5. delete_cost_center(self, cost_center_id: str) -> requests.Response
		"""
		cost_center_id = "0"
		result = self.cost_centers.delete_cost_center(cost_center_id=cost_center_id)
		print(result)
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
