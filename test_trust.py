#!/usr/bin/python3

filter_path = '/etc/mail/filters/15_trust'


def test_untrusted(run_filter):
    res = run_filter(filter_path)
    assert res.stdout == 'filter did not exit\n'
    assert res.stderr == ''
    assert res.returncode == 0


def test_trusted(run_filter):
    res = run_filter(filter_path, {'SIMTA_ACL_RESULT': 'trust'})
    assert res.stdout == 'logged: 15_trust: trusted host, skipping further tests\n'
    assert res.stderr == ''
    assert res.returncode == 0
