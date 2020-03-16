from elasticsearch_dsl import Document, Date, Keyword, Text,Integer,Boolean,datetime,Object,AttrList
from discussionboard.settings import connections
connections=connections
import time

class discussion(Document):
    parent=Text()
    child = AttrList([])
    created_by=Text()
    created_time=Date()
    isChild=Boolean()
    likeCount =Integer()
    comment = Text()

    class Index:
        name = 'discussion_fourm'

    def save(self, **kwargs):
        if not self.parent : return None
        if not self.created_time: self.created_time = datetime.now()
        if not self.likeCount: self.likeCount = 0
        if not self.isChild: self.isChild = False
        if not self.created_by: self.created_by = "Admin"
        if not self.comment: self.comment = ""
        timestr = time.strftime("%Y%m%d-%H%M%S")
        discussionId = "DISS" + "-" + timestr
        self.meta.id = discussionId
        super(discussion, self).save(**kwargs)
        return self