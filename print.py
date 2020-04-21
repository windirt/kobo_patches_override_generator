import yaml

files= ["libadobe.so.yaml","libnickel.so.1.0.0.yaml", "librmsdk.so.1.0.0.yaml","nickel.yaml"]

for file in files:
    data = yaml.load(open(file,'r'),Loader=yaml.FullLoader)
    print("------%s" % file)
    for key in data.keys():
        print("%s: yes" % key)

# data1 = yaml.load(open(file1,'r'),Loader=yaml.FullLoader)
# data2 = yaml.load(open(file2,'r'),Loader=yaml.FullLoader)
# data3 = yaml.load(open(file3,'r'),Loader=yaml.FullLoader)
# data4 = yaml.load(open(file4,'r'),Loader=yaml.FullLoader)

# print("-------libadobe.so.yaml")
# for key in data1.keys():
#     print("%s: yes" % key)

# print("-------libnickel.so.1.0.0.yaml")
# for key in data2.keys():
#     print("%s: yes" % key)

# print("-------librmsdk.so.1.0.0.yaml")
# for key in data3.keys():
#     print("%s: yes" % key)

# print("-------nickel.yaml")
# for key in data4.keys():
#     print("%s: yes" % key)

