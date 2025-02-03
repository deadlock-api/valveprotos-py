# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.customer_validator import check_one_of
from pydantic import BaseModel
from pydantic import Field
from pydantic import model_validator
import typing

class ESteamLearnDataType(IntEnum):
    STEAMLEARN_DATATYPE_INVALID = 0
    STEAMLEARN_DATATYPE_INT32 = 1
    STEAMLEARN_DATATYPE_FLOAT32 = 2
    STEAMLEARN_DATATYPE_BOOL = 3
    STEAMLEARN_DATATYPE_STRING = 4
    STEAMLEARN_DATATYPE_OBJECT = 5


class ESteammLearnRegisterDataSourceResult(IntEnum):
    STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR = 0
    STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_SUCCESS_CREATED = 1
    STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_SUCCESS_FOUND = 2
    STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_GENERIC = 3
    STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_INVALID_NAME = 4
    STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_INVALID_VERSION = 5
    STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_DATA_CHANGED = 6
    STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_DATA_INVALID = 7
    STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_FORBIDDEN = 8
    STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_INVALID_TIMESTAMP = 9
    STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_DISABLED = 10


class ESteamLearnCacheDataResult(IntEnum):
    STEAMLEARN_CACHE_DATA_ERROR = 0
    STEAMLEARN_CACHE_DATA_SUCCESS = 1
    STEAMLEARN_CACHE_DATA_ERROR_UNKNOWN_DATA_SOURCE = 2
    STEAMLEARN_CACHE_DATA_ERROR_UNCACHED_DATA_SOURCE = 3
    STEAMLEARN_CACHE_DATA_ERROR_INVALID_KEYS = 4
    STEAMLEARN_CACHE_DATA_ERROR_FORBIDDEN = 5
    STEAMLEARN_CACHE_DATA_ERROR_INVALID_TIMESTAMP = 6
    STEAMLEARN_CACHE_DATA_DISABLED = 7


class ESteamLearnSnapshotProjectResult(IntEnum):
    STEAMLEARN_SNAPSHOT_PROJECT_ERROR = 0
    STEAMLEARN_SNAPSHOT_PROJECT_SUCCESS_STORED = 1
    STEAMLEARN_SNAPSHOT_PROJECT_SUCCESS_QUEUED = 2
    STEAMLEARN_SNAPSHOT_PROJECT_ERROR_INVALID_PROJECT_ID = 3
    STEAMLEARN_SNAPSHOT_PROJECT_ERROR_UNKNOWN_DATA_SOURCE = 4
    STEAMLEARN_SNAPSHOT_PROJECT_ERROR_INVALID_DATA_SOURCE_KEY = 5
    STEAMLEARN_SNAPSHOT_PROJECT_ERROR_MISSING_CACHE_DURATION = 6
    STEAMLEARN_SNAPSHOT_PROJECT_ERROR_NO_PUBLISHED_CONFIG = 7
    STEAMLEARN_SNAPSHOT_PROJECT_ERROR_FORBIDDEN = 8
    STEAMLEARN_SNAPSHOT_PROJECT_ERROR_INVALID_TIMESTAMP = 9
    STEAMLEARN_SNAPSHOT_PROJECT_ERROR_INTERNAL_DATA_SOURCE_ERROR = 10
    STEAMLEARN_SNAPSHOT_PROJECT_DISABLED = 11
    STEAMLEARN_SNAPSHOT_PROJECT_ERROR_INVALID_PUBLISHED_VERSION = 12


class ESteamLearnGetAccessTokensResult(IntEnum):
    STEAMLEARN_GET_ACCESS_TOKENS_ERROR = 0
    STEAMLEARN_GET_ACCESS_TOKENS_SUCCESS = 1


class ESteamLearnInferenceResult(IntEnum):
    STEAMLEARN_INFERENCE_ERROR = 0
    STEAMLEARN_INFERENCE_SUCCESS = 1
    STEAMLEARN_INFERENCE_ERROR_INVALID_PROJECT_ID = 2
    STEAMLEARN_INFERENCE_ERROR_MISSING_CACHED_SCHEMA_DATA = 3
    STEAMLEARN_INFERENCE_ERROR_NO_PUBLISHED_CONFIG = 4
    STEAMLEARN_INFERENCE_ERROR_FORBIDDEN = 5
    STEAMLEARN_INFERENCE_ERROR_INVALID_TIMESTAMP = 6
    STEAMLEARN_INFERENCE_ERROR_INVALID_PUBLISHED_VERSION = 7
    STEAMLEARN_INFERENCE_ERROR_NO_FETCH_ID_FOUND = 8
    STEAMLEARN_INFERENCE_ERROR_TOO_BUSY = 9


