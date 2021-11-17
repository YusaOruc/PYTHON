from MessageBot import MessageUser

obj=MessageUser()
print(obj.add_user("Justin",152,"hello@gmail.com"))
print(obj.add_user("Tom",458))
print(obj.get_details())
print(obj.make_messages())