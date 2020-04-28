# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: healthbot-hackers@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class LicenseApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_iceberg_add_license_from_file(self, license_file, **kwargs):  # noqa: E501
        """Add license from file.  # noqa: E501

        Add license keys from file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_iceberg_add_license_from_file(license_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file license_file: License key file content (required)
        :param str authorization: authentication header object
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_iceberg_add_license_from_file_with_http_info(license_file, **kwargs)  # noqa: E501
        else:
            (data) = self.create_iceberg_add_license_from_file_with_http_info(license_file, **kwargs)  # noqa: E501
            return data

    def create_iceberg_add_license_from_file_with_http_info(self, license_file, **kwargs):  # noqa: E501
        """Add license from file.  # noqa: E501

        Add license keys from file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_iceberg_add_license_from_file_with_http_info(license_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file license_file: License key file content (required)
        :param str authorization: authentication header object
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['license_file', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_iceberg_add_license_from_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'license_file' is set
        if ('license_file' not in params or
                params['license_file'] is None):
            raise ValueError("Missing the required parameter `license_file` when calling `create_iceberg_add_license_from_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'license_file' in params:
            local_var_files['license_file'] = params['license_file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/license/keys/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_iceberg_delete_all_license(self, **kwargs):  # noqa: E501
        """Delete all licenses.  # noqa: E501

        Delete all the previously added license keys.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_iceberg_delete_all_license(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: authentication header object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_iceberg_delete_all_license_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_iceberg_delete_all_license_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_iceberg_delete_all_license_with_http_info(self, **kwargs):  # noqa: E501
        """Delete all licenses.  # noqa: E501

        Delete all the previously added license keys.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_iceberg_delete_all_license_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: authentication header object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_iceberg_delete_all_license" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/license/keys/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_iceberg_delete_license_by_id(self, license_id, **kwargs):  # noqa: E501
        """Delete a license.  # noqa: E501

        Delete a license matching the license id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_iceberg_delete_license_by_id(license_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str license_id: License id (required)
        :param str authorization: authentication header object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_iceberg_delete_license_by_id_with_http_info(license_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_iceberg_delete_license_by_id_with_http_info(license_id, **kwargs)  # noqa: E501
            return data

    def delete_iceberg_delete_license_by_id_with_http_info(self, license_id, **kwargs):  # noqa: E501
        """Delete a license.  # noqa: E501

        Delete a license matching the license id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_iceberg_delete_license_by_id_with_http_info(license_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str license_id: License id (required)
        :param str authorization: authentication header object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['license_id', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_iceberg_delete_license_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'license_id' is set
        if ('license_id' not in params or
                params['license_id'] is None):
            raise ValueError("Missing the required parameter `license_id` when calling `delete_iceberg_delete_license_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'license_id' in params:
            path_params['license_id'] = params['license_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/license/key/{license_id}/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_iceberg_get_all_license_id(self, **kwargs):  # noqa: E501
        """List of available license id's.  # noqa: E501

        Get the list of all available license id's.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_iceberg_get_all_license_id(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: authentication header object
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_iceberg_get_all_license_id_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_iceberg_get_all_license_id_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_iceberg_get_all_license_id_with_http_info(self, **kwargs):  # noqa: E501
        """List of available license id's.  # noqa: E501

        Get the list of all available license id's.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_iceberg_get_all_license_id_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: authentication header object
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_iceberg_get_all_license_id" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/license/keys/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_iceberg_license_features_info(self, **kwargs):  # noqa: E501
        """Status of all the licensed features.  # noqa: E501

        Get the status of all the licensed features. Also provides the compliance info per feature  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_iceberg_license_features_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: authentication header object
        :return: LicenseFeaturesSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_iceberg_license_features_info_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_iceberg_license_features_info_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_iceberg_license_features_info_with_http_info(self, **kwargs):  # noqa: E501
        """Status of all the licensed features.  # noqa: E501

        Get the status of all the licensed features. Also provides the compliance info per feature  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_iceberg_license_features_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: authentication header object
        :return: LicenseFeaturesSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_iceberg_license_features_info" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/license/status/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LicenseFeaturesSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_iceberg_license_file_by_license_id(self, license_id, **kwargs):  # noqa: E501
        """Download license file.  # noqa: E501

        Download the specified license file based on license id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_iceberg_license_file_by_license_id(license_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str license_id: License id (required)
        :param str authorization: authentication header object
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_iceberg_license_file_by_license_id_with_http_info(license_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_iceberg_license_file_by_license_id_with_http_info(license_id, **kwargs)  # noqa: E501
            return data

    def retrieve_iceberg_license_file_by_license_id_with_http_info(self, license_id, **kwargs):  # noqa: E501
        """Download license file.  # noqa: E501

        Download the specified license file based on license id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_iceberg_license_file_by_license_id_with_http_info(license_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str license_id: License id (required)
        :param str authorization: authentication header object
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['license_id', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_iceberg_license_file_by_license_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'license_id' is set
        if ('license_id' not in params or
                params['license_id'] is None):
            raise ValueError("Missing the required parameter `license_id` when calling `retrieve_iceberg_license_file_by_license_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'license_id' in params:
            path_params['license_id'] = params['license_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/license/key/{license_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_iceberg_license_key_contents(self, **kwargs):  # noqa: E501
        """Get the contents of all licenses.  # noqa: E501

        Get the license key contents for all the available licenses.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_iceberg_license_key_contents(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: authentication header object
        :return: LicenseKeysSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_iceberg_license_key_contents_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_iceberg_license_key_contents_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_iceberg_license_key_contents_with_http_info(self, **kwargs):  # noqa: E501
        """Get the contents of all licenses.  # noqa: E501

        Get the license key contents for all the available licenses.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_iceberg_license_key_contents_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: authentication header object
        :return: LicenseKeysSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_iceberg_license_key_contents" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/license/keys/contents/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LicenseKeysSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_iceberg_license_key_contents_by_id(self, license_id, **kwargs):  # noqa: E501
        """Get the contents of a license.  # noqa: E501

        Get the license key contents by the license id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_iceberg_license_key_contents_by_id(license_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str license_id: License id (required)
        :param str authorization: authentication header object
        :return: LicenseKeySchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_iceberg_license_key_contents_by_id_with_http_info(license_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_iceberg_license_key_contents_by_id_with_http_info(license_id, **kwargs)  # noqa: E501
            return data

    def retrieve_iceberg_license_key_contents_by_id_with_http_info(self, license_id, **kwargs):  # noqa: E501
        """Get the contents of a license.  # noqa: E501

        Get the license key contents by the license id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_iceberg_license_key_contents_by_id_with_http_info(license_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str license_id: License id (required)
        :param str authorization: authentication header object
        :return: LicenseKeySchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['license_id', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_iceberg_license_key_contents_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'license_id' is set
        if ('license_id' not in params or
                params['license_id'] is None):
            raise ValueError("Missing the required parameter `license_id` when calling `retrieve_iceberg_license_key_contents_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'license_id' in params:
            path_params['license_id'] = params['license_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/license/key/{license_id}/contents/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LicenseKeySchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_iceberg_replace_license(self, license_raw_keys, **kwargs):  # noqa: E501
        """Update the license.  # noqa: E501

        Update existing license keys with the new one provided in this request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_iceberg_replace_license(license_raw_keys, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LicenseRawKeysSchema license_raw_keys: License raw keys contents (required)
        :param str authorization: authentication header object
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_iceberg_replace_license_with_http_info(license_raw_keys, **kwargs)  # noqa: E501
        else:
            (data) = self.update_iceberg_replace_license_with_http_info(license_raw_keys, **kwargs)  # noqa: E501
            return data

    def update_iceberg_replace_license_with_http_info(self, license_raw_keys, **kwargs):  # noqa: E501
        """Update the license.  # noqa: E501

        Update existing license keys with the new one provided in this request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_iceberg_replace_license_with_http_info(license_raw_keys, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LicenseRawKeysSchema license_raw_keys: License raw keys contents (required)
        :param str authorization: authentication header object
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['license_raw_keys', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_iceberg_replace_license" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'license_raw_keys' is set
        if ('license_raw_keys' not in params or
                params['license_raw_keys'] is None):
            raise ValueError("Missing the required parameter `license_raw_keys` when calling `update_iceberg_replace_license`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'license_raw_keys' in params:
            body_params = params['license_raw_keys']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/license/keys/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
