#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apiplan.base import Base


class Settings(Base):
	"""
	Settings
	Contains the operations for setting collections.
		1. get_settings(self, **kwargs) -> requests.Response
		2. get_setting(self, setting_id: str) -> requests.Response
		3. create_setting(self, payload: dict) -> requests.Response
		4. update_setting(self, setting_id: str, payload: dict) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_settings(self, **kwargs) -> requests.Response:
		"""
		Get a collection of settings
		:keyword start: int, optional - The index of the first setting to return
		:keyword limit: int, optional - The maximum number of settings to return
		:keyword category: str, optional - The category of the settings to filter the data on. Settings are returned only if they match this value exactly
		:return: Retrieve a list of settings based on options for start, limit, and category. The items in the collection use the application/vnd.sas.marketing.planner.setting.summary media type.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			query_string = "?"
			if "start" in kwargs:
				query_string.join("start={0}&".format(kwargs["start"]))
			if "limit" in kwargs:
				query_string.join("limit={0}&".format(kwargs["limit"]))
			if "category" in kwargs:
				query_string.join("category={0}&".format(kwargs["category"]))
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/settings{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_setting(self, setting_id: str) -> requests.Response:
		"""
		Get a setting
		:param setting_id: required - The unique identifier for the setting
		:return: Returns the representation of the specified setting.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if setting_id is None:
			raise Exception("Setting ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/settings/{0}".format(setting_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_setting(self, payload: dict) -> requests.Response:
		"""
		Create a new setting
		:param payload: required
		:return: Creates a new setting based on the representation in the request body.
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
			api_path = "/settings"
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def update_setting(self, setting_id: str, payload: dict) -> requests.Response:
		"""
		Update a setting
		:param setting_id: required - The unique identifier for the setting
		:param payload: required
		:return: Updates the setting based on the value provided in request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if setting_id is None:
			raise Exception("Setting ID is missing.")
		try:
			action = "PATCH"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/settings/{0}".format(setting_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	Settings()
