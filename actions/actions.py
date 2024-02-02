from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from typing import Any, Text, Dict, List, Union, Optional

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType, FollowupAction


import requests
import json


required_slots_list = ["form_data"]
#
# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

global visited_video
visited_video = 0


required_slots_list_data = [
    "rpainfo"
]

cmc_url = "https://cmc.omfysgroup.com/"


class ValidateGetdataForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_getdata_form"

    def validate_rpainfo(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> Optional[Text]:

        current_intent = tracker.latest_message['intent'].get('name')
        current_slot = tracker.get_slot("rpainfo")
        print('current intent is ',
              tracker.latest_message['intent'].get('name'))
        print("rpainfo is =====>>> ",current_slot)
        print('value is', value)

        if value == "1" or current_slot == "oia_info":
            response_doc = requests.get(
                '{}/api/answer?question=oia'.format(cmc_url))
            response_doc1 = response_doc.json()
            print("new resp", response_doc1["answer"])
            if ((response_doc1["answer"]) == None):
                print("In the if statement of oia soln")
                dispatcher.utter_message(response="utter_oia_info")
                #dispatcher.utter_message(text="Hello World! Rajendra")
                return {"rpainfo": "1"}
            else:
                print("In the else statement of oia soln")
                dispatcher.utter_message(response_doc1["answer"])
                return {"rpainfo": "1"}
        elif value == "2" or current_slot == "chatbot_info":
            response_doc = requests.get(
                '{}/api/answer?question=chatbot'.format(cmc_url))
            response_doc1 = response_doc.json()
            print("new resp", response_doc1["answer"])
            if ((response_doc1["answer"]) == None):
                dispatcher.utter_message(response="utter_chatbot_info")
                return {"rpainfo": "2"}
            else:
                dispatcher.utter_message(response_doc1["answer"])
                return {"rpainfo": "2"}
        elif value == "3" or current_slot == "rpa_info":
            # response_doc = requests.get(
            #     '{}/api/answer?question=rpa'.format(cmc_url))
            # response_doc1 = response_doc.json()
            # print("new resp", response_doc1["answer"])
            # dispatcher.utter_message(response_doc1["answer"])
            print("<===IN RPA===>")
            dispatcher.utter_message(response="utter_rpa_info")
            return {"rpainfo": "3"}

        elif value == "4" or current_slot == "bsat_info":
            response_doc = requests.get(
                '{}/api/answer?question=bpm'.format(cmc_url))
            response_doc1 = response_doc.json()
            print("new resp", response_doc1["answer"])
            if ((response_doc1["answer"]) == None):
                dispatcher.utter_message(response="utter_bsat_info")
                return {"rpainfo": "4"}
            else:
                dispatcher.utter_message(response_doc1["answer"])
                return {"rpainfo": "4"}
        elif value == "5" or current_slot == "eai_info":
            response_doc = requests.get(
                '{}/api/answer?question=eai'.format(cmc_url))
            response_doc1 = response_doc.json()
            print("new resp", response_doc1["answer"])
            if ((response_doc1["answer"]) == None):
                dispatcher.utter_message(response="utter_eai_info")
                return {"rpainfo": "5"}
            else:
                dispatcher.utter_message(response_doc1["answer"])
                return {"rpainfo": "5"}
        elif value == "6" or current_slot == "mla_info":
            response_doc = requests.get(
                '{}/api/answer?question=mla'.format(cmc_url))
            response_doc1 = response_doc.json()
            print("new resp", response_doc1["answer"])
            if ((response_doc1["answer"]) == None):
                dispatcher.utter_message(response="utter_mla_info")
                return {"rpainfo": "6"}
            else:
                dispatcher.utter_message(response_doc1["answer"])
                return {"rpainfo": "6"}
        # elif value == "7" or current_slot == "opa_info":
        #     response_doc = requests.get(
        #         '{}/api/answer?question=opa'.format(cmc_url))
        #     response_doc1 = response_doc.json()
        #     print("new resp", response_doc1["answer"])
        #     dispatcher.utter_message(response_doc1["answer"])
        #     return {"rpainfo": "7"}
        # elif value == "8" or current_slot == "mobility_info":
        #     dispatcher.utter_message(template="utter_mobility_info")
        #     return {"rpainfo": "8"}

        return []




class ActionIndusInfo(Action):

    def name(self) -> Text:
        return "action_indus_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        current_intent = tracker.latest_message['intent'].get('name')
        current_slot = tracker.get_slot("ind_info")
        print('current intent is ',
              tracker.latest_message['intent'].get('name'))
        print("ind_info is =====>>> ",current_slot)

        if current_slot == "bfsi_info":
            print("<===IN bsfi===>")
            dispatcher.utter_message(response="utter_bsfi_info")
            
        elif current_slot == "mfcr_info":
            print("<===IN mfcr===>")
            dispatcher.utter_message(response="utter_mfcr_info")
            
        elif current_slot == "hlth_info":
            print("<===IN hlth===>")
            dispatcher.utter_message(response="utter_hlth_info")
            
        elif current_slot == "scmd_info":
            print("<===IN scmd===>")
            dispatcher.utter_message(response="utter_scmd_info")

        return []


class ActionHome(Action):

    def name(self) -> Text:
        return "action_home"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        # buttons = []
        # buttons.append({"title": "Home", "payload": "/home_path"})
        # msgStr = "Thank you"
        # dispatcher.utter_message(text=msgStr,buttons=buttons)
        dispatcher.utter_message(buttons=[{"payload": "/home_path", "title": "Home"}])
        return [SlotSet('rpainfo', None)]


class ActionAboutOmfys(Action):

    def name(self) -> Text:
        return "action_about_omfys"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # msgStr1 = "<ol><li><p style='font-size:12px'>OMFYS is one stop solutions handling the entire stack for AI transformation with specialisation on all the necessary solutions for transforming enterprise business processes smarter and AI driven.</li><li><p style='font-size:12px'>Pioneer in Oracle Digital Assistant platform implementation.</li><li><p style='font-size:12px'>Pioneer in Oracle Analytic Cloud and Autonomous Data Warehousing.</li><li><p style='font-size:12px'>Preferred Partner with Oracle Corporation and Strategic partner with Automation Anywhere Inc.</li><li><p style='font-size:12px'>Practice wise/Technology wise CoE in order to ensure seamless project execution and scalability.</li></ol>"
        msgStr1= "<b>1.</b> OMFYS is one stop solutions handling the entire stack for AI transformation with specialisation on all the necessary solutions for transforming enterprise business processes smarter and AI driven.<br> <b>2.</b> Pioneer in Oracle Digital Assistant platform implementation.<br> <b>3.</b> Pioneer in Oracle Analytic Cloud and Autonomous Data Warehousing.<br> <b>4.</b> Preferred Partner with Oracle Corporation and Strategic partner with Automation Anywhere Inc.<br> <b>5.</b> Practice wise/Technology wise CoE in order to ensure seamless project execution and scalability.<br>"
        dispatcher.utter_message(text=msgStr1)
        # list_details = []
        
        # list_details.append({
        #                     "type": "numbered_list",
        #                     "title": "About OMFYS",
        #                     "strings":
        #                                 [
        #                                     {
        #                                         "title": "OMFYS is one stop solutions handling the entire stack for AI transformation with specialisation on all the necessary solutions for transforming enterprise business processes smarter and AI driven."
                	
		# 									},
		# 									{
        #                                         "title": "Pioneer in Oracle Digital Assistant platform implementation."
												
		# 									},
        #                                     {
        #                                         "title": "Pioneer in Oracle Analytic Cloud and Autonomous Data Warehousing."
												
		# 									},
		# 									{
        #                                         "title": "Preferred Partner with Oracle Corporation and Strategic partner with Automation Anywhere Inc."
												
		# 									},
		# 									{
        #                                         "title": "Practice wise/Technology wise CoE in order to ensure seamless project execution and scalability."
												
		# 									}
        #                                     ]

        #                             })
        # dispatcher.utter_custom_json(gift_details)
        

        return []


class ActionCustomPayloadOne(Action):

    def name(self) -> Text:
        return "action_custom_payload_one"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        current_intent=tracker.latest_message['intent'].get('name')
        print("Contact_info intent=====>>>",current_intent)
        loc=[]

        if (current_intent == "contact_info"):
            print("in the contact_info action")
            loc.append({
                "type": "Iframe_location",
                "level": "second_level",
                "title": "I can show you below locations:",
                "videos": [
                    {
                        "payload": "current loc",
                        "link_href": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d15123.743045987496!2d73.8368797!3d18.6219589!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xfe5e94d999115e51!2sOMFYS%20Technologies%20India%20Pvt%20Ltd!5e0!3m2!1sen!2sin!4v1584178633182!5m2!1sen!2sin"
                    }
                ]
                })
            print("Inside custom action payload")
            # dispatcher.utter_custom_json(loc)
            dispatcher.utter_message(json_message=loc)

        elif (current_intent == "omfys_head"):
            print("in the omfys_head action")

            loc.append({
                "type": "Iframe_location",
                "level": "second_level",
                "title": "I can show you below locations:",
                "videos": [
                    {
                        "payload": "head loc",
                        "link_href": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d2489.9905460432815!2d-0.1237577!3d51.3848518!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x48760720afec118b%3A0xf22445bba34566a6!2sOMFYS!5e0!3m2!1sen!2sin!4v1585131287922!5m2!1sen!2sin"
                    }
                ]
                })
            print("Inside custom action payload")
            # dispatcher.utter_custom_json(loc)
            dispatcher.utter_message(json_message=loc)


        return []

class ActionCustomPayloadTwo(Action):

    def name(self) -> Text:
        return "action_custom_payload_two"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        current_intent_one = tracker.latest_message['intent'].get('name')

        global video_type
        video_type=""
        if current_intent_one =='rpa_demo':
            video_type = 'rpa'
        elif current_intent_one =='chatbot_demo':
            video_type = 'chatbot'
        elif current_intent_one =='opa_demo':
            video_type = 'opa'
        # video_type = 'rpa'
        if video_type:
            print("video type===>>>",video_type)
            response = requests.get('{}/api/listbycateory?contentCategory={}&contentType=video'.format(cmc_url,video_type))
            print("url for video", video_type)
            print(response)
            resp = response.json()
            video_type = ""
            gt=[]
            abc = len(resp)
            print("len of resp of list", abc)

            if (abc == 0):
                dispatcher.utter_message(template="utter_no_records")
                dispatcher.utter_template("utter_more",tracker)

            else :
                print("insidevideo calling")

                gt.append({
                    "type" : "Iframe_videos",
                    "level" : "second_level",
                    "title" : "I can show you below demos:",
                    "videos" : resp
                })
            
                dispatcher.utter_message(json_message=gt)
                # dispatcher.utter_template("utter_more",tracker)
        else:
            print("video type is not present")
            return[]

        # filtered_list = [ item for item in resp if item["contentType"] == "Video"]

        return []

class ActionCustomPayloadRpa(Action):

    def name(self) -> Text:
        return "action_custom_payload_rpa"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("Inside custom action rpa")

        # response_doc = requests.get('{}/api/answer?question=rpa'.format(cmc_url))

        # response_doc1 = response_doc.json()  

        # print("new resp",response_doc1["answer"])

        # dispatcher.utter_message(response_doc1["answer"])
        dispatcher.utter_message(response="utter_rpa_info")

        return []

class ActionCustomPayloadoia(Action):
    
    def name(self) -> Text:
        return "action_custom_payload_oia"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("Inside custom action opa")
        
        response_doc = requests.get('{}/api/answer?question=oia'.format(cmc_url))

        response_doc1 = response_doc.json()  

        print("new resp",response_doc1["answer"])

        dispatcher.utter_message(response_doc1["answer"])

        return []

class ActionCustomPayloadopa(Action):

    def name(self) -> Text:
        return "action_custom_payload_opa"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("Inside custom action opa")
        
        response_doc = requests.get('{}/api/answer?question=oia'.format(cmc_url))

        response_doc1 = response_doc.json()  

        print("new resp",response_doc1["answer"])

        dispatcher.utter_message(response_doc1["answer"])

        return []

class ActionCustomPayloadChatbot(Action):

    def name(self) -> Text:
        return "action_custom_payload_chatbot"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("Inside custom action opa")
        
        response_doc = requests.get('{}/api/answer?question=chatbot'.format(cmc_url))

        response_doc1 = response_doc.json()  

        print("new resp",response_doc1["answer"])

        dispatcher.utter_message(response_doc1["answer"])

        return []

class ActionCustomPayloadBsat(Action):

    def name(self) -> Text:
        return "action_custom_payload_bsat"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("Inside custom action opa")
        
        response_doc = requests.get('{}/api/answer?question=bsat'.format(cmc_url))

        response_doc1 = response_doc.json()  

        print("new resp",response_doc1["answer"])

        dispatcher.utter_message(response_doc1["answer"])

        return []

class ActionCustomPayloadBPM(Action):
    
    def name(self) -> Text:
        return "action_custom_payload_bpm"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("Inside custom action opa")
        
        response_doc = requests.get('{}/api/answer?question=bpm'.format(cmc_url))

        response_doc1 = response_doc.json()  

        print("new resp",response_doc1["answer"])

        dispatcher.utter_message(response_doc1["answer"])

        return []

class ActionCustomPayloadMla(Action):

    def name(self) -> Text:
        return "action_custom_payload_mla"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("Inside custom action opa")
        
        response_doc = requests.get('{}/api/answer?question=mla'.format(cmc_url))

        response_doc1 = response_doc.json()  

        print("new resp",response_doc1["answer"])

        dispatcher.utter_message(response_doc1["answer"])

        return []

class ActionCustomPayloadEai(Action):

    def name(self) -> Text:
        return "action_custom_payload_eai"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("Inside custom action opa")
        
        response_doc = requests.get('{}/api/answer?question=eai'.format(cmc_url))

        response_doc1 = response_doc.json()  

        print("new resp",response_doc1["answer"])

        dispatcher.utter_message(response_doc1["answer"])

        return []


class ActionCustomPayloadForm(Action):

    def name(self) -> Text:
        return "action_comment_form_filling"                     #------action_custom_payload_form-----#

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        global visited_video
        forms=[]
        if visited_video == 1:
            print("already visited to form")
            return[FollowupAction("action_custom_payload_two")]#----demo video-----#
        else:
            visited_video = 1
            ft=[]

            ft.append({
                 "type": "Iframe_form",
                 "level": "second_level",
                 "title": "I can show you below demos:",    #---------details form in JS---------------#
                 "Form":  "form"
            })
            # dispatcher.utter_message(json_message=forms)
            dispatcher.utter_message(json_message=ft)

        return []


# class ValidateCommentForm(FormValidationAction):

#     def name(self):
#         return "validate_comment_form"
        
#     async def required_slots(
#         self,
#         slots_mapped_in_domain: List[Text],
#         dispatcher: "CollectingDispatcher",
#         tracker: "Tracker",
#         domain: "DomainDict",
#         ) -> Optional[List[Text]]:

#         print("Inside required slot of apply leave form")
        
#         global required_slots_list
#         return required_slots_list


#     def validate_form_data(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker,
#                             domain: Dict[Text, Any]) -> Optional[Text]:

        
#         print('value of comment data ', value)

#         current_intent = tracker.latest_message['intent'].get('name')
#         print('current intent is ', tracker.latest_message['intent'].get('name'))

#         global wrong_attempt

#         if current_intent == 'stop':
#             global required_slots_list
#             required_slots_list = []
#             return []

#         try:

#             global form_data
#             form_data = tracker.latest_message['text'].split('|')
#             print(form_data)
#             print("lenth of form_data:---",form_data)


#             SlotSet('name',form_data[0])
#             SlotSet('emailId',form_data[1])
#             SlotSet('mobileNumber', form_data[2])
#             SlotSet('comment', form_data[3])
#             print("Inside form data",tracker.get_slot('name'), tracker.get_slot('emailId'))

#             return {'form_data':value}
#                 # return [SlotSet('form_data',form_data),SlotSet('start_date',form_data[0]),SlotSet('end_date',form_data[1]),SlotSet('leave_type', form_data[2]),SlotSet('purpose', form_data[3]),SlotSet('hand_over_Employee', form_data[4]),SlotSet('knowledge_summary',form_data[5])]

#         except:
#                 required_slots_list = []
#                 wrong_start_date_attempt = 0
#                 dispatcher.utter_message("Something Went wrong")
#                 return []

#     def validate_name(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker,
#                             domain: Dict[Text, Any]) -> Optional[Text]:
#         current_intent = tracker.latest_message['intent'].get('name')
#         if current_intent == 'stop':
#             global required_slots_list
#             required_slots_list = []
#             return self.deactivate()

#         return {'purpose': value}


#     def validate_comment(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker,
#                          domain: Dict[Text, Any]) -> Optional[Text]:
#         current_intent = tracker.latest_message['intent'].get('name')
#         if current_intent == 'stop':
#             global required_slots_list
#             required_slots_list = []
#             return self.deactivate()

#         return {'purpose': value}

#     def validate_knowledge_summary(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker,
#                                    domain: Dict[Text, Any]) -> Optional[Text]:
#         current_intent = tracker.latest_message['intent'].get('name')
#         if current_intent == 'stop':
#             global required_slots_list
#             required_slots_list = []
#             return self.deactivate()

#         return {"knowledge_summary": value}

class ActionAskPermission(Action):

    def name(self) -> Text:
        return "action_ask_user_permission"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global visited_video

        current_intent_one = tracker.latest_message['intent'].get('name')
        print ("cuerervcd gdchcdc jded", current_intent_one)
        global video_type
        
        video_type = current_intent_one
        if visited_video == 1:
            print("already visited")
            return [FollowupAction("action_comment_form_filling")]
        else:    
            dispatcher.utter_message(template="utter_user_permission")

        return []

class ActionTechnology(Action):

    def name(self) -> Text:
        return "action_get_video_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_technology_type")
        return []

