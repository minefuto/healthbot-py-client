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


class RuleSchemaRulepropertiesSupporteddevicesJuniperOperatingsystem(object):
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
        'os_name': 'str',
        'products': 'list[RuleSchemaRulepropertiesSupporteddevicesJuniperProducts]'
    }

    attribute_map = {
        'os_name': 'os-name',
        'products': 'products'
    }

    def __init__(self, os_name=None, products=None):  # noqa: E501
        """RuleSchemaRulepropertiesSupporteddevicesJuniperOperatingsystem - a model defined in Swagger"""  # noqa: E501

        self._os_name = None
        self._products = None
        self.discriminator = None

        self.os_name = os_name
        if products is not None:
            self.products = products

    @property
    def os_name(self):
        """Gets the os_name of this RuleSchemaRulepropertiesSupporteddevicesJuniperOperatingsystem.  # noqa: E501


        :return: The os_name of this RuleSchemaRulepropertiesSupporteddevicesJuniperOperatingsystem.  # noqa: E501
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """Sets the os_name of this RuleSchemaRulepropertiesSupporteddevicesJuniperOperatingsystem.


        :param os_name: The os_name of this RuleSchemaRulepropertiesSupporteddevicesJuniperOperatingsystem.  # noqa: E501
        :type: str
        """
        if os_name is None:
            raise ValueError("Invalid value for `os_name`, must not be `None`")  # noqa: E501
        allowed_values = ["junos", "junosEvolved"]  # noqa: E501
        if os_name not in allowed_values:
            raise ValueError(
                "Invalid value for `os_name` ({0}), must be one of {1}"  # noqa: E501
                .format(os_name, allowed_values)
            )

        self._os_name = os_name

    @property
    def products(self):
        """Gets the products of this RuleSchemaRulepropertiesSupporteddevicesJuniperOperatingsystem.  # noqa: E501


        :return: The products of this RuleSchemaRulepropertiesSupporteddevicesJuniperOperatingsystem.  # noqa: E501
        :rtype: list[RuleSchemaRulepropertiesSupporteddevicesJuniperProducts]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this RuleSchemaRulepropertiesSupporteddevicesJuniperOperatingsystem.


        :param products: The products of this RuleSchemaRulepropertiesSupporteddevicesJuniperOperatingsystem.  # noqa: E501
        :type: list[RuleSchemaRulepropertiesSupporteddevicesJuniperProducts]
        """

        self._products = products

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
        if issubclass(RuleSchemaRulepropertiesSupporteddevicesJuniperOperatingsystem, dict):
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
        if not isinstance(other, RuleSchemaRulepropertiesSupporteddevicesJuniperOperatingsystem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
