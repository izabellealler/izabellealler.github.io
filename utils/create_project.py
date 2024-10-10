import os
from datetime import datetime
from pathlib import Path

TODAY = datetime.now().strftime('%m%d')
YEAR = datetime.now().strftime('%Y')
SUBFOLDERS = ['docs', 'src']
PATH_DIR = Path(f'./projects/{YEAR}')
FODER_NAME = Path(f'project_{TODAY}')


def create_folder(path: str):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            print(f'Folder {path} created successfully.')
        else:
            print(f'Folder {path} already exists.')
    except Exception as e:
        print(f'Error: {e}')


def create_project_folder():
    try:
        project_path = os.path.join(PATH_DIR, FODER_NAME)
        create_folder(project_path)
        create_subfolders(project_path)
    except Exception as e:
        print(f'Error: {e}')


def create_subfolders(path: str):
    try:
        for subfolder in SUBFOLDERS:
            subfolder_path = os.path.join(path, subfolder)
            create_folder(subfolder_path)
            if subfolder == 'docs':
                create_index(subfolder_path)
            if subfolder == 'src':
                create_dotpy(subfolder_path)
    except Exception as e:
        print(f'Error: {e}')


def create_index(path: str):
    index_path = os.path.join(path, 'index.md')
    try:
        with open(index_path, 'w', encoding='utf-8') as folder:
            folder.write('# Title\n')
    except Exception as e:
        print(f'Error: {e}')


def create_dotpy(path: str):
    dotpy_path = os.path.join(path, 'sketch.py')
    try:
        with open(dotpy_path, 'w', encoding='utf-8') as folder:
            folder.write('# Comment\n')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    if os.path.exists(PATH_DIR):
        create_project_folder()
    else:
        create_folder(PATH_DIR)
        create_project_folder()
