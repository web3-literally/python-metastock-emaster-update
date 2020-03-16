from BaseParser import BaseParser
import requests
import xlrd


class HKEXParser(BaseParser):

    def __init__(self, download_url):
        BaseParser.__init__(self, 'HKEX', download_url)

    def ParseMarket(self):
        BaseParser.ParseMarket(self)
        try:
            f = requests.get(self.download_url)
            workbook = xlrd.open_workbook(file_contents=f.content)
            worksheet = workbook.sheet_by_index(0)
            for row_idx in range(3, worksheet.nrows):
                row = worksheet.row(row_idx)
                market_symbol = {}
                market_symbol['code'] = row[0].value.strip() + '.HK'
                if market_symbol['code'][0] == '0':
                    market_symbol['code'] = market_symbol['code'][1:]
                market_symbol['name'] = row[1].value.strip()
                self.market_symbols.append(market_symbol)
        except Exception as e:
            print(e)

    def SaveStocks(self):
        BaseParser.SaveStocks(self)
        BaseParser.SaveEmaster(self)
