blockchain = []

def getLastTransaction():
    if len(blockchain) < 1:
        return None

    return blockchain[-1]

def setNewItem(value, last = [1]):
    if last == None:
        last = [1]
    blockchain.append([last, value])

def askForTransaction():
    return float(input("Insira um novo valor: "))

def getUserInput(label = 'selecione um valor'):
    return input(label)

def showBlockchainList():
    print('=' * 20)
    for block in blockchain:
        print(block)
    print('=' * 20)

def verify_chain():
    is_valid = True
    for block_index in range(len(blockchain)):
        if(block_index == 0):
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else: 
            is_valid = False
            break
    return is_valid


while True:

    print('*' * 50)
    print("* please make a choice               *")
    print("* press 1 to insert a new input      *")
    print("* press 2 to show the blockchainlist *")
    print("* press q to quit                    *")
    print('*' * 50)
    userInput = getUserInput('Selecione uma opcao: ')
    if userInput == '1':
        setNewItem(askForTransaction(), getLastTransaction())
    elif userInput == '2':
        showBlockchainList()
    elif userInput == 'q':
        break
    elif userInput == 'h':
        if(len(blockchain) >- 1):
            blockchain[0] = 2
    else:
        print('Press a valid key')
    if not verify_chain():
        print('chain is invalid')
        break
        
print('loop done') 
