name_for_userid = {
	382: 'Alice',
	950: 'Bob',
	590: 'Dilbert',
}

def greeting(userid):
	return 'Hi %s!' % name_for_userid.get(userid, 'there')


print(greeting(382))
print(greeting(33333))