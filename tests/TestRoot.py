#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Root
Contains the operations for the root resource.
	1. get_root(self) -> requests.Response
"""

import os
import unittest
from sasci360apiplan import root


class TestRoot(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = os.environ.get("CI360_ALGORITHM", "HS256")
		api = os.environ.get("CI360_API", "/marketingPlan")
		encoding = os.environ.get("CI360_ENCODING", "UTF-8")
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.root = root.Root(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_root(self):
		"""
		1. get_root(self) -> requests.Response
		"""
		result = self.root.get_root()
		print(result)
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
