#!/bin/bash
import ConfigParser
import os


class GetConf(object):
    CONF_FILE = '../conf/default.conf'
    ELEMENT_PATH = '../conf/'

    def find_file(self, request_file):
        for path, dirs, file_list in os.walk(self.ELEMENT_PATH):
            for file_name in file_list:
                # print file_name
                if file_name[:-5] == request_file:
                    full_name = os.path.join(path, file_name)
                    return full_name
                else:
                    full_name = -1
        if full_name == -1:
            print "can't find conf file: %s" % request_file
            return -1

    def get_value(self, page, section, item):
        conf = ConfigParser.ConfigParser()
        conf_file = self.find_file(page)
        if conf_file != -1:
            conf.read(conf_file)
            value = conf.get(section, item)

        return value
# a = GetConf()
# c = a.find('default')
# print c
# b = a.get('default', 'default', 'base_url')
# print b
