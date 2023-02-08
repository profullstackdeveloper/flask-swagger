# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.protobuf_any import ProtobufAny  # noqa: F401,E501
from swagger_server import util


class GooglerpcStatus(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, code: int=None, message: str=None, details: List[ProtobufAny]=None):  # noqa: E501
        """GooglerpcStatus - a model defined in Swagger

        :param code: The code of this GooglerpcStatus.  # noqa: E501
        :type code: int
        :param message: The message of this GooglerpcStatus.  # noqa: E501
        :type message: str
        :param details: The details of this GooglerpcStatus.  # noqa: E501
        :type details: List[ProtobufAny]
        """
        self.swagger_types = {
            'code': int,
            'message': str,
            'details': List[ProtobufAny]
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message',
            'details': 'details'
        }
        self._code = code
        self._message = message
        self._details = details

    @classmethod
    def from_dict(cls, dikt) -> 'GooglerpcStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The googlerpcStatus of this GooglerpcStatus.  # noqa: E501
        :rtype: GooglerpcStatus
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """Gets the code of this GooglerpcStatus.

        The status code, which should be an enum value of [google.rpc.Code][google.rpc.Code].  # noqa: E501

        :return: The code of this GooglerpcStatus.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this GooglerpcStatus.

        The status code, which should be an enum value of [google.rpc.Code][google.rpc.Code].  # noqa: E501

        :param code: The code of this GooglerpcStatus.
        :type code: int
        """

        self._code = code

    @property
    def message(self) -> str:
        """Gets the message of this GooglerpcStatus.

        A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the [google.rpc.Status.details][google.rpc.Status.details] field, or localized by the client.  # noqa: E501

        :return: The message of this GooglerpcStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this GooglerpcStatus.

        A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the [google.rpc.Status.details][google.rpc.Status.details] field, or localized by the client.  # noqa: E501

        :param message: The message of this GooglerpcStatus.
        :type message: str
        """

        self._message = message

    @property
    def details(self) -> List[ProtobufAny]:
        """Gets the details of this GooglerpcStatus.

        A list of messages that carry the error details.  There is a common set of message types for APIs to use.  # noqa: E501

        :return: The details of this GooglerpcStatus.
        :rtype: List[ProtobufAny]
        """
        return self._details

    @details.setter
    def details(self, details: List[ProtobufAny]):
        """Sets the details of this GooglerpcStatus.

        A list of messages that carry the error details.  There is a common set of message types for APIs to use.  # noqa: E501

        :param details: The details of this GooglerpcStatus.
        :type details: List[ProtobufAny]
        """

        self._details = details