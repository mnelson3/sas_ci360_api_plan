#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Planning Items
Contains the operations for planning item collections.
	1. get_planning_items(self, **kwargs) -> requests.Response
	2. get_planning_items_tree(self, **kwargs) -> requests.Response
	3. get_planning_item(self, planning_item_id: str) -> requests.Response
	4. create_planning_item(self, payload: dict, **kwargs) -> requests.Response
	5. update_planning_item(self, planning_item_id: str, payload: dict) -> requests.Response
	6. rename_planning_item(self, planning_item_id: str, payload: dict) -> requests.Response
	7. delete_planning_item(self, planning_item_id: str) -> requests.Response
	8. add_planning_item(self, planning_item_id: str, payload: dict) -> requests.Response
	9. get_planning_item_hierarchy(self, planning_item_id: str) -> requests.Response
	10. get_planning_item_children(self, planning_item_id: str, **kwargs) -> requests.Response
	11. create_planning_item_children(self, planning_item_id: str, payload: dict) -> requests.Response
	12. add_planning_item_associations(self, planning_item_id: str, payload: dict) -> requests.Response
	13. remove_planning_item_associations(self, planning_item_id: str, payload: dict) -> requests.Response
	14. get_planning_item_children_tree(self, planning_item_id: str, **kwargs) -> requests.Response
