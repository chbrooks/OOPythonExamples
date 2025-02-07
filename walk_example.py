import os
import sys

## example of how to use os.walk()

if __name__ == "__main__" :
    if len(sys.argv) > 1 :
        root_name = sys.argv[-1]
    else :
        root_name = "."

    ## root is the path from the top of the tree to the file,
    ## dirs is a generator that gives all the directories
    ## all_files is a generator that gives all the files.
    for root, dirs, all_files in os.walk(root_name):
        # iterate over all the files.
        for f in all_files :
            # to open, we need to join the path and the filename
            # e.g. "./dir1/dir2" and 'file1'
            full_name = os.path.join(root, f)
            try :
                open(full_name, "r")
                print(f"opened {full_name}")
            except :
                print(f"Cannot open {full_name}")