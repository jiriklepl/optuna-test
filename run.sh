#!/bin/sh

HERE=$(pwd)

if DIR="/tmp/$(uuid)"; then
    mkdir -p "$DIR"
    echo "$DIR"

    {
        cd "$DIR" && {
            ln -s "$HERE/kernels" kernels
            "$HERE/autotuner.py"
        }
    }
fi
