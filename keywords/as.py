#--- as: Part of the with-as statement. The as keyword is used to create ----
#--- an alias. This allows us to refer to something as our preferred name. ---
import time as shine;

localtime = shine.asctime( shine.localtime(shine.time()) )
print "Local current time :", localtime
