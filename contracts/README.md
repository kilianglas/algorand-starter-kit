# Smart Contract Examples

This dir contains some basic PyTEAL smart contract examples.
The contracts can be deployed to e.g. the sandbox environment to get a feeling on how interaction with smart contracts works on Algorand.

## Setup
First setup a Python venv:
```bash
python -m venv venv
```
Activate the venv:
```bash
source venv/bin/activate
```
And install the requirements:
```bash
pip install -r requirements.txt
```
### Setup Sandbox
The next thing we need is the Algorand sanbox. 
Clone the sanbox repository:
```bash
git clone https://github.com/algorand/sandbox.git
```
Next we need to make the examples in this directory available to the sanbox docker container.
To do so, we need to add a volume to the docker-compose.yml located at the root of the *sanbox repo*.
The volume has to be added to the *algod* service, e.g. below the ports section:

``` yaml
volumes:
      - type: bind
      - source: path/to/this/dir 
      - target: /data
```
Subsitute *path/to/this/dir* with the path to this directory (on your machine).
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
      - source: /home/username/algorand-starter-kit/contracts
      - target: /data
```
The sanbox can be controlled by using the *sanbox* executable located at the root of the sanbox project.
To start the sanbox run:
```
./sanbox up -v
```
This should start the sanbox docker containers.

### Compiling and Deploying the Examples
Running the examples will compile the contained smart contracts and write the corresponding .teal files to the *build* directory.
E.g. to complie the counter exmple run:
``` bash
python counter.py
```
This should create the build directory containing the following files: 
- *counter_approval.teal*: Complied TEAL code of the approval program of the counter smart contract
- *counter_clear_state.teal*: Compiled TEAL code of the clear state program of the counter smart contract
This process is equivalent for the other examples.
After compilation, we can deploy the smart contracts.
First we need to enter the sanbox algod environment by running in at the root of the sanbox repository:
``` bash
./sanbox enter algod
```
This should open a shell in the sanbox node docker container. In this shell we can use the *goal* CLI to interact with the sandbox Algorand node.
You can find the goal documentation [here](https://developer.algorand.org/docs/clis/goal/goal).

The sanbox already containes some accounts we can use. You can list the available accounts running:
``` bash
goal account list
```
The output should look something like this:

```
[offline]	KWN5SMTE6PFAF65XYX7GYGEBXWMWSOS62FFDCUUTNJTJEX5T5KUXCMR24Q KWN5SMTE6PFAF65XYX7GYGEBXWMWSOS62FFDCUUTNJTJEX5T5KUXCMR24Q	1000225013863741 microAlgos
[online]	K6GMKGWDZGHNVXLYLWSKBNUJCXISL5E43BVEZYTIRS34YZB2PPZLDJUVQ4	K6GMKGWDZGHNVXLYLWSKBNUJCXISL5E43BVEZYTIRS34YZB2PPZLDJUVQ4	4000900004499000 microAlgos
[offline]	QSJE4OUVVJQKKO5WSOTY5OA6HV3ITG3OCYFOLPZGQJIJNUXKDQTEXCOS4E	QSJE4OUVVJQKKO5WSOTY5OA6HV3ITG3OCYFOLPZGQJIJNUXKDQTEXCOS4E	4000900000000000 microAlgos
```


