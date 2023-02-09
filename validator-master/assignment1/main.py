import csv
import gzip
import logging
from logging.handlers import RotatingFileHandler
import os
import os.path
import re
import json
import xmltodict
import argparse
import time
import shutil

###### Validate the file name and headers with aggreed format ######
def validatefile(filename, fileregex):
 validregex = "r\"" + fileregex + "\""
 if re.search(eval(validregex), os.path.basename(filename)):
  return True
 else:
  return False

def validate(data, type):  #function for validating the data as per its given type
    try:
        if type==".xml":    #for .xml type
            return True if re.search('<\?xml.*\?>', data).group() else False    #returning True if data has xml tag
        elif type==".json": #for .json type
            return True if json.loads(data) else False                          #returning True if being loaded into dict from given string data of json
        elif type==".csv":  #for .csv data
            return True if data.splitlines()[0].split(',') else False           #returning True if firstline of string data can be seperated by comma (,)
        else:
            raise TypeError('[!] invalid data format')
    except TypeError as error:
        logging.critical(str(error.__class__, error))

def get_file_content(confs):
    outfileDir = str(confs['outfile_directory'])
    archiveDir = str(confs['archive_directory'])
    srcDir = str(confs['source_directory'])
    fileRegex = str(confs['filename_regex'])
    fileExt = str(confs['filename_extension'])
    unknownDir = str(confs['unknown_directory'])
    logging.critical("**********************")
    logging.critical(str(srcDir))
    logging.critical(outfileDir)
    logging.critical(archiveDir)
    logging.critical("**********************")
    if os.path.exists(srcDir):
        files_list = os.listdir(srcDir)
        for file in files_list:
            if not validatefile(file,fileRegex):
                file = str(srcDir)+str(file)
                shutil.move(file,unknownDir)
                logging.critical(file+" fileRegex not matching moving to "+unknownDir)
                continue
            file = str(srcDir)+str(file)    
            if os.path.exists(file):    #checking if given file is existed or not
                filename, ext = os.path.splitext(file) 

                if ext=='.gz':          #checking if given file has .gz extension, and read data in gz format
                    filename, ext = os.path.splitext(filename) #getting the actual file extension (removing .gz)
                    fg = gzip.open(file,'rb')   
                    data = fg.read().decode('utf-8') #reading gz data
                else:                   #if does not have gz extension proceed reading data noramlly
                    fp = open(file,'r')
                    data =fp.read()

                if validate(data,ext):      #data can be validated according to its extension
                    
                    output_filename = outfileDir+str(filename).split('/')[-1] +"_"+ str(int(time.time()))+".json"
                    
                    

                    try:
                        if ext==".xml":    #for .xml type
                            with open(file) as xml_file:
                                data_dict = xmltodict.parse(xml_file.read())

                            json_data = json.dumps(data_dict)
                            output_file = open(output_filename,'w')
                            output_file.write(json_data)     #read data writing to output file
                            shutil.move(file,archiveDir)
                            logging.critical("moved "+str(file) + " to "+ str(archiveDir))
                            
                        elif ext==".json": #for .json type
                            shutil.copy(file,output_filename)
                            shutil.move(file,archiveDir)
                            logging.critical("moved "+str(file) + " to "+ str(archiveDir))
                        elif ext==".csv":  #for .csv data
                            data = {}
                            with open(file, encoding='utf-8') as csvf:
                                csvReader = csv.DictReader(csvf)
                                count = 0
                                for rows in csvReader:
                                    data[count] = rows
                                    count+=1

                            json_data = json.dumps(data)
                            output_file = open(output_filename,'w')
                            output_file.write(json_data)
                            shutil.move(file,archiveDir)
                            logging.critical("moved "+str(file) + " to "+ str(archiveDir))
                        else:
                            raise TypeError('[!] invalid data format')
                    except TypeError as error:
                        logging.critical(str(error.__class__, error))
                    
                else:
                    logging.critical(str(f'[!] improper {ext} data'))
            
            else:
                logging.critical(str('[!] file does not exists'))

def go_to_sleep(loop_start, loop_finish):
    global loop_count
    logging.critical(namespace.collectorname + ':loop:' + str(loop_count) + ' is Finished at ' + time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(loop_finish)) + ' (' + str(loop_finish) + '), after ' + str(loop_finish - loop_start) + ' seconds. with success api rate: ' + str(namespace.validrecords) + '/' + str(namespace.totalrecords))
    loop_count += 1

    # if the interval is "0", by default it will consider as 300 seconds
    if namespace.interval == 0:
        logging.info(namespace.collectorname + 'Interval defined as 0, hence i am going to sleep for 300 seconds ...')
        time.sleep(int(300))
        return True
    else:
        # collect the seconds to sleep after spending the time on current loop
        seconds_to_sleep = (int(namespace.interval) - (loop_finish - loop_start))
        seconds_to_sleep = 0 if seconds_to_sleep < 0 else seconds_to_sleep
        logging.critical(namespace.collectorname + ':next_loop (' + str(loop_count) + ') starts in ' + str(seconds_to_sleep) + ' seconds ...')
        # make the system to sleep for the duration of the sleep time
        if seconds_to_sleep > 0:
            time.sleep(float(seconds_to_sleep))
            return True
        # make the system to start the next loop
        else:
            return True

