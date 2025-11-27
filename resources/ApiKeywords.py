import json
from pages.UserApiPage import UserApiPage

class ApiKeywords:

    def __init__(self):
        self.user_api = UserApiPage()
        self.last_response = None
        self.current_user_id = None
        self.email = None
        self.password = None

    def user_id_is(self, user_id):
        self.current_user_id = int(user_id)

    def i_create_user_with_email_and_password(self, email,password):
        self.email = email
        self.password = password

    def i_request_single_user(self):
        self.last_response = self.user_api.get_single_user(self.current_user_id)

    def response_status_should_be(self, expected_status):
        actual = self.last_response.status_code
        if actual != int(expected_status):
            raise AssertionError(f"Expected {expected_status}, got {actual}")

    def response_should_contain_field(self, field):
        body = self.last_response.json()
        if field not in json.dumps(body):
            raise AssertionError(f"Field '{field}' not found in response")

    def i_send_create_user_request(self):
        self.last_response = self.user_api.create_user(self.email, self.password)

    def response_field_should_equal_to(self, field, expected_value):
        body = self.last_response.json()
        # Mendukung nested key dengan dot notation: data.email
        keys = field.split(".")
        actual_value = body
        for key in keys:
            if key not in actual_value:
                raise AssertionError(f"Field '{field}' not found in response")
            actual_value = actual_value[key]

        # Auto convert angka
        if isinstance(expected_value, str) and expected_value.isdigit():
            expected_value = int(expected_value)

        if actual_value != expected_value:
            raise AssertionError(
                f"Expected {field}={expected_value}, got {actual_value}"
            )



