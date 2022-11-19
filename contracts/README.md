# Smart Contract Examples

This directory contains some basic PyTEAL smart contract examples.
The contracts can be deployed to e.g. the sandbox environment to get a feeling on how interaction with smart contracts works on Algorand.

## Setup
Before you can actually play around with the simple examples, we need to setup our working environment. Since we're going to work with Python, install

- Python 3.6 or higher
- python-virtualenv (*virtualenv* in pip)

Python virtualenv allows you to create a lightweight "*virtual environment*", which has an independent set of installed Python packages. If you're working in a venv, you don't need to touch your local Python package configuration to fulfill requirements.

Now setup a Python venv:
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
Clone the sandbox repository:
```bash
git clone https://github.com/algorand/sandbox.git
```
Next we need to make the examples in this directory available to the sandbox docker container.
To do so, we need to add a volume to the docker-compose.yml located at the root of the *sandbox repo*.
The volume has to be added to the *algod* service, e.g. below the ports section:

``` yaml
volumes:
      - type: bind
      - source: path/to/this/dir 
      - target: /data
```
Substitute *path/to/this/dir* with the path to this directory (on your machine).
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
        source: /home/username/algorand-starter-kit/contracts
        target: /data
```
The sandbox can be controlled by using the *sandbox* executable located at the root of the sandbox project.
To start the sandbox run:
```
./sandbox up -v
```
This should start the sandbox docker containers.

## Compiling and Deploying the Examples
Running the examples will compile the contained smart contracts and write the corresponding .teal files to the *build* directory.
E.g. to compile the counter example run:
``` bash
python counter.py
```
This should create the build directory containing the following files: 
- *counter_approval.teal*: Complied TEAL code of the approval program of the counter smart contract
- *counter_clear_state.teal*: Compiled TEAL code of the clear state program of the counter smart contract
This process is equivalent for the other examples.
After compilation, we can deploy the smart contracts.
First, we need to enter the sandbox algod environment by running in at the root of the sandbox repository:
``` bash
./sanbox enter algod
```
This should open a shell in the sandbox node docker container. In this shell we can use the *goal* CLI to interact with the sandbox Algorand node.
You can find the goal documentation [here](https://developer.algorand.org/docs/clis/goal/goal).

The sandbox already contains some accounts we can use. You can list the available accounts running:
``` bash
goal account list
```
The output should look something like this:

```
[offline]	KWN5SMTE6PFAF65XYX7GYGEBXWMWSOS62FFDCUUTNJTJEX5T5KUXCMR24Q	KWN5SMTE6PFAF65XYX7GYGEBXWMWSOS62FFDCUUTNJTJEX5T5KUXCMR24Q	1000225013863741 microAlgos
[online]	K6GMKGWDZGHNVXLYLWSKBNUJCXISL5E43BVEZYTIRS34YZB2PPZLDJUVQ4	K6GMKGWDZGHNVXLYLWSKBNUJCXISL5E43BVEZYTIRS34YZB2PPZLDJUVQ4	4000900004499000 microAlgos
[offline]	QSJE4OUVVJQKKO5WSOTY5OA6HV3ITG3OCYFOLPZGQJIJNUXKDQTEXCOS4E	QSJE4OUVVJQKKO5WSOTY5OA6HV3ITG3OCYFOLPZGQJIJNUXKDQTEXCOS4E	4000900000000000 microAlgos
```
We will need the account addresses to play around with the deployed smart contracts, so copy them and store them in corresponding environment variables. E.g.:

``` bash
ACC_A=KWN5SMTE6PFAF65XYX7GYGEBXWMWSOS62FFDCUUTNJTJEX5T5KUXCMR24Q
ACC_B=K6GMKGWDZGHNVXLYLWSKBNUJCXISL5E43BVEZYTIRS34YZB2PPZLDJUVQ4
ACC_C=QSJE4OUVVJQKKO5WSOTY5OA6HV3ITG3OCYFOLPZGQJIJNUXKDQTEXCOS4E
```
The following subsections contain instructions on how to deploy and call the individual examples.

#### Counter
The counter example contains a smart contracts that maintains a simple counter that can be incremented or decremented by submitting corresponding application call
transactions. Furthermore, the app can be deleted by the account that has created it. 
First, we need to deploy the counter smart contract by using the app create command: 
``` bash
goal app create --creator $ACC_[A|B|C] --approval-prog /data/build/counter_approval.teal --clear-prog /data/build/counter_clear_state.teal --global-byteslices 1 --global-ints 1 --local-byteslices 0 --local-ints 0
```
The --creator option specifies the creator account of the smart contract, i.e. the sender of the application transaction. The --approval-prog and --clear-prog options pass
the files containing the code of the smart contract, i.e. the compiled approval and clear state programs. The remaining options specify the fields of the state used by the
smart contract. In the counter example, two fields are used. An integer field for the counter and a byte slice field for the owner address. Local state is not used.
This output should look something like this:
``` 
Transaction LFFZZJY3MYKSGDJ7DLNAASB3D6OVUOTKBQF4TITRC5E3QYZM64AQ still pending as of round 100
Transaction LFFZZJY3MYKSGDJ7DLNAASB3D6OVUOTKBQF4TITRC5E3QYZM64AQ still pending as of round 101 
Transaction LFFZZJY3MYKSGDJ7DLNAASB3D6OVUOTKBQF4TITRC5E3QYZM64AQ committed in round 102
Created app with app index 1 
```
*Important*: You need to remember the app index, since this index is required in order to interact with the app. You can look up the apps create by accounts by running:
``` bash
goal account list
```
After the app has been deployed, you can get information about the app by running (replace <APP_ID> by the correct app ID, e.g. 1 for the output depicted above):

``` bash
goal app info --app-id <APP_ID> 
```
You can read the global state of the app using goal as well:

``` bash
goal app read --app-id <APP_ID> --global
```
Right after the deployment, this should ouptut something like this:

``` bash
{
  "counter": {
    "tt": 2
  },
  "owner": {
    "tb": "U\ufffd\ufffd2d\ufffd\ufffd\u0002\ufffd\ufffd\ufffd\ufffdl\u0018\ufffd\ufffd\ufffdi:^\ufffdJ1R\ufffdjf\ufffd_\ufffd\ufffd\ufffd",
    "tt": 1
  }
```
Note that the counter value is not displayed. This is the case because the counter is initialized to 0. Once the value changes, it will be shown.
Now we want to increment the counter by issuing an application call transaction. To do so, run:
``` bash
goal app call --from $ACC_[A|B|C] --app-id <APP_ID> --app-arg "str:inc"
```
The --from option again specifies the sender account. The --app-arg option is used to pass an argument to the app call. In our
case, this can either be "inc" or "dec", to increment or decrement the counter, respectively. The "str:" prefix specifies the type of the argument, which is string in our case.
Running another

``` bash
goal app read --app-id <APP_ID> --global 
```
should now ouput 
``` 
{
  "counter": {
    "tt": 2,
    "ui": 1
  },
  "owner": {
    "tb": "U\ufffd\ufffd2d\ufffd\ufffd\u0002\ufffd\ufffd\ufffd\ufffdl\u0018\ufffd\ufffd\ufffdi:^\ufffdJ1R\ufffdjf\ufffd_\ufffd\ufffd\ufffd",
    "tt": 1
  }
```
You can decrement the counter by running:
``` bash
goal app call --from $ACC_[A|B|C] --app-id <APP_ID> --app-arg "str:dec"
```

### Voting

The voting smart contract implements a simple decentralized binary voting. The app keeps track of two counters, one for "yes" and one for "no" votes. In order to
participate in the voting, accounts need to register during a registration period. This can be done by opting into the application. After the registration period, the voting period
starts. Each registered account is allowed to submit at most one vote. We ensure this by application specific local state of the registered accounts. 
Note that we use (consensus) rounds, instead of block, timestamps to specify the registration and voting period in this example.

The voting app can be deployed by running:
``` bash
goal app create --creator $ACC_[A|B|C] --approval-prog /data/build/voting_approval.teal --clear-prog /data/build/voting_clear_state.teal --global-byteslices 0 --global-ints 6 --local-byteslices 1 --local-ints 0 --app-arg "int:<REG_BGN>" --app-arg "int:<REG_END>" --app-arg "int:<VOTE_BGN>" --app-arg "int:<VOTE_END>"
```
The application arguments are used to pass in the begin and end rounds of the registration and voting periods. You can obtain the current consensus round of the sandbox
node by running:
``` bash
goal node lastround
```
In order to register (opt in), run:
``` bash
goal app optin --app-id <APP_ID> --from $ACC_[A|B|C]
```
After the start of the voting period, registered accounts can vote "yes" or "no" using:
``` bash
goal app call --from $ACC_[A|B|C] --app_id <APP_ID> --app-arg "str:[yes|no]"
```
Voters can retract their vote by either submitting a close out or clear state call:
``` bash
goal app clear --app-id <APP_ACC> --from $ACC_[A|B|C]
```

### Withdraw

The withdraw example is intended to demonstrate the process of sending Algos to and from a smart contract. The example app holds the address of a specific account that is 
allowed to withdraw all Algos sent to the app account after a specified point in time. The account is also allowed to delete the app, which transfers the current balance of the app account
 to the account. Everyone is allowed to send Algos to the app. Note that the process of sending Algos to the app is not implemented as part of the smart 
contract logic, but is a primitive provided by Algorand.

Deploy the app by running:
``` bash
goal app create --creator $ACC_[A|B|C] --approval-prog /data/build/withdraw_approval.teal --clear-prog /data/build/withdraw_clear_state.teal --global-byteslices 1 --global-ints 1 --local-byteslices 0 --local-ints 0 --app-arg "int:<UNIX_TIME>" --app-account $ACC_[A|B|C]
```
Note that we use the app accounts array (--app-account option) to pass the withdraw account to the app. Take a look at the documentation [here](https://developer.algorand.org/docs/get-details/dapps/smart-contracts/apps/) for more details on this. The app argument is the withdraw time (unix time). 
Accounts can send Algos to the app using goal. In order to submit payment transaction, we first need to lookup the address of the app. This can be done using:
``` bash
goal app info --app-id <APP_ID>
```
This outputs the application account together with some other information. Copy the address to a environment variable, e.g.:

``` bash
APP_ACC=XIBF2HUZXFM6NONRNMIZTN2NFJTXL35ECO5DR25S73RGVH6KUJX67GLTOU
```
Now we can send Algos from one of the sandbox accounts:

``` bash
goal clerk send --amount 1000000 --from $ACC_[A|B|C] --to $APP_ACC
```
The withdraw account can call the app to withdraw the current balance of the app (after the withdraw time): 
``` bash
goal app call --app-id <APP_ID> --from <WITHDRAW_ACC> --app-arg "int:<AMOUNT>"
```
The app argument is used to specify the amount of Algos that should be withdrawn.
It is also possible to withdraw the remaining balance and delete the app:
``` bash
goal app delete --app-id <APP_ID> --from <WITHDRAW_ACC>
```
                         
