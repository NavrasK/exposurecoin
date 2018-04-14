# For functions related to the architechture of the blocks and blockchain

# transaction.py
#   These objects are the transactions themselves, and they contain who is sending the XP, where it is 
#   going, and how much is moving.
#       getTransaction
#           Returns a dictionary which contians the net change in both users' accounts.
#
# xp.py
#   These are the blocks which will be stored on the blockchain.  They contain some information about
#   their position in the chain as well as the details for the transactions.  Once a block is full
#   or a certain amount of time has elapsed the block will be added to the blockchain and a new one will
#   be created to be filled.
#       getTransactions
#           Returns the value of the transactions stored within the block as of the block being called
#       updateTransactions
#           Returns a temporary dictionary with the overall change in balance for a user based on a
#           transaction
#
# blockchain.py
#   This is where multiple blocks will be stored.  Once a block is accepted by consensus each user will
#   add it to their blockchain, and systems will be in place to ensure that all users have the same 
#   record of transactions.  
#       getAccepted
#           Returns the overall accepted final state of each user's balance, up until the first unresolved
#           conflict
#       updateTransactions
#           Returns a temporary dictionary with the overall change in balance for a user based on a
#           transaction
#
# tree.py
#   This is what each conflict node on the blockchain will be made of.  Whenever there is more than one 
#   list of transactions after an accepted node there is a discontinuity, and these conflicting nodes
#   are kept until the final accepted state of the network is found, when the branch with the correct 
#   sequence of transactions is longer than the false one.  This is bound to occur assuming there are 
#   more users on the network acting legitmiately, which we will assume is true for the purpose of the 
#   demonstration.
