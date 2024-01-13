#!/usr/bin/python3
"""
This script initializes an instance of the FileStorage class from the
'models.engine.file_storage' module and reloads previously stored data.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
