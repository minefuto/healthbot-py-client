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


class DevicegroupSchemaAuthenticationSsl(object):
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
        'ca_profile': 'str',
        'local_certificate': 'str',
        'server_common_name': 'str'
    }

    attribute_map = {
        'ca_profile': 'ca-profile',
        'local_certificate': 'local-certificate',
        'server_common_name': 'server-common-name'
    }

    def __init__(self, ca_profile=None, local_certificate=None, server_common_name=None):  # noqa: E501
        """DevicegroupSchemaAuthenticationSsl - a model defined in Swagger"""  # noqa: E501

        self._ca_profile = None
        self._local_certificate = None
        self._server_common_name = None
        self.discriminator = None

        self.ca_profile = ca_profile
        if local_certificate is not None:
            self.local_certificate = local_certificate
        self.server_common_name = server_common_name

    @property
    def ca_profile(self):
        """Gets the ca_profile of this DevicegroupSchemaAuthenticationSsl.  # noqa: E501

        Name of the ca-profile to be used  # noqa: E501

        :return: The ca_profile of this DevicegroupSchemaAuthenticationSsl.  # noqa: E501
        :rtype: str
        """
        return self._ca_profile

    @ca_profile.setter
    def ca_profile(self, ca_profile):
        """Sets the ca_profile of this DevicegroupSchemaAuthenticationSsl.

        Name of the ca-profile to be used  # noqa: E501

        :param ca_profile: The ca_profile of this DevicegroupSchemaAuthenticationSsl.  # noqa: E501
        :type: str
        """
        if ca_profile is None:
            raise ValueError("Invalid value for `ca_profile`, must not be `None`")  # noqa: E501

        self._ca_profile = ca_profile

    @property
    def local_certificate(self):
        """Gets the local_certificate of this DevicegroupSchemaAuthenticationSsl.  # noqa: E501

        Name of the local-certificate-profile to be used  # noqa: E501

        :return: The local_certificate of this DevicegroupSchemaAuthenticationSsl.  # noqa: E501
        :rtype: str
        """
        return self._local_certificate

    @local_certificate.setter
    def local_certificate(self, local_certificate):
        """Sets the local_certificate of this DevicegroupSchemaAuthenticationSsl.

        Name of the local-certificate-profile to be used  # noqa: E501

        :param local_certificate: The local_certificate of this DevicegroupSchemaAuthenticationSsl.  # noqa: E501
        :type: str
        """

        self._local_certificate = local_certificate

    @property
    def server_common_name(self):
        """Gets the server_common_name of this DevicegroupSchemaAuthenticationSsl.  # noqa: E501

        Common name used while creating server certificate  # noqa: E501

        :return: The server_common_name of this DevicegroupSchemaAuthenticationSsl.  # noqa: E501
        :rtype: str
        """
        return self._server_common_name

    @server_common_name.setter
    def server_common_name(self, server_common_name):
        """Sets the server_common_name of this DevicegroupSchemaAuthenticationSsl.

        Common name used while creating server certificate  # noqa: E501

        :param server_common_name: The server_common_name of this DevicegroupSchemaAuthenticationSsl.  # noqa: E501
        :type: str
        """
        if server_common_name is None:
            raise ValueError("Invalid value for `server_common_name`, must not be `None`")  # noqa: E501

        self._server_common_name = server_common_name

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
        if issubclass(DevicegroupSchemaAuthenticationSsl, dict):
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
        if not isinstance(other, DevicegroupSchemaAuthenticationSsl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
