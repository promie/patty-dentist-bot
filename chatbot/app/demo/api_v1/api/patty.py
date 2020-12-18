import re
from .helpers import sorted_availability, get_dentists, get_timeslot_for_dentist, get_reservation_list, emphasize_text, make_reservation, make_cancellation, find_key, get_dentists_names, sorted_available_timeslots, available_slots_by_day

def ask_patty(answer, expression):

  dentists_properties = get_dentists()
  dentists_names = get_dentists_names(dentists_properties)
  
  # Check whether the user has enquire about the individual dentist details
  expression_lower = [re.sub(r"[^a-zA-Z0-9]+", '', word.lower()) for word in expression.split()]
  dentists_lower = [name.lower() for name in dentists_names]

  dentist_info = set(expression_lower).intersection(dentists_lower)

  # THIS STATE CHECKS TO SEE IF THERE IS A KEYWORD FOR DENTIST OR DENTISTS IN ORDER TO RETURN THE LIST
  if answer == 'GET_ALL_DENTISTS' or 'dentists' in expression.lower() or 'dentist' in expression.lower():
    separator = ', '
    answer = f'Here is the list of our dentists:<br /><br />{emphasize_text(separator.join(dentists_names))}<br /><br />If you wish to see more information about each dentist you can simply type the name in the chat box'
    # THIS STATE CHECK THE KEYWORD OF TIMESLOT, AVAILABILITY OR AVAILABLE KEYWORD IN ORDER TO RETURN THE TIMESLOT
  elif answer == 'GET_TIMESLOTS' or 'timeslot' in expression.lower() or 'availability' in expression.lower() or 'available' in expression.lower() or 'time slot' in expression.lower() or 'time' in expression.lower():
    # check if the dentist name is there
    if len(dentist_info) == 0:
      answer = f"Please specify the dentists name for timeslot and availability. For example: {emphasize_text('<br /><br />Please show me availability for Patrick.')} or <br />{emphasize_text('When is Patrick available on Friday?')}"
      return answer
    else:

      dentist_name = list(dentist_info)[0].title()
      available_slots = get_timeslot_for_dentist(dentist_name)
      separator = ', '

      # GET AVAILABILITY FOR SPECIFIC DAY
      if 'mon' in expression.lower() or 'tue' in expression.lower() or 'wed' in expression.lower() or 'thur' in expression.lower() or 'fri' in expression.lower() or 'sat' in expression.lower() or 'sun' in expression.lower():
        available_slots_daily = available_slots_by_day(available_slots, expression)
        sorted_availability = sorted_available_timeslots(available_slots_daily)

        answer = f'Here is the list of availability for {emphasize_text(dentist_name)}: <br /><br />{emphasize_text(separator.join(sorted_availability))}'
      else:
        sorted_availability = sorted_available_timeslots(available_slots)

        answer = f'Here is the list of availability for {emphasize_text(dentist_name)}: <br /><br />{emphasize_text(separator.join(sorted_availability))}'
  # THIS STATE CHECKS THE LIST OF APPOINTMENTS
  elif answer == 'GET_APPOINTMENTS' or 'list of appointments' in expression.lower() or 'list of bookings' in expression.lower() or "list bookings" in expression.lower() or "list appointments" in expression.lower():
    if len(dentist_info) == 0:
      answer = f"Please specify the dentists name for the appointment list. For example: <br /><br />{emphasize_text('Please list of bookings with <em>Patrick</em>')} or <br />{emphasize_text('Display a list of appointments with <em>Patrick</em>')}"
      return answer
    else:

      dentist_name = list(dentist_info)[0].title()
      reserved_slots = get_reservation_list(dentist_name)
      separator = ', '
      appointment_text = 'appointments' if len(reserved_slots) > 1 else 'appointment'

      if len(reserved_slots) == 0:
        answer = f'You do not have any appointments with {emphasize_text(dentist_name)}. To make an appointment, simply type: <span style="color: green"><strong>APP:{dentist_name}:[Timeslot]</strong></span>'
      else:
        answer = f'You have {emphasize_text(len(reserved_slots))} {emphasize_text(appointment_text)} with {emphasize_text(dentist_name)}: {emphasize_text(separator.join(reserved_slots))}'

  # THIS STATE CHECKS FOR THE KEYWORD CANCEL
  elif answer == 'HOW_TO_CANCEL' or 'cancel' in expression.lower():
    answer = f"To cancel an appointment, please type: <br /><br />{emphasize_text('CAN:[Dentists Name]:[Timeslot]')}<br /><br />For Example:<br/><br />{emphasize_text('CAN:Patrick:Fri 9am-10am')}"

  # THIS STATE CHECKS FOR THE KEYWORD RESERVE, BOOK, RESERVATION, APPOINTMENT
  elif answer == 'MAKE_RESERVATION' or 'reserve' in expression.lower() or 'book' in expression.lower() or 'reservation' in expression.lower() or 'appointment' in expression.lower():
    answer = f"To make an appointment, please type: <br />{emphasize_text('APP:[Dentists Name]:[Timeslot]')}<br /><br />For Example:<br/><br />{emphasize_text('APP:Patrick:Mon 9am-10am')}"
  
  # THIS STATE IS WHEN USER MAKE A RESERVATION
  elif expression.lower().startswith('app:'):
    name = expression.split(':')[1].title()
    timeslot_id = expression.split(':')[2]

    if name.lower() not in dentists_lower:
      answer = 'Appointment cannot be processed! Please ensure that you spelt the dentist name and specify timeslot correctly'
    else:          
      existing_reservation = get_reservation_list(name)

      if timeslot_id in existing_reservation:
        # Get all timeslots for dentists
        available_slots = get_timeslot_for_dentist(name)
        available_slots_daily = available_slots_by_day(available_slots, timeslot_id)
        sorted_availability = sorted_available_timeslots(available_slots_daily)
        separator = ', '

        answer = f'{emphasize_text(name)} is already reserved for {emphasize_text(timeslot_id)}. You can select any of the following available timeslots for {emphasize_text(name)} on the same day: <br /><br />{emphasize_text(separator.join(sorted_availability))}'
      else:
        answer = make_reservation(name, timeslot_id)

  # THIS STATE IS WHEN THE USER CANCELS A RESERVATION
  elif expression.lower().startswith('can:'):
    name = expression.split(':')[1].title()
    timeslot_id = expression.split(':')[2]

    if name.lower() not in dentists_lower:
      answer = 'Cancellation cannot be processed! Please ensure that you spelt the dentist name and specify timeslot correctly'
    else:
      existing_reservation = get_reservation_list(name)

      if timeslot_id not in existing_reservation:
        answer = f"Cancellation cannot be processed as you do not have an appointment with {emphasize_text(name)} for {emphasize_text(timeslot_id)}."
      else:
        answer = make_cancellation(name, timeslot_id)
  
  # THIS BLOCK IS WHEN THERE IS THE NAME OF THE DENTIST BEING MENTIONED. IT WILL RETRIEVE INFORMATION FOR DENTIST
  elif answer == 'GET_DENTIST_INFO' or len(dentist_info) > 0:
    dentist_name = list(dentist_info)[0].title()

    dentist_info = next((sub for sub in dentists_properties if sub['name'] == dentist_name), None)
    dentist_specialization = dentist_info['specialization']
    dentist_location = dentist_info['location']
  
    answer = f'{emphasize_text(dentist_name)} specializes in {emphasize_text(dentist_specialization)} and is currently based in {emphasize_text(dentist_location)}.'

  return answer

