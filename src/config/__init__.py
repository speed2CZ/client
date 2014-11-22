__author__ = 'Sheeo'

import os
import version
import logging
from PyQt4 import QtCore

_settings = QtCore.QSettings("ForgedAllianceForever", "FA Lobby")


class Settings(object):
    @staticmethod
    def get(key, group=None):
        if group is None:
            value = _settings.value(key)
        else:
            _settings.beginGroup(group)
            value = _settings.value(key)
            _settings.endGroup()
        if value is None:
            if group is None:
                return defaults[key]
            else:
                return defaults[group][key]
        return value

    @staticmethod
    def set(key, value, group=None):
        if group is None:
            _settings.setValue(key, value)
        else:
            _settings.beginGroup(group)
            _settings.setValue(key, value)
            _settings.endGroup()


if version.is_development_version():
    # Setup logging output
    devh = logging.StreamHandler()
    devh.setFormatter(logging.Formatter('%(asctime)s %(levelname)-8s %(name)-40s %(message)s'))
    logging.getLogger().addHandler(devh)
    logging.getLogger().setLevel(logging.INFO)

    for k in []:
        logging.getLogger(k).setLevel(logging.DEBUG)

    logging.getLogger(__name__).info("Loading development configuration")
    from develop import defaults
else:
    from production import defaults
    logging.basicConfig(filename=Settings.get('FAF', 'LOG'), level=Settings.get('LEVEL', 'LOG'),
                        format='%(asctime)s %(levelname)-8s %(name)-40s %(message)s')

