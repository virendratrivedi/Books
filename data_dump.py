import pymongo
import pandas as pd
import json

#print(pd.__version__)

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb+srv://arpit_t:12345@cluster0.ekedees.mongodb.net/?retryWrites=true&w=majority")
db = client.test
#DATA_FILE_PATH = "/config/workspace/books.csv"
DATABASE_NAME = "mylib"
BOOK_DATA_FILE_PATH ='D:\\ML\\vscode\\Books\\books.csv'
USER_DATA_FILE_PATH ='D:\\ML\\vscode\\Books\\users.csv'
RATING_DATA_FILE_PATH ='D:\\ML\\vscode\\Books\\ratings.csv'

COLLECTION_NAME_BOOKS = "books"
COLLECTION_NAME_USERS = "users"
COLLECTION_NAME_RATINGS = "ratings"


if __name__=="__main__":

    books_df = pd.read_csv(BOOK_DATA_FILE_PATH,low_memory=False)
    users_df = pd.read_csv(USER_DATA_FILE_PATH,low_memory=False)
    ratings_df = pd.read_csv(RATING_DATA_FILE_PATH,low_memory=False)

    
    books_df.reset_index(drop=True,inplace=True)
    users_df.reset_index(drop=True,inplace=True)
    ratings_df.reset_index(drop=True,inplace=True)

    json_record_books = list(json.loads(books_df.T.to_json()).values())
    json_record_users = list(json.loads(users_df.T.to_json()).values())
    json_record_ratings = list(json.loads(ratings_df.T.to_json()).values())

    #print(json_record[0:2])
    client[DATABASE_NAME][COLLECTION_NAME_BOOKS].insert_many(json_record_books) 
    client[DATABASE_NAME][COLLECTION_NAME_USERS].insert_many(json_record_users) 
    client[DATABASE_NAME][COLLECTION_NAME_RATINGS].insert_many(json_record_ratings) 

    print(f"books rows and column: {books_df.shape}")
    print(f"users rows and column: {users_df.shape}")
    print(f"ratings rows and column: {ratings_df.shape}")




    '''
    df = pd.read_csv(DATA_FILE_PATH,low_memory=False)
    print(f"rows and column: {df.shape}")
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    #print(json_record[0:2])
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record) '''