class ActionCustomPayloadFormTwo(Action):

    def name(self) -> Text:
        return "action_custom_payload_form_two"   #---------------------sales contact--------------------#

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ft=[]
        
        ft.append({
                 "type": "Iframe_form",
                 "level": "second_level",
                 "title": "I can show you below demos:",
                 "Form":  "form"
            })
        # dispatcher.utter_custom_json(ft)
        dispatcher.utter_message(json_message=ft)

        return []

class ActionCustomPayloadDocument(Action):

    def name(self) -> Text:
        return "action_custom_payload_document"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        current_intent=tracker.latest_message['intent'].get('name')
        print(current_intent)
        print("Inside custom action payload11111111111111")
        response_doc = requests.get('{}/api/contentlist?contentType=Document'.format(cmc_url))
        response_doc = response_doc.json()
        print(response_doc)
        doc=[]
        doc.append({
                "type": "Iframe_documents",
                "level": "second_level",
                "title": "I can show you below locations:",
                "documents": response_doc
            })
        # dispatcher.utter_custom_json(doc)
        dispatcher.utter_message(json_message=doc)

class ActionPartnership(Action):
    
    def name(self) -> Text:
        return "action_affirm_deny_of_partnership"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Inside custom action partnership",tracker.latest_message['text'])
        automation = ["True" for w in ["automation anywhere","strategic","Inc"] if w in (tracker.latest_message['text']).split(" ")]
        oracle = ["True" for w in ["oracle","corporation","prefrred"] if w in (tracker.latest_message['text']).split(" ")]
        
        if automation is "True":
            dispatcher.utter_message("We are Strategic Partner of Automation Anywhere Inc.")
        elif oracle is "True":
            dispatcher.utter_message("We are preferred Partner of Oracle Corporation.")
        else:
            dispatcher.utter_message("We are preferred Partner of Oracle Corporation and Strategic Partner of Automation Anywhere Inc.")

        return []


