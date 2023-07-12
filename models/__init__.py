#!/usr/bin/python3

""" 
    The '__init.py__' is the first file run when a module from the file 'models'
    is imported, therefore we load our data base to 'storage' from this file
"""

from models.engine.file_storage import FileStorage


""" 
    here we load data from out JSON file to the class attribute '__objects' 
    in the instance 'storage', now we can manipulate out database 'file.json'
    as we please using the instance 'storage'
"""
storage = FileStorage()
storage.reload()