"""

import os
import unittest
from sasci360apiplan import planning_items


class TestPlanningItems(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = os.environ.get("CI360_ALGORITHM", "HS256")
		api = os.environ.get("CI360_API", "/marketingPlan")
		encoding = os.environ.get("CI360_ENCODING", "UTF-8")
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.planning_items = planning_items.PlanningItems(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_planning_items(self):
		result = self.planning_items.get_planning_items()
		print(result)
		self.assertIsNotNone(result)

	def test_get_planning_item(self):
		planning_item_id = "0"
		result = self.planning_items.get_planning_item(planning_item_id=planning_item_id)
		print(result)
		self.assertIsNotNone(result)

	def test_get_planning_items_tree(self):
		result = self.planning_items.get_planning_items_tree()
		print(result)
		self.assertIsNotNone(result)

	def test_get_planning_item_children(self):
		planning_item_id = "0"
		result = self.planning_items.get_planning_item_children(planning_item_id=planning_item_id)
		print(result)
		self.assertIsNotNone(result)

	def test_get_planning_item_children_tree(self):
		planning_item_id = "0"
		result = self.planning_items.get_planning_item_children_tree(planning_item_id=planning_item_id)
		print(result)
		self.assertIsNotNone(result)

	def test_get_planning_item_hierarchy(self):
		planning_item_id = "0"
		result = self.planning_items.get_planning_item_hierarchy(planning_item_id=planning_item_id)
		print(result)
		self.assertIsNotNone(result)

	def test_create_planning_item(self):
		payload = {
			"id": "string",
			"number": "string",
			"name": "string",
			"description": "string",
			"plannedStartDate": "2019-08-24T14:15:22Z",
			"plannedEndDate": "2019-08-24T14:15:22Z",
			"currencyCode": "string",
			"businessUnit": {
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
			},
			"budgetInformation": {
				"id": "string",
				"description": "string",
				"budget": 0,
				"reservedBudgetSameAsBudget": True,
				"availableBudget": 0,
				"allocatedBudget": 0,
				"reservedBudget": 0,
				"rolledUpBudget": 0,
				"totalCommitted": 0,
				"totalInvoiced": 0,
				"totalCommitmentOutstanding": 0,
				"totalCommitmentOverspent": 0,
				"spendNotOnCostCenters": 0,
				"totalExpenses": 0,
				"availableToSpend": 0,
				"costCenterBreakupTotal": 0,
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
			},
			"hierarchyDefinitionId": "string",
			"hierarchyDefinitionLevelId": "string",
			"hierarchyLevel": "string",
			"state": "planning",
			"statusLocalized": "string",
			"tags": [
				{
					"id": "string",
					"name": "string",
					"modifiedStatusCode": "string",
					"count": 0,
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
			],
			"type": "planningObject",
			"customAttributes": [
				{
					"groupId": "string",
					"label": "string",
					"visible": True,
					"obsolete": True,
					"fields": [
						{
							"label": "string",
							"value": [
								{
									"label": "string"
								}
							],
							"attributeCode": "string",
							"type": "string",
							"visible": True,
							"obsolete": True,
							"adHoc": True,
							"dynamic": True,
							"validator": [
								{
									"required": True
								}
							],
							"dataProvider": [
								{
									"key": "string",
									"text": "string"
								}
							]
						}
					]
				}
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
			],
			"version": 0
		}
		result = self.planning_items.create_planning_item(payload=payload)
		print(result)
		self.assertIsNotNone(result)

	def test_create_planning_item_children(self):
		planning_item_id = "0"
		payload = {
			"id": "string",
			"number": "string",
			"name": "string",
			"description": "string",
			"plannedStartDate": "2019-08-24T14:15:22Z",
			"plannedEndDate": "2019-08-24T14:15:22Z",
			"currencyCode": "string",
			"businessUnit": {
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
			},
			"budgetInformation": {
				"id": "string",
				"description": "string",
				"budget": 0,
				"reservedBudgetSameAsBudget": True,
				"availableBudget": 0,
				"allocatedBudget": 0,
				"reservedBudget": 0,
				"rolledUpBudget": 0,
				"totalCommitted": 0,
				"totalInvoiced": 0,
				"totalCommitmentOutstanding": 0,
				"totalCommitmentOverspent": 0,
				"spendNotOnCostCenters": 0,
				"totalExpenses": 0,
				"availableToSpend": 0,
				"costCenterBreakupTotal": 0,
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
			},
			"hierarchyDefinitionId": "string",
			"hierarchyDefinitionLevelId": "string",
			"hierarchyLevel": "string",
			"state": "planning",
			"statusLocalized": "string",
			"tags": [
				{
					"id": "string",
					"name": "string",
					"modifiedStatusCode": "string",
					"count": 0,
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
			],
			"type": "planningObject",
			"customAttributes": [
				{
					"groupId": "string",
					"label": "string",
					"visible": True,
					"obsolete": True,
					"fields": [
						{
							"label": "string",
							"value": [
								{
									"label": "string"
								}
							],
							"attributeCode": "string",
							"type": "string",
							"visible": True,
							"obsolete": True,
							"adHoc": True,
							"dynamic": True,
							"validator": [
								{
									"required": True
								}
							],
							"dataProvider": [
								{
									"key": "string",
									"text": "string"
								}
							]
						}
					]
				}
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
			],
			"version": 0
		}
		result = self.planning_items.create_planning_item_children(planning_item_id=planning_item_id, payload=payload)
		print(result)
		self.assertIsNotNone(result)

	def test_rename_planning_item(self):
		planning_item_id = "0"
		payload = {"op": "add", "path": "string", "value": {}, "from": "string"}
		result = self.planning_items.rename_planning_item(planning_item_id=planning_item_id, payload=payload)
		print(result)
		self.assertIsNotNone(result)

	def test_delete_planning_item(self):
		planning_item_id = "0"
		result = self.planning_items.delete_planning_item(planning_item_id=planning_item_id)
		print(result)
		self.assertIsNotNone(result)

	def test_add_planning_item(self):
		planning_item_id = "0"
		payload = {
			"id": "string",
			"number": "string",
			"name": "string",
			"description": "string",
			"plannedStartDate": "2019-08-24T14:15:22Z",
			"plannedEndDate": "2019-08-24T14:15:22Z",
			"currencyCode": "string",
			"businessUnit": {
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
			},
			"budgetInformation": {
				"id": "string",
				"description": "string",
				"budget": 0,
				"reservedBudgetSameAsBudget": True,
				"availableBudget": 0,
				"allocatedBudget": 0,
				"reservedBudget": 0,
				"rolledUpBudget": 0,
				"totalCommitted": 0,
				"totalInvoiced": 0,
				"totalCommitmentOutstanding": 0,
				"totalCommitmentOverspent": 0,
				"spendNotOnCostCenters": 0,
				"totalExpenses": 0,
				"availableToSpend": 0,
				"costCenterBreakupTotal": 0,
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
			},
			"hierarchyDefinitionId": "string",
			"hierarchyDefinitionLevelId": "string",
			"hierarchyLevel": "string",
			"state": "planning",
			"statusLocalized": "string",
			"tags": [
				{
					"id": "string",
					"name": "string",
					"modifiedStatusCode": "string",
					"count": 0,
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
			],
			"type": "planningObject",
			"customAttributes": [
				{
					"groupId": "string",
					"label": "string",
					"visible": True,
					"obsolete": True,
					"fields": [
						{
							"label": "string",
							"value": [
								{
									"label": "string"
								}
							],
							"attributeCode": "string",
							"type": "string",
							"visible": True,
							"obsolete": True,
							"adHoc": True,
							"dynamic": True,
							"validator": [
								{
									"required": True
								}
							],
							"dataProvider": [
								{
									"key": "string",
									"text": "string"
								}
							]
						}
					]
				}
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
			],
			"version": 0
		}
		result = self.planning_items.add_planning_item(planning_item_id=planning_item_id, payload=payload)
		print(result)
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
