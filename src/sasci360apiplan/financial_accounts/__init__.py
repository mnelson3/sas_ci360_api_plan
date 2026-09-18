#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apiplan.base import Base


class FinancialAccounts(Base):
	"""
	Financial Accounts
	Contains the operations for financial accounts.
		1. get_financial_accounts(self, **kwargs) -> requests.Response
		2. get_financial_account(self, financial_account_id: str) -> requests.Response
		3. create_financial_account(self, payload: dict) -> requests.Response
		4. update_financial_account(self, financial_account_id: str, payload: dict) -> requests.Response
		5. delete_financial_account(self, financial_account_id: str) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_financial_accounts(self, **kwargs) -> requests.Response:
		"""
		Get a collection of financial accounts
		:keyword start: int, optional - The index of the first financial account to return
		:keyword limit: int, optional - The maximum number of financial accounts to return
		:keyword filter: str, optional - The criteria for filtering the financial accounts. You can specify filter=eq(obsolete,false) or filter=eq(obsolete,true)
		:return: Returns a collection of financial accounts based on options for pagination, filtering, and sorting. The items in the collection use the application/vnd.sas.marketing.financial.account.summary media type.
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
				query_string.join("filter={0}&".format(kwargs["filter"]))
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/financialAccounts{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_financial_account(self, financial_account_id: str) -> requests.Response:
		"""
		Get a financial account
		:param financial_account_id: required - The unique identifier for the financial account
		:return: Returns the representation of the specified financial account.
		:rtype: requests.Response
		"""
		result = None
		if financial_account_id is None:
			raise Exception("Financial Account ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(self.token)
			}
			params = None
			api_path = "/financialAccounts/{0}".format(financial_account_id)
			url = "https://{0}{1}{2}".format(self.host, self.api, api_path)
			result = self.connection.connect(self, action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_financial_account(self, payload: dict) -> requests.Response:
		"""
		Create a new financial account
		:param payload: required
		:return: Creates a new financial account based on the representation in the request body.
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
			api_path = "/financialAccounts"
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def update_financial_account(self, financial_account_id: str, payload: dict) -> requests.Response:
		"""
		Update a financial account
		:param financial_account_id: required - The unique identifier for the financial account
		:param payload: required
		:return: Updates the specified financial account based on the representation in the request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if financial_account_id is None:
			raise Exception("Financial Account ID is missing.")
		try:
			action = "PUT"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/financialAccounts/{0}".format(financial_account_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def delete_financial_account(self, financial_account_id: str) -> requests.Response:
		"""
		Delete a financial account
		:param financial_account_id: required - The unique identifier for the financial account
		:return: Deletes the specified financial account.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if financial_account_id is None:
			raise Exception("Financial Account ID is missing.")
		try:
			action = "DELETE"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/financialAccounts/{0}".format(financial_account_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	FinancialAccounts()
