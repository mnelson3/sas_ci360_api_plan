#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Commitments
Contains the operations for commitment collections.
	1. get_commitments(self, planning_item_id: str, **kwargs) -> requests.Response
	2. get_commitment(self, planning_item_id: str, commitment_id: str) -> requests.Response
	3. create_commitment(self, planning_item_id: str, payload: dict) -> requests.Response
	4. update_commitment(self, planning_item_id: str, commitment_id: str, payload: dict) -> requests.Response
	5. delete_commitment(self, planning_item_id: str, commitment_id: str) -> requests.Response
	6. close_commitment(self, planning_item_id: str, commitment_id: str, payload: dict) -> requests.Response
"""

import os
import unittest
from sasci360apiplan import commitments


class TestCommitments(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = os.environ.get("CI360_ALGORITHM", "HS256")
		api = os.environ.get("CI360_API", "/marketingPlan")
		encoding = os.environ.get("CI360_ENCODING", "UTF-8")
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.commitments = commitments.Commitments(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_commitments(self):
		"""
		1. get_commitments(self, planning_item_id: str, **kwargs) -> requests.Response
		"""
		planning_item_id = "0"
		result = self.commitments.get_commitments(planning_item_id=planning_item_id)
		print(result)
		self.assertIsNotNone(result)

	def test_get_commitment(self):
		"""
		2. get_commitment(self, planning_item_id: str, commitment_id: str) -> requests.Response
		"""
		planning_item_id = "0"
		commitment_id = "0"
		result = self.commitments.get_commitment(planning_item_id=planning_item_id, commitment_id=commitment_id)
		print(result)
		self.assertIsNotNone(result)

	def test_create_commitment(self):
		"""
		3. create_commitment(self, planning_item_id: str, payload: dict) -> requests.Response
		"""
		planning_item_id = "0"
		payload = {
			"id": "string",
			"name": "string",
			"description": "string",
			"state": "new",
			"amount": 0,
			"vendorAmount": 0,
			"outstandingAmount": 0,
			"overspentAmount": 0,
			"number": "string",
			"invoiceCount": 0,
			"invoicedAmount": 0,
			"vendor": {
				"id": "string",
				"name": "string",
				"description": "string",
				"currency": "string",
				"number": "string",
				"obsolete": True,
				"associatedObjectCount": 0,
				"modifiedBy": "string",
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
			"paymentDate": "2019-08-24T14:15:22Z",
			"commitmentCreatedDate": "2019-08-24T14:15:22Z",
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
		result = self.commitments.create_commitment(planning_item_id=planning_item_id, payload=payload)
		print(result)
		self.assertIsNotNone(result)

	def test_update_commitment(self):
		"""
		4. update_commitment(self, planning_item_id: str, commitment_id: str, payload: dict) -> requests.Response
		"""
		planning_item_id = "0"
		commitment_id = "0"
		payload = {
			"id": "string",
			"name": "string",
			"description": "string",
			"state": "new",
			"amount": 0,
			"vendorAmount": 0,
			"outstandingAmount": 0,
			"overspentAmount": 0,
			"number": "string",
			"invoiceCount": 0,
			"invoicedAmount": 0,
			"vendor": {
				"id": "string",
				"name": "string",
				"description": "string",
				"currency": "string",
				"number": "string",
				"obsolete": True,
				"associatedObjectCount": 0,
				"modifiedBy": "string",
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
			"paymentDate": "2019-08-24T14:15:22Z",
			"commitmentCreatedDate": "2019-08-24T14:15:22Z",
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
		result = self.commitments.update_commitment(planning_item_id=planning_item_id, commitment_id=commitment_id, payload=payload)
		print(result)
		self.assertIsNotNone(result)

	def test_delete_commitment(self):
		"""
		5. delete_commitment(self, planning_item_id: str, commitment_id: str) -> requests.Response
		"""
		planning_item_id = "0"
		commitment_id = "0"
		result = self.commitments.delete_commitment(planning_item_id=planning_item_id, commitment_id=commitment_id)
		print(result)
		self.assertIsNotNone(result)

	def test_close_commitment(self):
		"""
		6. close_commitment(self, planning_item_id: str, commitment_id: str, payload: dict) -> requests.Response
		"""
		planning_item_id = "0"
		commitment_id = "0"
		payload = {
			"id": "string",
			"name": "string",
			"description": "string",
			"state": "closed",
			"amount": 0,
			"vendorAmount": 0,
			"outstandingAmount": 0,
			"overspentAmount": 0,
			"number": "string",
			"invoiceCount": 0,
			"invoicedAmount": 0,
			"vendor": {
				"id": "string",
				"name": "string",
				"description": "string",
				"currency": "string",
				"number": "string",
				"obsolete": True,
				"associatedObjectCount": 0,
				"modifiedBy": "string",
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
			"paymentDate": "2019-08-24T14:15:22Z",
			"commitmentCreatedDate": "2019-08-24T14:15:22Z",
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
		result = self.commitments.close_commitment(planning_item_id=planning_item_id, commitment_id=commitment_id, payload=payload)
		print(result)
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
