# -*- coding: utf-8 -*-

__author__='Sui'

'''
编写Web App骨架
'''

import logging; logging.basicConfig(level=logging.INFO)
import asyncio
from aiohttp import web

#制作响应函数
async def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')

#Web app服务器初始化
async def init(loop):
    app = web.Application(loop=loop)#制作响应函数集合
    app.router.add_route(method='GET',path='/',handler=index)#把响应函数添加到响应函数集合
    srv = await loop.create_server(app.make_handler(),'127.0.0.1',9000)#创建服务器(连接网址、端口，绑定handler)
    logging.info('server start at http://127.0.0.1:9000')#日志
    return srv

loop = asyncio.get_event_loop()#创建事件
loop.run_until_complete(init(loop))#运行
loop.run_forever()#服务器不关闭