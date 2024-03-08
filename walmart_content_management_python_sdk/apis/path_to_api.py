import typing_extensions

from walmart_content_management_python_sdk.paths import PathValues
from walmart_content_management_python_sdk.apis.paths.v3_feeds import V3Feeds
from walmart_content_management_python_sdk.apis.paths.v2_feeds import V2Feeds
from walmart_content_management_python_sdk.apis.paths.feeds import Feeds
from walmart_content_management_python_sdk.apis.paths.feeds_feed_id import FeedsFeedId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V3_FEEDS: V3Feeds,
        PathValues.V2_FEEDS: V2Feeds,
        PathValues.FEEDS: Feeds,
        PathValues.FEEDS_FEED_ID: FeedsFeedId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V3_FEEDS: V3Feeds,
        PathValues.V2_FEEDS: V2Feeds,
        PathValues.FEEDS: Feeds,
        PathValues.FEEDS_FEED_ID: FeedsFeedId,
    }
)
