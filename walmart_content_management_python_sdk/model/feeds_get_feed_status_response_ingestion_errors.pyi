# coding: utf-8

"""
    Content Management

    The content management feed allows you to process content for items in bulk. You can take in content via the content feeds. Use the XSDs to manage content.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from walmart_content_management_python_sdk import schemas  # noqa: F401


class FeedsGetFeedStatusResponseIngestionErrors(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    List of errors for an item
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def ingestionError() -> typing.Type['FeedsGetFeedStatusResponseIngestionErrorsIngestionError']:
                return FeedsGetFeedStatusResponseIngestionErrorsIngestionError
            __annotations__ = {
                "ingestionError": ingestionError,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ingestionError"]) -> 'FeedsGetFeedStatusResponseIngestionErrorsIngestionError': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ingestionError", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ingestionError"]) -> typing.Union['FeedsGetFeedStatusResponseIngestionErrorsIngestionError', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ingestionError", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ingestionError: typing.Union['FeedsGetFeedStatusResponseIngestionErrorsIngestionError', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FeedsGetFeedStatusResponseIngestionErrors':
        return super().__new__(
            cls,
            *args,
            ingestionError=ingestionError,
            _configuration=_configuration,
            **kwargs,
        )

from walmart_content_management_python_sdk.model.feeds_get_feed_status_response_ingestion_errors_ingestion_error import FeedsGetFeedStatusResponseIngestionErrorsIngestionError
