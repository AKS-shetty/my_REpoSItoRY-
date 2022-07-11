import pywhatkit

numb = input("Enter phone number: ")
pywhatkit.sendwhatmsg(numb, "Hello", 21, 18)

pywhatkit.sendwhatmsg(numb, "hii", 21, 20, 15, True, 2)  # closes tab after sending message in 2sec

#Group message ... every group has group id
gid = input("Enter group id: ")
pywhatkit.sendwhatmsg_to_group(gid, "text", hour, minute)


