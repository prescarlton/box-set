import os

TARGET_DIRECTORY = 'Z:\\Movies\\'
def moveFilesToFolders():
    '''moves all movies to their respective folders in TARGET_DIRECTORY'''
    for _, _, files in os.walk(TARGET_DIRECTORY):
        for file in files:
            dir_name = '.'.join(file.split('.')[:-1])
            if not os.path.exists(TARGET_DIRECTORY + dir_name):
                os.makedirs(TARGET_DIRECTORY + dir_name)
            os.system(f'move "{TARGET_DIRECTORY + file}" "{TARGET_DIRECTORY + dir_name}\\"')
            print(f'move "{TARGET_DIRECTORY + file}" "{TARGET_DIRECTORY + dir_name}\\"')


if __name__ == '__main__':
    moveFilesToFolders()