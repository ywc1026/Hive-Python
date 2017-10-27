
from dbbase.HIveBase import HiveBase


class UserFee(HiveBase):

    def create_table(self):
        # stat
        hql = """
            create table if not EXISTS stat.userfee (fdate string, fuserid int, fgameid int, ffee int)
            partitioned by (dt string)
            row format delimited fields terminated by ','
            location '/user/ywc/stat/userfee'
        """
        return self.execute(hql)

    def do_jobs(self):

        hql = """
            alter table stat.userfee add if not EXISTS partition(dt='{fdate}')
            location '/user/ywc/stat/userfee/{fdate}'
        """.format(fdate=self.today)
        return self.execute(hql)


if __name__ == '__main__':

    obj = UserFee()

    obj()
