import pytest

import ngiri


@pytest.mark.anyio
async def test_read_timeout(server):
    timeout = ngiri.Timeout(None, read=1e-6)

    async with ngiri.AsyncClient(timeout=timeout) as client:
        with pytest.raises(ngiri.ReadTimeout):
            await client.get(server.url.copy_with(path="/slow_response"))


@pytest.mark.anyio
async def test_write_timeout(server):
    timeout = ngiri.Timeout(None, write=1e-6)

    async with ngiri.AsyncClient(timeout=timeout) as client:
        with pytest.raises(ngiri.WriteTimeout):
            data = b"*" * 1024 * 1024 * 100
            await client.put(server.url.copy_with(path="/slow_response"), content=data)


@pytest.mark.anyio
@pytest.mark.network
async def test_connect_timeout(server):
    timeout = ngiri.Timeout(None, connect=1e-6)

    async with ngiri.AsyncClient(timeout=timeout) as client:
        with pytest.raises(ngiri.ConnectTimeout):
            # See https://stackoverflow.com/questions/100841/
            await client.get("http://10.255.255.1/")


@pytest.mark.anyio
async def test_pool_timeout(server):
    limits = ngiri.Limits(max_connections=1)
    timeout = ngiri.Timeout(None, pool=1e-4)

    async with ngiri.AsyncClient(limits=limits, timeout=timeout) as client:
        with pytest.raises(ngiri.PoolTimeout):
            async with client.stream("GET", server.url):
                await client.get(server.url)
