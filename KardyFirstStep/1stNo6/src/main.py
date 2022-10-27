""" ハジメの一歩会
* Copyright (c) 2022, Tech Lovers. All rights reserved
* Project Name    : 2022.10.24の宿題
* contents        : https://twitter.com/_0447222690292/status/1584544186237214720
* Creation Date   : 2022.10.26
* Programming language used: Python
* Author          : DEmodoriGatsuO
* Twitter         : https://twitter.com/DemodoriGatsuo Follow Me!
* Sorry           : I like English. But I can't use English.
*
* 一部の人だけ名前を入力したらGUIで遊べるようにしました。
* 全員に対応しておらずごめんなさい、、、

"""

import urllib.parse
import webbrowser
import tkinter as tk
from tkinter import messagebox

# class
class Student:
    """ 受講生クラス """
    def __init__(self, name):
        self._common = 'ハジメの一歩の会の参加者'
        self.name = name
        
    def print_student_info(self):
        return (self._common + '\n{}です'.format(self.name))

    def _method(self):
        s_quote = ("%E3%81%8B%E3%83%BC%E3%81%A7%E3%81%83%E3%81%95%E3%82%93%E3%80%81%E7%99%BE%E5%90%88%E5"
            + "%AE%AE%E3%81%95%E3%82%93%E3%81%82%E3%82%8A%E3%81%8C%E3%81%A8%E3%81%86%E3%81%94%E3%81"
            + "%96%E3%81%84%E3%81%BE%E3%81%97%E3%81%9F%EF%BC%81")
        
        messagebox.showinfo("Thank You!",urllib.parse.unquote(s_quote))
        return 

## common
class StudentMammals(Student):
    """ 哺乳類クラス """
    def __init__(self, name):
        super().__init__(name)
        self._biome = "哺乳類"

## land
class StudentHuman(Student):
    """ 人クラス """
    def __init__(self, name):
        super().__init__(name)
        self._life = "人"
        target_human = ("かーでぃ","ゆりみー","かおり")
        if name in target_human:
            propertys = {
                "かーでぃ": ("かーでぃ@ガノタなIoTプロフェッショナル","RPACommunity","ハジメの一歩会","@_0447222690292","IT知識は広ーく浅ーくをモットーに色々勉強してます。","https://lit.link/Kerdy"),
                "ゆりみー": ("百合宮桜@フルリモ女子","RPACommunity","ハジメの一歩会","@yurimiyasakura","宝塚花組と明日海りお様のファン","https://note.com/yurimiyasakura/"),
                "かおり"  : ("かおり","RPACommunity","外資ITサバイバル英語","@mocca1103","ハジメの一歩会 登壇予定!! 11.3","https://twitter.com/mocca1103")
            }
            self._biome = propertys[name][0]
            self._community = propertys[name][1]
            self._organizer = propertys[name][2]
            self._account = propertys[name][3]
            self._feature = propertys[name][4]
            self._url = propertys[name][5]

    def advertise(self):
        target_human = ("かーでぃ","ゆりみー","かおり")
        if self.name in target_human:
            webbrowser.open(self._url, new=1, autoraise=True)

## Sea
class StudentMarine(Student):
    """ 海洋生物クラス """
    def __init__(self, name):
        super().__init__(name)
        self._life = "海洋生物"

## nanamoji
class StudentSeaLion(StudentMammals, StudentMarine):
    """ ななもじ クラス """
    """ 海洋哺乳類クラス """
    def __init__(self, name):
        super().__init__(name)
        self._biome = "トド"
        self._community = "気ままに勉強会"
        self._organizer = ""
        self._account = "@sumiika88"
        self._feature = "ハジメの一歩会 登壇予定!!"

    def advertise(self):
        _url = "https://note.com/memomoji/"
        webbrowser.open(_url, new=1, autoraise=True)

## akiika
class StudentSquid(StudentMarine):
    """ あきイカ クラス """
    """ 軟体動物クラス """
    def __init__(self, name):
        super().__init__(name)
        self._biome = "イカ"
        self._community = "RPAcommunity"
        self._organizer = "#ゆるゆる勉強会"
        self._account = "@akiikasakiika"
        self._feature = "VTuber"

    def advertise(self):
        _url = "https://youtu.be/wjdUFmCuz34"
        webbrowser.open(_url, new=1, autoraise=True)

## 出戻りガツオ!!    
class StudentFish(StudentMarine):
    """ 出戻りガツオ クラス """
    """ 魚クラス """
    def __init__(self, name):
        super().__init__(name)
        self._biome = "サカナ"
        self._community = "気ままに勉強会"
        self._organizer = ""
        self._account = "@DemodoriGatsuo"
        self._feature = "2022.11.30 RPACommunity LT予定"

    def advertise(self):
        _url = "https://note.com/bonito_vba_gas/n/n586cd22f4b0b"
        webbrowser.open(_url, new=1, autoraise=True)

### Main
if __name__ == "__main__":
    your_name = input("貴方の名前を入力してください\n\n")

    if your_name in ("かーでぃ","ゆりみー","かおり"):
        me = StudentHuman(your_name)
    elif your_name in "ななもじ":
        me = StudentSeaLion(your_name)
    elif your_name in "あきイカ":
        me = StudentSquid(your_name)
    elif your_name in "出戻りガツオ":
        me = StudentFish(your_name)
    else:
        messagebox.showinfo("Thank You!",your_name) 
        exit()

    root = tk.Tk()
    root.geometry("300x400") 
    root.title("PROFILE")

    label1 = tk.Label(
        root, text=me.name, bd=5, width=30)
    label2 = tk.Label(
        root, text=me._biome, bd=5, width=30)
    label3 = tk.Label(
        root, text=me._community, bd=5, width=30)
    label4 = tk.Label(
        root, text=me._organizer, bd=5, width=30)
    label5 = tk.Label(
        root, text=me._account, bd=5, width=30)
    label6 = tk.Label(
        root, text=me._feature, bd=5, width=30)

    button1 = tk.Button(
        root, text="contents!", relief=tk.RAISED, bd=5, width=20, command=me.advertise)

    button2 = tk.Button(
        root, text="thanks!", relief=tk.RAISED, bd=5, width=20, command=me._method)

    # 配置
    label1.pack(pady=10)
    label2.pack(pady=10)
    label3.pack(pady=10)
    label4.pack(pady=10)
    label5.pack(pady=10)
    label6.pack(pady=10)
    button1.pack(pady=10)
    button2.pack(pady=10)

    root.mainloop()
