<!--
 * @Author: 七画一只妖 1157529280@qq.com
 * @Date: 2023-03-27 09:43:36
 * @LastEditors: 七画一只妖 1157529280@qq.com
 * @LastEditTime: 2023-12-01 21:49:06
 * @FilePath: \060坎公骑冠剑会战工具\README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# BaseKnightReport
## 坎公会战工具（更新中）

### 这是什么？
> 1.这是游戏《坎公骑冠剑》游戏中公会战查询数据的工具
> 2.因为找遍github也没找到python版本的会战查询工具于是自己做了个
> 3.该项目输出内容为图片，直接测试可以前往`main.py`查看
> 4.如果您的机器人使用的是python语言的框架，那么可以自行融合进去并根据需要进行修改
> 5.如果您使用的是nonebot2(beta5-rc3)，可以根据下面我写的配置进行使用

### 已完成功能
>- 1.输出每日伤害报表
>- 2.输出总榜
>- 3.查询当前进度
>- 4.查询所有成员出刀情况（非满刀的值有歧义，是否满刀是正确的，反正值等于3就是出完了）

### 注意事项/常见问题解决办法
>- 1.目前没摸清cookies过期时间的规律，如果你一开始可以使用，但是过了几天突然用不了了大概率是cookies过期了
>- 2.如果不是上面的问题，那么可能是公会数据还没刷新/接口异常等等，我将在以后的更新中捕获异常并给出对应的提示，以便于自己排查问题

### 使用方法
> [B站教程](https://www.bilibili.com/video/BV1yz4y1A7PQ/)

1.在config.json文件内填写好你的信息

2.如何获取cookies？
>- 1.浏览器开启无痕模式，不用无痕也行
>- 2.打开百宝袋地址 https://game.bilibili.com/tool/gt/
>- 3.使用B站登录
>- 4.在百宝袋页面按下【F12 没有F12右键审元素】打开DEV开发者工具 在【网络】一栏随便找到一个请求，找到Cookie字段并复制值
>- 5.关闭无痕窗口浏览器（不要使用bigfun退出登录 会导致接口失效 也不要切换账号会立刻失效）

3.运行main.py（也不用管不管注释了，直接运行就行，反正会分别生成4张图出来）

4.在payload2/cache文件夹下会生成结果图

### 效果展示与加入机器人后的效果
(以下是图片，在payload/cache文件夹下，数字即main.py里面的传参，目的是为了可以让多个用户使用，多个公会也可以共用一个机器人)

![](https://cdngoapl.twip.top/image/%E8%BF%9B%E5%BA%A6%E8%A1%A8_114514.jpg)
![](https://cdngoapl.twip.top/image/%E8%A1%A8%E6%A0%BC%E5%9B%BE_114514.jpg)


### 关键代码
这是这个接口参数生成的原理，如果你用的是其他语言，只需要根据以下代码的逻辑复刻即可
如果date为空，代表查询的是最新一天的数据
~~~python
# 两个常量
app_key = 'a5e793dd8b8e425c9bff92ed79e4458f'
app_secret = 'xoNO7qa9761mNPyLtTn8zxPeX80iLnDonYCOzqS7bG8='

# 生成接口载荷
def get_sign(date: str = None) -> dict:
    data = {
        'ts': int(time.time()),
        'nonce': '-'.join([binascii.hexlify(os.urandom(3)).decode() for _ in range(3)]),
        'appkey': app_key
    }

    # 将sign加入到data里面
    if date:
        data['date'] = date

    sorted_data = dict(sorted(data.items(), key=lambda x: x[0]))
    sorted_params_str = urlencode(sorted_data)
    sign = hashlib.md5(
        (sorted_params_str + f'&secret={app_secret}').encode()).hexdigest()
    
    data['sign'] = sign

    return data
~~~