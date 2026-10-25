"""Regression tests for the CS50P exercise helpers."""
import unittest
from unittest.mock import Mock, patch

from bitcoin.bitcoin import get_bitcoin_price
from camel.camel import to_snake_case
from extensions.extensions import get_mime_type
from fuel.fuel import convert, gauge
from meal.meal import check_meal_time
from plates.plates import is_valid
from twttr.twttr import shorten


class ProjectTests(unittest.TestCase):
    def test_bitcoin_price_parsing(self):
        response = Mock()
        response.json.return_value = {"data": {"priceUsd": "65000.25"}}
        with patch("bitcoin.bitcoin.requests.get", return_value=response) as get:
            self.assertEqual(get_bitcoin_price("test-key"), 65000.25)
        get.assert_called_once()
        self.assertEqual(get.call_args.kwargs["params"], {"apiKey": "test-key"})
        self.assertEqual(get.call_args.kwargs["timeout"], 10)
        response.raise_for_status.assert_called_once()

    def test_camel_case_conversion(self):
        self.assertEqual(to_snake_case("camelCase"), "camel_case")
        self.assertEqual(to_snake_case("already_snake"), "already_snake")

    def test_extension_lookup(self):
        self.assertEqual(get_mime_type("PHOTO.JPEG"), "image/jpeg")
        self.assertEqual(get_mime_type("document.pdf"), "application/pdf")
        self.assertEqual(get_mime_type("file.unknown"), "application/octet-stream")
        self.assertEqual(get_mime_type("no-extension"), "application/octet-stream")

    def test_fuel_conversion(self):
        self.assertEqual(convert("1/2"), 50)
        self.assertEqual(gauge(1), "E")
        self.assertEqual(gauge(99), "F")
        self.assertEqual(gauge(50), "50%")
        with self.assertRaises(ValueError):
            convert("2/1")
        with self.assertRaises(ValueError):
            convert("1/0")

    def test_meal_time(self):
        self.assertEqual(check_meal_time("7:30"), "breakfast time")
        self.assertEqual(check_meal_time("12:30"), "lunch time")
        self.assertEqual(check_meal_time("18:30"), "dinner time")
        self.assertIsNone(check_meal_time("10:00"))
        with self.assertRaises(ValueError):
            check_meal_time("25:00")

    def test_vanity_plates(self):
        self.assertTrue(is_valid("CS50"))
        self.assertTrue(is_valid("HELLO"))
        self.assertFalse(is_valid("CS05"))
        self.assertFalse(is_valid("CS5A"))
        self.assertFalse(is_valid("A!"))
        self.assertFalse(is_valid("TOOLONG"))

    def test_vowel_removal(self):
        self.assertEqual(shorten("Twitter"), "Twttr")
        self.assertEqual(shorten("AEIOU"), "")


if __name__ == "__main__":
    unittest.main()