class ESteamLearnInferenceMetadataResult(IntEnum):
    STEAMLEARN_INFERENCE_METADATA_ERROR = 0
    STEAMLEARN_INFERENCE_METADATA_SUCCESS = 1
    STEAMLEARN_INFERENCE_METADATA_ERROR_INVALID_PROJECT_ID = 2
    STEAMLEARN_INFERENCE_METADATA_ERROR_NO_PUBLISHED_CONFIG = 3
    STEAMLEARN_INFERENCE_METADATA_ERROR_FORBIDDEN = 4
    STEAMLEARN_INFERENCE_METADATA_ERROR_INVALID_TIMESTAMP = 5
    STEAMLEARN_INFERENCE_METADATA_ERROR_INVALID_PUBLISHED_VERSION = 6
    STEAMLEARN_INFERENCE_METADATA_ERROR_NO_FETCH_ID_FOUND = 7

class CMsgSteamLearnDataSourceDescElement(BaseModel):
    name: str = Field(default="")
    data_type: ESteamLearnDataType = Field(default=0)
    object: "CMsgSteamLearnDataSourceDescObject" = Field()
    count: int = Field(default=0)

class CMsgSteamLearnDataSourceDescObject(BaseModel):
    elements: typing.List[CMsgSteamLearnDataSourceDescElement] = Field(default_factory=list)

class CMsgSteamLearnDataSource(BaseModel):
    id: int = Field(default=0)
    name: str = Field(default="")
    version: int = Field(default=0)
    source_description: str = Field(default="")
    structure: CMsgSteamLearnDataSourceDescObject = Field()
    structure_crc: int = Field(default=0)
    cache_duration_seconds: int = Field(default=0)

class CMsgSteamLearnDataElement(BaseModel):
    name: str = Field(default="")
    data_int32s: typing.List[int] = Field(default_factory=list)
    data_floats: typing.List[float] = Field(default_factory=list)
    data_bools: typing.List[bool] = Field(default_factory=list)
    data_strings: typing.List[str] = Field(default_factory=list)
    data_objects: typing.List["CMsgSteamLearnDataObject"] = Field(default_factory=list)

class CMsgSteamLearnDataObject(BaseModel):
    elements: typing.List[CMsgSteamLearnDataElement] = Field(default_factory=list)

class CMsgSteamLearnData(BaseModel):
    data_source_id: int = Field(default=0)
    keys: typing.List[int] = Field(default_factory=list)
    data_object: CMsgSteamLearnDataObject = Field()

class CMsgSteamLearnDataList(BaseModel):
    data: typing.List[CMsgSteamLearnData] = Field(default_factory=list)

class CMsgSteamLearn_RegisterDataSource_Request(BaseModel):
    access_token: str = Field(default="")
    data_source: CMsgSteamLearnDataSource = Field()

class CMsgSteamLearn_RegisterDataSource_Response(BaseModel):
    result: ESteammLearnRegisterDataSourceResult = Field(default=0)
    data_source: CMsgSteamLearnDataSource = Field()

class CMsgSteamLearn_CacheData_Request(BaseModel):
    access_token: str = Field(default="")
    data: CMsgSteamLearnData = Field()

class CMsgSteamLearn_CacheData_Response(BaseModel):
    cache_data_result: ESteamLearnCacheDataResult = Field(default=0)

class CMsgSteamLearn_SnapshotProject_Request(BaseModel):
    access_token: str = Field(default="")
    project_id: int = Field(default=0)
    published_version: int = Field(default=0)
    keys: typing.List[int] = Field(default_factory=list)
    data: typing.List[CMsgSteamLearnData] = Field(default_factory=list)
    pending_data_limit_seconds: int = Field(default=0)

class CMsgSteamLearn_SnapshotProject_Response(BaseModel):
    snapshot_result: ESteamLearnSnapshotProjectResult = Field(default=0)

