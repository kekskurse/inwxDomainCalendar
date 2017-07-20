from inwx import domrobot, prettyprint, getOTP
from configuration import get_account_data
from icalendar import Calendar, Event
import datetime
import dateutil.parser



cal = Calendar()

def main():
    api_url, username, password, shared_secret = get_account_data(True, "config.cfg", "live")
    inwx_conn = domrobot(api_url, False)
    loginRet = inwx_conn.account.login({'lang': 'en', 'user': username, 'pass': password})

    if 'resData' in loginRet:
        loginRet = loginRet['resData']

    if 'tfa' in loginRet and loginRet['tfa'] == 'GOOGLE-AUTH':
        loginRet = inwx_conn.account.unlock({'tan': getOTP(shared_secret)})

    domainList = inwx_conn.domain.list({})
    for domain in domainList["resData"]["domain"]:
         reDate = dateutil.parser.parse(str(domain["reDate"]))
         upDate = dateutil.parser.parse(str(domain["upDate"]))

         preReData = (reDate - datetime.timedelta(days = 5))

         event = Event()
         event.add('summary', 'REMINDER! Domain Renewal '+domain["domain"])
         event.add('dtstart', preReData)
         event.add('dtend', (preReData + datetime.timedelta(minutes = 10)))
         event.add('dtstamp', upDate)
         cal.add_component(event)

         event = Event()
         event.add('summary', 'Domain Renewal '+domain["domain"])
         event.add('dtstart', reDate)
         event.add('dtend', (reDate + datetime.timedelta(minutes = 10)))
         event.add('dtstamp', upDate)
         cal.add_component(event)
         print(event)
    f = open('domains.ical', 'wb')
    f.write(cal.to_ical())
    f.close()

if __name__ == '__main__':
    main()
