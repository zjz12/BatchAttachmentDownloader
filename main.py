"""
https://github.com/Li-Jiajie/BatchAttachmentDownloader

BatchAttachmentDownloader   v1.3.0
邮件附件批量下载
Python 3开发，支持IMAP4与POP3协议

支持多种附件保存模式、筛选模式

使用场景：通过邮箱收作业、调查等，批量下载附件    等

2020.10.22
Jiajie Li

2020.12.11
very good zjz change a little for my darling
"""

import email_helper
import re

# ************************请设置以下参数************************

# 邮箱地址  （必填）
EMAIL_ADDRESS = ''
# 邮箱密码  （必填）
EMAIL_PASSWORD = ''

# 邮件协议  （必填，POP3或IMAP）
EMAIL_PROTOCOL = 'POP3'
# 服务器地址(SSL)    （必填，请根据协议填入合适的地址）
SERVER_ADDRESS = 'pop.139.com'

# 附件保存位置
SAVE_PATH = 'C:\emailFiles'
# 筛选起止时间    yyyy-MM-dd HH:mm:ss
DATE_BEGIN, DATE_END = '2020-10-16 00:00', ''  # 筛选起止时间（包含此时间）
# 时区 默认东八区北京时间，如需更改请按如下格式更改
TIME_ZONE = '+0800'
# 筛选包含此内容的邮件地址，''表示全部邮件地址
FROM_ADDRESS = ''
# 筛选包含此内容的发件人昵称，''表示全部发件人昵称
FROM_NAME = ''
# 筛选包含此内容的邮件主题，''表示全部邮件主题
SUBJECT = ''
"""
    保存模式    SAVE_MODE
【0：所有附件存入一个文件夹】
【1：每个邮箱地址一个文件夹】
【2：每个邮件主题一个文件夹】
【3：每个发件人的每个邮件主题一个文件夹】
【4：每个发件人昵称一个文件夹】
"""
SAVE_MODE = 0

# ************************请设置以上参数************************

if __name__ == '__main__':
    with open("config.txt",'r') as f:
        lines = f.readlines()
        pat = re.compile(r'\'(.*)\'')
        for line in lines:
            if 'EMAIL_ADDRESS' in line:
                tmp = pat.findall(line)
                if len(tmp) > 0:
                    EMAIL_ADDRESS = tmp[0]

            if 'EMAIL_PASSWORD' in line:
                tmp = pat.findall(line)
                if len(tmp) > 0:
                    EMAIL_PASSWORD = tmp[0]

            if 'SAVE_PATH' in line:
                tmp = pat.findall(line)
                if len(tmp) > 0:
                    SAVE_PATH = tmp[0]#.replace('\\','\\\\')

            if 'DATE_BEGIN' in line:
                tmp = pat.findall(line)
                if len(tmp) > 0:
                    DATE_BEGIN = tmp[0]

            if 'DATE_END' in line:
                tmp = pat.findall(line)
                if len(tmp) > 0:
                    DATE_END = tmp[0]

            if 'FROM_ADDRESS' in line:
                tmp = pat.findall(line)
                if len(tmp) > 0:
                    FROM_ADDRESS = tmp[0]

            if 'FROM_NAME' in line:
                tmp = pat.findall(line)
                if len(tmp) > 0:
                    FROM_NAME = tmp[0]

            if 'SUBJECT' in line:
                tmp = pat.findall(line)
                if len(tmp) > 0:
                    SUBJECT = tmp[0]

            if 'SAVE_MODE' in line:
                tmp = pat.findall(line)
                if len(tmp) > 0:
                    SAVE_MODE = tmp[0]
            #print(line)
            if line[0] in ['', '#']:
                continue




    # 服务器连接与邮箱登录
    downloader = email_helper.BatchEmail(EMAIL_PROTOCOL, SERVER_ADDRESS, EMAIL_ADDRESS, EMAIL_PASSWORD)

    # 选项设置
    downloader.set_save_mode(SAVE_MODE)
    downloader.save_path = SAVE_PATH
    downloader.date_begin = DATE_BEGIN
    downloader.date_end = DATE_END
    downloader.time_zone = TIME_ZONE
    downloader.from_name = FROM_NAME
    downloader.from_address = FROM_ADDRESS
    downloader.subject = SUBJECT

    # 下载附件
    downloader.download_attachments()
    downloader.close()
