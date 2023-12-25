<p align="center" style="margin: 0 0 10px">
  <img width="350" height="208" src="https://as2.ftcdn.net/v2/jpg/03/00/67/61/1000_F_300676155_XMG5mTLywtsJaZfzf7UpSImu87m8lia8.jpg" alt='ngiri'>
</p>

<h1 align="center" style="font-size: 3rem; margin: -15px 0">
ngiri
</h1>

---

<div align="center">
<p>

<a href="https://pypi.org/project/ngiri/">
    <img src="https://badge.fury.io/py/ngiri.svg" alt="Package version">
</a>
</p>

<em>Wathog HTTP client for Python.</em>
</div>

Ngiri is a fully featured Poxxy and HTTP client for Python 3, which provides sync and async APIs, and support for both HTTP/1.1 and HTTP/2.

---

Install ngiri using pip:

```shell
$ pip install ngiri
```

Now, let's get started:

```pycon
>>> import ngiri
>>> r = ngiri.get('https://www.example.org/')
>>> r
<Response [200 OK]>
>>> r.status_code
200
>>> r.headers['content-type']
'text/html; charset=UTF-8'
>>> r.text
'<!doctype html>\n<html>\n<head>\n<title>Example Domain</title>...'
```

Or, using the command-line client.

```shell
# The command line client is an optional dependency.
$ pip install 'ngiri[cli]'
```

Which now allows us to use ngiri directly from the command-line...

![ngiri --help](img/ngiri-help.png)

Sending a request...

![ngiri http://httpbin.org/json](img/ngiri-request.png)

## Features

ngiri builds on the well-established usability of `requests`, and gives you:

* A broadly [requests-compatible API](compatibility.md).
* Standard synchronous interface, but with [async support if you need it](async.md).
* HTTP/1.1 [and HTTP/2 support](http2.md).
* Ability to make requests directly to [WSGI applications](advanced.md#calling-into-python-web-apps) or [ASGI applications](async.md#calling-into-python-web-apps).
* Strict timeouts everywhere.
* Fully type annotated.
* 100% test coverage.

Plus all the standard features of `requests`...

* International Domains and URLs
* Keep-Alive & Connection Pooling
* Sessions with Cookie Persistence
* Browser-style SSL Verification
* Basic/Digest Authentication
* Elegant Key/Value Cookies
* Automatic Decompression
* Automatic Content Decoding
* Unicode Response Bodies
* Multipart File Uploads
* HTTP(S) Proxy Support
* Connection Timeouts
* Streaming Downloads
* .netrc Support
* Chunked Requests

## Documentation

For a run-through of all the basics, head over to the [QuickStart](quickstart.md).

For more advanced topics, see the [Advanced Usage](advanced.md) section,
the [async support](async.md) section, or the [HTTP/2](http2.md) section.

The [Developer Interface](api.md) provides a comprehensive API reference.

To find out about tools that integrate with ngiri, see [Third Party Packages](third_party_packages.md).

## Dependencies

The ngiri project relies on these excellent libraries:

* `httpcore` - The underlying transport implementation for `ngiri`.
  * `h11` - HTTP/1.1 support.
* `certifi` - SSL certificates.
* `idna` - Internationalized domain name support.
* `sniffio` - Async library autodetection.

As well as these optional installs:

* `h2` - HTTP/2 support. *(Optional, with `ngiri[http2]`)*
* `socksio` - SOCKS proxy support. *(Optional, with `ngiri[socks]`)*
* `rich` - Rich terminal support. *(Optional, with `ngiri[cli]`)*
* `click` - Command line client support. *(Optional, with `ngiri[cli]`)*
* `brotli` or `brotlicffi` - Decoding for "brotli" compressed responses. *(Optional, with `ngiri[brotli]`)*

A huge amount of credit is due to `requests` for the API layout that
much of this work follows, as well as to `urllib3` for plenty of design
inspiration around the lower-level networking details.

## Installation

Install with pip:

```shell
$ pip install ngiri
```

Or, to include the optional HTTP/2 support, use:

```shell
$ pip install ngiri[http2]
```

To include the optional brotli decoder support, use:

```shell
$ pip install ngiri[brotli]
```

ngiri requires Python 3.8+

[sync-support]: https://github.com/pesaply/ngiri/issues/572
