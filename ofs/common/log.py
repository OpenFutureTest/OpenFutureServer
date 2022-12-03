# -*- coding: utf8 -*-
import codecs
import datetime
import logging
import logging.handlers
import os
import re

from ofs import app

class MyLoggerHandler(logging.FileHandler):
    """"
    解决TimedRotatingFileHandler在多进程的情况下出现日志记录不完整，日志记录错位等问题
    """
    def __init__(self, filename, when='D', backupCount=365, encoding=None, delay=False):
        self.prefix = filename
        self.when = when.upper()
        # S - Every second a new file
        # M - Every minute a new file
        # H - Every hour a new file
        # D - Every day a new file
        if self.when == 'S':
            self.suffix = "%Y-%m-%d_%H-%M-%S"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}$"
        elif self.when == 'M':
            self.suffix = "%Y-%m-%d_%H-%M"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}$"
        elif self.when == 'H':
            self.suffix = "%Y-%m-%d_%H"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}$"
        elif self.when == 'D':
            self.suffix = "%Y-%m-%d"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}$"
        else:
            raise ValueError("Invalid rollover interval specified: %s" % self.when)
        self.filefmt = "%s.%s" % (self.prefix, self.suffix)
        self.filePath = datetime.datetime.now().strftime(self.filefmt)
        _dir = os.path.dirname(self.filePath)
        try:
            if os.path.exists(_dir) is False:
                os.makedirs(_dir)
        except Exception:
            print("can not make dirs")
            print("filepath is " + self.filePath)
            pass

        self.backupCount = backupCount
        if codecs is None:
            encoding = None
        logging.FileHandler.__init__(self, self.filePath, 'a', encoding, delay)

    def shouldChangeFileToWrite(self):
        _filePath = datetime.datetime.now().strftime(self.filefmt)
        if _filePath != self.filePath:
            self.filePath = _filePath
            return 1
        return 0

    def doChangeFile(self):
        self.baseFilename = os.path.abspath(self.filePath)
        if self.stream is not None:
            self.stream.flush()
            self.stream.close()
        if not self.delay:
            self.stream = self._open()
        if self.backupCount > 0:
            for s in self.getFilesToDelete():
                os.remove(s)

    def getFilesToDelete(self):
        dirName, baseName = os.path.split(self.baseFilename)
        fileNames = os.listdir(dirName)
        result = []
        prefix = self.prefix + "."
        plen = len(prefix)
        for fileName in fileNames:
            if fileName[:plen] == prefix:
                suffix = fileName[plen:]
                if re.compile(self.extMatch).match(suffix):
                    result.append(os.path.join(dirName, fileName))
        result.sort()
        if len(result) < self.backupCount:
            result = []
        else:
            result = result[:len(result) - self.backupCount]
        return result

    def emit(self, record):
        """
        Emit a record.
        """
        try:
            if self.shouldChangeFileToWrite():
                self.doChangeFile()
            logging.FileHandler.emit(self, record)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

# 日志记录
log_root = os.path.abspath(os.path.join(app.root_path, '../logs'))
if not os.path.exists(log_root):
    os.makedirs(log_root)

appHandler = MyLoggerHandler(os.path.join(log_root, 'app.log'))
logFormatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s '
                                 '[in %(pathname)s:%(lineno)d]')
appHandler.setFormatter(logFormatter)


my_loggers = dict()


def print_log(filename, message):
    try:
        my_logger = my_loggers.get(filename)
        if not my_logger:
            myhandler = MyLoggerHandler(
                os.path.join(log_root, '%s.log' % filename)
            )
            log_format = logging.Formatter('%(asctime)s: %(message)s')
            myhandler.setFormatter(log_format)
            my_logger = logging.getLogger(filename)
            my_logger.addHandler(myhandler)
            my_logger.setLevel(logging.INFO)
            my_loggers[filename] = my_logger
        my_logger.info(message)
    except:
        pass

__all__ = ['appHandler', 'print_log']