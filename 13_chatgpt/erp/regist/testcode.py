import unittest


class TestLoginForm(unittest.TestCase):
    def test_display_labels_and_inputs(self):
        # TODO: Implement the code to render the login form
        # and extract the labels and inputs.
        # For example:
        # form = render_login_form()
        # username_label = form.find_label_by_text("Username:")
        # password_label = form.find_label_by_text("Password:")
        # username_input = form.find_input_by_id("username")
        # password_input = form.find_input_by_id("password")

        self.assertEqual(username_label.text, "Username:")
        self.assertEqual(password_label.text, "Password:")
        self.assertIsNotNone(username_input)
        self.assertIsNotNone(password_input)


if __name__ == '__main__':
    unittest.main()
