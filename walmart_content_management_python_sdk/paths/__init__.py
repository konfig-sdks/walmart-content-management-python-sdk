# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from walmart_content_management_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V3_FEEDS = "/v3/feeds"
    V2_FEEDS = "/v2/feeds"
    FEEDS = "/feeds"
    FEEDS_FEED_ID = "/feeds/{feedId}"
