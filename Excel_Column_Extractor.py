import pandas as pd
import glob
import os
from dotenv import load_dotenv
load_dotenv()

filename = os.getenv('filename')
result=[]
# getting excel files from Directory Desktop
path = os.getenv('extraction_path')
file_type = os.getenv('file_type')
sheet = os.getenv('sheet')
column_to_extract = os.getenv('column_to_extract')

def get_files_from_dir(path,file_type):
    # read all the files with extension .xlsx i.e. excel 
    filenames = glob.glob(path + file_type)
    print('File names:', filenames)
    return filenames

def put_IMEI_in_file():
    filenames = get_files_from_dir(path,file_type)
    # for loop to iterate all excel files 
    for file in filenames:
        try:
            # reading excel files
            print("Reading file = ",file)
            df = pd.ExcelFile(file).parse(sheet)
            for i in df[column_to_extract]: 
                    if i not in result: 
                        result.append(i)
        except:
            print("Error in the file uploaded")
        # print(result)

    with open(filename, 'w') as f:
        for row in result:
            print(row)
            f.write("%s\n" % str(row))

def remove_blank_lines_at_end(filename):
    with open(filename) as f_input:
        data = f_input.read().rstrip('\n')

    with open(filename, 'w') as f_output:    
        f_output.write(data)

put_IMEI_in_file()
remove_blank_lines_at_end(filename)