HackaTUM 2022 Starter Pack
==========================

Welcome to the Algorand Challenge of HackaTUM 2022!

This repository functions as an entry point and reference, to ease your deep dive into the Algorand ecosystem.

This document is structured as follows:

1. [Quickstart Instructions](#Quickstart-Instructions)
2. [Tutorials](#Tutorials)
    1. [Algorand Ecosystem](#Algorand-Ecosystem)
    2. [Connect to Algorand Network](#Connect-to-Algorand-Network)
    3. [Setup Sandbox for local testing](#Setup-Sandbox-for-local-testing)
    4. [Writing SmartContracts](#Writing-SmartContracts)
3. [Ressources](#Ressources)
    1. [Pitch Slidedecks](#Pitch-Slidedecks)
    2. [HackaTUM Algorand Indexer](#HackaTUM-Algorand-Indexer)
    3. [Example Smart Contract Snippets](#Example-Smart-Contract-Snippets)
    4. [Testbed Access](#Testbed-Access)
4. [FAQ](#FAQ)
5. [Reference Overview](#Reference-Overview)

If you want to get your hands dirty as quickly as possible, jump right into the action and follow our [Quickstart Instructions](#Quickstart-Instructions). If you're completely new to Algorand, we suggest you start with a general introduction to the [Algorand Ecosystem](#Algorand-Ecosystem), in the [Tutorials](#Tutorials) section. Of course, if you're already familiar with some of the concepts, feel free to skip what you already know.

Besides the pointers to documentation and ressources, we also provide helpful infrastructure [Ressources](#Ressources) that you can use to build your solution.

If you just want the answer to a quick question, checkout the [FAQ](#FAQ) section.

For convenience, we also provide a structured overview of links to all relevant ressources in the [Reference Overview](#Reference-Overview).

Happy Hacking!

P.S. Dont forget to claim your attandence token!
* [Link to Typeform](https://1i6tgo34ofi.typeform.com/to/ehqxkDwm)
* [Link to Pera wallet tutorial](https://support.perawallet.app/en/article/create-a-new-algorand-account-on-pera-wallet-1ehbj11/)
* Opt-in 

https://support.perawallet.app/en/article/create-a-new-algorand-account-on-pera-wallet-1ehbj11/


## Quickstart Instructions in 4 steps! Should not take longer than 30 mins. 

1. Start off by having a glance at the abstract [Algorand Description](https://developer.algorand.org/docs/get-started/basics/why_algorand/). You now know the basics of the ecosystem you're going to work with.

2. Setup the [Algorand Sandbox Environment](#Setup-Sandbox-for-local-testing). Here you can play around with existing Algorand tools in a local environment. You can also configure the sandbox tools to connect to the public Algorand networks, to access public chain data via the tool APIs.
Required commands:
    * Install docker first if you dont have it: [Docker install steps](https://docs.docker.com/engine/install/)
    * Then, clone the repo: ```git clone https://github.com/algorand/sandbox.git```
    * Navigate to it: ```cd sandbox```
    * Start it: ```./sandbox up```
    * Check sandbox is up: ```docker ps```
    

3. If you're done playing around and want to start working on your envisioned solution, we recommend to focus on the required tools and information first. Follow our [Connect to Algorand Network](#Connect-to-Algorand-Network) tutorial to decide which path to take.

4. If you want to checkout specific transactions on the public chains, you can use the [Algo Explorer](https://algoexplorer.io). The Algorand developer docs also provide an [overview of existing tools in the ecosystem](https://developer.algorand.org/ecosystem-projects).

For quick questions take a look at our [FAQ](#FAQ).

If questions remain find us at our booth or the Algorand Challenge HQ.

Happy Hacking!


## Tutorials

### Algorand Ecosystem

If you're completely new to Algorand - or Blockchains in general - this is a great place to start.

Start off with a general [Introduction to Blockchains](https://developer.algorand.org/docs/get-started/basics/what_is_blockchain/) to get to know the datastructure you're going to work with. If you understood the basics of Blockchain-based systems, take a look at a [High-level Introduction of Algorand](https://developer.algorand.org/docs/get-started/basics/why_algorand/) as an ecosystem.

**Advanced**:
If you want to dive deeper into how Algorand consensus works on logical and network level, you can have a look at a more detailed [Description of Algorand Consensus](https://developer.algorand.org/docs/get-details/algorand_consensus/) or take a look at the original [Algorand Whitepaper](https://eprint.iacr.org/2017/454.pdf).

### Connect to Algorand Network

Your envisioned project might require that you connect to the public Algorand network. Depending on the problem you want to solve, the motivation for connecting to the network is different. To help you focus on the functionality you actually need, we discuss three typical usecases and the next important steps to get going. We choose the following three usecases:

1. [Analysis of Blockchain Data](#Analysis-of-Blockchain-Data)
2. [Development of SmartContracts](#Development-of-SmartContracts)
3. [Development of Algorand or Ecosystem Tooling](#Development-of-Algorand-or-Ecosystem-Tooling)

Of course, your project might require multiple or all of these things. Then just prioritize and follow them as you please.

#### Analysis of Blockchain Data

*Your envisioned solution revolves around using and analyzing data from the Algorand Blockchain. You don't necessarily need to build tooling or write Smart Contracts. You just need data and a way to automatically retrieve and evaluate it. Fast.*

First, it is important to understand how the public Algorand network is structured. Algorand operates multiple networks for different purposes. Check the [Algorand Network Overview](https://developer.algorand.org/docs/get-details/algorand-networks/). The `MainNet` is where the *real* Algorand transactions for *real* monetary value are processed.

For a first glance and easy, manual lookup of data, you can use one of the [Algorand Blockchain Explorers](https://developer.algorand.org/ecosystem-projects), for example the [Algo Explorer](https://algoexplorer.io/).

Now you want to start automating the data access. Instead of setting up an own node to fetch all the data and offer an interface, you can instead query an instance of the [Algorand Indexer](https://developer.algorand.org/docs/get-details/indexer/). The indexer offers a [REST API](https://developer.algorand.org/docs/rest-apis/indexer/) to search and filter Algorand blockchain data. For easier access, you can use one of the SDK client interfaces (for JavaScript, Python, Java and Go) to access the Indexer.

To make your life easier, we operate our own Indexer instance that you can directly use to get going. The indexer is availble under

* Testnet Data - `131.159.14.109:8980`
* Mainnet Data - `131.159.14.109:8981` 

#### Development of SmartContracts

*Your envisioned solution requires the development of SmartContract logic on the Algorand Blockchain. You need an easy-to-setup environment to start writing proof-of-concept code. Later you might want to test your solution against the real network.*

Don't worry about the public Algorand infrastructure for now. For development of your first SmartContract, you should start in the [Algorand Sandbox](https://github.com/algorand/sandbox). The sandbox provides a containerized setup of a completely local, private Algorand network to play around with. We describe the setup in more detail [in another section](#Setup-Sandbox-for-local-testing). If you're completely new to writing SmartContracts on Algorand, we provide more help in [the dedicated tutorial](#Writing-SmartContracts).

Now your code has reached some maturity and you want to test and deploy it towards a "real network". First, check out the [different node types](https://developer.algorand.org/docs/run-a-node/setup/types/) in the Algorand ecosystem. For advanced testing you can now consider [settting up a private network](https://developer.algorand.org/tutorials/create-private-network/) on your local machine (as a "more realistic sandbox"), or [setting up a real node](https://developer.algorand.org/docs/run-a-node/setup/types/).

Algorand operates [multiple networks](https://developer.algorand.org/docs/get-details/algorand-networks/) for different purposes. 
For testing, your Algorand node should be connecting to the [Algorand TestNet](https://developer.algorand.org/docs/archive/build-apps/setup/#choosing-a-network), which features a [Dispenser](https://developer.algorand.org/docs/get-details/algorand-networks/testnet/#faucet) to acquire testing currency.

#### Development of Algorand or Ecosystem Tooling

*Your envisioned solution requires extending or directly interfacing to existing Algorand tools, APIs or SDKs. You need an API to build against and the tooling to test it. Actual transaction creation, SmartContract logic or analysis is secondary for now.*

Since you plan to built with or on Algorand Tooling, you should look deeper into the Algorand ecosystem structure. Checkout [how the consensus mechanism works](https://developer.algorand.org/docs/get-details/algorand_consensus/) and understand that there are [multiple Algorand networks](https://developer.algorand.org/docs/get-details/algorand-networks/).

Take a look at the [existing ecosystem projects and tools](https://developer.algorand.org/ecosystem-projects/). Maybe you can use one of the existing tools to realize your idea faster.

The Algorand Developer Portal provides an [overview of the existing SDKs](https://developer.algorand.org/docs/sdks/) for the ecosystem. For testing and development you want to [setup the Algorand Sandbox](#Setup-Sandbox-for-local-testing) or even [install a full node](https://developer.algorand.org/docs/run-a-node/setup/install/) to natively access the Algorand CLI tools such as [goal](https://developer.algorand.org/docs/clis/goal/goal/), [kmd](https://developer.algorand.org/docs/clis/kmd/) or [algokey](https://developer.algorand.org/docs/clis/algokey/algokey/).

If your tooling involves usage of an indexer, you can use our HackaTUM indexer node, available under 

* Testnet Data - `131.159.14.109:8980`
* Mainnet Data - `131.159.14.109:8981`

### Setup Sandbox for local testing

The fastest way to setup a working environment for learning and testing is to use the [Algorand Sandbox](https://github.com/algorand/sandbox) environment. The sandbox provides access to all developer tools and a fresh Blockchain to work with. In its default configuration, a private network is setup insider of docker containers on your local machine. Extended installation and usage description can be found in the dedicated repository.

### Writing SmartContracts

Begin by reading the Algorand [Introduction of dApps](https://developer.algorand.org/docs/get-started/dapps/).

For development of SmartContracts we recommend using [PyTEAL](https://developer.algorand.org/docs/get-started/dapps/pyteal/), a smart contract language and SDK for usage with Python. This guide also assumes that you're going to use PyTEAL. Alternatively you can develop using [Reach](https://developer.algorand.org/docs/get-started/dapps/reach/). 

The PyTEAL tutorial developer pages introduce an exemplary SmartContract usecase, an autonomous NFT auction. To support your understanding, we provide a set of simpler, less complex PyTEAL smart contract examples in this repository: 

- [counter.py](master/contracts/counter.py): A simple counter that can be modified by calling the smart contract
- [voting.py](master/contracts/voting.py): A simple voting application, that collects and displays votes
- [withdraw.py](master/contracts/withdraw.py): A simple, conditional withdrawal logic

*Tip*: While reading the PyTEAL snippets, checkout python inline help for expressions (e.g. `Seq`, `Cond`, `Approve`, ...) to better understand coding examples.

```
>>> import pyteal
>>> help(pyteal)
>>> help(pyteal.Seq)
...
```

#### Getting started

Before you can actually play around with the simple examples, we need to setup our working environment. Since we're going to work with Python, install

- Python 3.6 or higher
- python-virtualenv (*virtualenv* in pip)

Python virtualenv allows you to create a lightweight "*virtual environment*", which has an independent set of installed Python packages. If you're working in a venv, you don't need to touch your local Python package configuration to fulfill requirements.

Navigate to your local clone of this repository and Setup *venv*:
```bash
python -m venv venv
```
Now activate the venv
```bash
source venv/bin/activate
```
and install all needed python requirements.
```bash
pip install -r requirements.txt
```

Great! Learning and prototyping Algorand Smart Contracts works best, using the [Algorand Sandbox](#Setup-Sandbox-for-local-testing). Set it up.

Now we need to make the content of this repo available to the sandbox docker container. To do so, we need to add a volume to the docker-compose.yml located at the root of the sandbox repo.
The volume has to be added to the *algod* service, e.g. below the ports section:

``` yaml
volumes:
      - type: bind
      - source: path/to/this/dir 
      - target: /data
```
Subsitute path/to/this/dir with the path to this repository (on your machine).
Afterwards, the complete file should look something like this:

``` yaml
services:
  algod:
    container_name: "${ALGOD_CONTAINER:-algorand-sandbox-algod}"
    build:
      context: .
      dockerfile: ./images/algod/Dockerfile
      args:
        CHANNEL: "${ALGOD_CHANNEL}"
        URL: "${ALGOD_URL}"
        BRANCH: "${ALGOD_BRANCH}"
        SHA: "${ALGOD_SHA}"
        BOOTSTRAP_URL: "${NETWORK_BOOTSTRAP_URL}"
        GENESIS_FILE: "${NETWORK_GENESIS_FILE}"
        TEMPLATE: "${NETWORK_TEMPLATE:-images/algod/template.json}"
        NETWORK_NUM_ROUNDS: "${NETWORK_NUM_ROUNDS:-30000}"
        NODE_ARCHIVAL: "${NODE_ARCHIVAL}"
        TOKEN: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        ALGOD_PORT: "4001"
        KMD_PORT: "4002"
        CDT_PORT: "9392"
    ports:
      - ${ALGOD_PORT:-4001}:4001
      - ${KMD_PORT:-4002}:4002
      - ${CDT_PORT:-9392}:9392
    volumes:
      - type: bind
      - source: /home/username/algorand-starter-kit 
      - target: /data
```
#### Deploy to Sandbox 

Now we will take a look at how to deploy transactions to the sandbox network.  Run the following commands in the root of the sandbox repository. First you need to start the Algorand Sandbox: 
```bash
./sandbox up -v
```
This can take some time, add the -v (verbose) flag to see what is going on. After the sandbox has been started successfully, enter `algod` in the docker container:

``` bash
./sandbox enter algod
```
Algod is  a client allowing you to talk to a Algorand node.

TODO @kilian something else coming here?


**Advanced**:

Under the hood, dApps in Algorand are running on the stack-based [Algorand Virtual Machine (AVM)](https://developer.algorand.org/docs/get-details/dapps/avm/). The AVM itself runs contracts written in the assembly-like [Transaction Execution Approval Language (TEAL)](https://developer.algorand.org/docs/get-details/dapps/avm/teal/). Direct development or optimization using TEAL is possible, but less comfortable than using an abstraction such as PyTEAL.

Algorand also offers [two types of contract logic](https://developer.algorand.org/docs/get-details/dapps/smart-contracts/), SmartContracts and SmartSignatures. The logic of a deployed SmartContract can be called by any node in the Algorand Blockchain. The logic of a SmartSignature is only evaluated once, during submission of the transaction which contains the logic.

## Resources

### Pitch Slidedecks
[Link to short and long pitch slides](https://tumde-my.sharepoint.com/:b:/g/personal/filip_rezabek_tum_de/EfJuLxWTpkxOjcs69QZAVcQB7BxNqUIlyx126LMuC16ecg?e=c3p4Bt)

### HackaTUM Algorand Indexer

To ease access to Algorand blockchain data, we operate a dedicated HackaTUM  [Algorand Indexer](https://developer.algorand.org/docs/get-details/indexer/). The indexer offers a [REST API](https://developer.algorand.org/docs/rest-apis/indexer/) to search and filter Algorand blockchain data. For easier access, you can use one of the SDK client interfaces (for JavaScript, Python, Java and Go) to access the Indexer.

Our indexer is available under

* Testnet Data - `131.159.14.109:8980`
* Mainnet Data - `131.159.14.109:8981` 

### Example Smart Contract Snippets

To make your first contact with PyTEAL easier, we provide a set of simple SmartContract examples as part of this repository. You can find an introduction and more information in our [SmartContract Tutorial](#Writing-SmartContracts).

### Testbed Access

Some participants might not own a laptop or a Server/VM,  powerful enough to comfortably run the [sandbox setup](#Setup-Sandbox-for-local-testing). For these teams, we offer SSH access to dedicated hardware hosts.

If your hardware doesn't do the trick for you, approach us at the booth or in the Algorand HQ room. We will allocate credentials for you.

## FAQ

### Where can i find the Algorand booth?

The Algorand booth is located in the entrance area of the [FMI Magistrale](https://www.ph.tum.de/about/visit/roomfinder/?room=magistrale). Look around, you cannot miss us :)

### Where can i find the Algorand HQ?

The Algorand Challenge HQ is located in room `00.08.059`:

https://www.ph.tum.de/about/visit/roomfinder/?room=00.08.059

See you there :)

### What is a blockchain?

https://developer.algorand.org/docs/get-started/basics/what_is_blockchain/

### How does the Algorand network function?

Overview:
- https://developer.algorand.org/docs/get-started/basics/why_algorand/

Consensus Algorithm:
- https://developer.algorand.org/docs/get-started/basics/why_algorand/#the-consensus-protocol
- https://developer.algorand.org/docs/get-details/algorand_consensus/

Multiple Public Networks:
- https://developer.algorand.org/docs/get-details/algorand-networks/
- https://developer.algorand.org/docs/archive/build-apps/setup/#choosing-a-network

### Is there an easily available environment I can play around with?

Use the sandbox environment:
- https://github.com/algorand/sandbox

[Try the simple SmartContract snippets](#Writing-SmartContracts) from this repository.

### Where can I acquire funds for account usage on the public TestNet?
- https://developer.algorand.org/docs/get-details/algorand-networks/testnet/#faucet
- https://bank.testnet.algorand.network/

### Where do I start to get building?

https://developer.algorand.org/docs/get-started/basics/where_to_start/

### What is a SmartContract?

https://developer.algorand.org/docs/get-started/dapps/

Detailed information: https://developer.algorand.org/docs/get-details/dapps/smart-contracts/apps/

### How do I write SmartContracts?

Refer to our [SmartContract Tutorial](#Writing-SmartContracts).

Other Ressources:

- Intro: https://developer.algorand.org/docs/get-started/dapps/
- PyTEAL: https://developer.algorand.org/docs/get-started/dapps/pyteal/
    - Auction Demo: https://github.com/algorand/auction-demo
    - Details: https://developer.algorand.org/docs/get-details/dapps/pyteal/

        Tip: Checkout python inline help "help(pyteal)" for expressions to
             better understand coding examples

- Reach: https://developer.algorand.org/docs/get-started/dapps/reach/

- Raw TEAL: https://developer.algorand.org/docs/get-details/dapps/avm/teal/
    - Raw Teal dev guidelines: https://developer.algorand.org/docs/get-details/dapps/avm/teal/guidelines/
    - Specification: https://developer.algorand.org/docs/get-details/dapps/avm/teal/specification/

## Are there Naming Services on Algorand?

- Algorand name service and marketplace for Non-Fungible Domains (NFDs) — unique, readable aliases for wallet addresses - [NFDomains](https://nf.domains/)
- ANS is a decentralized naming service. An Algorand smart contract stores names and governs the naming policy -  [Algorand Name Service](https://algonameservice.com/home)

### Which programs do I need to install?

This [depends on your usecase](#Connect-to-Algorand-Network). Choose the necessary software accordingly.
 
### Which SDK / Editor should I use?

https://developer.algorand.org/ecosystem-projects/#algodeskio

### How do I create an NFT / Token?

https://developer.algorand.org/docs/get-started/tokenization/nft/

### How do I access / use on-chain data for my application?

Block Explorers:
    https://developer.algorand.org/ecosystem-projects/#algo-explorer

Our indexer:
- SDK/API instructions: https://developer.algorand.org/docs/get-details/indexer/
- Example snippets: https://github.com/algorand/docs/tree/master/examples/indexer

- Indexer REST API available under
    * ```curl "131.159.14.109:8980/health"``` – testnet
    * ```curl "131.159.14.109:8981/health"``` - mainnet


### What are Decentralized Identifiers?

- Primer: https://github.com/WebOfTrustInfo/rwot5-boston/blob/master/topics-and-advance-readings/did-primer.md
- General Definition: https://w3c.github.io/did-core/
- Algorand Spec: https://github.com/algorandfoundation/did-algo

### Where do I get help on XYZ?

- Ask on the booth/workshop room!

## Reference Overview

### Algorand General and Ecosystem
- Algorand Developer Portal: https://developer.algorand.org/
- Algorand tutorials - https://developer.algorand.org/tutorials/
- Existing applications on the Algorand Ecosystem https://developer.algorand.org/ecosystem-projects/ 
- Workplace setup - https://developer.algorand.org/docs/archive/build-apps/setup/
- DApp hello world - https://developer.algorand.org/docs/archive/build-apps/hello_world/
- Great overview of other projects - https://github.com/aorumbayev/awesome-algorand
- Algorand School/Starting slides - https://github.com/cusma/algorand-school
- Crash courses - https://github.com/aorumbayev/awesome-algorand/blob/main/README.md#learning
 


### Decentralized Identifiers

#### DID Specifications
- https://github.com/w3c-ccg/did-pkh/blob/main/did-pkh-method-draft.md
- https://github.com/algorandfoundation/did-algo

#### SDK
- https://www.spruceid.dev/didkit/didkit - A toolkit for Verifiable Credential and Decentralized 

### Research 
- Original Algorand Papers:
    - Main Paper: https://dl.acm.org/doi/pdf/10.1145/3132747.3132757
    - Extended Report: https://eprint.iacr.org/2017/454.pdf

