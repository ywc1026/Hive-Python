#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'Administrator'

'''
desc
'''
import sys
sys.path.append('/home/hadoop/scs_jobs/scs_job')

from sqoop.sqoopexe import ShellExec



class ExportGameActive(ShellExec):


    def create_table(self):

        sql = '''create table if not EXISTS  gameactive
              (fdate varchar(64), fgamename varchar(64), fcount int)
              DEFAULT CHARACTER set utf8'''

        return self.mysql_db.execute_commit(sql)


    def do_jobs(self):

        sqoop_export = self.export_cmd.format(fdate=self.today, tablename='gameactive')

        return self.execute(cmd=sqoop_export)





if __name__ == '__main__':


    obj = ExportGameActive()

    obj()
