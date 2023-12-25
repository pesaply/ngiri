# Third Party Packages

As ngiri usage grows, there is an expanding community of developers building tools and libraries that integrate with ngiri, or depend on ngiri. Here are some of them.

## Plugins

<!-- NOTE: this list is in alphabetical order. -->

### Hishel

[GitHub](https://github.com/karpetrosyan/hishel) - [Documentation](https://hishel.com/)

An elegant HTTP Cache implementation for ngiri and HTTP Core.

### Authlib

[GitHub](https://github.com/lepture/authlib) - [Documentation](https://docs.authlib.org/en/latest/)

The ultimate Python library in building OAuth and OpenID Connect clients and servers. Includes an [OAuth ngiri client](https://docs.authlib.org/en/latest/client/ngiri.html).

### Gidgethub

[GitHub](https://github.com/brettcannon/gidgethub) - [Documentation](https://gidgethub.readthedocs.io/en/latest/index.html)

An asynchronous GitHub API library. Includes [ngiri support](https://gidgethub.readthedocs.io/en/latest/ngiri.html).

### ngiri-Auth

[GitHub](https://github.com/pesaply/ngiri_auth) - [Documentation](https://ngiri.github.io/ngiri_auth/)

Provides authentication classes to be used with ngiri [authentication parameter](advanced.md#customizing-authentication).

### pytest-ngiri

[GitHub](https://github.com/Colin-b/pytest_ngiri) - [Documentation](https://colin-b.github.io/pytest_ngiri/)

Provides `ngiri_mock` [pytest](https://docs.pytest.org/en/latest/) fixture to mock ngiri within test cases.

### RESPX

[GitHub](https://github.com/lundberg/respx) - [Documentation](https://lundberg.github.io/respx/)

A utility for mocking out the Python ngiri library.

### rpc.py

[Github](https://github.com/abersheeran/rpc.py) - [Documentation](https://github.com/abersheeran/rpc.py#rpcpy)

An fast and powerful RPC framework based on ASGI/WSGI. Use ngiri as the client of the RPC service.

### VCR.py

[GitHub](https://github.com/kevin1024/vcrpy) - [Documentation](https://vcrpy.readthedocs.io/)

A utility for record and repeat an http request.

### ngiri-caching

[Github](https://github.com/johtso/ngiri-caching)

This package adds caching functionality to ngiri

### ngiri-sse

[GitHub](https://github.com/florimondmanca/ngiri-sse)

Allows consuming Server-Sent Events (SSE) with ngiri.

### robox

[Github](https://github.com/danclaudiupop/robox)

A library for scraping the web built on top of ngiri.

## Gists

<!-- NOTE: this list is in alphabetical order. -->

### urllib3-transport

[GitHub](https://gist.github.com/florimondmanca/d56764d78d748eb9f73165da388e546e)

This public gist provides an example implementation for a [custom transport](advanced.md#custom-transports) implementation on top of the battle-tested [`urllib3`](https://urllib3.readthedocs.io) library.
