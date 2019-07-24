import logging


formatter = '%(asctime)s %(levelname)-8s %(filename)s:%(lineno)-4d %(message)-80s'
logging.basicConfig(format=formatter, datefmt='%m/%d/%Y %T')

log = logging.getLogger('TEST')


def add_log_level(level_name, level_num):
    logging.addLevelName(level_num, level_name)

    def logger_method(self, message, *args, **kws):
        if self.isEnabledFor(level_num):
            self._log(level_num, message, args, **kws)

    setattr(logging, level_name, level_num)
    setattr(logging.Logger, level_name.lower(), logger_method)


add_log_level('MASTER', 40)

log.master('abc')
log.critical('abc')
log.error('abc')

import ipdb
ipdb.set_trace()
