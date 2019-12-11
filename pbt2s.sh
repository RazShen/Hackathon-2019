#!/bin/bash

PROTO_PATH=/Users/raz.shenkman/Documents/workspace/protos

cat $1 | protoc -I $PROTO_PATH --encode=Config.SiteConfig $PROTO_PATH/config.proto

