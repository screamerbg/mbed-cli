# Copyright (c) 2016 ARM Limited, All Rights Reserved
# SPDX-License-Identifier: Apache-2.0

# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License.

# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software 
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, 
# either express or implied.

from util import *

test_import_urls = {
    'git': 'https://github.com/ARMmbed/mbed-os-example-blinky',
    'hg': 'https://developer.mbed.org/teams/Morpheus/code/mbed-Client-Morpheus-hg',
    'bld': 'https://developer.mbed.org/users/samux/code/USBSerial_HelloWorld'
}

test_import_ls = {
    'git': [
        "import-test-git",
        "`- mbed-os",
    ],
    'hg': [
        "import-test-hg",
        "`- mbed-os",
        "   |- core",
        "   |  |- mbed-rtos",
        "   |  |- mbed-uvisor",
        "   |  `- mbedtls",
        "   |- hal",
        "   |  `- targets/TARGET_Freescale",
        "   |     |- TARGET_KPSDK_MCUS",
        "   |     `- TARGET_MCU_K64F",
        "   |- net",
        "   |  |- ESP8266Interface",
        "   |  |  `- ESP8266",
        "   |  |     `- ATParser",
        "   |  |        `- BufferedSerial",
        "   |  |           `- Buffer",
        "   |  |- LWIPInterface",
        "   |  |  |- lwip",
        "   |  |  |- lwip-eth",
        "   |  |  `- lwip-sys",
        "   |  |- NetworkSocketAPI",
        "   |  |  `- DnsQuery",
        "   |  |- mbed-client",
        "   |  |- mbed-client-c",
        "   |  |- mbed-client-classic",
        "   |  |- mbed-client-mbedtls",
        "   |  |- mbed-trace",
        "   |  `- nanostack-libservice",
        "   `- tools",
    ],
    'bld': [
        "import-test-bld",
        "|- USBDevice",
        "`- mbed",
    ],
}

test_update_revs = {
    'git': ['mbed-os-5.1.1', 'master'],
    'hg': ['b02527cafcde8612ff051fea57e9975aca598807', ''],
    'bld': ['7', ''],
}

test_compile_mcus = {
    'git': ['K64F'],
    'hg': ['K64F'],
    'bld': ['LPC1768'],
}

# Tests 'mbed import'
def test_import_update(mbed, testscm):
    scm = testscm
    name = 'import-test-' + scm

    # First import
    popen(['python', mbed, 'import', test_import_urls[scm], name])
    assertls(mbed, name, test_import_ls[scm])

    # Update to specific hashes/tags
    with cd(name):
        for rev in test_update_revs[scm]:
            popen(['python', mbed, 'update', rev, '--clean'])
    assertls(mbed, name, test_import_ls[scm])

    with cd(name):
        popen(['python', mbed, 'ls'])
        popen(['python', mbed, 'releases'])
        popen(['python', mbed, 'compile', '-S'])
        popen(['python', mbed, 'target', '-S'])
        popen(['python', mbed, 'toolchain', '-S'])
        popen(['python', mbed, 'export', '-S'])

    # Compile with the codebase
    with cd(name):
        for mcu in test_compile_mcus[scm]:
            popen(['python', mbed, 'compile', '-m', mcu])
