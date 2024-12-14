from invoice import Invoice
from invoice.table_classifier import *
from models_ import table_classification_model


def Invoice_(image):
    inv = Invoice(image)
    data = inv.data_json()
    table = inv.to_json()

    return table, data


