#!/usr/bin/env bash

export PLATFORM=ANDROID

python3 -m pytest tests/ui/test_demo.py::test_login_with_login_and_password -l -vv --tb=short
