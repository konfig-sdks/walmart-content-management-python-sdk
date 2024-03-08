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

from walmart_content_management_python_sdk.pydantic.feed_record_response_errors import FeedRecordResponseErrors
from walmart_content_management_python_sdk.pydantic.feed_record_response_results import FeedRecordResponseResults

class FeedRecordResponse(BaseModel):
    errors: typing.Optional[FeedRecordResponseErrors] = Field(None, alias='errors')

    # Total number of feeds returned
    total_results: typing.Optional[int] = Field(None, alias='totalResults')

    # The object response to the starting number, where 0 is the first available
    offset: typing.Optional[int] = Field(None, alias='offset')

    # The number of items to be returned
    limit: typing.Optional[int] = Field(None, alias='limit')

    results: typing.Optional[FeedRecordResponseResults] = Field(None, alias='results')
    class Config:
        arbitrary_types_allowed = True