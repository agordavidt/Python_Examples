#!/usr/bin/python
"""Defines an object attribute lookup function."""

def loockup(obj):
	""Return a list of an object's available attributes."""
	return (dir(obj)
