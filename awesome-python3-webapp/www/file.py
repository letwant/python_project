import os
py_file_list = [x[0:-3] for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py' and x != 'file.py']
file_path = os.path.abspath('.')
file_name = file_path.split('\\')[-1:][0]
with open( file_path+'\__init__.py', 'a') as f:
    for py_file in py_file_list:
        f.write('from ' + str(file_name) + ' import ' + py_file + '\n')

os.remove(file_path+'\\file.py')