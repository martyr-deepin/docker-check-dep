#!/usr/bin/env python
# coding=utf-8

import apt
import sys
import os

DEPENDENCY_TYPES = [
    "Depends",
#    "Recommends",
#    "Suggests",
#    "Replaces",
#    "Enhances",
]

def extract_dependencies(package, dependency_type):
    """
    Generator that produce all the dependencies of a particular type
    """
    for dependency_list in package.candidate.get_dependencies(dependency_type):
        for dependency in dependency_list.or_dependencies:
            yield dependency.name

def reverse_dependencies(pkg):
    """Which packages have some kind of dependency on the given package"""

    cache = apt.cache.Cache()
    try:
        pkg = cache[pkg]
    except KeyError as error:
        print(error.args[0])
        sys.exit(1)

    dependents = { name : [] for name in DEPENDENCY_TYPES }

    for key in cache.keys():
        other_package = cache[key]
        for dependency_type, specific_dependents in dependents.items():
            if pkg.shortname in extract_dependencies(other_package, dependency_type):
                specific_dependents.append(other_package.shortname)

    for specific_depend in specific_dependents:
        if specific_depend in pkgs:
            deleted_pkg_file.write(specific_depend)
            deleted_pkg_file.write('\n')

pkg_file = open('resultpkg.log', 'r')
pkgs = []
for line in open('resultpkg.log'):
    line = pkg_file.readline().strip('\n')
    pkgs.append(line)
pkg_file.close()
deleted_pkg_file = open('deleted.list', 'w')

for pkg in pkgs:
    reverse_dependencies(pkg)
deleted_pkg_file.close()
old_deleted = []
new_deleted = []
deleted_pkg = open('deleted.list')
for line in open('deleted.list'):
    line = deleted_pkg.readline().strip('\n')
    old_deleted.append(line)
deleted_pkg.close()
for pkg in old_deleted:
    if pkg not in new_deleted:
        new_deleted.append(pkg)

for pkg in new_deleted:
    if pkg in pkgs:
        pkgs.remove(pkg)

#print(pkgs)
final_file = open('final.log', 'w')
final_file.write('依赖问题关键包: ')
for pkg in pkgs:
    final_file.write(pkg)
    final_file.write(' ')
final_file.close()
