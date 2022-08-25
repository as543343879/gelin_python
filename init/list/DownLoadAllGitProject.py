from urllib.request import urlopen
import json
import subprocess, shlex
import time
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


gitlabToken = 'AN-sr5Vihjayi9DkFEzM'
gitlabAddr = 'gitlab.lizhi.fm'
target = 'zhiyaGroup'


def get_sub_groups(parent_id):
    url = gen_subgroups_url(parent_id)
    allProjects = urlopen(url)
    allProjectsDict = json.loads(allProjects.read().decode()).get('projects')
    sub_ids = []
    if len(allProjectsDict) == 0:
        return sub_ids
    for thisProject in allProjectsDict:
        try:
            thisProjectURL = thisProject['ssh_url_to_repo']
            thisProjectPath = thisProject['path_with_namespace']
            if os.path.exists(thisProjectPath):
                command = shlex.split('git -C "%s" pull' % (thisProjectPath))
            else:
                command = shlex.split('git clone %s %s' % (thisProjectURL, thisProjectPath))
            resultCode = subprocess.Popen(command)
            time.sleep(1)
        except Exception as e:
            print("Error on %s: %s" % (thisProjectURL, e.strerror))
    return sub_ids


def download_code(parent_id):
    get_sub_groups(parent_id)
    return



def gen_subgroups_url(target_id):
    return "https://%s/api/v4/groups/%s/?private_token=%s" % (gitlabAddr, target_id, gitlabToken)


def gen_global_url():
    return "http://%s/api/v4/projects?private_token=%s" % (gitlabAddr, gitlabToken)


def download_global_code():
    url = gen_global_url()
    allProjects = urlopen(url)
    allProjectsDict = json.loads(allProjects.read().decode())
    if len(allProjectsDict) == 0:
        return
    for thisProject in allProjectsDict:
        try:
            thisProjectURL = thisProject['ssh_url_to_repo']
            thisProjectPath = thisProject['path_with_namespace']
            print(thisProjectURL + ' ' + thisProjectPath)

            if os.path.exists(thisProjectPath):
                command = shlex.split('git -C "%s" pull' % (thisProjectPath))
            else:
                command = shlex.split('git clone %s %s' % (thisProjectURL, thisProjectPath))

            resultCode = subprocess.Popen(command)
            print(resultCode)
            time.sleep(1)
        except Exception as e:
            print("Error on %s: %s" % (thisProjectURL, e.strerror))
    return


def main():
    # if target == '':
    #     download_global_code()
    # else:
        url = "https://%s/api/v4/groups?private_token=%s" % (gitlabAddr, gitlabToken)
        allProjects = urlopen(url)
        allProjectsDict = json.loads(allProjects.read().decode())
        if len(allProjectsDict) == 0:
            return
        target_id = ''
        for thisProject in allProjectsDict:
            try:
                this_name = thisProject['name']
                if target == this_name:
                    target_id = thisProject['id']
                    break
            except Exception as e:
                print("Error on %s: %s" % (this_name, e.strerror))
        download_code(target_id)
        return

main()


