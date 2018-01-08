import os

# get file names
# for each file
#     rename

def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir("/Users/letty/Downloads/prank")
    print(file_list)

    # (2) for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
        
rename_files()