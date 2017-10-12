import os
def rename_files():
  dir_path = os.getcwd() + '/prank'
  os.chdir(dir_path)
  file_list = os.listdir(dir_path)
  for file_name in file_list:
    os.rename(file_name,file_name.translate(None,"0123456789"))
rename_files()