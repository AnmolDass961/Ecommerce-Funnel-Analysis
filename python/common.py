import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

db_path = os.environ.get("FUNNEL_DB", "funnel.db")

conn = sqlite3.connect(db_path)
sf = pd.read_sql("select * from session_funnel", conn, parse_dates=["session_date"])
events = pd.read_sql("select * from events_raw", conn, parse_dates=["event_time", "event_date"])

sf["purchase_strict"] = ((sf["has_purchase"] == 1) & (sf["has_cart"] == 1)).astype(int)
sf["month"] = sf["session_date"].dt.to_period("M").astype(str)
