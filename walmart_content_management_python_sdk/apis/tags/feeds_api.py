# coding: utf-8

"""
    Content Management

    The content management feed allows you to process content for items in bulk. You can take in content via the content feeds. Use the XSDs to manage content.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from walmart_content_management_python_sdk.paths.v3_feeds.post import CreateContentFeed
from walmart_content_management_python_sdk.paths.v2_feeds.post import CreateRichMediaFeed
from walmart_content_management_python_sdk.paths.feeds.get import DisplayItemStatus
from walmart_content_management_python_sdk.paths.feeds_feed_id.get import GetFeedStatus
from walmart_content_management_python_sdk.apis.tags.feeds_api_raw import FeedsApiRaw


class FeedsApi(
    CreateContentFeed,
    CreateRichMediaFeed,
    DisplayItemStatus,
    GetFeedStatus,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: FeedsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = FeedsApiRaw(api_client)