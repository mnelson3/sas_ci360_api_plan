#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apiplan.base import Base


class Invoices(Base):
	"""
	Invoices
	Contains the operations for invoice collections.
		1. get_invoices_by_planning_item(self, planning_item_id: str, **kwargs) -> requests.Response
		2. get_invoices_by_commitment(self, planning_item_id: str, commitment_id: str, **kwargs) -> requests.Response
		3. get_invoice(self, planning_item_id: str, invoice_id: str) -> requests.Response
		4. get_invoice_by_commitment_invoice(self, planning_item_id: str, commitment_id: str, invoice_id: str) -> requests.Response
		5. create_invoice(self, planning_item_id: str, payload: dict) -> requests.Response
		6. create_invoice_under_commitment(self, planning_item_id: str, commitment_id: str, payload: dict) -> requests.Response
		7. move_invoice(self, planning_item_id: str, payload: dict) -> requests.Response
		8. move_invoice_by_commitment(self, planning_item_id: str, commitment_id: str, payload: dict) -> requests.Response
		9. update_invoice(self, planning_item_id: str, invoice_id: str, payload: dict) -> requests.Response
		10 update_invoice_under_commitment(self, planning_item_id: str, commitment_id: str, invoice_id: str, payload: dict) -> requests.Response
		11. delete_invoice_by_commitment(self, planning_item_id: str, commitment_id: str, invoice_id: str) -> requests.Response
		12. delete_invoice(self, planning_item_id: str, invoice_id: str) -> requests.Response
		13. reconcile_invoice(self, planning_item_id: str, invoice_id: str, payload: dict) -> requests.Response
		14 reconcile_invoice_by_commitment(self, planning_item_id: str, commitment_id: str, invoice_id: str, payload: dict) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_invoices_by_planning_item(self, planning_item_id: str, **kwargs) -> requests.Response:
		"""
		Get a collection of invoices under a planning item
		:param planning_item_id: required - The ID of the planning item to fetch the invoices for
		:keyword vendor_number: str, optional - The vendor number to filter the invoices on. Invoices are only returned if they match this value exactly
		:keyword start: int, optional - The index of the first invoice to return
		:keyword limit: int, optional - The maximum number of invoices to return
		:return: Returns a collection of invoices based on the options for pagination, filtering, and sorting. The items in the collection use the application/vnd.sas.marketing.invoice.summary media type.
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
			if "vendor_number" in kwargs:
				query_string.join("vendorNumber={0}&".format(kwargs["vendor_number"]))
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
			api_path = "/planningItems/{0}/invoices{1}".format(planning_item_id, res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_invoices_by_commitment(self, planning_item_id: str, commitment_id: str, **kwargs) -> requests.Response:
		"""
		Get a collection of invoices under a commitment
		:param planning_item_id: required - The ID of the planning item under which the commitment is associated
		:param commitment_id: required - The ID of the commitment under which the invoices are associated
		:keyword vendor_number: str, optional - The vendor number to filter the invoices on. Invoices are only returned if they match this value exactly
		:keyword start: int, optional - The index of the first invoice to return
		:keyword limit: int, optional - The maximum number of invoices to return
		:return: Returns a collection of invoices based on options for pagination, filtering, and sorting. The items in the collection use the application/vnd.sas.marketing.invoice.summary media type.
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
			query_string = "?"
			if "vendor_number" in kwargs:
				query_string.join("vendorNumber={0}&".format(kwargs["vendor_number"]))
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
			api_path = "/planningItems/{0}/commitments/{1}/invoices{2}".format(planning_item_id, commitment_id, res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_invoice(self, planning_item_id: str, invoice_id: str) -> requests.Response:
		"""
		Get an invoice
		:param planning_item_id: required - The ID of the planning item to which the invoices are associated
		:param invoice_id: required - The unique identifier for the invoice
		:return: Returns the representation of the specified invoice.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if planning_item_id is None:
			raise Exception("Planning Item ID is missing.")
		if invoice_id is None:
			raise Exception("Invoice ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/planningItems/{0}/invoices/{1}".format(planning_item_id, invoice_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_invoice_by_commitment_invoice(self, planning_item_id: str, commitment_id: str, invoice_id: str) -> requests.Response:
		"""
		Get an invoice
		:param planning_item_id: required - The ID of the planning item under which the commitment is associated
		:param commitment_id: required - The ID of the commitment under which invoices are associated
		:param invoice_id: required - The unique identifier for the invoice
		:return: Returns the representation of the specified invoice.
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
		if invoice_id is None:
			raise Exception("Invoice ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/planningItems/{0}/commitments/{1}/invoices/{2}".format(planning_item_id, commitment_id, invoice_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_invoice(self, planning_item_id: str, payload: dict) -> requests.Response:
		"""
		Create a new invoice
		:param planning_item_id: required - The ID of the planning item to create the invoices under
		:param payload: required
		:return: Creates a new invoice under a planning item based on the representation in the request body.
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
			api_path = "/planningItems/{0}/invoices".format(planning_item_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_invoice_under_commitment(self, planning_item_id: str, commitment_id: str, payload: dict) -> requests.Response:
		"""
		Create a new invoice under a commitment
		:param planning_item_id: required - The ID of the planning item under which the commitment is associated
		:param commitment_id: required - The ID of the commitment under which the invoices are associated
		:param payload: required - Object containing ImportFileRequest and DataDescriptor information
		:return: Creates a new invoice based on the representation in the request body.
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
			action = "POST"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/planningItems/{0}/commitments/{1}/invoices".format(planning_item_id, commitment_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def move_invoice(self, planning_item_id: str, payload: dict) -> requests.Response:
		"""
		Move selected invoices
		:param planning_item_id: required - The ID of the planning item under which the invoices are associated
		:param payload: required
		:return: Moves a selection of invoices from a planning item to a commitment. The destination is based on the representation in the request body. The invoices are either associated with a planning item directly or with a commitment under a planning item.
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
			api_path = "/planningItems/{0}/invoices#move".format(planning_item_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def move_invoice_by_commitment(self, planning_item_id: str, commitment_id: str, payload: dict) -> requests.Response:
		"""
		Move selected invoices
		:param planning_item_id: required - The ID of the planning item under which the commitment is associated
		:param commitment_id: required - The ID of the commitment under which the invoices are associated
		:param payload: required
		:return: Moves a selection of invoices from a planning item to a commitment. The destination is based on the representation in the request body. The invoices are either associated with a planning item directly or with a commitment under a planning item.
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
			action = "POST"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/planningItems/{0}/commitments/{1}/invoices#move".format(planning_item_id, commitment_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def update_invoice(self, planning_item_id: str, invoice_id: str, payload: dict) -> requests.Response:
		"""
		Update an invoice
		:param planning_item_id: required - The ID for the planning item to which the invoices are associated
		:param invoice_id: required - The unique identifier for the invoice
		:param payload: required
		:return: Updates the specified invoice based on the representation in the request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if planning_item_id is None:
			raise Exception("Planning Item ID is missing.")
		if invoice_id is None:
			raise Exception("Invoice ID is missing.")
		try:
			action = "PUT"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/planningItems/{0}/invoices/{1}".format(planning_item_id, invoice_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def update_invoice_under_commitment(self, planning_item_id: str, commitment_id: str, invoice_id: str, payload: dict) -> requests.Response:
		"""
		Update an invoice
		:param planning_item_id: required - The ID of the planning item under which the commitment is associated
		:param commitment_id: required - The ID of the commitment under which invoices are associated
		:param invoice_id: required - The unique identifier for the invoice
		:param payload: required
		:return: Updates the specified invoice based on the representation in the request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if planning_item_id is None:
			raise Exception("Planning Item ID is missing.")
		if commitment_id is None:
			raise Exception("Commitment IDis missing.")
		if invoice_id is None:
			raise Exception("Invoice ID is missing.")
		try:
			action = "PUT"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/planningItems/{0}/commitments/{1}/invoices/{2}".format(planning_item_id, commitment_id, invoice_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def delete_invoice_by_commitment(self, planning_item_id: str, commitment_id: str, invoice_id: str) -> requests.Response:
		"""
		Delete an invoice
		:param planning_item_id: required - The ID of the planning item under which commitment is associated
		:param commitment_id: required - The ID of the commitment under which invoices are associated
		:param invoice_id: required - The unique identifier for the invoice
		:return: Deletes the specified invoice.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if planning_item_id is None:
			raise Exception("Planning Item ID is missing.")
		if commitment_id is None:
			raise Exception("Commitment IDis missing.")
		if invoice_id is None:
			raise Exception("Invoice ID is missing.")
		try:
			action = "DELETE"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/planningItems/{0}/commitments/{1}/invoices/{2}".format(planning_item_id, commitment_id, invoice_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def delete_invoice(self, planning_item_id: str, invoice_id: str) -> requests.Response:
		"""
		Delete an invoice
		:param planning_item_id: required - The ID for the planning item to which the invoices are associated
		:param invoice_id: required - The unique identifier for the invoice
		:return: Deletes the specified invoice.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if planning_item_id is None:
			raise Exception("Planning Item ID is missing.")
		if invoice_id is None:
			raise Exception("Invoice ID is missing.")
		try:
			action = "DELETE"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/planningItems/{0}/invoices/{1}".format(planning_item_id, invoice_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def reconcile_invoice(self, planning_item_id: str, invoice_id: str, payload: dict) -> requests.Response:
		"""
		Reconcile an invoice
		:param planning_item_id: required - The ID of the planning item to which the invoices are associated
		:param invoice_id: required - The unique identifier of the invoice
		:param payload: required - Object containing ImportFileRequest and DataDescriptor information
		:return: Updates the specified invoice based on the representation in the request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if planning_item_id is None:
			raise Exception("Planning Item ID is missing.")
		if invoice_id is None:
			raise Exception("Commitment ID is missing.")
		try:
			action = "POST"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/planningItems/{0}/invoices/{1}/reconciliation".format(planning_item_id, invoice_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def reconcile_invoice_by_commitment(self, planning_item_id: str, commitment_id: str, invoice_id: str, payload: dict) -> requests.Response:
		"""
		Reconcile an invoice
		:param planning_item_id: required - The ID of the planning item under which the commitment is associated
		:param commitment_id: required - The ID of the commitment under which invoices are associated
		:param invoice_id: required - The unique identifier of the invoice
		:param payload: required - Object containing ImportFileRequest and DataDescriptor information
		:return: Updates the specified invoice based on the representation in the request body.
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
		if invoice_id is None:
			raise Exception("Commitment ID is missing.")
		try:
			action = "POST"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/planningItems/{0}/commitments/{1}/invoices/{2}/reconciliation".format(planning_item_id, commitment_id, invoice_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	Invoices()
