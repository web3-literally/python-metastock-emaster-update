from BaseParser import BaseParser
from AMEXParser import AMEXParser
from ASXParser import ASXParser
from HKEXParser import HKEXParser
from NASDParser import NASDParser
from NYSEParser import NYSEParser
from SGXParser import SGXParser
from metastock.files import MetastockFiles


def main():
    print("Stock Emaster Updater@V1.0.0")

    loadStocks()
    # loadEmaster()

def loadStocks():
    parsers = [BaseParser] * 6

    parsers[0] = NASDParser(
        'https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download')
    parsers[1] = ASXParser(
        'http://www.asx.com.au/asx/research/ASXListedCompanies.csv')
    parsers[2] = HKEXParser(
        'https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx')
    parsers[3] = AMEXParser(
        'https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=amex&render=download')
    parsers[4] = NYSEParser(
        'https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download')
    parsers[5] = SGXParser()

    for i in list(range(6)):
        parsers[i].ParseMarket()
        parsers[i].SaveStocks()

def loadEmaster():
    em_file = MetastockFiles("ascii")
    # list the symbols or extract the data
    em_file.list_all_symbols()

if __name__ == "__main__":
    main()

