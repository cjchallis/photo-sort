import os
import exifread
from shutil import copy


base = os.path.join("C:\\", "Users", "Challis", "Pictures", "Imports")
new = os.path.join("C:\\", "Users", "Challis", "Pictures")
no_date = os.path.join(new, "No Date")
vidbase = os.path.join("C:\\", "Users", "Challis", "Videos", "From Pics")

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
            full_dest = os.path.join(vidbase, pic)
        else:    
            f = open(full_path, 'rb')
            tags = exifread.process_file(f)
            try:
                date = tags["EXIF DateTimeOriginal"].values
            except KeyError:
                full_dest = os.path.join(no_date, pic)
            else:                
                y, m = date.split(":")[0:2]
                f.close()
                mname = "{0} - {1}".format(m, months[int(m)])
                dest_path = os.path.join(new, y, mname)
                if not os.path.exists(dest_path):
                    os.makedirs(dest_path)
                full_dest = os.path.join(dest_path, pic)
        
        copy_not_overwrite(full_path, full_dest)
    


                                         


