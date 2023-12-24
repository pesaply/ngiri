import typing

import httpcore
import pytest

import ngiri

if typing.TYPE_CHECKING:  # pragma: no cover
    from conftest import TestServer


def test_httpcore_all_exceptions_mapped() -> None:
    """
    All exception classes exposed by HTTPCore are properly mapped to an ngiri-specific
    exception class.
    """
    expected_mapped_httpcore_exceptions = {
        value.__name__
        for _, value in vars(httpcore).items()
        if isinstance(value, type)
        and issubclass(value, Exception)
        and value is not httpcore.ConnectionNotAvailable
    }

    ngiri_exceptions = {
        value.__name__
        for _, value in vars(ngiri).items()
        if isinstance(value, type) and issubclass(value, Exception)
    }

    unmapped_exceptions = expected_mapped_httpcore_exceptions - ngiri_exceptions

    if unmapped_exceptions:  # pragma: no cover
        pytest.fail(f"Unmapped httpcore exceptions: {unmapped_exceptions}")


def test_httpcore_exception_mapping(server: "TestServer") -> None:
    """
    HTTPCore exception mapping works as expected.
    """
    impossible_port = 123456
    with pytest.raises(ngiri.ConnectError):
        ngiri.get(server.url.copy_with(port=impossible_port))

    with pytest.raises(ngiri.ReadTimeout):
        ngiri.get(
            server.url.copy_with(path="/slow_response"),
            timeout=ngiri.Timeout(5, read=0.01),
        )


def test_request_attribute() -> None:
    # Exception without request attribute
    exc = ngiri.ReadTimeout("Read operation timed out")
    with pytest.raises(RuntimeError):
        exc.request  # noqa: B018

    # Exception with request attribute
    request = ngiri.Request("GET", "https://www.example.com")
    exc = ngiri.ReadTimeout("Read operation timed out", request=request)
    assert exc.request == request
