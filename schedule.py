import json
from datetime import datetime
import datetime as dt

def schedule():
    sched = ''
    with open("schedule.json", "r") as f:
        g = json.load(f)

    with open("times.json", "r") as t:
        p = json.load(t)
    

    for y in g:
        print(y + ":")
        sched += y + ":" + "\n"
        for x in g[y]:
            if(x == "-"):
                sched += "No schedule" + "\n"
                print("No schedule")
            else:
                s_time = datetime.strptime(p[x],'%H:%M')
                t_change = dt.timedelta(minutes=100)
                f_time = s_time + t_change
                
                sched += "\t" + "\t" + "\t" + "\t" + "\t" + g[y][x] + " " + s_time.strftime("%I:%M %p") + " - " + str(f_time.time().strftime("%I:%M %p")) + "\n"
                print(g[y][x] + " " + s_time.strftime("%I:%M %p") + " - " + str(f_time.time().strftime("%I:%M %p")))
    return sched
