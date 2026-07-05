# Custom Signal Shuffler & Deshuffler

This simple project is a communication channel simulator. It demonstrates how to intercept, shuffle, and restore (*deshuffle*) structured text signals using dynamic data structures (Stacks and Linked Lists), without relying on the language's built-in abstractions.

The system utilizes the concept of **deterministic pseudo-random generation** (seed/key-based), ensuring that the signal can only be decrypted if the receiver possesses the exact same credential as the transmitter.

---

## Concepts & Data Structures

To demonstrate low-level concepts and manual memory management, the project avoids built-in Python methods like `.append()`, `.pop()`, or standard dynamic lists for the core logic. Instead, the following components were built from scratch:

* **Dynamic Nodes (`Node`):** The foundational structure for data storage and pointer references (`next`).
* **Custom Stack (`Message/Stack`):** Used by the channel to push the masked signal, following the LIFO (*Last In, First Out*) principle.
* **Linked List (`LinkedList`):** Used by the receiver to reconstruct and sort characters back into their original indices through manual pointer manipulation.
* **Symmetric Deterministic Cipher:** Shuffling is strictly tied to the numerical key (`seed`). An incorrect key creates a secondary layer of chaos (an unsuccessful shuffle), protecting the message's integrity.

---

## System Architecture

The project is decoupled into modules with well-defined responsibilities:

1. **`Content`**: Manages loading the original signal, from a text file.
2. **`Channel (Shuffler)`**: Intercepts the original string, applies a deterministic pseudo-random permutation based on the sender's key, and generates the transmission Stack.
3. **`Receiver (Deshuffler)`**: Consumes the encrypted stack. Using symmetric keys (the same *seed*), it reconstructs the indexed structure via a Dynamic Linked List, restoring the original message.
4. **`Main`**: Orchestrates the Command Line Interface (CLI), exception handling, and visual validation.

---

## How to use

1. Navigate to the project directory
2. Run the main script:
```bash
  python main.py
```
3. Choose the seed value
