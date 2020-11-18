import os, os.path
import subprocess


root_path = r'\\filestore\\network storage\\Data\\ITD\\Team-ITD-Super-Site\\Images\\Product Renderings\\Render Queue\\'
render_queue = r'\\filestore\\network storage\\Data\\ITD\\Team-ITD-Super-Site\\Images\\Product Renderings\\Render Queue\\'
finished_renders = r'\\filestore\\network storage\\Data\\ITD\\Team-ITD-Super-Site\\Images\\Product Renderings\\Finished Renderings\\'

for _, folders, files in  os.walk(render_queue):
    
    for folder in folders:
        
        render_queue_folders = os.path.join(root_path, folder)
        finish_path = os.path.join(finished_renders, folder)

        files = os.listdir(render_queue_folders)

        for file in files:
            os.mkdir(finish_path)
            inside_finish_path = finish_path + "\\\\yes_queeeeeeeeeen"
            subprocess.call(["C:/Program Files/Blender Foundation/Blender 2.90/blender", '--background', "\\Images\\Product Renderings\\Render Queue\\{}\\{}".format(folder, file), '-o', finish_path, '-a'])

            



