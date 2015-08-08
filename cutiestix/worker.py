from __future__ import division
import logging

# PyQt
from PyQt4 import QtGui, QtCore

# stix-validator
import sdv

# internal
from . import settings
from . import models


LOG = logging.getLogger(__name__)


class ValidationWorker(QtCore.QObject):
    SIGNAL_VALIDATED = QtCore.pyqtSignal(int, float)
    SIGNAL_FINISHED  = QtCore.pyqtSignal()
    SIGNAL_EXCEPTION = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(ValidationWorker, self).__init__(parent)
        self._tasks = []

    def add_tasks(self, tasks):
        self._tasks.extend(tasks)

    def add_task(self, task):
        self._tasks.append(task)

    def _validate_item(self, item):
        fn      = item.filename
        version = item.stix_version
        profile = settings.STIX_PROFILE_FILENAME
        schemas = settings.XML_SCHEMA_DIR
        result  = models.ValidationResults()

        if item.validate_xml:
            result.xml = sdv.validate_xml(doc=fn, schemas=schemas, version=version)

        if item.validate_stix_profile:
            result.profile = sdv.validate_profile(doc=fn, profile=profile)

        if item.validate_best_practices:
            result.best_practices = sdv.validate_best_practices(doc=fn, version=version)

        return result

    @QtCore.pyqtSlot()
    def validate(self):
        LOG.debug("Validating %d docuemnts", len(self._tasks))
        LOG.info("Worker executing in thread %d", QtCore.QThread.currentThreadId())
        total = len(self._tasks)

        for idx, item in enumerate(self._tasks, start=1):
            LOG.debug("Running task %s", id(item))
            results = self._validate_item(item)
            item.results = results
            self.SIGNAL_VALIDATED.emit(id(item), (idx / total))


        LOG.debug("validate() done!")
        self.SIGNAL_FINISHED.emit()