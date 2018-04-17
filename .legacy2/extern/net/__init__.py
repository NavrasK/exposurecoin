# For functions related to inter-computer networking

# TODO: Place short descriptions for each file in this directory here

# NOTE: This will be a proof-of-concept implementation of the PasteBinServer as a 
#       way to store a publicly viewable registry of users public keys that is able
#       to be updated and read by the users.  The server is a central service which
#       will store the user information in a txt format, with each line being a new
#       user ID / public key.  It is assumed that in a real application of this 
#       this file wouldn't be so readily editable, but it is slightly more realistic
#       than simply having a locally stored txt file for everything

# NOTE: The above may or may not be false, still working on other architecture first,
#       but as of right now there is nothing here, just leave it for now

# NOTE: Networking has been moved to usr due to file system constraints