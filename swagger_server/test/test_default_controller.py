# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_parse_file(self):
        """Test case for parse_file

        send a file to parse
        """
        data = dict(file='file_example')
        response = self.client.open(
            '/MasterMinded/Parsersv2/1.0.0/send_file',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