if __name__ == '__main__':
 ###### Parse and add arguments for the collector ######
    parser = argparse.ArgumentParser()
    parser.add_argument("--interval", default=os.getenv('POLLING_INTERVAL', 300), help="Interval between polls in seconds, Default: 300")
    parser.add_argument("--collectorname", default=os.getenv('SEVONE_COLLECTOR_NAME', 'assignment1'), help="Name of the Collector. Default: 'assignment1'")

    parser.add_argument("--logfile", default=os.getenv("LOG_FILE", '/collector/log/assignment1.log'), help="Log file path. Default: /collector/log/assignment1.log")
    parser.add_argument("--loglevel", default=os.getenv("LOG_LEVEL", 'DEBUG'), help="Log level. Default: 104857600")
    parser.add_argument("--maxlogfilesize", default=os.getenv("MAX_LOG_FILE_SIZE", 104857600), help="Maximum Log file size in Bytes. Default: 104857600")

    parser.add_argument("--maxlogfilecount", default=os.getenv("MAX_LOG_FILE_COUNT", 3), help="Maximum Log file count. Default: 3")
    parser.add_argument("--configjson", default=os.getenv("CONFIGURATION_FILE", '/collector/configs/config.json'), help="configuration json file")

    ###### Reading Arguments to namespace and otherArgs ######
    namespace, otherArgs = parser.parse_known_args() 
 

    ###### Creating Logging configuration ######
    loglevels = {'CRITICAL' : logging.CRITICAL, 'ERROR' : logging.ERROR, 'WARNING' : logging.WARNING, 'INFO' : logging.INFO, 'DEBUG' : logging.DEBUG }
    loglevel = namespace.loglevel
    loglevel = loglevel.upper()
    namespace.maxlogfilesize=int(namespace.maxlogfilesize)
    namespace.maxlogfilecount=int(namespace.maxlogfilecount)
    logging.basicConfig(handlers=[RotatingFileHandler(namespace.logfile,"a", maxBytes=namespace.maxlogfilesize, backupCount=namespace.maxlogfilecount)],
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S %Z',
                        level=loglevels[loglevel])

    start_time = int(time.time())
    logging.critical(namespace.collectorname + ' is Starting at ' + time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(start_time)) + ' (' + str(start_time) + ')')

    loop_count = 1

    while True:

        loop_start = int(time.time())

         ##### To initialize the required variables #####
        namespace.totalrecords = namespace.parsesuccess = namespace.parsefailure = namespace.queryok = namespace.querynotok = namespace.totalparse = namespace.validrecords = 0

        ##### Read the config.json file
        if not os.path.isfile(namespace.configjson):
            logging.critical(namespace.collectorname + ':loop:' + str(loop_count) + ' Main JSON configuration ' + str(namespace.configjson) + ' file does not exist.')
            loop_finish = time.time()
            if go_to_sleep(loop_start, loop_finish):
                continue
        else:
            logging.critical(namespace.collectorname + ':loop:' + str(loop_count) + ' Main JSON configuration ' + str(namespace.configjson) + '     file exist. Continuing the process...')
            try: 
                with open(namespace.configjson, 'r') as configjsonfile:namespace.configdata = json.loads(configjsonfile.read())
            except Exception as e:
                logging.critical(namespace.collectorname + ':loop:' + str(loop_count) + ' Failed to parse the ' + str(namespace.configjson) + ' file. Please verify the configuration file to maintain the JSON format data. Exception: ' + str(e))
                loop_finish = time.time()
                if go_to_sleep(loop_start, loop_finish):
                    continue

        ##### Get the instance configurations of each instance
        namespace.instConfs = {}
        for eachkey, eachconfig in namespace.configdata.items():
            if eachkey == 'settings' and isinstance(namespace.configdata[eachkey], dict):
                for apikey, eachapidata in namespace.configdata[eachkey].items():
                    namespace.instConfs[apikey] = eachapidata['method']
        
        ##### Get the source directories of each instance
        namespace.sourceDirs = { }
        for eachkey,eachconfig in namespace.instConfs.items():
            for apikey, eachapidata in namespace.instConfs[eachkey].items():
                    namespace.sourceDirs[eachkey] = eachconfig['source_directory']

        for levelKey, instconfs in namespace.instConfs.items():
            # files_list = os.listdir(srcDir)
            # logging.critical("Files are as follows")
            # logging.critical(str(files_list))
            # for file in files_list:
            #     file = str(srcDir)+str(file)
            if type(instconfs) == dict and 'source_directory' in list(instconfs.keys()):
                get_file_content(instconfs)

        loop_finish = time.time()
        if go_to_sleep(loop_start, loop_finish):
                continue