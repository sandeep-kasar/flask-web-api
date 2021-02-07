# mongo-engine packages
from mongoengine import (Document,
                         EmbeddedDocument,
                         EmbeddedDocumentField,
                         StringField,
                         EmailField,
                         BooleanField,
                         IntField,
                         DecimalField,
                         DateTimeField,
                         ReferenceField)
# other packages
import datetime


class Orders(Document):
    """
    Template for a mongoengine document, which represents a order.

    :param order_no: unique required for display purpose e.g ORD1001
    :param user_id: this is the user id from mongodb document
    :param meal_id: this is the meal id from mongodb document
    :param table_no: this is the table number for billing purpose like TBL10
    :param quantity: this is int value indicating meal item quantity
    :param bill: this is the decimal value indicating order bill
    :param order_date: date of order 
    :Example:

    >>> import mongoengine
    >>> from app import default_config

    >>> mongoengine.connect(**default_config['MONGODB_SETTINGS'])
    MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True, read_preference=Primary())

    # Create test order
    >>> new_order = orders(order_no="ORD1001","user_id"="601fafad3911530651fe822b",
                            "meal_id"="601fafad3911530651fe822b","table_no"="TBL10","quantity"="10",
                            "bill"="100.50","order_date"="2016-05-25T10=05:44Z")
    >>> new_order.save()
    >>> new_order.order_no = "ORD1001"
    >>> new_order.save()

    # Remove test order
    >>> new_order.delete()

    """

    order_no = StringField(required=True, regex=None)
    user_id = StringField(required=True, regex=None)
    meal_id = StringField(required=True, regex=None)
    table_no = StringField(required=True, regex=None)
    quantity = IntField(min_value=1, max_value=100, required=True)
    bill = DecimalField(min_value=10, max_value=10000, force_string=False, precision=2, rounding='ROUND_HALF_UP')
    order_date = DateTimeField(default=datetime.datetime.utcnow)