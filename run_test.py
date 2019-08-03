# coding=utf-8
# @Time    : 2019/8/2 23:04
# @Author  : Rock
# @File    : run_test.py
# @describe: 运行入口

import os
import time
import smtplib
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def send_mail(file_new):
    # 邮件配置信息
    smtpserver = 'smtp.qq.com'
    user = '739965647@qq.com'
    password = 'passowrd'
    sender = "739965647@qq.com"
    receiver = ["rockche@inslabs.org"]

    msg = MIMEMultipart()
    msg['Subject'] = Header('接口自动化测试报告','utf-8')
    msg["From"] = sender
    msg["To"] = ",".join(receiver)

    # 邮件正文内容
    msg.attach(MIMEText('附件为本次接口自动化测试报告，为保证最佳浏览效果，请使用Chrome打开查看', 'plain', 'utf-8'))
    # 构造附件，传入最新的测试报告文件
    sendfile = open(file_new, 'rb').read()
    att= MIMEText(sendfile,'base64','utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="ApiTestReport.html"'
    msg.attach(att)

    smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtp.connect(smtpserver)
    smtp.login(user,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    print("邮件发送成功")


def new_report(testreport):
    reprotlist = os.listdir(testreport)
    reprotlist.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, reprotlist[-1])
    print("测试结束，报告路径: "+file_new)
    return file_new


if __name__ == '__main__':
    # 定义测试用例的目录为当前目录
    test_dir = './case'
    test_report = './report'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

    # 按照一定格式获取当前时间
    now = time.strftime("%Y-%m-%d %H.%M")

    # 定义报告存放路径和文件名
    filename = test_report + "\\" + now + 'result.html'

    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='校精灵接口自动化测试报告',
                            description='用例执行情况：')

    runner.run(discover)  # 运行测试用例
    fp.close()  # 关闭报告文件

    new_report = new_report(test_report)
    send_mail(new_report)  # 发送测试报告
