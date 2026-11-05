import pandas as pd, sqlite3

con = sqlite3.connect("funnel.db")

events = pd.read_csv("data/events.csv", parse_dates=["event_time", "event_date"])
sessions = pd.read_csv("data/sessions.csv", parse_dates=["session_start", "session_date"])
products = pd.read_csv("data/products.csv")

events.to_sql("events_raw", con, if_exists="replace", index=False)
sessions.to_sql("sessions_raw", con, if_exists="replace", index=False)
products.to_sql("products", con, if_exists="replace", index=False)

con.execute("CREATE INDEX idx_ev_session ON events_raw(session_id)")
con.execute("CREATE INDEX idx_ev_type ON events_raw(event_type)")
con.close()