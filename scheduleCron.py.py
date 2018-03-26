from crontab import CronTab # this code will schedule the Twilio web app hourly except when john is in sleep
 
my_cron = CronTab(user='root')
job = my_cron.new(command='python app.py')
job.minute().on(0)
job.hour().during(7,22) # Assuming that john is sleeping for 10 p.m. to 7 a.m.
 
my_cron.write()
