
from dbbase.HIveBase import HiveBase


class UserInfo(HiveBase):

    def create_table(self):
        # stat
        hql = """
            create table if not EXISTS stat.userinfo (fuserid int, fage int, farea string, fmoney int)
            row format delimited fields terminated by ','
            location '/user/hadoop/stat/userinfo'
        """
        return self.execute(hql)

    def do_jobs(self):
        hql = """
            load data inpath '/user/hadoop/stat/userinfo' into table stat.userinfo
        """
        return self.execute(hql)


if __name__ == '__main__':

    obj = UserInfo()

    obj()
