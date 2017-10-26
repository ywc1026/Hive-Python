
from dbbase.HIveBase import HiveBase


class GameInfo(HiveBase):

    def create_table(self):
        # stat
        hql = """
            create table if not EXISTS stat.gameinfo (fgameid int, fgamename string)
            row format delimited fields terminated by ','
            location '/user/hadoop/stat/userinfo'
        """
        return self.execute(hql)

    def do_jobs(self):
        hql = """
            load data inpath '/user/hadoop/stat/gameinfo' into table stat.gameinfo
        """
        return self.execute(hql)


if __name__ == '__main__':

    obj = GameInfo()

    obj()
