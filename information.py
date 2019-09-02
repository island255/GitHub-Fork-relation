# -*- coding:utf-8 -*-
'''
Created on 2018年5月13日

@author: Yu Qu
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
            if(repo_name.count('/')==4):
                name=repo_name[19:]
                url='https://api.github.com/repos/'+name
                r = requests.get(url,headers=headers)
                if(r.status_code == 200):
                    repo=g.get_repo(name)
                    name=repo.full_name
                    print name
                    created_time=repo.created_at
                    watchers_count=repo.subscribers_count
                    stars_count=repo.stargazers_count
                    forks_count=repo.forks_count
                    out_file.write(name+",https://github.com/"+name+','+created_time.strftime('%Y-%b-%d')+","+str(watchers_count)+","+str(stars_count)+","+str(forks_count)+'\n')
                    out_file.flush()
                    get_repo_statistics(repo)
                else:
                    print 'The repository does not exist: '+name
                time.sleep(0.1)
            elif(repo_name.count('/')==3):
                name=repo_name[repo_name.rindex('/')+1:]
                url='https://api.github.com/users/'+name+'/repos'
                r = requests.get(url,headers=headers)
                if(r.status_code == 200):
                    user=g.get_user(name)
                    repos=user.get_repos()
                    for repo in repos:
                        name=repo.full_name
                        print name
                        created_time=repo.created_at
                        watchers_count=repo.subscribers_count
                        stars_count=repo.stargazers_count
                        forks_count=repo.forks_count
                        out_file.write(name+",https://github.com/"+name+','+created_time.strftime('%Y-%b-%d')+","+str(watchers_count)+","+str(stars_count)+","+str(forks_count)+'\n')
                        out_file.flush()
                        get_repo_statistics(repo)
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

out_file=open('Repo_URl_Readme_new_0814.txt','w')

download_file_record=open('Repo_download_link.csv','w')
get_coin_url(coin_git)
download_file_record.close()
    
