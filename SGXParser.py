from BaseParser import BaseParser
import codecs
import csv
import datetime
import re
import urllib.parse
import urllib.request


class SGXParser(BaseParser):

    def __init__(self):
        BaseParser.__init__(self, 'SGX', self.GenerateUrl())

    def GenerateUrl(self):
        dt = datetime.datetime.now()
        url = 'https://links.sgx.com/FileOpen/%d%s%s%s%d.ashx?App=ISINCode&FileID=1' \
              % (dt.day, '%20', dt.strftime("%b"), '%20', dt.year)
        return url
        # return urllib.parse.quote(url)

    def ParseMarket(self):
        BaseParser.ParseMarket(self)
        try:
            f = urllib.request.urlopen(self.download_url)
            csvfile = csv.reader(codecs.iterdecode(f, 'utf-8'))
            is_header = True
            for line in csvfile:
                if not line or len(line) == 0:
                    continue

                if is_header:
                    is_header = False
                    continue

                market_symbol = {}
                market_symbol['code'] = line[0][80:90].strip()
                market_symbol['name'] = line[0][90:].strip()
                self.market_symbols.append(market_symbol)

        except Exception as e:
            print(e)
