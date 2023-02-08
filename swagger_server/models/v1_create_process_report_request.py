# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.v1_process_report import V1ProcessReport  # noqa: F401,E501
from swagger_server import util


class V1CreateProcessReportRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, report: V1ProcessReport=None):  # noqa: E501
        """V1CreateProcessReportRequest - a model defined in Swagger

        :param report: The report of this V1CreateProcessReportRequest.  # noqa: E501
        :type report: V1ProcessReport
        """
        self.swagger_types = {
            'report': V1ProcessReport
        }

        self.attribute_map = {
            'report': 'report'
        }
        self._report = report

    @classmethod
    def from_dict(cls, dikt) -> 'V1CreateProcessReportRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The v1CreateProcessReportRequest of this V1CreateProcessReportRequest.  # noqa: E501
        :rtype: V1CreateProcessReportRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def report(self) -> V1ProcessReport:
        """Gets the report of this V1CreateProcessReportRequest.


        :return: The report of this V1CreateProcessReportRequest.
        :rtype: V1ProcessReport
        """
        return self._report

    @report.setter
    def report(self, report: V1ProcessReport):
        """Sets the report of this V1CreateProcessReportRequest.


        :param report: The report of this V1CreateProcessReportRequest.
        :type report: V1ProcessReport
        """

        self._report = report
