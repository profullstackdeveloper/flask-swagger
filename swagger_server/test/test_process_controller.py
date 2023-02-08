# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.googlerpc_status import GooglerpcStatus  # noqa: E501
from swagger_server.models.v1_create_process_metadata_request import V1CreateProcessMetadataRequest  # noqa: E501
from swagger_server.models.v1_create_process_metadata_response import V1CreateProcessMetadataResponse  # noqa: E501
from swagger_server.models.v1_create_process_report_request import V1CreateProcessReportRequest  # noqa: E501
from swagger_server.models.v1_create_process_report_response import V1CreateProcessReportResponse  # noqa: E501
from swagger_server.models.v1_generate_report_from_process_metadata_response import V1GenerateReportFromProcessMetadataResponse  # noqa: E501
from swagger_server.models.v1_get_process_metadata_response import V1GetProcessMetadataResponse  # noqa: E501
from swagger_server.models.v1_get_process_report_response import V1GetProcessReportResponse  # noqa: E501
from swagger_server.models.v1_list_process_metadata_response import V1ListProcessMetadataResponse  # noqa: E501
from swagger_server.models.v1_update_process_metadata_request import V1UpdateProcessMetadataRequest  # noqa: E501
from swagger_server.models.v1_update_process_metadata_response import V1UpdateProcessMetadataResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProcessController(BaseTestCase):
    """ProcessController integration test stubs"""

    def test_process_service_create_process_metadata(self):
        """Test case for process_service_create_process_metadata

        Create new process metadata. Called from UI when pressing '+ Create new process' and manually by Analysts.
        """
        body = V1CreateProcessMetadataRequest()
        response = self.client.open(
            '/api/v1/process-metadata',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_process_service_create_process_report(self):
        """Test case for process_service_create_process_report

        Create a process report. If there is an existing report for the process, the existing reports will remain in the DB (for a while) if you want to revert.
        """
        body = V1CreateProcessReportRequest()
        response = self.client.open(
            '/api/v1/process-report',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_process_service_generate_report_from_process_metadata(self):
        """Test case for process_service_generate_report_from_process_metadata

        Trigger Argo workflow that generates a report from existing metadata.
        """
        response = self.client.open(
            '/api/v1/genreate-report/{processId}'.format(process_id='process_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_process_service_get_process_metadata(self):
        """Test case for process_service_get_process_metadata

        Return a process metadata, if exists.
        """
        response = self.client.open(
            '/api/v1/process-metadata/{processMetadataId}'.format(process_metadata_id='process_metadata_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_process_service_get_process_report(self):
        """Test case for process_service_get_process_report

        Get a single process report.
        """
        response = self.client.open(
            '/api/v1/process-report/{processId}'.format(process_id='process_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_process_service_list_process_metadata(self):
        """Test case for process_service_list_process_metadata

        List all process metadata (used from process lib screen).
        """
        query_string = [('limit', 789)]
        response = self.client.open(
            '/api/v1/process-metadata',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_process_service_update_process_metadata(self):
        """Test case for process_service_update_process_metadata

        Update an existing process metadata.
        """
        body = V1UpdateProcessMetadataRequest()
        response = self.client.open(
            '/api/v1/process-metadata',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
