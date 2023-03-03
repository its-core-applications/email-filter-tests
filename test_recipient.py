#!/usr/bin/python3

import os

filter_path = '/etc/mail/filters/35_recipient'


def test_untrusted(run_filter):
    res = run_filter(filter_path)
    assert res.stdout == 'filter did not exit\n'
    assert res.stderr == ''
    assert res.returncode == 0


def test_blocked(run_filter, files_dir):
    res = run_filter(filter_path, {'SIMTA_TFILE': os.path.join(files_dir, 't_recipient_block')})
    assert res.stdout == 'logged: 35_recipient: /etc/mail/recipient.deny matched postmaster@example.com\n'
    assert res.stderr == ''
    assert res.returncode == 2


def test_trusted(run_filter, files_dir):
    res = run_filter(filter_path, {'SIMTA_TFILE': os.path.join(files_dir, 't_recipient_trust')})
    assert res.stdout == 'logged: 35_recipient: /etc/mail/recipient.trust matched postmaster@umich.edu\n'
    assert res.stderr == ''
    assert res.returncode == 0
