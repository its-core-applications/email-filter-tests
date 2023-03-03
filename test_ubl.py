#!/usr/bin/python3

filter_path = '/etc/mail/filters/21_ubl'


def test_nohit(run_filter):
    res = run_filter(filter_path)
    assert res.stdout == 'filter did not exit\n'
    assert res.stderr == ''
    assert res.returncode == 0


def test_hit(run_filter):
    res = run_filter(filter_path, {'SIMTA_AUTH_ID': 'xX-CutieLoveSoulRipper-Xx'})
    assert res.stdout == 'logged: 21_ubl: xX-CutieLoveSoulRipper-Xx found in ubl.dnsbl: 127.0.0.1 (local policy)\n'
    assert res.stderr == ''
    assert res.returncode == 2
