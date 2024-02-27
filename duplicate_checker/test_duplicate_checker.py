import unittest

import pandas as pd
from .duplicate_checker import count_and_sample_duplicates_by_columns


class TestDuplicateChecker(unittest.TestCase):
    def setUp(self):
        """Set up test data for the unit tests and Assignment."""
        self.df = pd.DataFrame(
            data=[
                ["A", "a", "x", 1],
                ["A", "b", "x", 1],
                ["A", "c", "x", 1],
                ["B", "a", "x", 1],
                ["B", "b", "x", 1],
                ["B", "c", "x", 1],
                ["A", "a", "y", 1],
            ],
            columns=["col_1", "col_2", "col_3", "col_4"],
        )

    def test_columns_col_1(self):
        """Test duplicates based on ['col_1']."""
        result = count_and_sample_duplicates_by_columns(self.df, ["col_1"])
        expected_samples = pd.DataFrame(
            {"col_1": ["A", "B"], "number_of_duplicates": [4, 3]}
        )
        self.assertEqual(result["count"], 7)
        pd.testing.assert_frame_equal(result["samples"], expected_samples)

    def test_columns_col_1_col_2(self):
        """Test duplicates based on ['col_1', 'col_2']."""
        result = count_and_sample_duplicates_by_columns(self.df, ["col_1", "col_2"])
        expected_samples = pd.DataFrame(
            {"col_1": ["A"], "col_2": ["a"], "number_of_duplicates": [2]}
        )
        self.assertEqual(result["count"], 2)
        pd.testing.assert_frame_equal(result["samples"], expected_samples)

    def test_columns_col_1_col_2_col_3(self):
        """Test duplicates based on ['col_1', 'col_2', 'col_3']."""
        result = count_and_sample_duplicates_by_columns(
            self.df, ["col_1", "col_2", "col_3"]
        )
        self.assertEqual(result["count"], 0)
        self.assertTrue(result["samples"].empty)

    def test_empty_dataframe(self):
        """Test with an empty DataFrame."""
        df_empty = pd.DataFrame()
        result = count_and_sample_duplicates_by_columns(df_empty, ["col_1"])
        self.assertEqual(result["count"], 0)
        self.assertTrue(result["samples"].empty)

    def test_invalid_column_name(self):
        """Test with an invalid column name."""
        result = count_and_sample_duplicates_by_columns(self.df, ["invalid_column"])
        self.assertEqual(result["count"], 0)
        expected_columns = ["invalid_column", "number_of_duplicates"]
        self.assertTrue(result["samples"].empty)
        self.assertListEqual(list(result["samples"].columns), expected_columns)


if __name__ == "__main__":
    unittest.main()
