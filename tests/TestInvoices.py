#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Invoices
Contains the operations for invoice collections.
	1. get_invoices_by_planning_item(self, planning_item_id: str, **kwargs) -> requests.Response
	2. get_invoices_by_commitment(self, planning_item_id: str, commitment_id: str, **kwargs) -> requests.Response
	3. get_invoice(self, planning_item_id: str, invoice_id: str) -> requests.Response
	4. get_invoice_by_commitment_invoice(self, planning_item_id: str, commitment_id: str, invoice_id: str) -> requests.Response
	5. create_invoice(self, planning_item_id: str, payload: dict) -> requests.Response
	6. create_invoice_under_commitment(self, planning_item_id: str, commitment_id: str, payload: dict) -> requests.Response
	7. move_invoice(self, planning_item_id: str, payload: dict) -> requests.Response
	8. move_invoice_by_commitment(self, planning_item_id: str, commitment_id: str, payload: dict) -> requests.Response
	9. update_invoice(self, planning_item_id: str, invoice_id: str, payload: dict) -> requests.Response
	10. update_invoice_under_commitment(self, planning_item_id: str, commitment_id: str, invoice_id: str, payload: dict) -> requests.Response
	11. delete_invoice_by_commitment(self, planning_item_id: str, commitment_id: str, invoice_id: str) -> requests.Response
	12. delete_invoice(self, planning_item_id: str, invoice_id: str) -> requests.Response
	13. reconcile_invoice(self, planning_item_id: str, invoice_id: str, payload: dict) -> requests.Response
	14. reconcile_invoice_by_commitment(self, planning_item_id: str, commitment_id: str, invoice_id: str, payload: dict) -> requests.Response
