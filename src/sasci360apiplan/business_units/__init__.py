#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apiplan.base import Base


class BusinessUnits(Base):
	"""
	Business Units
	Contains the operations for business unit collections.
		1. get_business_units(self, **kwargs) -> requests.Response
		2. get_business_unit(self, business_unit_id: str) -> requests.Response
		3. create_business_unit(self, payload: dict) -> requests.Response
		4. update_business_unit(self, business_unit_id: str, payload: dict) -> requests.Response
		5. delete_business_unit(self, business_unit_id: str) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_business_units(self, **kwargs) -> requests.Response:
		"""
		Get a collection of business units
		:keyword parent: str, optional - The parent value to filter business units. Business units are returned only if they match exactly
		:keyword obsolete: bool, optional - The obsolete flag to filter businessUnits. Business units are returned only if they match exactly
		:keyword start: int, optional - The index of the first business unit to return
		:keyword limit: int, optional - The maximum number of business units to return
		:return: Returns a collection of business units based on options for pagination, filtering, and sorting. The items in the collection use the application/vnd.sas.marketing.business.unit.summary media type.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			query_string = "?"
			if "parent" in kwargs:
				query_string.join("parent={0}&".format(kwargs["parent"]))
			if "obsolete" in kwargs:
				query_string.join("obsolete={0}&".format(kwargs["obsolete"]))
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
			api_path = "/businessUnits{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_business_unit(self, business_unit_id: str) -> requests.Response:
		"""
		Get a business unit
		:param business_unit_id: required - The unique identifier for the business unit
		:return: Returns the representation of the specified business unit.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if business_unit_id is None:
			raise Exception("Business Unit ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/businessUnits/{0}".format(business_unit_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_business_unit(self, payload: dict) -> requests.Response:
		"""
		Create a new business unit
		:param payload: required
		:return: Creates a new business unit based on the representation in the request body.
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
			api_path = "/businessUnits"
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(self, action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def update_business_unit(self, business_unit_id: str, payload: dict) -> requests.Response:
		"""
		Update a business unit
		:param business_unit_id: required - The unique identifier for the business unit
		:param payload: required
		:return: Updates a business unit based on the value provided in request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if business_unit_id is None:
			raise Exception("Business Unit ID is missing.")
		try:
			action = "PATCH"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/businessUnits/{0}".format(business_unit_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def delete_business_unit(self, business_unit_id: str) -> requests.Response:
		"""
		Delete a business unit
		:param business_unit_id: required - The unique identifier for the business unit
		:return: Deletes the specified business unit.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if business_unit_id is None:
			raise Exception("Business Unit ID is missing.")
		try:
			action = "DELETE"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/businessUnits/{0}".format(business_unit_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	BusinessUnits()
