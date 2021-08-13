#!/usr/bin/env python

import paramiko
import requests
import socket
import sys


def get_http_result(url):
    try:
        r = requests.get(url, allow_redirects=False)
    except requests.exceptions.SSLError as e:
        print('No TLS: {} ({})'.format(url, e))
        return ('TLS Error', '')
    except requests.exceptions.ConnectionError as e:
        print('DNS entry not exist: {} ({})'.format(url, e))
        return ('DNS entry not exist', '')

    if r.is_redirect:
        return (r.headers['Location'], '')
    else:
        return (str(r.status_code), r.content.decode('raw_unicode_escape'))


def check_http(url, http_expectation):
    (http_code, http_text) = get_http_result(url)

    if http_expectation.find('|') != -1:
        http_got = '{}|{}'.format(http_code, http_text)
    else:
        http_got = http_code

    if http_got != http_expectation:
        print('{} 😡 => {} != {}'.format(url, http_got, http_expectation))
        return '{};{}'.format(url, http_got)
    else:
        print('{} ✅ => {}'.format(url, http_got))
        return False

## Example for ssh
## ===============
#def check_ssh(hostname, user, private_key, command='hostname'):
#    client = paramiko.SSHClient()
#    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
#    client.connect(hostname,
#                   username=user,
#                   key_filename=private_key)
#
#    chan = client.get_transport().open_session()
#    chan.exec_command(command)
#    key = True
#    while key:
#        if chan.recv_ready():
#            print("recv:\n%s" % chan.recv(4096).decode('ascii'))
#        if chan.recv_stderr_ready():
#            print("error:\n%s" % chan.recv_stderr(4096).decode('ascii'))
#        if chan.exit_status_ready():
#            print("exit status: %s" % chan.recv_exit_status())
#            key = False
#            client.close()
#
#    client.close()
#
# result = check_ssh('ssh-host', 'user', 'ssh-private-key')

redirect_in_error = []

if len(sys.argv) >= 2:
    file_to_check = sys.argv[1]
else:
    file_to_check = 'list_url.csv'

try:
    csv_list = open(file_to_check)
except IOError:
    print("Can't open {}".format(file_to_check))
    sys.exit(1)

for line in csv_list.readlines():
    print('\n')
    (url, http_expected) = line.rstrip().split(';')
    redirects = check_http(url, http_expected)
    if redirects:
        redirect_in_error.append(redirects)

if len(redirect_in_error) > 0:
    print
    print('\n\nSummary, list of errors:\n========')

    for redirect in redirect_in_error:
        print(redirect)
