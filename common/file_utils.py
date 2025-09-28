import json
import os
import shutil
import zipfile


def convert_project_to_string(project_path: str) -> str:
    extraction_path = "extracted_folder"
    if os.path.exists(extraction_path) and os.path.isdir(extraction_path):
        shutil.rmtree(extraction_path)

    try:
        with zipfile.ZipFile(project_path, 'r') as zip_ref:
            zip_ref.extractall(extraction_path)
        print(f"All contents of '{project_path}' extracted to '{extraction_path}' successfully.")
    except FileNotFoundError:
        print(f"Error: Zip file '{project_path}' not found.")
    except zipfile.BadZipFile:
        print(f"Error: '{project_path}' is not a valid zip file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    file_content_list = []
    for dirpath, dirnames, filenames in os.walk(extraction_path):
        # print("traverse directory", dirpath, dirnames, filenames)
        for filename in filenames:
            full_file_path = os.path.join(dirpath, filename)
            # print("full file path: ", full_file_path)
            file_path = full_file_path.replace("extracted_folder/", "")
            file_path_list = file_path.split("/")
            file_path = "/".join(file_path_list[1:])
            print(file_path)
            file_content = ""
            with open(full_file_path, "r") as file:
                file_content = file.read()
            file_content_list.append({
                "file_path": file_path,
                "file_content": file_content,
            })
    if os.path.exists(extraction_path) and os.path.isdir(extraction_path):
        shutil.rmtree(extraction_path)
    if os.path.exists(project_path):
        os.remove(project_path)
    return json.dumps(file_content_list)


# s = convert_project_to_string("assets/nestjs-channel-messenger-demo-main.zip")
# with open("tmp.txt", "w") as file:
#     file.write(s)
# print("write {} characters to tmp.txt".format(len(s)))
