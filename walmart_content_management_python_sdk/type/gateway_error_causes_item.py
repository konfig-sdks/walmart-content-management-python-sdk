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


class RequiredGatewayErrorCausesItem(TypedDict):
    pass

class OptionalGatewayErrorCausesItem(TypedDict, total=False):
    description: str

    code: str

    field: str

    type: str

class GatewayErrorCausesItem(RequiredGatewayErrorCausesItem, OptionalGatewayErrorCausesItem):
    pass
