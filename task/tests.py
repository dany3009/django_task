from django.test.client import Client
import unittest

class TestAddCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        
    def add(self):
        self.client.login(username = 'admin', password = 'admin')
        self.client.post('/admin/task/group/add/', { 'name' : 'TK-32', 'warden' : '3' })
        self.client.post('/admin/task/student/add/', { 'name' : 'Bill William Klinthon', 'birth_date' : '1936-03-18', 'icket_number' : '7534', 'group' : '3' })
