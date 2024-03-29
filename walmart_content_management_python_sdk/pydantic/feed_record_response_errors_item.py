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

from walmart_content_management_python_sdk.pydantic.feed_record_response_errors_item_causes import FeedRecordResponseErrorsItemCauses
from walmart_content_management_python_sdk.pydantic.feed_record_response_errors_item_error_identifiers import FeedRecordResponseErrorsItemErrorIdentifiers

class FeedRecordResponseErrorsItem(BaseModel):
    code: str = Field(alias='code')

    info: typing.Optional[str] = Field(None, alias='info')

    description: typing.Optional[str] = Field(None, alias='description')

    field: typing.Optional[str] = Field(None, alias='field')

    severity: typing.Optional[Literal["INFO", "WARN", "ERROR"]] = Field(None, alias='severity')

    category: typing.Optional[Literal["APPLICATION", "SYSTEM", "REQUEST", "DATA"]] = Field(None, alias='category')

    causes: typing.Optional[FeedRecordResponseErrorsItemCauses] = Field(None, alias='causes')

    error_identifiers: typing.Optional[FeedRecordResponseErrorsItemErrorIdentifiers] = Field(None, alias='errorIdentifiers')

    component: typing.Optional[str] = Field(None, alias='component')

    type: typing.Optional[str] = Field(None, alias='type')

    service_name: typing.Optional[str] = Field(None, alias='serviceName')

    gateway_error_category: typing.Optional[Literal["INTERNAL_DATA_ERROR", "EXTERNAL_DATA_ERROR", "SYSTEM_ERROR"]] = Field(None, alias='gatewayErrorCategory')
    class Config:
        arbitrary_types_allowed = True
