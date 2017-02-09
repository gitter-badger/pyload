# -*- coding: utf-8 -*-
# Autogenerated by pyload
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING

from __future__ import absolute_import, unicode_literals

from builtins import str

from pyload.remote.apitypes import *

enums = [
    "Connection",
    "DownloadState",
    "DownloadStatus",
    "FileStatus",
    "InputType",
    "Interaction",
    "MediaType",
    "PackageStatus",
    "Permission",
    "ProgressType",
    "Role",
]

classes = {
    'AccountInfo': [int, str, str, int, bool, int, int, int, bool, bool, bool, (list, ConfigItem)],
    'AddonInfo': [str, str, str],
    'AddonService': [str, str, str, (list, str), bool, int],
    'ConfigHolder': [str, str, str, str, (list, ConfigItem), (None, (list, AddonInfo))],
    'ConfigInfo': [str, str, str, str, bool, (None, bool)],
    'ConfigItem': [str, str, str, Input, str],
    'DownloadInfo': [str, str, str, int, str, str],
    'DownloadProgress': [int, int, int, int, int],
    'EventInfo': [str, (list, str)],
    'FileDoesNotExist': [int],
    'FileInfo': [int, str, int, int, int, int, int, int, int, (None, DownloadInfo)],
    'Input': [int, (None, str), (None, str)],
    'InteractionTask': [int, int, Input, str, str, str],
    'InvalidConfigSection': [str],
    'LinkStatus': [str, str, int, int, (None, str), (None, str)],
    'OnlineCheck': [int, (dict, str, LinkStatus)],
    'PackageDoesNotExist': [int],
    'PackageInfo': [int, str, str, int, int, str, str, str, int, (list, str), int, bool, int, PackageStats, (list, int), (list, int)],
    'PackageStats': [int, int, int, int],
    'ProgressInfo': [str, str, str, int, int, int, int, int, (None, DownloadProgress)],
    'ServiceDoesNotExist': [str, str],
    'ServiceException': [str],
    'StatusInfo': [int, int, int, int, int, bool, bool, bool, bool, int],
    'TreeCollection': [PackageInfo, (dict, int, FileInfo), (dict, int, PackageInfo)],
    'UserData': [int, str, str, int, int, str, int, int, str, int, int, str],
    'UserDoesNotExist': [str],
}

methods = {
    'addLinks': None,
    'addLocalFile': None,
    'addPackage': int,
    'addPackageChild': int,
    'addPackageP': int,
    'addUser': UserData,
    'checkContainer': OnlineCheck,
    'check_html': OnlineCheck,
    'checkLinks': OnlineCheck,
    'createAccount': AccountInfo,
    'createPackage': int,
    'deleteConfig': None,
    'deleteFiles': bool,
    'deletePackages': bool,
    'findFiles': TreeCollection,
    'findPackages': TreeCollection,
    'freeSpace': int,
    'generateDownloadLink': str,
    'generatePackages': (dict, str, list),
    'getAccountInfo': AccountInfo,
    'getAccountTypes': (list, str),
    'getAccounts': (list, AccountInfo),
    'getAddonHandler': (dict, str, list),
    'getAllFiles': TreeCollection,
    'getAllInfo': (dict, str, list),
    'getAllUserData': (dict, int, UserData),
    'getAvailablePlugins': (list, ConfigInfo),
    'get_config': (dict, str, ConfigHolder),
    'getConfigValue': str,
    'getCoreConfig': (list, ConfigInfo),
    'getFileInfo': FileInfo,
    'getFileTree': TreeCollection,
    'getFilteredFileTree': TreeCollection,
    'getFilteredFiles': TreeCollection,
    'getInfoByPlugin': (list, AddonInfo),
    'getInteractionTasks': (list, InteractionTask),
    'getLog': (list, str),
    'getPackageContent': TreeCollection,
    'getPackageInfo': PackageInfo,
    'getPluginConfig': (list, ConfigInfo),
    'getProgressInfo': (list, ProgressInfo),
    'getQuota': int,
    'getServerVersion': str,
    'getStatusInfo': StatusInfo,
    'getUserData': UserData,
    'get_ws_address': str,
    'invokeAddon': str,
    'invokeAddonHandler': str,
    'isInteractionWaiting': bool,
    'loadConfig': ConfigHolder,
    'login': bool,
    'moveFiles': bool,
    'movePackage': bool,
    'orderFiles': None,
    'orderPackage': None,
    'parseLinks': (dict, str, list),
    'pauseServer': None,
    'pollResults': OnlineCheck,
    'quit': None,
    'recheckPackage': None,
    'removeAccount': None,
    'removeFiles': None,
    'removePackages': None,
    'removeUser': None,
    'restart': None,
    'restartFailed': None,
    'restartFile': None,
    'restartPackage': None,
    'saveConfig': None,
    'searchSuggestions': (list, str),
    'setConfigValue': None,
    'setInteractionResult': None,
    'setPackagePaused': int,
    'setPassword': bool,
    'stopAllDownloads': None,
    'stopDownloads': None,
    'togglePause': bool,
    'toggleReconnect': bool,
    'unpauseServer': None,
    'updateAccount': AccountInfo,
    'updateAccountInfo': None,
    'updatePackage': PackageInfo,
    'updateUserData': None,
    'uploadContainer': int,
}
