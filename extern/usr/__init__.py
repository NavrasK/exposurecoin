# For functions related to user logins, account creation and handling

# user.py
#   This contains all the functions directly related to each "user" object.  This will take in the 
#   user's keys and credentials (all calculated externally).  More can potentially be added for
#   things such as local balance, username / password and such, but that can be handled at a later
#   time as we need it
#       savekey
#           Checks if the user's private key has already been saved, if it hasn't then it 
#           creates a folder named after the user_id (so it is anonymous and there should be no crossover)
#           where it stores their private key.  More realistically these would be stored on the
#           user's machine but as the users are all only local this is the system they use.  In addition
#           these user folders will be where anything else that the user saves locally to their "device"
#           should be placed.
