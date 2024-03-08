import typing_extensions

from walmart_content_management_python_sdk.apis.tags import TagValues
from walmart_content_management_python_sdk.apis.tags.feeds_api import FeedsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.FEEDS: FeedsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.FEEDS: FeedsApi,
    }
)
