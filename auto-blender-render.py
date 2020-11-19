import os
import sys
import os.path
import subprocess
from colorama import init, Fore, Back, Style

init(convert=True)

os.chdir(r'\\filestore\\network storage\\Data\\ITD\\Team-ITD-Super-Site')
que_dir = r'\\filestore\\network storage\\Data\\ITD\\Team-ITD-Super-Site\\Images\\Product Renderings\\Render Queue\\'
finished_dir = r'\\filestore\\network storage\\Data\\ITD\\Team-ITD-Super-Site\\Images\\Product Renderings\\Finished Renderings\\'

for _, folders, files in os.walk(que_dir):

    for folder in folders:

        que_dir_folders = os.path.join(que_dir, folder)
        finished_path = os.path.join(finished_dir, folder)

        if os.path.exists(finished_path):

            print(Fore.YELLOW +
                  '\n\n__________________FOLDER SKIPPED__________________\n\n')
            print(Fore.YELLOW + 'Folder: %s -- Skipped, already exists' % (folder))
            print(Fore.YELLOW + '\n________________________________________________\n')
            print(Style.RESET_ALL)
            continue

        else:

            file_counter = 1
            os.mkdir(finished_path)
            finished_render_folder = finished_path + "\\\\"
            files = os.listdir(que_dir_folders)

            for file in files:
                if file.endswith('.blend'):
                    file_counter + 1
                    file_folder = os.path.join(
                        finished_render_folder, file.replace('.blend', ''))

                    try:

                        subprocess.call(["C:/Program Files/Blender Foundation/Blender 2.90/blender", '--background',
                                         "\\Images\\Product Renderings\\Render Queue\\{}\\{}".format(folder, file), '-o', file_folder, '-a'])
                        print(Fore.GREEN +
                              '\n\n__________________STATUS UPDATE__________________\n\n')
                        print(Fore.GREEN + 'File: %s Complete' % (file))
                        print(Fore.GREEN +
                              'Congrats, have a taco with your success  🌮')
                        print(
                            Fore.GREEN + '\n________________________________________________\n')
                        print(Style.RESET_ALL)

                    except Exception as e:
                        print(e)
                else:
                    print(
                        Fore.YELLOW + '\n\n__________________SKIPPING FILE__________________\n\n')
                    print(Fore.YELLOW + 'File: %s -- Not .BLEND filetype' % (file))
                    print(
                        Fore.YELLOW + '\n________________________________________________\n')
                    print(Style.RESET_ALL)
