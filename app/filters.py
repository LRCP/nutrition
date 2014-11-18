from app import app


@app.template_filter('num_round')
def num_round_filter(s, precision=2):
    if s == 'N/A':
        return s
    elif precision == 0:
        return int(round(s, precision))
    else:
        return round(s, precision)

