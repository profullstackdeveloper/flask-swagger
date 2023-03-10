# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.v1_process_report import V1ProcessReport  # noqa: F401,E501
from swagger_server import util


class V1CreateProcessReportResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, created_report: V1ProcessReport=None):  # noqa: E501
        """V1CreateProcessReportResponse - a model defined in Swagger

        :param created_report: The created_report of this V1CreateProcessReportResponse.  # noqa: E501
        :type created_report: V1ProcessReport
        """
        self.swagger_types = {
            'created_report': V1ProcessReport
        }

        self.attribute_map = {
            'created_report': 'createdReport'
        }
        self._created_report = created_report

    @classmethod
    def from_dict(cls, dikt) -> 'V1CreateProcessReportResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The v1CreateProcessReportResponse of this V1CreateProcessReportResponse.  # noqa: E501
        :rtype: V1CreateProcessReportResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created_report(self) -> V1ProcessReport:
        """Gets the created_report of this V1CreateProcessReportResponse.


        :return: The created_report of this V1CreateProcessReportResponse.
        :rtype: V1ProcessReport
        """
        return self._created_report

    @created_report.setter
    def created_report(self, created_report: V1ProcessReport):
        """Sets the created_report of this V1CreateProcessReportResponse.


        :param created_report: The created_report of this V1CreateProcessReportResponse.
        :type created_report: V1ProcessReport
        """

        self._created_report = created_report
