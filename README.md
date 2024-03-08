<div align="center">

[![Visit Walmart](./header.png)](https://developer.walmart.com&#x2F;)

# Walmart<a id="walmart"></a>

The content management feed allows you to process content for items in bulk. You can take in content via the content feeds. Use the XSDs to manage content.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`walmart.feeds.create_content_feed`](#walmartfeedscreate_content_feed)
  * [`walmart.feeds.create_rich_media_feed`](#walmartfeedscreate_rich_media_feed)
  * [`walmart.feeds.display_item_status`](#walmartfeedsdisplay_item_status)
  * [`walmart.feeds.get_feed_status`](#walmartfeedsget_feed_status)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Walmart&serviceName=Content%20Management&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from walmart_content_management_python_sdk import Walmart, ApiException

walmart = Walmart(
    client_id="YOUR_API_KEY",
    private_key="YOUR_API_KEY",
)

try:
    # Content feeds
    create_content_feed_response = walmart.feeds.create_content_feed(
        feed_type="CONTENT_PRODUCT",
        wm_qos_correlation_id="b3261d2d-028a-4ef7-8602-633c23200af6",
        wm_svc_name="Walmart Service Name",
        wm_sec_timestamp="1443748249449",
        wm_sec_auth_signature="9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg=",
        wm_consumer_id="Get the Consumer ID from Developer Center after logging in",
        file=open("/path/to/file", "rb"),
        wm_consumer_channel_type="string_example",
    )
    print(create_content_feed_response)
except ApiException as e:
    print("Exception when calling FeedsApi.create_content_feed: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from walmart_content_management_python_sdk import Walmart, ApiException

walmart = Walmart(
    client_id="YOUR_API_KEY",
    private_key="YOUR_API_KEY",
)


async def main():
    try:
        # Content feeds
        create_content_feed_response = await walmart.feeds.acreate_content_feed(
            feed_type="CONTENT_PRODUCT",
            wm_qos_correlation_id="b3261d2d-028a-4ef7-8602-633c23200af6",
            wm_svc_name="Walmart Service Name",
            wm_sec_timestamp="1443748249449",
            wm_sec_auth_signature="9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg=",
            wm_consumer_id="Get the Consumer ID from Developer Center after logging in",
            file=open("/path/to/file", "rb"),
            wm_consumer_channel_type="string_example",
        )
        print(create_content_feed_response)
    except ApiException as e:
        print("Exception when calling FeedsApi.create_content_feed: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from walmart_content_management_python_sdk import Walmart, ApiException

walmart = Walmart(
    client_id="YOUR_API_KEY",
    private_key="YOUR_API_KEY",
)

try:
    # Content feeds
    create_content_feed_response = walmart.feeds.raw.create_content_feed(
        feed_type="CONTENT_PRODUCT",
        wm_qos_correlation_id="b3261d2d-028a-4ef7-8602-633c23200af6",
        wm_svc_name="Walmart Service Name",
        wm_sec_timestamp="1443748249449",
        wm_sec_auth_signature="9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg=",
        wm_consumer_id="Get the Consumer ID from Developer Center after logging in",
        file=open("/path/to/file", "rb"),
        wm_consumer_channel_type="string_example",
    )
    pprint(create_content_feed_response.body)
    pprint(create_content_feed_response.body["feed_id"])
    pprint(create_content_feed_response.headers)
    pprint(create_content_feed_response.status)
    pprint(create_content_feed_response.round_trip_time)
except ApiException as e:
    print("Exception when calling FeedsApi.create_content_feed: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `walmart.feeds.create_content_feed`<a id="walmartfeedscreate_content_feed"></a>

You can update 10,000 items at once; updates with more than 10,000 items are not supported. Keep feed sizes below 10 MB to ensure optimal feed processing time.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_content_feed_response = walmart.feeds.create_content_feed(
    feed_type="CONTENT_PRODUCT",
    wm_qos_correlation_id="b3261d2d-028a-4ef7-8602-633c23200af6",
    wm_svc_name="Walmart Service Name",
    wm_sec_timestamp="1443748249449",
    wm_sec_auth_signature="9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg=",
    wm_consumer_id="Get the Consumer ID from Developer Center after logging in",
    file=open("/path/to/file", "rb"),
    wm_consumer_channel_type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### feed_type: `str`<a id="feed_type-str"></a>

The feed Type

##### wm_qos_correlation_id: `str`<a id="wm_qos_correlation_id-str"></a>

A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID

##### wm_svc_name: `str`<a id="wm_svc_name-str"></a>

Walmart Service Name

##### wm_sec_timestamp: `str`<a id="wm_sec_timestamp-str"></a>

The Epoch timestamp

##### wm_sec_auth_signature: `str`<a id="wm_sec_auth_signature-str"></a>

The vendor's digital signature, generated by running the JAR file or custom generation code

##### wm_consumer_id: `str`<a id="wm_consumer_id-str"></a>

A unique ID required to access the API

##### file: `IO`<a id="file-io"></a>

Feed file to upload

##### wm_consumer_channel_type: `str`<a id="wm_consumer_channel_type-str"></a>

A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FeedsCreateContentFeedRequest`](./walmart_content_management_python_sdk/type/feeds_create_content_feed_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FeedsCreateContentFeedResponse`](./walmart_content_management_python_sdk/pydantic/feeds_create_content_feed_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v3/feeds` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `walmart.feeds.create_rich_media_feed`<a id="walmartfeedscreate_rich_media_feed"></a>

Rich Media includes material such as videos, comparison tables, and view360 media which is item-specific.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_rich_media_feed_response = walmart.feeds.create_rich_media_feed(
    body='<?xml version="1.0" encoding="UTF-8"?>\n<RichMediaFeed xmlns="http://walmart.com/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://walmart.com/ RichMediaFeed.xsd ">\n    <RichMediaFeedHeader>\n        <version>2.1.2</version>\n        <requestId>requestId</requestId>\n        <requestBatchId>requestBatchId</requestBatchId>\n        <feedDate>2001-12-31T12:00:00</feedDate>\n        <mart>WALMART_US</mart>\n    </RichMediaFeedHeader>\n    <RichMedia>\n        <productIdentifiers>\n            <productIdentifier>\n                <productIdType>UPC</productIdType>\n                <productId>815812013182</productId>\n            </productIdentifier>\n        </productIdentifiers>\n        <Modules processMode="MERGE">\n            <view360 provider="">\n                <html-content>html-content</html-content>\n            </view360>\n            <marketing-content provider="">\n                <html-content>html-content</html-content>\n            </marketing-content>\n            <product-tour provider="">\n                <html-content>html-content</html-content>\n            </product-tour>\n            <videos provider="">\n                <video provider="">\n                    <title>title</title>\n                    <description>description</description>\n                    <language>en-US</language>\n                    <closed-caption>\n                        <url>url</url>\n                        <format>webvtt</format>\n                        <language>en-US</language>\n                    </closed-caption>\n                    <age-gate>0</age-gate>\n                    <source-mobile>\n                        <url>url</url>\n                        <width>720</width>\n                        <height>480</height>\n                        <format>mp4</format>\n                        <thumbnail>\n                            <url>url</url>\n                            <format>png</format>\n                            <width>120</width>\n                            <height>100</height>\n                        </thumbnail>\n                        <poster>\n                            <url>url</url>\n                            <format>jpg</format>\n                            <width>720</width>\n                            <height>480</height>\n                        </poster>\n                    </source-mobile>\n                    <sources>\n                        <source>\n                            <url>url</url>\n                            <width>720</width>\n                            <height>480</height>\n                            <format>mp4</format>\n                            <screen>mobile</screen>\n                            <thumbnail>\n                                <url>url</url>\n                                <format>png</format>\n                                <width>120</width>\n                                <height>100</height>\n                            </thumbnail>\n                            <poster>\n                                <url>url</url>\n                                <format>jpg</format>\n                                <width>720</width>\n                                <height>480</height>\n                            </poster>\n                        </source>\n                    </sources>\n                    <duration>0</duration>\n                    <likes>0</likes>\n                    <views>0</views>\n                    <tags>tags</tags>\n                </video>\n            </videos>\n            <documents provider="">\n                <document>\n                    <title>title</title>\n                    <url>url</url>\n                    <format>pdf</format>\n                    <pages>0</pages>\n                    <thumbnail>\n                        <url>url</url>\n                        <format>png</format>\n                        <width>120</width>\n                        <height>100</height>\n                    </thumbnail>\n                    <size>0</size>\n                </document>\n            </documents>\n            <customer-review-videos provider="">\n                <customer-review-video provider="">\n                    <title>title</title>\n                    <description>description</description>\n                    <language>en-US</language>\n                    <closed-caption>\n                        <url>url</url>\n                        <format>webvtt</format>\n                        <language>en-US</language>\n                    </closed-caption>\n                    <age-gate>0</age-gate>\n                    <source-computer>\n                        <url>url</url>\n                        <width>720</width>\n                        <height>480</height>\n                        <format>mp4</format>\n                        <thumbnail>\n                            <url>url</url>\n                            <format>png</format>\n                            <width>120</width>\n                            <height>100</height>\n                        </thumbnail>\n                        <poster>\n                            <url>url</url>\n                            <format>jpg</format>\n                            <width>720</width>\n                            <height>480</height>\n                        </poster>\n                    </source-computer>\n                    <sources>\n                        <source>\n                            <url>url</url>\n                            <width>720</width>\n                            <height>480</height>\n                            <format>mp4</format>\n                            <screen>mobile</screen>\n                            <thumbnail>\n                                <url>url</url>\n                                <format>png</format>\n                                <width>120</width>\n                                <height>100</height>\n                            </thumbnail>\n                            <poster>\n                                <url>url</url>\n                                <format>jpg</format>\n                                <width>720</width>\n                                <height>480</height>\n                            </poster>\n                        </source>\n                    </sources>\n                    <duration>0</duration>\n                    <likes>0</likes>\n                    <views>0</views>\n                    <tags>tags</tags>\n                </customer-review-video>\n            </customer-review-videos>\n            <comparison-table provider="">\n                <headline>\n                    <image>\n                        <title>title</title>\n                        <url>url</url>\n                        <height>0</height>\n                        <width>0</width>\n                        <format>png</format>\n                    </image>\n                </headline>\n                <feature-column>\n                    <sections>\n                        <section>\n                            <header>\n                                <caption>caption</caption>\n                            </header>\n                            <feature>\n                                <caption>caption</caption>\n                            </feature>\n                        </section>\n                    </sections>\n                </feature-column>\n                <product-columns>\n                    <product-column>\n                        <products-info>\n                            <product-info>\n                                <title>title</title>\n                                <thumbnail>\n                                    <url>url</url>\n                                    <format>png</format>\n                                    <width>120</width>\n                                    <height>120</height>\n                                </thumbnail>\n                                <productIdentifiers>\n                                    <productIdentifier>\n                                        <productIdType>UPC</productIdType>\n                                        <productId>productId</productId>\n                                    </productIdentifier>\n                                </productIdentifiers>\n                            </product-info>\n                        </products-info>\n                        <value>value</value>\n                    </product-column>\n                </product-columns>\n            </comparison-table>\n            <expert-reviews provider="">\n                <expert-review provider="">\n                    <html-content>html-content</html-content>\n                </expert-review>\n            </expert-reviews>\n            <misc-modules provider="">\n                <misc-module>\n                    <attributeName>attributeName</attributeName>\n                    <attributeValue>attributeValue</attributeValue>\n                </misc-module>\n            </misc-modules>\n        </Modules>\n        <additionalProductAttributes>\n            <NameValueAttribute>\n                <name>name</name>\n                <type>LOCALIZABLE_TEXT</type>\n                <value>\n                    <value>value</value>\n                    <group>group</group>\n                    <rank>0</rank>\n                </value>\n            </NameValueAttribute>\n        </additionalProductAttributes>\n    </RichMedia>\n</RichMediaFeed>\n',
    feed_type="item",
    wm_qos_correlation_id="b3261d2d-028a-4ef7-8602-633c23200af6",
    wm_svc_name="Walmart Service Name",
    wm_sec_timestamp="1443748249449",
    wm_sec_auth_signature="9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg=",
    wm_consumer_id="Get the Consumer ID from Developer Center after logging in",
    wm_consumer_channel_type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### feed_type: `str`<a id="feed_type-str"></a>

The feed Type

##### wm_qos_correlation_id: `str`<a id="wm_qos_correlation_id-str"></a>

A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID

##### wm_svc_name: `str`<a id="wm_svc_name-str"></a>

Walmart Service Name

##### wm_sec_timestamp: `str`<a id="wm_sec_timestamp-str"></a>

The Epoch timestamp

##### wm_sec_auth_signature: `str`<a id="wm_sec_auth_signature-str"></a>

The vendor's digital signature, generated by running the JAR file or custom generation code

##### wm_consumer_id: `str`<a id="wm_consumer_id-str"></a>

A unique ID required to access the API

##### wm_consumer_channel_type: `str`<a id="wm_consumer_channel_type-str"></a>

A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding

##### requestBody: `str`<a id="requestbody-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`FeedsCreateRichMediaFeedResponse`](./walmart_content_management_python_sdk/pydantic/feeds_create_rich_media_feed_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/feeds` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `walmart.feeds.display_item_status`<a id="walmartfeedsdisplay_item_status"></a>

You can display an item status for a specific feed ID. Use the feed ID returned from the upload an item feed API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
display_item_status_response = walmart.feeds.display_item_status(
    feed_id="feedId_example",
    wm_qos_correlation_id="b3261d2d-028a-4ef7-8602-633c23200af6",
    wm_svc_name="Walmart Service Name",
    wm_sec_timestamp="1443748249449",
    wm_sec_auth_signature="9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg=",
    wm_consumer_id="Get the Consumer ID from Developer Center after logging in",
    offset="0",
    limit="20",
    wm_consumer_channel_type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### feed_id: `str`<a id="feed_id-str"></a>

A unique ID returned from the Bulk Upload API, used for tracking the Feed File. Special characters must be escaped (e.g., feedId: '...3456@789...' must be entered in the URL as '...3456%40789).

##### wm_qos_correlation_id: `str`<a id="wm_qos_correlation_id-str"></a>

A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID

##### wm_svc_name: `str`<a id="wm_svc_name-str"></a>

Walmart Service Name

##### wm_sec_timestamp: `str`<a id="wm_sec_timestamp-str"></a>

The Epoch timestamp

##### wm_sec_auth_signature: `str`<a id="wm_sec_auth_signature-str"></a>

The vendor's digital signature, generated by running the JAR file or custom generation code

##### wm_consumer_id: `str`<a id="wm_consumer_id-str"></a>

A unique ID required to access the API

##### offset: `str`<a id="offset-str"></a>

The object response to the starting number, where 0 is the first entity that can be requested.

##### limit: `str`<a id="limit-str"></a>

The number of entities to be returned. Maximum 20 entities.

##### wm_consumer_channel_type: `str`<a id="wm_consumer_channel_type-str"></a>

A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding

#### 🔄 Return<a id="🔄-return"></a>

[`FeedsDisplayItemStatusResponse`](./walmart_content_management_python_sdk/pydantic/feeds_display_item_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/feeds` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `walmart.feeds.get_feed_status`<a id="walmartfeedsget_feed_status"></a>

You can display the status of all items for a specific feed ID. Use the feed ID returned from the upload an item feed API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_feed_status_response = walmart.feeds.get_feed_status(
    feed_id="feedId_example",
    wm_qos_correlation_id="b3261d2d-028a-4ef7-8602-633c23200af6",
    wm_svc_name="Walmart Service Name",
    wm_sec_timestamp="1443748249449",
    wm_sec_auth_signature="9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg=",
    wm_consumer_id="Get the Consumer ID from Developer Center after logging in",
    include_details="false",
    offset="0",
    limit="20",
    wm_consumer_channel_type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### feed_id: `str`<a id="feed_id-str"></a>

A unique ID returned from the Bulk Upload API, used for tracking the Feed File. Special characters must be escaped (e.g., feedId: '...3456@789...' must be entered in the URL as '...3456%40789).

##### wm_qos_correlation_id: `str`<a id="wm_qos_correlation_id-str"></a>

A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID

##### wm_svc_name: `str`<a id="wm_svc_name-str"></a>

Walmart Service Name

##### wm_sec_timestamp: `str`<a id="wm_sec_timestamp-str"></a>

The Epoch timestamp

##### wm_sec_auth_signature: `str`<a id="wm_sec_auth_signature-str"></a>

The vendor's digital signature, generated by running the JAR file or custom generation code

##### wm_consumer_id: `str`<a id="wm_consumer_id-str"></a>

A unique ID required to access the API

##### include_details: `str`<a id="include_details-str"></a>

Includes details of each entity in the feed. Do not set this parameter to true.

##### offset: `str`<a id="offset-str"></a>

The object response to the starting number, where 0 is the first entity that can be requested.

##### limit: `str`<a id="limit-str"></a>

The number of entities to be returned. Maximum 20 entities.

##### wm_consumer_channel_type: `str`<a id="wm_consumer_channel_type-str"></a>

A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding

#### 🔄 Return<a id="🔄-return"></a>

[`FeedsGetFeedStatusResponse`](./walmart_content_management_python_sdk/pydantic/feeds_get_feed_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/feeds/{feedId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
