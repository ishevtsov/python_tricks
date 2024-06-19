class NameTooShortError(ValueError):
	pass

def validate(name):
	if len(name) < 10:
		raise NameTooShortError(f'len({name}) must be >= 10 char')

validate('Joe')