import json
import xml.etree.ElementTree as ET
from types import SimpleNamespace

import abc


class BaseProcessor(object):

    def __init__(self) -> None:
        self.filename = None
        self.data = {}

    @abc.abstractmethod
    def loadFile(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def loadData(self):
        raise NotImplementedError()

    @property
    def get_data(self):
        return self.data

    def isValid(self) -> bool:
        if not self.data:
            try:
                raise ValueError
            except ValueError:
                print('\n>> >> ERROR: Data Empty << <<')
            exit()

        net_sales_money = int(self.data.itemization[0].net_sales_money.amount)
        tax_money = int(self.data.tax_money.amount)
        total_payed = int(self.data.tender.total_money.amount)
        return total_payed == (net_sales_money + tax_money)


class XMLProcessor(BaseProcessor):

    def __init__(self, filename) -> None:
        super().__init__()
        self.filename = filename
        self.root = None

    def processXML(self):
        self.loadFile()
        self.loadData()

    def loadFile(self):
        tree = ET.parse(self.filename)
        self.set_root(tree.getroot())

    def loadData(self):
        root = self.get_root()
        self.data = self.get_element_data(root[:])

    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root

    def get_element_data(self, elemArr):
        data = {}
        for elemnt in elemArr:
            if len(elemnt) > 0:
                if "element" == elemnt[0].tag:
                    elements = []
                    for e in elemnt[:]:
                        elements.append(self.get_element_data(e[:]))
                    data[elemnt.tag] = elements
                else:
                    data[elemnt.tag] = self.get_element_data(elemnt[:])
            else:
                data[elemnt.tag] = elemnt.text
        data = SimpleNamespace(**data)
        return data


class JSONProcessor(BaseProcessor):

    def __init__(self, filename) -> None:
        super().__init__()
        self.filename = filename

    def loadFile(self):
        with open(self.filename) as f:
            self.data = json.load(f, object_hook=lambda d: SimpleNamespace(**d))

    def processJSON(self):
        self.loadFile()
