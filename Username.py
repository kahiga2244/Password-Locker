class User:
    """
    class that generates new user
    """
    user_details = []

    def __init__(self, fname, sname, password):
        self.fname = fname
        self.sname = sname
        self.password = password
    # This saves a new user registration

    def save_user(self):

        """
        this save method adds and stores our user
        """
        User.user_details.append(self)

    # deleting the user account

    def delete_account(self):
        """
        delete account method to remove user account
        """
        User.user_details.remove(self)

    # finding user by first_name
    @classmethod
    def find_by_fname(cls, fname):
        """
        find user by their first name
        Args:
            fname: first name of the user to search for
        returns:
            user searched for
        """
        for user in cls.user_details:
            if user.fname == fname:
                return user

    # confirm user exist
    @classmethod
    def user_exist(cls, fname):
        """
        method that checks if the user exists by name
        Args:
        first_name checks if the name exists
        returns a boolean depending if the name exists
        """
        for user in cls.user_details:
            if user.fname == fname:
                return True
        return False
    # display user
    @classmethod
    def display_user(cls):
        """
        Function that displays users 
        """

        return cls.user_details()