import pandas as pd
from mongoengine import Document, StringField, FileField, DictField

from io import BytesIO


def store(name, object, metadata=None):
    Frame.objects(name=name).update_one(name=name, metadata=metadata, upsert=True)
    return Frame.objects(name=name).first().put(frame=object)


def load(name):
    f = Frame.objects(name=name).first()
    assert f, "The frame object {name} does not exist".format(name=name)
    return f


# I would love to hide this class better
class Frame(Document):
    name = StringField(required=True, max_length=200, unique=True)
    data = FileField()
    metadata = DictField(default={})

    @property
    def frame(self):
        str_data = BytesIO(self.data.read()).read().decode()

        try:
            return pd.read_json(str_data, typ="frame", orient="split")
        except ValueError:
            return pd.read_json(str_data, typ="series", orient="split")

    def __str__(self):
        return "{name}: \n{frame}".format(name=self.name, frame=self.frame)

    def put(self, frame):
        if self.data:
            self.data.replace(frame.to_json(orient="split").encode())
        else:
            self.data.new_file()
            self.data.write(frame.to_json(orient="split").encode())
            self.data.close()

        self.save()
        return self.reload()