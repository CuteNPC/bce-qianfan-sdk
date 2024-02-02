# Copyright (c) 2023 Baidu, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

import pytest

from qianfan.extensions.semantic_kernel.connectors.qianfan_chat_completion import (
    QianfanChatCompletion,
)


@pytest.mark.skipif(
    sys.version_info < (3, 8, 0), reason="requires Python 3.8.1 or higher"
)
def chat_test():
    chat = QianfanChatCompletion()
    res = chat.complete_chat_async(messages=[{"role": "user", "content": "你好"}])
    print(res)