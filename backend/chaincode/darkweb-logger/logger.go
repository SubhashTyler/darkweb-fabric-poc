package main

import (
    "fmt"
    "github.com/hyperledger/fabric-contract-api-go/contractapi"
)

type SmartContract struct {
    contractapi.Contract
}

func (s *SmartContract) LogData(ctx contractapi.TransactionContextInterface, id, hash, source, timestamp string) error {
    record := fmt.Sprintf(`{"hash":"%s","source":"%s","timestamp":"%s"}`, hash, source, timestamp)
    return ctx.GetStub().PutState(id, []byte(record))
}

func main() {
    cc, _ := contractapi.NewChaincode(new(SmartContract))
    cc.Start()
}
