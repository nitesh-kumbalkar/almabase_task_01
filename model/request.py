from marshmallow import Schema, fields

class RequestSchema(Schema):

    """ /api/ - POST

    Parameters:
     - org (str)
     - n (int)
     - m (int)
    """

    org = fields.Str(required=True)  # OrgName
    n = fields.Int(required=True)    # no. of popular repo
    m = fields.Int(required=True)    # no. of top commit