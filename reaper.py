import time
import easygui

print(r"""   
	    ;::::;                           
           ;::::; :;                          
         ;:::::'   :;                         
        ;:::::;     ;.                        
       ,:::::'       ;           OOO         
       ::::::;       ;          OOOOO        
       ;:::::;       ;         OOOOOOOO       
      ,;::::::;     ;'         / OOOOOOO      
    ;:::::::::`. ,,,;.        /  / DOOOOOO    
  .';:::::::::::::::::;,     /  /     DOOOO   
 ,::::::;::::::;;;;::::;,   /  /        DOOO  
;`::::::`'::::::;;;::::: ,#/  /          DOOO 
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O 
  `:::::`::::::::;'/  / `:#                  
   ::::::`:::::;' /  /  `# 
	 
	 """)


print("""
 _______  _______  _______  _______  _______  _______ 
(  ____ )(  ____ \(  ___  )(  ____ )(  ____ \(  ____ )
| (    )|| (    \/| (   ) || (    )|| (    \/| (    )|
| (____)|| (__    | (___) || (____)|| (__    | (____)|
|     __)|  __)   |  ___  ||  _____)|  __)   |     __)
| (\ (   | (      | (   ) || (      | (      | (\ (   
| ) \ \__| (____/\| )   ( || )      | (____/\| ) \ \__
|/   \__/(_______/|/     \||/       (_______/|/   \__/""")




#reason for dox
print("this is optional, but you can enter the reason for the dox")
reason_for_dox = input(str())

#basic info of the victim
print("first we need some basic info on the victim. If you dont have the required info for a question just type \'NONE\'")
time.sleep(1)
first_name = input(str("What is the first name if the victim? "))
last_name = input(str("what is the last name of the victim? "))
victim_phone_number = input(str("what is the victim's phone number? "))
victim_address = input(str("what is the victims address? "))
victim_age = input(str("what is the victim\'s age?"))
victim_face = input(str("victim\'s face. (Upload the victim\'s face to an image hosting plantform and then enter the link here) "))

print()

#socials
print("now we need the socials of the victim. If you dont have the required info for a question just type \'NONE\'")
time.sleep(1)
facebook = input(str("What is your victim\'s Facebook? "))
instagram = input(str("What is your victim\'s Instagram? "))
twitter = input(str("What is your victim\'s Twitter? "))
youtube = input(str("What is your victim\'s YouTube? "))
discord = input(str("What is your victim\'s Discord? "))
reddit = input(str("What is your victim\'s Reddit? "))
tiktok = input(str("What is your victim\'s TikTok? "))
linkedin = input(str("What is your victim\'s LinkedIn? "))
snapchat = input(str("What is your victim\'s SnapChat? "))

print()

#extra info
print("is there any extra info you would like to enter?")
extra_info = input(str())

#dox name
dox_name = input(str("what would you like the dox name to be?"))

file_save_location = easygui.filesavebox()
f = open(dox_name + ".txt", "w")
f = open(file_save_location,"a")


f.write(r"""
		;::::;                           
           ;::::; :;                          
         ;:::::'   :;                         
        ;:::::;     ;.                        
       ,:::::'       ;           OOO         
       ::::::;       ;          OOOOO        
       ;:::::;       ;         OOOOOOOO       
      ,;::::::;     ;'         / OOOOOOO      
    ;:::::::::`. ,,,;.        /  / DOOOOOO    
  .';:::::::::::::::::;,     /  /     DOOOO   
 ,::::::;::::::;;;;::::;,   /  /        DOOO  
;`::::::`'::::::;;;::::: ,#/  /          DOOO 
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O 
  `:::::`::::::::;'/  / `:#                  
   ::::::`:::::;' /  /  `# 
""" + "\n")

f.write("DOXED WITH REAPER" + "\n")
f.write(" \n")


f.write("Reason for dox: " + reason_for_dox + "\n")

f.write(" \n")
f.write("=====================" + "\n")
f.write(" \n")

f.write("VICTIM INFO:\n")
f.write("First Name: " + first_name + "\n")
f.write("Last Name: " + last_name + "\n")
f.write("Phone Number: " + first_name + "\n")
f.write("Address: " + victim_address + "\n")
f.write("Age: " + victim_age + "\n")
f.write("Face: " + victim_address + "\n")

f.write("  \n")
f.write("=====================\n")
f.write(" \n")

f.write("VICTIM SOCIALS:" + "\n")
f.write("Facebook: " + facebook + "\n")
f.write("Instagram : " + instagram + "\n")
f.write("Twitter: " + twitter + "\n")
f.write("YouTube: " + youtube + "\n")
f.write("Discord: " + discord + "\n")
f.write("Reddit: " + reddit + "\n")
f.write("TikTok: " + tiktok + "\n")
f.write("LinkedIn: " + linkedin + "\n")
f.write("SnapChat: " + snapchat + "\n")

f.write(" " + "\n")
f.write("=====================" + "\n")
f.write(" " + "\n")

f.write("EXTRA INFO" + "\n")
f.write(extra_info + "\n")

f.close()