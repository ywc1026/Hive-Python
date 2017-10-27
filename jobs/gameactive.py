

from dbbase.HIveBase import HiveBase
import sys


class GameActive(HiveBase):

    def create_table(self):
        # analysis
        hql = """
                create table if not EXISTS analysis.gameactive (fdate string, fgamename string, fcount int)
                partitioned by (dt string)
                row format delimited fields terminated by ','
                location '/user/ywc/analysis/gameactive'
                """
        return self.execute(hql)

    def do_jobs(self):
        hql = """
                    insert overwrite table analysis.gameactive
                    partition (dt='{fdate}')
                    select gt.fdate as fdate, gi.fgamename as fgamename, count(gt.fuserid) as fcount from stat.gametime as gt
                    left join stat.gameinfo as gi
                    on gt.fgameid=gi,fgameid
                    where
                    gt.fdate='{fdate}'
                    group by gi.fgamename, gt.fdate
                """.format(fdate=self.today)

        return self.execute(hql)


if __name__ == '__main__':

    try:
        date = sys.argv[1]
    except Exception as e:
        date = None

    obj = GameActive()

    obj()