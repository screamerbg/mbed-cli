# Copyright (c) 2016 ARM Limited, All Rights Reserved
# SPDX-License-Identifier: Apache-2.0

# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License.

# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software 
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, 
# either express or implied.

from util import *

# Tests 'mbed new'
def test_new(mbed, testscm):
    scm = testscm
    if scm not in ['git', 'hg']:
        return
    base = 'new-test-' + scm

    name = base + '-1'
    popen(['python', mbed, 'new', name, '--scm', scm])
    assertls(mbed, name, [
        name,
        "`- mbed-os",
    ])

    name = base + '-2'
    popen(['python', mbed, 'new', name, '--scm', scm])
    assertls(mbed, name, [
        name,
        "`- mbed-os",
    ])