# [Eth](https://ethereum.org/en/developers/docs/intro-to-ethereum/)

- Ethereum is a blockchain with a computer embedded in it. In the Ethereum universe, there is a single, canonical computer (called the Ethereum Virtual Machine, or EVM) whose state everyone on the Ethereum network agrees on. Everyone who participates in the Ethereum network (every Ethereum node) keeps a copy of the state of this computer. Additionally, any participant can broadcast a request for this computer to perform arbitrary computation. Whenever such a request is broadcast, other participants on the network verify, validate, and carry out ("execute") the computation. This execution causes a state change in the EVM, which is committed and propagated throughout the entire network.
- Ether burn occurs in every transaction on Ethereum. When users pay for their transactions, a base gas fee, set by the network according to transactional demand, gets destroyed.
- Gwei	10-9
-  A dapp has its backend code running on a decentralized peer-to-peer network. Contrast this with an app where the backend code is running on centralized servers. A dapp can have frontend code and user interfaces written in any language (just like an app) to make calls to its backend. Furthermore, its frontend can get hosted on decentralized storage such as IPFS(opens in a new tab).
    - Decentralized - dapps operate on Ethereum, an open public decentralized platform where no one person or group has control
    - Deterministic - dapps perform the same function irrespective of the environment in which they get executed
    - Turing complete - dapps can perform any action given the required resources
    - Isolated - dapps are executed in a virtual environment so that if the smart contract has a bug, it won’t hamper the normal functioning of the blockchain network
- It’s hard for developers to make updates to their dapps (or the underlying data stored by a dapp)
- There is a huge performance overhead, and scaling is really hard

Web3
- Web2 refers to the version of the internet most of us know today. An internet dominated by companies that provide services in exchange for your personal data. Web3, in the context of Ethereum, refers to decentralized apps that run on the blockchain.
-  core principles:
    - Web3 is **decentralized**: instead of large swathes of the internet controlled and owned by centralized entities, ownership gets distributed amongst its builders and users.
    - Web3 is **permissionless**: everyone has equal access to participate in Web3, and no one gets excluded.
    - Web3 has **native payments**: it uses cryptocurrency for spending and sending money online instead of relying on the outdated infrastructure of banks and payment processors.
    - Web3 is **trustless**: it operates using incentives and economic mechanisms instead of relying on trusted third-parties.
- Examples: 
    - **Web3 tweets** uncensorable because control is decentralized
    - **Web3 payment**, no personal data and can't prevent payments
    - **Web3 servers** can't go down – they use Ethereum, a decentralized network of 1000s of computers as their backend
- limitations:
    - **Scalability** – transactions are slower on web3 because they're decentralized. Changes to state, like a payment, need to be processed by a node and propagated throughout the network.
    - **UX** – interacting with web3 applications is difficult
    - **Accessibility** – the lack of integration in modern web browsers
    - **Cost** 

Decentralization
> I happily played World of Warcraft during 2007–2010, but one day Blizzard removed the damage component from my beloved warlock's Siphon Life spell. I cried myself to sleep, and on that day I realized what horrors centralized services can bring. I soon decided to quit.

https://medium.com/@VitalikButerin/the-meaning-of-decentralization-a0c92b76a274
- ![](/images/3-axes-decen.webp) Blockchains are politically decentralized (no one controls them) and architecturally decentralized (no infrastructural central point of failure) but they are logically centralized (there is one commonly agreed state and the system behaves like a single computer)

Account
- last 20 bytes of hash(public key)

Nodes
- The software must be run on your computer to turn it into an Ethereum node. There are two separate pieces of software (known as 'clients') required to form a node.
    - The **execution client** The execution client bundles transactions from the local mempool into an "execution payload" and executes them locally to generate a state change. This information is passed to the consensus client
    - The **consensus client** (also known as the Beacon Node, CL client or formerly the Eth2 client) implements the proof-of-stake consensus algorithm, which enables the network to achieve agreement based on validated data from the execution client. There is also a third piece of software, known as a 'validator' that can be added to the consensus client, allowing a node to participate in securing the network.
- types of nodes:
    - Full: block-by-block validation of the blockchain, including downloading and verifying the block body and state data for each block
    - Archive nodes: full nodes that verify every block from genesis and never delete any of the downloaded data.
    - Light nodes: only download block headers. Any other information gets requested from a full node

Consensus
- reaching consensus means that at least 66% of the nodes on the network agree on the global state of the network.
- To participate as a validator, a user must deposit 32 ETH into the deposit contract and run three separate pieces of software: an execution client, a consensus client, and a validator client. Once activated, validators receive new blocks from peers on the Ethereum network. The transactions delivered in the block are re-executed to check that the proposed changes to Ethereum's state are valid, and the block signature is checked. The validator then sends a vote (called an attestation) in favor of that block across the network.
- Time in proof-of-stake Ethereum is divided into slots (12 seconds) and epochs (32 slots). **One validator is randomly selected to be a block proposer in every slot**. This validator is responsible for creating a new block and sending it out to other nodes on the network. Also in every slot, a committee of validators is randomly chosen, whose votes are used to determine the validity of the block being proposed. Dividing the validator set up into committees is important for keeping the network load manageable. Committees divide up the validator set so that every active validator attests in every epoch, but not in every slot.



EVM
- https://ethereum.org/en/developers/docs/evm/ Instead of a distributed ledger, Ethereum is a distributed state machine(opens in a new tab). Ethereum's state is a large data structure which holds not only all accounts and balances, but a machine state, which can change from block to block according to a pre-defined set of rules, and which can execute arbitrary machine code. The specific rules of changing state from block to block are defined by the EVM.

