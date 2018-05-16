# -*- coding: utf-8 -*-

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PDOKLocatieserverFilterPlugin class from file pdoklocatieserverfilter.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    from .pdoklocatieserverfilter import PDOKLocatieserverFilterPlugin
    return PDOKLocatieserverFilterPlugin(iface)
