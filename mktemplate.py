#
# vim: fenc=utf-8:ts=4:et:ai

import os,shutil
dir_name = "20170419_F04"
url = "http://nabetani.sakura.ne.jp/hena/ordf04octsp/"
os.mkdir(dir_name)
shutil.copy("mktemplate.py",dir_name+"/main.py")
# url testarea to testarea.txt