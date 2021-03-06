#   Copyright 2020 The KNIX Authors
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import sys

PYTHON_VERSION = sys.version_info

def is_string(string):
    if PYTHON_VERSION >= (3, ):
        return isinstance(string, str)

    return isinstance(string, basestring)

def ensure_long(value):
    if PYTHON_VERSION >= (3, ):
        return int(value)

    return long(value)
