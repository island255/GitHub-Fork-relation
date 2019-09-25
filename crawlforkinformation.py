# -*- coding:utf-8 -*-
'''
Created on 2018年5月13日

@author: Jia Ang
'''

from github import Github
import time
import datetime
import requests
from math import *

def coin_git_mapping():
    coin_git={}
    repo_file=open('coinlink.csv','r')
    lines=repo_file.readlines()
    for index,each_line in enumerate(lines):
        if(not index==0):
            records=each_line.strip('\n').split(',')
            name=records[0]
            coin_git[name]=records[1]
            
    return coin_git

def get_repo_statistics(repo):
    name=repo.full_name
    try:
        download_link=repo.get_archive_link(archive_format="zipball")
        print download_link
        
        download_file_record.write(name.replace("/","+")+".zip"+","+download_link+'\n')
        download_file_record.flush()
    except Exception, e:
        print str(e)


def get_coin_url(coin_git):
    for each_coin in coin_git:
        try:
            repo_name=coin_git[each_coin]
            print repo_name
            repo_name=repo_name.rstrip('/')
            name=repo_name[19:]
            url='https://api.github.com/repos/'+name
            r = requests.get(url,headers=headers)
            if(r.status_code == 200):
                num=num+1
                repo=g.get_repo(name)
                name=repo.full_name
                print name
                if(repo.parent!=None):
                    fork = repo.parent.full_name
                    forksource = repo.source.full_name
                    out_file.write(name+','+fork+','+forksource+'\n')
                    out_file.flush()
            else:
                print 'The repository does not exist: '+name
            time.sleep(0.1)
        except:
            print "connection error!!"
    out_file.close()    


global g
g=Github("d10a0416ce78a66d48bccba259367f9e833e3aff",timeout=1000)
headers = {'Authorization': 'token d10a0416ce78a66d48bccba259367f9e833e3aff'}
coin_git=coin_git_mapping()
# print coin_git


out_file=open('all_coin_fork_relation_20190902.txt','w')

num=0
# download_file_record=open('Repo_download_link.csv','w')
get_coin_url(coin_git)

print num
# download_file_record.close()
    
