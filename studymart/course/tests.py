from django.test import TestCase
from django.urls import reverse


class SuccessRedirectTests(TestCase):
    def test_form_redirects_to_success_page_after_valid_submission(self):
        response = self.client.post(
            reverse("show_form"),
            {
                "student_name": "Test User",
                "student_email": "test@example.com",
                "batch": 10,
                "course": "Django",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("success"))
