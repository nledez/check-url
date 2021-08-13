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
Summary:
http://github.com/;https://github.com/
```
