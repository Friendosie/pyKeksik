from types import SimpleNamespace
import requests
import json

def sendRequestToApi(session, post_args, link):
    post_data = json.loads(session.post(link, headers={'Content-Type': 'application/json'}, json=post_args).text, object_hook=lambda d: SimpleNamespace(**d))
    
    if post_data.success:
        return post_data.list
    else:
        raise Exception(post_data.error, post_data.msg)

class KeksikApi:

    def __init__(self,
                group_id=None,
                token=None,
                v=1):
        # Обязательные обьекты
        self.group_id = abs(group_id)
        self.token = str(token)
        self.v = v
        # HTTP сессия
        self.Session = requests.Session()
        
        # Классы
        self.donates = self.donates(self.group_id, self.token, self.v, self.Session)
        self.campaigns = self.campaigns(self.group_id, self.token, self.v, self.Session)
        self.payments = self.payments(self.group_id, self.token, self.v, self.Session)
        
    class donates:

        def __init__(self,
                group_id=None,
                token=None,
                v=1,
                session=None):
            self.group_id = abs(group_id)
            self.token = str(token)
            self.v = v
            self.Session = session
            

        def get(self,
            length=20,
            offset=None,
            start_date=None,
            end_date=None,
            sort=None,
            reverse=None
            ):
            post_args = {
                'group':self.group_id,
                'token':self.token,
                'v':self.v,
                'len':length,
                'offset':offset,
                'start_date':start_date,
                'end_date':end_date,
                'sort':sort,
                'reverse':reverse
                }
            return sendRequestToApi(self.Session, post_args, 'https://api.keksik.io/donates/get')
        
        def getLast(self, last=None):
            post_args = {
                'group':self.group_id,
                'token':self.token,
                'v':self.v,
                'last':last
                }

            return sendRequestToApi(self.Session, post_args, 'https://api.keksik.io/donates/get-last')
        
        def changeStatus(self, id, status):
            post_args = {
                'group':self.group_id,
                'token':self.token,
                'v':self.v,
                'id':id,
                'status':status
                }

            return sendRequestToApi(self.Session, post_args, 'https://api.keksik.io/donates/change-status')
        
        def answer(self, id, answer):
            post_args = {
                'group':self.group_id,
                'token':self.token,
                'v':self.v,
                'id':id,
                'answer':answer
                }

            return sendRequestToApi(self.Session, post_args, 'https://api.keksik.io/donates/change-status')
        
        def changeRewardStatus(self, id, status):
            post_args = {
                'group':self.group_id,
                'token':self.token,
                'v':self.v,
                'id':id,
                'status':status
                }

            return sendRequestToApi(self.Session, post_args, 'https://api.keksik.io/donates/change-status')
    
    class campaigns:

        def __init__(self,
                group_id=None,
                token=None,
                v=1,
                session=None):
            self.group_id = abs(group_id)
            self.token = str(token)
            self.v = v
            self.Session = session
            
        
        def get(self, ids=None):
            post_args = {
                'group':self.group_id,
                'token':self.token,
                'v':self.v,
                'ids':ids
                }

            return sendRequestToApi(self.Session, post_args, 'https://api.keksik.io/campaigns/get')
        
        def getActive(self):
            post_args = {
                'group':self.group_id,
                'token':self.token,
                'v':self.v
                }

            return sendRequestToApi(self.Session, post_args, 'https://api.keksik.io/campaigns/get-active')
        
        def getRewards(self, campaign):
            post_args = {
                'group':self.group_id,
                'token':self.token,
                'v':self.v,
                'campaign':campaign
                }

            return sendRequestToApi(self.Session, post_args, 'https://api.keksik.io/campaigns/get-rewards')
        
        def change(self,
            id,
            title=None,
            status=None,
            end=None,
            point=None,
            start_received=None,
            start_backers=None
            ):
            post_args = {
                'group':self.group_id,
                'token':self.token,
                'v':self.v,
                'id':id,
                'title':title,
                'status':status,
                'end':end,
                'point':point,
                'start_received':start_received,
                'start_backers':start_backers
                }

            return sendRequestToApi(self.Session, post_args, 'https://api.keksik.io/campaigns/change')
        
        def changeReward(self,
            id,
            title=None,
            desc=None,
            min_donate=None,
            limits=None,
            status=None
            ):
            post_args = {
                'group':self.group_id,
                'token':self.token,
                'v':self.v,
                'id':id,
                'title':title,
                'desc':desc,
                'min_donate':min_donate,
                'limits':limits,
                'status':status
                }

            return sendRequestToApi(self.Session, post_args, 'https://api.keksik.io/campaigns/change-reward')
    
    class payments:

        def __init__(self,
                group_id=None,
                token=None,
                v=1,
                session=None):
            self.group_id = abs(group_id)
            self.token = str(token)
            self.v = v
            self.Session = session
            
        
        def get(self, ids=None):
            post_args = {
                'group':self.group_id,
                'token':self.token,
                'v':self.v,
                'ids':ids
                }

            return sendRequestToApi(self.Session, post_args, 'https://api.keksik.io/payments/get')
        
        def create(self, 
            system,
            purse,
            amount,
            name=None
            ):
            post_args = {
                'group':self.group_id,
                'token':self.token,
                'v':self.v,
                'system':system,
                'purse':purse,
                'name':name,
                'amount':amount
                }

            return sendRequestToApi(self.Session, post_args, 'https://api.keksik.io/payments/get')
    
    def balance(self, ):
        post_args = {
            'group':self.group_id,
            'token':self.token,
            'v':self.v,
            }

        return sendRequestToApi(self.Session, post_args, 'https://api.keksik.io/payments/get')