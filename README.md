What
----

This is a tool help you to check URL, http error codes or redirects


Install
-------

```
./install.sh
```

or

```
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```


Usage
-----

```
$ ./check_url.py example.csv
https://www.github.com/ ✅ => https://github.com/
https://github.com/ ✅ => 200
https://github.com/not-url ✅ => 404
http://github.com/ 😡 => https://github.com/ != 200
DNS entry not exist: http://example-not-exist.com/ (HTTPConnectionPool(host='example-not-exist.com', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x106760af0>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known')))
http://example-not-exist.com/ 😡 => DNS entry not exist != 200
No TLS: https://bad-tls.ledez.net/ (HTTPSConnectionPool(host='bad-tls.ledez.net', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLCertVerificationError("hostname 'bad-tls.ledez.net' doesn't match 'archive-blog-staging.ledez.net'"))))
https://bad-tls.ledez.net/ 😡 => TLS Error != 200

Errors summary:
http://github.com/;https://github.com/
http://example-not-exist.com/;DNS entry not exist
https://bad-tls.ledez.net/;TLS Error
```
