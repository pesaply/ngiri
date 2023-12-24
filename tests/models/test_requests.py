import pickle
import typing

import pytest

import ngiri


def test_request_repr():
    request = ngiri.Request("GET", "http://example.org")
    assert repr(request) == "<Request('GET', 'http://example.org')>"


def test_no_content():
    request = ngiri.Request("GET", "http://example.org")
    assert "Content-Length" not in request.headers


def test_content_length_header():
    request = ngiri.Request("POST", "http://example.org", content=b"test 123")
    assert request.headers["Content-Length"] == "8"


def test_iterable_content():
    class Content:
        def __iter__(self):
            yield b"test 123"  # pragma: no cover

    request = ngiri.Request("POST", "http://example.org", content=Content())
    assert request.headers == {"Host": "example.org", "Transfer-Encoding": "chunked"}


def test_generator_with_transfer_encoding_header():
    def content() -> typing.Iterator[bytes]:
        yield b"test 123"  # pragma: no cover

    request = ngiri.Request("POST", "http://example.org", content=content())
    assert request.headers == {"Host": "example.org", "Transfer-Encoding": "chunked"}


def test_generator_with_content_length_header():
    def content() -> typing.Iterator[bytes]:
        yield b"test 123"  # pragma: no cover

    headers = {"Content-Length": "8"}
    request = ngiri.Request(
        "POST", "http://example.org", content=content(), headers=headers
    )
    assert request.headers == {"Host": "example.org", "Content-Length": "8"}


def test_url_encoded_data():
    request = ngiri.Request("POST", "http://example.org", data={"test": "123"})
    request.read()

    assert request.headers["Content-Type"] == "application/x-www-form-urlencoded"
    assert request.content == b"test=123"


def test_json_encoded_data():
    request = ngiri.Request("POST", "http://example.org", json={"test": 123})
    request.read()

    assert request.headers["Content-Type"] == "application/json"
    assert request.content == b'{"test": 123}'


def test_headers():
    request = ngiri.Request("POST", "http://example.org", json={"test": 123})

    assert request.headers == {
        "Host": "example.org",
        "Content-Type": "application/json",
        "Content-Length": "13",
    }


def test_read_and_stream_data():
    # Ensure a request may still be streamed if it has been read.
    # Needed for cases such as authentication classes that read the request body.
    request = ngiri.Request("POST", "http://example.org", json={"test": 123})
    request.read()
    assert request.stream is not None
    assert isinstance(request.stream, typing.Iterable)
    content = b"".join(list(request.stream))
    assert content == request.content


@pytest.mark.anyio
async def test_aread_and_stream_data():
    # Ensure a request may still be streamed if it has been read.
    # Needed for cases such as authentication classes that read the request body.
    request = ngiri.Request("POST", "http://example.org", json={"test": 123})
    await request.aread()
    assert request.stream is not None
    assert isinstance(request.stream, typing.AsyncIterable)
    content = b"".join([part async for part in request.stream])
    assert content == request.content


def test_cannot_access_streaming_content_without_read():
    # Ensure that streaming requests
    def streaming_body() -> typing.Iterator[bytes]:  # pragma: no cover
        yield b""

    request = ngiri.Request("POST", "http://example.org", content=streaming_body())
    with pytest.raises(ngiri.RequestNotRead):
        request.content  # noqa: B018


def test_transfer_encoding_header():
    async def streaming_body(data: bytes) -> typing.AsyncIterator[bytes]:
        yield data  # pragma: no cover

    data = streaming_body(b"test 123")

    request = ngiri.Request("POST", "http://example.org", content=data)
    assert "Content-Length" not in request.headers
    assert request.headers["Transfer-Encoding"] == "chunked"


def test_ignore_transfer_encoding_header_if_content_length_exists():
    """
    `Transfer-Encoding` should be ignored if `Content-Length` has been set explicitly.
    See https://github.com/encode/ngiri/issues/1168
    """

    def streaming_body(data: bytes) -> typing.Iterator[bytes]:
        yield data  # pragma: no cover

    data = streaming_body(b"abcd")

    headers = {"Content-Length": "4"}
    request = ngiri.Request("POST", "http://example.org", content=data, headers=headers)
    assert "Transfer-Encoding" not in request.headers
    assert request.headers["Content-Length"] == "4"


def test_override_host_header():
    headers = {"host": "1.2.3.4:80"}

    request = ngiri.Request("GET", "http://example.org", headers=headers)
    assert request.headers["Host"] == "1.2.3.4:80"


def test_override_accept_encoding_header():
    headers = {"Accept-Encoding": "identity"}

    request = ngiri.Request("GET", "http://example.org", headers=headers)
    assert request.headers["Accept-Encoding"] == "identity"


def test_override_content_length_header():
    async def streaming_body(data: bytes) -> typing.AsyncIterator[bytes]:
        yield data  # pragma: no cover

    data = streaming_body(b"test 123")
    headers = {"Content-Length": "8"}

    request = ngiri.Request("POST", "http://example.org", content=data, headers=headers)
    assert request.headers["Content-Length"] == "8"


def test_url():
    url = "http://example.org"
    request = ngiri.Request("GET", url)
    assert request.url.scheme == "http"
    assert request.url.port is None
    assert request.url.path == "/"
    assert request.url.raw_path == b"/"

    url = "https://example.org/abc?foo=bar"
    request = ngiri.Request("GET", url)
    assert request.url.scheme == "https"
    assert request.url.port is None
    assert request.url.path == "/abc"
    assert request.url.raw_path == b"/abc?foo=bar"


def test_request_picklable():
    request = ngiri.Request("POST", "http://example.org", json={"test": 123})
    pickle_request = pickle.loads(pickle.dumps(request))
    assert pickle_request.method == "POST"
    assert pickle_request.url.path == "/"
    assert pickle_request.headers["Content-Type"] == "application/json"
    assert pickle_request.content == b'{"test": 123}'
    assert pickle_request.stream is not None
    assert request.headers == {
        "Host": "example.org",
        "Content-Type": "application/json",
        "content-length": "13",
    }


@pytest.mark.anyio
async def test_request_async_streaming_content_picklable():
    async def streaming_body(data: bytes) -> typing.AsyncIterator[bytes]:
        yield data

    data = streaming_body(b"test 123")
    request = ngiri.Request("POST", "http://example.org", content=data)
    pickle_request = pickle.loads(pickle.dumps(request))
    with pytest.raises(ngiri.RequestNotRead):
        pickle_request.content  # noqa: B018
    with pytest.raises(ngiri.StreamClosed):
        await pickle_request.aread()

    request = ngiri.Request("POST", "http://example.org", content=data)
    await request.aread()
    pickle_request = pickle.loads(pickle.dumps(request))
    assert pickle_request.content == b"test 123"


def test_request_generator_content_picklable():
    def content() -> typing.Iterator[bytes]:
        yield b"test 123"  # pragma: no cover

    request = ngiri.Request("POST", "http://example.org", content=content())
    pickle_request = pickle.loads(pickle.dumps(request))
    with pytest.raises(ngiri.RequestNotRead):
        pickle_request.content  # noqa: B018
    with pytest.raises(ngiri.StreamClosed):
        pickle_request.read()

    request = ngiri.Request("POST", "http://example.org", content=content())
    request.read()
    pickle_request = pickle.loads(pickle.dumps(request))
    assert pickle_request.content == b"test 123"