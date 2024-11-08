from modules.module1 import module1_func
from modules.module2 import module2_func

# Импорт из пакета
from package.folder1.file1 import file1_func_folder1
from package.folder1.file2 import file2_func_folder1
from package.folder2.file1 import file1_func_folder2
from package.folder2.file2 import file2_func_folder2
from package.folder3.file1 import file1_func_folder3
from package.folder3.file2 import file2_func_folder3
from package.folder2.nested_folder.file1 import file1_func_nested
from package.folder2.nested_folder.file2 import file2_func_nested

# Вызов функций
module1_func()
module2_func()
file1_func_folder1()
file2_func_folder1()
file1_func_folder2()
file2_func_folder2()
file1_func_folder3()
file2_func_folder3()
file1_func_nested()
file2_func_nested()