#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 18:20:52 2024

@author: Ronja Rösner

Main script for CRYtabia.
"""

# import custom functions for constructing interface
from mainInterface import MainInterface

# import the program name and version from the setup file
from setup import NAME, VERSION
from mapInterface import MAP_ADDON_VERSION
from tableInterface import TABLE_ADDON_VERSION

# turn the importet program info into strings
program_name=str(NAME[0])
program_version=str(VERSION[0])

# function for constructing the application
def main():
	main_window=MainInterface(program_name,program_version,MAP_ADDON_VERSION,TABLE_ADDON_VERSION)
	main_window.focus_set()
	main_window.mainloop()



if __name__ == "__main__":
	main()
