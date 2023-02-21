from django.shortcuts import render
from django.http import HttpResponse
from unishk.utils import get_db_handle, get_collection_handle


def index(self):
    db_handle, mongo_client = get_db_handle()
    collection_handle = get_collection_handle(db_handle, "fakultetis")
    emertimi= collection_handle.find_one({"emertimi":"Fakulteti i Gjuheve te Huaja"})
    print (emertimi)
    