class CMsgSteamLearn_Inference_Request(BaseModel):
    access_token: str = Field(default="")
    project_id: int = Field(default=0)
    published_version: int = Field(default=0)
    override_train_id: int = Field(default=0)
    data: CMsgSteamLearnDataList = Field()
    additional_data: typing.List[float] = Field(default_factory=list)

class CMsgSteamLearn_BatchOperation_Request(BaseModel):
    cache_data_requests: typing.List[CMsgSteamLearn_CacheData_Request] = Field(default_factory=list)
    snapshot_requests: typing.List[CMsgSteamLearn_SnapshotProject_Request] = Field(default_factory=list)
    inference_requests: typing.List[CMsgSteamLearn_Inference_Request] = Field(default_factory=list)

class CMsgSteamLearn_InferenceBackend_Response(BaseModel):
    class Sequence(BaseModel):
        value: typing.List[float] = Field(default_factory=list)

    class RegressionOutput(BaseModel):
        value: float = Field(default=0.0)

    class BinaryCrossEntropyOutput(BaseModel):
        value: float = Field(default=0.0)

    class MutliBinaryCrossEntropyOutput(BaseModel):
        weight: typing.List[float] = Field(default_factory=list)
        value: typing.List[float] = Field(default_factory=list)
        value_sequence: typing.List["CMsgSteamLearn_InferenceBackend_Response.Sequence"] = Field(default_factory=list)

    class CategoricalCrossEntropyOutput(BaseModel):
        weight: typing.List[float] = Field(default_factory=list)
        value: typing.List[float] = Field(default_factory=list)
        value_sequence: typing.List["CMsgSteamLearn_InferenceBackend_Response.Sequence"] = Field(default_factory=list)

    class Output(BaseModel):
        _one_of_dict = {"Output.ResponseType": {"fields": {"binary_crossentropy", "categorical_crossentropy", "multi_binary_crossentropy", "regression"}}}
        one_of_validator = model_validator(mode="before")(check_one_of)
        binary_crossentropy: "CMsgSteamLearn_InferenceBackend_Response.BinaryCrossEntropyOutput" = Field()
        categorical_crossentropy: "CMsgSteamLearn_InferenceBackend_Response.CategoricalCrossEntropyOutput" = Field()
        multi_binary_crossentropy: "CMsgSteamLearn_InferenceBackend_Response.MutliBinaryCrossEntropyOutput" = Field()
        regression: "CMsgSteamLearn_InferenceBackend_Response.RegressionOutput" = Field()

    outputs: typing.List[Output] = Field(default_factory=list)

class CMsgSteamLearn_Inference_Response(BaseModel):
    inference_result: ESteamLearnInferenceResult = Field(default=0)
    backend_response: CMsgSteamLearn_InferenceBackend_Response = Field()
    keys: typing.List[int] = Field(default_factory=list)

class CMsgSteamLearn_BatchOperation_Response(BaseModel):
    cache_data_responses: typing.List[CMsgSteamLearn_CacheData_Response] = Field(default_factory=list)
    snapshot_responses: typing.List[CMsgSteamLearn_SnapshotProject_Response] = Field(default_factory=list)
    inference_responses: typing.List[CMsgSteamLearn_Inference_Response] = Field(default_factory=list)

class CMsgSteamLearnAccessTokens(BaseModel):
    class CacheDataAccessToken(BaseModel):
        data_source_id: int = Field(default=0)
        access_token: str = Field(default="")

    class SnapshotProjectAccessToken(BaseModel):
        project_id: int = Field(default=0)
        access_token: str = Field(default="")

    class InferenceAccessToken(BaseModel):
        project_id: int = Field(default=0)
        access_token: str = Field(default="")

    register_data_source_access_token: str = Field(default="")
    cache_data_access_tokens: typing.List["CMsgSteamLearnAccessTokens.CacheDataAccessToken"] = Field(default_factory=list)
    snapshot_project_access_tokens: typing.List["CMsgSteamLearnAccessTokens.SnapshotProjectAccessToken"] = Field(default_factory=list)
    inference_access_tokens: typing.List["CMsgSteamLearnAccessTokens.InferenceAccessToken"] = Field(default_factory=list)

class CMsgSteamLearn_GetAccessTokens_Request(BaseModel):
    appid: int = Field(default=0)

class CMsgSteamLearn_GetAccessTokens_Response(BaseModel):
    result: ESteamLearnGetAccessTokensResult = Field(default=0)
    access_tokens: CMsgSteamLearnAccessTokens = Field()

