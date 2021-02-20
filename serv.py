import Char
import aiohttp
import asyncio
from aiohttp import web
import json

async def handle(request):
    points= request.match_info.get('points', "100")
    #print(int(points))
    jason=Char.createpers(int(points)).json()
    print(request)
    response_obj = { 'data' : jason }
    return web.Response(text=json.dumps(jason),content_type='application/json')

app = web.Application()
app.router.add_get('/{points}', handle)

web.run_app(app)
