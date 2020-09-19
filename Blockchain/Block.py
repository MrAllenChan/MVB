import json

from Blockchain.Transaction import Transaction


class Block:
    def __init__(self, tx=None, prev=None, nonce=None, powerOfWork=None, jsonObj=None):
        # if jsonObj:
        #     self.__createWithJsonObj(jsonObj)
        #     return
        self.tx: Transaction = tx  # <a single transaction>
        self.prev = prev  # <hash of the previous block>
        self.nonce = nonce  # <the nonce value, used for proof-of-work>
        self.pow = powerOfWork  # <the proof-of-work, a hash of the tx, prev, and nonce fields>

    def getJsonObj(self):
        jsonObj = {"tx": self.tx.getJsonObj(), "prev": str(self.prev), "nonce": str(self.nonce), "pow": str(self.pow)}
        return jsonObj

    def toString(self):
        itemList = [self.tx.toString(), str(self.prev), str(self.nonce), str(self.pow)]
        return ''.join(itemList)

    # def __createWithJsonObj(self, blockJsonObj: dict):
    #     self.tx = Transaction(jsonObj=blockJsonObj['tx'])
    #     self.prev = blockJsonObj['prev']
    #     self.pow = blockJsonObj['pow']
    #     self.nonce = blockJsonObj['nonce']


class BlockTreeNode:
    def __init__(self, prevBlockTreeNode, nowBlock: Block, blockHeight: int):
        self.prevBlockTreeNode = prevBlockTreeNode
        self.nowBlock = nowBlock
        self.blockHeight = blockHeight
