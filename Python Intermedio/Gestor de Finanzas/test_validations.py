from datetime import datetime, timedelta

import validations

class TestIsValidText:
    def test_text_with_content_is_valid(self):
        assert validations.is_valid_text("Super") is True

    def test_empty_text_is_not_valid(self):
        assert validations.is_valid_text("") is False

    def test_text_with_only_spaces_is_not_valid(self):
        assert validations.is_valid_text("   ") is False

class TestIsValidDate:
    def test_date_with_correct_format_is_valid(self):
        assert validations.is_valid_date("02/07/2025") is True

    def test_date_with_wrong_format_is_not_valid(self):
        assert validations.is_valid_date("2025-07-02") is False

    def test_empty_date_is_not_valid(self):
        assert validations.is_valid_date("") is False

    def test_date_with_nonexistent_day_is_not_valid(self):
        assert validations.is_valid_date("31/02/2025") is False

class TestIsValidAmount:
    def test_positive_amount_is_valid(self):
        assert validations.is_valid_amount("150.50") is True

    def test_negative_amount_is_not_valid(self):
        assert validations.is_valid_amount("-150.50") is False

    def test_zero_amount_is_not_valid(self):
        assert validations.is_valid_amount("0") is False

    def test_non_numeric_amount_is_not_valid(self):
        assert validations.is_valid_amount("abc") is False

class TestIsNotFutureDate:
    def test_todays_date_is_valid(self):
        today = datetime.now().strftime(validations.DATE_FORMAT)
        assert validations.is_not_future_date(today) is True

    def test_past_date_is_valid(self):
        yesterday = (datetime.now() - timedelta(days=1)).strftime(validations.DATE_FORMAT)
        assert validations.is_not_future_date(yesterday) is True

    def test_future_date_is_not_valid(self):
        tomorrow = (datetime.now() + timedelta(days=1)).strftime(validations.DATE_FORMAT)
        assert validations.is_not_future_date(tomorrow) is False

    def test_date_with_wrong_format_is_not_valid(self):
        assert validations.is_not_future_date("2025-07-02") is False
