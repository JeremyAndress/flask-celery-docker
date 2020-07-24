#EXAMPLES QUERY

def insert_notif(channel,number,date):
    return f"""INSERT INTO public.table
            (channel, number, date)
            VALUES('{channel}', '{number}', '{date}' );"""

