""" ハジメの一歩会
* Copyright (c) 2022, Tech Lovers. All rights reserved
* Project Name    : 2022.10.17の宿題
* contents        : https://twitter.com/_0447222690292/status/1582008738852241408
* Creation Date   : 2022.10.17
* Programming language used: Python
* Author          : DEmodoriGatsuO
* Twitter         : https://twitter.com/DemodoriGatsuo Follow Me!
* Sorry           : I like English. But I can't use English.
*

"""
import datetime
_weekday_str = ("月","火","水","木","金","土","日")
def get_first_step(_weekday:int):
    if _weekday == 0:
        _str = "今日は燃えるゴミの日"
    elif _weekday == 1:
        _str = "明日は燃えないゴミの日"
    elif _weekday == 2:
        _str = "明後日は資源ゴミの日"
    elif _weekday == 3:
        _str = "明々後日は燃えるゴミの日"
    else:
        _str = _weekday_str[_weekday] + "曜日は、何もありません。"
    return _str

if __name__ == "__main__":
    print(get_first_step(datetime.date.today().weekday()))
