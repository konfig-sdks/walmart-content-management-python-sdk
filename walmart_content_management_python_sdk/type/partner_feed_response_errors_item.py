# coding: utf-8

"""
    Content Management

    The content management feed allows you to process content for items in bulk. You can take in content via the content feeds. Use the XSDs to manage content.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from walmart_content_management_python_sdk.type.partner_feed_response_errors_item_causes import PartnerFeedResponseErrorsItemCauses
from walmart_content_management_python_sdk.type.partner_feed_response_errors_item_error_identifiers import PartnerFeedResponseErrorsItemErrorIdentifiers

class RequiredPartnerFeedResponseErrorsItem(TypedDict):
    code: str

class OptionalPartnerFeedResponseErrorsItem(TypedDict, total=False):
    info: str

    description: str

    field: str

    severity: str

    category: str

    causes: PartnerFeedResponseErrorsItemCauses

    errorIdentifiers: PartnerFeedResponseErrorsItemErrorIdentifiers

    component: str

    type: str

    serviceName: str

    gatewayErrorCategory: str

class PartnerFeedResponseErrorsItem(RequiredPartnerFeedResponseErrorsItem, OptionalPartnerFeedResponseErrorsItem):
    pass