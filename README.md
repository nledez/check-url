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
$ ./check_url.py ./list_url.csv

https://www.github.com/ ✅ => https://github.com/


https://github.com/ ✅ => 200


https://github.com/not-url ✅ => 404


http://github.com/ 😡 => https://github.com/ != 200


DNS entry not exist: http://jeijejieijejiwjaijaajeajajiajajajajia.com/ (HTTPConnectionPool(host
='jeijejieijejiwjaijaajeajajiajajajajia.com', port=80): Max retries exceeded with url: / (Cause
d by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f71e4af8910>: Failed t
o establish a new connection: [Errno -2] Name or service not known')))
http://jeijejieijejiwjaijaajeajajiajajajajia.com/ 😡 => DNS entry not exist != 200


No TLS: https://toto.sogilis.com/ (HTTPSConnectionPool(host='toto.sogilis.com', port=443): Max
retries exceeded with url: / (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of p
rotocol (_ssl.c:1129)'))))
https://toto.sogilis.com/ 😡 => TLS Error != 200


Summary, list of errors:
========
http://github.com/;https://github.com/
http://jeijejieijejiwjaijaajeajajiajajajajia.com/;DNS entry not exist
https://toto.sogilis.com/;TLS Error

```
