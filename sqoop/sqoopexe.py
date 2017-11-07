# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'

'''
desc
'''
import sys
sys.path.append('/home/hadoop/scs_jobs/scs_job')

import paramiko
from logger import logger
from db_mysql import Connection
import config
from datetime import datetime

class ShellExec(object):



    host = '192.168.1.104'
    port = 22
    user = 'hadoop'
    password = 'qq633922'

    mysql_db = Connection(host=config.MYSQL_HOST, port=config.MYSQL_PORT, user=config.MYSQL_USER, password=config.MYSQL_PASSWORD, database=config.MYSQL_DB)

    def __init__(self, date=None):

        self._connect()

        if date:
            self.today = date
        else:
            self.today = datetime.now().date().strftime('%Y-%m-%d')


        self.export_cmd = """
            /usr/local/sqoop/bin/sqoop export   \
            --connect jdbc:mysql://127.0.0.1:3306/analysis?characterEncoding=utf8  \
            -m 1  \
            --username root   \
            --password 633922   \
            --export-dir /user/hadoop/analysis/{tablename}/dt={fdate}  \
            --table {tablename}   \
            --fields-terminated-by ','
        """



    def _connect(self):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            self.ssh.connect(hostname=self.host, port=self.port, username=self.user, password=self.password)
        except Exception as e:
            logger.error('connection fail - {}'.format(e))


    def execute(self, cmd=None):
        logger.info('cmd--{}'.format(cmd))

        stdin, stdout, stderr = self.ssh.exec_command(cmd)

        sto = stdout.read()
        ste = stderr.read()

        logger.info(sto)
        logger.info(ste)
        return sto, ste


    def create_table(self):
        raise '子类必须实现'


    def do_jobs(self):
        raise '子类必须实现'



    def __call__(self, *args, **kwargs):

        logger.info('日期--{}'.format(self.today))

        logger.info('开始建表--')
        res = self.create_table()
        if res:
            logger.info('建表成功')
        else:
            logger.warning('建表失败')

        logger.info('开始导出，耐心--')
        res = self.do_jobs()
        if res:
            logger.info('导出成功')
        else:
            logger.warning('导出失败')




