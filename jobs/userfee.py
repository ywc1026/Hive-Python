
from dbbase.HIveBase import HiveBase
import sys


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

    try:
        date = sys.argv[1]
    except Exception as e:
        date = None

    obj = UserFee()

    obj()
