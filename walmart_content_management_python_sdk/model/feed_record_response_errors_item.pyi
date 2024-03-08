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


class FeedRecordResponseErrorsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "code",
        }
        
        class properties:
            code = schemas.StrSchema
            info = schemas.StrSchema
            description = schemas.StrSchema
            field = schemas.StrSchema
            
            
            class severity(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def INFO(cls):
                    return cls("INFO")
                
                @schemas.classproperty
                def WARN(cls):
                    return cls("WARN")
                
                @schemas.classproperty
                def ERROR(cls):
                    return cls("ERROR")
            
            
            class category(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def APPLICATION(cls):
                    return cls("APPLICATION")
                
                @schemas.classproperty
                def SYSTEM(cls):
                    return cls("SYSTEM")
                
                @schemas.classproperty
                def REQUEST(cls):
                    return cls("REQUEST")
                
                @schemas.classproperty
                def DATA(cls):
                    return cls("DATA")
        
            @staticmethod
            def causes() -> typing.Type['FeedRecordResponseErrorsItemCauses']:
                return FeedRecordResponseErrorsItemCauses
        
            @staticmethod
            def errorIdentifiers() -> typing.Type['FeedRecordResponseErrorsItemErrorIdentifiers']:
                return FeedRecordResponseErrorsItemErrorIdentifiers
            component = schemas.StrSchema
            type = schemas.StrSchema
            serviceName = schemas.StrSchema
            
            
            class gatewayErrorCategory(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def INTERNAL_DATA_ERROR(cls):
                    return cls("INTERNAL_DATA_ERROR")
                
                @schemas.classproperty
                def EXTERNAL_DATA_ERROR(cls):
                    return cls("EXTERNAL_DATA_ERROR")
                
                @schemas.classproperty
                def SYSTEM_ERROR(cls):
                    return cls("SYSTEM_ERROR")
            __annotations__ = {
                "code": code,
                "info": info,
                "description": description,
                "field": field,
                "severity": severity,
                "category": category,
                "causes": causes,
                "errorIdentifiers": errorIdentifiers,
                "component": component,
                "type": type,
                "serviceName": serviceName,
                "gatewayErrorCategory": gatewayErrorCategory,
            }
    
    code: MetaOapg.properties.code
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["info"]) -> MetaOapg.properties.info: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field"]) -> MetaOapg.properties.field: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["severity"]) -> MetaOapg.properties.severity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["causes"]) -> 'FeedRecordResponseErrorsItemCauses': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errorIdentifiers"]) -> 'FeedRecordResponseErrorsItemErrorIdentifiers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["component"]) -> MetaOapg.properties.component: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceName"]) -> MetaOapg.properties.serviceName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gatewayErrorCategory"]) -> MetaOapg.properties.gatewayErrorCategory: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["code", "info", "description", "field", "severity", "category", "causes", "errorIdentifiers", "component", "type", "serviceName", "gatewayErrorCategory", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["info"]) -> typing.Union[MetaOapg.properties.info, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field"]) -> typing.Union[MetaOapg.properties.field, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["severity"]) -> typing.Union[MetaOapg.properties.severity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> typing.Union[MetaOapg.properties.category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["causes"]) -> typing.Union['FeedRecordResponseErrorsItemCauses', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errorIdentifiers"]) -> typing.Union['FeedRecordResponseErrorsItemErrorIdentifiers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["component"]) -> typing.Union[MetaOapg.properties.component, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceName"]) -> typing.Union[MetaOapg.properties.serviceName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gatewayErrorCategory"]) -> typing.Union[MetaOapg.properties.gatewayErrorCategory, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["code", "info", "description", "field", "severity", "category", "causes", "errorIdentifiers", "component", "type", "serviceName", "gatewayErrorCategory", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        code: typing.Union[MetaOapg.properties.code, str, ],
        info: typing.Union[MetaOapg.properties.info, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        field: typing.Union[MetaOapg.properties.field, str, schemas.Unset] = schemas.unset,
        severity: typing.Union[MetaOapg.properties.severity, str, schemas.Unset] = schemas.unset,
        category: typing.Union[MetaOapg.properties.category, str, schemas.Unset] = schemas.unset,
        causes: typing.Union['FeedRecordResponseErrorsItemCauses', schemas.Unset] = schemas.unset,
        errorIdentifiers: typing.Union['FeedRecordResponseErrorsItemErrorIdentifiers', schemas.Unset] = schemas.unset,
        component: typing.Union[MetaOapg.properties.component, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        serviceName: typing.Union[MetaOapg.properties.serviceName, str, schemas.Unset] = schemas.unset,
        gatewayErrorCategory: typing.Union[MetaOapg.properties.gatewayErrorCategory, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FeedRecordResponseErrorsItem':
        return super().__new__(
            cls,
            *args,
            code=code,
            info=info,
            description=description,
            field=field,
            severity=severity,
            category=category,
            causes=causes,
            errorIdentifiers=errorIdentifiers,
            component=component,
            type=type,
            serviceName=serviceName,
            gatewayErrorCategory=gatewayErrorCategory,
            _configuration=_configuration,
            **kwargs,
        )

from walmart_content_management_python_sdk.model.feed_record_response_errors_item_causes import FeedRecordResponseErrorsItemCauses
from walmart_content_management_python_sdk.model.feed_record_response_errors_item_error_identifiers import FeedRecordResponseErrorsItemErrorIdentifiers