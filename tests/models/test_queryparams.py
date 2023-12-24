import pytest

import ngiri


@pytest.mark.parametrize(
    "source",
    [
        "a=123&a=456&b=789",
        {"a": ["123", "456"], "b": 789},
        {"a": ("123", "456"), "b": 789},
        [("a", "123"), ("a", "456"), ("b", "789")],
        (("a", "123"), ("a", "456"), ("b", "789")),
    ],
)
def test_queryparams(source):
    q = ngiri.QueryParams(source)
    assert "a" in q
    assert "A" not in q
    assert "c" not in q
    assert q["a"] == "123"
    assert q.get("a") == "123"
    assert q.get("nope", default=None) is None
    assert q.get_list("a") == ["123", "456"]

    assert list(q.keys()) == ["a", "b"]
    assert list(q.values()) == ["123", "789"]
    assert list(q.items()) == [("a", "123"), ("b", "789")]
    assert len(q) == 2
    assert list(q) == ["a", "b"]
    assert dict(q) == {"a": "123", "b": "789"}
    assert str(q) == "a=123&a=456&b=789"
    assert repr(q) == "QueryParams('a=123&a=456&b=789')"
    assert ngiri.QueryParams({"a": "123", "b": "456"}) == ngiri.QueryParams(
        [("a", "123"), ("b", "456")]
    )
    assert ngiri.QueryParams({"a": "123", "b": "456"}) == ngiri.QueryParams(
        "a=123&b=456"
    )
    assert ngiri.QueryParams({"a": "123", "b": "456"}) == ngiri.QueryParams(
        {"b": "456", "a": "123"}
    )
    assert ngiri.QueryParams() == ngiri.QueryParams({})
    assert ngiri.QueryParams([("a", "123"), ("a", "456")]) == ngiri.QueryParams(
        "a=123&a=456"
    )
    assert ngiri.QueryParams({"a": "123", "b": "456"}) != "invalid"

    q = ngiri.QueryParams([("a", "123"), ("a", "456")])
    assert ngiri.QueryParams(q) == q


def test_queryparam_types():
    q = ngiri.QueryParams(None)
    assert str(q) == ""

    q = ngiri.QueryParams({"a": True})
    assert str(q) == "a=true"

    q = ngiri.QueryParams({"a": False})
    assert str(q) == "a=false"

    q = ngiri.QueryParams({"a": ""})
    assert str(q) == "a="

    q = ngiri.QueryParams({"a": None})
    assert str(q) == "a="

    q = ngiri.QueryParams({"a": 1.23})
    assert str(q) == "a=1.23"

    q = ngiri.QueryParams({"a": 123})
    assert str(q) == "a=123"

    q = ngiri.QueryParams({"a": [1, 2]})
    assert str(q) == "a=1&a=2"


def test_empty_query_params():
    q = ngiri.QueryParams({"a": ""})
    assert str(q) == "a="

    q = ngiri.QueryParams("a=")
    assert str(q) == "a="

    q = ngiri.QueryParams("a")
    assert str(q) == "a="


def test_queryparam_update_is_hard_deprecated():
    q = ngiri.QueryParams("a=123")
    with pytest.raises(RuntimeError):
        q.update({"a": "456"})


def test_queryparam_setter_is_hard_deprecated():
    q = ngiri.QueryParams("a=123")
    with pytest.raises(RuntimeError):
        q["a"] = "456"


def test_queryparam_set():
    q = ngiri.QueryParams("a=123")
    q = q.set("a", "456")
    assert q == ngiri.QueryParams("a=456")


def test_queryparam_add():
    q = ngiri.QueryParams("a=123")
    q = q.add("a", "456")
    assert q == ngiri.QueryParams("a=123&a=456")


def test_queryparam_remove():
    q = ngiri.QueryParams("a=123")
    q = q.remove("a")
    assert q == ngiri.QueryParams("")


def test_queryparam_merge():
    q = ngiri.QueryParams("a=123")
    q = q.merge({"b": "456"})
    assert q == ngiri.QueryParams("a=123&b=456")
    q = q.merge({"a": "000", "c": "789"})
    assert q == ngiri.QueryParams("a=000&b=456&c=789")


def test_queryparams_are_hashable():
    params = (
        ngiri.QueryParams("a=123"),
        ngiri.QueryParams({"a": 123}),
        ngiri.QueryParams("b=456"),
        ngiri.QueryParams({"b": 456}),
    )

    assert len(set(params)) == 2
