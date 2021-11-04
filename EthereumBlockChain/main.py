from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/950a2525db6f4f05981e6a115cd5b72e"

web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())
print(web3.eth.blockNumber)
