# coding: utf-8

"""
    Content Management

    The content management feed allows you to process content for items in bulk. You can take in content via the content feeds. Use the XSDs to manage content.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from walmart_content_management_python_sdk import schemas  # noqa: F401


class FeedsGetFeedStatusResponseErrorsItemCauses(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['FeedsGetFeedStatusResponseErrorsItemCausesItem']:
            return FeedsGetFeedStatusResponseErrorsItemCausesItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['FeedsGetFeedStatusResponseErrorsItemCausesItem'], typing.List['FeedsGetFeedStatusResponseErrorsItemCausesItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FeedsGetFeedStatusResponseErrorsItemCauses':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'FeedsGetFeedStatusResponseErrorsItemCausesItem':
        return super().__getitem__(i)

from walmart_content_management_python_sdk.model.feeds_get_feed_status_response_errors_item_causes_item import FeedsGetFeedStatusResponseErrorsItemCausesItem
