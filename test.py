__author__ = 'pavel'

#import sys
#sys.path.append('clouds')
import clouds.yandex_disk as YaDisk
import clouds.google_drive as GDrive

def main():

    ya_user = ''
    ya_pwd = ''

    #api = YaDisk.YandexDisk('./secrets/yandex.json')

    #print(api.ls('/Photo'))

    #api.mkdirs('eyadisk/333/4444/555')
    #api.upload('./README.md', '/eyadisk/README.MD')
    #print(api.publish('/eyadisk/README.MD'))

    gdrive = GDrive.GoogleDrive('./secrets/google.json')
    # files = gdrive.ls('/Documents/')
    # for f in files:
    #     print(f.name+' '+f.mtype)
    #
    # print(gdrive.dirs_cache)
    gdrive.mkdir('ervwrbrbtrthnrnryn22/rberbtybetb/rebtbetytnt5n/tb4t4tn4yn4yn')


if __name__ == '__main__':
	main()