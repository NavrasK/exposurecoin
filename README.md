# exposurecoin
Python based blockchain proof of concept cyptocurrency

BACKGROUND:

This is a cryptocurrency that can be used in a relatively small group of people who make multiple transactions in bursts.  For example if you are betting on horse races in an illegal gambling ring.  You could use this crypto to handle bets during the event, then settle up at the end, or keep the program running for the next time there is a couple races.  That way the transactions are more secret and dirty money doesn't exchange hands until the end.  From this background there is some assumptions that can be made.

ASSUMPTIONS:
 - There is a relatively small number of users
 - There will be multiple transactions made at the end of each "event"
 - Each transaction is made between two people
 - There is low trust among players, and there are scammers in their midsts, but fewer than a third of players are scammers
 - All players will be connected to the internet on the same network and will have access to pastebin
 - All players have the prerequiste files and add ons installed, and have set up their yaml files with their pastebin API developer key at least
 - Players want to remain anonymous
 - This is a proof of concept, not a fully fledged cryptocurrency

CONVENTIONS:

External class files are named as "name_.py" in all lowercase

PREREQUISITES:

install pyyaml with "$ pip install pyyaml"

create a pastebin account and get your dev API key

CREDITS: 

Pastebin API created by AcidVegas (https://www.github.com/acidvegas/pastebin)