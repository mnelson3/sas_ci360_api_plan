#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apiplan.base import Base


class BudgetHierarchy(Base):
	"""
	Budget Hierarchy Module
	Contains the operations for a planning hierarchy's budget details
		1. get_budget(self, planning_item_id: str) -> requests.Response
		2. update_budget(self, planning_item_id: str, payload: dict) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_budget(self, planning_item_id: str) -> requests.Response:
		"""
		Get budget details for a planning item's hierarchy
		:param planning_item_id: required - The ID of the planning item under which the commitment is associated
		:return: Returns the representation of the budget hierarchy for a planning item.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if planning_item_id is None:
			raise Exception("Planning Item ID is missing.")
		try:
			method = "GET"
			api_path = "/planningItems/{0}/budgetHierarchy".format(planning_item_id)
			payload = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=method, data=payload, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def update_budget(self, planning_item_id: str, payload: dict) -> requests.Response:
		"""
		Update budget details for a planning item's hierarchy
		:param planning_item_id: required - The ID of the planning item under which the commitment is associated
		:param payload: required
		:return: Updates the budget details of a planning item based on the representation in the request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if planning_item_id is None:
			raise Exception("Planning Item ID is missing.")
		try:
			method = "PUT"
			api_path = "/planningItems/{0}/budgetHierarchy".format(planning_item_id)
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=method, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	BudgetHierarchy()
