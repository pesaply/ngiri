import typing

import pytest

import ngiri


def test_get(server):
    response = ngiri.get(server.url)
    assert response.status_code == 200
    assert response.reason_phrase == "OK"
    assert response.text == "Habari, Dunia!"
    assert response.http_version == "HTTP/1.1"


def test_post(server):
    response = ngiri.post(server.url, content=b"Habari, Dunia!")
    assert response.status_code == 200
    assert response.reason_phrase == "OK"


def test_post_byte_iterator(server):
    def data() -> typing.Iterator[bytes]:
        yield b"Habari"
        yield b", "
        yield b"Dunia!"

    response = ngiri.post(server.url, content=data())
    assert response.status_code == 200
    assert response.reason_phrase == "OK"


def test_post_byte_stream(server):
    class Data(ngiri.SyncByteStream):
        def __iter__(self):
            yield b"Habari"
            yield b", "
            yield b"Dunia!"

    response = ngiri.post(server.url, content=Data())
    assert response.status_code == 200
    assert response.reason_phrase == "OK"


def test_options(server):
    response = ngiri.options(server.url)
    assert response.status_code == 200
    assert response.reason_phrase == "OK"


def test_head(server):
    response = ngiri.head(server.url)
    assert response.status_code == 200
    assert response.reason_phrase == "OK"


def test_put(server):
    response = ngiri.put(server.url, content=b"Habari, Dunia!")
    assert response.status_code == 200
    assert response.reason_phrase == "OK"


def test_patch(server):
    response = ngiri.patch(server.url, content=b"Habari, Dunia!")
    assert response.status_code == 200
    assert response.reason_phrase == "OK"


def test_delete(server):
    response = ngiri.delete(server.url)
    assert response.status_code == 200
    assert response.reason_phrase == "OK"


def test_stream(server):
    with ngiri.stream("GET", server.url) as response:
        response.read()

    assert response.status_code == 200
    assert response.reason_phrase == "OK"
    assert response.text == "Habari, Dunia!"
    assert response.http_version == "HTTP/1.1"


def test_get_invalid_url():
    with pytest.raises(ngiri.UnsupportedProtocol):
        ngiri.get("invalid://example.org")
