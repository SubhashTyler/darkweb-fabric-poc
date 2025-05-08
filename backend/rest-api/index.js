const { Gateway, Wallets } = require('fabric-network');
const fs = require('fs');

(async () => {
  const ccp = JSON.parse(fs.readFileSync('connection-org1.json'));
  const wallet = await Wallets.newFileSystemWallet('./wallet');
  const gateway = new Gateway();

  await gateway.connect(ccp, {
    wallet,
    identity: 'appUser',
    discovery: { enabled: true, asLocalhost: true }
  });

  const network = await gateway.getNetwork('mychannel');
  const contract = network.getContract('darkweb');

  const data = JSON.parse(fs.readFileSync('../../scraper/scraped.json'));
  await contract.submitTransaction('LogData', data.id, data.hash, data.source, data.timestamp);
  console.log("Logged to Fabric.");
})();
