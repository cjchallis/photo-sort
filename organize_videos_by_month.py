import os
import datetime
from shutil import copy


base = os.path.join("C:\\", "Users", "Challis", "Videos", "From Pics")
new = os.path.join("C:\\", "Users", "Challis", "Videos")
no_date = os.path.join(new, "No Date")
for p in (new, no_date):
    if not os.path.exists(p):
        os.makedirs(p)


months = {1: "January",
          2: "February",
          3: "March",
          4: "April",
          5: "May",
          6: "June",
          7: "July",
          8: "August",
          9: "September",
          10: "October",
          11: "November",
          12: "December"
          }

def copy_not_overwrite(src, dest):
    i = 2
    path = os.path.dirname(dest)
    file = os.path.basename(dest)
    print(dest)
    print(file)
    pieces = file.split(".")
    ext = pieces[-1]
    name = "".join(pieces[:-1])
    while os.path.exists(dest):
        dest = os.path.join(path, "{0}_{1:d}.{2}".format(name, i, ext))
        i = i + 1
    copy(src, dest)


for path, subdirs, files in os.walk(base):
    for pic in files:
        full_path = os.path.join(path, pic)
        ext = pic.split(".")[-1]
        if ext.upper() in ["MOV", "MP4"]:
            full_dest = os.path.join(base, pic)
            mtime = os.path.getmtime(full_path)
            date = datetime.datetime.utcfromtimestamp(mtime)
            y = date.year
            m = date.month
            mname = "{0:02d} - {1}".format(m, months[m])
            dest_path = os.path.join(new, str(y), mname)
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            full_dest = os.path.join(dest_path, pic)
        
            copy_not_overwrite(full_path, full_dest)
            os.utime(full_dest, (mtime, mtime))
    


                                         


