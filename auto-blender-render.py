import os
import os.path
import subprocess

que_dir = r'\\filestore\\network storage\\Data\\ITD\\Team-ITD-Super-Site\\Images\\Product Renderings\\Render Queue\\'
finished_dir = r'\\filestore\\network storage\\Data\\ITD\\Team-ITD-Super-Site\\Images\\Product Renderings\\Finished Renderings\\'

for _, folders, files in os.walk(que_dir):

    for folder in folders:

        que_dir_folders = os.path.join(que_dir, folder)
        finished_path = os.path.join(finished_dir, folder)

        if os.path.exists(finished_path):

            print('Folder Already Exists: SKIPPING -- %s' % folder)
            continue

        else:

            file_counter = 1
            os.mkdir(finished_path)
            finished_render_folder = finished_path + "\\\\"
            files = os.listdir(que_dir_folders)

            for file in files:
                file_counter + 1
                file_folder = os.path.join(
                    finished_render_folder, file.replace('.blend', ''))

                try:

                    subprocess.call(["C:/Program Files/Blender Foundation/Blender 2.90/blender", '--background',
                                     "\\Images\\Product Renderings\\Render Queue\\{}\\{}".format(folder, file), '-o', file_folder, '-a'])
                    print('\n\n__________________STATUS UPDATE__________________\n                 File: %s Complete\n________________________________________________\n\n' %
                          (file))
                except Exception as e:
                    print(e)


