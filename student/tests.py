from django.test import TestCase
from django.urls import reverse

class StudentProfileTestCase(TestCase):
    def test_valid_student_profile(self):
        response = self.client.get('/student/101/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Alice')

    def test_invalid_student_profile(self):
        response = self.client.get('/student/999/')
        self.assertEqual(response.status_code, 404)

