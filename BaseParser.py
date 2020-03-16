from pathlib import Path
from metastock.files import MSEMasterFile


class BaseParser(object):
    market_symbols = []
    market_name = ''
    download_url = ''
    stock_base_path = 'C:\\inetpub\\ftproot\\Markets\\'
    # stock_base_path = 'f:\\task\\temp\\20200314-python-emaster\\temp\\stock\\'
    emaster_base_path = 'c:\\MetaStock Data\\'
    # emaster_base_path = 'f:\\task\\temp\\20200314-python-emaster\\temp\\emaster\\'

    def __init__(self, market_name, download_url):
        self.market_symbols = []
        self.market_name = market_name
        self.download_url = download_url

    def ParseMarket(self):
        print('Parsing market from url ' + self.download_url)

    def SaveStocks(self):
        try:
            store_path = self.stock_base_path + self.market_name + '\\Stocks\\'
            Path(store_path).mkdir(parents=True, exist_ok=True)
            with open(store_path + 'StockCode.txt', 'w') as file:
                for stock in self.market_symbols:
                    stock_code = stock['code']
                    stock_name = stock['name']
                    line = stock_code + '\t' + stock_name + '\n'
                    file.write(line)
        except Exception as e:
            print(e)

    def SaveEmaster(self):
        try:
            save_path = self.emaster_base_path + self.market_name + '\\'
            Path(save_path).mkdir(parents=True, exist_ok=True)
            save_path += 'EMASTER'
            emasterfile = MSEMasterFile('ascii')
            emasterfile.save_symbols(save_path, self.market_symbols)
        except Exception as e:
            print(e)