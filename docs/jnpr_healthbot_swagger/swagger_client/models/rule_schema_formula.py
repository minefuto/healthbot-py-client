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


class RuleSchemaFormula(object):
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
        'anomaly_detection': 'RuleSchemaFormulaAnomalydetection',
        'count': 'RuleSchemaFormulaCount',
        'dynamic_threshold': 'RuleSchemaFormulaDynamicthreshold',
        'max': 'RuleSchemaFormulaMax',
        'mean': 'RuleSchemaFormulaMean',
        'microburst': 'RuleSchemaFormulaMicroburst',
        'min': 'RuleSchemaFormulaMin',
        'outlier_detection': 'RuleSchemaFormulaOutlierdetection',
        'predict': 'RuleSchemaFormulaPredict',
        'rate_of_change': 'RuleSchemaFormulaRateofchange',
        'stddev': 'RuleSchemaFormulaStddev',
        'sum': 'RuleSchemaFormulaSum',
        'user_defined_function': 'RuleSchemaFormulaUserdefinedfunction'
    }

    attribute_map = {
        'anomaly_detection': 'anomaly-detection',
        'count': 'count',
        'dynamic_threshold': 'dynamic-threshold',
        'max': 'max',
        'mean': 'mean',
        'microburst': 'microburst',
        'min': 'min',
        'outlier_detection': 'outlier-detection',
        'predict': 'predict',
        'rate_of_change': 'rate-of-change',
        'stddev': 'stddev',
        'sum': 'sum',
        'user_defined_function': 'user-defined-function'
    }

    def __init__(self, anomaly_detection=None, count=None, dynamic_threshold=None, max=None, mean=None, microburst=None, min=None, outlier_detection=None, predict=None, rate_of_change=None, stddev=None, sum=None, user_defined_function=None):  # noqa: E501
        """RuleSchemaFormula - a model defined in Swagger"""  # noqa: E501

        self._anomaly_detection = None
        self._count = None
        self._dynamic_threshold = None
        self._max = None
        self._mean = None
        self._microburst = None
        self._min = None
        self._outlier_detection = None
        self._predict = None
        self._rate_of_change = None
        self._stddev = None
        self._sum = None
        self._user_defined_function = None
        self.discriminator = None

        if anomaly_detection is not None:
            self.anomaly_detection = anomaly_detection
        if count is not None:
            self.count = count
        if dynamic_threshold is not None:
            self.dynamic_threshold = dynamic_threshold
        if max is not None:
            self.max = max
        if mean is not None:
            self.mean = mean
        if microburst is not None:
            self.microburst = microburst
        if min is not None:
            self.min = min
        if outlier_detection is not None:
            self.outlier_detection = outlier_detection
        if predict is not None:
            self.predict = predict
        if rate_of_change is not None:
            self.rate_of_change = rate_of_change
        if stddev is not None:
            self.stddev = stddev
        if sum is not None:
            self.sum = sum
        if user_defined_function is not None:
            self.user_defined_function = user_defined_function

    @property
    def anomaly_detection(self):
        """Gets the anomaly_detection of this RuleSchemaFormula.  # noqa: E501


        :return: The anomaly_detection of this RuleSchemaFormula.  # noqa: E501
        :rtype: RuleSchemaFormulaAnomalydetection
        """
        return self._anomaly_detection

    @anomaly_detection.setter
    def anomaly_detection(self, anomaly_detection):
        """Sets the anomaly_detection of this RuleSchemaFormula.


        :param anomaly_detection: The anomaly_detection of this RuleSchemaFormula.  # noqa: E501
        :type: RuleSchemaFormulaAnomalydetection
        """

        self._anomaly_detection = anomaly_detection

    @property
    def count(self):
        """Gets the count of this RuleSchemaFormula.  # noqa: E501


        :return: The count of this RuleSchemaFormula.  # noqa: E501
        :rtype: RuleSchemaFormulaCount
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this RuleSchemaFormula.


        :param count: The count of this RuleSchemaFormula.  # noqa: E501
        :type: RuleSchemaFormulaCount
        """

        self._count = count

    @property
    def dynamic_threshold(self):
        """Gets the dynamic_threshold of this RuleSchemaFormula.  # noqa: E501


        :return: The dynamic_threshold of this RuleSchemaFormula.  # noqa: E501
        :rtype: RuleSchemaFormulaDynamicthreshold
        """
        return self._dynamic_threshold

    @dynamic_threshold.setter
    def dynamic_threshold(self, dynamic_threshold):
        """Sets the dynamic_threshold of this RuleSchemaFormula.


        :param dynamic_threshold: The dynamic_threshold of this RuleSchemaFormula.  # noqa: E501
        :type: RuleSchemaFormulaDynamicthreshold
        """

        self._dynamic_threshold = dynamic_threshold

    @property
    def max(self):
        """Gets the max of this RuleSchemaFormula.  # noqa: E501


        :return: The max of this RuleSchemaFormula.  # noqa: E501
        :rtype: RuleSchemaFormulaMax
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this RuleSchemaFormula.


        :param max: The max of this RuleSchemaFormula.  # noqa: E501
        :type: RuleSchemaFormulaMax
        """

        self._max = max

    @property
    def mean(self):
        """Gets the mean of this RuleSchemaFormula.  # noqa: E501


        :return: The mean of this RuleSchemaFormula.  # noqa: E501
        :rtype: RuleSchemaFormulaMean
        """
        return self._mean

    @mean.setter
    def mean(self, mean):
        """Sets the mean of this RuleSchemaFormula.


        :param mean: The mean of this RuleSchemaFormula.  # noqa: E501
        :type: RuleSchemaFormulaMean
        """

        self._mean = mean

    @property
    def microburst(self):
        """Gets the microburst of this RuleSchemaFormula.  # noqa: E501


        :return: The microburst of this RuleSchemaFormula.  # noqa: E501
        :rtype: RuleSchemaFormulaMicroburst
        """
        return self._microburst

    @microburst.setter
    def microburst(self, microburst):
        """Sets the microburst of this RuleSchemaFormula.


        :param microburst: The microburst of this RuleSchemaFormula.  # noqa: E501
        :type: RuleSchemaFormulaMicroburst
        """

        self._microburst = microburst

    @property
    def min(self):
        """Gets the min of this RuleSchemaFormula.  # noqa: E501


        :return: The min of this RuleSchemaFormula.  # noqa: E501
        :rtype: RuleSchemaFormulaMin
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this RuleSchemaFormula.


        :param min: The min of this RuleSchemaFormula.  # noqa: E501
        :type: RuleSchemaFormulaMin
        """

        self._min = min

    @property
    def outlier_detection(self):
        """Gets the outlier_detection of this RuleSchemaFormula.  # noqa: E501


        :return: The outlier_detection of this RuleSchemaFormula.  # noqa: E501
        :rtype: RuleSchemaFormulaOutlierdetection
        """
        return self._outlier_detection

    @outlier_detection.setter
    def outlier_detection(self, outlier_detection):
        """Sets the outlier_detection of this RuleSchemaFormula.


        :param outlier_detection: The outlier_detection of this RuleSchemaFormula.  # noqa: E501
        :type: RuleSchemaFormulaOutlierdetection
        """

        self._outlier_detection = outlier_detection

    @property
    def predict(self):
        """Gets the predict of this RuleSchemaFormula.  # noqa: E501


        :return: The predict of this RuleSchemaFormula.  # noqa: E501
        :rtype: RuleSchemaFormulaPredict
        """
        return self._predict

    @predict.setter
    def predict(self, predict):
        """Sets the predict of this RuleSchemaFormula.


        :param predict: The predict of this RuleSchemaFormula.  # noqa: E501
        :type: RuleSchemaFormulaPredict
        """

        self._predict = predict

    @property
    def rate_of_change(self):
        """Gets the rate_of_change of this RuleSchemaFormula.  # noqa: E501


        :return: The rate_of_change of this RuleSchemaFormula.  # noqa: E501
        :rtype: RuleSchemaFormulaRateofchange
        """
        return self._rate_of_change

    @rate_of_change.setter
    def rate_of_change(self, rate_of_change):
        """Sets the rate_of_change of this RuleSchemaFormula.


        :param rate_of_change: The rate_of_change of this RuleSchemaFormula.  # noqa: E501
        :type: RuleSchemaFormulaRateofchange
        """

        self._rate_of_change = rate_of_change

    @property
    def stddev(self):
        """Gets the stddev of this RuleSchemaFormula.  # noqa: E501


        :return: The stddev of this RuleSchemaFormula.  # noqa: E501
        :rtype: RuleSchemaFormulaStddev
        """
        return self._stddev

    @stddev.setter
    def stddev(self, stddev):
        """Sets the stddev of this RuleSchemaFormula.


        :param stddev: The stddev of this RuleSchemaFormula.  # noqa: E501
        :type: RuleSchemaFormulaStddev
        """

        self._stddev = stddev

    @property
    def sum(self):
        """Gets the sum of this RuleSchemaFormula.  # noqa: E501


        :return: The sum of this RuleSchemaFormula.  # noqa: E501
        :rtype: RuleSchemaFormulaSum
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        """Sets the sum of this RuleSchemaFormula.


        :param sum: The sum of this RuleSchemaFormula.  # noqa: E501
        :type: RuleSchemaFormulaSum
        """

        self._sum = sum

    @property
    def user_defined_function(self):
        """Gets the user_defined_function of this RuleSchemaFormula.  # noqa: E501


        :return: The user_defined_function of this RuleSchemaFormula.  # noqa: E501
        :rtype: RuleSchemaFormulaUserdefinedfunction
        """
        return self._user_defined_function

    @user_defined_function.setter
    def user_defined_function(self, user_defined_function):
        """Sets the user_defined_function of this RuleSchemaFormula.


        :param user_defined_function: The user_defined_function of this RuleSchemaFormula.  # noqa: E501
        :type: RuleSchemaFormulaUserdefinedfunction
        """

        self._user_defined_function = user_defined_function

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
        if issubclass(RuleSchemaFormula, dict):
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
        if not isinstance(other, RuleSchemaFormula):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
