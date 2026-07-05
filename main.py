"""
This code receives, shuffle and reconstruct a phrase 
using lists, nodes, pointers and stacks fundamentals.
"""

from node import Node
from content import Content
import random

class Message:
    def __init__(self):
        self.top = None
        self._size = 0
        self._content = None

    def push(self, elem):
        node = Node(elem)               # Create node
        node.next = self.top            # Created node points to top
        self.top = node                 # Top node becames the created node
        self._size = self._size + 1
        data = self.top.data            # Created node is stored in data variable
        
    
    def pop(self):
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.data
        raise IndexError("The stack is empty!")

    # Length of stack
    def __len__(self):
        return self._size
    
    # Shows stack content
    def __repr__(self):
        r=""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data)
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()
    

class Channel:
    def shuffle(self, file, seed):
        random.seed(seed)
        file_list = list(range(len(file)))
        random.shuffle(file_list)
        shuffle_result = Message()
        for index in file_list:
            letter = file[index]
            shuffle_result.push(letter)
        return shuffle_result

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
    
    # Length of list
    def __len__(self):
        return self._size
    
    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")
        return pointer
    
    def insert(self, index, elem):
        node = self._getnode(index)
        node.data = elem

    def insert_head(self, elem):
        node = Node(elem)
        node.next = self.head
        self.head = node
        self._size += 1


class Receiver:
    def deshuffle(self, shuffled_list, signal_size, seed):
        random.seed(seed)
        file_list = list(range(signal_size))
        random.shuffle(file_list)
        final_list = LinkedList()
        for _ in range(signal_size):
            final_list.insert_head('')
    
        letter_position = (len(file_list) - 1)
        while len(shuffled_list) > 0:
            letter = shuffled_list.pop()
            original_index = file_list[letter_position]
            final_list.insert(original_index, letter)
            letter_position -= 1
        final_text = ''
        pointer = final_list.head
        while pointer:
            final_text += str(pointer.data)
            pointer = pointer.next
        return final_text
        
if __name__ == '__main__':

    signal_content = Content()

    user_key = input('Choose a numerical key or press Enter to use the standard key: ')
    if not user_key.strip():
        access_key = signal_content._key
    else:
        try:
            access_key = int(user_key)
        except ValueError:
            print('ERROR! Key must be numerical! Using standard key.')
            access_key = signal_content._key

    channel = Channel()
    stacked_signal = channel.shuffle(signal_content.data, access_key)

    
    original_signal = signal_content.data
    print(f'Shuffled signal: {stacked_signal}\n')

    user_rec_key = (input('Type the numerical key: '))
    if not user_rec_key.strip():
        receiver_access_key = signal_content._key
    else:
        try:
            receiver_access_key = int(user_rec_key)
        except ValueError:
            print('ERROR! Invalid key! It must be numerical! Using standard key.')
            receiver_access_key = signal_content._key

    receiver = Receiver()
    restored_signal = receiver.deshuffle(stacked_signal, len(signal_content.data), receiver_access_key)
    
    print(f'Restored signal: {restored_signal}')

    if restored_signal == signal_content.data and user_key == user_rec_key and user_key.isdigit():
        print("The key was CORRECT!")
    else:
        print("INCORRECT or INVALID key!")
    #print(f'\n\nOriginal signal: {original_signal}\n')

