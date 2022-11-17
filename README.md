# Algorand/PyTEAL Starter Repo for HackaTUM Participants

## Setup
Setup venv
```bash
python -m venv venv
```
Activate venv
```bash
source venv/bin/activate
```
Install requirements
```bash
pip install -r requirements.txt
```
### Setup Sandbox
Get sandbox repo (run this outside of this directory)
```bash
git clone https://github.com/algorand/sandbox.git
```
Now we need to make the content of this repo available to the sanbox docker container.
To do so, we need to add a volume to the docker-compose.yml located at the root of the sanbox repo.
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
## Deploy to Sanbox 
No we will take a look at how to deploy transactions to the sanbox net. 
Run all of these commands in the root of the sanbox repository.
First you need to start the algorand sanbox net: 
```bash
./sanbox up -v
```
This can take some time, add the -v (verbose) flag to see what is going on.
After the sanbox has been started successfully, enter algod in the docker container:

``` bash
./sanbox enter algod
```
Algod is  a client allowing you to talk to a Algorand node.

