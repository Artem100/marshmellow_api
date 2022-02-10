from marshmallow import Schema, fields


class PostsSchema(Schema):
    title = fields.Str(required=True)
    body = fields.Str(allow_none=True)
    userId = fields.Int(required=True)