#!/usr/bin/python3

import os


filter_path = '/etc/mail/filters/45_akira'


def test_nohit(run_filter, files_dir):
    res = run_filter(filter_path, {'SIMTA_DFILE': os.path.join(files_dir, 'd_akira_nohit')})
    assert res.stdout == 'filter did not exit\n'
    assert res.stderr == ''
    assert res.returncode == 0


def test_hit(run_filter, files_dir):
    res = run_filter(filter_path, {'SIMTA_DFILE': os.path.join(files_dir, 'd_akira_hit')})
    assert res.stdout == 'logged: 45_akira: matched deletion criteria\n'
    assert res.stderr == ''
    assert res.returncode == 4


def test_hit_umich(run_filter, files_dir):
    res = run_filter(filter_path, {
        'SIMTA_DFILE': os.path.join(files_dir, 'd_akira_hit'),
        'SIMTA_SMTP_MAIL_FROM': 'postmaster@umich.edu',
    })
    assert res.stdout == 'filter did not exit\n'
    assert res.stderr == ''
    assert res.returncode == 0
