import unittest
from backend import DataGetter

class TestDataGetter(unittest.TestCase):
    file_path = 'sample_tiny.json'
    document_id = "140224132818-2a89379e80cb7340d8504ad002fab76d"
    limit = 10

    visitor_id = "76175bb1ea9805a1"
    data_getter = DataGetter(file_path)

    def test_get_countries_data(self):
        countries = self.data_getter.get_countries_data(document_uuid=self.document_id)
        self.assertIsInstance(countries, dict)  # Check if the returned value is a dictionary

    def test_get_continent_data(self):
        continents = self.data_getter.get_continent_data(document_uuid=self.document_id)
        self.assertIsInstance(continents, dict)  # Check if the returned value is a dictionary

    def test_get_top_10_readers(self):
        top_readers = self.data_getter.get_reading_time(limit=self.limit)
        self.assertIsInstance(top_readers, list)  # Check if the returned value is a list

    def test_get_also_like_document(self):
        doc_list = self.data_getter.get_also_like_documents(self.document_id, self.visitor_id, sorting_function = lambda x: self.data_getter.order(x, "desc", self.limit))
        self.assertIsInstance(doc_list, list)  # Check if the returned value is a list

    def test_also_like_document_graph(self):
        doc_graph = self.data_getter.generate_also_like_graph(self.document_id, self.visitor_id)
        self.assertIsInstance(doc_graph, dict)  # Check if the returned value is a dictionary

    def test_get_browsers(self):
        great_browsers = self.data_getter.get_browser_data()
        self.assertIsInstance(great_browsers, dict)  # Check if the returned value is a dictionary

if __name__ == '__main__':
    unittest.main()
