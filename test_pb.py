#!/usr/bin/python3

filter_path = '/etc/mail/filters/70_pb'


def test_basic(run_filter):
    res = run_filter(filter_path)
    assert res.stdout.startswith('logged: 70_pb: PenaltyBox:')
    assert res.stderr == ''
    assert res.returncode == 1
