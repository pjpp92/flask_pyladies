from wtforms import Form, BooleanField, TextField, validators

class add_post(Form):
    author = TextField('Author', [validators.Length(min=1)])
    post = TextField('Post', [validators.Length(min=1)])
    title = TextField('Title', [validators.Length(min=1)])
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])

class add_comment(Form):
    comment = TextField('comment', [validators.Length(min=1, max=250)])
    accept_reg = BooleanField('I accept the reg')