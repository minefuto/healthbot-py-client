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


class RuleSchemaWhen(object):
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
        'does_not_match_with': 'list[RuleSchemaWhenDoesnotmatchwith]',
        'equal_to': 'list[RuleSchemaWhenEqualto]',
        'exists': 'list[RuleSchemaWhenExists]',
        'greater_than': 'list[RuleSchemaWhenEqualto]',
        'greater_than_or_equal_to': 'list[RuleSchemaWhenEqualto]',
        'increasing_at_least_by_rate': 'list[RuleSchemaWhenIncreasingatleastbyrate]',
        'increasing_at_least_by_value': 'list[RuleSchemaWhenIncreasingatleastbyvalue]',
        'increasing_at_most_by_rate': 'list[RuleSchemaWhenIncreasingatleastbyrate]',
        'increasing_at_most_by_value': 'list[RuleSchemaWhenIncreasingatleastbyvalue]',
        'less_than': 'list[RuleSchemaWhenEqualto]',
        'less_than_or_equal_to': 'list[RuleSchemaWhenEqualto]',
        'matches_with': 'list[RuleSchemaWhenDoesnotmatchwith]',
        'max_rate_of_increase': 'list[RuleSchemaWhenMaxrateofincrease]',
        'min_rate_of_increase': 'list[RuleSchemaWhenMaxrateofincrease]',
        'not_equal_to': 'list[RuleSchemaWhenEqualto]',
        'range': 'list[RuleSchemaWhenRange]',
        'user_defined_function': 'list[RuleSchemaWhenUserdefinedfunction]'
    }

    attribute_map = {
        'does_not_match_with': 'does-not-match-with',
        'equal_to': 'equal-to',
        'exists': 'exists',
        'greater_than': 'greater-than',
        'greater_than_or_equal_to': 'greater-than-or-equal-to',
        'increasing_at_least_by_rate': 'increasing-at-least-by-rate',
        'increasing_at_least_by_value': 'increasing-at-least-by-value',
        'increasing_at_most_by_rate': 'increasing-at-most-by-rate',
        'increasing_at_most_by_value': 'increasing-at-most-by-value',
        'less_than': 'less-than',
        'less_than_or_equal_to': 'less-than-or-equal-to',
        'matches_with': 'matches-with',
        'max_rate_of_increase': 'max-rate-of-increase',
        'min_rate_of_increase': 'min-rate-of-increase',
        'not_equal_to': 'not-equal-to',
        'range': 'range',
        'user_defined_function': 'user-defined-function'
    }

    def __init__(self, does_not_match_with=None, equal_to=None, exists=None, greater_than=None, greater_than_or_equal_to=None, increasing_at_least_by_rate=None, increasing_at_least_by_value=None, increasing_at_most_by_rate=None, increasing_at_most_by_value=None, less_than=None, less_than_or_equal_to=None, matches_with=None, max_rate_of_increase=None, min_rate_of_increase=None, not_equal_to=None, range=None, user_defined_function=None):  # noqa: E501
        """RuleSchemaWhen - a model defined in Swagger"""  # noqa: E501

        self._does_not_match_with = None
        self._equal_to = None
        self._exists = None
        self._greater_than = None
        self._greater_than_or_equal_to = None
        self._increasing_at_least_by_rate = None
        self._increasing_at_least_by_value = None
        self._increasing_at_most_by_rate = None
        self._increasing_at_most_by_value = None
        self._less_than = None
        self._less_than_or_equal_to = None
        self._matches_with = None
        self._max_rate_of_increase = None
        self._min_rate_of_increase = None
        self._not_equal_to = None
        self._range = None
        self._user_defined_function = None
        self.discriminator = None

        if does_not_match_with is not None:
            self.does_not_match_with = does_not_match_with
        if equal_to is not None:
            self.equal_to = equal_to
        if exists is not None:
            self.exists = exists
        if greater_than is not None:
            self.greater_than = greater_than
        if greater_than_or_equal_to is not None:
            self.greater_than_or_equal_to = greater_than_or_equal_to
        if increasing_at_least_by_rate is not None:
            self.increasing_at_least_by_rate = increasing_at_least_by_rate
        if increasing_at_least_by_value is not None:
            self.increasing_at_least_by_value = increasing_at_least_by_value
        if increasing_at_most_by_rate is not None:
            self.increasing_at_most_by_rate = increasing_at_most_by_rate
        if increasing_at_most_by_value is not None:
            self.increasing_at_most_by_value = increasing_at_most_by_value
        if less_than is not None:
            self.less_than = less_than
        if less_than_or_equal_to is not None:
            self.less_than_or_equal_to = less_than_or_equal_to
        if matches_with is not None:
            self.matches_with = matches_with
        if max_rate_of_increase is not None:
            self.max_rate_of_increase = max_rate_of_increase
        if min_rate_of_increase is not None:
            self.min_rate_of_increase = min_rate_of_increase
        if not_equal_to is not None:
            self.not_equal_to = not_equal_to
        if range is not None:
            self.range = range
        if user_defined_function is not None:
            self.user_defined_function = user_defined_function

    @property
    def does_not_match_with(self):
        """Gets the does_not_match_with of this RuleSchemaWhen.  # noqa: E501


        :return: The does_not_match_with of this RuleSchemaWhen.  # noqa: E501
        :rtype: list[RuleSchemaWhenDoesnotmatchwith]
        """
        return self._does_not_match_with

    @does_not_match_with.setter
    def does_not_match_with(self, does_not_match_with):
        """Sets the does_not_match_with of this RuleSchemaWhen.


        :param does_not_match_with: The does_not_match_with of this RuleSchemaWhen.  # noqa: E501
        :type: list[RuleSchemaWhenDoesnotmatchwith]
        """

        self._does_not_match_with = does_not_match_with

    @property
    def equal_to(self):
        """Gets the equal_to of this RuleSchemaWhen.  # noqa: E501


        :return: The equal_to of this RuleSchemaWhen.  # noqa: E501
        :rtype: list[RuleSchemaWhenEqualto]
        """
        return self._equal_to

    @equal_to.setter
    def equal_to(self, equal_to):
        """Sets the equal_to of this RuleSchemaWhen.


        :param equal_to: The equal_to of this RuleSchemaWhen.  # noqa: E501
        :type: list[RuleSchemaWhenEqualto]
        """

        self._equal_to = equal_to

    @property
    def exists(self):
        """Gets the exists of this RuleSchemaWhen.  # noqa: E501


        :return: The exists of this RuleSchemaWhen.  # noqa: E501
        :rtype: list[RuleSchemaWhenExists]
        """
        return self._exists

    @exists.setter
    def exists(self, exists):
        """Sets the exists of this RuleSchemaWhen.


        :param exists: The exists of this RuleSchemaWhen.  # noqa: E501
        :type: list[RuleSchemaWhenExists]
        """

        self._exists = exists

    @property
    def greater_than(self):
        """Gets the greater_than of this RuleSchemaWhen.  # noqa: E501


        :return: The greater_than of this RuleSchemaWhen.  # noqa: E501
        :rtype: list[RuleSchemaWhenEqualto]
        """
        return self._greater_than

    @greater_than.setter
    def greater_than(self, greater_than):
        """Sets the greater_than of this RuleSchemaWhen.


        :param greater_than: The greater_than of this RuleSchemaWhen.  # noqa: E501
        :type: list[RuleSchemaWhenEqualto]
        """

        self._greater_than = greater_than

    @property
    def greater_than_or_equal_to(self):
        """Gets the greater_than_or_equal_to of this RuleSchemaWhen.  # noqa: E501


        :return: The greater_than_or_equal_to of this RuleSchemaWhen.  # noqa: E501
        :rtype: list[RuleSchemaWhenEqualto]
        """
        return self._greater_than_or_equal_to

    @greater_than_or_equal_to.setter
    def greater_than_or_equal_to(self, greater_than_or_equal_to):
        """Sets the greater_than_or_equal_to of this RuleSchemaWhen.


        :param greater_than_or_equal_to: The greater_than_or_equal_to of this RuleSchemaWhen.  # noqa: E501
        :type: list[RuleSchemaWhenEqualto]
        """

        self._greater_than_or_equal_to = greater_than_or_equal_to

    @property
    def increasing_at_least_by_rate(self):
        """Gets the increasing_at_least_by_rate of this RuleSchemaWhen.  # noqa: E501

        Rate of increase between successive values is at least given rate  # noqa: E501

        :return: The increasing_at_least_by_rate of this RuleSchemaWhen.  # noqa: E501
        :rtype: list[RuleSchemaWhenIncreasingatleastbyrate]
        """
        return self._increasing_at_least_by_rate

    @increasing_at_least_by_rate.setter
    def increasing_at_least_by_rate(self, increasing_at_least_by_rate):
        """Sets the increasing_at_least_by_rate of this RuleSchemaWhen.

        Rate of increase between successive values is at least given rate  # noqa: E501

        :param increasing_at_least_by_rate: The increasing_at_least_by_rate of this RuleSchemaWhen.  # noqa: E501
        :type: list[RuleSchemaWhenIncreasingatleastbyrate]
        """

        self._increasing_at_least_by_rate = increasing_at_least_by_rate

    @property
    def increasing_at_least_by_value(self):
        """Gets the increasing_at_least_by_value of this RuleSchemaWhen.  # noqa: E501

        Increase between successive values is at least given value  # noqa: E501

        :return: The increasing_at_least_by_value of this RuleSchemaWhen.  # noqa: E501
        :rtype: list[RuleSchemaWhenIncreasingatleastbyvalue]
        """
        return self._increasing_at_least_by_value

    @increasing_at_least_by_value.setter
    def increasing_at_least_by_value(self, increasing_at_least_by_value):
        """Sets the increasing_at_least_by_value of this RuleSchemaWhen.

        Increase between successive values is at least given value  # noqa: E501

        :param increasing_at_least_by_value: The increasing_at_least_by_value of this RuleSchemaWhen.  # noqa: E501
        :type: list[RuleSchemaWhenIncreasingatleastbyvalue]
        """

        self._increasing_at_least_by_value = increasing_at_least_by_value

    @property
    def increasing_at_most_by_rate(self):
        """Gets the increasing_at_most_by_rate of this RuleSchemaWhen.  # noqa: E501

        Rate of increase between successive values is at most given rate  # noqa: E501

        :return: The increasing_at_most_by_rate of this RuleSchemaWhen.  # noqa: E501
        :rtype: list[RuleSchemaWhenIncreasingatleastbyrate]
        """
        return self._increasing_at_most_by_rate

    @increasing_at_most_by_rate.setter
    def increasing_at_most_by_rate(self, increasing_at_most_by_rate):
        """Sets the increasing_at_most_by_rate of this RuleSchemaWhen.

        Rate of increase between successive values is at most given rate  # noqa: E501

        :param increasing_at_most_by_rate: The increasing_at_most_by_rate of this RuleSchemaWhen.  # noqa: E501
        :type: list[RuleSchemaWhenIncreasingatleastbyrate]
        """

        self._increasing_at_most_by_rate = increasing_at_most_by_rate

    @property
    def increasing_at_most_by_value(self):
        """Gets the increasing_at_most_by_value of this RuleSchemaWhen.  # noqa: E501

        Increase between successive values is at most given value  # noqa: E501

        :return: The increasing_at_most_by_value of this RuleSchemaWhen.  # noqa: E501
        :rtype: list[RuleSchemaWhenIncreasingatleastbyvalue]
        """
        return self._increasing_at_most_by_value

    @increasing_at_most_by_value.setter
    def increasing_at_most_by_value(self, increasing_at_most_by_value):
        """Sets the increasing_at_most_by_value of this RuleSchemaWhen.

        Increase between successive values is at most given value  # noqa: E501

        :param increasing_at_most_by_value: The increasing_at_most_by_value of this RuleSchemaWhen.  # noqa: E501
        :type: list[RuleSchemaWhenIncreasingatleastbyvalue]
        """

        self._increasing_at_most_by_value = increasing_at_most_by_value

    @property
    def less_than(self):
        """Gets the less_than of this RuleSchemaWhen.  # noqa: E501


        :return: The less_than of this RuleSchemaWhen.  # noqa: E501
        :rtype: list[RuleSchemaWhenEqualto]
        """
        return self._less_than

    @less_than.setter
    def less_than(self, less_than):
        """Sets the less_than of this RuleSchemaWhen.


        :param less_than: The less_than of this RuleSchemaWhen.  # noqa: E501
        :type: list[RuleSchemaWhenEqualto]
        """

        self._less_than = less_than

    @property
    def less_than_or_equal_to(self):
        """Gets the less_than_or_equal_to of this RuleSchemaWhen.  # noqa: E501


        :return: The less_than_or_equal_to of this RuleSchemaWhen.  # noqa: E501
        :rtype: list[RuleSchemaWhenEqualto]
        """
        return self._less_than_or_equal_to

    @less_than_or_equal_to.setter
    def less_than_or_equal_to(self, less_than_or_equal_to):
        """Sets the less_than_or_equal_to of this RuleSchemaWhen.


        :param less_than_or_equal_to: The less_than_or_equal_to of this RuleSchemaWhen.  # noqa: E501
        :type: list[RuleSchemaWhenEqualto]
        """

        self._less_than_or_equal_to = less_than_or_equal_to

    @property
    def matches_with(self):
        """Gets the matches_with of this RuleSchemaWhen.  # noqa: E501


        :return: The matches_with of this RuleSchemaWhen.  # noqa: E501
        :rtype: list[RuleSchemaWhenDoesnotmatchwith]
        """
        return self._matches_with

    @matches_with.setter
    def matches_with(self, matches_with):
        """Sets the matches_with of this RuleSchemaWhen.


        :param matches_with: The matches_with of this RuleSchemaWhen.  # noqa: E501
        :type: list[RuleSchemaWhenDoesnotmatchwith]
        """

        self._matches_with = matches_with

    @property
    def max_rate_of_increase(self):
        """Gets the max_rate_of_increase of this RuleSchemaWhen.  # noqa: E501


        :return: The max_rate_of_increase of this RuleSchemaWhen.  # noqa: E501
        :rtype: list[RuleSchemaWhenMaxrateofincrease]
        """
        return self._max_rate_of_increase

    @max_rate_of_increase.setter
    def max_rate_of_increase(self, max_rate_of_increase):
        """Sets the max_rate_of_increase of this RuleSchemaWhen.


        :param max_rate_of_increase: The max_rate_of_increase of this RuleSchemaWhen.  # noqa: E501
        :type: list[RuleSchemaWhenMaxrateofincrease]
        """

        self._max_rate_of_increase = max_rate_of_increase

    @property
    def min_rate_of_increase(self):
        """Gets the min_rate_of_increase of this RuleSchemaWhen.  # noqa: E501


        :return: The min_rate_of_increase of this RuleSchemaWhen.  # noqa: E501
        :rtype: list[RuleSchemaWhenMaxrateofincrease]
        """
        return self._min_rate_of_increase

    @min_rate_of_increase.setter
    def min_rate_of_increase(self, min_rate_of_increase):
        """Sets the min_rate_of_increase of this RuleSchemaWhen.


        :param min_rate_of_increase: The min_rate_of_increase of this RuleSchemaWhen.  # noqa: E501
        :type: list[RuleSchemaWhenMaxrateofincrease]
        """

        self._min_rate_of_increase = min_rate_of_increase

    @property
    def not_equal_to(self):
        """Gets the not_equal_to of this RuleSchemaWhen.  # noqa: E501


        :return: The not_equal_to of this RuleSchemaWhen.  # noqa: E501
        :rtype: list[RuleSchemaWhenEqualto]
        """
        return self._not_equal_to

    @not_equal_to.setter
    def not_equal_to(self, not_equal_to):
        """Sets the not_equal_to of this RuleSchemaWhen.


        :param not_equal_to: The not_equal_to of this RuleSchemaWhen.  # noqa: E501
        :type: list[RuleSchemaWhenEqualto]
        """

        self._not_equal_to = not_equal_to

    @property
    def range(self):
        """Gets the range of this RuleSchemaWhen.  # noqa: E501


        :return: The range of this RuleSchemaWhen.  # noqa: E501
        :rtype: list[RuleSchemaWhenRange]
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this RuleSchemaWhen.


        :param range: The range of this RuleSchemaWhen.  # noqa: E501
        :type: list[RuleSchemaWhenRange]
        """

        self._range = range

    @property
    def user_defined_function(self):
        """Gets the user_defined_function of this RuleSchemaWhen.  # noqa: E501


        :return: The user_defined_function of this RuleSchemaWhen.  # noqa: E501
        :rtype: list[RuleSchemaWhenUserdefinedfunction]
        """
        return self._user_defined_function

    @user_defined_function.setter
    def user_defined_function(self, user_defined_function):
        """Sets the user_defined_function of this RuleSchemaWhen.


        :param user_defined_function: The user_defined_function of this RuleSchemaWhen.  # noqa: E501
        :type: list[RuleSchemaWhenUserdefinedfunction]
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
        if issubclass(RuleSchemaWhen, dict):
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
        if not isinstance(other, RuleSchemaWhen):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
