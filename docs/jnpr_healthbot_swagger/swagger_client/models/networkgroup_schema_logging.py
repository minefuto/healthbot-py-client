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


class NetworkgroupSchemaLogging(object):
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
        'log_level': 'str',
        'non_sensor_rules': 'DevicegroupSchemaLoggingNonsensorrules',
        'reports_generation': 'DevicegroupSchemaLoggingReportsgeneration',
        'trigger_evaluation': 'DevicegroupSchemaLoggingTriggerevaluation',
        'ml_model_builder': 'DevicegroupSchemaLoggingMLmodelbuilder'
    }

    attribute_map = {
        'log_level': 'log-level',
        'non_sensor_rules': 'non-sensor-rules',
        'reports_generation': 'reports-generation',
        'trigger_evaluation': 'trigger-evaluation',
        'ml_model_builder': 'ML-model-builder'
    }

    def __init__(self, log_level=None, non_sensor_rules=None, reports_generation=None, trigger_evaluation=None, ml_model_builder=None):  # noqa: E501
        """NetworkgroupSchemaLogging - a model defined in Swagger"""  # noqa: E501

        self._log_level = None
        self._non_sensor_rules = None
        self._reports_generation = None
        self._trigger_evaluation = None
        self._ml_model_builder = None
        self.discriminator = None

        if log_level is not None:
            self.log_level = log_level
        if non_sensor_rules is not None:
            self.non_sensor_rules = non_sensor_rules
        if reports_generation is not None:
            self.reports_generation = reports_generation
        if trigger_evaluation is not None:
            self.trigger_evaluation = trigger_evaluation
        if ml_model_builder is not None:
            self.ml_model_builder = ml_model_builder

    @property
    def log_level(self):
        """Gets the log_level of this NetworkgroupSchemaLogging.  # noqa: E501

        Global log level  # noqa: E501

        :return: The log_level of this NetworkgroupSchemaLogging.  # noqa: E501
        :rtype: str
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        """Sets the log_level of this NetworkgroupSchemaLogging.

        Global log level  # noqa: E501

        :param log_level: The log_level of this NetworkgroupSchemaLogging.  # noqa: E501
        :type: str
        """
        allowed_values = ["error", "debug", "warn", "info"]  # noqa: E501
        if log_level not in allowed_values:
            raise ValueError(
                "Invalid value for `log_level` ({0}), must be one of {1}"  # noqa: E501
                .format(log_level, allowed_values)
            )

        self._log_level = log_level

    @property
    def non_sensor_rules(self):
        """Gets the non_sensor_rules of this NetworkgroupSchemaLogging.  # noqa: E501


        :return: The non_sensor_rules of this NetworkgroupSchemaLogging.  # noqa: E501
        :rtype: DevicegroupSchemaLoggingNonsensorrules
        """
        return self._non_sensor_rules

    @non_sensor_rules.setter
    def non_sensor_rules(self, non_sensor_rules):
        """Sets the non_sensor_rules of this NetworkgroupSchemaLogging.


        :param non_sensor_rules: The non_sensor_rules of this NetworkgroupSchemaLogging.  # noqa: E501
        :type: DevicegroupSchemaLoggingNonsensorrules
        """

        self._non_sensor_rules = non_sensor_rules

    @property
    def reports_generation(self):
        """Gets the reports_generation of this NetworkgroupSchemaLogging.  # noqa: E501


        :return: The reports_generation of this NetworkgroupSchemaLogging.  # noqa: E501
        :rtype: DevicegroupSchemaLoggingReportsgeneration
        """
        return self._reports_generation

    @reports_generation.setter
    def reports_generation(self, reports_generation):
        """Sets the reports_generation of this NetworkgroupSchemaLogging.


        :param reports_generation: The reports_generation of this NetworkgroupSchemaLogging.  # noqa: E501
        :type: DevicegroupSchemaLoggingReportsgeneration
        """

        self._reports_generation = reports_generation

    @property
    def trigger_evaluation(self):
        """Gets the trigger_evaluation of this NetworkgroupSchemaLogging.  # noqa: E501


        :return: The trigger_evaluation of this NetworkgroupSchemaLogging.  # noqa: E501
        :rtype: DevicegroupSchemaLoggingTriggerevaluation
        """
        return self._trigger_evaluation

    @trigger_evaluation.setter
    def trigger_evaluation(self, trigger_evaluation):
        """Sets the trigger_evaluation of this NetworkgroupSchemaLogging.


        :param trigger_evaluation: The trigger_evaluation of this NetworkgroupSchemaLogging.  # noqa: E501
        :type: DevicegroupSchemaLoggingTriggerevaluation
        """

        self._trigger_evaluation = trigger_evaluation

    @property
    def ml_model_builder(self):
        """Gets the ml_model_builder of this NetworkgroupSchemaLogging.  # noqa: E501


        :return: The ml_model_builder of this NetworkgroupSchemaLogging.  # noqa: E501
        :rtype: DevicegroupSchemaLoggingMLmodelbuilder
        """
        return self._ml_model_builder

    @ml_model_builder.setter
    def ml_model_builder(self, ml_model_builder):
        """Sets the ml_model_builder of this NetworkgroupSchemaLogging.


        :param ml_model_builder: The ml_model_builder of this NetworkgroupSchemaLogging.  # noqa: E501
        :type: DevicegroupSchemaLoggingMLmodelbuilder
        """

        self._ml_model_builder = ml_model_builder

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
        if issubclass(NetworkgroupSchemaLogging, dict):
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
        if not isinstance(other, NetworkgroupSchemaLogging):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
