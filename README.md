# Dark Web Data Logging on Hyperledger Fabric

This PoC scrapes onion websites over Tor, hashes the data, and stores it on a permissioned blockchain using Hyperledger Fabric.

## Structure

- `scraper/`: Python script that uses Tor to scrape .onion data.
- `backend/chaincode/`: Go smart contract to store hashed data.
- `backend/rest-api/`: Node.js service to submit data to Fabric.
- `docker-compose.yaml`: Orchestrates Tor, scraper, and Fabric API.
- `scripts/setup.sh`: Dependency installation.

## How to Run

1. Run setup: `bash scripts/setup.sh`
2. Start containers: `docker-compose up --build`
3. Chaincode and Fabric network should be configured separately or added here.

For educational use only.
