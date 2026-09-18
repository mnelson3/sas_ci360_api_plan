#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apiplan.base import Base


class Commitments(Base):
	"""
	Commitments
	Contains the operations for commitment collections.
		1. get_commitments(self, planning_item_id: str, **kwargs) -> requests.Response
		2. get_commitment(self, planning_item_id: str, commitment_id: str) -> requests.Response
		3. create_commitment(self, planning_item_id: str, payload: dict) -> requests.Response
		4. update_commitment(self, planning_item_id: str, commitment_id: str, payload: dict) -> requests.Response
		5. delete_commitment(self, planning_item_id: str, commitment_id: str) -> requests.Response
		6. close_commitment(self, planning_item_id: str, commitment_id: str, payload: dict) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_commitments(self, planning_item_id: str, **kwargs) -> requests.Response:
		"""
		Get a collection of commitments
		:param planning_item_id: required - The ID of the planning item under which the commitment is associated
		:keyword start: int, optional - The index of the first commitment to return
		:keyword limit: int, optional - The maximum number of commitments to return
		:return: Returns a collection of commitments based on options for pagination, filtering, and sorting. The items in the collection use the application/vnd.sas.marketing.commitment.summary media type.
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
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/planningItems/{0}/commitments{1}".format(planning_item_id, res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_commitment(self, planning_item_id: str, commitment_id: str) -> requests.Response:
		"""
		Get a commitment
		:param planning_item_id: required - The ID of the planning item under which the commitment is associated
		:param commitment_id: required - The unique identifier for the commitment
		:return: Returns the representation of the specified commitment.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if planning_item_id is None:
			raise Exception("Planning Item ID is missing.")
		if commitment_id is None:
			raise Exception("Commitment ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/planningItems/{0}/commitments/{1}".format(planning_item_id, commitment_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_commitment(self, planning_item_id: str, payload: dict) -> requests.Response:
		"""
		Create a new commitment
		:param planning_item_id: required - The ID of the planning item under which the commitment is associated
		:param payload: required - The representation of a commitment
		:return: Creates a new commitment based on the representation in the request body.
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
			api_path = "/planningItems/{0}/commitments".format(planning_item_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def update_commitment(self, planning_item_id: str, commitment_id: str, payload: dict) -> requests.Response:
		"""
		Update a commitment
		:param planning_item_id: required - The ID of the planning item under which the commitment is associated
		:param commitment_id: required - The unique identifier for the commitment
		:param payload: required
		:return: Updates the specified commitment based on the representation in the request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if planning_item_id is None:
			raise Exception("Planning Item ID is missing.")
		if commitment_id is None:
			raise Exception("Commitment ID is missing.")
		try:
			action = "PUT"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/planningItems/{0}/commitments/{1}".format(planning_item_id, commitment_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def delete_commitment(self, planning_item_id: str, commitment_id: str) -> requests.Response:
		"""
		Delete a commitment
		:param planning_item_id: required - The ID of the planning item under which commitment is associated
		:param commitment_id: required - The unique identifier for the commitment
		:return: Deletes the specified commitment.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if planning_item_id is None:
			raise Exception("Planning Item ID is missing.")
		if commitment_id is None:
			raise Exception("Commitment ID is missing.")
		try:
			action = "DELETE"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/planningItems/{0}/commitments/{1}".format(planning_item_id, commitment_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def close_commitment(self, planning_item_id: str, commitment_id: str, payload: dict) -> requests.Response:
		"""
		Create a new commitment
		:param planning_item_id: required - The ID of the planning item under which the commitment is associated
		:param commitment_id: required - The unique identifier for the commitment
		:param payload: required - The representation of a commitment
		:return: Creates a new commitment based on the representation in the request body.
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
			api_path = "/planningItems/{0}/commitments/{1}".format(planning_item_id, commitment_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	Commitments()
