name_for_userid = {
	382: 'Alice',
	950: 'Bob',
	590: 'Dilbert',
}

def greeting(userid):
	try:
		return 'Hi %s!' % name_for_userid[userid]
	except KeyError:
		return 'Hi there!'


print(greeting(382))
print(greeting(33333))