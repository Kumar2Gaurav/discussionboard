from channels.generic.websocket import WebsocketConsumer
import json
import time
import pandas as pd
from collections import Counter
class ChatConsumer(WebsocketConsumer):
    def connect(self):

        self.accept()
        
        while True:
            
            result=[]
            df=pd.read_csv("/usr/local/liquid_developement/catsmagroo_v3/cluster_level_two.csv")
            situation_list,tech_list=[],[]
            [situation_list.append(x) if x not in situation_list else '' for x in df['situation_id']]
            for index,situation in enumerate(situation_list):
                most_common_1, num_most_common_1 = Counter(df[df['situation_id']==situation]['tech']).most_common(1)[0]
                result.append({'situation_id':situation,'situation_name':most_common_1})
            self.send(text_data=json.dumps({
                'data': result
            }))
            time.sleep(30)


    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print("message recevied",message)
        # i =0
        # while i< 5:
        #     i+=1
        self.send(text_data=json.dumps({
            'message': 'this is so cool'
        }))
            # time.sleep(10)
