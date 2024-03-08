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


class RequiredFeedsCreateContentFeedResponse(TypedDict):
    pass

class OptionalFeedsCreateContentFeedResponse(TypedDict, total=False):
    # A unique ID, returned from the Bulk Upload API, used for tracking the feed file.
    feedId: str

class FeedsCreateContentFeedResponse(RequiredFeedsCreateContentFeedResponse, OptionalFeedsCreateContentFeedResponse):
    pass
