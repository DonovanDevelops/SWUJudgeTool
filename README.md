There are two things that need to be run to update this offline tool:
1. update_cards.py
    - Running this file generates a new cards_data.js file, which is what the page uses to
    populate the information on the Cards and Additional Rulings tabs.
2. All of the child elements in #updatePolicyInsideHere
    - The elements in this div for the Policy Clarifications are just inspector copy element from
    https://nexus.cascadegames.com/resources/Policy_Clarifications/. Inspecting the page and copying the first child div inside the main element
    (the one with class="container"), right click on the element in the inspector, then click "Copy", then "Copy element" and paste it inside
    #updatePolicyInsideHere, overwriting the existing content.