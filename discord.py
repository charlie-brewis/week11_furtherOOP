class User:

    def __init__(self, user_id: str, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.recieved_messages = []
        self.pinned_messages = []

    def recieve_message(self, message, sender_id):
        self.recieved_messages.append([sender_id, message])

    def send_message(self, message, recipient):
        recipient.recieve_message(message, self.user_id)
    
    def pin_message(self, message_index):
        self.pinned_messages.append(self.recieved_messages[message_index])
    
    def view_messages(self):
        print("")
        # Remove the pinned messages from recieved messages so theyre not displayed twice
        remove_pinned = self.recieved_messages
        if len(self.pinned_messages) > 0:
            for message in self.pinned_messages:
                remove_pinned.remove(message)

            print("Pinned messages:")
            for sender_id, message_content in self.pinned_messages:
                print(f"Message: {message_content}, recieved from user: {sender_id}")
        
        print("Recieved messages:")
        for sender_id, message_content in remove_pinned:
            print(f"Message: {message_content}, recieved from user: {sender_id}")


class Nitro_user(User):
    def __init__(self, user_id: str, user_name):
        super().__init__(user_id, user_name)


class Verified_user(User):
    def __init__(self, user_id: str, user_name):
        super().__init__(user_id, user_name)

    def send_message(self, message, recipient):
        if len(message) <= 100:
            super().send_message(message, recipient)
        else:
            print("Error: Verified Users cannot send messages over 100 characters. Consider upgrading to Nitro for this functionality.")
    
    def pin_message(self, message_index):
        print("Error: Only Nitro Users can pin messages.")


# I know this is technically wrong but it works and seemed fun to try - reduces code repition too i guess
class Unverified_user(Verified_user):
    def __init__(self, user_id: str, user_name):
        super().__init__(user_id, user_name)

    def send_message(self, message, recipient):
        print("Error: Unverified Users cannot send messages. Consider upgrading to Verified or Nitro for this functionality.")
    

def test_users():
    unverified_user = Unverified_user('a', 'uua')
    verified_user = Verified_user('b', 'vub')
    nitro_user = Nitro_user('c', 'nuc')

    unverified_user.send_message("Hello vub", verified_user)
    verified_user.send_message("I didnt quite get that uua", unverified_user)
    unverified_user.view_messages()
    nitro_user.send_message("It's because he's unverified", verified_user)
    verified_user.send_message("WHAT A LOSER!", nitro_user)
    nitro_user.pin_message(-1)
    nitro_user.send_message("IKR", verified_user)
    verified_user.pin_message(-1)
    nitro_user.send_message("YOU'RE A LOSER TOO", verified_user)
    verified_user.view_messages()
    verified_user.send_message("Thats mean", nitro_user)
    nitro_user.view_messages()


test_users()