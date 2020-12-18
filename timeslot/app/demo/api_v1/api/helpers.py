import json

def read_from_file():
    with open("api_v1/api/timeslots.json", "r") as timeslots:
        return json.loads(timeslots.read())

def write_to_file(content):
    with open("api_v1/api/timeslots.json", "w") as timeslots:
        timeslots.write(json.dumps(content))

availability = [
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
