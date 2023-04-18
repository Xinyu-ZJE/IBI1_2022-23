class Triathlon(object):
    def __init__(self,first_name,last_name,location,time_swim,time_cycle,time_run):
        self.first_name=first_name
        self.last_name=last_name
        self.location=location
        self.time_swim=time_swim
        self.time_cycle=time_cycle
        self.time_run=time_run
        self.time_total=time_run+time_swim+time_cycle
    def speak(self):
        print("name: {},{}; location:{}; swim time: {} s; cycle time:{} s; run time:{} s; total time:{} s".format(self.first_name,self.last_name,self.location,self.time_swim,self.time_cycle,self.time_run,self.time_total))
#for example p=Triathlon('first name','last name','location','swim time','cycle time','run time')
p=Triathlon('John','Holmes','London',10,10,10)
p.speak()
# The output is 'name: John,Holmes; location:London; swim time: 10 s; cycle time:10 s; run time:10 s; total time:30 s'
