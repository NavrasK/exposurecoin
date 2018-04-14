# For functions and resources related to encryption, hashing and decryption

# encrypt.py
#   This handles all encryption and decrytion based tasks.  It doesn't need any inputs on startup, but
#   each function within need to be supplied with the proper inputs in their external calls
#       generateNonce
#           A nonce is a single use value for use with combining hashes, to be used by the 
#           brute force method of proof of work
#       pair
#           Returns a public / private key pair
#       hash
#           Hashes and returns the hashed combination of all inputs (in the order in which they are passed)
#       sign
#           Signs an input with a provided key
#       verify
#           Tries to decrypt an input with a provided key
