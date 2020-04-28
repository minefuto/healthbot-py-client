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


class RuleSchemaWhenEqualto(object):
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
        'all': 'list[ERRORUNKNOWN]',
        'any': 'list[ERRORUNKNOWN]',
        'left_operand': 'str',
        'right_operand': 'str',
        'time_range': 'str'
    }

    attribute_map = {
        'all': 'all',
        'any': 'any',
        'left_operand': 'left-operand',
        'right_operand': 'right-operand',
        'time_range': 'time-range'
    }

    def __init__(self, all=None, any=None, left_operand=None, right_operand=None, time_range=None):  # noqa: E501
        """RuleSchemaWhenEqualto - a model defined in Swagger"""  # noqa: E501

        self._all = None
        self._any = None
        self._left_operand = None
        self._right_operand = None
        self._time_range = None
        self.discriminator = None

        if all is not None:
            self.all = all
        if any is not None:
            self.any = any
        self.left_operand = left_operand
        self.right_operand = right_operand
        if time_range is not None:
            self.time_range = time_range

    @property
    def all(self):
        """Gets the all of this RuleSchemaWhenEqualto.  # noqa: E501

        With this flag, result is set to True only if all the data matches the given condition  # noqa: E501

        :return: The all of this RuleSchemaWhenEqualto.  # noqa: E501
        :rtype: list[ERRORUNKNOWN]
        """
        return self._all

    @all.setter
    def all(self, all):
        """Sets the all of this RuleSchemaWhenEqualto.

        With this flag, result is set to True only if all the data matches the given condition  # noqa: E501

        :param all: The all of this RuleSchemaWhenEqualto.  # noqa: E501
        :type: list[ERRORUNKNOWN]
        """

        self._all = all

    @property
    def any(self):
        """Gets the any of this RuleSchemaWhenEqualto.  # noqa: E501

        With this flag, result is set to True if any one of the data matches the condition  # noqa: E501

        :return: The any of this RuleSchemaWhenEqualto.  # noqa: E501
        :rtype: list[ERRORUNKNOWN]
        """
        return self._any

    @any.setter
    def any(self, any):
        """Sets the any of this RuleSchemaWhenEqualto.

        With this flag, result is set to True if any one of the data matches the condition  # noqa: E501

        :param any: The any of this RuleSchemaWhenEqualto.  # noqa: E501
        :type: list[ERRORUNKNOWN]
        """

        self._any = any

    @property
    def left_operand(self):
        """Gets the left_operand of this RuleSchemaWhenEqualto.  # noqa: E501

        Left operand  # noqa: E501

        :return: The left_operand of this RuleSchemaWhenEqualto.  # noqa: E501
        :rtype: str
        """
        return self._left_operand

    @left_operand.setter
    def left_operand(self, left_operand):
        """Sets the left_operand of this RuleSchemaWhenEqualto.

        Left operand  # noqa: E501

        :param left_operand: The left_operand of this RuleSchemaWhenEqualto.  # noqa: E501
        :type: str
        """
        if left_operand is None:
            raise ValueError("Invalid value for `left_operand`, must not be `None`")  # noqa: E501

        self._left_operand = left_operand

    @property
    def right_operand(self):
        """Gets the right_operand of this RuleSchemaWhenEqualto.  # noqa: E501

        right operand  # noqa: E501

        :return: The right_operand of this RuleSchemaWhenEqualto.  # noqa: E501
        :rtype: str
        """
        return self._right_operand

    @right_operand.setter
    def right_operand(self, right_operand):
        """Sets the right_operand of this RuleSchemaWhenEqualto.

        right operand  # noqa: E501

        :param right_operand: The right_operand of this RuleSchemaWhenEqualto.  # noqa: E501
        :type: str
        """
        if right_operand is None:
            raise ValueError("Invalid value for `right_operand`, must not be `None`")  # noqa: E501

        self._right_operand = right_operand

    @property
    def time_range(self):
        """Gets the time_range of this RuleSchemaWhenEqualto.  # noqa: E501

        How much back in time should we look for data. Specify positive integer followed by s/m/h/d/w/y/o representing seconds/minutes/hours/days/weeks/years/offset. Eg: 2s  # noqa: E501

        :return: The time_range of this RuleSchemaWhenEqualto.  # noqa: E501
        :rtype: str
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this RuleSchemaWhenEqualto.

        How much back in time should we look for data. Specify positive integer followed by s/m/h/d/w/y/o representing seconds/minutes/hours/days/weeks/years/offset. Eg: 2s  # noqa: E501

        :param time_range: The time_range of this RuleSchemaWhenEqualto.  # noqa: E501
        :type: str
        """
        if time_range is not None and not re.search(r'^[1-9][0-9]*(o|s|m|h|d|w|y|offset)$', time_range):  # noqa: E501
            raise ValueError(r"Invalid value for `time_range`, must be a follow pattern or equal to `/^[1-9][0-9]*(o|s|m|h|d|w|y|offset)$/`")  # noqa: E501

        self._time_range = time_range

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
        if issubclass(RuleSchemaWhenEqualto, dict):
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
        if not isinstance(other, RuleSchemaWhenEqualto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
