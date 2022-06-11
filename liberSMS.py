import sqlite3
from datetime import date
from resh_calc import resh_calc
import schedule
from textmyself2 import textmyself
import time
import os

def schedule_texts():
    # Get current date
    today = date.today()
    today = str(today)

    # Making sure that the correct dirctory is being looked at for the DB
    script_directory = os.path.dirname(os.path.abspath(__file__))
    data_base = os.path.join(script_directory, "Your_DB_here.sqlite")

    # Connect to database and retreieve data
    conn = sqlite3.connect(data_base)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS requests(id INTEGER, phone_number VARCHAR,
                lat VARCHAR,lng VARCHAR, perfomed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (id))''')
    cur.execute('''SELECT phone_number, lat, lng, MAX(perfomed_at)
                            FROM requests
                            GROUP BY phone_number''')
    values = cur.fetchall()

    # Clear all previously scheduled texts to avoid dupication
    schedule.clear()

    # Iterate over list returned by DB query
    for x in values:
        number = x[0]
        lat =x[1]
        lng = x[2]

        # Run calculation to get sunrise, noon, sunset, and lunar midnight times for individual
        resh_times = resh_calc(today, lat, lng)

        # Defining texts to be sent at sunrise, noon, sunset, and lunar midnight times
        def ra():
            textmyself('''Hail unto Thee who art Ra in Thy rising, even unto Thee who art Ra in Thy strength, who travellest over the Heavens in Thy bark at the Uprising of the Sun.

            Tahuti standeth in His splendour at the prow, and Ra-Hoor abideth at the helm.

            Hail unto Thee from the Abodes of Night!''', number)

        def ahathoor():
            textmyself('''Hail unto Thee who art Ahathoor in Thy triumphing, even unto Thee who art Ahathoor in Thy beauty, who travellest over the Heavens in thy bark at the Mid-course of the Sun.

            Tahuti standeth in His splendour at the prow, and Ra-Hoor abideth at the helm.

            Hail unto Thee from the Abodes of Morning!''', number)

        def tum():
            textmyself('''Hail unto Thee who art Tum in Thy setting, even unto Thee who art Tum in Thy joy, who travellest over the Heavens in Thy bark at the Down-going of the Sun.

            Tahuti standeth in His splendour at the prow, and Ra-Hoor abideth at the helm.

            Hail unto Thee from the Abodes of Day!''', number)

        def khephra():
            textmyself('''Hail unto thee who art Khephra in Thy hiding, even unto Thee who art Khephra in Thy silence, who travellest over the Heavens in Thy bark at the Midnight Hour of the Sun.

            Tahuti standeth in His splendour at the prow, and Ra-Hoor abideth at the helm.

            Hail unto Thee from the Abodes of Evening.''', number)

        # Schedule texts at sunrise, solar noon, sunset, and lunar midnight
        schedule.every().day.at(resh_times[0]).do(ra).tag('user-tasks')
        schedule.every().day.at(resh_times[1]).do(ahathoor).tag('user-tasks')
        schedule.every().day.at(resh_times[2]).do(tum).tag('user-tasks')
        #schedule.every().day.at(resh_times[3]).do(khephra).tag('user-tasks')

while True:
    schedule_texts()
    print('successful run')
    for num in range (0,43200):
        schedule.run_pending()
        time.sleep(1)