"""

import os
import unittest
from sasci360apiplan import invoices


class TestInvoices(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = os.environ.get("CI360_ALGORITHM", "HS256")
		api = os.environ.get("CI360_API", "/marketingPlan")
		encoding = os.environ.get("CI360_ENCODING", "UTF-8")
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.invoices = invoices.Invoices(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_invoices_by_planning_item(self):
		"""
		1. get_invoices_by_planning_item(self, planning_item_id: str, **kwargs) -> requests.Response
		"""
		planning_item_id = "0"
		result = self.invoices.get_invoices_by_planning_item(planning_item_id=planning_item_id)
		print(result)
		self.assertIsNotNone(result)

	def test_get_invoices_by_commitment(self):
		"""
		2. get_invoices_by_commitment(self, planning_item_id: str, commitment_id: str, **kwargs) -> requests.Response
		"""
		planning_item_id = "0"
		commitment_id = "0"
		result = self.invoices.get_invoices_by_commitment(planning_item_id=planning_item_id, commitment_id=commitment_id)
		print(result)
		self.assertIsNotNone(result)

	def test_get_invoice(self):
		"""
		3. get_invoice(self, planning_item_id: str, invoice_id: str) -> requests.Response
		"""
		planning_item_id = "0"
		invoice_id = "0"
		result = self.invoices.get_invoice(planning_item_id=planning_item_id, invoice_id=invoice_id)
		print(result)
		self.assertIsNotNone(result)

	def test_get_invoice_by_commitment_invoice(self):
		"""
		4. get_invoice_by_commitment_invoice(self, planning_item_id: str, commitment_id: str, invoice_id: str) -> requests.Response
		"""
		planning_item_id = "0"
		commitment_id = "0"
		invoice_id = "0"
		result = self.invoices.get_invoice_by_commitment_invoice(planning_item_id=planning_item_id, commitment_id=commitment_id, invoice_id=invoice_id)
		print(result)
		self.assertIsNotNone(result)

	def test_create_invoice(self):
		"""
		5. create_invoice(self, planning_item_id: str, payload: dict) -> requests.Response
		"""
		planning_item_id = "0"
		payload = {
			"id": "1234",
			"name": "Invoice001",
			"description": "string",
			"amount": 200,
			"vendorAmount": {
				"units": "string",
				"value": 0
			},
			"number": "Invoice001",
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
			"state": "new",
			"localizedState": "string",
			"invoiceCreatedDate": "2019-08-24T14:15:22Z",
			"createdBy": "string",
			"creationTimeStamp": "2019-08-24T14:15:22Z",
			"modifiedBy": "string",
			"modifiedTimeStamp": "2019-08-24T14:15:22Z",
			"lineItems": [
				{
					"id": "string",
					"name": "string",
					"description": "string",
					"number": 0,
					"quantity": 0,
					"rate": 0,
					"vendorAmount": {
						"units": "string",
						"value": 0
					},
					"amount": {
						"units": "string",
						"value": 0
					},
					"createdBy": "string",
					"creationTimeStamp": "2019-08-24T14:15:22Z",
					"modifiedBy": "string",
					"modifiedTimeStamp": "2019-08-24T14:15:22Z"
				}
			],
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
		result = self.invoices.create_invoice(planning_item_id=planning_item_id, payload=payload)
		print(result)
		self.assertIsNotNone(result)

	def test_create_invoice_under_commitment(self):
		"""
		6. create_invoice_under_commitment(self, planning_item_id: str, commitment_id: str, payload: dict) -> requests.Response
		"""
		planning_item_id = "0"
		commitment_id = "0"
		payload = {
			"id": "1234",
			"name": "Invoice001",
			"description": "string",
			"amount": 200,
			"vendorAmount": {
				"units": "string",
				"value": 0
			},
			"number": "Invoice001",
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
			"state": "new",
			"localizedState": "string",
			"invoiceCreatedDate": "2019-08-24T14:15:22Z",
			"createdBy": "string",
			"creationTimeStamp": "2019-08-24T14:15:22Z",
			"modifiedBy": "string",
			"modifiedTimeStamp": "2019-08-24T14:15:22Z",
			"lineItems": [
				{
					"id": "string",
					"name": "string",
					"description": "string",
					"number": 0,
					"quantity": 0,
					"rate": 0,
					"vendorAmount": {
						"units": "string",
						"value": 0
					},
					"amount": {
						"units": "string",
						"value": 0
					},
					"createdBy": "string",
					"creationTimeStamp": "2019-08-24T14:15:22Z",
					"modifiedBy": "string",
					"modifiedTimeStamp": "2019-08-24T14:15:22Z"
				}
			],
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
		result = self.invoices.create_invoice_under_commitment(planning_item_id=planning_item_id, commitment_id=commitment_id, payload=payload)
		print(result)
		self.assertIsNotNone(result)

	def test_move_invoice(self):
		"""
		7. move_invoice(self, planning_item_id: str, payload: dict) -> requests.Response
		"""
		planning_item_id = "0"
		payload = {
			"version": 0,
			"template": "http://example.com",
			"type": "id",
			"resources": [
				"string"
			],
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
		result = self.invoices.move_invoice(planning_item_id=planning_item_id, payload=payload)
		print(result)
		self.assertIsNotNone(result)

	def test_move_invoice_by_commitment(self):
		"""
		8. move_invoice_by_commitment(self, planning_item_id: str, commitment_id: str, payload: dict) -> requests.Response
		"""
		planning_item_id = "0"
		commitment_id = "0"
		payload = {
			"name": "string",
			"start": 0,
			"limit": 20,
			"count": 250,
			"accept": "application/json",
			"links": [
				{
					"method": "GET",
					"rel": "self",
					"href": "https://extapigwservice-<server>/<endpoint>/",
					"uri": "/<endpoint>",
					"type": "application/vnd.sas.collection"
				}
			],
			"version": 2,
			"items": [
				{
					"id": "string",
					"name": "string",
					"amount": 0,
					"number": "string",
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
					"state": "new",
					"localizedState": "string",
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
			]
		}
		result = self.invoices.move_invoice_by_commitment(planning_item_id=planning_item_id, commitment_id=commitment_id, payload=payload)
		print(result)
		self.assertIsNotNone(result)

	def test_update_invoice(self):
		"""
		9. update_invoice(self, planning_item_id: str, invoice_id: str, payload: dict) -> requests.Response
		"""
		planning_item_id = "0"
		invoice_id = "0"
		payload = {
			"id": "1234",
			"name": "Invoice001",
			"description": "string",
			"amount": 200,
			"vendorAmount": {
				"units": "string",
				"value": 0
			},
			"number": "Invoice001",
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
			"state": "new",
			"localizedState": "string",
			"invoiceCreatedDate": "2019-08-24T14:15:22Z",
			"createdBy": "string",
			"creationTimeStamp": "2019-08-24T14:15:22Z",
			"modifiedBy": "string",
			"modifiedTimeStamp": "2019-08-24T14:15:22Z",
			"lineItems": [
				{
					"id": "string",
					"name": "string",
					"description": "string",
					"number": 0,
					"quantity": 0,
					"rate": 0,
					"vendorAmount": {
						"units": "string",
						"value": 0
					},
					"amount": {
						"units": "string",
						"value": 0
					},
					"createdBy": "string",
					"creationTimeStamp": "2019-08-24T14:15:22Z",
					"modifiedBy": "string",
					"modifiedTimeStamp": "2019-08-24T14:15:22Z"
				}
			],
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
		result = self.invoices.update_invoice(planning_item_id=planning_item_id, invoice_id=invoice_id, payload=payload)
		print(result)
		self.assertIsNotNone(result)

	def test_update_invoice_under_commitment(self):
		"""
		10. update_invoice_under_commitment(self, planning_item_id: str, commitment_id: str, invoice_id: str, payload: dict) -> requests.Response
		"""
		planning_item_id = "0"
		commitment_id = "0"
		invoice_id = "0"
		payload = {
			"id": "1234",
			"name": "Invoice001",
			"description": "string",
			"amount": 200,
			"vendorAmount": {
				"units": "string",
				"value": 0
			},
			"number": "Invoice001",
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
			"state": "new",
			"localizedState": "string",
			"invoiceCreatedDate": "2019-08-24T14:15:22Z",
			"createdBy": "string",
			"creationTimeStamp": "2019-08-24T14:15:22Z",
			"modifiedBy": "string",
			"modifiedTimeStamp": "2019-08-24T14:15:22Z",
			"lineItems": [
				{
					"id": "string",
					"name": "string",
					"description": "string",
					"number": 0,
					"quantity": 0,
					"rate": 0,
					"vendorAmount": {
						"units": "string",
						"value": 0
					},
					"amount": {
						"units": "string",
						"value": 0
					},
					"createdBy": "string",
					"creationTimeStamp": "2019-08-24T14:15:22Z",
					"modifiedBy": "string",
					"modifiedTimeStamp": "2019-08-24T14:15:22Z"
				}
			],
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
		result = self.invoices.update_invoice_under_commitment(
			planning_item_id=planning_item_id,
			commitment_id=commitment_id,
			invoice_id=invoice_id,
			payload=payload
		)
		print(result)
		self.assertIsNotNone(result)

	def test_delete_invoice_by_commitment(self):
		"""
		11. delete_invoice_by_commitment(self, planning_item_id: str, commitment_id: str, invoice_id: str) -> requests.Response
		"""
		planning_item_id = "0"
		commitment_id = "0"
		invoice_id = "0"
		result = self.invoices.delete_invoice_by_commitment(
			planning_item_id=planning_item_id,
			commitment_id=commitment_id,
			invoice_id=invoice_id
		)
		print(result)
		self.assertIsNotNone(result)

	def test_delete_invoice(self):
		"""
		12. delete_invoice(self, planning_item_id: str, invoice_id: str) -> requests.Response
		"""
		planning_item_id = "0"
		invoice_id = "0"
		result = self.invoices.delete_invoice(
			planning_item_id=planning_item_id,
			invoice_id=invoice_id
		)
		print(result)
		self.assertIsNotNone(result)

	def test_reconcile_invoice(self):
		"""
		13. reconcile_invoice(self, planning_item_id: str, invoice_id: str, payload: dict) -> requests.Response
		"""
		planning_item_id = "0"
		invoice_id = "0"
		payload = {
			"id": "string",
			"name": "string",
			"description": "string",
			"amount": 0,
			"vendorAmount": 0,
			"reconcileAmount": 0,
			"number": "string",
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
			"state": "string",
			"localizedState": "string",
			"invoiceCreatedDate": "2019-08-24T14:15:22Z",
			"createdBy": "string",
			"creationTimeStamp": "2019-08-24T14:15:22Z",
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
		}
		result = self.invoices.reconcile_invoice(
			planning_item_id=planning_item_id,
			invoice_id=invoice_id,
			payload=payload
		)
		print(result)
		self.assertIsNotNone(result)

	def test_reconcile_invoice_by_commitment(self):
		"""
		14. reconcile_invoice_by_commitment(self, planning_item_id: str, commitment_id: str, invoice_id: str, payload: dict) -> requests.Response
		"""
		planning_item_id = "0"
		commitment_id = "0"
		invoice_id = "0"
		payload = {
			"id": "string",
			"name": "string",
			"description": "string",
			"amount": 0,
			"vendorAmount": 0,
			"reconcileAmount": 0,
			"number": "string",
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
			"state": "string",
			"localizedState": "string",
			"invoiceCreatedDate": "2019-08-24T14:15:22Z",
			"createdBy": "string",
			"creationTimeStamp": "2019-08-24T14:15:22Z",
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
		}
		result = self.invoices.reconcile_invoice_by_commitment(
			planning_item_id=planning_item_id,
			commitment_id=commitment_id,
			invoice_id=invoice_id,
			payload=payload
		)
		print(result)
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
