import os, random, shutil

shutil.rmtree('./DAGM_8/mix')
os.mkdir('./DAGM_8/mix')

###########################################################
def copyFile_OK(fileDir_ok, tarDir):
    pathDir_ok = os.listdir(fileDir_ok)
    sample_ok = random.sample(pathDir_ok, 950)
    for name in sample_ok:
        fname_ok = name.split('.')[0]
        ftype_ok = name.split('.')[1]
        shutil.copyfile(fileDir_ok+name, tarDir+fname_ok+'_OK.'+ftype_ok)
#        shutil.copyfile(fileDir+name, tarDir+name)

def copyFile_NG(fileDir_ng, tarDir):
    pathDir_ng = os.listdir(fileDir_ng)
    sample_ng = random.sample(pathDir_ng, 50)
    for name in sample_ng:
        fname_ng = name.split('.')[0]
        ftype_ng = name.split('.')[1]
        shutil.copyfile(fileDir_ng+name, tarDir+fname_ng+'_NG.'+ftype_ng)
#        shutil.copyfile(fileDir+name, tarDir+name)

if __name__ == '__main__':
    fileDir_OK = './DAGM_8/ok_original/'
    fileDir_NG = './DAGM_8/ng_original/'
    tarDir  = './DAGM_8/mix/'
    copyFile_OK(fileDir_OK, tarDir)
    copyFile_NG(fileDir_NG, tarDir)
