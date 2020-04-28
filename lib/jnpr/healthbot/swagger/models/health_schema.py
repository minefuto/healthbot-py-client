# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: healthbot-hackers@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class HealthSchema(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'device_health': 'DeviceHealthSchema',
        'network_health': 'GroupHealthSchema'
    }

    attribute_map = {
        'device_health': 'device-health',
        'network_health': 'network-health'
    }

    def __init__(self, device_health=None, network_health=None):  # noqa: E501
        """HealthSchema - a model defined in Swagger"""  # noqa: E501

        self._device_health = None
        self._network_health = None
        self.discriminator = None

        if device_health is not None:
            self.device_health = device_health
        if network_health is not None:
            self.network_health = network_health

    @property
    def device_health(self):
        """Gets the device_health of this HealthSchema.  # noqa: E501


        :return: The device_health of this HealthSchema.  # noqa: E501
        :rtype: DeviceHealthSchema
        """
        return self._device_health

    @device_health.setter
    def device_health(self, device_health):
        """Sets the device_health of this HealthSchema.


        :param device_health: The device_health of this HealthSchema.  # noqa: E501
        :type: DeviceHealthSchema
        """

        self._device_health = device_health

    @property
    def network_health(self):
        """Gets the network_health of this HealthSchema.  # noqa: E501


        :return: The network_health of this HealthSchema.  # noqa: E501
        :rtype: GroupHealthSchema
        """
        return self._network_health

    @network_health.setter
    def network_health(self, network_health):
        """Sets the network_health of this HealthSchema.


        :param network_health: The network_health of this HealthSchema.  # noqa: E501
        :type: GroupHealthSchema
        """

        self._network_health = network_health

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(HealthSchema, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HealthSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
