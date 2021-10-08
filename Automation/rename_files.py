import os

# switching to the required directory
os.chdir(folderPath)

for file in os.listdir():
    file_name, file_extension = os.path.splitext(file)

    # splits the file name into a list of values, based on the separation parameter
    common_str, title = file_name.split("-")
    title.strip()

    # creates new title, with the extracted title value.
    new_title = f"{title}"
    os.rename(file_name + file_extension, new_title + file_extension)