class CMsgSteamLearn_InferenceMetadata_Request(BaseModel):
    access_token: str = Field(default="")
    project_id: int = Field(default=0)
    published_version: int = Field(default=0)
    override_train_id: int = Field(default=0)

class CMsgSteamLearn_InferenceMetadataBackend_Request(BaseModel):
    project_id: int = Field(default=0)
    fetch_id: int = Field(default=0)

class CMsgSteamLearn_InferenceMetadata_Response(BaseModel):
    class RowRange(BaseModel):
        min_row: int = Field(default=0)
        max_row: int = Field(default=0)

    class Range(BaseModel):
        data_element_path: str = Field(default="")
        min_value: float = Field(default=0.0)
        max_value: float = Field(default=0.0)

    class StdDev(BaseModel):
        data_element_path: str = Field(default="")
        mean: float = Field(default=0.0)
        std_dev: float = Field(default=0.0)

    class CompactTable(BaseModel):
        class Entry(BaseModel):
            value: int = Field(default=0)
            mapping: int = Field(default=0)
            count: int = Field(default=0)

        class MapValuesEntry(BaseModel):
            key: int = Field(default=0)
            value: "CompactTable.Entry" = Field()

        class MapMappingsEntry(BaseModel):
            key: int = Field(default=0)
            value: "CompactTable.Entry" = Field()

        name: str = Field(default="")
        map_values: MapValuesEntry = Field()
        map_mappings: MapMappingsEntry = Field()

    class SequenceTable(BaseModel):
        class Entry(BaseModel):
            values: typing.List[int] = Field(default_factory=list)
            crc: int = Field(default=0)
            count: int = Field(default=0)

        class MapValuesEntry(BaseModel):
            key: int = Field(default=0)
            value: "SequenceTable.Entry" = Field()

        class MapMappingsEntry(BaseModel):
            key: str = Field(default="")
            value: "SequenceTable.Entry" = Field()

        name: str = Field(default="")
        map_values: MapValuesEntry = Field()
        map_mappings: MapMappingsEntry = Field()
        total_count: int = Field(default=0)

    class KMeans(BaseModel):
        class Cluster(BaseModel):
            x: float = Field(default=0.0)
            y: float = Field(default=0.0)
            radius: float = Field(default=0.0)
            radius_75pct: float = Field(default=0.0)
            radius_50pct: float = Field(default=0.0)
            radius_25pct: float = Field(default=0.0)

        name: str = Field(default="")
        clusters: typing.List[Cluster] = Field(default_factory=list)

    class SnapshotHistogram(BaseModel):
        min_value: float = Field(default=0.0)
        max_value: float = Field(default=0.0)
        num_buckets: int = Field(default=0)
        bucket_counts: typing.List[int] = Field(default_factory=list)

    class AppInfo(BaseModel):
        country_allow: str = Field(default="")
        country_deny: str = Field(default="")
        platform_win: bool = Field(default=False)
        platform_mac: bool = Field(default=False)
        platform_linux: bool = Field(default=False)
        adult_violence: bool = Field(default=False)
        adult_sex: bool = Field(default=False)

    class AppInfoEntry(BaseModel):
        key: int = Field(default=0)
        value: "CMsgSteamLearn_InferenceMetadata_Response.AppInfo" = Field()

    inference_metadata_result: ESteamLearnInferenceMetadataResult = Field(default=0)
    row_range: "CMsgSteamLearn_InferenceMetadata_Response.RowRange" = Field()
    ranges: typing.List["CMsgSteamLearn_InferenceMetadata_Response.Range"] = Field(default_factory=list)
    std_devs: typing.List["CMsgSteamLearn_InferenceMetadata_Response.StdDev"] = Field(default_factory=list)
    compact_tables: typing.List["CMsgSteamLearn_InferenceMetadata_Response.CompactTable"] = Field(default_factory=list)
    sequence_tables: typing.List["CMsgSteamLearn_InferenceMetadata_Response.SequenceTable"] = Field(default_factory=list)
    kmeans: typing.List["CMsgSteamLearn_InferenceMetadata_Response.KMeans"] = Field(default_factory=list)
    app_info: "CMsgSteamLearn_InferenceMetadata_Response.AppInfoEntry" = Field()
    snapshot_histogram: "CMsgSteamLearn_InferenceMetadata_Response.SnapshotHistogram" = Field()
