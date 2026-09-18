#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apiplan.base import Base


class Vendors(Base):
	"""
	Vendors
	Contains the operations for a vendor resource.
		1. get_vendors(self, **kwargs) -> requests.Response
		2. get_vendor(self, vendor_id: str) -> requests.Response
		3. create_vendor(self, payload: dict) -> requests.Response
		4. update_vendor(self, vendor_id: str, payload: dict) -> requests.Response
		5. delete_vendor(self, vendor_id: str) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_vendors(self, **kwargs) -> requests.Response:
		"""
		Get a collection of vendors
		:keyword name: str, optional - The name of the vendors to return. Vendors are returned only if they match this value exactly
		:keyword start: int, optional - The index of the first vendor to return
		:keyword limit: int, optional - The maximum number of vendors to return
		:return: Returns a collection of vendors based on the options for pagination, filtering, and sorting. The items in the collection use the application/vnd.sas.marketing.vendor.summary media type.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			query_string = "?"
			if "name" in kwargs:
				query_string.join("name={0}&".format(kwargs["name"]))
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
			api_path = "/vendors{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_vendor(self, vendor_id: str) -> requests.Response:
		"""
		Get a vendor
		:param vendor_id: required - The unique identifier for the vendor
		:return: Returns the representation of the specified vendor.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if vendor_id is None:
			raise Exception("Vendor ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/vendors/{0}".format(vendor_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_vendor(self, payload: dict) -> requests.Response:
		"""
		Create a new vendor
		:param payload: required
		:return: Creates a new vendor based on the representation in the request body.
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
			api_path = "/vendors"
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def update_vendor(self, vendor_id: str, payload: dict) -> requests.Response:
		"""
		Update a vendor
		:param vendor_id: required - The unique identifier for the vendor
		:param payload: required
		:return: Updates the specified vendor based on the representation in the request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if vendor_id is None:
			raise Exception("Vendor ID is missing.")
		try:
			action = "PUT"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/vendors/{0}".format(vendor_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def delete_vendor(self, vendor_id: str) -> requests.Response:
		"""
		Delete a vendor
		:param vendor_id: required - The unique identifier for the vendor
		:return: Deletes the specified vendor.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if vendor_id is None:
			raise Exception("Vendor ID is missing.")
		try:
			action = "DELETE"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/vendors/{0}".format(vendor_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	Vendors()
