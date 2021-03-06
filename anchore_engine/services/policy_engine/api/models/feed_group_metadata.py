# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from anchore_engine.services.policy_engine.api.models.base_model_ import Model
from anchore_engine.services.policy_engine.api import util


class FeedGroupMetadata(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name=None, created_at=None, last_sync=None, record_count=None):  # noqa: E501
        """FeedGroupMetadata - a model defined in Swagger

        :param name: The name of this FeedGroupMetadata.  # noqa: E501
        :type name: str
        :param created_at: The created_at of this FeedGroupMetadata.  # noqa: E501
        :type created_at: datetime
        :param last_sync: The last_sync of this FeedGroupMetadata.  # noqa: E501
        :type last_sync: datetime
        :param record_count: The record_count of this FeedGroupMetadata.  # noqa: E501
        :type record_count: int
        """
        self.swagger_types = {
            'name': str,
            'created_at': datetime,
            'last_sync': datetime,
            'record_count': int
        }

        self.attribute_map = {
            'name': 'name',
            'created_at': 'created_at',
            'last_sync': 'last_sync',
            'record_count': 'record_count'
        }

        self._name = name
        self._created_at = created_at
        self._last_sync = last_sync
        self._record_count = record_count

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FeedGroupMetadata of this FeedGroupMetadata.  # noqa: E501
        :rtype: FeedGroupMetadata
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this FeedGroupMetadata.


        :return: The name of this FeedGroupMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FeedGroupMetadata.


        :param name: The name of this FeedGroupMetadata.
        :type name: str
        """

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this FeedGroupMetadata.


        :return: The created_at of this FeedGroupMetadata.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FeedGroupMetadata.


        :param created_at: The created_at of this FeedGroupMetadata.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def last_sync(self):
        """Gets the last_sync of this FeedGroupMetadata.


        :return: The last_sync of this FeedGroupMetadata.
        :rtype: datetime
        """
        return self._last_sync

    @last_sync.setter
    def last_sync(self, last_sync):
        """Sets the last_sync of this FeedGroupMetadata.


        :param last_sync: The last_sync of this FeedGroupMetadata.
        :type last_sync: datetime
        """

        self._last_sync = last_sync

    @property
    def record_count(self):
        """Gets the record_count of this FeedGroupMetadata.


        :return: The record_count of this FeedGroupMetadata.
        :rtype: int
        """
        return self._record_count

    @record_count.setter
    def record_count(self, record_count):
        """Sets the record_count of this FeedGroupMetadata.


        :param record_count: The record_count of this FeedGroupMetadata.
        :type record_count: int
        """

        self._record_count = record_count
