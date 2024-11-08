#!/bin/bash

protoc --proto_path=protos/deadlock/ --python_out=valveprotos_py/ --pyi_out=valveprotos_py/ protos/deadlock/*
