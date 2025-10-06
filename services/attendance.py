def auto_close_out(sessions, shift_end_hour):
    # If last session has no OUT after shift_end, close it
    for sess in sessions:
        if sess["out_time"] is None and sess["in_time"].hour < shift_end_hour:
            sess["out_time"] = sess["in_time"].replace(hour=shift_end_hour, minute=0, second=0)
            sess["duration"] = sess["out_time"] - sess["in_time"]
    return sessions