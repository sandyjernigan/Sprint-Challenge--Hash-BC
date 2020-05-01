## Interview Questions

Explain in detail the workings of a dynamic array:
* What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back? 

> Arrays typically have a linear time complexity. Functions such as adding/removing from the front of an arry would have an O(n) time complexity, since it has to shift all of the numbers over. Whereas, adding/removing from the end of the array would return an O(1). 

> Other more complex functions using arrays can quickly rack into the quadratic time complexity in order to complete. 

* What is the worse case scenario if you try to extend the storage size of a dynamic array?

> If you try to extend the storage size of a dynamic array, the worst case scenario is there will not be enough room. Therefore, python will move the array to another section with more room. But this increases the run time as it has to iternate over everything to move it.

Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?

> Block chain is a set of blocks of encoded data that can be shared across a network of computers. 

> Each block is a record, but even if you have very similar things (or transactions) the block is encoded (hashed) in such a way that it is unique. 

> The chain is the reference that each block is linked together, each block contains the previous blocks hash.

> Block chains can be stored in simple databases or in the form of files. We have been storing these using a class object.
  
Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?

> Proof of work functions by requring the user to prove that they have a vlaid block. The proof in the block must provide the correct hash. 

> This protects the chain, by preventing any change to an excisting block. If you try to change an old block, it will be rejected if the information does not provide the correct hash. Even if you can fool it into thinking it is correct, there will be other newer blocks. Each block is linked, so that it is nearly impossible to fool all of the blocks into accepting that the edited block is valid. Either the proof will fail or the hash will not match. 

> If the attacker manages to get 51% of the chain, or have the longest-chain, then it is possible the attacker can trick the system into believeing it is the correct chain. The entity with 51% or greater control of the "mining power" will win the right to add the next block. Therefore the entity could attempt to add in fake blocks if they have enough "mining power" to override the others. As long as no 1 individual or group has more than 50% control, then the chain is safe.