import requests
import smtplib 


api_key = "get api key for gmaps from dev site"


# home address input
home = input("Enter a home address\n") 
  
# work address input
clg = input("Enter a college address\n") 
  
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

# get response
r = requests.get(url + "origins=" + home + "&destinations=" + clg + "&key=" + api_key) 
 
# return time as text and as seconds
time = r.json()["rows"][0]["elements"][0]["duration"]["text"]       
seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]
  

print("\nThe total travel time from home to college is", time)

# check if travel time is more than 1 hour
if (seconds > 3600):
    # give your own data
    sender = "my mail"    
    recipient = "friend's mail"       
    subject = "Can't Reach..."   
    message = "Hi bro,\n\nSorry, but I can't make it to the college today. There is way too much traffic !"
    
    
    email = "Subject: {}\n\n{}".format(subject, message)
    
    s = smtplib.SMTP("smtp.gmail.com", 587) 
      
    s.starttls()        
    s.login(sender, password)     
    
    s.sendmail(sender, recipient, email) 
    s.quit() 
  
    print("\nSuccessfully sent a email to", recipient, "since the travel time was too long")