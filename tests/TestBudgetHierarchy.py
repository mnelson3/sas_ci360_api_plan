#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Budget Hierarchy Module
Contains the operations for a planning hierarchy's budget details
	1. get_budget(self, planning_item_id: str) -> requests.Response
	2. update_budget(self, planning_item_id: str, payload: dict) -> requests.Response
"""

import os
import unittest
from sasci360apiplan import budget_hierarchy


class TestBudgetHierarchy(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = os.environ.get("CI360_ALGORITHM", "HS256")
		api = os.environ.get("CI360_API", "/marketingPlan")
		encoding = os.environ.get("CI360_ENCODING", "UTF-8")
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.budget_hierarchy = budget_hierarchy.BudgetHierarchy(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_budget(self):
		"""
		1. get_budget(self, planning_item_id: str) -> requests.Response
		"""
		planning_item_id = "0"
		result = self.budget_hierarchy.get_budget(planning_item_id=planning_item_id)
		self.assertIsNotNone(result)

	def test_update_budget(self):
		"""
		2. update_budget(self, planning_item_id: str, payload: dict) -> requests.Response
		"""
		planning_item_id = "0"
		payload = {
			"id": "string",
			"rootId": "string",
			"name": "string",
			"budget": 0,
			"reservedBudgetSameAsBudget": True,
			"reservedBudget": 0,
			"availableBudget": 0,
			"expenses": 0,
			"availableToSpend": 0,
			"allocatedBudget": 0,
			"rolledUpBudget": 0,
			"children": [
				{}
			],
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
			]
		}
		result = self.budget_hierarchy.update_budget(planning_item_id=planning_item_id, payload=payload)
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
