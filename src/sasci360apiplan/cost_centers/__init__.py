#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apiplan.base import Base


class CostCenters(Base):
	"""
	Cost Centers
	Contains the operations for cost center collections.
		1. get_cost_centers(self, **kwargs) -> requests.Response
		2. get_cost_center(self, cost_center_id: str) -> requests.Response
		3. create_cost_center(self, payload: dict) -> requests.Response
		4. update_cost_center(self, cost_center_id: str, payload: dict) -> requests.Response
		5. delete_cost_center(self, cost_center_id: str) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_cost_centers(self, **kwargs) -> requests.Response:
		"""
		Get a collection of cost centers
		:keyword filter: str, optional - The advance filter string used to filter cost centers. Cost centers are returned only if they match the filter exactly
		:keyword start: int, optional - The index of the first cost center to return
		:keyword limit: int, optional - The maximum number of cost centers to return
		:return: Returns a collection of cost centers based on options for pagination, filtering, and sorting. The items in the collection use the application/vnd.sas.marketing.cost.center media type.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			query_string = "?"
			if "filter" in kwargs:
				query_string.join("filter={0}&".format(kwargs["filter"]))
			if "start" in kwargs:
				query_string.join("start={0}&".format(kwargs["start"]))
			if "limit" in kwargs:
				query_string.join("limit={0}&".format(kwargs["limit"]))
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/costCenters{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_cost_center(self, cost_center_id: str) -> requests.Response:
		"""
		Get a cost center
		:param cost_center_id: str, required - The unique identifier for the cost center
		:return: Returns the representation of the specified cost center.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if cost_center_id is None:
			raise Exception("Cost Center ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/costCenters/{0}".format(cost_center_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_cost_center(self, payload: dict) -> requests.Response:
		"""
		Create a new cost center
		:param payload: required
		:return: Creates a new cost center based on the representation in the request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			action = "POST"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/costCenters"
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def update_cost_center(self, cost_center_id: str, payload: dict) -> requests.Response:
		"""
		Update a cost center
		:param cost_center_id: required - The unique identifier for the cost center
		:param payload: required
		:return: Updates the specified cost center based on the representation in the request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if cost_center_id is None:
			raise Exception("Cost Center ID is missing.")
		try:
			action = "PUT"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/costCenters/{0}".format(cost_center_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def delete_cost_center(self, cost_center_id: str) -> requests.Response:
		"""
		Delete a cost center
		:param cost_center_id: required - The unique identifier for the cost center
		:return: Deletes the specified cost center.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if cost_center_id is None:
			raise Exception("Cost Center ID is missing.")
		try:
			action = "DELETE"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/costCenters/{0}".format(cost_center_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	CostCenters()
