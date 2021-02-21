import Char
import aiohttp
import asyncio
from aiohttp import web
import json
import aiohttp_cors

@asyncio.coroutine
async def handler(request):
    points= request.match_info.get('points', "100")
    tu= request.match_info.get('tu', "3")
    print(int(tu))
    jason=Char.createpers(int(points),int(tu)).json()
    print(jason)
    response_obj = { 'data' : jason }
    return web.Response(text=json.dumps(jason),content_type='application/json',headers={
            "X-Custom-Server-Header": "Custom data",
        })

app = web.Application()
cors = aiohttp_cors.setup(app)
resource = cors.add(app.router.add_resource("/{points}/{tu}"))
oute = cors.add(
    resource.add_route("GET", handler), {
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers=("X-Custom-Server-Header",),
            allow_headers=("X-Requested-With", "Content-Type"),
            max_age=3600,
        )
    })
#app.router.add_get('/{points}', handle)

web.run_app(app)
