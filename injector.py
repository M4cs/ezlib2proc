import os

class Runner:
    def __init__(self):
        self.running = False

if os.path.exists(os.path.realpath('./lib2proc')) and os.path.exists(os.path.realpath('./lib2proc.dylib')):
    pass
else:
    print("Error! Can't Find the lib2proc binary... Is it in this folder?")
runner = Runner()
pid = input("Enter PID to Target: ")
dll_path = os.path.realpath(input("Enter Path To Library to Inject: ")) 
mono = int(input("Mono? (0 = No; 1 = Yes): "))
if mono == 1:
    mono_ns = input("Namespace: ")
    mono_module = input("Class: ")
    mono_func = input("Load Method: ")
    mono_unload_func = input("Unload Method: ")
else:
    mono_ns = ""
    mono_module = ""
    mono_func = ""
    mono_unload_func = ""

query = "./lib2proc {} {}".format(pid, dll_path)
if mono:
    query += " --mono " + ".".join([mono_ns, mono_module, mono_func])
x = os.system(query)
if x != 0:
    exit()
runner.running = True
print("\nType Unload to Unload Library, Load to Reload the Library (May Crash Game), or Quit to Exit\n")
uquery = "./lib2proc {} {}".format(pid, dll_path)
if mono:
    uquery += " --mono " + ".".join([mono_ns, mono_module, mono_unload_func])
while True:
    cmd = input(">")
    if unload.lower() == "unload":
        if runner.running:
            os.system(uquery)
        runner.running = False
    if cmd.lower() == "load":
        if runner.running:
            os.system(uquery)
        runner.running = False
        os.system(query)
    if cmd.lower() == "quit":
        runner.running = False
        exit()
    
