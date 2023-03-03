#!/usr/bin/python3

import os


filter_path = '/etc/mail/filters/40_string'


def test_nohit(run_filter, files_dir):
    res = run_filter(filter_path, {'SIMTA_DFILE': os.path.join(files_dir, 'd_string_nohit')})
    assert res.stdout == 'filter did not exit\n'
    assert res.stderr == ''
    assert res.returncode == 0


def test_hit(run_filter, files_dir):
    res = run_filter(filter_path, {'SIMTA_DFILE': os.path.join(files_dir, 'd_string_hit')})
    assert res.stdout == 'logged: 40_string: /etc/mail/string.deny matched sibboleth\n'
    assert res.stderr == ''
    assert res.returncode == 1
