#!/usr/bin/env python
# coding : utf-8

from subprocess import Popen

#early_list = ["adobereader-jpn"]

bioinfo_list = [
    "sci-libs/scipy", 
    "sci-biology/emboss", 
    ""
]


def make_package_list():
    result = []
    result.extend(bioinfo_list)
    #result.extend(R_list2)

    return result


def emerge(pkg_list):
    for ebuild in pkg_list:
        com = "emerge " + ebuid
        print com
        p = Popen(com, shell=True)
        p.wait()


def main():
    pkg_list = make_package_list()
    emerge(apt_list)



if __name__ == "__main__":
    main()

