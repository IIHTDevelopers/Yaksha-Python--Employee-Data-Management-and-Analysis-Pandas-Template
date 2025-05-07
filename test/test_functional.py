import unittest
import pandas as pd
from mainclass import EmployeeDataAnalysis
from test.TestUtils import TestUtils
import os

class FunctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analysis = EmployeeDataAnalysis("employee_data.csv")
        cls.test_obj = TestUtils()

    def test_csv_loading(self):
        """Test if the CSV file is loaded correctly."""
        try:
            if not self.analysis:
                self.test_obj.yakshaAssert("TestCSVLoading", False, "functional")
                print("TestCSVLoading = Failed")
                return
            obj = not self.analysis.df.empty
            self.test_obj.yakshaAssert("TestCSVLoading", obj, "functional")
            print("TestCSVLoading = Passed" if obj else "TestCSVLoading = Failed")
        except:
            self.test_obj.yakshaAssert("TestCSVLoading", False, "functional")
            print("TestCSVLoading = Failed")
                
    def test_display_head(self):
        """Test if the first 5 rows are returned correctly."""
        try:
            head = self.analysis.display_head()
            if head is None:
                head = []
            obj = len(head) == 5
            self.test_obj.yakshaAssert("TestDisplayHead", obj, "functional")
            print("TestDisplayHead = Passed" if obj else "TestDisplayHead = Failed")
        except Exception as e:
            print("TestDisplayHead = Failed")

    def test_retrieve_column_label_based(self):
        """Test retrieving columns using label-based indexing."""
        try:
            result = self.analysis.retrieve_columns_label_based("Name")
            obj = result.equals(self.analysis.df["Name"])
            self.test_obj.yakshaAssert("TestRetrieveColumnLabelBased", obj, "functional")
            print("TestRetrieveColumnLabelBased = Passed" if obj else "TestRetrieveColumnLabelBased = Failed")
        except Exception as e:
            print("TestRetrieveColumnLabelBased = Failed")

    def test_retrieve_column_position_based(self):
        """Test retrieving columns using position-based indexing."""
        try:
            result = self.analysis.retrieve_columns_position_based(1)
            obj = result.equals(self.analysis.df.iloc[:, 1])
            self.test_obj.yakshaAssert("TestRetrieveColumnPositionBased", obj, "functional")
            print("TestRetrieveColumnPositionBased = Passed" if obj else "TestRetrieveColumnPositionBased = Failed")
        except Exception as e:
            print("TestRetrieveColumnPositionBased = Failed")

    def test_export_updated_csv(self):
        """Check if the updated CSV file is saved."""
        self.analysis.export_updated_csv()
        try:
            pd.read_csv("updated_employee_data.csv")
            obj = True
        except FileNotFoundError:
            obj = False
        self.test_obj.yakshaAssert("TestExportUpdatedCSV", obj, "functional")
        print("TestExportUpdatedCSV = Passed" if obj else "TestExportUpdatedCSV = Failed")
