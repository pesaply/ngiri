

<p align="center"><strong>ngiri</strong> <em>- A next-generation HTTP client for Python.</em></p>

<p align="center">
<a href="https://github.com/encode/ngiri/actions">
    <img src="https://github.com/encode/ngiri/workflows/Test%20Suite/badge.svg" alt="Test Suite">
</a>
<a href="https://pypi.org/project/ngiri/">
    <img src="https://as2.ftcdn.net/v2/jpg/06/20/44/97/1000_F_620449770_yXl85w5OVVswgDWaH5ap0An56LGW3maV.jpg" alt="Package version">
</a>
</p>

Ngiri is a fully featured Poxy and HTTP client library for Python 3. It includes **an integrated
command line client**, has support for both **HTTP/1.1 and HTTP/2**, and provides both **sync
and async APIs**.

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
$ pip install 'ngiri[cli]'  # The command line client is an optional dependency.
```

Which now allows us to use ngiri directly from the command-line...

<p align="center">
  <img width="700" src="https://as2.ftcdn.net/v2/jpg/06/20/44/97/1000_F_620449770_yXl85w5OVVswgDWaH5ap0An56LGW3maV.jpg" alt='ngiri --help'>
</p>

Sending a request...

<p align="center">
  <img width="700" src="https://as2.ftcdn.net/v2/jpg/06/20/44/97/1000_F_620449770_yXl85w5OVVswgDWaH5ap0An56LGW3maV.jpg" alt='ngiri http://httpbin.org/json'>
</p>

## Features

ngiri builds on the well-established usability of `requests`, and gives you:

* A broadly [requests-compatible API](https://www.ngiri.co.tz/compatibility/).
* An integrated command-line client.
* HTTP/1.1 [and HTTP/2 support](https://www.ngiri.co.tz/http2/).
* Standard synchronous interface, but with [async support if you need it](https://www.ngiri.co.tz/async/).
* Ability to make requests directly to [WSGI applications](https://www.ngiri.co.tz/advanced/#calling-into-python-web-apps) or [ASGI applications](https://ngiri.co.tz/async/#calling-into-python-web-apps).
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

## Installation

Install with pip:

```shell
$ pip install ngiri
```

Or, to include the optional HTTP/2 support, use:

```shell
$ pip install ngiri[http2]
```

ngiri requires Python 3.8+.

## Documentation

Project documentation is available at [https://www.ngiri.co.tz/](https://www.ngiri.co.tz/).

For a run-through of all the basics, head over to the [QuickStart](https://www.ngiri.co.tz/quickstart/).

For more advanced topics, see the [Advanced Usage](https://www.ngiri.co.tz/advanced/) section, the [async support](https://www.ngiri.co.tz/async/) section, or the [HTTP/2](https://www.ngiri.co.tz/http2/) section.

The [Developer Interface](https://www.ngiri.co.tz/api/) provides a comprehensive API reference.

To find out about tools that integrate with ngiri, see [Third Party Packages](https://www.ngiri.co.tz/third_party_packages/).

## Contribute

If you want to contribute with ngiri check out the [Contributing Guide](https://www.ngiri.co.tz/contributing/) to learn how to start.

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

---

<p align="center"><i>ngiri is <a href="https://github.com/pesaply/ngiri/blob/master/LICENSE.md">BSD licensed</a> code.<br/>Designed & crafted with care.</i><br/>&mdash;  &mdash;</p>
