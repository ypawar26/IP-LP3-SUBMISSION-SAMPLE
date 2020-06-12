#YASHODEEP PAWAR USERID:2470
string=input()
def removeduplicate(string):
    uniqs=''
    for x in string:
        if not(x in uniqs):
            uniqs=uniqs+x
    return uniqs
print(removeduplicate(string))