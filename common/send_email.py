# coding=utf-8
# @Time    : 2019/8/19 11:04
# @Author  : Rock
# @File    : run_test.py
# @describe: 发送邮件

import os
import smtplib

from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.get_value import GetValue


class SendEmail(GetValue):
    def __init__(self, file_path):
        self.file_path = file_path

    def new_report(self):
        report_list = os.listdir(self.file_path)
        report_list.sort(key=lambda fn: os.path.getmtime(self.file_path + "\\" + fn))
        file_new = os.path.join(self.file_path, report_list[-1])
        print("测试结束，报告路径: "+file_new)
        return file_new

    def send_mail(self, report_file):
        # 邮件配置信息
        smtpserver = 'smtp.qq.com'
        user = '739965647@qq.com'
        password = self.mail_pass
        sender = "739965647@qq.com"
        receiver = ["rockche@inslabs.org"]

        msg = MIMEMultipart()
        msg['Subject'] = Header('接口自动化测试报告','utf-8')
        msg["From"] = sender
        msg["To"] = ",".join(receiver)

        # 邮件正文内容
        msg.attach(MIMEText('附件为本次接口自动化测试报告，为保证最佳浏览效果，请使用Chrome打开查看', 'plain', 'utf-8'))

        # 构造附件，传入最新的测试报告文件
        sendfile = open(report_file, 'rb').read()
        att = MIMEText(sendfile, 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="ApiTestReport.html"'
        msg.attach(att)

        smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
        smtp.connect(smtpserver)
        smtp.login(user, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print("邮件发送成功")
