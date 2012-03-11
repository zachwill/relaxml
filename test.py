#!/usr/bin/env python

"""Unit tests for the relaxml module."""

import unittest
import tempfile

from relaxml import xml as xml2dict
from relaxml import XML2Dict


class TestXML2Dict(unittest.TestCase):

    def setUp(self):
        self.xml = '<?xml version="1.0" encoding="UTF-8" ?>\n'

    def test_simple_xml_to_dict(self):
        xml = self.xml + '<a><b>5</b><c>9</c></a>'
        expected_output = {'a': {'b': '5', 'c': '9'}}
        self.assertEqual(xml2dict(xml), expected_output)

    def test_xml_to_list_of_values(self):
        xml = self.xml + '<a><b>1</b><b>2</b><b>3</b></a>'
        expected_output = {'a': {'b': ['1', '2', '3']}}
        self.assertEqual(xml2dict(xml), expected_output)

    def test_xml_to_mixture_of_lists_and_dicts(self):
        xml = self.xml + '<a><b>1</b><b>2</b><c><d>3</d></c></a>'
        expected_output = {'a': {'b': ['1', '2'], 'c': {'d': '3'}}}
        self.assertEqual(xml2dict(xml), expected_output)

    def test_xml_attributes_retained(self):
        xml = self.xml + '<numbers one="1" two="2" />'
        expected_output = {'numbers': {'one': '1', 'two': '2'}}
        self.assertEqual(xml2dict(xml), expected_output)

    def test_both_attributes_and_child_nodes(self):
        xml = self.xml + '<a foo="foo">bar</a>'
        expected_output = {'a': {'a': 'bar', 'foo': 'foo'}}
        self.assertEqual(xml2dict(xml), expected_output)

    def test_error_raised_when_passed_complicated_XML(self):
        xml = self.xml + '<tag tag="foo">bar</tag>'
        self.assertRaises(ValueError, xml2dict, xml)

    def test_against_XML_namespaces(self):
        namespaces_table = """
        <h:table xmlns:h="http://www.w3.org/TR/html4/">
          <h:tr>
           <h:td>Apples</h:td>
           <h:td>Bananas</h:td>
         </h:tr>
        </h:table>"""
        xml = self.xml + namespaces_table
        expected_output = {
            ('http://www.w3.org/TR/html4/', 'table'): {
                ('http://www.w3.org/TR/html4/', 'tr'): {
                    ('http://www.w3.org/TR/html4/', 'td'): ['Apples', 'Bananas']
                }
            }
        }
        self.assertEquals(xml2dict(xml), expected_output)

    def test_node_attribute_has_same_name_as_child(self):
        xml = self.xml + '<a b="foo"><b><c>1</c></b></a>'
        expected_output = {'a': {'b': ['foo', {'c': '1'}]}}
        self.assertEquals(xml2dict(xml), expected_output)

    def test_parsing_XML_from_file_from_function(self):
        xml = self.xml + '<a foo="bar" hello="word" />'
        f = tempfile.TemporaryFile(mode="w+t")
        f.write(xml)
        f.seek(0)
        expected_output = {'a': {'foo': 'bar', 'hello': 'word'}}
        self.assertEquals(xml2dict(f), expected_output)

    def test_parsing_XML_from_file_with_parse_method(self):
        xml = self.xml + '<a foo="bar" hello="word" />'
        f = tempfile.NamedTemporaryFile(mode="w+t")
        f.write(xml)
        f.seek(0)
        expected_output = {'a': {'foo': 'bar', 'hello': 'word'}}
        self.assertEquals(XML2Dict().parse(f.name), expected_output)


if __name__ == '__main__':
    unittest.main()
