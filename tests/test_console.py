#!/usr/bin/python3
"""Defines unittests for console.py."""

import os
import unittest
import models
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """Tests the console"""

    def test_do_create(self):
        """ Tests create method """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count State")
            state_count = int(f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Place")
            place_count = int(f.getvalue())
        # checks error message if no class argument given
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        # checks error message if no class argument is invalid
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BadClassName")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        # tests obj created successfully when first object
        HBNBCommand().onecmd("create State name=\"California\"")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count State")
            self.assertEqual(f.getvalue(), "{}\n".format(state_count + 1))
        # tests obj created successfully when not first
        HBNBCommand().onecmd("create State name=\"Nevada\"")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count State")
            self.assertEqual(f.getvalue(), "{}\n".format(state_count + 2))
        # tests obj created with different class, saves id
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                "create Place name=\"My_little_house\" number_rooms=4")
            p_id = f.getvalue()
            p_id = p_id[:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Place")
            self.assertEqual(f.getvalue(), "{}\n".format(place_count + 1))
        # checks that after do_create, obj exists in dictionary
        dict_key = "Place." + p_id
        __objects = FileStorage.all(self)
        self.assertTrue(dict_key in __objects.keys())
        # tests that underscores in value were changed to spaces
        self.assertEqual(__objects[dict_key].name, "My little house")
