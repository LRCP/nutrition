from app import app


@app.template_filter('num_round')
def num_round_filter(s, precision=1):
    if s == 'N/A':
        return s
    elif precision == 0:
        return int(round(s, precision))
    elif s == None:
        return ""
    else:
        return round(s, precision)

