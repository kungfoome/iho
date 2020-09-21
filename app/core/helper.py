from datetime import datetime, timedelta


def get_ofxdatetime():
    return (datetime.today() - timedelta(days=1)).strftime("%Y%m%d")
