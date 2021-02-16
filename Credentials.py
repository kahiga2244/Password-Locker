import random
import string

class Credentials:
    '''
    class that generates instances of new credentials
    '''
    app_details = []
    
    def __init__(self,app,app_password):
        self.app = app
        self.app_password = app_password
    
    def save_app(self):
        '''
        function that stores our accounts
        '''
        Credentials.app_details.append(self)
    def delete_app(self):
        '''
        Function that remove app and password
        '''
        Credentials.app_details.remove(self)
    
    @classmethod
    def find_app(cls,app):
        '''
        Finding app by the name
        Args:
            app: app name to search for
        returns:
            app searched for
        '''
        for credentials in cls.app_details:
            if credentials.app == app:
                return app
    
    @classmethod
    def app_exist(cls,app):
        '''
        Method that checks if app exist
        Args:
            app name to check if app exist
        Returns:
            a boolean depending on the app checked for
        '''
        for credentials in cls.app_details:
            if credentials.app == app:
                return True
        return False

    @classmethod
    def gen_password(self):
        '''
        Function to generate random password with six digits
        '''
        char = string.ascii_uppercase + string.ascii_lowercase
        gen_password = ''.join(random.choice(char) for i in range(0, 9))
        return gen_password

    @classmethod
    def display_app(cls, app):
        '''
        Function that displays app
        '''    
        
        return cls.app_details()