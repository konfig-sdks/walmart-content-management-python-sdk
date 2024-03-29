# coding: utf-8

"""
    Content Management

    The content management feed allows you to process content for items in bulk. You can take in content via the content feeds. Use the XSDs to manage content.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from walmart_content_management_python_sdk.paths.v3_feeds.post import CreateContentFeedRaw
from walmart_content_management_python_sdk.paths.v2_feeds.post import CreateRichMediaFeedRaw
from walmart_content_management_python_sdk.paths.feeds.get import DisplayItemStatusRaw
from walmart_content_management_python_sdk.paths.feeds_feed_id.get import GetFeedStatusRaw


class FeedsApiRaw(
    CreateContentFeedRaw,
    CreateRichMediaFeedRaw,
    DisplayItemStatusRaw,
    GetFeedStatusRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
