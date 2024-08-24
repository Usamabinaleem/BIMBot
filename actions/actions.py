# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# actions.py

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import ifcopenshell
#
# class ActionCheckIFCClass(Action):
#
#     def name(self) -> str:
#         return "action_check_ifc_class"
#
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
#         # Extract the entity name (IFC class) from the slot
#         ifc_class = tracker.get_slot('ifc_class')
#
#         # Load the IFC file (ensure this path is accessible and correct)
#         ifc_file = ifcopenshell.open('QueensBuildings.ifc')
#
#         # Check if the IFC class exists in the model
#         entities = ifc_file.by_type(ifc_class)
#         if entities:
#             dispatcher.utter_message(text=f"The model contains the entity {ifc_class}.")
#         else:
#             dispatcher.utter_message(text=f"The model does not contain the entity {ifc_class}.")
#
#         return []


#this code works for the initial IFC classes

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import ifcopenshell
#
#
# class ActionCheckIFCClass(Action):
#
#     def name(self) -> str:
#         return "action_check_ifc_class"
#
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
#         # Extract the entity name (IFC class) from the slot
#         ifc_class = tracker.get_slot('ifc_class')
#
#         # Debug: Print the extracted slot value
#         print(f"Extracted ifc_class: {ifc_class}")
#
#         if not ifc_class:
#             dispatcher.utter_message(text="I couldn't identify the IFC class you are asking about.")
#             return []
#
#         # Load the IFC file (ensure this path is accessible and correct)
#         try:
#             ifc_file = ifcopenshell.open('QueensBuildings.ifc')
#         except Exception as e:
#             dispatcher.utter_message(text=f"Failed to open the IFC file: {str(e)}")
#             return []
#
#         # Check if the IFC class exists in the model
#         entities = ifc_file.by_type(ifc_class)
#         if entities:
#             dispatcher.utter_message(text=f"The model contains the entity {ifc_class}.")
#         else:
#             dispatcher.utter_message(text=f"The model does not contain the entity {ifc_class}.")
#
#         return []



# actions.py

# actions.py

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import ifcopenshell

# class ActionCheckIFCClass(Action):
#
#     def name(self) -> str:
#         return "action_check_ifc_class"
#
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
#         # Extract the entity name (IFC class) from the slot
#         ifc_class = tracker.get_slot('ifc_class')
#
#         # Debug: Print the extracted slot value
#         print(f"Extracted ifc_class: {ifc_class}")
#
#         if not ifc_class:
#             dispatcher.utter_message(text="I couldn't identify the IFC class you are asking about.")
#             return []
#
#         # Load the IFC file (ensure this path is accessible and correct)
#         try:
#             ifc_file = ifcopenshell.open('FS0912-BDP-01-ZZ-M-A-0002.ifc')
#         except Exception as e:
#             dispatcher.utter_message(text=f"Failed to open the IFC file: {str(e)}")
#             return []
#
#         # Normalize the IFC class input to match IFC schema convention
#         ifc_class = ifc_class.strip().upper()
#
#         # Check if the IFC class exists in the model
#         try:
#             entities = ifc_file.by_type(ifc_class)
#         except Exception as e:
#             dispatcher.utter_message(text=f"Error in searching the IFC file: {str(e)}")
#             return []
#
#         if entities:
#             dispatcher.utter_message(text=f"The model contains {len(entities)} entities of type {ifc_class}.")
#         else:
#             dispatcher.utter_message(text=f"The model does not contain any entities of type {ifc_class}.")
#
#         return []
#
#
# #testing IFC attributes
#
# # actions.py
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import ifcopenshell
# import ifcopenshell.util.element
#
# class ActionQueryIFCProperty(Action):
#
#     def name(self) -> str:
#         return "action_query_ifc_property"
#
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
#         ifc_class = tracker.get_slot('ifc_class')
#
#         print(f"Extracted ifc_class: {ifc_class}")
#
#         if not ifc_class:
#             dispatcher.utter_message(text="I couldn't identify the IFC class you're asking about.")
#             return []
#
#         try:
#             ifc_file = ifcopenshell.open('FS0912-BDP-01-ZZ-M-A-0002.ifc')  # Update with your actual IFC file path
#         except Exception as e:
#             dispatcher.utter_message(text=f"Failed to open the IFC file: {str(e)}")
#             return []
#
#         ifc_class = ifc_class.strip().upper()
#
#         try:
#             entities = ifc_file.by_type(ifc_class)
#         except Exception as e:
#             dispatcher.utter_message(text=f"Error in searching the IFC file: {str(e)}")
#             return []
#
#         if not entities:
#             dispatcher.utter_message(text=f"The model does not contain any entities of type {ifc_class}.")
#             return []
#
#         results = []
#         for entity in entities:
#             psets = ifcopenshell.util.element.get_psets(entity)
#             entity_results = {pset_name: pset_values for pset_name, pset_values in psets.items()}
#             results.append(entity_results)
#
#         if results:
#             dispatcher.utter_message(text=f"The properties of {ifc_class} are: {results}")
#         else:
#             dispatcher.utter_message(text=f"No properties found for {ifc_class}.")
#
#         return []