class ActionHrInquiry(Action):
    def name(self):
        return 'action_hr_inquiry'

    def run(self, dispatcher, tracker, domain):
        names_response = requests.get('{}/allemployeeApi'.format(mindsconnect_url))
        names_data = names_response.json()
        current_intent=tracker.latest_message['intent'].get('name')
        print(current_intent)
        forms = []
        names_display = []
        names_display.append({"option_value": "All"})
        names_display.append({"option_value": "Not Applicable"})
        for name_details in names_data:
            # print("names_details",name_details['emp_first_name'], name_details['emp_last_name'])
            names_display.append({"option_value":name_details['emp_first_name']+ ' ' + name_details['emp_last_name']})

        print("Asked for to fill details for leave form")
        # print(names_display,"names_display")

        forms.append({
                    "type":"Form",
                    "title":"Please fill following details to apply leave.",
                    "fields":
                        [
                                    {
                                        "field":"Full Name",
                                        "type":"text",
                                        "name":"FullName",
                                        "placeholder":"Full Name"
                                    },
                                    {
                                        "field":"Your Email",
                                        "type":"email",
                                        "name":"YourEmail",
                                        "placeholder":"Your Email"
                                    },
                                    {
                                        "field":"Leave Type",
                                        "type":"dropdown",
                                        "name":"Technology",
                                        "placeholder":"Technology",
                                        "value_list":
                                        [
                                            { "option_value":"PL"},
                                            {"option_value":"CL"},
                                            {"option_value":"LWP"},
                                            {"option_value":"OD"},
                                            {"option_value":"SOD"}
                                        ]
                                    },
                                    {
                                        "field":"Technoligy",
                                        "type":"dropdown",
                                        "name":"technology",
                                        "placeholder":"Select Technology",
                                        # "value_list" : names_display
                                        "value_list":
                                        [
                                            {"option_value":"undefine 1"},
                                            {"option_value":"undefine 2"},
                                            {"option_value":"undefine 3"},
                                            {"option_value":"undefine 4"},
                                            {"option_value":"undefine 5"}
                                        ]
                                    },
                                    {
                                        "field":"comment",
                                        "type":"text",
                                        "name":"comment",
                                        "placeholder":"Eg.Comment"
                                    }                                
                                ]   
                        })

        dispatcher.utter_custom_json(forms)
        print("form sent",forms)
            
        return [SlotSet('separate_detail', None),SlotSet('name2', None)]
