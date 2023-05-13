from pymongo import MongoClient

mongo = MongoClient('mongodb+srv://shivanisangale8:s6buFluinl2PUP5h@cluster0.yjhsqfu.mongodb.net/?retryWrites=true&w=majority') #need mongo uri from atlan mongo
db = mongo.users


class StoreOnCloud():

    """
    Class StoreOnCloud()
        A class for storing user credentials in a cloud-based MongoDB database.

        Attributes:
        -----------
        None

        Methods:
        --------
        retrieve_user(username: str) -> tuple(dict, bool):
            Retrieves the user credentials associated with the given username from the database.

        insert_user(username: str, password: str) -> tuple(dict, bool):
            Inserts a new user with the given username and password into the database.

        update_user(username: str, password: str) -> tuple(dict, bool):
            Updates the user credentials associated with the given username in the database.

        delete_user(username: str) -> tuple(dict, bool):
            Deletes the user with the given username from the database.
    """
    
    def retrieve_user(self, email: str, password: str) -> tuple :
        try:
            result = False
            data = db.details.find_one({'email': email, 'password': password })
            if data:
                result = True
                output = "User is valid!"
            else:
                output = "User not found!"
        except Exception as e:
            output = f"Some error has occurred: {e}"
        return {'status':str(result), 'result': output }, result


    def insert_user(self, username: str, password: str, firstName: str, lastName: str, email: str) -> tuple :
        try:
            result = False
            data = db.details.find_one({'username': username })
            if data:
                output = "User already exists."
            else:
                datatoput = {}
                if firstName:
                    datatoput.update({'firstName': firstName })
                if lastName:
                    datatoput.update({'lastName': lastName })
                if username:
                    datatoput.update({'username': username })
                if email:
                    datatoput.update({'email': email })
                if password:
                    datatoput.update({'password': password })
                db.details.insert_one(datatoput)
                output = "User registered successfully."
                result = True
        except Exception as e:
            output = f"Some error has occurred: {e}"
        return {'registered':str(result), 'result': output }, result


    def update_user(self, username: str, password: str) -> tuple :
        try:
            result = False
            data = db.details.find_one({'username': username })
            if data:
                update_dict = {}
                if username is not None:
                    update_dict['username'] = data.get('username', []) + username
                if password is not None:
                    update_dict['actor'] = data.get('password', []) + password

                if update_dict:
                    db.details.update_one(
                        {'username': username },
                        {'$set': update_dict }
                    )
                    output = "Profile updated successfully"
                    result = True
                else:
                    output = "No fields provided for update"
            else:
                output = "User not found!"
        except Exception as e:
            output = f"Some error has occurred: {e}"
        return {'result': output }, result


    def delete_user(self, username: str) -> tuple :
        try:
            result = False
            data = db.details.find_one({'username': username })
            if data:
                db.details.delete_one({'username': username })
                output = "User deleted successfully"
                result = True
            else:
                output = "User not found!"
        except Exception as e:
            output = f"Some error has occurred: {e}"
        return {'result': output }, result
