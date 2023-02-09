import json
import re
import os
import gzip

def validate_filename(filename,settings):
        basename, ext = os.path.splitext(filename)

        f_re = settings[ext]['f_re']

        if re.match(f_re,filename):
            return True
        else:
            return False

        
def validate_data(data, ext, settings):
    
    d_re = settings[ext]['d_re']

    lines = data.splitlines()
    
    for every_line in lines:
        if not re.search(d_re, every_line):
            return False
    else:
        return True



if __name__=="__main__":

    #filename = 'A20221106.1215+0000-20221106.1230+0000_eq0iotsmme03.xml.gz'
    #filename = 'ABB Device 1_1593606077.csv'
    filename = 'G20211124.1830-20211124.1845.json'

    settings_file  = './settings.json'

    if os.path.exists(settings_file) and os.path.exists(filename):
        settings = json.load(open(settings_file,'r'))

        gz_flag = False
        if '.gz' in filename: #checking if given file has .gz extension, and read data in gz format
            filename, ext = os.path.splitext(filename) #getting the actual file extension (removing .gz)
            gz_flag = True

        if validate_filename(filename, settings):    #validating the file naming format

            basename, ext = os.path.splitext(filename)

            if gz_flag:                             #checking if gz flag is set, means gz file if there
                gz_file = gzip.open(filename+'.gz','rb')
                data = gz_file.read().decode('utf-8')
            
            fp = open(filename,'r')
            data =fp.read()


            if validate_data(data, ext, settings):      #validating data format with its extension

                if ext=='.json':                        #extracting json data for deviceName, objectName, indicators
                    deviceName_re = r'\"deviceName\": \"(.*?)\"'
                    objectName_re = r'\"objectName\": \"(.*?)\"'
                    indicators_re = r'\"indicators\": (\{[\s\"a-zA-Z0-9:,]*\})'


                    deviceName_list = re.findall(deviceName_re,data)
                    objectName_list = re.findall(objectName_re,data)
                    indicators_list = [ re.sub(r'[\s]*','',matched_str) for matched_str in re.findall(indicators_re,data) ]

                    result = []
                    for i in range(len(deviceName_list)):
                        result.append({
                                'deviceName' : deviceName_list[i],
                                'objectName' : objectName_list[i],
                                'indicators' : eval(indicators_list[i])
                            })
                
                if ext=='.xml':
                    pass

                if ext=='.csv':
                    pass

                
                output_file = open('./output_file','w')
                output_file.write(str(result))     #data writing to output file
                print('[*] output_file created')

            else:
                print(f'[!] improper {ext} data')
        
        else:
            print('[!] Invalid file naming format')
    else:
        print('[!] settings file or given file not found.')