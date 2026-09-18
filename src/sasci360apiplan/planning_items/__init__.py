#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apiplan.base import Base


class PlanningItems(Base):
	"""
	Planning Items
	Contains the operations for planning item collections.
		1. get_planning_items(self, **kwargs) -> requests.Response
		2. get_planning_items_tree(self, **kwargs) -> requests.Response
		3. get_planning_item(self, planning_item_id: str) -> requests.Response
		4. create_planning_item(self, payload: dict, **kwargs) -> requests.Response
		5. update_planning_item(self, planning_item_id: str, payload: dict) -> requests.Response
		6. rename_planning_item(self, planning_item_id: str, payload: dict) -> requests.Response
		7. delete_planning_item(self, planning_item_id: str) -> requests.Response
		8. add_planning_item(self, planning_item_id: str, payload: dict) -> requests.Response
		9. get_planning_item_hierarchy(self, planning_item_id: str) -> requests.Response
		10. get_planning_item_children(self, planning_item_id: str, **kwargs) -> requests.Response
		11. create_planning_item_children(self, planning_item_id: str, payload: dict) -> requests.Response
		12. add_planning_item_associations(self, planning_item_id: str, payload: dict) -> requests.Response
		13. remove_planning_item_associations(self, planning_item_id: str, payload: dict) -> requests.Response
		14. get_planning_item_children_tree(self, planning_item_id: str, **kwargs) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_planning_items(self, **kwargs) -> requests.Response:
		"""
		Get a collection of planning items
		:keyword start: int, optional - The index of the first planning item to return
		:keyword limit: int, optional - The maximum number of planning items to return
		:keyword filter: str, optional - The criteria for filtering the planning items
		:return: Returns a collection of planning items based on options for pagination, filtering, and sorting. The items in the collection use the application/vnd.sas.marketing.planning.item.summary media type.
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
			if "filter" in kwargs:
				query_string.join("parent={0}&".format(kwargs["parent"]))
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/planningItems{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_planning_items_tree(self, **kwargs) -> requests.Response:
		"""
		Get a collection of planning item hierarchies
		:keyword start: int, optional - The index of the first planning item to return
		:keyword limit: int, optional - The maximum number of planning items to return
		:keyword filter: str, optional - The criteria for filtering the planning items
		:return: Returns a collection of planning items based on options for pagination, filtering, and sorting. The items in the collection use the application/vnd.sas.marketing.planning.item.summary media type.
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
			if "filter" in kwargs:
				query_string.join("parent={0}&".format(kwargs["parent"]))
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/planningItems#tree{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_planning_item(self, planning_item_id: str) -> requests.Response:
		"""
		Get a planning item
		:param planning_item_id: required - The unique identifier for the planning item
		:return: Returns the representation of the specified planning item.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if planning_item_id is None:
			raise Exception("Planning Item ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/planningItems/{0}".format(planning_item_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_planning_item(self, payload: dict, **kwargs) -> requests.Response:
		"""
		Create a new planning item
		:param payload: required
		:keyword action: str, optional - An optional action to take when the planning item is created. This parameter can have two values: copy - creates a copy of the planning item with the specified ID. You can specify a new name for the item. saveAs - copies the planning item with the specified ID and saves it as a new item
		:keyword copy_of: str, optional - The ID of the planning item to copy
		:keyword copy_parent: bool, optional - Specifies if parent information should be copied when the planning item is copied
		:return: Creates a new planning item based on the representation in the request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			query_string = "?"
			if "action" in kwargs:
				query_string.join("action={0}&".format(kwargs["action"]))
			if "copy_of" in kwargs:
				query_string.join("copyOf={0}&".format(kwargs["copy_of"]))
			if "copy_parent" in kwargs:
				query_string.join("copyParent={0}&".format(kwargs["copy_parent"]))
			action = "POST"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/planningItems{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def update_planning_item(self, planning_item_id: str, payload: dict) -> requests.Response:
		"""
		Update a planning item
		:param planning_item_id: required - The unique identifier for the planning item
		:param payload: required
		:return: Updates the specified planning item based on the representation in the request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if planning_item_id is None:
			raise Exception("Planning Item ID is missing.")
		try:
			action = "PUT"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/planningItems/{0}".format(planning_item_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def rename_planning_item(self, planning_item_id: str, payload: dict) -> requests.Response:
		"""
		Rename a planning item
		:param planning_item_id: required - The unique identifier for the planning item
		:param payload: required
		:return: Renames the specified planning item based on the representation in the request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if planning_item_id is None:
			raise Exception("Planning Item ID is missing.")
		try:
			action = "PATCH"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/planningItems/{0}".format(planning_item_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def delete_planning_item(self, planning_item_id: str) -> requests.Response:
		"""
		Delete a planning item
		:param planning_item_id: required - The unique identifier for the planning item
		:return: Deletes the specified planning item.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if planning_item_id is None:
			raise Exception("Planning Item ID is missing.")
		try:
			action = "DELETE"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/planningItems/{0}".format(planning_item_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def add_planning_item(self, planning_item_id: str, payload: dict) -> requests.Response:
		"""
		Add planning item
		:param planning_item_id: required - The unique identifier for the planning item
		:param payload: required
		:return: Adds the specified planning item based on the representation in the request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if planning_item_id is None:
			raise Exception("Planning Item ID is missing.")
		try:
			action = "POST"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/planningItems/{0}".format(planning_item_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_planning_item_hierarchy(self, planning_item_id: str) -> requests.Response:
		"""
		Get hierarchy information for a planning item
		:param planning_item_id: required - The unique identifier for the planning item
		:return: Returns the hierarchy for a planning item. By traversing the 'parent' attribute (and nested 'parent' attributes) in the response, you can determine the path of a planning item.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if planning_item_id is None:
			raise Exception("Planning Item ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/planningItems/{0}#hierarchyInfo".format(planning_item_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_planning_item_children(self, planning_item_id: str, **kwargs) -> requests.Response:
		"""
		Get a collection of a planning item's children
		param planning_item_id: required - The unique identifier for the planning item
		:keyword start: int, optional - The index of the first planning item to return
		:keyword limit: int, optional - The maximum number of planning items to return
		:keyword filter: str, optional - The criteria for filtering the planning items
		:return: Returns a collection of all children under a specified planning item based on options for pagination, filtering, and sorting. The items in the collection use the application/vnd.sas.marketing.planning.item.summary media type.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if planning_item_id is None:
			raise Exception("Planning Item ID is missing.")
		try:
			query_string = "?"
			if "start" in kwargs:
				query_string.join("start={0}&".format(kwargs["start"]))
			if "limit" in kwargs:
				query_string.join("limit={0}&".format(kwargs["limit"]))
			if "filter" in kwargs:
				query_string.join("parent={0}&".format(kwargs["parent"]))
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/planningItems/{0}/children{1}".format(planning_item_id, res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_planning_item_children(self, planning_item_id: str, payload: dict) -> requests.Response:
		"""
		Create a new planning item
		:param planning_item_id: required - The unique identifier for the planning item
		:param payload: required
		:return: Creates a new child planning item based on the representation in the request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if planning_item_id is None:
			raise Exception("Planning Item ID is missing.")
		try:
			action = "POST"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/planningItems/{0}/children".format(planning_item_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def add_planning_item_associations(self, planning_item_id: str, payload: dict) -> requests.Response:
		"""
		Add associations to a planning item
		:param planning_item_id: required - The unique identifier for the planning item
		:param payload: required
		:return: Builds a hierarchy from orphan planning items, activities, and tasks. A planning item can be associated with one or more instances of a task, activity, or other planning item.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if planning_item_id is None:
			raise Exception("Planning Item ID is missing.")
		try:
			action = "POST"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/planningItems/{0}/children/associations".format(planning_item_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def remove_planning_item_associations(self, planning_item_id: str, payload: dict) -> requests.Response:
		"""
		Remove associations to a planning item
		:param planning_item_id: required - The unique identifier for the planning item
		:param payload: required
		:return: Removes associations from a planning item's hierarchy. Dissociated instances become orphans and can be used for subsequent associations. A planning item can be associated with one or more instances of tasks, activities, or other planning items.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if planning_item_id is None:
			raise Exception("Planning Item ID is missing.")
		try:
			action = "POST"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/planningItems/{0}/children/dissociations".format(planning_item_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_planning_item_children_tree(self, planning_item_id: str, **kwargs) -> requests.Response:
		"""
		Get a tree of a planning item's children
		:param planning_item_id: required - The unique identifier for the planning item
		:keyword start: int, optional - The index of the first planning item to return
		:keyword limit: int, optional - The maximum number of planning items to return
		:keyword filter: str, optional - The criteria for filtering the planning items
		:return: Returns a tree representation of a planning item's children based on options for pagination, filtering, and sorting. The items in the collection use the application/vnd.sas.marketing.planning.item.summary.hierarchy media type.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if planning_item_id is None:
			raise Exception("Planning Item ID is missing.")
		try:
			query_string = "?"
			if "start" in kwargs:
				query_string.join("start={0}&".format(kwargs["start"]))
			if "limit" in kwargs:
				query_string.join("limit={0}&".format(kwargs["limit"]))
			if "filter" in kwargs:
				query_string.join("parent={0}&".format(kwargs["parent"]))
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/planningItems/{0}/children#tree{1}".format(planning_item_id, res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	PlanningItems()
