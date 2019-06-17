import os, random, shutil
from PIL import Image

dataname = 'DAGM_8'

###########################################################
shutil.rmtree('./'+dataname+'/mix')
os.mkdir('./'+dataname+'/mix')

###########################################################
def copyFile_OK(fileDir_ok, tarDir):
    pathDir_ok = os.listdir(fileDir_ok)
    sample_ok = random.sample(pathDir_ok, 1900)
    for name in sample_ok:
        fname_ok = name.split('.')[0]
        ftype_ok = name.split('.')[1]
        shutil.copyfile(fileDir_ok+name, tarDir+fname_ok+'_OK.'+ftype_ok)
#        shutil.copyfile(fileDir+name, tarDir+name)

def copyFile_NG(fileDir_ng, tarDir):
    pathDir_ng = os.listdir(fileDir_ng)
    sample_ng = random.sample(pathDir_ng, 100)
    for name in sample_ng:
        fname_ng = name.split('.')[0]
        ftype_ng = name.split('.')[1]
        shutil.copyfile(fileDir_ng+name, tarDir+fname_ng+'_NG.'+ftype_ng)
#        shutil.copyfile(fileDir+name, tarDir+name)

if __name__ == '__main__':
    fileDir_OK = './'+dataname+'/ok_original/'
    fileDir_NG = './'+dataname+'/ng_original/'
    tarDir  = './'+dataname+'/mix/'
    copyFile_OK(fileDir_OK, tarDir)
    copyFile_NG(fileDir_NG, tarDir)

items = os.listdir(tarDir)
count_ok, count_ng = 0, 0
for names in items:
    if names.endswith('OK.PNG'):
        count_ok += 1
    if names.endswith('NG.PNG'):
        count_ng += 1
print(count_ok, count_ng)

###########################################################
for i in range(count_ok+count_ng):
    im = Image.open(tarDir+items[i])
    fname = items[i].split('.')[0]
    ftype = items[i].split('.')[1]
    im_2 = im.rotate(90)
    im_2.save(tarDir+fname+'_1.'+ftype)
    im_3 = im.rotate(180)
    im_3.save(tarDir+fname+'_2.'+ftype)
    im_4 = im.rotate(270)
    im_4.save(tarDir+fname+'_3.'+ftype)
    
alls = os.listdir(tarDir)
cnt_ok, cnt_ng = 0, 0
for names in alls:
    if names.endswith('OK.PNG')or names.endswith('OK_1.PNG')or names.endswith('OK_2.PNG')or names.endswith('OK_3.PNG'):
        cnt_ok += 1
    if names.endswith('NG.PNG')or names.endswith('NG_1.PNG')or names.endswith('NG_2.PNG')or names.endswith('NG_3.PNG'):
        cnt_ng += 1
print(cnt_ok, cnt_ng)
