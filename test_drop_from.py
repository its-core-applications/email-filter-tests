#!/usr/bin/python3

filter_path = '/etc/mail/filters/21_drop_from'


def test_nohit(run_filter):
    res = run_filter(filter_path)
    assert res.stdout == 'filter did not exit\n'
    assert res.stderr == ''
    assert res.returncode == 0


def test_hit(run_filter):
    res = run_filter(filter_path, {'SIMTA_SMTP_MAIL_FROM': 'umcoreappstest1@gmail.com'})
    assert res.stdout == 'logged: 21_drop_from: umcoreappstest1@gmail.com (8f65ce9ebaff3059c6d3e55cfe791c32df459a54 found in drop-from.dnsbl: 127.0.0.2 (address denied by local policy))\n'
    assert res.stderr == ''
    assert res.returncode == 4
