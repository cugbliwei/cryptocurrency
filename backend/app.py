from aiohttp import web
from api import api


routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    return web.Response(text="Hello, world")


@routes.post('/otc/user/set')
async def otc_user_set(request):
    data = await request.post()
    username = data['username']
    password = data['password']
    nickname = data.get('nickname', '')
    token = data.get('token', '')
    result = api.user_set(username, password, nickname, token)
    if not result:
        return web.json_response({'status': True, 'msg': ''})
    else:
        return web.json_response({'status': False, 'msg': result})


@routes.post('/otc/user/get')
async def otc_user_get(request):
    data = await request.post()
    username = data['username']
    password = data['password']
    result = api.user_get(username, password)
    if result:
        return web.json_response({'status': True, 'msg': ''})
    else:
        return web.json_response({'status': False, 'msg': '查无此账号'})


@routes.post('/otc/profile')
async def otc_profile(request):
    data = await request.post()
    refresh_time = data['refresh_time']
    result = api.set_profile(refresh_time)
    if not result:
        return web.json_response({'status': True, 'msg': '设置成功'})
    else:
        return web.json_response({'status': False, 'msg': '设置失败'})


@routes.post('/otc/rank')
async def otc_predict(request):
    data = await request.post()
    coin_name = data['coin_name']
    nickname = data['nickname']
    results = api.otc_rank(coin_name, nickname)
    return web.json_response(results)


@routes.post('/otc/sumary')
async def otc_sumary(request):
    data = await request.post()
    coin_name = data['coin_name']
    results = api.otc_sumary(coin_name)
    return web.json_response(results)


@routes.post('/otc/origin')
async def otc_origin(request):
    data = await request.post()
    coin_name = data['coin_name']
    results = api.get_origin(coin_name)
    return web.json_response(results)


def run():
    app = web.Application()
    app.router.add_routes(routes)
    web.run_app(app, port='80')


if __name__ == '__main__':
    run()
