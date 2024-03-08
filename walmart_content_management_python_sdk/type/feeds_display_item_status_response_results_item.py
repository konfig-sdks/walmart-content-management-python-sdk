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


class RequiredFeedsDisplayItemStatusResponseResultsItem(TypedDict):
    pass

class OptionalFeedsDisplayItemStatusResponseResultsItem(TypedDict, total=False):
    # A unique ID used for tracking the Feed File
    feedId: str

    # The source of the feed
    feedSource: str

    # The feed type
    feedType: str

    # The seller ID
    partnerId: str

    # The number of items received
    itemsReceived: int

    # The number of items in the feed that have successfully processed
    itemsSucceeded: int

    # The number of items in the feed that failed due to a data or system error
    itemsFailed: int

    # The number of items in the feed that are still in progress
    itemsProcessing: int

    # Can be one of the following: RECEIVED, INPROGRESS, PROCESSED, or ERROR. For details, see the definitions listed under 'Feed Statuses' at the beginning of this section.
    feedStatus: str

    # The date and time the feed was submitted. Format: yyyymmddThh:mm:ss.xxxz
    feedDate: datetime

    # The batch ID for the feed, if provided
    batchId: str

    # The most recent time the feed was modified. Format: yyyymmddThh:mm:ss.xxxz
    modifiedDtm: datetime

class FeedsDisplayItemStatusResponseResultsItem(RequiredFeedsDisplayItemStatusResponseResultsItem, OptionalFeedsDisplayItemStatusResponseResultsItem):
    pass
