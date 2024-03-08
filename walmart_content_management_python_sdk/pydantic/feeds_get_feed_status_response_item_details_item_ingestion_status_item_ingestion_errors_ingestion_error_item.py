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


class FeedsGetFeedStatusResponseItemDetailsItemIngestionStatusItemIngestionErrorsIngestionErrorItem(BaseModel):
    # Error Type
    type: Literal["DATA_ERROR", "SYSTEM_ERROR", "TIMEOUT_ERROR"] = Field(alias='type')

    # Error code
    code: str = Field(alias='code')

    # Error description
    description: typing.Optional[str] = Field(None, alias='description')
    class Config:
        arbitrary_types_allowed = True