#File upload code


# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import ifcopenshell
# import os
#
# class ActionCheckIFCClass(Action):
#
#     def name(self) -> str:
#         return "action_check_ifc_class"
#
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
#         ifc_class = tracker.get_slot('ifc_class')
#
#         print(f"Extracted ifc_class: {ifc_class}")
#
#         if not ifc_class:
#             dispatcher.utter_message(text="I couldn't identify the IFC class you are asking about.")
#             return []
#
#         # Load the most recently uploaded IFC file
#         try:
#             uploaded_files = os.listdir('uploads')
#             if not uploaded_files:
#                 dispatcher.utter_message(text="No IFC file has been uploaded.")
#                 return []
#             latest_file = max([os.path.join('uploads', f) for f in uploaded_files], key=os.path.getctime)
#             ifc_file = ifcopenshell.open(latest_file)
#         except Exception as e:
#             dispatcher.utter_message(text=f"Failed to open the IFC file: {str(e)}")
#             return []
#
#         ifc_class = ifc_class.strip().upper()
#
#         try:
#             entities = ifc_file.by_type(ifc_class)
#         except Exception as e:
#             dispatcher.utter_message(text=f"Error in searching the IFC file: {str(e)}")
#             return []
#
#         if entities:
#             dispatcher.utter_message(text=f"The model contains {len(entities)} entities of type {ifc_class}.")
#         else:
#             dispatcher.utter_message(text=f"The model does not contain any entities of type {ifc_class}.")
#
#         return []
#
#
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import ifcopenshell
# import os
#
# class ActionQueryIFCProperty(Action):
#
#     def name(self) -> str:
#         return "action_query_ifc_property"
#
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
#         ifc_class = tracker.get_slot('ifc_class')
#
#         print(f"Extracted ifc_class: {ifc_class}")
#
#         if not ifc_class:
#             dispatcher.utter_message(text="I couldn't identify the IFC class you're asking about.")
#             return []
#
#         # Load the most recently uploaded IFC file
#         try:
#             upload_folder = 'uploads'  # Ensure this is the correct path to the uploads folder
#             uploaded_files = os.listdir(upload_folder)
#             if not uploaded_files:
#                 dispatcher.utter_message(text="No IFC file has been uploaded.")
#                 return []
#             latest_file = max([os.path.join(upload_folder, f) for f in uploaded_files], key=os.path.getctime)
#             ifc_file = ifcopenshell.open(latest_file)
#         except Exception as e:
#             dispatcher.utter_message(text=f"Failed to open the IFC file: {str(e)}")
#             return []
#
#         # Normalize the IFC class input to match IFC schema convention
#         ifc_class = ifc_class.strip().upper()
#
#         try:
#             entities = ifc_file.by_type(ifc_class)
#         except Exception as e:
#             dispatcher.utter_message(text=f"Error in searching the IFC file: {str(e)}")
#             return []
#
#         if not entities:
#             dispatcher.utter_message(text=f"The model does not contain any entities of type {ifc_class}.")
#             return []
#
#         results = []
#         for entity in entities:
#             psets = ifcopenshell.util.element.get_psets(entity)
#             entity_results = {pset_name: pset_values for pset_name, pset_values in psets.items()}
#             results.append(entity_results)
#
#         if results:
#             dispatcher.utter_message(text=f"The properties of {ifc_class} are: {results}")
#         else:
#             dispatcher.utter_message(text=f"No properties found for {ifc_class}.")
#
#         return []




#might fix the latest ifc file upload


import os
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import ifcopenshell


class ActionCheckIFCClass(Action):

    def name(self) -> str:
        return "action_check_ifc_class"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        ifc_class = tracker.get_slot('ifc_class')

        if not ifc_class:
            dispatcher.utter_message(text="I couldn't identify the IFC class you're asking about.")
            return []

        try:
            # Load the most recently uploaded IFC file
            upload_folder = 'uploads'
            uploaded_files = os.listdir(upload_folder)
            if not uploaded_files:
                dispatcher.utter_message(text="No IFC file has been uploaded.")
                return []

            latest_file = max([os.path.join(upload_folder, f) for f in uploaded_files], key=os.path.getctime)
            ifc_file = ifcopenshell.open(latest_file)

        except Exception as e:
            dispatcher.utter_message(text=f"Failed to open the IFC file: {str(e)}")
            return []

        ifc_class = ifc_class.strip().upper()

        try:
            entities = ifc_file.by_type(ifc_class)
        except Exception as e:
            dispatcher.utter_message(text=f"Error in searching the IFC file: {str(e)}")
            return []

        if entities:
            dispatcher.utter_message(text=f"The model contains {len(entities)} entities of type {ifc_class}.")
        else:
            dispatcher.utter_message(text=f"The model does not contain any entities of type {ifc_class}.")

        return []




