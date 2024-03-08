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


class PartnerItemIngestionStatus(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The ingestion status of an individual item
    """


    class MetaOapg:
        required = {
            "ingestionStatus",
        }
        
        class properties:
            
            
            class ingestionStatus(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "INPROGRESS": "INPROGRESS",
                        "SUCCESS": "SUCCESS",
                        "DATA_ERROR": "DATA_ERROR",
                        "SYSTEM_ERROR": "SYSTEM_ERROR",
                        "TIMEOUT_ERROR": "TIMEOUT_ERROR",
                    }
                
                @schemas.classproperty
                def INPROGRESS(cls):
                    return cls("INPROGRESS")
                
                @schemas.classproperty
                def SUCCESS(cls):
                    return cls("SUCCESS")
                
                @schemas.classproperty
                def DATA_ERROR(cls):
                    return cls("DATA_ERROR")
                
                @schemas.classproperty
                def SYSTEM_ERROR(cls):
                    return cls("SYSTEM_ERROR")
                
                @schemas.classproperty
                def TIMEOUT_ERROR(cls):
                    return cls("TIMEOUT_ERROR")
            martId = schemas.Int32Schema
            sku = schemas.StrSchema
            wpid = schemas.StrSchema
            index = schemas.Int32Schema
        
            @staticmethod
            def ingestionErrors() -> typing.Type['PartnerItemIngestionStatusIngestionErrors']:
                return PartnerItemIngestionStatusIngestionErrors
            __annotations__ = {
                "ingestionStatus": ingestionStatus,
                "martId": martId,
                "sku": sku,
                "wpid": wpid,
                "index": index,
                "ingestionErrors": ingestionErrors,
            }
    
    ingestionStatus: MetaOapg.properties.ingestionStatus
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ingestionStatus"]) -> MetaOapg.properties.ingestionStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["martId"]) -> MetaOapg.properties.martId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sku"]) -> MetaOapg.properties.sku: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wpid"]) -> MetaOapg.properties.wpid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["index"]) -> MetaOapg.properties.index: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ingestionErrors"]) -> 'PartnerItemIngestionStatusIngestionErrors': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ingestionStatus", "martId", "sku", "wpid", "index", "ingestionErrors", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ingestionStatus"]) -> MetaOapg.properties.ingestionStatus: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["martId"]) -> typing.Union[MetaOapg.properties.martId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sku"]) -> typing.Union[MetaOapg.properties.sku, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wpid"]) -> typing.Union[MetaOapg.properties.wpid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["index"]) -> typing.Union[MetaOapg.properties.index, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ingestionErrors"]) -> typing.Union['PartnerItemIngestionStatusIngestionErrors', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ingestionStatus", "martId", "sku", "wpid", "index", "ingestionErrors", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ingestionStatus: typing.Union[MetaOapg.properties.ingestionStatus, str, ],
        martId: typing.Union[MetaOapg.properties.martId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sku: typing.Union[MetaOapg.properties.sku, str, schemas.Unset] = schemas.unset,
        wpid: typing.Union[MetaOapg.properties.wpid, str, schemas.Unset] = schemas.unset,
        index: typing.Union[MetaOapg.properties.index, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ingestionErrors: typing.Union['PartnerItemIngestionStatusIngestionErrors', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PartnerItemIngestionStatus':
        return super().__new__(
            cls,
            *args,
            ingestionStatus=ingestionStatus,
            martId=martId,
            sku=sku,
            wpid=wpid,
            index=index,
            ingestionErrors=ingestionErrors,
            _configuration=_configuration,
            **kwargs,
        )

from walmart_content_management_python_sdk.model.partner_item_ingestion_status_ingestion_errors import PartnerItemIngestionStatusIngestionErrors
