Money
- barter->commodity currency (sth many ppl will exachange for because they need it)->precious metal (rich people want it, a transition to centralized currency)->paper money, now completely centralized
- note the theme of incresing centralization and convinience, which is like political development where people exchange power/freedom for safety/convinience
- credit is essentailly the same as paper money. It's going a little decentralized now since everyone can issue credit now, but it's still backed by companies which represent a transition from monarchy to aristocracy.
- impersonation risk: whenever you assign power to someone other than youself, you create the risk that someone will steal the power, ie, people can bluff. Increasing political power, wealth, and credit are the same.
- current power balance: In politics we are essentially aristocracy with the modification of universal human rights including rights to own things, implying social fluidity. In America power has been allocated significantly to minorities (in the sense of less power) including middle class men. It is currently impossible to allocate more, though the decetralization process has been steady. 
- current wealth balance: total wealth by Americans 134t. Asset of US 269t, debt 145t, net 123t. Total asset of US banks 24t. Total assets of China's financial institutions 480t yuan (68.03t usd)

Cryptonia 
- gold is subject to robbery->powerful benevolent error free dragon 
- tiresome trip to change amount
- DragonBucks: equilavence to a portion fo the the deposit with dragon's signature->stolable->instead of face value, issue checks that has entries of 2 parties' names written by dragon and amount written by villager
- everyone needs n notes (n = number of villigers); recipient can change amount; villiger and outsiders can steal the checks
- need authentification and tamper resistence together: Without authentication, someone could just write a new note even if existing notes are tamper-resistant. Without tamper resistance, someone could modify a note that already has a legitimate signature.
- use the sender's unique spell on the magic wax to seal the amount. 

Encryption
- everyone has a unique private key and shared public key which is f(private). A signiture is private x message. If the function has the property that f(a)*b=f(ab), then signiture=f(private x message)=f(private) x message=public x message. So people can verify if the signiture is really signed by someone by checking if public x message=signiture. However, anyone can get secret key from public key if f is linear. 
- We reduce the linearity of f to f(a x b)=f(f(a) x f(b))
- the verification is signiture=f(private x message)=f(f(private) x message)=f(public x message). You see that anyone can see the public key and therefore make up a signiture
- We need to ensure that public key doesn't directly enable one to make the signiture. That is, f(public x message) != signiture. We reformulate public = f(private x g) so f(public x message)=f(private x g x message) and there is no way to produce f(private x message) with f(private x g x message). Verification is f(sig x g) = f(private x message x g) = f(public x message)

![](/images/crypto-basic-0.png)

Decentralization
- note that previously we were concerned with how to veriify transactions but not the absolute amount of money one holds, which depends compeltely on the dragon. In other words, we lack a decentralized balance sheet/ledger
- solution is to give everyone a ledger

Minting problem
- if it was too easy to make new CCs, some people would stop doing useful work in the town and just try to mint new currency:

Signiture uniqueness
- no duplicate sig should exist because then you would use one message and its sig over and over to fake transactions

Secret key uniqueness
- if your public key is same as some one else, your verification f(private1 x message x g)=f(f(private1 x g) x message)=f(public1 x message)=f(public2 x message)=f(f(private2 x g) x message)=f(private2 x message x g)

Attacks
- If someone knows your s mod n or s x g.
- s mod n can be calculated by public/g mod n, iff g x s < n
- or you can find g inverse p such that p x g mod n = 1 so p x g x s mod n = p x (g x s mod n) mod n = p x public mod n = s mod n. The solution is to choose large n. But there exists a way to compute p in logn time. 
- now we see modular multiplication isn't secure. We try modular exponentiation. public = g^s mod n. This protects against finding s mod n but you will have people's secret key?

Hash collision
- why we want collision resistence (hard to find x and y st H(x)=H(y)): 
- cryptographic hash function — collision resistance and preimage resistance. Preimage resistance means that, given a hash value y, it’s hard to find a “pre-image” x that leads to H(x)=y. We’ve skipped over preimage resistance because, for the types of hash functions we care about, collision resistance implies preimage resistance.

Design a hash function
- 8bit register automatically does mod 256
- first try: split into 8 bit chunks and add them together
- second try: ((x1 x 31)+x2)x31...

Inverting hash function
- n




# Block Chain
- linked list
- hash pointer: as long as you have an authentic copy of one block, any change in previous blocks will propagate to last block before yours and you can check if it matches. ![](/images/merkle-tree-1.png)
- merkle tree: ![](/images/merkle-tree-2.png)

