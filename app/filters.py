from app import app


@app.template_filter('num_round')
def num_round_filter(s):
    if s == 'N/A':
        return s
    else:
        return round(s, 2)