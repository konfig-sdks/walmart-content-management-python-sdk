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
from pydantic import BaseModel, Field, RootModel

from walmart_content_management_python_sdk.pydantic.feeds_display_item_status_response_errors_item_causes_item import FeedsDisplayItemStatusResponseErrorsItemCausesItem

FeedsDisplayItemStatusResponseErrorsItemCauses = typing.List[FeedsDisplayItemStatusResponseErrorsItemCausesItem]
