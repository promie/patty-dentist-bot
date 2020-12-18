import requests

def get_dentists():
  result = requests.get('http://localhost:8000/api/v1/dentists')

  jsonResult = result.json()

  return jsonResult

def get_timeslot_for_dentist(did):
  result = requests.get(f'http://localhost:4000/api/v1/dentists/{did}/timeslots')

  jsonResult = result.json()
  available_slots = list(find_key(jsonResult['times'], 'available'))

  return available_slots

def get_reservation_list(did):
  result = requests.get(f'http://localhost:4000/api/v1/dentists/{did}/timeslots')

  jsonResult = result.json()
  reserved_slots = list(find_key(jsonResult['times'], 'reserved'))

  return reserved_slots
  

def emphasize_text(txt):
  return f'<span style="color: green"><strong>{txt}</strong></span>'

def make_reservation(did, timeslot_id):
  try:
    result = requests.put(f'http://localhost:4000/api/v1/dentists/{did}/timeslots/{timeslot_id}/reserve')

    jsonResult = result.json()
    return jsonResult['message']

  except:
    return 'Appointment cannot be processed! Please ensure that you spelt the dentist name and specify timeslot correctly'


def make_cancellation(did, timeslot_id):
  try:
    result = requests.put(f'http://localhost:4000/api/v1/dentists/{did}/timeslots/{timeslot_id}/cancel')

    jsonResult = result.json()
    return jsonResult['message']

  except:
    return 'Cancellation cannot be processed! Please ensure that you spelt the dentist name and specify timeslot correctly'
  
def find_key(input_dict, value):
    return {k for k, v in input_dict.items() if v == value}


def get_dentists_names(dentists_list):
  dentists = []

  for dentist in dentists_list:
    dentists.append(dentist.get('name'))
  
  return sorted(dentists)

def sorted_available_timeslots(original_timeslots):
  new_sorted_list = []

  for lst in sorted_availability:
    if lst in original_timeslots:
      new_sorted_list.append(lst)
  
  return new_sorted_list

def available_slots_by_day(available_slots, expression):
  if 'mon' in expression.lower():
    result = list(filter(lambda x: x.startswith('Mon'), available_slots))
  elif 'tue' in expression.lower():
    result = list(filter(lambda x: x.startswith('Tue'), available_slots))
  elif 'wed' in expression.lower():
    result = list(filter(lambda x: x.startswith('Wed'), available_slots))
  elif 'thu' in expression.lower():
    result = list(filter(lambda x: x.startswith('Thur'), available_slots))
  elif 'fri' in expression.lower():
    result = list(filter(lambda x: x.startswith('Fri'), available_slots))
  elif 'sat' in expression.lower():
    result = list(filter(lambda x: x.startswith('Sat'), available_slots))
  elif 'sun' in expression.lower():
    result = list(filter(lambda x: x.startswith('Sun'), available_slots))

  return result
  


sorted_availability = [
      "Mon 9am-10am",
      "Mon 10am-11am",
      "Mon 11am-12pm",
      "Mon 12pm-1pm",
      "Mon 1pm-2pm",
      "Mon 2pm-3pm",
      "Mon 3pm-4pm",
      "Mon 4pm-5pm",
      "Tue 9am-10am",
      "Tue 10am-11am",
      "Tue 11am-12pm",
      "Tue 12pm-1pm",
      "Tue 1pm-2pm",
      "Tue 2pm-3pm",
      "Tue 3pm-4pm",
      "Tue 4pm-5pm",
      "Wed 9am-10am",
      "Wed 10am-11am",
      "Wed 11am-12pm",
      "Wed 12pm-1pm",
      "Wed 1pm-2pm",
      "Wed 2pm-3pm",
      "Wed 3pm-4pm",
      "Wed 4pm-5pm",
      "Thu 9am-10am",
      "Thu 10am-11am",
      "Thu 11am-12pm",
      "Thu 12pm-1pm",
      "Thu 1pm-2pm",
      "Thu 2pm-3pm",
      "Thu 3pm-4pm",
      "Thu 4pm-5pm",
      "Fri 9am-10am",
      "Fri 10am-11am",
      "Fri 11am-12pm",
      "Fri 12pm-1pm",
      "Fri 1pm-2pm",
      "Fri 2pm-3pm",
      "Fri 3pm-4pm",
      "Fri 4pm-5pm",
      "Sat 9am-10am",
      "Sat 10am-11am",
      "Sat 11am-12pm",
      "Sat 12pm-1pm",
      "Sat 1pm-2pm",
      "Sat 2pm-3pm",
      "Sat 3pm-4pm",
      "Sat 4pm-5pm",
      "Sun 9am-10am",
      "Sun 10am-11am",
      "Sun 11am-12pm",
      "Sun 12pm-1pm",
      "Sun 1pm-2pm",
      "Sun 2pm-3pm",
      "Sun 3pm-4pm",
      "Sun 4pm-5pm"
]