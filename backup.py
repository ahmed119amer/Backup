import shutil
import model.osfunction as osfunction
from model.date import day_name


osfunction.path_change()
# print(name)
# نسخ ملف من مكان معين الى مكان اخر
shutil.copy('gg.jpg',day_name())


# to make copy 
# shutil.copy('gg.jpg', 'gg1.jpg')

# original = r'F:\gg.jpg'
# target = r'F:\Users\gg.jpg'

# shutil.copyfile(original, target)