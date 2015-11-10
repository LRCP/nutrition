from app import app

#the name of the filter is num_round
@app.template_filter('num_round')
#the name for the function is num_round_filter.
def num_round_filter(s, precision=2):
    if s is None or precision is None:
        return s
    elif precision == 0:
        return int(round(s, precision))
    else:
        return round(s, precision)