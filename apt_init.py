#!/usr/bin/env python
# coding : utf-8

import subprocess

early_list = ["adobereader-jpn"]

japanese_list = ["fcitx", 
                 "fcitx-mozc", 
                 "fcitx-frontend-gtk2",
                 "fcitx-frontend-gtk3",
                 "fcitx-frontend-qt4",
                 "fcitx-frontend-qt5",
                 "fcitx-ui-classic",
                 "fcitx-config-gtk",
                 "mozc-utils-gui"]


emacs_list = [ "emacs24",
               "ess",
               "anthy-el",
               "emacs-goodies-el",
               "scala-mode-el",
               "eldav",
               "w3m-el" ]

dev_list =   ["gcc",
              "gfortran",
              "g++",
              "libc6-dev-amd64",
              "cmake"
              "libreadline6-dev",
              "libpng3",
              "libpng3-dev",
              "netpbm",
              "libnetpbm10",
              "libnetpbm10-dev",
              "flex",
              "perl-doc",
              "tcl-dev",
              "tk-dev",
              "xorg-dev",
              "bison",
              "cmake"]

latex_list = ["tetex-base",
              "tetex-extra",
              "ptex-bin",
              "xdvik-ja",
              "dvipsk-ja", 
              "dvipdfmx",
              "okumura-clsfiles",
              "vfdata-morisawa5",
              "gs",
              "gs-esp",
              "texlive-fonts-recommended",
              "texlive-fonts-extra",
              "texlive-bibtex-extra"]

mysql_list = ["mysql-client-5.6",
              "mysql-server-5.6",
              "mysql-admin",
              "mysql-query-browser"]


net_list = ["openssh-client",
            "openssh-server",
            "firefox",
            "libneon26",
            "libneon26-dev", 
            "apache2",
            "apache2-threaded-dev",
            "apache2-mpm-prefork",
            "apache2-common",
            "apache2-utils",
            "cadaver",
            "ntp",
            "libapache2-svn",
            "subversion",
            "subversion-tools",
            "libapache2-mod-encoding"]


tool_list = ["lha",
             "xdiskusage",
             "ncdu",
             "recoll",
             "task-spooler",
             "inkscape",
             "libclucene-dev",
             "imagemagick",
             "xpdf-japanese",
             "lftp",
             "sysstat"]

perl_list = ["libwww-mechanize-perl",
             "libjson-perl",
             "libset-intspan-perl",
             "libset-scalar-perl"]

R_list = [ "imagemagick",
           "libxt-dev",
           "libgtk2.0-dev",
           "netcdf-bin",
           "netcdfg-dev",
           "libiodbc2-dev",
           "blacs-mpich-dev",
           "blacs1-mpich",
           "libtiff4-dev",
           "libgmp3-dev",
           "libgd2-xpm",
           "libgd2-xpm-dev",
           "libgd-tools",
           "hdf5-tools",
           "h5utils", 
           "ggobi",
           "libgl1-mesa-dev", 
           "libgl1-mesa-dri", 
           "libglu1-mesa-dev",
           "fftw-dev",
           "libgtk2.0-dev",
           "libmysql++-dev",
           "libmysqlclient15-dev",
           "libgsl0",
           "libgsl0-dev",
           "gsl-bin",
           "libhdf5-mpich-dev",
           "libhdf5-mpich-1.6.5-0",
           "h5utils",
           "hdf5-tools",
           "tcllib",
           "libboost-dev",
           "libquantlib-0.3.14",
           "libquantlib0-dev",
           "curl",
           "libcurl4-gnutls-dev",
           "libnetcdf-dev",
           "libxml2",
           "libxml2-dev",
           "openmpi-dev",
           "libgeos-dev",
           "libgdal-dev",
           "libproj-dev",
           "libmpfr-dev",
           "cl-fftw3",
           "libfftw3-dev",
           "libqtcore4",
           "libqt4-core",
           "libsoqt4-dev",
           "coinor-libclp-dev",
           "libudunits2-dev",
           "libdb-dev",
           "glpk",
           "mpc",
           "libmpc-dev",
           "octave",
           "liboctave-dev",
           "libdieharder-dev",
           "liblua5.1-dev",
           "liblua5.2-dev",
           "libsprng2-dev",
           "libapparmor-dev"
           "libsbml5-dev"
           "libzmq-dev"
           "libsndfile1-dev"
           "libgtkmm-2.4-dev"
           "r-base"
           "r-base-core"
           "r-base-dev"
           "r-bioc-*"
           "quantlib-example"]

R_list2 = ["r-cran*"]

java_list = ["maven",
             #"tomcat7",
             #"tomcat7-admin",
             "libc6-i386"]

java_install = """
sudo -E apt-get --install-recommends  purge openjdk*
sudo -E apt-get --install-recommends  -y install software-properties-common
sudo -E add-apt-repository ppa:webupd8team/java
sudo -E apt-get --install-recommends  update
sudo -E apt-get --install-recommends  -y install oracle-java6-installer # Java6
sudo -E apt-get --install-recommends  -y install oracle-java7-installer # Java7
sudo -E apt-get --install-recommends  -y install oracle-java8-installer # Java8
"""

upgrade = """
sudo -E apt-get update
sudo -E apt-get dist-upgrade
"""

#-------------------------------------------

def main():
    exec_lines(java_install)
    install_debs(early_list)
    exec_lines(upgrade)

    apt_list = make_apt_list()
    install_debs(apt_list)


def exec_lines(lines):
    coms = lines.split("\n")
    for com in coms:
        print com
        subprocess.call(com, shell=True)


def make_apt_list():
    result = []
    #result.extend(early_list)
    result.extend(java_list)
    result.extend(emacs_list)
    result.extend(japanese_list)
    result.extend(dev_list)
    result.extend(latex_list)
    #result.extend(mysql_list)
    result.extend(perl_list)
    result.extend(net_list)
    result.extend(tool_list)
    result.extend(R_list)
    result.extend(R_list2)

    return result


def install_debs(apt_list):
    for apt in apt_list:
        com = "sudo -E apt-get --install-recommends  -y install " + apt
        print com
        subprocess.call(com, shell=True)




if __name__ == "__main__":
    main()

