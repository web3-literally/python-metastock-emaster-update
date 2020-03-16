from BaseParser import BaseParser
import codecs
import csv
import urllib.request


class ASXParser(BaseParser):

    def __init__(self, download_url):
        BaseParser.__init__(self, 'ASX', download_url)

    def ParseMarket(self):
        BaseParser.ParseMarket(self)
        try:
            f = urllib.request.urlopen(self.download_url)
            csvfile = csv.reader(codecs.iterdecode(f, 'utf-8'))
            is_header = True
            for line in csvfile:
                if not line or len(line) < 2:
                    continue

                if is_header:
                    is_header = False
                    continue

                market_symbol = {}
                market_symbol['code'] = line[1].strip() + '.AS'
                market_symbol['name'] = line[0].strip()
                self.market_symbols.append(market_symbol)

        except Exception as e:
            print(e)

    def SaveStocks(self):
        BaseParser.SaveStocks(self)
        BaseParser.SaveEmaster(self)
