import os
import json
from PySide6.QtCore import QStandardPaths
#! add file.close to all of te other thingies
def Setup():
    dataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
    dataPath = os.path.join(dataLocation, 'DeepWarden', 'data')
    presetNamesPath = os.path.join(dataPath, 'PresetNames.json')
    presetRenameContentPath = os.path.join(dataPath, 'presetRenamecontent.txt')
    presetRenameNumPath = os.path.join(dataPath, 'presetRenameNum.txt')
    SettingsPath = os.path.join(dataPath, 'Settings.json')
    if not os.path.isdir(dataLocation):
        os.mkdir(dataLocation)
    if not os.path.isdir(os.path.join(dataLocation, 'DeepWarden')):
        os.mkdir(os.path.join(dataLocation, 'DeepWarden'))
    if not os.path.isdir(dataPath):
        os.mkdir(dataPath)
    if not os.path.isfile(SettingsPath):
        print('setup')
        with open(SettingsPath, 'x') as f:
            baseSettings = {
                'theme': 'dark',
                'notifs': 'True',
                'show-intro': 'True',
                'autoSprint': 'False'
            }
            json.dump(baseSettings, f)
        f.close()
    if not os.path.isfile(presetRenameContentPath):
        open(presetRenameContentPath, 'x')
    if not os.path.isfile(presetRenameNumPath):
        open(presetRenameNumPath, 'x')
    if not os.path.isfile(presetNamesPath):
        File = open(presetNamesPath, 'w')
        File.close()
        DataFile = open(presetNamesPath, 'w')
        names = {
            "Preset1Name": "Preset 1",
            "Preset2Name": "Preset 2",
            "Preset3Name": "Preset 3",
            "Preset4Name": "Preset 4",
            "Preset5Name": "Preset 5",
            "Preset6Name": "Preset 6",
            "Preset7Name": "Preset 7",
            "Preset8Name": "Preset 8",
            "Preset9Name": "Preset 9",
            "Preset10Name": "Preset 10",
        }
        compiledNames = (json.dumps(names))
        DataFile.write(compiledNames)
        DataFile.close()