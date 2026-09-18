#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apiplan.base import Base


class HierarchyDefinitions(Base):
	"""
	Hierarchy Definitions
	Contains the operations for hierarchy definition collections.
		1. get_hierarchy_definitions(self, **kwargs) -> requests.Response
		2. get_hierarchy_definition(self, hierarchy_definition_id: str) -> requests.Response
		3. create_hierarchy_definition(self, payload: dict) -> requests.Response
		4. update_hierarchy_definition(self, hierarchy_definition_id: str, payload: dict) -> requests.Response
		5. delete_hierarchy_definition(self, hierarchy_definition_id: str) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_hierarchy_definitions(self, **kwargs) -> requests.Response:
		"""
		Get a collection of hierarchy definitions
		:keyword start: int, optional - The index of the first hierarchy definition to return
		:keyword limit: int, optional - The maximum number of hierarchy definitions to return
		:keyword type: str, optional - The type value to filter hierarchy definitions on
		:keyword sub_type: str, optional - The subType value to filter hierarchy definitions on
		:return: Returns a collection of hierarchy definitions based on options for pagination, filtering, and sorting. The items in the collection use the application/vnd.sas.marketing.hierarchy.definition.summary media type.
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
			if "type" in kwargs:
				query_string.join("parent={0}&".format(kwargs["parent"]))
			if "sub_type" in kwargs:
				query_string.join("subType={0}&".format(kwargs["sub_type"]))
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/hierarchyDefinitions{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_hierarchy_definition(self, hierarchy_definition_id: str) -> requests.Response:
		"""
		Get a hierarchy definition
		:param hierarchy_definition_id: required - The unique identifier for the hierarchy definition
		:return: Returns the representation of the specified hierarchy definition.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if hierarchy_definition_id is None:
			raise Exception("Hierarchy Definition ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/hierarchycomponents/schemas/{0}".format(hierarchy_definition_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_hierarchy_definition(self, payload: dict) -> requests.Response:
		"""
		Create a new hierarchy definition
		:param payload: required
		:return: Creates a new hierarchy definition based on the representation in the request body.
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
			api_path = "/hierarchyDefinitions"
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def update_hierarchy_definition(self, hierarchy_definition_id: str, payload: dict) -> requests.Response:
		"""
		Update a hierarchy definition
		:param hierarchy_definition_id: required - The unique identifier for the hierarchy definition
		:param payload: required
		:return: Updates the specified hierarchy definition based on the representation in the request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if hierarchy_definition_id is None:
			raise Exception("Hierarchy Definition ID is missing.")
		try:
			action = "PUT"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/hierarchycomponents/schemas/{0}".format(hierarchy_definition_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def delete_hierarchy_definition(self, hierarchy_definition_id: str) -> requests.Response:
		"""
		Delete a hierarchy definition
		:param hierarchy_definition_id: required - The unique identifier for the hierarchy definition
		:return: Deletes the specified hierarchy definition.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if hierarchy_definition_id is None:
			raise Exception("Hierarchy Definition ID is missing.")
		try:
			action = "DELETE"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/hierarchycomponents/schemas/{0}".format(hierarchy_definition_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	HierarchyDefinitions()
