
from dbbase.HIveBase import HiveBase


class Test(HiveBase):

    def create_table(self):
        pass

    def do_jobs(self):
        pass


if __name__ == '__main__':

    obj = Test()

    obj()