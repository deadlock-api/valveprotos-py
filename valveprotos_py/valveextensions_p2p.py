# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from enum import IntEnum
from pydantic import BaseModel

class EProtoDebugVisiblity(IntEnum):
    k_EProtoDebugVisibility_Always = 0
    k_EProtoDebugVisibility_Server = 70
    k_EProtoDebugVisibility_ValveServer = 80
    k_EProtoDebugVisibility_GC = 90
    k_EProtoDebugVisibility_Never = 100
