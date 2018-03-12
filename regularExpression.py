import re
text = "(021)88776543 010-55667890 02584453362 0571 66345673 "
m = re.findall(r"\(?0\d{2,3}[) -]?\d{7,8}", text)
if m:
    print (m)
else:
    print ('not match')


# print('\be\tf')

import re
text = "红海行动真是一部经典的电影，好电影， "
m = re.findall(r"['经典' '好']?", text)
if m:
    print (m)
else:
    print ('not match')



