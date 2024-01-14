#!/usr/bin/python3
"""Packge for the Storage engine"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
