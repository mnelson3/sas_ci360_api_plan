#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Settings
Contains the operations for setting collections.
	1. get_settings(self, **kwargs) -> requests.Response
	2. get_setting(self, setting_id: str) -> requests.Response
	3. create_setting(self, payload: dict) -> requests.Response
	4. update_setting(self, setting_id: str, payload: dict) -> requests.Response
"""

import os
import unittest
from sasci360apiplan import settings


class TestSettings(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = os.environ.get("CI360_ALGORITHM", "HS256")
		api = os.environ.get("CI360_API", "/marketingPlan")
		encoding = os.environ.get("CI360_ENCODING", "UTF-8")
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.settings = settings.Settings(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_settings(self):
		"""
		1. get_settings(self, **kwargs) -> requests.Response
		"""
		result = self.settings.get_settings()
		print(result)
		self.assertIsNotNone(result)

	def test_get_setting(self):
		"""
		2. get_setting(self, setting_id: str) -> requests.Response
		"""
		setting_id = "0"
		result = self.settings.get_setting(setting_id=setting_id)
		print(result)
		self.assertIsNotNone(result)

	def test_create_setting(self):
		"""
		3. create_setting(self, payload: dict) -> requests.Response
		"""
		payload = {
			"id": "string",
			"enableMessages": True,
			"enableBusinessUnit": True,
			"enablePlanningForActivitiesTasks": True,
			"enableCostCenters": True,
			"allowOverbudgetingForReservedAmount": True,
			"category": "string",
			"tenantCurrencies": [
				{
					"obsolete": True,
					"defaultSelection": True,
					"currencyCode": "string",
					"description": "string",
					"usageCount": 0,
					"validForTenant": True
				}
			],
			"financialPeriodStartMonth": "january",
			"financialPeriodInterval": 0,
			"financialPeriodEndMonth": "january",
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
		result = self.settings.create_setting(payload=payload)
		print(result)
		self.assertIsNotNone(result)

	def test_update_setting(self):
		"""
		4. update_setting(self, setting_id: str, payload: dict) -> requests.Response
		"""
		setting_id = "0"
		payload = {
			"operations": [
				{
					"op": "add",
					"path": "string",
					"value": {},
					"from": "string"
				}
			]
		}
		result = self.settings.update_setting(setting_id=setting_id, payload=payload)
		print(result)
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
