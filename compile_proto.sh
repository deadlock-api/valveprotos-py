#!/bin/bash

protoc --proto_path=protos/deadlock/ --python_out=valveprotos_py/ --pyi_out=valveprotos_py/ --plugin=protoc-gen-protobuf-to-pydantic=.venv/bin/protoc-gen-protobuf-to-pydantic protos/deadlock/* --protobuf-to-pydantic_out=valveprotos_py/
