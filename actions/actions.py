# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from asyncore import dispatcher
from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#

class Actiontraveldestination(Action):
     def name(self) -> Text:
         return "action_search_travel_destination"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
             entities= tracker.latest_message['entities']
             name = ['']
             for e in entities:
              if e['entity']=='travel':
               name == e['value']
             if name == 'destination':
              message = 'TravelDestination'  
             dispatcher.utter_message(text=message)
             return[]

class ActionBookTickets(Action):

     def name(self) -> Text:
         return "action_search_book_tickets"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities= tracker.latest_message['entities']
        name = [''] 
        for e in entities:
          if e['entity']== 'travel':     
           name = e['value']
          if name == 'tickets':
            message = 'Book Tickets' 
            dispatcher.utter_message(text=message)
                                                                    
            return[]

class ActionHotelAccomodation(Action):

     def name(self) -> Text:
         return "action_search_hotel_accomodation"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         entities= tracker.latest_message['entities']
         name = [''] 
         for e in entities:
          if e['entity']== 'travel':     
            name = e['value']
          if name == 'Accomodation':
            message = 'Hotel Accomodation' 
          dispatcher.utter_message(text=message)
              
          return[]

