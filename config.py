from configparser import ConfigParser

#Get the configparser object
config_object = ConfigParser()

#Assume we need a sections in the config file, let's call SERVERCONFIG

config_object["SERVERCONFIG"] = {
    "count": 16,
    "duration": 0.1,
    "frequency": 2000
}

#Write the above sections to config.ini file
with open('config.ini', 'w') as conf:
    config_object.write(conf)