## Ledger
- suppose we have a online banking system where you can only send money you have and the ledger is a big excel sheet on bank's server. 
- hackers might change their money amount. the bank could sign all changes with the bank's secret key to the ledger and verify. However, bank itself might be bad. 
- publish the ledger as a blockchain. Each block would contain transaction information and updated account balances so anyone suspicious about ZooCash’s operation would be able to audit its entire history. Note that audit is not enough since centralized agency can usually get away even if audit fails
- payCash(amount:sender→recipient,sender's signature) and createCash().
- at this point, only sender can sign his own transaction; but only the bank can record it on chain and use createCash(). So it's still centralized. Also the bank's secret key is now vulnerable since it decides everything. 

## Avoid repeated keys

## Decentralized ledger
- everyone (node) has a copy as long as they can verify a transaction and calculate hash of a block
- (note btc chain as of 2025.1.1 is ~600GB) We want users to be able to validate the parts of the ledger that are relevant to them without imposing unreasonable storage and computation requirements.
- efficiient storing
    - list
    - list with branches
    - braches are merkle trees (eth)
- unique bill
- new payCash(): 
    - split bill: payCash(#14:2→{7:20Z¢ as #27,2:80¢ as #28},2†) where # means bill id and 7 and 2 are account id
    - merge bill: payCash({#54:1,#23:2}→3:55Z¢ as #67,1†,2†).


## Double spending
- With cryptocurrencies, it's free for users to make new, anonymous accounts, so we don't allow debt
- for account based/ether like model, we can include transaction counter for each account so a receiver can't duplicate previous transactions
- for bill based/btc like model, 

# Who adds the block (Proof of work)
- A simple model for distributed blockchain maintenance would be for the participants who are running nodes to take turns proposing new blocks to be added to the chain, with the turn order decided randomly.
- problem is the block maker might sneak sth bad in. We could try to prevent the submission of invalid blocks by adding penalties, but the threat of potential punishment might discourage even honest nodes from submitting blocks
- To promote valid blocks rather than just discouraging invalid blocks, we could offer a direct reward
- One way to encourage users to propose valid blocks would be to allow the block proposer to include a createCash() transaction to themselves for a fixed amount of Z
- now it's important to decide who gets to propose the next block
- we could use a random competition st everyone has a chance and it's hard for one node to control the chain and easy for audit
- Anyone is allowed to add a block, but it’s only valid if
    - it contains a hash pointer to the previous block,
    - it contains a single createCash()createCash() call for a set amount of Z¢
    - it contains only valid transactions (properly signed, no double-spends)
    - it solves a certain hash puzzle — that is, the beginning of the hash of the block encodes to a certain pattern
- note that a block has a place to include anything you want so you can quickly try different things there until you solve the puzzle
- this approach will incentivize miners to include nothing in the block
- soluion: transaction makers need to pay miner

# Potential attacks
- if you regert a transaction, you can propose a block with a hash pointer to the block before your transaction. You forked the chain.
- the miners can decide to only follow longest chain, in other words, whichever community with over half the computiing power decide the legit chain. 
- another case is 2 miners mined the same block with different hash (both sovled the puzzle with diffferent hash). this will naturally resolve when one chain becomes longer. This means sometimes a transaction will not make it to the main chain but it's easy to just schedule it later.
- Here are some malicious actions someone might want to perform:
    1. Successfully create a backtracking fork.
    2. Use createCash() multiple times per block.
    3. Suppress certain transactions from making itto the main chain.
    4. Double-spend within the same fork.
    5. Spend cash owned by other accounts.
- only 1 and 3 can be achieved by 51% attack. Others are written into validation/consensus protocols and are verified independently. Further, they wouldn’t be able to do it without other miners noticing. In the case of a transaction suppression attack, miners would notice that their blocks with those transactions always end up getting abandoned for other forks. In the case of a backtrack fork attack, miners would notice that an older, shorter fork overtook what was previously the main fork. This will destroy confidence of the chain and the value of their attack will decrease. 

# Smart Contract
- The part of transaction we haven't dealt with is that most transactions involve two parties. We might have a bad merchant who doesn't deliver. 
- To avoid this, it would help to have a way of “locking” cash, so that the merchant knows the customer has enough money to pay but the cash doesn’t get unlocked and transferred until the customer has actually received the product. We need 2 functions delayPay(sender, receiver, amount, sender_sig) and releasePay(ref, sender_sig, receiver_sig)
- escrow payments: However, the merchant is now in risk. The sender might not initiate the release call. we need an an arbiter trusted by both the customer and the merchant — who can sign releasePayment() in place of either the customer or merchant. 
- In principle, smart contracts can run on more than just signed function calls. They might collect information from the internet automatically and use that info to determine what they do.
- We could also have timeLockPay where the money automatically returns to sender if no agreement is reached in a set time
- ICO (initial coin offering): Ethereum is the second biggest cryptocurrency and started from an ICO on Bitcoin.  In an IPO, a fixed number of shares are sold at a fixed price. To mimic this behavior, an ICO smart contract should automatically send tokens (acting as “shares”) to accounts that send it ZooCash based on a fixed exchange ratio, but stop accepting payments after the set number of tokens have been distributed. ![]
- In principle, smart contracts could handle things like loans, prediction markets, insurance payouts, or royalty payments automatically.