#Properties with structured data


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import ifcopenshell
import os

class ActionQueryIFCProperty(Action):

    def name(self) -> str:
        return "action_query_ifc_property"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        ifc_class = tracker.get_slot('ifc_class')
        entity_name = tracker.get_slot('entity_name')  # Assume there is an entity_name slot for specific names

        if not ifc_class:
            dispatcher.utter_message(text="I couldn't identify the IFC class you're asking about.")
            return []

        try:
            # Load the most recently uploaded IFC file
            upload_folder = 'uploads'
            uploaded_files = os.listdir(upload_folder)
            if not uploaded_files:
                dispatcher.utter_message(text="No IFC file has been uploaded.")
                return []

            latest_file = max([os.path.join(upload_folder, f) for f in uploaded_files], key=os.path.getctime)
            ifc_file = ifcopenshell.open(latest_file)

        except Exception as e:
            dispatcher.utter_message(text=f"Failed to open the IFC file: {str(e)}")
            return []

        ifc_class = ifc_class.strip().upper()

        try:
            entities = ifc_file.by_type(ifc_class)
        except Exception as e:
            dispatcher.utter_message(text=f"Error in searching the IFC file: {str(e)}")
            return []

        if not entities:
            dispatcher.utter_message(text=f"The model does not contain any entities of type {ifc_class}.")
            return []

        specific_entity = None
        for entity in entities:
            if entity_name and entity.Name and entity_name.lower() in entity.Name.lower():
                specific_entity = entity
                break

        if not specific_entity:
            dispatcher.utter_message(text=f"No specific {ifc_class} entity found by the name '{entity_name}'.")
            return []

        try:
            # Retrieve the property sets
            psets = ifcopenshell.util.element.get_psets(specific_entity)

            if not psets:
                dispatcher.utter_message(text=f"No properties found for {ifc_class} named '{entity_name}'.")
                return []

            formatted_properties = f"The properties of {ifc_class} named '{entity_name}' are:\n"
            for pset_name, pset_values in psets.items():
                formatted_properties += f"\n{pset_name}:\n"
                for prop_name, prop_value in pset_values.items():
                    formatted_properties += f"  - {prop_name}: {prop_value}\n"

            # Only dispatch the final formatted properties without the debug message
            dispatcher.utter_message(text=formatted_properties)

        except Exception as e:
            dispatcher.utter_message(text=f"An error occurred while retrieving properties: {str(e)}")

        return []



#names of ifc classes


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import ifcopenshell
import os

class ActionListIFCEntities(Action):

    def name(self) -> str:
        return "action_list_ifc_entities"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        ifc_class = tracker.get_slot('ifc_class')

        if not ifc_class:
            dispatcher.utter_message(text="I couldn't identify the IFC class you're asking about.")
            return []

        try:
            # Load the most recently uploaded IFC file
            upload_folder = 'uploads'
            uploaded_files = os.listdir(upload_folder)
            if not uploaded_files:
                dispatcher.utter_message(text="No IFC file has been uploaded.")
                return []

            latest_file = max([os.path.join(upload_folder, f) for f in uploaded_files], key=os.path.getctime)
            ifc_file = ifcopenshell.open(latest_file)

        except Exception as e:
            dispatcher.utter_message(text=f"Failed to open the IFC file: {str(e)}")
            return []

        ifc_class = ifc_class.strip().upper()

        try:
            entities = ifc_file.by_type(ifc_class)
        except Exception as e:
            dispatcher.utter_message(text=f"Error in searching the IFC file: {str(e)}")
            return []

        if not entities:
            dispatcher.utter_message(text=f"No entities of type {ifc_class} found in the model.")
            return []

        # Collecting the names directly from the Name attribute
        entity_names = []
        for entity in entities:
            if entity.Name:
                print(f"Found entity with Name: {entity.Name}")
                entity_names.append(entity.Name)
            else:
                print(f"Entity ID {entity.id()} has no Name attribute.")

        if entity_names:
            dispatcher.utter_message(text=f"The names of all {ifc_class} entities in the model are: {', '.join(entity_names[:50])}")
            if len(entity_names) > 50:
                dispatcher.utter_message(text=f"And more... (total {len(entity_names)} entities)")
        else:
            dispatcher.utter_message(text=f"No named entities of type {ifc_class} found in the model.")

        return []
