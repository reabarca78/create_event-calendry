def create_payload(email, invitee_landed_at, start_time, event_id):
    return {"analytics": {"invitee_landed_at": invitee_landed_at, "browser": "Firefox 77",
                         "device": "Kali Linux VM", "fields_filled": 3, "fields_presented": 4,
                         "booking_flow": "v3", "seconds_to_convert": 150}, "embed": {},
           "event": {"start_time": start_time,
                     "location_configuration": {"kind": "physical", "location": "Gold's Gym Uruca",
                                                "phone_number": None, "additional_info": None}, "guests": {}},
           "event_fields": [{"id": 17948761, "name": "Please share anything that will help prepare for our meeting.",
                             "format": "text", "required": False, "position": 0, "answer_choices": None,
                             "include_other": False, "value": ""}], "event_type_uuid": event_id,
           "invitee": {"timezone": "America/Guatemala", "time_notation": "24h", "full_name": "Eduardo Abarca",
                       "email": email, "phone_number": "+506 8888 8888"}, "payment_token": {},
           "recaptcha_token": "", "single_use_slug": False, "tracking": {}}

