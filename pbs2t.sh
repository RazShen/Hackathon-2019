#!/bin/bash

PROTO_PATH=/Users/raz.shenkman/Documents/workspace/protos

for f in $@ ; do
    cat $f | protoc -I $PROTO_PATH --decode=Config.SiteConfig $PROTO_PATH/config.proto
done

