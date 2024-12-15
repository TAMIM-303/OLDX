import platform,os
os.system("clear")
xd = platform.architecture()[0]
if "64" in xd:import OLD
else:print(f"The Old clone tool has not yet been released for {xd} It may be available for all bit versions soon.")
