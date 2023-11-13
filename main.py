'''
Author: 七画一只妖 1157529280@qq.com
Date: 2023-03-27 09:01:10
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2023-11-13 14:51:35
FilePath: \060坎公骑冠剑会战工具\main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import asyncio

from payload2 import data_format

import asyncio
loop = asyncio.get_event_loop()


# 填写完cookies之后就能在这操作了，想要运行下面功能就把哪行解开运行即可

# 日报
# print(loop.run_until_complete(data_format.today_report("114514")))

# 总伤
# print(loop.run_until_complete(data_format.all_report("114514")))

# 进度
try:
    print(loop.run_until_complete(data_format.get_rate("114514")))
except Exception as e:
    print(e)
