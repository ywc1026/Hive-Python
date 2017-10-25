
from pyhive import hive
from logger import logger
import config


class HiveBase(object):

    def __init__(self):

        self.port = config.HIVE_PORT
        self.host = config.HIVE_HOST

    def execute(self, hql=None):

        try:
            logger.info('hql--{}'.format(hql))

            conn = hive.connect(host=self.host, port=self.port)
            cursor = conn.cursor()
            cursor.execute()
            cursor.commit()
            cursor.close()
            conn.close()
            return True

        except Exception as e:
            logger.error("hive execute error")
            cursor.close()
            conn.close()
            return False

    def create_table(self):
        raise 'Subclass must achive this function'

    def do_jobs(self):
        raise 'Subclass must achive this function'

    def __call__(self, *args, **kwargs):
        logger.info("Start creating table...")
        res = self.create_table()
        if res:
            logger.info("Success of create table.")
        else:
            logger.info("Failed of create table.")
        logger.info("Start analysis, patient, please...")
        res = self.do_jobs()
        if res:
            logger.info("Finish count.")
        else:
            logger.info("Failed of count.")
