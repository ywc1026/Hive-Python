
from dbbase.HIveBase import HiveBase


class GameTime(HiveBase):

    def create_table(self):
        # stat
        hql = """
            create table if not EXISTS stat.gametime (fdate string, fuserid int, fgameid int, fgametime int)
            partitioned by (dt string)
            row format delimited fields terminated by ','
            location '/user/ywc/stat/gametime'
        """
        return self.execute(hql)

    def do_jobs(self):

        hql = """
            alter table stat.gametime add if not EXISTS partition(dt='{fdate}')
            location '/user/ywc/stat/gametime/{fdate}'
        """.format(fdate=self.today)
        return self.execute(hql)


if __name__ == '__main__':

    obj = GameTime()

    obj()
