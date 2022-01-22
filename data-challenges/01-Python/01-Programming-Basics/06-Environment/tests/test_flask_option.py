# pylint: disable-all

import unittest
import os
from flask_option import start

class TestFlaskOption(unittest.TestCase):
    def test_start_with_flask_env_development(self):
        os.environ['FLASK_ENV'] = 'development'
        self.assertEqual(start(), "Starting in development mode...")

    def test_start_with_flask_env_production(self):
        os.environ['FLASK_ENV'] = 'production'
        self.assertEqual(start(), "Starting in production mode...")

    def test_start_with_no_flask_env(self):
        del os.environ['FLASK_ENV']
        self.assertEqual(start(), "Starting in production mode...")
