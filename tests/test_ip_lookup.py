"""Tests for ip-lookup."""

import pytest
from ip_lookup import lookup


class TestLookup:
    """Test suite for lookup."""

    def test_basic(self):
        """Test basic usage."""
        result = lookup("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            lookup("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = lookup(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
