#!/usr/bin/env python
import unittest
loader = unittest.TestLoader()
start_dir = 'test_collateral/'
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)