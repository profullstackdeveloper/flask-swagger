# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class V1ProcessAnchors(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, teams: List[str]=None, domains: List[str]=None, users: List[str]=None, related_terms: List[str]=None):  # noqa: E501
        """V1ProcessAnchors - a model defined in Swagger

        :param teams: The teams of this V1ProcessAnchors.  # noqa: E501
        :type teams: List[str]
        :param domains: The domains of this V1ProcessAnchors.  # noqa: E501
        :type domains: List[str]
        :param users: The users of this V1ProcessAnchors.  # noqa: E501
        :type users: List[str]
        :param related_terms: The related_terms of this V1ProcessAnchors.  # noqa: E501
        :type related_terms: List[str]
        """
        self.swagger_types = {
            'teams': List[str],
            'domains': List[str],
            'users': List[str],
            'related_terms': List[str]
        }

        self.attribute_map = {
            'teams': 'teams',
            'domains': 'domains',
            'users': 'users',
            'related_terms': 'relatedTerms'
        }
        self._teams = teams
        self._domains = domains
        self._users = users
        self._related_terms = related_terms

    @classmethod
    def from_dict(cls, dikt) -> 'V1ProcessAnchors':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The v1ProcessAnchors of this V1ProcessAnchors.  # noqa: E501
        :rtype: V1ProcessAnchors
        """
        return util.deserialize_model(dikt, cls)

    @property
    def teams(self) -> List[str]:
        """Gets the teams of this V1ProcessAnchors.


        :return: The teams of this V1ProcessAnchors.
        :rtype: List[str]
        """
        return self._teams

    @teams.setter
    def teams(self, teams: List[str]):
        """Sets the teams of this V1ProcessAnchors.


        :param teams: The teams of this V1ProcessAnchors.
        :type teams: List[str]
        """

        self._teams = teams

    @property
    def domains(self) -> List[str]:
        """Gets the domains of this V1ProcessAnchors.


        :return: The domains of this V1ProcessAnchors.
        :rtype: List[str]
        """
        return self._domains

    @domains.setter
    def domains(self, domains: List[str]):
        """Sets the domains of this V1ProcessAnchors.


        :param domains: The domains of this V1ProcessAnchors.
        :type domains: List[str]
        """

        self._domains = domains

    @property
    def users(self) -> List[str]:
        """Gets the users of this V1ProcessAnchors.


        :return: The users of this V1ProcessAnchors.
        :rtype: List[str]
        """
        return self._users

    @users.setter
    def users(self, users: List[str]):
        """Sets the users of this V1ProcessAnchors.


        :param users: The users of this V1ProcessAnchors.
        :type users: List[str]
        """

        self._users = users

    @property
    def related_terms(self) -> List[str]:
        """Gets the related_terms of this V1ProcessAnchors.


        :return: The related_terms of this V1ProcessAnchors.
        :rtype: List[str]
        """
        return self._related_terms

    @related_terms.setter
    def related_terms(self, related_terms: List[str]):
        """Sets the related_terms of this V1ProcessAnchors.


        :param related_terms: The related_terms of this V1ProcessAnchors.
        :type related_terms: List[str]
        """

        self._related_terms = related_terms