- https://takenobu-hs.github.io/downloads/ethereum_evm_illustrated.pdf
- The world state is a set of (mapping between address and account state)/(account). An account is an object in the world state. 
- EOA is controlled by a private key. EOA cannot contain EVM code.
- A transaction is submitted by external actor.
- There are two practical types of transaction, contract creation and message call.
- 

# Web3
The term "web3" was coined in 2014 by Ethereum co-founder Gavin Wood,

[intro to web3 app](https://www.preethikasireddy.com/post/the-architecture-of-a-web-3-0-application): ![](/images/web3.png)

[web3.py](https://ethereum.org/en/developers/tutorials/a-developers-guide-to-ethereum-part-one/)
```
pip install ipython
pip install web3
pip install 'web3[tester]'

ipython
```

```py
from web3 import Web3

Web3.to_wei(1, 'ether')
Web3.from_wei(500000000, 'gwei')

w3 = Web3(Web3.EthereumTesterProvider())
w3.is_connected() # boolean

w3.eth.accounts # list of ten strings
w3.eth.get_balance(w3.eth.accounts[0])

acct = w3.eth.account.create()
acct.address
acct.key

w3.eth.get_block('latest')
#	AttributeDict({
#	   'number': 0,
#	   'hash': HexBytes('0x9469878...'),
#	   'parentHash': HexBytes('0x0000000...'), this is genesis block
#	   ...
#	   'transactions': []
#	})

tx_hash = w3.eth.send_transaction({
   'from': w3.eth.accounts[0],
   'to': w3.eth.accounts[1],
   'value': w3.to_wei(3, 'ether'),
   'gas': 21000
})
w3.eth.wait_for_transaction_receipt(tx_hash)
w3.eth.get_transaction(tx_hash)

#AttributeDict({
#	   'hash': HexBytes('0x15e9fb95dc39...'),
#	   'blockNumber': 1,
#	   'transactionIndex': 0,
#	   'from': '0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf',
#	   'to': '0x2B5AD5c4795c026514f8317c7a215E218DcCD6cF',
#	   'value': 3000000000000000000,
#	   ...
#	})
```
web3.py knows EthereumTesterProvider is managing w3.eth.accounts and that we're using a test environment. For our convenience, w3.eth.accounts are "unlocked," meaning transactions from the accounts are approved (signed) by default.

with actual provider
```py
from web3 import Web3

# Connect to an Ethereum node
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# Define the transaction
tx = {
    'from': w3.eth.accounts[0],
    'to': w3.eth.accounts[1],
    'value': w3.to_wei(3, 'ether'),
    'gas': 21000,
    'gasPrice': w3.eth.get_block('pending')['baseFeePerGas'],
    'nonce': w3.eth.get_transaction_count(w3.eth.accounts[0]),
}

# Sign the transaction with the private key
private_key = "0xYOUR_PRIVATE_KEY"
signed_tx = w3.eth.account.sign_transaction(tx, private_key)

# Send the signed transaction
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

# Wait for the receipt
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# Get transaction details
transaction_details = w3.eth.get_transaction(tx_hash)
print(transaction_details)
```

#### Smart contract 
>  You can leave the contract open for the world to use, restrict its usage to only your account, or require a certain balance or the ownership of a particular asset to interact with it. Either way, if your contract is deployed to Ethereum Mainnet, that code is public!
```py
Example = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = Example.constructor().transact()

myContract = web3.eth.contract(address=address, abi=abi)
twentyone = myContract.functions.multiply7(3).call()
```

#### Messaging
> the terms "on-chain" and "off-chain" are shorthand for whether data lives on the Ethereum blockchain. For example, smart contract state is managed on-chain, but message signing occurs off-chain.
```py
# 1. write a message
msg = "hi"

# 2. sign it with an account's private key
pk = b"..."
signed_message = sign_message(message=msg, private_key=pk)

# 3. send `signed_message` over the wire

# 4. message receiver decodes sender's public address
sender = decode_message_sender(msg, signed_message.signature)
print(sender)
# '0x5ce9454...b9aB12E'
```


### Solidity
https://snakecharmers.ethereum.org/a-developers-guide-to-ethereum-pt-3/

The constructor method is executed only once, when the contract is first deployed.
```c#
// SPDX-License-Identifier: MIT
pragma solidity 0.8.17;

contract Billboard {
    string public message;
    
    constructor(string memory _message) {
        message = _message;
    }
    
    function writeBillboard(string memory _message) public {
        message = _message;
    }
}
```

ABI (Application Binary Interface) is a machine-readable data blob that conveys how a contract can be interacted with – which functions are available and expected data types. It's some JSON that you pass into an Ethereum library (e.g., web3.py, ethers.js, etc.), so that it can provide you with a human-friendly interface. Does the name make sense now? An ABI communicates the interface for your application's bytecode.

```py
# Instantiate a contract factory:
Billboard = w3.eth.contract(abi=abi, bytecode=bytecode)

# Deploy an instance of the contract:
tx_hash = Billboard.constructor("eth very wow").transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# Retrieve the deployed contract instance:
billboard = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)

# Interact with the contract instance:
billboard.functions.message().call()
# eth very wow

billboard.functions.writeBillboard("sneks everywhere").transact()

billboard.functions.message().call() # sneks everywhere
```

Inheritance
```c#
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MyToken is ERC20 {
    constructor() ERC20("ExampleToken", "XMPL") { ... }
}

```

### Remix 

### ERC20/Tokens on Chain
ERC20 is a standard made by the community

https://www.quicknode.com/guides/ethereum-development/smart-contracts/how-to-create-and-deploy-an-erc20-token