from shutil import  ignore_patterns, copy2, copystat
import os
import sys


def clone(src,dst):
	
    # if ignore is not None:
    #     ignored_names = ignore(src, names)
    # else:
    #     ignored_names = set()

    #folders_to_copy = ['info','df']

    if not os.path.exists(dst):
    	os.makedirs(dst)

    names = os.listdir(src)
    
    errors = []
    for name in names:
        
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)

        try:
            # if symlinks and os.path.islink(srcname):
            #     linkto = os.readlink(srcname)
            #     os.symlink(linkto, dstname)
            if os.path.isdir(srcname):
                clone(srcname, dstname)
            else:
                copy2(srcname, dstname)
            # XXX What about devices, sockets etc.?
        except (IOError, os.error) as why:
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        
    try:
        copystat(src, dst)
    except WindowsError:
        # can't copy file access times on Windows
        pass
    except OSError as why:
        errors.extend((src, dst, str(why)))
    


if sys.argv[1:] is None or len(sys.argv[1:])>2:
	print "Just put name of src and dst folder"
else:
	source = sys.argv[1]
	destination = sys.argv[2]
	clone(source, destination)