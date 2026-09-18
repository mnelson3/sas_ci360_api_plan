#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Financial Accounts
Contains the operations for financial accounts.
	1. get_financial_accounts(self, **kwargs) -> requests.Response
	2. get_financial_account(self, financial_account_id: str) -> requests.Response
	3. create_financial_account(self, payload: dict) -> requests.Response
	4. update_financial_account(self, financial_account_id: str, payload: dict) -> requests.Response
	5. delete_financial_account(self, financial_account_id: str) -> requests.Response
"""

import os
import unittest
from sasci360apiplan import financial_accounts


class TestFinancialAccounts(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = os.environ.get("CI360_ALGORITHM", "HS256")
		api = os.environ.get("CI360_API", "/marketingPlan")
		encoding = os.environ.get("CI360_ENCODING", "UTF-8")
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.financial_accounts = financial_accounts.FinancialAccounts(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_financial_accounts(self):
		"""
		1. get_financial_accounts(self, **kwargs) -> requests.Response
		"""
		result = self.financial_accounts.get_financial_accounts()
		print(result)
		self.assertIsNotNone(result)

	def test_get_financial_account(self):
		"""
		2. get_financial_account(self, financial_account_id: str) -> requests.Response
		"""
		financial_account_id = "0"
		result = self.financial_accounts.get_financial_account(financial_account_id=financial_account_id)
		print(result)
		self.assertIsNotNone(result)

	def test_create_financial_account(self):
		"""
		3. create_financial_account(self, payload: dict) -> requests.Response
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
		result = self.financial_accounts.create_financial_account(payload=payload)
		print(result)
		self.assertIsNotNone(result)

	def test_update_financial_account(self):
		"""
		4. update_financial_account(self, financial_account_id: str, payload: dict) -> requests.Response
		"""
		financial_account_id = "0"
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
		result = self.financial_accounts.update_financial_account(financial_account_id=financial_account_id, payload=payload)
		print(result)
		self.assertIsNotNone(result)

	def test_delete_financial_account(self):
		"""
		5. delete_financial_account(self, financial_account_id: str) -> requests.Response
		"""
		financial_account_id = "0"
		result = self.financial_accounts.delete_financial_account(financial_account_id=financial_account_id)
		print(result)
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
