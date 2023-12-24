# Exceptions

This page lists exceptions that may be raised when using ngiri.

For an overview of how to work with ngiri exceptions, see [Exceptions (Quickstart)](quickstart.md#exceptions).

## The exception hierarchy

* HTTPError
    * RequestError
        * TransportError
            * TimeoutException
                * ConnectTimeout
                * ReadTimeout
                * WriteTimeout
                * PoolTimeout
            * NetworkError
                * ConnectError
                * ReadError
                * WriteError
                * CloseError
            * ProtocolError
                * LocalProtocolError
                * RemoteProtocolError
            * ProxyError
            * UnsupportedProtocol
        * DecodingError
        * TooManyRedirects
    * HTTPStatusError
* InvalidURL
* CookieConflict
* StreamError
    * StreamConsumed
    * ResponseNotRead
    * RequestNotRead
    * StreamClosed

---

## Exception classes

::: ngiri.HTTPError
    :docstring:

::: ngiri.RequestError
    :docstring:

::: ngiri.TransportError
    :docstring:

::: ngiri.TimeoutException
    :docstring:

::: ngiri.ConnectTimeout
    :docstring:

::: ngiri.ReadTimeout
    :docstring:

::: ngiri.WriteTimeout
    :docstring:

::: ngiri.PoolTimeout
    :docstring:

::: ngiri.NetworkError
    :docstring:

::: ngiri.ConnectError
    :docstring:

::: ngiri.ReadError
    :docstring:

::: ngiri.WriteError
    :docstring:

::: ngiri.CloseError
    :docstring:

::: ngiri.ProtocolError
    :docstring:

::: ngiri.LocalProtocolError
    :docstring:

::: ngiri.RemoteProtocolError
    :docstring:

::: ngiri.ProxyError
    :docstring:

::: ngiri.UnsupportedProtocol
    :docstring:

::: ngiri.DecodingError
    :docstring:

::: ngiri.TooManyRedirects
    :docstring:

::: ngiri.HTTPStatusError
    :docstring:

::: ngiri.InvalidURL
    :docstring:

::: ngiri.CookieConflict
    :docstring:

::: ngiri.StreamError
    :docstring:

::: ngiri.StreamConsumed
    :docstring:

::: ngiri.StreamClosed
    :docstring:

::: ngiri.ResponseNotRead
    :docstring:

::: ngiri.RequestNotRead
    :docstring:
