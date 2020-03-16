from discussionapp.elasticmodel import discussion
class Discussion:
    data = None
    def __init__(self, data=None):
        self.data = data

    def create_discussion(self):
        if self.data['parent']:
            try:
                diss = discussion(parent=self.data['parent'],comment=self.data['comment'],created_by=self.data['user'],timeout=30).save()
                childId = diss.meta.id
                # parent = discussion.get(id = self.data['parent'])
                # childList = parent.child
                # childList.append(childId)
                # parent.child = childList
                # parent.update()
                return {"Status": True, "Msg": childId+" successfully created "}
            except Exception as e:
                return {"Status": False, "Msg": str(e)}

        else:
            return {"Status":False,"Msg":"Parent is missing!"}


