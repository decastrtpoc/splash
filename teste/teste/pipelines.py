from teste import util
from teste.settings import *
import json
class testePipeline(object):
    def __init__(self):
        self.db = util.set_mongo_server()
    def process_item(self, item, spider):
        try:
            if "vivaId" in item:
                self.db[MONGODB_COLNAME].insert(dict(item))
        except Exception as ex:
            spider.logger.warn('Pipeline Error (others): %s %s' % (str(ex),  str(item)))