main_list=[12,254,287,[1,1,5]]
req_list=[1,1,5]
def check():
    for i in main_list:
        if i== req_list:
            return True
a=check()
if a:
    print("it's match")
else:
    print("it's gone")
