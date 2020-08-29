import logging
logging.basicConfig(filename='info.log', format='%(message)s', level=logging.INFO)


def write_log(line):
    logging.info(line)


def found_in_log(event_id, schedule_date):
    with open('info.log') as f:
        for line in f:
            line = line.strip()
            value = line.split('/')
            if event_id == value[0] and schedule_date == value[1]:
                return True
    return False
