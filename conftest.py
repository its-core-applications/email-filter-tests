#!/usr/bin/env python3

import os
import subprocess

import pytest


@pytest.fixture(scope='session')
def files_dir():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'files')


@pytest.fixture
def run_filter():
    def _run_filter(path, extra_env={}):
        fake_mscan = f'''
MESSAGE_ACCEPT=0
MESSAGE_TEMPFAIL=1
MESSAGE_REJECT=2
MESSAGE_DELETE=4
MESSAGE_DISCONNECT=8
MESSAGE_TARPIT=16
MESSAGE_JAIL=32
MESSAGE_BOUNCE=64

log() {{
    echo "logged: $*"
}}

filter_exit() {{
    exit $1
}}

. {path}

echo "filter did not exit"
exit $MESSAGE_ACCEPT
'''

        env = {
            'SIMTA_DFILE': '',
            'SIMTA_TFILE': '',
            'SIMTA_REMOTE_IP': '127.0.0.1',
            'SIMTA_REMOTE_HOSTNAME': 'localhost.example.com',
            'SIMTA_REVERSE_LOOKUP': '0',
            # SIMTA_ACL_RESULT
            'SIMTA_SMTP_MAIL_FROM': 'flowerysong@example.com',
            'SIMTA_SMTP_HELO': 'mx.example.com',
            'SIMTA_HEADER_FROM': 'flowerysong@example.com',
            'SIMTA_MID': '11223344@example.com',
            'SIMTA_UID': 'DEAD60FF',
            'SIMTA_PID': '666',
            'SIMTA_CID': '1337',
            'SIMTA_WRITE_BEFORE_BANNER': '0',
            # SIMTA_AUTH_ID
            'SIMTA_CHECKSUM': '3177546c74e4f0062909eae43d948bfc',
            'SIMTA_CHECKSUM_SIZE': '1024',
            'SIMTA_BODY_CHECKSUM': 'dead60ff74e4f0062909eae43d948bfc',
            'SIMTA_BODY_CHECKSUM_SIZE': '512',
            'SIMTA_BAD_HEADERS': '0',
            # SIMTA_SPF_RESULT
            # SIMTA_SPF_DOMAIN
            # SIMTA_DMARC_RESULT
            # SIMTA_DMARC_DOMAIN
            # SIMTA_DKIM_DOMAINS
        }

        env.update(extra_env)

        return subprocess.run(
            '/bin/dash',
            input=fake_mscan,
            capture_output=True,
            text=True,
            env=env,
        )

    return _run_filter
