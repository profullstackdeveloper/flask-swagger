# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.v1_process_metadata import V1ProcessMetadata  # noqa: F401,E501
from swagger_server import util


class V1UpdateProcessMetadataRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, md: V1ProcessMetadata=None):  # noqa: E501
        """V1UpdateProcessMetadataRequest - a model defined in Swagger

        :param md: The md of this V1UpdateProcessMetadataRequest.  # noqa: E501
        :type md: V1ProcessMetadata
        """
        self.swagger_types = {
            'md': V1ProcessMetadata
        }

        self.attribute_map = {
            'md': 'md'
        }
        self._md = md

    @classmethod
    def from_dict(cls, dikt) -> 'V1UpdateProcessMetadataRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The v1UpdateProcessMetadataRequest of this V1UpdateProcessMetadataRequest.  # noqa: E501
        :rtype: V1UpdateProcessMetadataRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def md(self) -> V1ProcessMetadata:
        """Gets the md of this V1UpdateProcessMetadataRequest.


        :return: The md of this V1UpdateProcessMetadataRequest.
        :rtype: V1ProcessMetadata
        """
        return self._md

    @md.setter
    def md(self, md: V1ProcessMetadata):
        """Sets the md of this V1UpdateProcessMetadataRequest.


        :param md: The md of this V1UpdateProcessMetadataRequest.
        :type md: V1ProcessMetadata
        """

        self._md = md
