# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime
import GLOBALS
import JarvisSpeak
import _thread
import threading
import iso8601
from pytz import timezone


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def fetchUpcomingEvents():
    try:
        fmt = '%Y-%m-%d %H:%M:%S %Z'
        ist =  timezone('Asia/Kolkata')
        service = GLOBALS.GOOGLE_SERVICE
        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                            maxResults=10, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])
    
        if not events:
            print('No upcoming events found.')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            d = iso8601.parse_date(start).astimezone(ist)
            print(d.strftime(fmt), event['summary'])
    except:
        print("Failed to fetch events")

def createAnEvent():
    threadName= "CalEventThread"
    listActiveThreads = [th.name.lower() for th in threading.enumerate()]
    print(listActiveThreads)
    if threadName.lower() in listActiveThreads:
        print("Event calendar thread already active.")
        return
        
    GLOBALS.CAL_EVENT_THREAD = MyThread(threadName)
    GLOBALS.CAL_EVENT_THREAD.start()
    



class MyThread(threading.Thread):
   def __init__(self, threadName):
      threading.Thread.__init__(self)
      self.name = threadName
   def run(self):
      print ("Starting " + self.name)
      createEvent(self.name)
      print ("Exiting " + self.name)
    
def createEvent(threadName):
    try:
        service = GLOBALS.GOOGLE_SERVICE
        timeZone = "Asia/Kolkata"
        JarvisSpeak.speak("Creating an event for you.")
        JarvisSpeak.speak("Fill in the details")
        summary= input("Summary:")
        description= input("Description:")
        
        start_date= input("start date: 'YYYY-MM-DD':")
        start_time= input("start time: 'HH:MM:SS':")
        start_date_time = str(start_date)+'T'+str(start_time)+'+05:30'
        print("Start date time is: "+start_date_time)
        
        end_date= input("end date: 'YYYY-MM-DD':")
        end_time= input("end time: 'HH:MM:SS':")
        #2020-07-11T09:00:00+05:30
        end_date_time = str(end_date)+'T'+str(end_time)+'+05:30'
        print("End date time is: "+end_date_time)
         
        attendees_list = []
        n = int(input("Enter number of attendees: "))
        for i in range(0, n): 
            ele = input("enter attendee:") 
            attendees_list.append(ele)
            
        print(attendees_list)
        
        reminder_email_minutes = input("Reminder email in Minutes:")
        reminder_email_popup_minutes = input("Popup in Minutes:")
        
        attendeesDictList=[]
        for attendee in attendees_list:
            attendeesDictList.append({
                "email":attendee
            })
        
        event = {
          'summary': summary,
          'location': '',
          'description': description,
          'start': {
            'dateTime': start_date_time,
            'timeZone': timeZone,
          },
          'end': {
            'dateTime': end_date_time,
            'timeZone': timeZone,
          },
          'recurrence': [],
          'attendees': attendeesDictList,
          'reminders': {
            'useDefault': False,
            'overrides': [
              {'method': 'email', 'minutes': reminder_email_minutes},
              {'method': 'popup', 'minutes': reminder_email_popup_minutes},
            ],
          }
        }
        print(event)        
        event_actual = service.events().insert(calendarId='primary', body=event).execute()
        print('Event created: %s' % (event_actual.get('htmlLink')))
        JarvisSpeak.speak("Event created successfully")
        
    except Exception as e:
        print("Failed to create an event: {}".format(e))
        JarvisSpeak.speak("Failed to create an event. Try again.")


