from datetime import datetime

def time():
    now = datetime.now()
    time = now.strftime("%H:%M %P")
    time_int = int(time[0:2])
    return time_int
def time_meridian():
    now = datetime.now()
    time = now.strftime("%H:%M %P")
    time_str = time[6:8]
    return time_str

def sample_responses(input_text):
    user_message = str(input_text).lower()
    
    if user_message in ("hello", "hi"):
        if time() <= 8 and time() >= 5 and time_meridian() == "PM": 
            return "Good Morning, sir! How can I help you today?"
        elif time() <= 8 and time() >= 5 and time_meridian() == "AM":
            return "Good Evening, sir! How can I help you?"
        else:
            return "How can I help you today?"
        
    if user_message in ("who are you", "who are you?"):
        return "I am Bo-bot"
    
    if user_message in ("levi"):
        return "That's the name of my creator. You can reach him at @Leviticus_98."
    
    if user_message in ("who made you", "who made you?"):
        return "My creator is Levi. You can reach him at @Leviticus_98."
    
    if user_message in ("time", "what time is it?", "what time is it"):
        now = datetime.now()
        date_time = now.strftime("%d-%m-%y, %H:%M:%S")
        return str(date_time)
    return "I don't understand you"

def help():
    help_str = ("{}" "\n" "{}" "\n" "{}" "\n" "{}" "\n" "{}").format("For time, ask 'time', 'what time is it',", "For books, ask /book,", "For bot's identity, ask 'who are you' or /about", "For author's info, ask 'who made you'", "For Covid report, ask /covid")
    return help_str