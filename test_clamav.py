#!/usr/bin/python3

filter_path = '/etc/mail/filters/80_clamav'


def test_basic(run_filter):
    res = run_filter(filter_path)
    assert res.stdout == 'filter did not exit\n'
    assert res.stderr == ''
    assert res.returncode == 0
